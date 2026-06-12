#!/usr/bin/env python3
"""Read-only source drift watcher for the Vibe Coding Bible.

The watcher fetches a curated list of official source URLs, normalizes the
fetched content, compares compact signatures to a committed baseline, and emits
a Markdown report for human review. Fetched pages are treated only as untrusted
data to hash and summarize; the script never follows instructions embedded in
external content.
"""
from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import textwrap
import urllib.error
import urllib.parse
import urllib.request
from html.parser import HTMLParser
from pathlib import Path
from typing import Any

USER_AGENT = "VCBSourceDriftWatcher/1.0 (+https://github.com/frnklfrwsr/vibe-coding-bible)"
ISSUE_TITLE = "Daily VCB source drift report"
MAX_FETCH_BYTES = 2_000_000
SOURCE_ID_RE = re.compile(r"^[a-z0-9][a-z0-9_.-]*$")
REPORTABLE_STATUSES = {"changed", "fetch_failed", "missing_from_baseline", "missing_from_watchlist"}


class ConfigError(Exception):
    """Raised when local configuration is invalid."""


class VisibleTextParser(HTMLParser):
    """Extract visible-ish text and title while ignoring script/style blocks."""

    ignored_tags = {"script", "style", "noscript", "svg", "canvas"}
    spacing_tags = {
        "address",
        "article",
        "aside",
        "blockquote",
        "br",
        "dd",
        "div",
        "dl",
        "dt",
        "figcaption",
        "footer",
        "h1",
        "h2",
        "h3",
        "h4",
        "h5",
        "h6",
        "header",
        "hr",
        "li",
        "main",
        "nav",
        "ol",
        "p",
        "pre",
        "section",
        "table",
        "td",
        "th",
        "tr",
        "ul",
    }

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self._ignored_depth = 0
        self._in_title = False
        self._title_parts: list[str] = []
        self._text_parts: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        tag = tag.lower()
        if tag in self.ignored_tags:
            self._ignored_depth += 1
            return
        if tag == "title":
            self._in_title = True
            return
        if tag in self.spacing_tags and self._ignored_depth == 0:
            self._text_parts.append(" ")

    def handle_endtag(self, tag: str) -> None:
        tag = tag.lower()
        if tag in self.ignored_tags and self._ignored_depth:
            self._ignored_depth -= 1
            return
        if tag == "title":
            self._in_title = False
            return
        if tag in self.spacing_tags and self._ignored_depth == 0:
            self._text_parts.append(" ")

    def handle_data(self, data: str) -> None:
        if self._ignored_depth:
            return
        if self._in_title:
            self._title_parts.append(data)
            return
        self._text_parts.append(data)

    @property
    def title(self) -> str:
        return collapse_whitespace(" ".join(self._title_parts))

    @property
    def text(self) -> str:
        return collapse_whitespace(" ".join(self._text_parts))


def utc_now() -> str:
    return dt.datetime.now(dt.UTC).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def collapse_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", html.unescape(value)).strip()


def normalize_content(raw: bytes, content_type: str | None) -> tuple[str, str]:
    charset = "utf-8"
    if content_type:
        match = re.search(r"charset=([A-Za-z0-9_.-]+)", content_type, flags=re.I)
        if match:
            charset = match.group(1)
    try:
        text = raw.decode(charset, errors="replace")
    except LookupError:
        text = raw.decode("utf-8", errors="replace")

    parser = VisibleTextParser()
    try:
        parser.feed(text)
        parser.close()
        normalized = parser.text or collapse_whitespace(text)
        title = parser.title
    except Exception:
        normalized = collapse_whitespace(text)
        title = ""
    return title, normalized


def stable_json(data: Any) -> str:
    return json.dumps(data, sort_keys=True, separators=(",", ":"), ensure_ascii=False)


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(block)
    return digest.hexdigest()


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError as exc:
        raise ConfigError(f"Missing required file: {path}") from exc
    except json.JSONDecodeError as exc:
        raise ConfigError(f"Invalid JSON in {path}: {exc}") from exc


def write_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, indent=2, sort_keys=False, ensure_ascii=False) + "\n", encoding="utf-8")


def load_watchlist(path: Path) -> list[dict[str, Any]]:
    doc = load_json(path)
    if not isinstance(doc, dict):
        raise ConfigError("Watchlist must be a JSON object.")
    sources = doc.get("sources")
    if not isinstance(sources, list) or not sources:
        raise ConfigError("Watchlist must contain a non-empty sources array.")

    required = {"source_id", "url", "category", "evidence_level", "volatility", "owner_area", "notes"}
    seen: set[str] = set()
    entries: list[dict[str, Any]] = []
    for index, entry in enumerate(sources, start=1):
        if not isinstance(entry, dict):
            raise ConfigError(f"Watchlist entry {index} must be an object.")
        missing = sorted(required - set(entry))
        if missing:
            raise ConfigError(f"Watchlist entry {index} missing required fields: {missing}")
        source_id = str(entry["source_id"])
        if not SOURCE_ID_RE.match(source_id):
            raise ConfigError(f"Invalid source_id {source_id!r}; use lowercase IDs with dots, dashes, or underscores.")
        if source_id in seen:
            raise ConfigError(f"Duplicate source_id in watchlist: {source_id}")
        seen.add(source_id)

        parsed = urllib.parse.urlparse(str(entry["url"]))
        if parsed.scheme != "https" or not parsed.netloc:
            raise ConfigError(f"Watchlist URL for {source_id} must be an absolute https URL.")
        normalized_entry = {key: str(entry[key]) for key in required}
        entries.append(normalized_entry)
    return entries


def load_baseline(path: Path) -> dict[str, Any]:
    doc = load_json(path)
    if not isinstance(doc, dict):
        raise ConfigError("Baseline must be a JSON object.")
    sources = doc.get("sources")
    if not isinstance(sources, dict):
        raise ConfigError("Baseline must contain a sources object keyed by source_id.")
    return doc


def fetch_signature(entry: dict[str, Any], timeout: float) -> dict[str, Any]:
    source_id = entry["source_id"]
    url = entry["url"]
    fetched_at = utc_now()
    request = urllib.request.Request(
        url,
        headers={
            "User-Agent": USER_AGENT,
            "Accept": "text/html,application/xhtml+xml,text/plain,*/*;q=0.5",
            "Accept-Encoding": "identity",
        },
        method="GET",
    )

    base: dict[str, Any] = {
        "source_id": source_id,
        "url": url,
        "category": entry["category"],
        "evidence_level": entry["evidence_level"],
        "volatility": entry["volatility"],
        "owner_area": entry["owner_area"],
        "notes": entry["notes"],
        "fetched_at": fetched_at,
    }
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            raw = response.read(MAX_FETCH_BYTES + 1)
            truncated = len(raw) > MAX_FETCH_BYTES
            if truncated:
                raw = raw[:MAX_FETCH_BYTES]
            content_type = response.headers.get("Content-Type", "")
            title, normalized = normalize_content(raw, content_type)
            normalized_hash = hashlib.sha256(normalized.encode("utf-8")).hexdigest()
            return {
                **base,
                "fetch_status": "ok",
                "http_status": int(response.status),
                "final_url": response.geturl(),
                "content_type": content_type,
                "raw_bytes_length": len(raw),
                "normalized_length": len(normalized),
                "normalized_sha256": normalized_hash,
                "title": title,
                "truncated": truncated,
                "error": "",
            }
    except urllib.error.HTTPError as exc:
        return {
            **base,
            "fetch_status": "failed",
            "http_status": int(exc.code),
            "final_url": getattr(exc, "url", url),
            "content_type": "",
            "raw_bytes_length": 0,
            "normalized_length": 0,
            "normalized_sha256": "",
            "title": "",
            "truncated": False,
            "error": f"HTTP {exc.code}: {short_error(exc.reason)}",
        }
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        return {
            **base,
            "fetch_status": "failed",
            "http_status": None,
            "final_url": url,
            "content_type": "",
            "raw_bytes_length": 0,
            "normalized_length": 0,
            "normalized_sha256": "",
            "title": "",
            "truncated": False,
            "error": short_error(exc),
        }


def short_error(exc: Any) -> str:
    return collapse_whitespace(str(exc))[:240]


def build_baseline(watchlist_path: Path, entries: list[dict[str, Any]], signatures: dict[str, dict[str, Any]]) -> dict[str, Any]:
    return {
        "schema_version": 1,
        "generated_at": utc_now(),
        "user_agent": USER_AGENT,
        "normalization": {
            "summary": "HTML script/style/noscript/svg/canvas blocks ignored where feasible; whitespace collapsed before SHA-256.",
            "max_fetch_bytes": MAX_FETCH_BYTES,
        },
        "watchlist_sha256": file_sha256(watchlist_path),
        "source_count": len(entries),
        "sources": {entry["source_id"]: signatures[entry["source_id"]] for entry in entries},
    }


def compare_signatures(
    entries: list[dict[str, Any]],
    current: dict[str, dict[str, Any]],
    baseline: dict[str, Any],
) -> list[dict[str, Any]]:
    baseline_sources = baseline.get("sources", {})
    results: list[dict[str, Any]] = []

    for entry in entries:
        source_id = entry["source_id"]
        current_sig = current[source_id]
        baseline_sig = baseline_sources.get(source_id)
        if current_sig.get("fetch_status") != "ok":
            status = "fetch_failed"
        elif not baseline_sig or not baseline_sig.get("normalized_sha256"):
            status = "missing_from_baseline"
        elif current_sig.get("normalized_sha256") == baseline_sig.get("normalized_sha256"):
            status = "unchanged"
        else:
            status = "changed"
        results.append(
            {
                "source_id": source_id,
                "status": status,
                "entry": entry,
                "current": current_sig,
                "baseline": baseline_sig,
            }
        )

    watchlist_ids = {entry["source_id"] for entry in entries}
    for source_id in sorted(set(baseline_sources) - watchlist_ids):
        baseline_sig = baseline_sources[source_id]
        results.append(
            {
                "source_id": source_id,
                "status": "missing_from_watchlist",
                "entry": None,
                "current": None,
                "baseline": baseline_sig,
            }
        )
    return results


def status_counts(results: list[dict[str, Any]]) -> dict[str, int]:
    counts = {status: 0 for status in ["unchanged", "changed", "fetch_failed", "missing_from_baseline", "missing_from_watchlist"]}
    for result in results:
        counts[result["status"]] = counts.get(result["status"], 0) + 1
    return counts


def has_reportable_findings(results: list[dict[str, Any]]) -> bool:
    return any(result["status"] in REPORTABLE_STATUSES for result in results)


def md(value: Any, limit: int = 120) -> str:
    text = collapse_whitespace(str(value or ""))
    if len(text) > limit:
        text = textwrap.shorten(text, width=limit, placeholder="...")
    return text.replace("|", "\\|") or "-"


def short_hash(value: Any) -> str:
    text = str(value or "")
    return text[:12] if text else "-"


def render_report(
    mode: str,
    watchlist_path: Path,
    baseline_path: Path,
    entries: list[dict[str, Any]],
    results: list[dict[str, Any]] | None,
    signatures: dict[str, dict[str, Any]],
    github_note: str | None = None,
) -> str:
    generated_at = utc_now()
    lines = [
        "# Daily VCB Source Drift Report",
        "",
        f"Generated: `{generated_at}`",
        f"Mode: `{mode}`",
        f"Watchlist: `{watchlist_path.as_posix()}`",
        f"Baseline: `{baseline_path.as_posix()}`",
        f"Watchlist source count: `{len(entries)}`",
        "",
        "Fetched external pages are treated as untrusted data. This watcher hashes normalized source text and reports metadata only; it does not follow page instructions, modify VCB content, run Codex/OpenAI automation, or create pull requests.",
        "",
    ]

    if results is None:
        ok_count = sum(1 for signature in signatures.values() if signature.get("fetch_status") == "ok")
        failed = [signature for signature in signatures.values() if signature.get("fetch_status") != "ok"]
        lines.extend(
            [
                "## Baseline Update",
                "",
                f"Baseline signatures written for `{len(signatures)}` source(s).",
                f"Successful fetches: `{ok_count}`.",
                f"Fetch failures recorded: `{len(failed)}`.",
                "",
            ]
        )
        if failed:
            lines.extend(["| Source | URL | Error |", "|---|---|---|"])
            for signature in failed:
                lines.append(f"| `{md(signature.get('source_id'))}` | {md(signature.get('url'))} | {md(signature.get('error'))} |")
            lines.append("")
        return "\n".join(lines).rstrip() + "\n"

    counts = status_counts(results)
    reportable_count = sum(counts.get(status, 0) for status in REPORTABLE_STATUSES)
    lines.extend(
        [
            "## Status Summary",
            "",
            "| Status | Count |",
            "|---|---:|",
        ]
    )
    for status in ["unchanged", "changed", "fetch_failed", "missing_from_baseline", "missing_from_watchlist"]:
        lines.append(f"| `{status}` | {counts.get(status, 0)} |")
    lines.extend(["", f"Reportable finding count: `{reportable_count}`.", ""])

    if reportable_count == 0:
        lines.extend(["## Findings", "", "No source drift or fetch failures were detected against the committed baseline.", ""])
    else:
        lines.extend(
            [
                "## Findings",
                "",
                "| Source | Status | Category | Owner area | Volatility | Why it may matter |",
                "|---|---|---|---|---|---|",
            ]
        )
        for result in results:
            if result["status"] not in REPORTABLE_STATUSES:
                continue
            entry = result.get("entry") or {}
            baseline_sig = result.get("baseline") or {}
            source_id = result["source_id"]
            lines.append(
                "| "
                f"`{md(source_id)}` | "
                f"`{result['status']}` | "
                f"{md(entry.get('category') or baseline_sig.get('category'))} | "
                f"{md(entry.get('owner_area') or baseline_sig.get('owner_area'))} | "
                f"{md(entry.get('volatility') or baseline_sig.get('volatility'))} | "
                f"{md(entry.get('notes') or baseline_sig.get('notes'), limit=180)} |"
            )
        lines.append("")

        lines.extend(["## Source Details", ""])
        for result in results:
            if result["status"] not in REPORTABLE_STATUSES:
                continue
            current_sig = result.get("current") or {}
            baseline_sig = result.get("baseline") or {}
            entry = result.get("entry") or baseline_sig or {}
            lines.extend(
                [
                    f"### `{result['source_id']}`",
                    "",
                    f"- Status: `{result['status']}`",
                    f"- URL: {md(entry.get('url') or baseline_sig.get('url'))}",
                    f"- Category: `{md(entry.get('category') or baseline_sig.get('category'))}`",
                    f"- Evidence level: `{md(entry.get('evidence_level') or baseline_sig.get('evidence_level'))}`",
                    f"- Owner area: `{md(entry.get('owner_area') or baseline_sig.get('owner_area'))}`",
                    f"- Notes: {md(entry.get('notes') or baseline_sig.get('notes'), limit=220)}",
                ]
            )
            if current_sig:
                lines.extend(
                    [
                        f"- Current title: {md(current_sig.get('title'))}",
                        f"- Current normalized length: `{current_sig.get('normalized_length', '-')}`",
                        f"- Current normalized SHA-256: `{short_hash(current_sig.get('normalized_sha256'))}`",
                    ]
                )
                if current_sig.get("fetch_status") != "ok":
                    lines.append(f"- Fetch error: {md(current_sig.get('error'), limit=220)}")
            if baseline_sig:
                lines.extend(
                    [
                        f"- Baseline title: {md(baseline_sig.get('title'))}",
                        f"- Baseline normalized length: `{baseline_sig.get('normalized_length', '-')}`",
                        f"- Baseline normalized SHA-256: `{short_hash(baseline_sig.get('normalized_sha256'))}`",
                    ]
                )
            lines.append("")

    if github_note:
        lines.extend(["## GitHub Reporting", "", github_note, ""])
    return "\n".join(lines).rstrip() + "\n"


def github_request(method: str, path: str, token: str, payload: dict[str, Any] | None = None) -> Any:
    api_url = os.environ.get("GITHUB_API_URL", "https://api.github.com").rstrip("/")
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    request = urllib.request.Request(
        f"{api_url}{path}",
        data=body,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "Content-Type": "application/json",
            "User-Agent": USER_AGENT,
            "X-GitHub-Api-Version": "2022-11-28",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            raw = response.read()
            if not raw:
                return None
            return json.loads(raw.decode("utf-8"))
    except urllib.error.HTTPError as exc:
        detail = exc.read().decode("utf-8", errors="replace")[:500]
        raise ConfigError(f"GitHub API request failed: HTTP {exc.code} {detail}") from exc
    except (urllib.error.URLError, TimeoutError, OSError) as exc:
        raise ConfigError(f"GitHub API request failed: {short_error(exc)}") from exc


def publish_github_report(report: str) -> str:
    token = os.environ.get("GITHUB_TOKEN")
    repo = os.environ.get("GITHUB_REPOSITORY")
    if not token:
        raise ConfigError("GITHUB_TOKEN is required to create or update the drift report issue.")
    if not repo or "/" not in repo:
        raise ConfigError("GITHUB_REPOSITORY must be set to owner/name.")

    encoded_title = urllib.parse.quote(ISSUE_TITLE)
    issues = github_request("GET", f"/repos/{repo}/issues?state=open&per_page=100", token)
    if not isinstance(issues, list):
        raise ConfigError("Unexpected GitHub issues API response.")

    matches = [
        issue
        for issue in issues
        if issue.get("title") == ISSUE_TITLE and "pull_request" not in issue and isinstance(issue.get("number"), int)
    ]
    if matches:
        issue = sorted(matches, key=lambda item: item["number"])[0]
        github_request("POST", f"/repos/{repo}/issues/{issue['number']}/comments", token, {"body": report})
        return f"Added a new comment to existing drift report issue `#{issue['number']}`."

    created = github_request(
        "POST",
        f"/repos/{repo}/issues",
        token,
        {
            "title": ISSUE_TITLE,
            "body": report,
        },
    )
    if not isinstance(created, dict) or "number" not in created:
        raise ConfigError("Unexpected GitHub issue creation response.")
    return f"Created drift report issue `#{created['number']}`."


def parse_args(argv: list[str]) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Check official VCB sources for signature drift.")
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--update-baseline", action="store_true", help="Fetch sources and write a new baseline file.")
    mode.add_argument("--check", action="store_true", help="Fetch sources and compare to the committed baseline.")
    parser.add_argument("--no-github", action="store_true", help="Disable GitHub issue creation/commenting.")
    parser.add_argument("--watchlist", type=Path, default=Path("watchlists/source-drift-watchlist.json"))
    parser.add_argument("--baseline", type=Path, default=Path("watchlists/source-drift-baseline.json"))
    parser.add_argument("--report-output", type=Path, help="Optional path to write the Markdown report.")
    parser.add_argument("--timeout", type=float, default=20.0, help="Per-source fetch timeout in seconds.")
    return parser.parse_args(argv)


def main(argv: list[str]) -> int:
    args = parse_args(argv)
    if args.timeout <= 0:
        raise ConfigError("--timeout must be greater than zero.")

    entries = load_watchlist(args.watchlist)
    signatures = {entry["source_id"]: fetch_signature(entry, args.timeout) for entry in entries}
    github_note: str | None = None
    exit_code = 0

    if args.update_baseline:
        baseline_doc = build_baseline(args.watchlist, entries, signatures)
        write_json(args.baseline, baseline_doc)
        report = render_report("update-baseline", args.watchlist, args.baseline, entries, None, signatures)
    else:
        baseline_doc = load_baseline(args.baseline)
        results = compare_signatures(entries, signatures, baseline_doc)
        reportable = has_reportable_findings(results)
        if reportable and not args.no_github:
            try:
                github_note = publish_github_report(render_report("check", args.watchlist, args.baseline, entries, results, signatures))
            except ConfigError as exc:
                github_note = f"GitHub issue reporting failed: `{md(exc, limit=300)}`"
                exit_code = 2
        elif reportable and args.no_github:
            github_note = "GitHub reporting skipped because `--no-github` was supplied."
        else:
            github_note = "No drift was detected, so no GitHub issue update was needed."
        report = render_report("check", args.watchlist, args.baseline, entries, results, signatures, github_note)

    if args.report_output:
        args.report_output.parent.mkdir(parents=True, exist_ok=True)
        args.report_output.write_text(report, encoding="utf-8")
    print(report, end="")
    return exit_code


if __name__ == "__main__":
    try:
        raise SystemExit(main(sys.argv[1:]))
    except ConfigError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(2)
