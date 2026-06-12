#!/usr/bin/env python3
"""Lightweight VCB repository-contract validator.

Checks:
- JSON parse and schema compile
- manifest inventory
- active chapter/topic frontmatter instance validation
- required Markdown headings
- VCB topic and section marker pairing
- active/planned namespace drift in indexes
- active index routes pointing to authored active IDs
- shortcut profile/index resolution
- shortcut-register table row shape and declared-table placement
- evidence source ID resolution
- tool-register resolution for indexes and active chunk report
- active chunk report source-ID resolution across registered source prefixes
- browser/Chrome tool namespace consistency
- llms.txt / llms-full.txt begin-marker and visible active-heading freshness
- source_status.official_openai consistency against Evidence and Sources
- source-register Chunk 13 table placement and row shape
- Chunk 14 Codex feature-card coverage and routing
- Chunk 15 workflow/prompting card coverage and routing
- Markdown VCB begin-marker versions match frontmatter versions
- README and manifest next-chunk route agreement
- duplicate Codex feature full-list sections in indexes
- duplicate workflow/prompting full-list sections in indexes
- Chunk 14 and Chunk 15 report validation claims are backed by validator checks
- Chunk 15 workflow/prompting card coverage, routing, and scope guardrails
- feature-flag source metadata consistency
- visible index status text and duplicate historical chunk sections
- Chapter 33 blueprint playbook coverage
- pricing snapshot routing/status consistency
- source_status.official_vendor consistency against Evidence and Sources
- pricing-snapshot route/status/source-register consistency
- source_status.official_vendor consistency with Evidence and Sources
- terminal report marker for the active chunk report
- root governance metadata drift across README, manifest, and chunk report
- index terminal STOP_RETRIEVAL / END_INDEX signposts
- cross-artifact VCB begin/end marker pairing
- SOURCE_REGISTER source rows stay inside declared table sections
- Chunk 17 frontend/refactor/dependency workflow card coverage and routing
- manifest redirect-map consistency
- Chunk 17 task-index atomic route replacement checks
- Chunk 18 failure-mode topic-card coverage and routing
- Chunk 18 per-index failure-mode routing coverage
- Chunk 18 task-index atomic failure-mode route checks
- Chunk 18 full-list failure-mode section completeness
- stale planned failure-mode route replacement checks
- semantic failure-mode index section routing checks
- duplicate active failure-mode rows inside a single index section
- repeated source-map active-status phrase checks
- Chunk 19 constraint/budget topic-card coverage and routing
- Chunk 19 exact pricing/limits stable-prose guardrail
- Chunk 19 report claim coverage
- no live Markdown content after VCB end markers except report terminal status lines
- nested manifest source_artifacts.source_files inventory consistency
- active chunk report file-inventory coverage
- Chunk 20 shortcut harm-reduction topic-card coverage and routing
- Chunk 20 shortcut-register active status and scope guardrails
- SHORTCUT_REGISTER shortcut rows stay inside declared table sections
- Chunk 21 security/permission shortcut topic-card coverage and routing
- Chunk 21 semantic task/failure/coach shortcut route coverage
- Chunk 21 root validation metadata, generic LLM shortcut routing, and semantic shortcut/risk route checks
- Chunk 22 setup/process shortcut topic-card coverage and routing
- Chunk 22 semantic setup/process task/failure/coach/risk/shortcut route coverage
- Chunk 22 duplicate full-list section, repeated source-map status, related-topic, changelog-heading, and routing-claim truthfulness checks
- Chunk 23 tool-sprawl/skill/reusable-process shortcut coverage, semantic routes, active-ID redirect hygiene, source-map hygiene, and scope guardrails
- Chunk 24 multi-AI/model-bias shortcut governance, status metadata, LLM active-content, package-count, semantic route, and planned-alias replacement checks
- Chunk 25 parallel/cloud/automation shortcut coverage, semantic routes, source-map hygiene, README next-scope hygiene, and scope guardrails
- Chunk 26 repository-contract cleanup for glossary bias routes and shortcut alias/deprecation routing
- Chunk 27 first-party OpenAI/Codex primary tool-card coverage, routing, source posture, and scope guardrails
- Chunk 28 first-party OpenAI/Codex adjunct surface tool-card coverage, routing, source posture, and scope guardrails
- Chunk 29 first-party OpenAI/Codex customization/control tool-card coverage, routing, source posture, and scope guardrails
- Chunk 30 first-party OpenAI/Codex Security tool-card coverage, routing, source posture, and scope guardrails
- Chunk 31 first-party OpenAI/Codex governance/maintenance tool-card coverage, routing, source posture, nested manifest inventory, README routing, source-refresh truthfulness, and scope guardrails
- Chunk 32 repository/CI/dependency/QA tool-card coverage, routing, official vendor source posture, and scope guardrails
- Chunk 34 browser-dev/app-builder/UI-generation tool-card coverage, routing, official vendor source posture, and scope guardrails
- Chunk 35 hosting/backend/auth/payment/observability/product-analytics tool-card coverage, routing, official vendor source posture, and scope guardrails
- Chunk 36 Docker/container, Figma/design, and Linear/project-management tool-card coverage, routing, official vendor source posture, and scope guardrails
- Chunk 40 tool-catalog coverage-gap audit, ecosystem expansion, deferred/planned register coverage, routing, source posture, and scope guardrails
- Chunk 41 finalization-readiness audit, register count agreement, finalization gap list, LLM route cleanup, and scope guardrails
- Chunk 42 release-candidate scope/disposition cleanup, no-premature-RC claims, changelog convention, register count agreement, and scope guardrails
- Chunk 43 release-candidate packaging, RC status, package aliases, documented limitations, register counts, integrity reporting, stale non-RC wording, and packaging-only scope guardrails
- Chunk 44 final-release packaging, final-release status, package aliases, documented limitations, register counts, integrity reporting, and no-substantive-content scope guardrails"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter
from pathlib import Path
from typing import Any

try:
    import yaml
    import jsonschema
except Exception as exc:  # pragma: no cover
    print(f"Missing dependency: {exc}", file=sys.stderr)
    sys.exit(2)

ROOT = Path(__file__).resolve().parents[1]
BACKTICK_ID_RE = re.compile(r"`([A-Za-z][A-Za-z0-9_]*(?:\.[A-Za-z0-9_.-]+)+)`")
VCB_INDEX_ID_RE = re.compile(r"`((?:vcb|tool)\.[A-Za-z0-9_.-]+)`")
IGNORED_INVENTORY_PARTS = {".git", "__pycache__"}

FINAL_RELEASE_1_HISTORICAL_INVENTORY_SHA256 = "f60357a9381e09cd8292e68260f346068fb3f559530c201e02594a53d28e64a4"
FINAL_RELEASE_1_HISTORICAL_CONTENT_SHA256 = "445869cfcf787dd2cbab04e2d55ab912d1253ae436f667d010fcfc66d65092ae"
FINAL_RELEASE_1_HISTORICAL_SOURCE_FILE_COUNT = "333"

REQUIRED_TOPIC_HEADINGS = [
    "## 1. For the Human: Plain-Language Concept",
    "## 2. For the AI Coach: How to Teach This to Your Human",
    "## Shortcut Reality",
    "## Budget and Constraint Notes",
    "## Stable Core",
    "## Volatile Surface",
    "## Obsolescence Watch",
    "## Evidence and Sources",
    "## Related Topics",
]


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def rel_path(path: Path) -> str:
    """Return a stable repository-relative path for manifest comparisons."""
    return path.relative_to(ROOT).as_posix()


def is_inventory_file(path: Path) -> bool:
    """True when a filesystem path should be part of the repository inventory."""
    if not path.is_file():
        return False
    rel_parts = path.relative_to(ROOT).parts
    if any(part in IGNORED_INVENTORY_PARTS for part in rel_parts):
        return False
    return path.suffix != ".pyc"


def actual_source_paths() -> list[str]:
    return sorted(rel_path(path) for path in ROOT.rglob("*") if is_inventory_file(path))


def parse_frontmatter(path: Path) -> dict[str, Any] | None:
    """Parse repository YAML frontmatter without treating body rules as metadata.

    Topic/chapter/report files may put a VCB begin marker on the first line
    and YAML frontmatter immediately after it. Root, index, and register files
    put YAML frontmatter at byte 0. Other `---` lines are normal Markdown
    separators and must not be parsed as frontmatter.
    """
    text = read(path)
    candidate = text
    first_line, sep, remainder = text.partition("\n")
    if sep and re.match(r"^<!--\s*VCB:BEGIN_[^>]*-->$", first_line):
        candidate = remainder
    match = re.match(r"^---\n(.*?)\n---\n", candidate, flags=re.S)
    if not match:
        return None
    data = yaml.safe_load(match.group(1)) or {}
    return data if isinstance(data, dict) else None





def chunk_number_from(value: str) -> int | None:
    match = re.search(r"chunk_(\d+)", value or "")
    return int(match.group(1)) if match else None


def validate_root_governance(manifest: dict[str, Any], errors: list[str]) -> tuple[str, Path]:
    current_chunk = manifest.get("chunk_gate", {}).get("current_chunk", "")
    current_num = chunk_number_from(current_chunk)
    active_chunk_id = str(manifest.get("active_chunk", {}).get("id", ""))
    if current_num is None:
        errors.append(f"manifest.chunk_gate.current_chunk is not a chunk_N value: {current_chunk!r}")
        current_num = 0

    readme_path = ROOT / "README.md"
    readme_fm = parse_frontmatter(readme_path) or {}
    readme_status = str(readme_fm.get("status", ""))
    if f"chunk_{current_num}" not in readme_status:
        errors.append(
            "README.md frontmatter status does not match current chunk: "
            f"status={readme_status!r}, expected chunk_{current_num}"
        )

    readme_text = read(readme_path)
    body_match = re.search(r"\*\*Chunk ID:\*\* `([^`]+)`", readme_text)
    if not body_match:
        errors.append("README.md body missing **Chunk ID:** line")
    else:
        body_chunk_id = body_match.group(1)
        valid_body_ids = {current_chunk, active_chunk_id} - {""}
        if not any(v in body_chunk_id or body_chunk_id in v for v in valid_body_ids):
            errors.append(
                "README.md body current chunk does not match manifest: "
                f"body={body_chunk_id!r}, allowed={sorted(valid_body_ids)}"
            )

    approval = str(manifest.get("editor_gate", {}).get("approval_applied", ""))
    expected_prior = current_num - 1
    if expected_prior >= 0:
        if f"Chunk {expected_prior} approved" not in approval or f"Chunk {current_num} authored" not in approval:
            errors.append(
                "manifest.editor_gate.approval_applied does not match current chunk transition: "
                f"{approval!r}; expected Chunk {expected_prior} approved and Chunk {current_num} authored"
            )

    report = ROOT / f"CHUNK_{current_num}_REPORT.md"
    if report.exists():
        report_fm = parse_frontmatter(report) or {}
        report_chunk_id = str(report_fm.get("chunk_id", ""))
        valid_report_ids = {current_chunk, active_chunk_id} - {""}
        if not any(v in report_chunk_id or report_chunk_id in v for v in valid_report_ids):
            errors.append(
                f"CHUNK_{current_num}_REPORT.md chunk_id does not match manifest current chunk: "
                f"report={report_chunk_id!r}, allowed={sorted(valid_report_ids)}"
            )
    return current_chunk, report




def expected_canonical_package(manifest: dict[str, Any]) -> str:
    return str(manifest.get("canonical_review_package", ""))


def manifest_source_paths(manifest: dict[str, Any]) -> list[str]:
    return sorted(item["path"] if isinstance(item, dict) else item for item in manifest.get("source_files", []))


def validate_nested_manifest_inventory(manifest: dict[str, Any], actual: list[str], listed: list[str], errors: list[str]) -> None:
    source_artifacts = manifest.get("source_artifacts", {})
    if int(source_artifacts.get("total_files", -1)) != len(actual):
        errors.append(
            "manifest.source_artifacts.total_files does not match actual package files: "
            f"{source_artifacts.get('total_files')} != {len(actual)}"
        )
    all_tracked = sorted(source_artifacts.get("all_tracked_files", []))
    if all_tracked != listed or all_tracked != actual:
        errors.append(
            "manifest.source_artifacts.all_tracked_files does not match source_files and actual package files: "
            f"all_tracked={len(all_tracked)} source_files={len(listed)} actual={len(actual)}"
        )

    if "source_files" in source_artifacts:
        nested_source_files = sorted(source_artifacts.get("source_files", []))
        if nested_source_files != listed or nested_source_files != actual:
            errors.append(
                "manifest.source_artifacts.source_files does not match top-level manifest.source_files and actual package files: "
                f"nested={len(nested_source_files)} source_files={len(listed)} actual={len(actual)} "
                f"missing={sorted(set(listed) - set(nested_source_files))} extra={sorted(set(nested_source_files) - set(listed))}"
            )
        if source_artifacts.get("source_files_match_manifest") is True and nested_source_files != listed:
            errors.append(
                "manifest.source_artifacts.source_files_match_manifest is true but nested source_files is stale"
            )

    expected_buckets = {
        "report_files": sorted(p for p in actual if re.fullmatch(r"CHUNK_\d+_REPORT\.md", p)),
        "chapter_files": sorted(p for p in actual if p.startswith("chapters/") and p.endswith(".md") and not p.endswith(".gitkeep")),
        "topic_files": sorted(p for p in actual if p.startswith("topics/") and p.endswith(".md") and not p.endswith(".gitkeep")),
        "tool_catalog_files": sorted(p for p in actual if p.startswith("topics/tool-catalog/") and p.endswith(".md") and not p.endswith(".gitkeep")),
        "index_files": sorted(p for p in actual if p.startswith("indexes/") and p.endswith(".md")),
        "schema_files": sorted(p for p in actual if p.startswith("schemas/") and p.endswith(".schema.json")),
        "register_files": sorted(p for p in actual if p in {
            "CHANGELOG.md",
            "DEPRECATION_REGISTER.md",
            "FIELD_PRACTICES.md",
            "PRICING_SNAPSHOT_REGISTER.md",
            "SHORTCUT_REGISTER.md",
            "SOURCE_REGISTER.md",
            "TOOL_REGISTER.md",
        }),
        "protocol_files": sorted(p for p in actual if p in {
            "AUTHORING_PROTOCOL.md",
            "EDITORIAL_PROTOCOL.md",
            "UPDATE_PROTOCOL.md",
        }),
    }
    for key, expected in expected_buckets.items():
        observed = sorted(source_artifacts.get(key, []))
        if observed != expected:
            errors.append(
                f"manifest.source_artifacts.{key} mismatch: "
                f"expected={expected} observed={observed}"
            )
        count_key = f"{key}_count"
        if count_key in source_artifacts and int(source_artifacts.get(count_key, -1)) != len(expected):
            errors.append(
                f"manifest.source_artifacts.{count_key} does not match derived {key} length: "
                f"{source_artifacts.get(count_key)!r} != {len(expected)}"
            )


def validate_manifest_package_counts(manifest: dict[str, Any], actual: list[str], listed: list[str], errors: list[str]) -> None:
    """Reject stale package-count metadata after a chunk adds files."""
    expected = len(actual)
    package = manifest.get("package", {}) if isinstance(manifest.get("package"), dict) else {}
    package_count_keys = (
        "total_files",
        "file_count",
        "source_file_count",
        "source_files_count",
        "actual_package_inventory_count",
        "all_tracked_file_count",
        "manifest_source_file_count",
    )
    for key in package_count_keys:
        if key in package and int(package.get(key, -1)) != expected:
            errors.append(f"manifest.package.{key} does not match actual package inventory: {package.get(key)!r} != {expected}")
        if key in package and int(package.get(key, -1)) != len(listed):
            errors.append(
                f"manifest.package.{key} does not match manifest.source_files length: "
                f"{package.get(key)!r} != {len(listed)}"
            )

    for key in ("source_file_count", "source_files_count", "actual_package_inventory_count"):
        if key in manifest and int(manifest.get(key, -1)) != expected:
            errors.append(
                f"manifest.{key} does not match actual package inventory: "
                f"{manifest.get(key)!r} != {expected}"
            )
        if key in manifest and int(manifest.get(key, -1)) != len(listed):
            errors.append(
                f"manifest.{key} does not match manifest.source_files length: "
                f"{manifest.get(key)!r} != {len(listed)}"
            )

    source_artifacts = manifest.get("source_artifacts", {}) if isinstance(manifest.get("source_artifacts"), dict) else {}
    artifact_count_keys = (
        "total_files",
        "actual_package_inventory_count",
        "source_file_count",
        "source_files_count",
        "all_tracked_files_count",
        "all_tracked_file_count",
        "manifest_source_file_count",
        "file_count",
    )
    for key in artifact_count_keys:
        if key in source_artifacts and int(source_artifacts.get(key, -1)) != expected:
            errors.append(f"manifest.source_artifacts.{key} does not match actual package inventory: {source_artifacts.get(key)!r} != {expected}")

    artifact_hygiene = manifest.get("artifact_hygiene", {}) if isinstance(manifest.get("artifact_hygiene"), dict) else {}
    for key in ("actual_package_inventory_count", "source_file_count", "source_files_count"):
        if key in artifact_hygiene and int(artifact_hygiene.get(key, -1)) != expected:
            errors.append(f"manifest.artifact_hygiene.{key} does not match actual package inventory: {artifact_hygiene.get(key)!r} != {expected}")

    if len(listed) != expected:
        errors.append(f"manifest.source_files length does not match actual package inventory: {len(listed)} != {expected}")


def validate_current_chunk_status_metadata(manifest: dict[str, Any], errors: list[str]) -> None:
    """Version-bumped governance/routing artifacts must not keep prior-chunk status labels."""
    current_chunk = str(manifest.get("chunk_gate", {}).get("current_chunk", ""))
    current_num = chunk_number_from(current_chunk)
    if current_num is None:
        return
    expected_status = f"chunk_{current_num}_updated"
    version_token = f"chunk{current_num}"

    manifest_status = str(manifest.get("status", ""))
    manifest_version = str(manifest.get("version", ""))
    if version_token in manifest_version and manifest_status != expected_status:
        errors.append(
            "manifest.status does not match current chunk version: "
            f"status={manifest_status!r}, expected={expected_status!r}"
        )

    routing_paths = [
        ROOT / "README.md",
        ROOT / "llms.txt",
        ROOT / "llms-full.txt",
        ROOT / "SOURCE_REGISTER.md",
        ROOT / "SHORTCUT_REGISTER.md",
        ROOT / "CHANGELOG.md",
    ] + sorted((ROOT / "indexes").glob("*.md"))
    for path in routing_paths:
        fm = parse_frontmatter(path) or {}
        version = str(fm.get("version", ""))
        status = str(fm.get("status", ""))
        if version_token in version and status != expected_status:
            errors.append(
                f"{path.relative_to(ROOT)} frontmatter status does not match current chunk version: "
                f"status={status!r}, expected={expected_status!r}"
            )


def validate_canonical_package_references(manifest: dict[str, Any], errors: list[str]) -> None:
    expected = expected_canonical_package(manifest)
    if not expected:
        errors.append("manifest.canonical_review_package is missing")
        return
    references = {
        "manifest.canonical_review_package": manifest.get("canonical_review_package"),
        "manifest.package.canonical_review_package": manifest.get("package", {}).get("canonical_review_package"),
        "manifest.artifact_hygiene.canonical_review_package": manifest.get("artifact_hygiene", {}).get("canonical_review_package"),
        "manifest.source_artifacts.canonical_review_package": manifest.get("source_artifacts", {}).get("canonical_review_package"),
    }
    source_artifacts = manifest.get("source_artifacts", {}) if isinstance(manifest.get("source_artifacts"), dict) else {}
    for package_alias in ("package_file", "review_package"):
        if package_alias in source_artifacts:
            references[f"manifest.source_artifacts.{package_alias}"] = source_artifacts.get(package_alias)
    if isinstance(manifest.get("active_chunk"), dict) and "canonical_review_package" in manifest.get("active_chunk", {}):
        references["manifest.active_chunk.canonical_review_package"] = manifest["active_chunk"].get("canonical_review_package")
    current_chunk = str(manifest.get("chunk_gate", {}).get("current_chunk", ""))
    current_num = chunk_number_from(current_chunk)
    for label, value in references.items():
        if value != expected:
            errors.append(f"{label} is inconsistent: {value!r} != {expected!r}")
        if current_num is not None and isinstance(value, str):
            match = re.search(r"vibe-coding-bible-chunk-(\d+)", value)
            if match and int(match.group(1)) != current_num:
                errors.append(
                    f"{label} points to prior/future chunk package instead of current Chunk {current_num}: {value!r}"
                )


def declared_field_practice_statuses() -> set[str]:
    text = read(ROOT / "FIELD_PRACTICES.md")
    if "## Status Labels" not in text or "## Promotion Rules" not in text:
        return set()
    block = text.split("## Status Labels", 1)[1].split("## Promotion Rules", 1)[0]
    statuses: set[str] = set()
    for line in block.splitlines():
        m = re.match(r"\|\s*([a-z_]+)\s*\|", line.strip())
        if m and m.group(1) not in {"Status", "---"}:
            statuses.add(m.group(1))
    return statuses


def validate_field_practice_register(errors: list[str]) -> None:
    text = read(ROOT / "FIELD_PRACTICES.md")
    statuses = declared_field_practice_statuses()
    if not statuses:
        errors.append("FIELD_PRACTICES.md status labels could not be parsed")
        return
    if "## Candidate Field Practice Routing Table" not in text or "## Field-Practice Evaluation Prompt" not in text:
        errors.append("FIELD_PRACTICES.md missing expected table boundaries")
        return
    block = text.split("## Candidate Field Practice Routing Table", 1)[1].split("## Field-Practice Evaluation Prompt", 1)[0]
    header: list[str] | None = None
    for line in block.splitlines():
        s = line.strip()
        if not s.startswith("|") or set(s.replace("|", "").strip()) <= {"-", ":"}:
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if header is None:
            header = cells
            if "Current register status" not in header:
                errors.append("FIELD_PRACTICES.md table missing Current register status column")
            continue
        if len(cells) != len(header):
            errors.append(f"FIELD_PRACTICES.md table row shape mismatch: expected {len(header)} cells, got {len(cells)} in {line}")
            continue
        status = cells[header.index("Current register status")]
        if "/" in status:
            errors.append(f"FIELD_PRACTICES.md has slash-combined status value: {status!r}")
        if status not in statuses:
            errors.append(f"FIELD_PRACTICES.md status {status!r} is not declared in Status Labels {sorted(statuses)}")


def active_topic_files() -> list[Path]:
    files = [p for p in (ROOT / "chapters").glob("*.md")]
    files.extend(p for p in (ROOT / "topics").glob("*/*.md"))
    return sorted(p for p in files if p.name != ".gitkeep")


def schema_paths_for(frontmatter: dict[str, Any]) -> list[Path]:
    base = ROOT / "schemas" / "topic.schema.json"
    if frontmatter.get("type") == "chapter":
        return [base, ROOT / "schemas" / "chapter.schema.json"]
    if frontmatter.get("type") == "shortcut":
        return [base, ROOT / "schemas" / "shortcut.schema.json"]
    if frontmatter.get("type") == "tool_card":
        return [base, ROOT / "schemas" / "tool.schema.json"]
    if frontmatter.get("type") == "field_practice":
        return [base, ROOT / "schemas" / "field-practice.schema.json"]
    return [base]


def local_overlay_schema(schema: dict[str, Any]) -> dict[str, Any]:
    return {k: v for k, v in schema.items() if k not in {"$id", "$schema", "allOf"}}


def resolve_schema(schema_path: Path, seen: set[Path] | None = None) -> dict[str, Any]:
    seen = seen or set()
    schema_path = schema_path.resolve()
    schema = json.loads(read(schema_path))
    if schema_path in seen:
        return schema
    seen.add(schema_path)

    def resolve_node(node: Any) -> Any:
        if isinstance(node, dict):
            if "$ref" in node:
                ref = node["$ref"]
                ref_path = (schema_path.parent / ref).resolve() if not ref.startswith("http") else ROOT / "schemas" / ref.rsplit("/", 1)[-1]
                replacement = resolve_schema(ref_path, seen.copy())
                merged = {k: v for k, v in node.items() if k != "$ref"}
                if merged:
                    base = dict(replacement)
                    base.update(merged)
                    return resolve_node(base)
                return resolve_node(replacement)
            return {k: resolve_node(v) for k, v in node.items()}
        if isinstance(node, list):
            return [resolve_node(v) for v in node]
        return node

    return resolve_node(schema)


def id_root(identifier: str) -> str:
    parts = identifier.split(".")
    if identifier.startswith("vcb.") and len(parts) >= 2:
        return ".".join(parts[:2])
    if identifier.startswith("tool."):
        return "tool"
    return parts[0]


def authored_active_ids() -> set[str]:
    ids: set[str] = set()
    for path in active_topic_files():
        fm = parse_frontmatter(path) or {}
        if fm.get("id"):
            ids.add(str(fm["id"]))
    return ids


def shortcut_register_ids() -> set[str]:
    text = read(ROOT / "SHORTCUT_REGISTER.md")
    ids: set[str] = set()
    for line in text.splitlines():
        if line.strip().startswith("| `vcb.shortcut."):
            ids.update(re.findall(r"`(vcb\.shortcut\.[A-Za-z0-9_.-]+)`", line))
    return ids


def source_register_ids() -> set[str]:
    text = read(ROOT / "SOURCE_REGISTER.md")
    ids: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"\| `([^`]+)` \|", line.strip())
        if match:
            ids.add(match.group(1))
    return ids


def tool_register_ids() -> set[str]:
    text = read(ROOT / "TOOL_REGISTER.md")
    ids: set[str] = set()
    for line in text.splitlines():
        match = re.match(r"\| `(tool\.[^`]+)` \|", line.strip())
        if match:
            ids.add(match.group(1))
    return ids


def report_source_ids(path: Path) -> set[str]:
    """All source-like dotted IDs in the active report must resolve to SOURCE_REGISTER.

    This is intentionally prefix-agnostic for source families, but excludes
    obvious file names and code symbols such as `llms.txt`, `package.json`,
    and `process.env`.
    """
    ids = set(BACKTICK_ID_RE.findall(read(path))) if path.exists() else set()
    ignored_first_segments = {"process", "package", "tsconfig", "README", "SOURCE_REGISTER", "CHUNK_13_REPORT", "llms"}
    ignored_suffixes = (".md", ".txt", ".json", ".yaml", ".yml", ".toml")
    out: set[str] = set()
    for sid in ids:
        if sid.startswith(("vcb.", "tool.")):
            continue
        if sid.endswith(ignored_suffixes):
            continue
        first = sid.split(".", 1)[0]
        if first in ignored_first_segments:
            continue
        out.add(sid)
    return out


def report_tool_ids(path: Path) -> set[str]:
    return set(re.findall(r"`(tool\.[A-Za-z0-9_.-]+)`", read(path))) if path.exists() else set()


def index_tool_ids() -> set[str]:
    ids: set[str] = set()
    for path in (ROOT / "indexes").glob("*.md"):
        ids.update(re.findall(r"`(tool\.[A-Za-z0-9_.-]+)`", read(path)))
    return ids


def duplicate_register_ids(path: Path) -> set[str]:
    seen: set[str] = set()
    dupes: set[str] = set()
    for line in read(path).splitlines():
        match = re.match(r"\| `([^`]+)` \|", line.strip())
        if not match:
            continue
        ident = match.group(1)
        if ident in seen:
            dupes.add(ident)
        seen.add(ident)
    return dupes


def validate_index_status_and_chunk_headings(manifest: dict[str, Any], errors: list[str]) -> None:
    current_num = chunk_number_from(manifest.get("chunk_gate", {}).get("current_chunk", ""))
    neutral = "> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes."
    for path in sorted((ROOT / "indexes").glob("*.md")):
        text = read(path)
        status_lines = re.findall(r"^> Status: .*$", text, flags=re.M)
        if not status_lines:
            errors.append(f"index missing visible status line: {path.relative_to(ROOT)}")
        for line in status_lines:
            if line == neutral:
                continue
            if current_num is not None and f"Status: Chunk {current_num} routing index" in line:
                continue
            errors.append(
                f"index visible status line is stale or noncanonical in {path.relative_to(ROOT)}: {line!r}"
            )
        chunk_headings = re.findall(r"^#{2,6}\s+Chunk\s+\d+.*$", text, flags=re.M | re.I)
        if chunk_headings:
            errors.append(
                f"historical chunk heading(s) remain in primary index {path.relative_to(ROOT)}: {chunk_headings}"
            )


def validate_chapter_33_playbooks(errors: list[str]) -> None:
    path = ROOT / "chapters" / "33-codex-playbooks.md"
    text = read(path)
    required = [
        "### Playbook: new project bootstrap",
        "### Playbook: unknown repo tour",
        "### Playbook: small feature slice",
        "### Playbook: reproducible bug fix",
        "### Playbook: add tests",
        "### Playbook: refactor safely",
        "### Playbook: frontend from screenshot",
        "### Playbook: review local diff",
        "### Playbook: PR review",
        "### Playbook: generate release notes",
        "### Playbook: CI failure triage",
        "### Playbook: investigate production error",
        "### Playbook: add API endpoint",
        "### Playbook: migrate dependency",
        "### Playbook: remove dead code",
        "### Playbook: improve docs",
        "### Playbook: build MVP prototype",
        "### Playbook: harden auth-sensitive code",
        "### Playbook: create a skill",
        "### Playbook: create an automation",
    ]
    missing = [label for label in required if label not in text]
    if missing:
        errors.append(f"Chapter 33 missing required blueprint playbook headings: {missing}")

    task_index = read(ROOT / "indexes" / "INDEX_BY_TASK.md")
    prompt_library = read(ROOT / "indexes" / "PROMPT_LIBRARY.md")
    if "## Bootstrap a new project" not in task_index or "new project bootstrap playbook" not in task_index:
        errors.append("INDEX_BY_TASK missing new-project-bootstrap route")
    if "## New project bootstrap prompt" not in prompt_library or "Bootstrap a new project/repo" not in prompt_library:
        errors.append("PROMPT_LIBRARY missing new-project-bootstrap prompt")



def duplicate_source_urls() -> dict[str, list[str]]:
    """Return official/source URL duplicates in SOURCE_REGISTER, excluding intentionally duplicated blank/placeholder URLs."""
    url_to_ids: dict[str, list[str]] = {}
    for line in read(ROOT / "SOURCE_REGISTER.md").splitlines():
        match = re.match(r"\| `([^`]+)` \| [^|]+ \| ([^|]+) \|", line.strip())
        if not match:
            continue
        sid, url = match.group(1), match.group(2).strip().strip("`")
        if not url or url.lower() in {"tbd", "n/a", "deferred"}:
            continue
        if not url.startswith(("http://", "https://")):
            continue
        url_to_ids.setdefault(url, []).append(sid)
    return {url: ids for url, ids in url_to_ids.items() if len(ids) > 1}


def validate_pricing_snapshots(errors: list[str]) -> None:
    schema_path = ROOT / "schemas" / "pricing-snapshot.schema.json"
    schema = resolve_schema(schema_path)
    for path in sorted((ROOT / "pricing-snapshots").glob("*.md")):
        if path.name == ".gitkeep":
            continue
        fm = parse_frontmatter(path)
        if fm is None:
            errors.append(f"pricing snapshot missing frontmatter: {path.relative_to(ROOT)}")
            continue
        fm_for_validation = {k: (v.isoformat() if hasattr(v, "isoformat") else v) for k, v in fm.items()}
        jsonschema.Draft202012Validator(schema).validate(fm_for_validation)


def validate_pricing_snapshot_routes(manifest: dict[str, Any], errors: list[str]) -> None:
    routes = manifest.get("pricing_snapshot_ids", {})
    if not isinstance(routes, dict):
        errors.append("manifest.pricing_snapshot_ids must be a mapping")
        return
    active = set(manifest.get("active_pricing_snapshot_ids", []))
    planned = set(manifest.get("planned_pricing_snapshot_ids", []))
    if active & planned:
        errors.append(f"pricing snapshots listed as both active and planned: {sorted(active & planned)}")

    for policy_key in ("topic_namespace_policy", "namespace_policy"):
        policy = manifest.get(policy_key, {})
        policy_active = set(policy.get("active_pricing_snapshot_ids", []))
        policy_planned = set(policy.get("planned_pricing_snapshot_ids", []))
        if policy_active != active:
            errors.append(f"{policy_key}.active_pricing_snapshot_ids does not match manifest active list")
        if policy_planned != planned:
            errors.append(f"{policy_key}.planned_pricing_snapshot_ids does not match manifest planned list")
        if policy_active & policy_planned:
            errors.append(f"{policy_key} lists pricing snapshots as both active and planned: {sorted(policy_active & policy_planned)}")

    for ident in active:
        route = routes.get(ident)
        if not isinstance(route, str) or not route or route.upper() == "DEFERRED":
            errors.append(f"active pricing snapshot {ident} has no concrete file path")
            continue
        if not (ROOT / route).exists():
            errors.append(f"active pricing snapshot route does not exist: {ident} -> {route}")
    for ident in planned:
        route = routes.get(ident)
        if route is None:
            errors.append(f"planned pricing snapshot {ident} missing from manifest.pricing_snapshot_ids")
        elif isinstance(route, str) and route.upper() not in {"DEFERRED", "DEFERRED_SNAPSHOT"} and (ROOT / route).exists():
            errors.append(f"planned pricing snapshot {ident} points to an existing file instead of deferred status: {route}")
        elif isinstance(route, str) and route.upper() not in {"DEFERRED", "DEFERRED_SNAPSHOT"} and not (ROOT / route).exists():
            errors.append(f"planned pricing snapshot {ident} uses stale/nonexistent path instead of explicit DEFERRED: {route}")

    stability = read(ROOT / "indexes" / "INDEX_BY_STABILITY.md")
    statuses: dict[str, set[str]] = {}
    for line in stability.splitlines():
        for ident in re.findall(r"`(vcb\.pricing_snapshot\.[A-Za-z0-9_.-]+)`", line):
            m = re.search(r"→\s*([A-Za-z0-9_/-]+)", line)
            statuses.setdefault(ident, set()).add(m.group(1) if m else "unknown")
    for ident, vals in statuses.items():
        if len(vals) != 1:
            errors.append(f"INDEX_BY_STABILITY has conflicting statuses for {ident}: {sorted(vals)}")
    for ident in active:
        if statuses.get(ident) != {"active_snapshot"}:
            errors.append(f"active pricing snapshot {ident} must route as active_snapshot in INDEX_BY_STABILITY; observed {statuses.get(ident)}")

    source_text = read(ROOT / "SOURCE_REGISTER.md")
    openai_active = "vcb.pricing_snapshot.openai_codex" in active
    for line in source_text.splitlines():
        if line.startswith("| `openai.codex.pricing` "):
            if openai_active and "deferred" in line.lower():
                errors.append("openai.codex.pricing row still says pricing snapshot is deferred while OpenAI snapshot is active")
            if openai_active and "vcb.pricing_snapshot.openai_codex" not in line:
                errors.append("openai.codex.pricing row does not point to active vcb.pricing_snapshot.openai_codex")


NON_OPENAI_VENDOR_SOURCE_PREFIXES = (
    "github.",
    "git.",
    "owasp.",
    "w3c.",
    "mdn.",
    "npm.",
    "playwright.",
    "aws.",
    "openssf.",
    "vercel.",
    "supabase.",
    "stripe.",
    "clerk.",
    "auth0.",
    "sentry.",
    "posthog.",
    "react.",
    "typescript.",
    "eslint.",
    "liquibase.",
    "flyway.",
    "vite.",
    "webpack.",
    "opentelemetry.",
    "prisma.",
    "postgres.",
    "jest.",
    "nodejs.",
    "openfeature.",
    "anthropic.",
    "cursor.",
    "windsurf.",
    "replit.",
    "lovable.",
    "bolt.",
    "v0.",
    "docker.",
    "figma.",
    "linear.",
    "cloudflare.",
    "netlify.",
    "neon.",
    "resend.",
    "vitest.",
    "storybook.",
)



def validate_llms_source_maps(manifest: dict[str, Any], errors: list[str]) -> None:
    current_num = chunk_number_from(manifest.get("chunk_gate", {}).get("current_chunk", ""))
    expectations = [
        (ROOT / "llms.txt", "VCB:BEGIN_LLMS"),
        (ROOT / "llms-full.txt", "VCB:BEGIN_LLMS_FULL"),
    ]
    for path, marker in expectations:
        text = read(path)
        fm = parse_frontmatter(path) or {}
        version = str(fm.get("version", ""))
        match = re.search(rf"<!-- {marker} id=[^ ]+ version=([^ >]+) -->", text)
        if not match:
            errors.append(f"{path.name} missing {marker} begin marker")
            continue
        marker_version = match.group(1)
        if marker_version != version:
            errors.append(f"{path.name} begin marker version mismatch: marker={marker_version!r} frontmatter={version!r}")

        active_headings = re.findall(r"^## Active Chunk (\d+) content\s*$", text, flags=re.M)
        for num in active_headings:
            if current_num is not None and int(num) != current_num:
                errors.append(f"{path.name} has stale visible active-chunk heading: Active Chunk {num} content")

        current_active_match = re.search(r"(?ms)^## Current Active Content\s*\n(.*?)(?=^## |\Z)", text)
        if current_active_match:
            current_active_body = current_active_match.group(1)
            first_nonempty = next((line.strip() for line in current_active_body.splitlines() if line.strip()), "")
            expected_phrase = ""
            if current_num == 24:
                expected_phrase = f"Multi-AI/model-bias shortcut cards from Chunk {current_num} are active."
                if expected_phrase not in current_active_body:
                    errors.append(f"{path.name} Current Active Content does not name active Chunk 24 multi-AI/model-bias cards")
                if current_active_body.count(expected_phrase) != 1:
                    errors.append(f"{path.name} Current Active Content must contain exactly one Chunk 24 active-content phrase")
                if "Chunk 23" in first_nonempty:
                    errors.append(f"{path.name} Current Active Content opens with stale Chunk 23 status: {first_nonempty!r}")
            if current_num == 25:
                expected_phrase = "Parallel/cloud/automation shortcut cards from Chunk 25 are active."
                if expected_phrase not in current_active_body:
                    errors.append(f"{path.name} Current Active Content does not name active Chunk 25 parallel/cloud/automation cards")
                if current_active_body.count(expected_phrase) != 1:
                    errors.append(f"{path.name} Current Active Content must contain exactly one Chunk 25 active-content phrase")
                if "Chunk 24" in first_nonempty or "multi-AI" in first_nonempty:
                    errors.append(f"{path.name} Current Active Content opens with stale Chunk 24 status: {first_nonempty!r}")
        else:
            errors.append(f"{path.name} missing Current Active Content section")

    full_text = read(ROOT / "llms-full.txt")
    stale_full_headings = []
    for line in re.findall(r"^## Chunk (\d+) .*$", full_text, flags=re.M):
        if current_num is None or int(line) != current_num:
            stale_full_headings.append(line)
    if stale_full_headings:
        errors.append(f"llms-full.txt has stale chunk-specific routing headings: {stale_full_headings}")


def validate_source_status_official_openai(errors: list[str]) -> None:
    for path in active_topic_files():
        fm = parse_frontmatter(path) or {}
        source_status = fm.get("source_status", {}) if isinstance(fm.get("source_status"), dict) else {}
        declared = bool(source_status.get("official_openai", False))
        ids = evidence_ids(path)
        has_openai = any(sid.startswith("openai.") for sid in ids)
        if declared != has_openai:
            errors.append(
                "source_status.official_openai mismatch in "
                f"{path.relative_to(ROOT)}: declared={declared} evidence_has_openai={has_openai} ids={sorted(ids)}"
            )


def validate_source_register_chunk13_table(errors: list[str]) -> None:
    text = read(ROOT / "SOURCE_REGISTER.md")
    if "## Notes" not in text:
        errors.append("SOURCE_REGISTER.md missing ## Notes section")
        return
    before_notes, after_notes = text.split("## Notes", 1)
    for required in ("jest.docs_getting_started", "nodejs.docs_environment_variables", "openfeature.docs_intro"):
        row_pattern = rf"^\| `{re.escape(required)}` \|"
        if not re.search(row_pattern, before_notes, flags=re.M):
            errors.append(f"SOURCE_REGISTER Chunk 13 row for {required} is not inside the canonical source table")
    dangling = [line for line in after_notes.splitlines() if line.strip().startswith("| `")]
    if dangling:
        errors.append(f"SOURCE_REGISTER rows appear under ## Notes instead of a valid table: {dangling[:5]}")


def validate_feature_flag_metadata(errors: list[str]) -> None:
    path = ROOT / "topics" / "concepts" / "feature-flag.md"
    fm = parse_frontmatter(path) or {}
    ids = evidence_ids(path)
    if "openfeature.docs_intro" not in ids:
        errors.append("feature-flag concept does not cite openfeature.docs_intro")
    if "martin_fowler.feature_toggles" not in ids:
        errors.append("feature-flag concept does not cite martin_fowler.feature_toggles as supporting E3 source")
    if fm.get("evidence_level") != "E0_OFFICIAL_DOCS":
        errors.append(f"feature-flag evidence_level should be E0_OFFICIAL_DOCS when OpenFeature is the primary definition anchor; observed {fm.get('evidence_level')!r}")
    source_status = fm.get("source_status", {}) if isinstance(fm.get("source_status"), dict) else {}
    if source_status.get("official_vendor") is not True:
        errors.append("feature-flag source_status.official_vendor should be true when citing openfeature.docs_intro")

def validate_source_status_official_vendor(errors: list[str]) -> None:
    for path in active_topic_files():
        fm = parse_frontmatter(path) or {}
        source_status = fm.get("source_status", {}) if isinstance(fm.get("source_status"), dict) else {}
        declared = bool(source_status.get("official_vendor", False))
        ids = evidence_ids(path)
        has_vendor = any(sid.startswith(NON_OPENAI_VENDOR_SOURCE_PREFIXES) for sid in ids)
        if declared != has_vendor:
            errors.append(
                "source_status.official_vendor mismatch in "
                f"{path.relative_to(ROOT)}: declared={declared} evidence_has_non_openai_vendor={has_vendor} ids={sorted(ids)}"
            )


def evidence_ids(path: Path) -> set[str]:
    text = read(path)
    marker = "## Evidence and Sources"
    if marker not in text:
        return set()
    section = text.split(marker, 1)[1]
    next_heading = re.search(r"\n## ", section)
    if next_heading:
        section = section[: next_heading.start()]
    return set(BACKTICK_ID_RE.findall(section))


def validate_markdown_contract(path: Path, fm: dict[str, Any], errors: list[str]) -> None:
    text = read(path)
    rel = path.relative_to(ROOT)
    tid = str(fm.get("id", ""))
    for heading in REQUIRED_TOPIC_HEADINGS:
        if heading not in text:
            errors.append(f"missing required heading {heading!r} in {rel}")
    if f"<!-- VCB:BEGIN_TOPIC id={tid}" not in text:
        errors.append(f"missing BEGIN_TOPIC marker for {tid} in {rel}")
    if f"<!-- VCB:END_TOPIC id={tid}" not in text:
        errors.append(f"missing END_TOPIC marker for {tid} in {rel}")
    if "<!-- VCB:STOP_RETRIEVAL" not in text:
        errors.append(f"missing STOP_RETRIEVAL marker in {rel}")
    begins = re.findall(r"<!-- VCB:BEGIN_SECTION id=([^ >]+)", text)
    ends = re.findall(r"<!-- VCB:END_SECTION id=([^ >]+)", text)
    if sorted(begins) != sorted(ends):
        errors.append(f"section marker mismatch in {rel}: begins={begins} ends={ends}")
    for suffix in ("human", "ai_coach"):
        sid = f"{tid}.{suffix}"
        if sid not in begins or sid not in ends:
            errors.append(f"missing {suffix} section marker pair for {tid} in {rel}")


SHORTCUT_REGISTER_TABLE_HEADER = [
    "Shortcut ID",
    "Planned file",
    "Best-practice alternative",
    "Prototype risk",
    "Production risk",
    "Recoverability",
    "Minimum guardrail",
    "Status",
]


def markdown_table_cells(line: str) -> list[str]:
    return [cell.strip() for cell in line.strip().strip("|").split("|")]


def is_markdown_separator_row(line: str) -> bool:
    stripped = line.strip()
    if not stripped.startswith("|"):
        return False
    body = stripped.strip("|").strip()
    return bool(body) and set(body.replace("|", "").replace(" ", "")) <= {"-", ":"}


def table_shape_ok() -> bool:
    text = read(ROOT / "SHORTCUT_REGISTER.md")
    if "## Shortcut Routing Table" not in text or "## Shortcut Card Typing" not in text:
        print("SHORTCUT_REGISTER missing expected table boundaries")
        return False
    block = text.split("## Shortcut Routing Table", 1)[1].split("## Shortcut Card Typing", 1)[0]
    for line in block.splitlines():
        s = line.strip()
        if not s.startswith("|") or is_markdown_separator_row(s):
            continue
        cells = markdown_table_cells(s)
        if cells == SHORTCUT_REGISTER_TABLE_HEADER:
            continue
        if len(cells) != len(SHORTCUT_REGISTER_TABLE_HEADER):
            print(f"Bad shortcut table row shape ({len(cells)} cells): {line}")
            return False
    return True


def validate_shortcut_register_table_placement(errors: list[str]) -> None:
    """Ensure shortcut-register rows stay inside declared shortcut tables.

    A blank line terminates a Markdown table. Shortcut rows that resume after a
    blank line or prose must be introduced by a new heading and the standard
    shortcut-table header; regex ID resolution alone is not sufficient.
    """
    path = ROOT / "SHORTCUT_REGISTER.md"
    text = read(path)
    active_table = False
    pending_heading = False
    expecting_separator = False
    declared_tables = 0

    for lineno, line in enumerate(text.splitlines(), start=1):
        stripped = line.strip()

        if re.match(r"^##\s+", stripped):
            active_table = False
            pending_heading = True
            expecting_separator = False
            continue

        if not stripped:
            active_table = False
            # Preserve pending_heading so a heading may be followed by blank line(s) before the table header.
            continue

        if stripped.startswith("|"):
            cells = markdown_table_cells(stripped)
            if cells == SHORTCUT_REGISTER_TABLE_HEADER:
                if not pending_heading:
                    errors.append(f"SHORTCUT_REGISTER.md shortcut table header at line {lineno} is not introduced by a heading")
                active_table = True
                pending_heading = False
                expecting_separator = True
                declared_tables += 1
                continue

            if is_markdown_separator_row(stripped):
                if not active_table:
                    # Non-shortcut tables outside shortcut routing regions are harmless.
                    pending_heading = False
                    continue
                if len(cells) != len(SHORTCUT_REGISTER_TABLE_HEADER):
                    errors.append(f"SHORTCUT_REGISTER.md shortcut table separator has unexpected column count at line {lineno}: {len(cells)}")
                expecting_separator = False
                continue

            shortcut_row = bool(re.match(r"^\|\s*`vcb\.shortcut\.[^`]+`\s*\|", stripped))
            if shortcut_row:
                if not active_table:
                    ident = re.findall(r"`(vcb\.shortcut\.[^`]+)`", stripped)
                    errors.append(f"SHORTCUT_REGISTER.md shortcut row outside declared shortcut table at line {lineno}: {ident[0] if ident else stripped}")
                if len(cells) != len(SHORTCUT_REGISTER_TABLE_HEADER):
                    errors.append(f"SHORTCUT_REGISTER.md shortcut row has unexpected column count at line {lineno}: {len(cells)}")
                if expecting_separator:
                    errors.append(f"SHORTCUT_REGISTER.md shortcut table at line {lineno} is missing separator row after header")
                pending_heading = False
                continue

            if active_table:
                if len(cells) != len(SHORTCUT_REGISTER_TABLE_HEADER):
                    errors.append(f"SHORTCUT_REGISTER.md row inside shortcut table has unexpected column count at line {lineno}: {len(cells)}")
                if expecting_separator:
                    errors.append(f"SHORTCUT_REGISTER.md shortcut table at line {lineno} is missing separator row after header")
            pending_heading = False
            continue

        # Prose/code/list content terminates the possibility that a following table header belongs to the prior heading.
        active_table = False
        pending_heading = False
        expecting_separator = False

    if declared_tables == 0:
        errors.append("SHORTCUT_REGISTER.md has no declared shortcut routing table")



def validate_chunk_13_concept_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    current = manifest.get("chunk_gate", {}).get("current_chunk", "")
    if current != "chunk_13":
        return
    required_ids = {
        "vcb.concepts.api_basics": "topics/concepts/api-basics.md",
        "vcb.concepts.frontend_backend": "topics/concepts/frontend-backend.md",
        "vcb.concepts.database_schema": "topics/concepts/database-schema.md",
        "vcb.concepts.authentication": "topics/concepts/authentication.md",
        "vcb.concepts.authorization": "topics/concepts/authorization.md",
        "vcb.concepts.state": "topics/concepts/state.md",
        "vcb.concepts.async": "topics/concepts/async.md",
        "vcb.concepts.dependency": "topics/concepts/dependency.md",
        "vcb.concepts.test": "topics/concepts/test.md",
        "vcb.concepts.typecheck": "topics/concepts/typecheck.md",
        "vcb.concepts.lint": "topics/concepts/lint.md",
        "vcb.concepts.migration": "topics/concepts/migration.md",
        "vcb.concepts.environment_variable": "topics/concepts/environment-variable.md",
        "vcb.concepts.build_step": "topics/concepts/build-step.md",
        "vcb.concepts.ci": "topics/concepts/ci.md",
        "vcb.concepts.feature_flag": "topics/concepts/feature-flag.md",
        "vcb.concepts.observability": "topics/concepts/observability.md",
    }
    active = authored_active_ids()
    for ident, rel in required_ids.items():
        if ident not in active:
            errors.append(f"Chunk 13 required concept ID not authored: {ident}")
        if not (ROOT / rel).exists():
            errors.append(f"Chunk 13 required concept file missing: {rel}")
    concept_index = read(ROOT / "indexes" / "INDEX_BY_CONCEPT.md")
    task_index = read(ROOT / "indexes" / "INDEX_BY_TASK.md")
    for ident in required_ids:
        active_line = f"`{ident}` → active"
        if active_line not in concept_index and f"`{ident}` → active:" not in concept_index:
            errors.append(f"INDEX_BY_CONCEPT missing active route for Chunk 13 concept: {ident}")
        if ident not in task_index:
            errors.append(f"INDEX_BY_TASK missing route for Chunk 13 concept: {ident}")



def validate_chunk_14_codex_feature_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    current = manifest.get("chunk_gate", {}).get("current_chunk", "")
    if current != "chunk_14":
        return
    required_ids = {
        "vcb.codex.app": "topics/codex/app.md",
        "vcb.codex.cli": "topics/codex/cli.md",
        "vcb.codex.ide_extension": "topics/codex/ide-extension.md",
        "vcb.codex.cloud": "topics/codex/cloud.md",
        "vcb.codex.github_review": "topics/codex/github-review.md",
        "vcb.codex.config": "topics/codex/config.md",
        "vcb.codex.agents_md": "topics/codex/agents-md.md",
        "vcb.codex.skills": "topics/codex/skills.md",
        "vcb.codex.mcp": "topics/codex/mcp.md",
        "vcb.codex.hooks": "topics/codex/hooks.md",
        "vcb.codex.automations": "topics/codex/automations.md",
        "vcb.codex.subagents": "topics/codex/subagents.md",
        "vcb.codex.computer_use": "topics/codex/computer-use.md",
        "vcb.codex.feature_maturity": "topics/codex/feature-maturity.md",
        "vcb.codex.changelog_monitoring": "topics/codex/changelog-monitoring.md",
    }
    active = authored_active_ids()
    for ident, rel in required_ids.items():
        if ident not in active:
            errors.append(f"Chunk 14 required Codex feature ID not authored: {ident}")
        if not (ROOT / rel).exists():
            errors.append(f"Chunk 14 required Codex feature file missing: {rel}")
    index_files = [
        ROOT / "indexes" / "INDEX_BY_CODEX_SURFACE.md",
        ROOT / "indexes" / "INDEX_BY_CONCEPT.md",
        ROOT / "indexes" / "INDEX_BY_TASK.md",
        ROOT / "indexes" / "INDEX_FOR_AI_COACHES.md",
    ]
    combined = "\n".join(read(p) for p in index_files)
    llms = read(ROOT / "llms.txt")
    for ident in required_ids:
        if f"`{ident}` → active" not in combined and f"`{ident}` → active:" not in combined:
            errors.append(f"primary indexes missing active route for Chunk 14 Codex feature: {ident}")
        if ident not in llms:
            errors.append(f"llms.txt missing fast route for Chunk 14 Codex feature: {ident}")


CHUNK_15_WORKFLOW_PROMPTING_IDS = {
    "vcb.prompting.four_part_prompt": "topics/prompting/four-part-prompt.md",
    "vcb.prompting.acceptance_criteria": "topics/prompting/acceptance-criteria.md",
    "vcb.prompting.plan_first": "topics/prompting/plan-first.md",
    "vcb.prompting.context_management": "topics/prompting/context-management.md",
    "vcb.workflow.unknown_codebase": "topics/workflows/unknown-codebase.md",
    "vcb.workflow.feature_slicing": "topics/workflows/feature-slicing.md",
    "vcb.workflow.bug_repro": "topics/workflows/bug-repro.md",
    "vcb.workflow.testing": "topics/workflows/testing.md",
}


def validate_chunk_15_workflow_prompting_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    current = manifest.get("chunk_gate", {}).get("current_chunk", "")
    if current != "chunk_15":
        return
    active = authored_active_ids()
    manifest_required = set(manifest.get("chunk_15_required_topic_ids", []) or [])
    if manifest_required != set(CHUNK_15_WORKFLOW_PROMPTING_IDS):
        errors.append(
            "manifest.chunk_15_required_topic_ids mismatch: "
            f"expected={sorted(CHUNK_15_WORKFLOW_PROMPTING_IDS)} observed={sorted(manifest_required)}"
        )
    manifest_cards = manifest.get("workflow_prompting_cards", {})
    if not isinstance(manifest_cards, dict):
        errors.append("manifest.workflow_prompting_cards must be a mapping for Chunk 15")
        manifest_cards = {}
    if manifest_cards != CHUNK_15_WORKFLOW_PROMPTING_IDS:
        errors.append(
            "manifest.workflow_prompting_cards does not match Chunk 15 required card map: "
            f"observed={manifest_cards!r}"
        )
    for ident, rel in CHUNK_15_WORKFLOW_PROMPTING_IDS.items():
        if ident not in active:
            errors.append(f"Chunk 15 required workflow/prompting ID not authored: {ident}")
        if not (ROOT / rel).exists():
            errors.append(f"Chunk 15 required workflow/prompting file missing: {rel}")

    allowed_prompting = {Path(p).name for p in CHUNK_15_WORKFLOW_PROMPTING_IDS.values() if p.startswith("topics/prompting/")}
    allowed_workflows = {Path(p).name for p in CHUNK_15_WORKFLOW_PROMPTING_IDS.values() if p.startswith("topics/workflows/")}
    observed_prompting = {p.name for p in (ROOT / "topics" / "prompting").glob("*.md") if p.name != ".gitkeep"}
    observed_workflows = {p.name for p in (ROOT / "topics" / "workflows").glob("*.md") if p.name != ".gitkeep"}
    if observed_prompting != allowed_prompting:
        errors.append(f"Chunk 15 prompting-card scope drift: expected={sorted(allowed_prompting)} observed={sorted(observed_prompting)}")
    if observed_workflows != allowed_workflows:
        errors.append(f"Chunk 15 workflow-card scope drift: expected={sorted(allowed_workflows)} observed={sorted(observed_workflows)}")
    for disallowed in ["topics/tool-catalog", "topics/shortcuts", "topics/field-practices"]:
        files = sorted(p.name for p in (ROOT / disallowed).glob("*.md") if p.name != ".gitkeep")
        if files:
            errors.append(f"Chunk 15 must not add {disallowed} topic cards: {files}")
    pricing_files = sorted(p.name for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep")
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 15 must not expand pricing snapshots: {pricing_files}")

    index_files = [
        ROOT / "indexes" / "INDEX_BY_TASK.md",
        ROOT / "indexes" / "INDEX_BY_CONCEPT.md",
        ROOT / "indexes" / "PROMPT_LIBRARY.md",
        ROOT / "indexes" / "INDEX_FOR_AI_COACHES.md",
    ]
    combined = "\n".join(read(p) for p in index_files)
    llm_maps = read(ROOT / "llms.txt") + "\n" + read(ROOT / "llms-full.txt")
    for ident in CHUNK_15_WORKFLOW_PROMPTING_IDS:
        if f"`{ident}` → active" not in combined and f"`{ident}` → active:" not in combined:
            errors.append(f"primary indexes missing active route for Chunk 15 workflow/prompting topic: {ident}")
        if ident not in llm_maps:
            errors.append(f"llms maps missing route for Chunk 15 workflow/prompting topic: {ident}")


def validate_llm_source_maps(manifest: dict[str, Any], errors: list[str]) -> None:
    current_num = chunk_number_from(manifest.get("chunk_gate", {}).get("current_chunk", ""))
    if current_num is None:
        return
    checks = [
        (ROOT / "llms.txt", "VCB:BEGIN_LLMS"),
        (ROOT / "llms-full.txt", "VCB:BEGIN_LLMS_FULL"),
    ]
    for path, marker_name in checks:
        text = read(path)
        fm = parse_frontmatter(path) or {}
        version = str(fm.get("version", ""))
        marker = re.search(r"<!-- " + re.escape(marker_name) + r" id=[^ ]+ version=([^ >]+) -->", text)
        if not marker:
            errors.append(f"{path.name} missing {marker_name} begin marker")
        elif marker.group(1) != version:
            errors.append(f"{path.name} begin marker version {marker.group(1)!r} does not match frontmatter version {version!r}")
        stale_active = re.findall(r"^## Active Chunk (\d+) content$", text, flags=re.M)
        for n in stale_active:
            if int(n) != current_num:
                errors.append(f"{path.name} has stale visible active-chunk heading: Active Chunk {n} content")
        if path.name == "llms-full.txt":
            stale_chunk_specific = re.findall(r"^## Chunk (\d+) (?:fast routing|Active Files).*$", text, flags=re.M | re.I)
            for n in stale_chunk_specific:
                if int(n) != current_num:
                    errors.append(f"llms-full.txt has stale chunk-specific routing heading for Chunk {n}")


def validate_source_status_official_openai(errors: list[str]) -> None:
    for path in active_topic_files():
        fm = parse_frontmatter(path) or {}
        source_status = fm.get("source_status", {}) if isinstance(fm.get("source_status"), dict) else {}
        declared = bool(source_status.get("official_openai", False))
        ids = evidence_ids(path)
        has_openai = any(sid.startswith("openai.") for sid in ids)
        if declared != has_openai:
            errors.append(
                "source_status.official_openai mismatch in "
                f"{path.relative_to(ROOT)}: declared={declared} evidence_has_openai={has_openai} ids={sorted(ids)}"
            )


def validate_source_register_table_placement(errors: list[str]) -> None:
    """Ensure source-register rows stay inside declared table sections.

    A blank line terminates a Markdown table. Source rows that resume after a
    blank line without a new source-table heading and header are visually
    dangling even if regex source-ID resolution can still find them.
    """
    path = ROOT / "SOURCE_REGISTER.md"
    active_table: str | None = None
    source_sections_seen: set[str] = set()
    source_row_count = 0
    for lineno, raw_line in enumerate(read(path).splitlines(), start=1):
        line = raw_line.strip()
        if not line:
            active_table = None
            continue
        if line.startswith("## "):
            active_table = None
            continue
        if not line.startswith("|"):
            continue

        cells = [c.strip() for c in line.strip("|").split("|")]
        first = cells[0] if cells else ""
        if first == "Source ID":
            active_table = "source"
            source_sections_seen.add(f"line {lineno}")
            if cells != ["Source ID", "Title", "URL / Location", "Evidence", "Verification status", "Use for", "Volatility"]:
                errors.append(f"SOURCE_REGISTER.md source table header has unexpected columns at line {lineno}: {cells}")
            continue
        if first == "Synthesis ID":
            active_table = "synthesis"
            continue
        if set(line.replace("|", "").strip()) <= {"-", ":"}:
            continue

        match = re.match(r"\|\s*`([^`]+)`\s*\|", line)
        if not match:
            continue
        ident = match.group(1)
        if ident.startswith("vcb.synthesis."):
            if active_table != "synthesis":
                errors.append(f"SOURCE_REGISTER.md synthesis row outside synthesis table at line {lineno}: {ident}")
            elif len(cells) != 6:
                errors.append(f"SOURCE_REGISTER.md synthesis row has {len(cells)} cells at line {lineno}; expected 6")
            continue

        source_row_count += 1
        if active_table != "source":
            errors.append(f"SOURCE_REGISTER.md source row outside declared source table at line {lineno}: {ident}")
        elif len(cells) != 7:
            errors.append(f"SOURCE_REGISTER.md source row has {len(cells)} cells at line {lineno}; expected 7: {ident}")

    if source_row_count == 0:
        errors.append("SOURCE_REGISTER.md has no parsed source rows")
    if not source_sections_seen:
        errors.append("SOURCE_REGISTER.md has no declared Source ID table section")

def validate_feature_flag_source_metadata(errors: list[str]) -> None:
    path = ROOT / "topics" / "concepts" / "feature-flag.md"
    if not path.exists():
        return
    fm = parse_frontmatter(path) or {}
    ids = evidence_ids(path)
    if "openfeature.docs_intro" not in ids:
        errors.append("feature-flag concept does not cite openfeature.docs_intro")
    if fm.get("evidence_level") != "E0_OFFICIAL_DOCS":
        errors.append("feature-flag concept evidence_level must be E0_OFFICIAL_DOCS when OpenFeature is the primary definition anchor")
    sk = fm.get("source_kind")
    if sk != "official_docs_plus_maintainer_synthesis":
        errors.append(f"feature-flag concept source_kind mismatch: {sk!r}")


def strip_fenced_code_blocks(text: str) -> str:
    """Remove fenced code blocks before scanning for active VCB markers.

    Authoring protocol files contain example marker strings with placeholder versions.
    Those examples are documentation, not repository signposts.
    """
    return re.sub(r"(?ms)^```.*?^```\s*", "", text)


def validate_markdown_begin_marker_frontmatter_versions(errors: list[str]) -> None:
    """Every actual VCB:BEGIN_* marker with a version must match frontmatter."""
    marker_re = re.compile(r"<!--\s*VCB:BEGIN_[^>]*?\bversion=([^\s>]+)[^>]*?-->")
    for path in sorted(ROOT.rglob("*.md")):
        fm = parse_frontmatter(path) or {}
        version = fm.get("version")
        if not version:
            continue
        body = strip_fenced_code_blocks(read(path))
        for match in marker_re.finditer(body):
            observed = match.group(1)
            if observed == "...":
                continue
            if observed != str(version):
                errors.append(
                    f"VCB begin-marker version mismatch in {path.relative_to(ROOT)}: "
                    f"frontmatter={version!r} marker={observed!r}"
                )



def validate_vcb_marker_pairing_and_index_terminals(errors: list[str]) -> None:
    """Validate hard VCB signpost pairing across routing/source-map artifacts."""
    paths = sorted(list(ROOT.rglob("*.md")) + list(ROOT.rglob("*.txt")))
    begin_re = re.compile(r"<!--\s*VCB:BEGIN_([A-Z_]+)\s+id=([^\s>]+)[^>]*?-->")
    for path in paths:
        if "__pycache__" in path.parts or path.name == "TREE.txt":
            continue
        text = strip_fenced_code_blocks(read(path))
        rel = path.relative_to(ROOT)
        for kind, ident in begin_re.findall(text):
            if f"VCB:END_{kind} id={ident}" not in text:
                errors.append(f"VCB marker pair missing in {rel}: BEGIN_{kind} id={ident} has no matching END_{kind}")
        if path.parent == ROOT / "indexes" and "VCB:BEGIN_INDEX" in text:
            if "<!-- VCB:STOP_RETRIEVAL" not in text:
                errors.append(f"index missing STOP_RETRIEVAL marker: {rel}")
            for ident in re.findall(r"<!--\s*VCB:BEGIN_INDEX\s+id=([^\s>]+)", text):
                if f"<!-- VCB:END_INDEX id={ident} -->" not in text:
                    errors.append(f"index missing END_INDEX marker for {ident}: {rel}")


def validate_readme_next_chunk_route(manifest: dict[str, Any], errors: list[str]) -> None:
    expected = str(manifest.get("next_recommended_chunk", {}).get("id", ""))
    if not expected:
        errors.append("manifest.next_recommended_chunk.id is missing")
        return
    readme_text = read(ROOT / "README.md")
    match = re.search(r"Recommended next chunk after approval:\s*`([^`]+)`", readme_text)
    if not match:
        errors.append("README.md missing recommended next-chunk route")
    elif match.group(1) != expected:
        errors.append(
            "README.md recommended next-chunk route does not match manifest.next_recommended_chunk.id: "
            f"README={match.group(1)!r} manifest={expected!r}"
        )
    report_path = ROOT / f"CHUNK_{chunk_number_from(manifest.get('chunk_gate', {}).get('current_chunk', ''))}_REPORT.md"
    if report_path.exists():
        report_text = read(report_path)
        report_next = re.search(r"Recommended next chunk after approval:\s*`([^`]+)`", report_text)
        if report_next and report_next.group(1) != expected:
            errors.append(
                f"{report_path.name} recommended next-chunk route does not match manifest: "
                f"{report_next.group(1)!r} != {expected!r}"
            )


def validate_manifest_redirect_consistency(manifest: dict[str, Any], errors: list[str]) -> None:
    """The two manifest namespace redirect mirrors must be identical.

    Conflicting redirect maps are machine-readable governance drift: the same
    alias could resolve to different active topic cards depending on which
    policy block an LLM or tool reads.
    """
    topic_redirects = manifest.get("topic_namespace_policy", {}).get("topic_id_redirects", {})
    namespace_redirects = manifest.get("namespace_policy", {}).get("topic_id_redirects", {})
    if not isinstance(topic_redirects, dict) or not isinstance(namespace_redirects, dict):
        errors.append("manifest topic_id_redirects blocks must both be mappings")
        return
    if topic_redirects != namespace_redirects:
        keys = sorted(set(topic_redirects) | set(namespace_redirects))
        diffs = [
            f"{key}: topic_namespace_policy={topic_redirects.get(key)!r} namespace_policy={namespace_redirects.get(key)!r}"
            for key in keys
            if topic_redirects.get(key) != namespace_redirects.get(key)
        ]
        errors.append("manifest topic_namespace_policy.topic_id_redirects and namespace_policy.topic_id_redirects disagree: " + "; ".join(diffs))


CHUNK_17_TASK_ROUTE_REQUIREMENTS = {
    "Improve frontend UI": {
        "vcb.workflow.frontend_work",
        "vcb.workflow.visual_qa",
        "vcb.workflow.accessibility_review",
    },
    "Refactor safely": {"vcb.workflow.refactoring"},
    "Remove dead code": {"vcb.workflow.refactoring"},
    "Choose dependencies, packages, or frameworks": {"vcb.workflow.dependency_decisions"},
    "Migrate a dependency": {"vcb.workflow.dependency_update_review"},
    "Generate release notes": {"vcb.workflow.release_notes"},
    "Improve documentation": {"vcb.workflow.documentation_updates"},
}

PLANNED_ROUTE_REPLACEMENTS = {
    "vcb.workflow.documentation_update": "vcb.workflow.documentation_updates",
}


def has_active_route(section: str, ident: str) -> bool:
    return bool(re.search(rf"`{re.escape(ident)}`\s*→\s*active(?:\s|:|$)", section))


def validate_chunk_17_task_index_atomic_routes(manifest: dict[str, Any], errors: list[str]) -> None:
    """Ensure the task index routes common tasks to the active Chunk 17 cards.

    Aggregate Chunk 17 lists are useful as inventories, but task sections must
    route to the smallest active card once that card exists.
    """
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_17":
        return
    path = ROOT / "indexes" / "INDEX_BY_TASK.md"
    text = read(path)
    sections = {heading: body for heading, body in markdown_h2_sections(text)}
    for heading, required_ids in CHUNK_17_TASK_ROUTE_REQUIREMENTS.items():
        body = sections.get(heading)
        if body is None:
            errors.append(f"INDEX_BY_TASK.md missing required task section for Chunk 17 route checks: {heading}")
            continue
        for ident in sorted(required_ids):
            if not has_active_route(body, ident):
                errors.append(
                    f"INDEX_BY_TASK.md section {heading!r} missing active atomic Chunk 17 route: {ident}"
                )

    active = authored_active_ids()
    for index_path in sorted((ROOT / "indexes").glob("*.md")):
        body = read(index_path)
        for old_ident, new_ident in PLANNED_ROUTE_REPLACEMENTS.items():
            if f"`{old_ident}`" in body:
                errors.append(f"stale planned route {old_ident} remains in {index_path.relative_to(ROOT)}")
            if new_ident in active and re.search(rf"`{re.escape(old_ident)}`\s*→\s*planned", body):
                errors.append(
                    f"planned route {old_ident} shadows authored active replacement {new_ident} in {index_path.relative_to(ROOT)}"
                )


def validate_vcb_begin_end_pairs(errors: list[str]) -> None:
    """Every active VCB:BEGIN_* marker must have a matching VCB:END_* marker."""
    begin_re = re.compile(r"<!--\s*VCB:BEGIN_([A-Z_]+)\s+id=([^\s>]+)[^>]*-->")
    end_re = re.compile(r"<!--\s*VCB:END_([A-Z_]+)\s+id=([^\s>]+)\s*-->")
    for path in sorted(ROOT.rglob("*.md")):
        body = strip_fenced_code_blocks(read(path))
        begins = Counter(begin_re.findall(body))
        ends = Counter(end_re.findall(body))
        if begins != ends:
            missing = sorted((begins - ends).elements())
            extra = sorted((ends - begins).elements())
            if missing:
                errors.append(f"VCB begin marker lacks matching end marker in {path.relative_to(ROOT)}: {missing}")
            if extra:
                errors.append(f"VCB end marker lacks matching begin marker in {path.relative_to(ROOT)}: {extra}")


def validate_index_terminal_signposts(errors: list[str]) -> None:
    """Every routing index must have BEGIN_INDEX, STOP_RETRIEVAL, and matching END_INDEX."""
    begin_re = re.compile(r"<!--\s*VCB:BEGIN_INDEX\s+id=([^\s>]+)[^>]*-->")
    end_re = re.compile(r"<!--\s*VCB:END_INDEX\s+id=([^\s>]+)\s*-->")
    stop_re = re.compile(r"<!--\s*VCB:STOP_RETRIEVAL\b[^>]*-->")
    for path in sorted((ROOT / "indexes").glob("*.md")):
        body = strip_fenced_code_blocks(read(path))
        begin = begin_re.search(body)
        if not begin:
            errors.append(f"index file missing VCB:BEGIN_INDEX marker: {path.relative_to(ROOT)}")
            continue
        begin_id = begin.group(1)
        stop_matches = list(stop_re.finditer(body))
        end_matches = list(end_re.finditer(body))
        if not stop_matches:
            errors.append(f"index file missing VCB:STOP_RETRIEVAL marker: {path.relative_to(ROOT)}")
        if not end_matches:
            errors.append(f"index file missing VCB:END_INDEX marker: {path.relative_to(ROOT)}")
            continue
        end_id = end_matches[-1].group(1)
        if end_id != begin_id:
            errors.append(
                f"index VCB:END_INDEX id mismatch in {path.relative_to(ROOT)}: "
                f"begin={begin_id!r} end={end_id!r}"
            )
        if stop_matches and stop_matches[-1].start() > end_matches[-1].start():
            errors.append(f"index STOP_RETRIEVAL appears after END_INDEX in {path.relative_to(ROOT)}")

def validate_markdown_terminal_end_content(manifest: dict[str, Any], errors: list[str]) -> None:
    """No live markdown content may appear after terminal VCB END markers.

    Historical chunk reports preserve the repository convention of a single
    AUTHOR_STATUS line after END_REPORT. Other artifacts must end at the VCB
    boundary except for whitespace.
    """
    end_re = re.compile(r"<!--\s*VCB:END_[A-Z_]+\s+id=[^>]+-->")
    for path in sorted(ROOT.rglob("*.md")):
        text = read(path)
        matches = list(end_re.finditer(text))
        if not matches:
            continue
        tail = text[matches[-1].end():].strip()
        if not tail:
            continue
        if re.fullmatch(r"AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW", tail) and re.fullmatch(r"CHUNK_\d+_REPORT\.md", path.name):
            continue
        errors.append(f"live content appears after terminal VCB END marker in {path.relative_to(ROOT)}")
    changelog = ROOT / "CHANGELOG.md"
    if changelog.exists():
        text = read(changelog)
        end_match = re.search(r"<!--\s*VCB:END_CHANGELOG\s+id=vcb\.register\.changelog\s*-->", text)
        if end_match and text[end_match.end():].strip():
            errors.append("CHANGELOG.md has live content after VCB:END_CHANGELOG")



CODEX_FEATURE_IDS = {
    "vcb.codex.app",
    "vcb.codex.cli",
    "vcb.codex.ide_extension",
    "vcb.codex.cloud",
    "vcb.codex.github_review",
    "vcb.codex.config",
    "vcb.codex.agents_md",
    "vcb.codex.skills",
    "vcb.codex.mcp",
    "vcb.codex.hooks",
    "vcb.codex.automations",
    "vcb.codex.subagents",
    "vcb.codex.computer_use",
    "vcb.codex.feature_maturity",
    "vcb.codex.changelog_monitoring",
}


def markdown_h2_sections(text: str) -> list[tuple[str, str]]:
    matches = list(re.finditer(r"(?m)^##\s+(.+?)\s*$", text))
    sections: list[tuple[str, str]] = []
    for index, match in enumerate(matches):
        start = match.end()
        end = matches[index + 1].start() if index + 1 < len(matches) else len(text)
        sections.append((match.group(1).strip(), text[start:end]))
    return sections


def validate_duplicate_codex_feature_full_list_sections(errors: list[str]) -> None:
    """Reject repeated all-feature blocks inside one index.

    Repeating individual feature IDs in distinct routing contexts is acceptable.
    Repeating the entire 15-card feature list in multiple sections of the same index is not.
    """
    for path in sorted((ROOT / "indexes").glob("*.md")):
        full_sections: list[str] = []
        for heading, body in markdown_h2_sections(read(path)):
            ids = set(re.findall(r"`(vcb\.codex\.[A-Za-z0-9_.-]+)`", body))
            if CODEX_FEATURE_IDS.issubset(ids):
                full_sections.append(heading)
        if len(full_sections) > 1:
            errors.append(
                f"duplicate full Codex feature routing sections in {path.relative_to(ROOT)}: {full_sections}"
            )


WORKFLOW_PROMPTING_IDS = {
    "vcb.prompting.four_part_prompt",
    "vcb.prompting.acceptance_criteria",
    "vcb.prompting.plan_first",
    "vcb.prompting.context_management",
    "vcb.workflow.unknown_codebase",
    "vcb.workflow.feature_slicing",
    "vcb.workflow.bug_repro",
    "vcb.workflow.testing",
}


def validate_duplicate_workflow_prompting_full_list_sections(errors: list[str]) -> None:
    """Reject repeated full workflow/prompting card blocks inside one index.

    Repeating individual card IDs in useful routing contexts is acceptable.
    Repeating the entire Chunk 15 workflow/prompting list more than once in one index is retrieval noise.
    """
    for path in sorted((ROOT / "indexes").glob("*.md")):
        full_sections: list[str] = []
        for heading, body in markdown_h2_sections(read(path)):
            ids = set(re.findall(r"`(vcb\.(?:prompting|workflow)\.[A-Za-z0-9_.-]+)`", body))
            if WORKFLOW_PROMPTING_IDS.issubset(ids):
                full_sections.append(heading)
        if len(full_sections) > 1:
            errors.append(
                f"duplicate full workflow/prompting routing sections in {path.relative_to(ROOT)}: {full_sections}"
            )



CHUNK_16_REVIEW_SAFETY_IDS = {
    "vcb.workflow.codex_output_review": "topics/workflows/codex-output-review.md",
    "vcb.workflow.reviewing_diffs": "topics/workflows/reviewing-diffs.md",
    "vcb.workflow.github_pr_review": "topics/workflows/github-pr-review.md",
    "vcb.safety.security_review": "topics/safety/security-review.md",
    "vcb.safety.secrets": "topics/safety/secrets.md",
    "vcb.workflow.ci_triage": "topics/workflows/ci-triage.md",
    "vcb.workflow.ci_noninteractive": "topics/workflows/ci-noninteractive.md",
    "vcb.safety.production_red_lines": "topics/safety/production-red-lines.md",
}

REVIEW_SAFETY_WORKFLOW_IDS = set(CHUNK_16_REVIEW_SAFETY_IDS)


def validate_duplicate_review_safety_full_list_sections(errors: list[str]) -> None:
    """Reject repeated full Chunk 16 review/safety routing blocks inside one index."""
    for path in sorted((ROOT / "indexes").glob("*.md")):
        full_sections: list[str] = []
        for heading, body in markdown_h2_sections(read(path)):
            ids = set(re.findall(r"`(vcb\.(?:workflow|safety)\.[A-Za-z0-9_.-]+)`", body))
            if REVIEW_SAFETY_WORKFLOW_IDS.issubset(ids):
                full_sections.append(heading)
        if len(full_sections) > 1:
            errors.append(
                f"duplicate full review/safety workflow routing sections in {path.relative_to(ROOT)}: {full_sections}"
            )


def validate_chunk_16_review_safety_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    current = manifest.get("chunk_gate", {}).get("current_chunk", "")
    if current != "chunk_16":
        return
    active = authored_active_ids()
    manifest_required = set(manifest.get("chunk_16_required_topic_ids", []) or [])
    if manifest_required != set(CHUNK_16_REVIEW_SAFETY_IDS):
        errors.append(
            "manifest.chunk_16_required_topic_ids mismatch: "
            f"expected={sorted(CHUNK_16_REVIEW_SAFETY_IDS)} observed={sorted(manifest_required)}"
        )
    manifest_cards = manifest.get("review_safety_workflow_cards", {})
    if not isinstance(manifest_cards, dict):
        errors.append("manifest.review_safety_workflow_cards must be a mapping for Chunk 16")
        manifest_cards = {}
    if manifest_cards != CHUNK_16_REVIEW_SAFETY_IDS:
        errors.append(
            "manifest.review_safety_workflow_cards does not match Chunk 16 required card map: "
            f"observed={manifest_cards!r}"
        )
    for ident, rel in CHUNK_16_REVIEW_SAFETY_IDS.items():
        if ident not in active:
            errors.append(f"Chunk 16 required review/safety workflow ID not authored: {ident}")
        if not (ROOT / rel).exists():
            errors.append(f"Chunk 16 required review/safety workflow file missing: {rel}")

    allowed_prompting = {Path(p).name for p in CHUNK_15_WORKFLOW_PROMPTING_IDS.values() if p.startswith("topics/prompting/")}
    allowed_workflows = {Path(p).name for p in CHUNK_15_WORKFLOW_PROMPTING_IDS.values() if p.startswith("topics/workflows/")}
    allowed_workflows |= {Path(p).name for p in CHUNK_16_REVIEW_SAFETY_IDS.values() if p.startswith("topics/workflows/")}
    allowed_safety = {Path(p).name for p in CHUNK_16_REVIEW_SAFETY_IDS.values() if p.startswith("topics/safety/")}
    observed_prompting = {p.name for p in (ROOT / "topics" / "prompting").glob("*.md") if p.name != ".gitkeep"}
    observed_workflows = {p.name for p in (ROOT / "topics" / "workflows").glob("*.md") if p.name != ".gitkeep"}
    observed_safety = {p.name for p in (ROOT / "topics" / "safety").glob("*.md") if p.name != ".gitkeep"}
    if observed_prompting != allowed_prompting:
        errors.append(f"Chunk 16 must not alter prompting-card scope: expected={sorted(allowed_prompting)} observed={sorted(observed_prompting)}")
    if observed_workflows != allowed_workflows:
        errors.append(f"Chunk 16 workflow-card scope drift: expected={sorted(allowed_workflows)} observed={sorted(observed_workflows)}")
    if observed_safety != allowed_safety:
        errors.append(f"Chunk 16 safety-card scope drift: expected={sorted(allowed_safety)} observed={sorted(observed_safety)}")
    for disallowed in ["topics/tool-catalog", "topics/shortcuts", "topics/field-practices"]:
        files = sorted(p.name for p in (ROOT / disallowed).glob("*.md") if p.name != ".gitkeep")
        if files:
            errors.append(f"Chunk 16 must not add {disallowed} topic cards: {files}")
    pricing_files = sorted(p.name for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep")
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 16 must not expand pricing snapshots: {pricing_files}")

    index_files = [
        ROOT / "indexes" / "INDEX_BY_TASK.md",
        ROOT / "indexes" / "INDEX_BY_CONCEPT.md",
        ROOT / "indexes" / "INDEX_BY_FAILURE_MODE.md",
        ROOT / "indexes" / "INDEX_BY_RISK_LEVEL.md",
        ROOT / "indexes" / "INDEX_BY_RECOVERABILITY.md",
        ROOT / "indexes" / "INDEX_FOR_AI_COACHES.md",
        ROOT / "indexes" / "PROMPT_LIBRARY.md",
    ]
    combined = "\n".join(read(p) for p in index_files)
    llm_maps = read(ROOT / "llms.txt") + "\n" + read(ROOT / "llms-full.txt")
    for ident in CHUNK_16_REVIEW_SAFETY_IDS:
        if f"`{ident}` → active" not in combined and f"`{ident}` → active:" not in combined:
            errors.append(f"primary indexes missing active route for Chunk 16 review/safety workflow topic: {ident}")
        if ident not in llm_maps:
            errors.append(f"llms maps missing route for Chunk 16 review/safety workflow topic: {ident}")

CHUNK_14_MACHINE_REPORT_CLAIMS = {
    "Manifest source-file inventory matches actual package files: passed",
    "Manifest source_artifacts inventory matches actual package files: passed",
    "Manifest all_tracked_files matches source_files and actual package files: passed",
    "Canonical review package references are consistent across manifest fields: passed",
    "New Codex feature topic files created in Chunk 14: passed",
    "Required Chunk 14 Codex feature-card slice present: passed",
    "Required topic sections present: passed",
    "Required VCB markers present in new Codex feature files: passed",
    "llms.txt / llms-full.txt source-map versions match current chunk: passed",
    "README root frontmatter status matches current chunk: passed",
    "README body current chunk matches manifest current chunk: passed",
    "README and manifest next-chunk IDs match exactly: passed",
    "Index/register VCB begin-marker versions match frontmatter versions: passed",
    "Duplicate workflow/prompting full-list sections removed from primary indexes: passed",
    "Duplicate Codex feature full-list sections removed from primary indexes: passed",
    "Active Chunk 14 machine-claim catalog matches validator checks: passed",
    "Manifest editor_gate approval_applied matches current chunk transition: passed",
    "Current chunk report chunk_id matches manifest active chunk: passed",
    "Root governance metadata drift scan: passed",
    "Index namespace drift scan covers active and planned index routes: passed",
    "Active index routes point to authored active IDs: passed",
    "Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed",
    "Index shortcut routes resolve to SHORTCUT_REGISTER: passed",
    "Index tool IDs resolve to TOOL_REGISTER: passed",
    "Evidence source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed",
    "source_status.official_openai matches Evidence and Sources sections: passed",
    "source_status.official_vendor matches Evidence and Sources sections: passed",
    "Duplicate source URL detection: passed",
    "Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed",
    "Report final line is AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW: passed",
}


def extract_machine_report_claims(text: str) -> set[str]:
    match = re.search(
        r"(?ms)^### Machine-enforced checks\n(.*?)(?=^### |^## |\Z)",
        text,
    )
    if not match:
        return set()
    claims: set[str] = set()
    for raw_line in match.group(1).splitlines():
        line = raw_line.strip()
        if not line.startswith("- "):
            continue
        claim = line[2:].strip()
        if claim.endswith(": passed"):
            claims.add(claim)
    return claims




CHUNK_25_SHORTCUT_IDS = {
    "vcb.shortcut.unattended_cloud_delegation": "topics/shortcuts/unattended-cloud-delegation.md",
    "vcb.shortcut.ambiguous_cloud_task": "topics/shortcuts/ambiguous-cloud-task.md",
    "vcb.shortcut.cloud_task_without_context": "topics/shortcuts/cloud-task-without-context.md",
    "vcb.shortcut.parallel_cloud_sprawl": "topics/shortcuts/parallel-cloud-sprawl.md",
    "vcb.shortcut.conflicting_parallel_agents": "topics/shortcuts/conflicting-parallel-agents.md",
    "vcb.shortcut.automation_spam": "topics/shortcuts/automation-spam.md",
    "vcb.shortcut.automation_mutation_without_review": "topics/shortcuts/automation-mutation-without-review.md",
    "vcb.shortcut.browser_clicking_without_repro": "topics/shortcuts/browser-clicking-without-repro.md",
    "vcb.shortcut.logged_in_browser_secrets": "topics/shortcuts/logged-in-browser-secrets.md",
}

CHUNK_25_REQUIRED_INDEXES = [
    "indexes/GLOSSARY.md",
    "indexes/INDEX_BY_BUDGET_PROFILE.md",
    "indexes/INDEX_BY_CODEX_SURFACE.md",
    "indexes/INDEX_BY_CONCEPT.md",
    "indexes/INDEX_BY_FAILURE_MODE.md",
    "indexes/INDEX_BY_PROJECT_TYPE.md",
    "indexes/INDEX_BY_RECOVERABILITY.md",
    "indexes/INDEX_BY_RISK_LEVEL.md",
    "indexes/INDEX_BY_SHORTCUT.md",
    "indexes/INDEX_BY_STABILITY.md",
    "indexes/INDEX_BY_TASK.md",
    "indexes/INDEX_BY_TOOL_CATEGORY.md",
    "indexes/INDEX_FOR_AI_COACHES.md",
    "indexes/PROMPT_LIBRARY.md",
]

CHUNK_25_SECTION_REQUIREMENTS = [
    ("indexes/INDEX_BY_SHORTCUT.md", "Parallel Cloud and Automation Shortcut Routes", set(CHUNK_25_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_TASK.md", "Parallel Cloud and Automation Shortcut Routes", set(CHUNK_25_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_FAILURE_MODE.md", "Parallel Cloud and Automation Shortcut Routes", set(CHUNK_25_SHORTCUT_IDS)),
    ("indexes/INDEX_FOR_AI_COACHES.md", "Parallel Cloud and Automation Shortcut Routes", set(CHUNK_25_SHORTCUT_IDS)),
    ("indexes/PROMPT_LIBRARY.md", "Parallel Cloud and Automation Shortcut Routes", set(CHUNK_25_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_RISK_LEVEL.md", "Parallel Cloud and Automation Shortcut Routes", set(CHUNK_25_SHORTCUT_IDS)),
]

CHUNK_25_REPORT_REQUIRED_CLAIMS = {
    "New parallel/cloud/automation shortcut topic files created in Chunk 25: passed",
    "Required Chunk 25 parallel/cloud/automation shortcut-card slice present: passed",
    "Manifest parallel_cloud_automation_shortcut_cards map matches authored Chunk 25 files: passed",
    "Manifest chunk_25_required_topic_ids matches authored Chunk 25 IDs: passed",
    "Manifest redirects do not shadow active Chunk 25 canonical IDs: passed",
    "Required VCB markers present in new Chunk 25 shortcut files: passed",
    "Required sections present in new Chunk 25 shortcut files: passed",
    "SHORTCUT_REGISTER marks authored Chunk 25 shortcut IDs active: passed",
    "Primary indexes route active Chunk 25 parallel/cloud/automation shortcut cards: passed",
    "Prompt library routes active Chunk 25 parallel/cloud/automation shortcut cards: passed",
    "AI coach index routes active Chunk 25 parallel/cloud/automation shortcut cards: passed",
    "LLM source maps route active Chunk 25 parallel/cloud/automation shortcut cards: passed",
    "Generic LLM shortcut route covers active Chunk 20, Chunk 21, Chunk 22, Chunk 23, Chunk 24, and Chunk 25 shortcut-card slices: passed",
    "General Fast Routing includes semantic Chunk 25 parallel/cloud/automation shortcut intents before fallback routing: passed",
    "Semantic risk/shortcut/task/failure index sections route active Chunk 25 cards: passed",
    "Stale planned routes for authored Chunk 25 shortcuts are absent from indexes and SHORTCUT_REGISTER: passed",
    "No single index section contains duplicate active Chunk 25 shortcut rows: passed",
    "No primary index contains multiple full-list sections for the Chunk 25 shortcut-card set: passed",
    "Active Chunk 25 related-topic IDs resolve to active topic cards: passed",
    "CHANGELOG.md has one current-chunk heading for Chunk 25: passed",
    "Chunk 25 report/changelog routing claims match routed surfaces and consolidated index state: passed",
    "Chunk 25 did not start full shortcut expansion or disallowed topic-card families: passed",
    "Active Chunk 25 report inventory lists created shortcut cards and updated routing/governance files: passed",
    "Active Chunk 25 machine-claim catalog matches validator checks: passed",
}


def validate_chunk_25_parallel_cloud_automation_shortcut_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_25":
        return
    required = CHUNK_25_SHORTCUT_IDS

    readme_sections = {h: b for h, b in markdown_h2_sections(read(ROOT / "README.md"))}
    readme_next = readme_sections.get("Next Chunk", "")
    manifest_next_id = str(manifest.get("next_recommended_chunk", {}).get("id", ""))
    if manifest_next_id and f"`{manifest_next_id}`" not in readme_next:
        errors.append("README.md Next Chunk section does not name manifest.next_recommended_chunk.id")
    stale_scope_terms = ["approved parallel/cloud/automation slice", "unattended cloud delegation, parallel task conflicts, automation overreach"]
    if any(term in readme_next for term in stale_scope_terms):
        errors.append("README.md Next Chunk section still describes completed Chunk 25 parallel/cloud/automation scope")
    if "Blocked until the editor sets the exact bounded Chunk 26 scope" not in readme_next:
        errors.append("README.md Next Chunk section must clearly block Chunk 26 until editor-scoped approval")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    if "Chunk 25" not in current_checks or "parallel/cloud/automation" not in current_checks:
        errors.append("manifest.validation_expectations.current_chunk_checks must name Chunk 25 parallel/cloud/automation shortcut checks")
    if manifest.get("parallel_cloud_automation_shortcut_cards") != required:
        errors.append("manifest.parallel_cloud_automation_shortcut_cards does not match Chunk 25 required card map")
    if manifest.get("chunk_25_required_topic_ids") != list(required):
        errors.append("manifest.chunk_25_required_topic_ids does not match required Chunk 25 IDs")

    active_ids = authored_active_ids()
    for policy_name in ["topic_namespace_policy", "namespace_policy"]:
        redirects = manifest.get(policy_name, {}).get("topic_id_redirects", {})
        if not isinstance(redirects, dict):
            continue
        for key, value in redirects.items():
            if key in active_ids and key != value:
                errors.append(f"manifest.{policy_name}.topic_id_redirects uses active canonical ID as redirect key: {key} -> {value}")
            if key in required and key != value:
                errors.append(f"manifest.{policy_name}.topic_id_redirects must not shadow authored Chunk 25 ID: {key} -> {value}")

    topic_cards = manifest.get("topic_cards", {})
    for ident, rel in required.items():
        path = ROOT / rel
        if topic_cards.get(ident) != rel:
            errors.append(f"manifest.topic_cards missing Chunk 25 route: {ident} -> {rel}")
        if not path.exists():
            errors.append(f"missing Chunk 25 shortcut file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != ident or fm.get("type") != "shortcut" or fm.get("status") != "active":
            errors.append(f"frontmatter for {rel} does not declare active shortcut ID {ident}")
        body = read(path)
        if f"<!-- VCB:BEGIN_TOPIC id={ident}" not in body:
            errors.append(f"{rel} missing matching Chunk 25 begin topic marker")
        if f"<!-- VCB:END_TOPIC id={ident} -->" not in body:
            errors.append(f"{rel} missing matching end topic marker")
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in body:
                errors.append(f"{rel} missing required topic heading {heading}")
        if "## Quick Navigation" not in body:
            errors.append(f"{rel} missing shortcut-card Quick Navigation section")

    allowed_shortcut_files = (
        {Path(v).name for v in CHUNK_20_SHORTCUT_IDS.values()}
        | {Path(v).name for v in CHUNK_21_SHORTCUT_IDS.values()}
        | {Path(v).name for v in CHUNK_22_SHORTCUT_IDS.values()}
        | {Path(v).name for v in CHUNK_23_SHORTCUT_IDS.values()}
        | {Path(v).name for v in CHUNK_24_SHORTCUT_IDS.values()}
        | {Path(v).name for v in required.values()}
        | {".gitkeep"}
    )
    observed_shortcut_files = {p.name for p in (ROOT / "topics" / "shortcuts").glob("*")}
    if observed_shortcut_files != allowed_shortcut_files:
        errors.append(f"Chunk 25 shortcut-card scope drift: expected={sorted(allowed_shortcut_files)} observed={sorted(observed_shortcut_files)}")
    for disallowed in ["topics/tool-catalog", "topics/field-practices"]:
        files = [p.name for p in (ROOT / disallowed).glob("*.md")]
        if files:
            errors.append(f"Chunk 25 must not add {disallowed} topic cards: {files}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md")]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 25 must not expand pricing snapshots: {pricing_files}")

    statuses = shortcut_register_statuses()
    register_text = read(ROOT / "SHORTCUT_REGISTER.md")
    for ident in required:
        if statuses.get(ident) != "active":
            errors.append(f"SHORTCUT_REGISTER row for {ident} must be active; observed={statuses.get(ident)!r}")
        if re.search(rf"`{re.escape(ident)}`[^\n]*\|\s*planned\s*\|", register_text):
            errors.append(f"SHORTCUT_REGISTER still lists authored Chunk 25 shortcut as planned: {ident}")

    for rel in CHUNK_25_REQUIRED_INDEXES:
        body = read(ROOT / rel)
        full_list_sections = []
        for heading, section_body in markdown_h2_sections(body):
            section_ids = set(re.findall(r"`(vcb\.shortcut\.[A-Za-z0-9_.-]+)`", section_body))
            if set(required).issubset(section_ids):
                full_list_sections.append(heading)
            for ident in required:
                if section_body.count(f"`{ident}`") > 1 and "intentional duplicate" not in section_body.lower():
                    errors.append(f"{rel} section {heading!r} contains duplicate active Chunk 25 shortcut route: {ident}")
        if len(full_list_sections) > 1:
            errors.append(f"{rel} contains duplicate full-list Chunk 25 shortcut sections: {full_list_sections}")
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing route for Chunk 25 shortcut card: {ident}")
            if re.search(rf"`{re.escape(ident)}`\s*→\s*planned", body):
                errors.append(f"{rel} has stale planned route for authored Chunk 25 shortcut: {ident}")

    for rel in ["README.md", "llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing Chunk 25 source-map/root route: {ident}")

    required_terms = [
        "active shortcut-card slices", "Chunk 20 harm-reduction cards", "Chunk 21 security/permission cards",
        "Chunk 22 setup/process cards", "Chunk 23 tool-sprawl/skill/reusable-workflow cards",
        "Chunk 24 multi-AI/model-bias cards", "Chunk 25 parallel/cloud/automation cards",
    ]
    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        if "User asks to make a shortcut safer" in body and not all(term in body for term in required_terms):
            errors.append(f"{rel} generic shortcut safety route does not cover active Chunk 20-25 shortcut-card slices")
        status_phrase = "Parallel/cloud/automation shortcut cards from Chunk 25 are active."
        if body.count(status_phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 25 status phrase; observed={body.count(status_phrase)}")
        full_list_sections = len(re.findall(r"^## Active Chunk 25 Parallel Cloud and Automation Shortcut Cards\s*$", body, flags=re.M))
        if full_list_sections != 1:
            errors.append(f"{rel} must contain exactly one consolidated full-list section for Chunk 25 shortcut cards; observed={full_list_sections}")
        fast = {h: b for h, b in markdown_h2_sections(body)}.get("Parallel Cloud and Automation Shortcut Fast Routing", "")
        semantic_terms = ["unattended cloud", "ambiguous", "missing context", "parallel", "automation", "browser", "signed-in"]
        if not fast or not all(term in fast.lower() for term in semantic_terms):
            errors.append(f"{rel} general Fast Routing lacks direct semantic Chunk 25 shortcut-intent coverage")
        fallback_pos = body.find("## Shortcut Harm-Reduction Card Fast Routing")
        fast_pos = body.find("## Parallel Cloud and Automation Shortcut Fast Routing")
        if fallback_pos >= 0 and (fast_pos < 0 or fast_pos > fallback_pos):
            errors.append(f"{rel} Chunk 25 semantic Fast Routing appears after shortcut fallback")

    for rel, heading, ids in CHUNK_25_SECTION_REQUIREMENTS:
        sections = {h: b for h, b in markdown_h2_sections(read(ROOT / rel))}
        section_body = sections.get(heading, "")
        if not section_body:
            errors.append(f"{rel} missing Chunk 25 semantic section: {heading}")
        for ident in ids:
            if f"`{ident}`" not in section_body:
                errors.append(f"{rel} section {heading!r} missing active Chunk 25 route: {ident}")

    existing_semantic_requirements = [
        ("indexes/INDEX_BY_TASK.md", "Use cloud, subagents, browser, or GUI surfaces", {
            "vcb.shortcut.unattended_cloud_delegation", "vcb.shortcut.ambiguous_cloud_task", "vcb.shortcut.cloud_task_without_context",
            "vcb.shortcut.parallel_cloud_sprawl", "vcb.shortcut.conflicting_parallel_agents", "vcb.shortcut.browser_clicking_without_repro", "vcb.shortcut.logged_in_browser_secrets",
        }),
        ("indexes/INDEX_BY_FAILURE_MODE.md", "Cloud, subagent, or GUI work runs too broadly", {
            "vcb.shortcut.unattended_cloud_delegation", "vcb.shortcut.ambiguous_cloud_task", "vcb.shortcut.cloud_task_without_context",
            "vcb.shortcut.parallel_cloud_sprawl", "vcb.shortcut.conflicting_parallel_agents", "vcb.shortcut.browser_clicking_without_repro", "vcb.shortcut.logged_in_browser_secrets",
        }),
        ("indexes/INDEX_BY_FAILURE_MODE.md", "CI or automation mutates too much", {"vcb.shortcut.automation_mutation_without_review", "vcb.shortcut.automation_spam"}),
        ("indexes/INDEX_FOR_AI_COACHES.md", "Human wants broad permissions, automation, or GUI control", {"vcb.shortcut.unattended_cloud_delegation", "vcb.shortcut.automation_mutation_without_review", "vcb.shortcut.logged_in_browser_secrets", "vcb.shortcut.browser_clicking_without_repro"}),
        ("indexes/INDEX_BY_SHORTCUT.md", "Advanced agentic workflow shortcuts", {"vcb.shortcut.parallel_cloud_sprawl", "vcb.shortcut.conflicting_parallel_agents", "vcb.shortcut.unattended_cloud_delegation"}),
        ("indexes/PROMPT_LIBRARY.md", "Cloud delegation prompt", {"vcb.shortcut.unattended_cloud_delegation", "vcb.shortcut.ambiguous_cloud_task", "vcb.shortcut.cloud_task_without_context", "vcb.shortcut.parallel_cloud_sprawl"}),
        ("indexes/PROMPT_LIBRARY.md", "Automation design prompt", {"vcb.shortcut.automation_spam", "vcb.shortcut.automation_mutation_without_review"}),
        ("indexes/PROMPT_LIBRARY.md", "Browser/GUI task prompt", {"vcb.shortcut.browser_clicking_without_repro", "vcb.shortcut.logged_in_browser_secrets"}),
    ]
    for rel, heading, ids in existing_semantic_requirements:
        sections = {h: b for h, b in markdown_h2_sections(read(ROOT / rel))}
        section_body = sections.get(heading, "")
        if not section_body.strip():
            errors.append(f"{rel} semantic section {heading!r} is empty while active Chunk 25 cards exist")
            continue
        if "→ active" not in section_body:
            errors.append(f"{rel} semantic section {heading!r} routes only to older/planned material while active Chunk 25 cards exist")
        for ident in ids:
            if f"`{ident}`" not in section_body:
                errors.append(f"{rel} semantic section {heading!r} missing active Chunk 25 route: {ident}")

    planned_alias_requirements = [
        ("vcb.shortcut.unbounded_cloud_delegation", "vcb.shortcut.unattended_cloud_delegation"),
        ("vcb.shortcut.parallel_conflict", "vcb.shortcut.conflicting_parallel_agents"),
        ("vcb.shortcut.parallel_write_conflicts", "vcb.shortcut.conflicting_parallel_agents"),
        ("vcb.shortcut.browser_use_with_secrets", "vcb.shortcut.logged_in_browser_secrets"),
        ("vcb.shortcut.unattended_gui_work", "vcb.shortcut.browser_clicking_without_repro"),
        ("vcb.shortcut.screenshot_only_verification", "vcb.shortcut.browser_clicking_without_repro"),
    ]
    for rel in CHUNK_25_REQUIRED_INDEXES + ["SHORTCUT_REGISTER.md"]:
        body = read(ROOT / rel)
        for planned, active in planned_alias_requirements:
            if f"`{planned}`" in body:
                planned_pos = body.find(f"`{planned}`")
                active_pos = body.find(f"`{active}`")
                if active_pos < 0 or active_pos > planned_pos:
                    errors.append(f"{rel} planned near-duplicate route {planned} must show active replacement {active} first")

    shortcut_sections = {h: b for h, b in markdown_h2_sections(read(ROOT / "indexes/INDEX_BY_SHORTCUT.md"))}
    verification_shortcuts = shortcut_sections.get("Verification shortcuts", "")
    planned = "vcb.shortcut.screenshot_only_verification"
    active = "vcb.shortcut.browser_clicking_without_repro"
    planned_token = f"`{planned}`"
    active_token = f"`{active}`"
    if not verification_shortcuts.strip():
        errors.append("indexes/INDEX_BY_SHORTCUT.md missing semantic section: Verification shortcuts")
    elif planned_token in verification_shortcuts:
        planned_pos = verification_shortcuts.find(planned_token)
        active_pos = verification_shortcuts.find(active_token)
        chapter_pos_candidates = [pos for pos in [verification_shortcuts.find("`vcb.chapter.")] if pos >= 0]
        first_chapter_pos = min(chapter_pos_candidates) if chapter_pos_candidates else -1
        if active_pos < 0:
            errors.append("indexes/INDEX_BY_SHORTCUT.md Verification shortcuts lists screenshot_only_verification without active browser_clicking_without_repro replacement")
        elif active_pos > planned_pos:
            errors.append("indexes/INDEX_BY_SHORTCUT.md Verification shortcuts must show active browser_clicking_without_repro before planned screenshot_only_verification")
        elif first_chapter_pos >= 0 and active_pos > first_chapter_pos:
            errors.append("indexes/INDEX_BY_SHORTCUT.md Verification shortcuts must show active browser_clicking_without_repro before chapter fallback routes")

    active_vcb_ids = authored_active_ids()
    for ident, rel in required.items():
        path = ROOT / rel
        fm = parse_frontmatter(path) or {}
        body = read(path)
        fm_related = set(str(value) for value in (fm.get("related_topics") or []) if str(value).startswith("vcb."))
        body_related = set()
        related_match = re.search(r"(?ms)^## Related Topics\n(.*?)(?=^## |^<!-- VCB:STOP_RETRIEVAL|\\Z)", body)
        if related_match:
            body_related.update(re.findall(r"`?(vcb\.[A-Za-z0-9_.-]+)`?", related_match.group(1)))
        unresolved = sorted((fm_related | body_related) - active_vcb_ids)
        if unresolved:
            errors.append(f"{rel} has unresolved related_topics IDs: {unresolved}")

    changelog_text = read(ROOT / "CHANGELOG.md")
    chunk25_headings = re.findall(r"^## .*Chunk 25.*$", changelog_text, flags=re.M)
    if len(chunk25_headings) != 1:
        errors.append(f"CHANGELOG.md must contain exactly one Chunk 25 heading; observed={chunk25_headings}")
    combined_claims = (read(ROOT / "CHUNK_25_REPORT.md") if (ROOT / "CHUNK_25_REPORT.md").exists() else "") + "\n" + read(ROOT / "CHANGELOG.md")
    for label, rel in {
        "PROMPT_LIBRARY.md": "indexes/PROMPT_LIBRARY.md", "INDEX_FOR_AI_COACHES.md": "indexes/INDEX_FOR_AI_COACHES.md", "INDEX_BY_SHORTCUT.md": "indexes/INDEX_BY_SHORTCUT.md", "INDEX_BY_TASK.md": "indexes/INDEX_BY_TASK.md", "INDEX_BY_FAILURE_MODE.md": "indexes/INDEX_BY_FAILURE_MODE.md", "INDEX_BY_BUDGET_PROFILE.md": "indexes/INDEX_BY_BUDGET_PROFILE.md", "INDEX_BY_RISK_LEVEL.md": "indexes/INDEX_BY_RISK_LEVEL.md", "INDEX_BY_RECOVERABILITY.md": "indexes/INDEX_BY_RECOVERABILITY.md", "INDEX_BY_CONCEPT.md": "indexes/INDEX_BY_CONCEPT.md", "INDEX_BY_STABILITY.md": "indexes/INDEX_BY_STABILITY.md", "INDEX_BY_PROJECT_TYPE.md": "indexes/INDEX_BY_PROJECT_TYPE.md", "INDEX_BY_CODEX_SURFACE.md": "indexes/INDEX_BY_CODEX_SURFACE.md", "INDEX_BY_TOOL_CATEGORY.md": "indexes/INDEX_BY_TOOL_CATEGORY.md", "GLOSSARY.md": "indexes/GLOSSARY.md"
    }.items():
        if label in combined_claims and not any(f"`{ident}`" in read(ROOT / rel) for ident in required):
            errors.append(f"Chunk 25 report/changelog claims {label} routing, but the file has no Chunk 25 shortcut routes")


def validate_chunk_25_report_inventory(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_25":
        return
    path = ROOT / "CHUNK_25_REPORT.md"
    if not path.exists():
        errors.append("CHUNK_25_REPORT.md missing for active Chunk 25")
        return
    text = read(path)
    required_created = set(CHUNK_25_SHORTCUT_IDS.values()) | {"CHUNK_25_REPORT.md"}
    required_updated = {"README.md", "manifest.json", "llms.txt", "llms-full.txt", "SHORTCUT_REGISTER.md", "SOURCE_REGISTER.md", "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", *CHUNK_25_REQUIRED_INDEXES}
    for rel in sorted(required_created | required_updated):
        if f"`{rel}`" not in text:
            errors.append(f"CHUNK_25_REPORT.md file inventory omits required Chunk 25 path: {rel}")
    if "## Recommended Next Chunk" not in text:
        errors.append("CHUNK_25_REPORT.md missing recommended next chunk section")
    if "## Unresolved questions" not in text or "None." not in text:
        errors.append("CHUNK_25_REPORT.md must explicitly state unresolved questions")
    claims = extract_machine_report_claims(text)
    if not claims:
        errors.append("CHUNK_25_REPORT.md missing validation claims block")
    missing = sorted(CHUNK_25_REPORT_REQUIRED_CLAIMS - claims)
    if missing:
        errors.append(f"CHUNK_25_REPORT.md missing implemented validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_25_REPORT_REQUIRED_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_25_REPORT.md has unsupported validation claims: {unsupported}")


CHUNK_26_REPORT_REQUIRED_CLAIMS = {
    "Chunk 26 repository-contract cleanup scope is active: passed",
    "README and manifest identify Chunk 26 cleanup and block Chunk 27 until editor scope: passed",
    "Glossary limitation/bias terms route to active atomic shortcut/failure cards: passed",
    "Shortcut alias/deprecation register policy covers manifest shortcut redirects to active cards: passed",
    "Deprecation-register reserved redirect rows are non-self and manifest-backed: passed",
    "Active routing surfaces show canonical active shortcut replacements before redirected planned aliases: passed",
    "Active chapter/topic metadata avoids redirected shortcut aliases for the hardened alias set: passed",
    "LLM maps expose current Chunk 26 repository-contract cleanup routing: passed",
    "Chunk 26 did not add topic-card, tool-card, field-practice, pricing, broad workflow, broad shortcut, or narrative-chapter expansion: passed",
    "CHANGELOG.md has one current-chunk heading for Chunk 26: passed",
    "Active Chunk 26 report inventory lists created and updated repository-contract files: passed",
    "Active Chunk 26 machine-claim catalog matches validator checks: passed",
}


def manifest_shortcut_alias_redirects_to_active(manifest: dict[str, Any]) -> dict[str, str]:
    """Return shortcut redirect aliases whose canonical target is an authored active shortcut card."""
    redirects = manifest.get("topic_namespace_policy", {}).get("topic_id_redirects", {})
    active_ids = authored_active_ids()
    if not isinstance(redirects, dict):
        return {}
    return {
        str(alias): str(target)
        for alias, target in redirects.items()
        if str(alias).startswith("vcb.shortcut.")
        and str(target).startswith("vcb.shortcut.")
        and alias != target
        and str(target) in active_ids
    }




def markdown_table_id_rows(section: str) -> list[tuple[str, str, str]]:
    """Return first two backtick IDs from Markdown table rows."""
    rows: list[tuple[str, str, str]] = []
    for line in section.splitlines():
        stripped = line.strip()
        if not stripped.startswith("|") or "`" not in stripped:
            continue
        if re.fullmatch(r"\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?", stripped):
            continue
        ids = re.findall(r"`([^`]+)`", stripped)
        if len(ids) >= 2:
            rows.append((ids[0], ids[1], stripped))
    return rows


def validate_chunk_26_deprecation_reserved_redirects(
    manifest: dict[str, Any], deprecation_text: str, errors: list[str]
) -> None:
    """Reject no-op deprecation rows and ensure reserved redirects match manifest metadata."""
    redirects = manifest.get("topic_namespace_policy", {}).get("topic_id_redirects", {})
    if not isinstance(redirects, dict):
        errors.append("manifest.topic_namespace_policy.topic_id_redirects must be a mapping for Chunk 26 deprecation validation")
        return

    for old_id, replacement_id, _line in markdown_table_id_rows(deprecation_text):
        if old_id == replacement_id:
            errors.append(f"DEPRECATION_REGISTER.md contains a self-redirect row: {old_id} -> {replacement_id}")

    reserved = {h: b for h, b in markdown_h2_sections(deprecation_text)}.get("Reserved Redirects From Chunk 0 Namespace Cleanup", "")
    if not reserved.strip():
        errors.append("DEPRECATION_REGISTER.md missing Reserved Redirects From Chunk 0 Namespace Cleanup section")
        return
    reserved_rows = markdown_table_id_rows(reserved)
    if not reserved_rows:
        errors.append("DEPRECATION_REGISTER.md reserved redirect section has no manifest-backed rows")

    required_reserved_redirects = {
        "vcb.shortcuts.skipping_tests": "vcb.shortcut.skipping_tests",
        "vcb.shortcuts.broad_agent_permissions": "vcb.shortcut.broad_agent_permissions",
        "vcb.shortcuts.unattended_long_runs": "vcb.shortcut.unattended_long_runs",
        "vcb.workflow.subagents": "vcb.codex.subagents",
        "vcb.security.secrets": "vcb.safety.secrets",
        "vcb.dependencies.no_new_deps": "vcb.workflow.dependency_decisions",
        "vcb.review.diff_review": "vcb.workflow.reviewing_diffs",
        "vcb.git.small_diffs": "vcb.workflow.reviewing_diffs",
        "vcb.testing.regression_tests": "vcb.workflow.testing",
    }
    observed = {old_id: replacement_id for old_id, replacement_id, _line in reserved_rows}
    for old_id, expected_replacement in sorted(required_reserved_redirects.items()):
        if observed.get(old_id) != expected_replacement:
            errors.append(
                "DEPRECATION_REGISTER.md reserved redirect table missing required manifest-backed row: "
                f"{old_id} -> {expected_replacement}"
            )

    for old_id, replacement_id, _line in reserved_rows:
        manifest_replacement = redirects.get(old_id)
        if manifest_replacement is None:
            errors.append(f"DEPRECATION_REGISTER.md reserved redirect row is not backed by manifest: {old_id} -> {replacement_id}")
        elif str(manifest_replacement) != replacement_id:
            errors.append(
                "DEPRECATION_REGISTER.md reserved redirect row contradicts manifest: "
                f"{old_id} -> {replacement_id}, manifest has {manifest_replacement}"
            )

def validate_chunk_26_repository_contract_cleanup(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_26":
        return

    readme_sections = {h: b for h, b in markdown_h2_sections(read(ROOT / "README.md"))}
    readme_text = read(ROOT / "README.md")
    readme_next = readme_sections.get("Next Chunk", "")
    manifest_next_id = str(manifest.get("next_recommended_chunk", {}).get("id", ""))
    if "chunk_26_editor_scoped_next_slice" not in readme_text:
        errors.append("README.md does not identify Chunk 26 cleanup as the current chunk")
    for term in ["repository-contract cleanup", "glossary route hardening", "planned-alias/deprecation policy cleanup", "no new topic-card expansion"]:
        if term not in readme_text:
            errors.append(f"README.md Chunk 26 scope/non-scope text is missing required term: {term}")
    if manifest_next_id and f"`{manifest_next_id}`" not in readme_next:
        errors.append("README.md Next Chunk section does not name manifest.next_recommended_chunk.id for Chunk 26")
    if "Blocked until the editor sets the exact bounded Chunk 27 scope" not in readme_next:
        errors.append("README.md Next Chunk section must block Chunk 27 until editor-scoped approval")
    if any(stale in readme_next for stale in ["parallel/cloud/automation", "multi-AI/model-bias", "remaining shortcut-card slices"]):
        errors.append("README.md Next Chunk section contains stale content-expansion scope after Chunk 26 cleanup")

    if manifest.get("active_chunk", {}).get("id") != "chunk_26_editor_scoped_next_slice":
        errors.append("manifest.active_chunk.id must be chunk_26_editor_scoped_next_slice")
    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 26", "repository-contract cleanup", "glossary", "alias"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 26 term: {term}")

    expected_topic_counts = {
        "topics/shortcuts": 50,
        "topics/tool-catalog": 0,
        "topics/field-practices": 0,
    }
    for rel, expected in expected_topic_counts.items():
        observed = len([p for p in (ROOT / rel).glob("*.md")]) if (ROOT / rel).exists() else 0
        if observed != expected:
            errors.append(f"Chunk 26 scope drift in {rel}: observed {observed}, expected {expected}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md")]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 26 must not expand pricing snapshots: {pricing_files}")

    glossary = read(ROOT / "indexes/GLOSSARY.md")
    limitation = {h: b for h, b in markdown_h2_sections(glossary)}.get("Limitation and bias terms", "")
    required_glossary_routes = {
        "vcb.shortcut.trusting_estimates_before_inspection",
        "vcb.shortcut.ignoring_model_biases",
        "vcb.shortcut.consensus_as_correctness",
        "vcb.shortcut.best_of_n_without_review",
        "vcb.shortcut.cherry_picking_ai_answers",
        "vcb.failure.done_claim_without_evidence",
        "vcb.failure.hallucinated_apis",
    }
    if not limitation.strip():
        errors.append("indexes/GLOSSARY.md missing Limitation and bias terms section")
    for ident in required_glossary_routes:
        if f"`{ident}`" not in limitation:
            errors.append(f"indexes/GLOSSARY.md Limitation and bias terms missing active route: {ident}")
    alias_glossary = {h: b for h, b in markdown_h2_sections(glossary)}.get("Shortcut alias and redirected planned-route terms", "")
    for ident in ["vcb.shortcut.default_config_forever", "vcb.shortcut.many_ais_same_files", "vcb.shortcut.parallel_agents_edit_same_files", "vcb.shortcut.browser_clicking_without_repro"]:
        if f"`{ident}`" not in alias_glossary:
            errors.append(f"indexes/GLOSSARY.md alias section missing active canonical route: {ident}")

    aliases = manifest_shortcut_alias_redirects_to_active(manifest)
    if not aliases:
        errors.append("Chunk 26 expected manifest shortcut alias redirects to active shortcut cards, but none were found")
    register_text = read(ROOT / "SHORTCUT_REGISTER.md")
    deprecation_text = read(ROOT / "DEPRECATION_REGISTER.md")
    validate_chunk_26_deprecation_reserved_redirects(manifest, deprecation_text, errors)
    if "## Redirected Planned Aliases for Active Shortcut Cards" not in register_text:
        errors.append("SHORTCUT_REGISTER.md missing redirected planned alias policy section")
    if "## Shortcut Alias Redirects Hardened in Chunk 26" not in deprecation_text:
        errors.append("DEPRECATION_REGISTER.md missing Chunk 26 shortcut alias redirect section")
    for alias, active in sorted(aliases.items()):
        if f"`{alias}`" not in deprecation_text or f"`{active}`" not in deprecation_text:
            errors.append(f"DEPRECATION_REGISTER.md missing shortcut alias redirect row: {alias} -> {active}")
        if f"`{alias}`" in register_text:
            alias_pos = register_text.find(f"`{alias}`")
            active_pos = register_text.find(f"`{active}`")
            if active_pos < 0 or active_pos > alias_pos:
                errors.append(f"SHORTCUT_REGISTER.md must show active replacement {active} before redirected/planned alias {alias}")

    routing_surfaces = [
        ROOT / "indexes" / "GLOSSARY.md",
        ROOT / "indexes" / "INDEX_BY_SHORTCUT.md",
        ROOT / "llms.txt",
        ROOT / "llms-full.txt",
    ]
    for path in routing_surfaces:
        body = read(path)
        for alias, active in sorted(aliases.items()):
            if f"`{alias}`" in body:
                alias_pos = body.find(f"`{alias}`")
                active_pos = body.find(f"`{active}`")
                if active_pos < 0 or active_pos > alias_pos:
                    errors.append(f"{path.relative_to(ROOT)} must show active replacement {active} before redirected/planned alias {alias}")

    shortcut_sections = {h: b for h, b in markdown_h2_sections(read(ROOT / "indexes" / "INDEX_BY_SHORTCUT.md"))}
    section_expectations = [
        ("Persistent guidance and tool shortcuts", "vcb.shortcut.using_global_config_for_everything", "vcb.shortcut.default_config_forever"),
        ("Advanced agentic workflow shortcuts", "vcb.shortcut.parallel_agents_same_files", "vcb.shortcut.many_ais_same_files"),
        ("Advanced agentic workflow shortcuts", "vcb.shortcut.parallel_tasks_same_files", "vcb.shortcut.parallel_agents_edit_same_files"),
        ("Verification shortcuts", "vcb.shortcut.screenshot_only_verification", "vcb.shortcut.browser_clicking_without_repro"),
    ]
    for heading, alias, active in section_expectations:
        section = shortcut_sections.get(heading, "")
        if not section.strip():
            errors.append(f"indexes/INDEX_BY_SHORTCUT.md missing semantic section: {heading}")
            continue
        if f"`{alias}`" in section:
            alias_pos = section.find(f"`{alias}`")
            active_pos = section.find(f"`{active}`")
            if active_pos < 0 or active_pos > alias_pos:
                errors.append(f"INDEX_BY_SHORTCUT.md section {heading!r} must show active {active} before alias {alias}")

    # Active chapter/topic metadata should not carry redirected shortcut aliases once an active canonical route exists.
    metadata_fields = {"shortcut_profiles", "related_topics"}
    for path in active_topic_files():
        fm = parse_frontmatter(path) or {}
        for field in metadata_fields:
            values = fm.get(field) or []
            if not isinstance(values, list):
                continue
            for value in values:
                if str(value) in aliases:
                    errors.append(
                        f"{path.relative_to(ROOT)} frontmatter {field} uses redirected shortcut alias {value}; "
                        f"use {aliases[str(value)]}"
                    )

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        phrase = "Repository-contract cleanup from Chunk 26 is active: glossary bias routes and planned-alias/deprecation routes are hardened."
        if body.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 26 cleanup phrase; observed={body.count(phrase)}")
        fast = {h: b for h, b in markdown_h2_sections(body)}.get("Repository-Contract Cleanup Fast Routing", "")
        for term in ["glossary", "planned shortcut alias", "DEPRECATION_REGISTER.md", "SHORTCUT_REGISTER.md", "vcb.shortcut.using_global_config_for_everything", "vcb.shortcut.screenshot_only_verification"]:
            if term not in fast:
                errors.append(f"{rel} Repository-Contract Cleanup Fast Routing missing term: {term}")

    changelog_text = read(ROOT / "CHANGELOG.md")
    chunk26_headings = re.findall(r"^## .*Chunk 26.*$", changelog_text, flags=re.M)
    if len(chunk26_headings) != 1:
        errors.append(f"CHANGELOG.md must contain exactly one Chunk 26 heading; observed={chunk26_headings}")

    path = ROOT / "CHUNK_26_REPORT.md"
    if not path.exists():
        errors.append("CHUNK_26_REPORT.md missing for active Chunk 26")
        return
    report_text = read(path)
    required_inventory = {
        "CHUNK_26_REPORT.md", "README.md", "manifest.json", "llms.txt", "llms-full.txt",
        "SHORTCUT_REGISTER.md", "DEPRECATION_REGISTER.md", "CHANGELOG.md", "TREE.txt",
        "indexes/GLOSSARY.md", "indexes/INDEX_BY_SHORTCUT.md", "scripts/validate_repository.py",
        "chapters/19-codex-config.md", "chapters/27-cloud-delegation-parallel-work.md", "chapters/30-computer-use-browser-gui-tasks.md",
        "topics/codex/app.md", "topics/codex/cloud.md", "topics/codex/config.md", "topics/codex/computer-use.md", "topics/codex/subagents.md",
        "topics/failure-modes/ui-taste-gap.md", "topics/workflows/frontend-work.md", "topics/workflows/visual-qa.md",
    }
    for rel in sorted(required_inventory):
        if f"`{rel}`" not in report_text:
            errors.append(f"CHUNK_26_REPORT.md file inventory omits required Chunk 26 path: {rel}")
    claims = extract_machine_report_claims(report_text)
    if not claims:
        errors.append("CHUNK_26_REPORT.md missing validation claims block")
    missing = sorted(CHUNK_26_REPORT_REQUIRED_CLAIMS - claims)
    if missing:
        errors.append(f"CHUNK_26_REPORT.md missing implemented validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_26_REPORT_REQUIRED_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_26_REPORT.md has unsupported validation claims: {unsupported}")


def validate_chunk_14_report_claims(manifest: dict[str, Any], report: Path, errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_14":
        return
    if not report.exists():
        return
    text = read(report)
    required_claims = {
        "README and manifest next-chunk IDs match exactly: passed",
        "Index/register VCB begin-marker versions match frontmatter versions: passed",
        "Duplicate Codex feature full-list sections removed from primary indexes: passed",
        "Active Chunk 14 machine-claim catalog matches validator checks: passed",
        "Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed",
    }
    claims = extract_machine_report_claims(text)
    if not claims:
        errors.append("CHUNK_14_REPORT.md missing ### Machine-enforced checks claim block")
        return
    missing = sorted(required_claims - claims)
    if missing:
        errors.append(f"CHUNK_14_REPORT.md missing required machine-enforced validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_14_MACHINE_REPORT_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_14_REPORT.md has unsupported machine-enforced validation claims: {unsupported}")
    if "Active Chunk 14 validation claims are enforced by validator checks: passed" in text:
        errors.append(
            "CHUNK_14_REPORT.md uses overbroad validation-claim wording; "
            "use the machine-claim catalog wording instead"
        )



CHUNK_15_MACHINE_REPORT_CLAIMS = {
    "Manifest source-file inventory matches actual package files: passed",
    "Manifest source_artifacts inventory matches actual package files: passed",
    "Manifest all_tracked_files matches source_files and actual package files: passed",
    "Canonical review package references are consistent across manifest fields: passed",
    "New workflow/prompting topic files created in Chunk 15: passed",
    "Required Chunk 15 workflow/prompting-card slice present: passed",
        "Manifest workflow_prompting_cards map matches authored Chunk 15 files: passed",
        "Manifest chunk_15_required_topic_ids matches authored Chunk 15 IDs: passed",
    "Required topic sections present: passed",
    "Required VCB markers present in new workflow/prompting files: passed",
    "llms.txt / llms-full.txt source-map versions match current chunk: passed",
    "README root frontmatter status matches current chunk: passed",
    "README body current chunk matches manifest current chunk: passed",
    "README and manifest next-chunk IDs match exactly: passed",
    "Index/register VCB begin-marker versions match frontmatter versions: passed",
    "Duplicate workflow/prompting full-list sections removed from primary indexes: passed",
    "Active Chunk 15 machine-claim catalog matches validator checks: passed",
    "Manifest editor_gate approval_applied matches current chunk transition: passed",
    "Current chunk report chunk_id matches manifest active chunk: passed",
    "Root governance metadata drift scan: passed",
    "Index namespace drift scan covers active and planned index routes: passed",
    "Active index routes point to authored active IDs: passed",
    "Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed",
    "Index shortcut routes resolve to SHORTCUT_REGISTER: passed",
    "Index tool IDs resolve to TOOL_REGISTER: passed",
    "Evidence source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed",
    "source_status.official_openai matches Evidence and Sources sections: passed",
    "source_status.official_vendor matches Evidence and Sources sections: passed",
    "Duplicate source URL detection: passed",
    "Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed",
    "Report final line is AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW: passed",
}


def validate_chunk_15_report_claims(manifest: dict[str, Any], report: Path, errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_15":
        return
    if not report.exists():
        return
    text = read(report)
    required_claims = {
        "New workflow/prompting topic files created in Chunk 15: passed",
        "Required Chunk 15 workflow/prompting-card slice present: passed",
        "Manifest workflow_prompting_cards map matches authored Chunk 15 files: passed",
        "Manifest chunk_15_required_topic_ids matches authored Chunk 15 IDs: passed",
        "README and manifest next-chunk IDs match exactly: passed",
        "Index/register VCB begin-marker versions match frontmatter versions: passed",
        "Duplicate workflow/prompting full-list sections removed from primary indexes: passed",
        "Active Chunk 15 machine-claim catalog matches validator checks: passed",
        "Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed",
    }
    claims = extract_machine_report_claims(text)
    if not claims:
        errors.append("CHUNK_15_REPORT.md missing ### Machine-enforced checks claim block")
        return
    missing = sorted(required_claims - claims)
    if missing:
        errors.append(f"CHUNK_15_REPORT.md missing required machine-enforced validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_15_MACHINE_REPORT_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_15_REPORT.md has unsupported machine-enforced validation claims: {unsupported}")


CHUNK_16_MACHINE_REPORT_CLAIMS = {
    "Manifest source-file inventory matches actual package files: passed",
    "Manifest source_artifacts inventory matches actual package files: passed",
    "Manifest all_tracked_files matches source_files and actual package files: passed",
    "Canonical review package references are consistent across manifest fields: passed",
    "New review/safety workflow topic files created in Chunk 16: passed",
    "Required Chunk 16 review/safety workflow-card slice present: passed",
    "Manifest review_safety_workflow_cards map matches authored Chunk 16 files: passed",
    "Manifest chunk_16_required_topic_ids matches authored Chunk 16 IDs: passed",
    "Required topic sections present: passed",
    "Required VCB markers present in new review/safety workflow files: passed",
    "llms.txt / llms-full.txt source-map versions match current chunk: passed",
    "README root frontmatter status matches current chunk: passed",
    "README body current chunk matches manifest current chunk: passed",
    "README and manifest next-chunk IDs match exactly: passed",
    "Index/register VCB begin-marker versions match frontmatter versions: passed",
    "Index files include STOP_RETRIEVAL and matching END_INDEX markers: passed",
    "VCB begin/end marker pairs exist across Markdown artifacts: passed",
    "SOURCE_REGISTER source rows are inside declared Source ID tables: passed",
    "Duplicate review/safety full-list sections removed from primary indexes: passed",
    "Active Chunk 16 machine-claim catalog matches validator checks: passed",
    "Manifest editor_gate approval_applied matches current chunk transition: passed",
    "Current chunk report chunk_id matches manifest active chunk: passed",
    "Root governance metadata drift scan: passed",
    "Index namespace drift scan covers active and planned index routes: passed",
    "Active index routes point to authored active IDs: passed",
    "Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed",
    "Index shortcut routes resolve to SHORTCUT_REGISTER: passed",
    "Index tool IDs resolve to TOOL_REGISTER: passed",
    "Evidence source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed",
    "source_status.official_openai matches Evidence and Sources sections: passed",
    "source_status.official_vendor matches Evidence and Sources sections: passed",
    "Duplicate source URL detection: passed",
    "Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed",
    "Report final line is AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW: passed",
}


def validate_chunk_16_report_claims(manifest: dict[str, Any], report: Path, errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_16":
        return
    if not report.exists():
        return
    text = read(report)
    required_claims = {
        "New review/safety workflow topic files created in Chunk 16: passed",
        "Required Chunk 16 review/safety workflow-card slice present: passed",
        "Manifest review_safety_workflow_cards map matches authored Chunk 16 files: passed",
        "Manifest chunk_16_required_topic_ids matches authored Chunk 16 IDs: passed",
        "README and manifest next-chunk IDs match exactly: passed",
        "Index/register VCB begin-marker versions match frontmatter versions: passed",
    "Index files include STOP_RETRIEVAL and matching END_INDEX markers: passed",
    "VCB begin/end marker pairs exist across Markdown artifacts: passed",
    "SOURCE_REGISTER source rows are inside declared Source ID tables: passed",
        "Duplicate review/safety full-list sections removed from primary indexes: passed",
        "Active Chunk 16 machine-claim catalog matches validator checks: passed",
        "Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed",
    }
    claims = extract_machine_report_claims(text)
    if not claims:
        errors.append("CHUNK_16_REPORT.md missing ### Machine-enforced checks claim block")
        return
    missing = sorted(required_claims - claims)
    if missing:
        errors.append(f"CHUNK_16_REPORT.md missing required machine-enforced validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_16_MACHINE_REPORT_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_16_REPORT.md has unsupported machine-enforced validation claims: {unsupported}")


CHUNK_17_FRONTEND_REFACTOR_DEPENDENCY_IDS = {
    "vcb.workflow.frontend_work": "topics/workflows/frontend-work.md",
    "vcb.workflow.visual_qa": "topics/workflows/visual-qa.md",
    "vcb.workflow.accessibility_review": "topics/workflows/accessibility-review.md",
    "vcb.workflow.refactoring": "topics/workflows/refactoring.md",
    "vcb.workflow.dependency_decisions": "topics/workflows/dependency-decisions.md",
    "vcb.workflow.dependency_update_review": "topics/workflows/dependency-update-review.md",
    "vcb.workflow.release_notes": "topics/workflows/release-notes.md",
    "vcb.workflow.documentation_updates": "topics/workflows/documentation-updates.md",
}

FRONTEND_REFACTOR_DEPENDENCY_WORKFLOW_IDS = set(CHUNK_17_FRONTEND_REFACTOR_DEPENDENCY_IDS)


def validate_duplicate_frontend_refactor_dependency_full_list_sections(errors: list[str]) -> None:
    """Reject repeated full Chunk 17 frontend/refactor/dependency/docs blocks inside one index."""
    for path in sorted((ROOT / "indexes").glob("*.md")):
        full_sections: list[str] = []
        for heading, body in markdown_h2_sections(read(path)):
            ids = set(re.findall(r"`(vcb\.workflow\.[A-Za-z0-9_.-]+)`", body))
            if FRONTEND_REFACTOR_DEPENDENCY_WORKFLOW_IDS.issubset(ids):
                full_sections.append(heading)
        if len(full_sections) > 1:
            errors.append(
                f"duplicate full frontend/refactor/dependency workflow routing sections in {path.relative_to(ROOT)}: {full_sections}"
            )


def validate_chunk_17_frontend_refactor_dependency_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    current = manifest.get("chunk_gate", {}).get("current_chunk", "")
    if current != "chunk_17":
        return
    active = authored_active_ids()
    manifest_required = set(manifest.get("chunk_17_required_topic_ids", []) or [])
    if manifest_required != set(CHUNK_17_FRONTEND_REFACTOR_DEPENDENCY_IDS):
        errors.append(
            "manifest.chunk_17_required_topic_ids mismatch: "
            f"expected={sorted(CHUNK_17_FRONTEND_REFACTOR_DEPENDENCY_IDS)} observed={sorted(manifest_required)}"
        )
    manifest_cards = manifest.get("frontend_refactor_dependency_workflow_cards", {})
    if not isinstance(manifest_cards, dict):
        errors.append("manifest.frontend_refactor_dependency_workflow_cards must be a mapping for Chunk 17")
        manifest_cards = {}
    if manifest_cards != CHUNK_17_FRONTEND_REFACTOR_DEPENDENCY_IDS:
        errors.append(
            "manifest.frontend_refactor_dependency_workflow_cards does not match Chunk 17 required card map: "
            f"observed={manifest_cards!r}"
        )
    for ident, rel in CHUNK_17_FRONTEND_REFACTOR_DEPENDENCY_IDS.items():
        if ident not in active:
            errors.append(f"Chunk 17 required frontend/refactor/dependency workflow ID not authored: {ident}")
        if not (ROOT / rel).exists():
            errors.append(f"Chunk 17 required frontend/refactor/dependency workflow file missing: {rel}")

    allowed_prompting = {Path(p).name for p in CHUNK_15_WORKFLOW_PROMPTING_IDS.values() if p.startswith("topics/prompting/")}
    allowed_workflows = {Path(p).name for p in CHUNK_15_WORKFLOW_PROMPTING_IDS.values() if p.startswith("topics/workflows/")}
    allowed_workflows |= {Path(p).name for p in CHUNK_16_REVIEW_SAFETY_IDS.values() if p.startswith("topics/workflows/")}
    allowed_workflows |= {Path(p).name for p in CHUNK_17_FRONTEND_REFACTOR_DEPENDENCY_IDS.values() if p.startswith("topics/workflows/")}
    allowed_safety = {Path(p).name for p in CHUNK_16_REVIEW_SAFETY_IDS.values() if p.startswith("topics/safety/")}
    observed_prompting = {p.name for p in (ROOT / "topics" / "prompting").glob("*.md") if p.name != ".gitkeep"}
    observed_workflows = {p.name for p in (ROOT / "topics" / "workflows").glob("*.md") if p.name != ".gitkeep"}
    observed_safety = {p.name for p in (ROOT / "topics" / "safety").glob("*.md") if p.name != ".gitkeep"}
    if observed_prompting != allowed_prompting:
        errors.append(f"Chunk 17 must not alter prompting-card scope: expected={sorted(allowed_prompting)} observed={sorted(observed_prompting)}")
    if observed_workflows != allowed_workflows:
        errors.append(f"Chunk 17 workflow-card scope drift: expected={sorted(allowed_workflows)} observed={sorted(observed_workflows)}")
    if observed_safety != allowed_safety:
        errors.append(f"Chunk 17 must not alter safety-card scope: expected={sorted(allowed_safety)} observed={sorted(observed_safety)}")
    for disallowed in ["topics/tool-catalog", "topics/shortcuts", "topics/field-practices"]:
        files = sorted(p.name for p in (ROOT / disallowed).glob("*.md") if p.name != ".gitkeep")
        if files:
            errors.append(f"Chunk 17 must not add {disallowed} topic cards: {files}")
    pricing_files = sorted(p.name for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep")
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 17 must not expand pricing snapshots: {pricing_files}")

    index_files = [
        ROOT / "indexes" / "INDEX_BY_TASK.md",
        ROOT / "indexes" / "INDEX_BY_CONCEPT.md",
        ROOT / "indexes" / "INDEX_BY_FAILURE_MODE.md",
        ROOT / "indexes" / "INDEX_BY_RISK_LEVEL.md",
        ROOT / "indexes" / "INDEX_BY_RECOVERABILITY.md",
        ROOT / "indexes" / "INDEX_BY_BUDGET_PROFILE.md",
        ROOT / "indexes" / "INDEX_BY_PROJECT_TYPE.md",
        ROOT / "indexes" / "INDEX_FOR_AI_COACHES.md",
        ROOT / "indexes" / "PROMPT_LIBRARY.md",
    ]
    combined = "\n".join(read(p) for p in index_files)
    llm_maps = read(ROOT / "llms.txt") + "\n" + read(ROOT / "llms-full.txt")
    for ident in CHUNK_17_FRONTEND_REFACTOR_DEPENDENCY_IDS:
        if f"`{ident}` → active" not in combined and f"`{ident}` → active:" not in combined:
            errors.append(f"primary indexes missing active route for Chunk 17 frontend/refactor/dependency workflow topic: {ident}")
        if ident not in llm_maps:
            errors.append(f"llms maps missing route for Chunk 17 frontend/refactor/dependency workflow topic: {ident}")


CHUNK_17_MACHINE_REPORT_CLAIMS = {
    "Manifest source-file inventory matches actual package files: passed",
    "Manifest source_artifacts inventory matches actual package files: passed",
    "Manifest all_tracked_files matches source_files and actual package files: passed",
    "Canonical review package references are consistent across manifest fields: passed",
    "New frontend/refactor/dependency workflow topic files created in Chunk 17: passed",
    "Required Chunk 17 frontend/refactor/dependency workflow-card slice present: passed",
    "Manifest frontend_refactor_dependency_workflow_cards map matches authored Chunk 17 files: passed",
    "Manifest chunk_17_required_topic_ids matches authored Chunk 17 IDs: passed",
    "Required topic sections present: passed",
    "Required VCB markers present in new frontend/refactor/dependency workflow files: passed",
    "llms.txt / llms-full.txt source-map versions match current chunk: passed",
    "README root frontmatter status matches current chunk: passed",
    "README body current chunk matches manifest current chunk: passed",
    "README and manifest next-chunk IDs match exactly: passed",
    "Index/register VCB begin-marker versions match frontmatter versions: passed",
    "Index files include STOP_RETRIEVAL and matching END_INDEX markers: passed",
    "VCB begin/end marker pairs exist across Markdown artifacts: passed",
    "SOURCE_REGISTER source rows are inside declared Source ID tables: passed",
    "Duplicate frontend/refactor/dependency full-list sections removed from primary indexes: passed",
    "Manifest topic_namespace_policy and namespace_policy redirect maps match exactly: passed",
    "INDEX_BY_TASK routes active Chunk 17 cards through task-level sections: passed",
    "Stale documentation_update planned route is absent from indexes: passed",
    "Planned-route replacements do not shadow authored active Chunk 17 cards: passed",
    "Active Chunk 17 machine-claim catalog matches validator checks: passed",
    "Manifest editor_gate approval_applied matches current chunk transition: passed",
    "Current chunk report chunk_id matches manifest active chunk: passed",
    "Root governance metadata drift scan: passed",
    "Index namespace drift scan covers active and planned index routes: passed",
    "Active index routes point to authored active IDs: passed",
    "Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed",
    "Index shortcut routes resolve to SHORTCUT_REGISTER: passed",
    "Index tool IDs resolve to TOOL_REGISTER: passed",
    "Evidence source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed",
    "source_status.official_openai matches Evidence and Sources sections: passed",
    "source_status.official_vendor matches Evidence and Sources sections: passed",
    "Duplicate source URL detection: passed",
    "Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed",
    "Report final line is AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW: passed",
}


def validate_chunk_17_report_claims(manifest: dict[str, Any], report: Path, errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_17":
        return
    if not report.exists():
        return
    text = read(report)
    required_claims = {
        "New frontend/refactor/dependency workflow topic files created in Chunk 17: passed",
        "Required Chunk 17 frontend/refactor/dependency workflow-card slice present: passed",
        "Manifest frontend_refactor_dependency_workflow_cards map matches authored Chunk 17 files: passed",
        "Manifest chunk_17_required_topic_ids matches authored Chunk 17 IDs: passed",
        "README and manifest next-chunk IDs match exactly: passed",
        "Index/register VCB begin-marker versions match frontmatter versions: passed",
        "Index files include STOP_RETRIEVAL and matching END_INDEX markers: passed",
        "VCB begin/end marker pairs exist across Markdown artifacts: passed",
        "SOURCE_REGISTER source rows are inside declared Source ID tables: passed",
        "Duplicate frontend/refactor/dependency full-list sections removed from primary indexes: passed",
        "Manifest topic_namespace_policy and namespace_policy redirect maps match exactly: passed",
        "INDEX_BY_TASK routes active Chunk 17 cards through task-level sections: passed",
        "Stale documentation_update planned route is absent from indexes: passed",
        "Planned-route replacements do not shadow authored active Chunk 17 cards: passed",
        "Active Chunk 17 machine-claim catalog matches validator checks: passed",
        "Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed",
    }
    claims = extract_machine_report_claims(text)
    if not claims:
        errors.append("CHUNK_17_REPORT.md missing ### Machine-enforced checks claim block")
        return
    missing = sorted(required_claims - claims)
    if missing:
        errors.append(f"CHUNK_17_REPORT.md missing required machine-enforced validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_17_MACHINE_REPORT_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_17_REPORT.md has unsupported machine-enforced validation claims: {unsupported}")


CHUNK_18_FAILURE_MODE_IDS = {
    "vcb.failure.hallucinated_apis": "topics/failure-modes/hallucinated-apis.md",
    "vcb.failure.context_pollution": "topics/failure-modes/context-pollution.md",
    "vcb.failure.weakened_tests": "topics/failure-modes/weakened-tests.md",
    "vcb.failure.broad_refactor_drift": "topics/failure-modes/broad-refactor-drift.md",
    "vcb.failure.dependency_bloat": "topics/failure-modes/dependency-bloat.md",
    "vcb.failure.ui_taste_gap": "topics/failure-modes/ui-taste-gap.md",
    "vcb.failure.ci_false_confidence": "topics/failure-modes/ci-false-confidence.md",
    "vcb.failure.done_claim_without_evidence": "topics/failure-modes/done-claim-without-evidence.md",
}

CHUNK_18_TASK_ROUTE_REQUIREMENTS = {
    "Diagnose Codex work going wrong": set(CHUNK_18_FAILURE_MODE_IDS),
    "Prompt, plan, context, and done criteria": {"vcb.failure.context_pollution", "vcb.failure.done_claim_without_evidence"},
    "Write or update tests": {"vcb.failure.weakened_tests"},
    "Improve frontend UI": {"vcb.failure.ui_taste_gap"},
    "Refactor safely": {"vcb.failure.broad_refactor_drift"},
    "Choose dependencies, packages, or frameworks": {"vcb.failure.dependency_bloat"},
    "Run CI or non-interactive Codex": {"vcb.failure.ci_false_confidence"},
    "Add an API endpoint": {"vcb.failure.hallucinated_apis"},
    "Review Codex output or a PR": {"vcb.failure.hallucinated_apis", "vcb.failure.weakened_tests", "vcb.failure.broad_refactor_drift", "vcb.failure.done_claim_without_evidence"},
}

PLANNED_FAILURE_MODE_REPLACEMENTS = {
    "vcb.failure.done_claim_without_evidence": "vcb.failure.done_claim_without_evidence",
    "vcb.failure.summary_bias": "vcb.failure.done_claim_without_evidence",
    "vcb.failure.unreproduced_bug_fix": "vcb.failure.done_claim_without_evidence",
    "vcb.failure.hallucinated_apis": "vcb.failure.hallucinated_apis",
    "vcb.failure.context_pollution": "vcb.failure.context_pollution",
    "vcb.failure.weakened_tests": "vcb.failure.weakened_tests",
    "vcb.failure.broad_refactor_drift": "vcb.failure.broad_refactor_drift",
    "vcb.failure.dependency_bloat": "vcb.failure.dependency_bloat",
    "vcb.failure.ui_taste_gap": "vcb.failure.ui_taste_gap",
    "vcb.failure.ci_false_confidence": "vcb.failure.ci_false_confidence",
    "vcb.failure.silent_behavior_changes": "vcb.failure.broad_refactor_drift",
}

CHUNK_18_REQUIRED_ROUTE_SURFACES = {
    "indexes/PROMPT_LIBRARY.md": set(CHUNK_18_FAILURE_MODE_IDS),
    "indexes/INDEX_FOR_AI_COACHES.md": set(CHUNK_18_FAILURE_MODE_IDS),
    "indexes/INDEX_BY_STABILITY.md": set(CHUNK_18_FAILURE_MODE_IDS),
    "indexes/INDEX_BY_CONCEPT.md": set(CHUNK_18_FAILURE_MODE_IDS),
    "indexes/INDEX_BY_SHORTCUT.md": set(CHUNK_18_FAILURE_MODE_IDS),
}

CHUNK_18_FULL_LIST_SECTION_REQUIREMENTS = {
    "indexes/GLOSSARY.md": {"Failure-mode glossary entries": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/INDEX_BY_BUDGET_PROFILE.md": {"Budget-aware failure-mode controls": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/INDEX_BY_RECOVERABILITY.md": {"Failure modes by recoverability": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/INDEX_BY_RISK_LEVEL.md": {"High-risk AI-coding failure modes": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/INDEX_BY_FAILURE_MODE.md": {"Active Failure-Mode Topic Cards": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/INDEX_BY_TASK.md": {"Diagnose Codex work going wrong": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/PROMPT_LIBRARY.md": {"Failure-mode diagnosis prompt": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/INDEX_FOR_AI_COACHES.md": {"Human asks for failure-mode diagnosis or accepts vague done claims": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/INDEX_BY_STABILITY.md": {"Quarterly review — active failure-mode cards": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/INDEX_BY_CONCEPT.md": {"AI coding failure-mode concepts": set(CHUNK_18_FAILURE_MODE_IDS)},
    "indexes/INDEX_BY_SHORTCUT.md": {"Shortcut routes for active failure modes": set(CHUNK_18_FAILURE_MODE_IDS)},
}

CHUNK_18_ROUTING_SURFACE_FILES = {
    "indexes/PROMPT_LIBRARY.md",
    "indexes/INDEX_FOR_AI_COACHES.md",
    "indexes/INDEX_BY_STABILITY.md",
    "indexes/INDEX_BY_CONCEPT.md",
    "indexes/INDEX_BY_SHORTCUT.md",
    "indexes/GLOSSARY.md",
    "indexes/INDEX_BY_BUDGET_PROFILE.md",
    "indexes/INDEX_BY_RECOVERABILITY.md",
    "indexes/INDEX_BY_RISK_LEVEL.md",
    "indexes/INDEX_BY_TASK.md",
    "indexes/INDEX_BY_FAILURE_MODE.md",
}

FAILURE_MODE_ACTIVE_STATUS_PHRASE = "Failure-mode cards from Chunk 18 are active."

FAILURE_MODE_TOPIC_IDS = set(CHUNK_18_FAILURE_MODE_IDS)


FAILURE_MODE_INDEX_SEMANTIC_REQUIREMENTS = {
    "Codex summary sounds done but the diff says otherwise": {"vcb.failure.done_claim_without_evidence"},
    "Codex patches without reproducing the bug": {"vcb.failure.done_claim_without_evidence"},
    "Bad estimates and confident wrong summaries": {"vcb.failure.done_claim_without_evidence"},
}


def validate_chunk_18_failure_mode_index_semantics(manifest: dict[str, Any], errors: list[str]) -> None:
    """Ensure likely semantic lookup sections route to the active atomic failure card.

    Aggregate inventory is not enough. A reader who lands in a named failure-mode
    section should see the smallest active failure card for that diagnosis.
    """
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_18":
        return
    rel = "indexes/INDEX_BY_FAILURE_MODE.md"
    text = read(ROOT / rel)
    sections = {heading: body for heading, body in markdown_h2_sections(text)}
    for heading, required_ids in FAILURE_MODE_INDEX_SEMANTIC_REQUIREMENTS.items():
        body = sections.get(heading)
        if body is None:
            errors.append(f"{rel} missing semantic failure-mode section: {heading}")
            continue
        for ident in sorted(required_ids):
            if not has_active_route(body, ident):
                errors.append(f"{rel} section {heading!r} missing semantic active route: {ident}")

    for heading, body in sections.items():
        if "intentional duplicate" in body.lower():
            continue
        active_failure_ids = re.findall(
            r"(?m)^-\s+`(vcb\.failure\.[A-Za-z0-9_.-]+)`\s+→\s+active(?:\s|:|$)",
            body,
        )
        dupes = sorted(ident for ident, count in Counter(active_failure_ids).items() if count > 1)
        if dupes:
            errors.append(f"{rel} section {heading!r} contains duplicate active failure-mode rows: {dupes}")


def validate_duplicate_failure_mode_full_list_sections(errors: list[str]) -> None:
    """Reject repeated full Chunk 18 failure-mode blocks inside one index."""
    for path in sorted((ROOT / "indexes").glob("*.md")):
        full_sections: list[str] = []
        for heading, body in markdown_h2_sections(read(path)):
            ids = set(re.findall(r"`(vcb\.failure\.[A-Za-z0-9_.-]+)`", body))
            if FAILURE_MODE_TOPIC_IDS.issubset(ids):
                full_sections.append(heading)
        if len(full_sections) > 1:
            errors.append(
                f"duplicate full failure-mode routing sections in {path.relative_to(ROOT)}: {full_sections}"
            )


def validate_chunk_18_per_index_route_surfaces(manifest: dict[str, Any], errors: list[str]) -> None:
    """Ensure updated routing surfaces actually route the active Chunk 18 cards.

    Combined-index checks are insufficient: a missing route in PROMPT_LIBRARY.md
    must fail even when the same ID appears somewhere else.
    """
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_18":
        return
    for rel, required_ids in sorted(CHUNK_18_REQUIRED_ROUTE_SURFACES.items()):
        text = read(ROOT / rel)
        for ident in sorted(required_ids):
            if not has_active_route(text, ident):
                errors.append(f"{rel} missing active route for Chunk 18 failure-mode card: {ident}")

    for rel, section_requirements in sorted(CHUNK_18_FULL_LIST_SECTION_REQUIREMENTS.items()):
        sections = {heading: body for heading, body in markdown_h2_sections(read(ROOT / rel))}
        for heading, required_ids in sorted(section_requirements.items()):
            body = sections.get(heading)
            if body is None:
                errors.append(f"{rel} missing required full-list Chunk 18 failure-mode section: {heading}")
                continue
            observed = set(re.findall(r"`(vcb\.failure\.[A-Za-z0-9_.-]+)`", body))
            missing = sorted(required_ids - observed)
            if missing:
                errors.append(f"{rel} section {heading!r} omits required Chunk 18 failure-mode IDs: {missing}")

    # Any index explicitly version-bumped for Chunk 18 should have at least one current-chunk failure route.
    for path in sorted((ROOT / "indexes").glob("*.md")):
        text = read(path)
        frontmatter = parse_frontmatter(path) or {}
        if frontmatter.get("version") == "0.19.0-draft.chunk18" or frontmatter.get("status") == "chunk_18_updated":
            if "vcb.failure." not in text:
                errors.append(f"Chunk 18 updated index has no failure-mode route: {path.relative_to(ROOT)}")


def validate_chunk_18_source_map_and_report_truth(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_18":
        return
    llms = read(ROOT / "llms.txt")
    if llms.count(FAILURE_MODE_ACTIVE_STATUS_PHRASE) != 1:
        errors.append(
            "llms.txt must contain the Chunk 18 active failure-mode status phrase exactly once; "
            f"observed={llms.count(FAILURE_MODE_ACTIVE_STATUS_PHRASE)}"
        )

    # Reports/changelog must not claim a routing surface for Chunk 18 when that surface has no active failure routes.
    report_text = read(ROOT / "CHUNK_18_REPORT.md") if (ROOT / "CHUNK_18_REPORT.md").exists() else ""
    changelog_text = read(ROOT / "CHANGELOG.md") if (ROOT / "CHANGELOG.md").exists() else ""
    combined_claims = report_text + "\n" + changelog_text
    for rel in sorted(CHUNK_18_ROUTING_SURFACE_FILES):
        basename = rel.split("/", 1)[-1]
        if basename in combined_claims or rel in combined_claims:
            text = read(ROOT / rel)
            if "vcb.failure." not in text:
                errors.append(f"Chunk 18 report/changelog claims {rel} routing, but the file has no failure-mode routes")



def validate_chunk_18_failure_mode_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_18":
        return
    active = authored_active_ids()
    manifest_required = set(manifest.get("chunk_18_required_topic_ids", []) or [])
    if manifest_required != set(CHUNK_18_FAILURE_MODE_IDS):
        errors.append(
            "manifest.chunk_18_required_topic_ids mismatch: "
            f"expected={sorted(CHUNK_18_FAILURE_MODE_IDS)} observed={sorted(manifest_required)}"
        )
    manifest_cards = manifest.get("failure_mode_cards", {})
    if not isinstance(manifest_cards, dict):
        errors.append("manifest.failure_mode_cards must be a mapping for Chunk 18")
        manifest_cards = {}
    if manifest_cards != CHUNK_18_FAILURE_MODE_IDS:
        errors.append(
            "manifest.failure_mode_cards does not match Chunk 18 required card map: "
            f"observed={manifest_cards!r}"
        )
    for ident, rel in CHUNK_18_FAILURE_MODE_IDS.items():
        if ident not in active:
            errors.append(f"Chunk 18 required failure-mode ID not authored: {ident}")
        if not (ROOT / rel).exists():
            errors.append(f"Chunk 18 required failure-mode file missing: {rel}")

    allowed_prompting = {Path(p).name for p in CHUNK_15_WORKFLOW_PROMPTING_IDS.values() if p.startswith("topics/prompting/")}
    allowed_workflows = {Path(p).name for p in CHUNK_15_WORKFLOW_PROMPTING_IDS.values() if p.startswith("topics/workflows/")}
    allowed_workflows |= {Path(p).name for p in CHUNK_16_REVIEW_SAFETY_IDS.values() if p.startswith("topics/workflows/")}
    allowed_workflows |= {Path(p).name for p in CHUNK_17_FRONTEND_REFACTOR_DEPENDENCY_IDS.values() if p.startswith("topics/workflows/")}
    allowed_safety = {Path(p).name for p in CHUNK_16_REVIEW_SAFETY_IDS.values() if p.startswith("topics/safety/")}
    allowed_failures = {Path(p).name for p in CHUNK_18_FAILURE_MODE_IDS.values()}
    observed_prompting = {p.name for p in (ROOT / "topics" / "prompting").glob("*.md") if p.name != ".gitkeep"}
    observed_workflows = {p.name for p in (ROOT / "topics" / "workflows").glob("*.md") if p.name != ".gitkeep"}
    observed_safety = {p.name for p in (ROOT / "topics" / "safety").glob("*.md") if p.name != ".gitkeep"}
    observed_failures = {p.name for p in (ROOT / "topics" / "failure-modes").glob("*.md") if p.name != ".gitkeep"}
    if observed_prompting != allowed_prompting:
        errors.append(f"Chunk 18 must not alter prompting-card scope: expected={sorted(allowed_prompting)} observed={sorted(observed_prompting)}")
    if observed_workflows != allowed_workflows:
        errors.append(f"Chunk 18 must not alter workflow-card scope: expected={sorted(allowed_workflows)} observed={sorted(observed_workflows)}")
    if observed_safety != allowed_safety:
        errors.append(f"Chunk 18 must not alter safety-card scope: expected={sorted(allowed_safety)} observed={sorted(observed_safety)}")
    if observed_failures != allowed_failures:
        errors.append(f"Chunk 18 failure-mode-card scope drift: expected={sorted(allowed_failures)} observed={sorted(observed_failures)}")
    for disallowed in ["topics/tool-catalog", "topics/shortcuts", "topics/field-practices"]:
        files = sorted(p.name for p in (ROOT / disallowed).glob("*.md") if p.name != ".gitkeep")
        if files:
            errors.append(f"Chunk 18 must not add {disallowed} topic cards: {files}")
    pricing_files = sorted(p.name for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep")
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 18 must not expand pricing snapshots: {pricing_files}")
    index_files = [
        ROOT / "indexes" / "INDEX_BY_TASK.md",
        ROOT / "indexes" / "INDEX_BY_FAILURE_MODE.md",
        ROOT / "indexes" / "INDEX_BY_CONCEPT.md",
        ROOT / "indexes" / "INDEX_BY_RISK_LEVEL.md",
        ROOT / "indexes" / "INDEX_BY_RECOVERABILITY.md",
        ROOT / "indexes" / "INDEX_BY_BUDGET_PROFILE.md",
        ROOT / "indexes" / "INDEX_BY_PROJECT_TYPE.md",
        ROOT / "indexes" / "INDEX_FOR_AI_COACHES.md",
        ROOT / "indexes" / "PROMPT_LIBRARY.md",
        ROOT / "indexes" / "GLOSSARY.md",
    ]
    combined = "\n".join(read(p) for p in index_files)
    llm_maps = read(ROOT / "llms.txt") + "\n" + read(ROOT / "llms-full.txt")
    for ident in CHUNK_18_FAILURE_MODE_IDS:
        if f"`{ident}` → active" not in combined and f"`{ident}` → active:" not in combined:
            errors.append(f"primary indexes missing active route for Chunk 18 failure-mode topic: {ident}")
        if ident not in llm_maps:
            errors.append(f"llms maps missing route for Chunk 18 failure-mode topic: {ident}")


def validate_chunk_18_task_index_atomic_routes(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_18":
        return
    text = read(ROOT / "indexes" / "INDEX_BY_TASK.md")
    sections = {heading: body for heading, body in markdown_h2_sections(text)}
    for heading, required_ids in CHUNK_18_TASK_ROUTE_REQUIREMENTS.items():
        body = sections.get(heading)
        if body is None:
            errors.append(f"INDEX_BY_TASK.md missing required task section for Chunk 18 route checks: {heading}")
            continue
        for ident in sorted(required_ids):
            if not has_active_route(body, ident):
                errors.append(f"INDEX_BY_TASK.md section {heading!r} missing active Chunk 18 failure-mode route: {ident}")
    active = authored_active_ids()
    for index_path in sorted((ROOT / "indexes").glob("*.md")):
        body = read(index_path)
        for old_ident, new_ident in PLANNED_FAILURE_MODE_REPLACEMENTS.items():
            if old_ident == new_ident:
                if re.search(rf"`{re.escape(old_ident)}`\s*→\s*planned", body):
                    errors.append(f"stale planned failure-mode route {old_ident} remains in {index_path.relative_to(ROOT)}")
            elif new_ident in active and re.search(rf"`{re.escape(old_ident)}`\s*→\s*planned", body):
                errors.append(f"planned failure route {old_ident} shadows authored active replacement {new_ident} in {index_path.relative_to(ROOT)}")


CHUNK_18_MACHINE_REPORT_CLAIMS = {
    "Manifest source-file inventory matches actual package files: passed",
    "Manifest source_artifacts inventory matches actual package files: passed",
    "Manifest all_tracked_files matches source_files and actual package files: passed",
    "Canonical review package references are consistent across manifest fields: passed",
    "New failure-mode topic files created in Chunk 18: passed",
    "Required Chunk 18 failure-mode-card slice present: passed",
    "Manifest failure_mode_cards map matches authored Chunk 18 files: passed",
    "Manifest chunk_18_required_topic_ids matches authored Chunk 18 IDs: passed",
    "Required topic sections present: passed",
    "Required VCB markers present in new failure-mode files: passed",
    "llms.txt / llms-full.txt source-map versions match current chunk: passed",
    "README root frontmatter status matches current chunk: passed",
    "README body current chunk matches manifest current chunk: passed",
    "README and manifest next-chunk IDs match exactly: passed",
    "Index/register VCB begin-marker versions match frontmatter versions: passed",
    "Index files include STOP_RETRIEVAL and matching END_INDEX markers: passed",
    "VCB begin/end marker pairs exist across Markdown artifacts: passed",
    "SOURCE_REGISTER source rows are inside declared Source ID tables: passed",
    "Duplicate failure-mode full-list sections removed from primary indexes: passed",
    "PROMPT_LIBRARY routes active Chunk 18 failure-mode cards: passed",
    "INDEX_FOR_AI_COACHES routes active Chunk 18 failure-mode cards: passed",
    "INDEX_BY_STABILITY routes active Chunk 18 failure-mode cards: passed",
    "INDEX_BY_CONCEPT routes active Chunk 18 failure-mode cards: passed",
    "INDEX_BY_SHORTCUT routes active Chunk 18 failure-mode cards: passed",
    "Full-list Chunk 18 failure-mode sections include all required IDs: passed",
    "llms.txt active-chunk status phrases are not repeated: passed",
    "Chunk 18 report/changelog routing claims match routed surfaces: passed",
    "INDEX_BY_TASK routes active Chunk 18 failure-mode cards through task-level sections: passed",
    "Stale planned failure-mode routes are absent from indexes: passed",
    "INDEX_BY_FAILURE_MODE semantic sections route done-claim failures to the active atomic card: passed",
    "INDEX_BY_FAILURE_MODE has no duplicate active failure-mode rows inside a single section: passed",
    "Active Chunk 18 machine-claim catalog matches validator checks: passed",
    "Manifest editor_gate approval_applied matches current chunk transition: passed",
    "Current chunk report chunk_id matches manifest active chunk: passed",
    "Root governance metadata drift scan: passed",
    "Index namespace drift scan covers active and planned index routes: passed",
    "Active index routes point to authored active IDs: passed",
    "Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed",
    "Index shortcut routes resolve to SHORTCUT_REGISTER: passed",
    "Index tool IDs resolve to TOOL_REGISTER: passed",
    "Evidence source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report source IDs resolve to SOURCE_REGISTER: passed",
    "Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed",
    "source_status.official_openai matches Evidence and Sources sections: passed",
    "source_status.official_vendor matches Evidence and Sources sections: passed",
    "Duplicate source URL detection: passed",
    "Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed",
    "Report final line is AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW: passed",
}


def validate_chunk_18_report_claims(manifest: dict[str, Any], report: Path, errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_18":
        return
    if not report.exists():
        return
    claims = extract_machine_report_claims(read(report))
    if not claims:
        errors.append("CHUNK_18_REPORT.md missing ### Machine-enforced checks claim block")
        return
    required_claims = {
        "New failure-mode topic files created in Chunk 18: passed",
        "Required Chunk 18 failure-mode-card slice present: passed",
        "Manifest failure_mode_cards map matches authored Chunk 18 files: passed",
        "Manifest chunk_18_required_topic_ids matches authored Chunk 18 IDs: passed",
        "INDEX_BY_TASK routes active Chunk 18 failure-mode cards through task-level sections: passed",
        "Stale planned failure-mode routes are absent from indexes: passed",
        "Duplicate failure-mode full-list sections removed from primary indexes: passed",
        "PROMPT_LIBRARY routes active Chunk 18 failure-mode cards: passed",
        "INDEX_FOR_AI_COACHES routes active Chunk 18 failure-mode cards: passed",
        "INDEX_BY_STABILITY routes active Chunk 18 failure-mode cards: passed",
        "INDEX_BY_CONCEPT routes active Chunk 18 failure-mode cards: passed",
        "INDEX_BY_SHORTCUT routes active Chunk 18 failure-mode cards: passed",
        "Full-list Chunk 18 failure-mode sections include all required IDs: passed",
        "llms.txt active-chunk status phrases are not repeated: passed",
        "Chunk 18 report/changelog routing claims match routed surfaces: passed",
        "INDEX_BY_FAILURE_MODE semantic sections route done-claim failures to the active atomic card: passed",
        "INDEX_BY_FAILURE_MODE has no duplicate active failure-mode rows inside a single section: passed",
        "Active Chunk 18 machine-claim catalog matches validator checks: passed",
    }
    missing = sorted(required_claims - claims)
    if missing:
        errors.append(f"CHUNK_18_REPORT.md missing required machine-enforced validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_18_MACHINE_REPORT_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_18_REPORT.md has unsupported machine-enforced validation claims: {unsupported}")


CHUNK_19_REQUIRED_IDS = {
    "vcb.constraints.operating_mode": "topics/constraints/operating-mode.md",
    "vcb.constraints.attention_budget": "topics/constraints/attention-budget.md",
    "vcb.constraints.usage_burn": "topics/constraints/usage-burn.md",
    "vcb.constraints.recovery_budget": "topics/constraints/recovery-budget.md",
    "vcb.constraints.build_vs_maintenance": "topics/constraints/build-vs-maintenance.md",
    "vcb.constraints.production_quality": "topics/constraints/production-quality-constraints.md",
    "vcb.constraints.scope_budget": "topics/constraints/scope-budget.md",
    "vcb.constraints.review_budget": "topics/constraints/review-budget.md",
}


def validate_chunk_19_constraint_budget_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    current_chunk_for_chunk19 = manifest.get("chunk_gate", {}).get("current_chunk")
    required = CHUNK_19_REQUIRED_IDS
    cards = manifest.get("constraint_budget_cards", {})
    if cards != required:
        errors.append("manifest.constraint_budget_cards does not match Chunk 19 required card map")
    if manifest.get("chunk_19_required_topic_ids") != list(required):
        errors.append("manifest.chunk_19_required_topic_ids does not match required Chunk 19 IDs")
    topic_cards = manifest.get("topic_cards", {})
    for ident, rel in required.items():
        path = ROOT / rel
        if topic_cards.get(ident) != rel:
            errors.append(f"manifest.topic_cards missing Chunk 19 route: {ident} -> {rel}")
        if not path.exists():
            errors.append(f"Chunk 19 required constraint/budget file missing: {rel}")
            continue
        text = read(path)
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in text:
                errors.append(f"{rel} missing required heading: {heading}")
        if f"<!-- VCB:BEGIN_TOPIC id={ident} version=0.1.0 -->" not in text:
            errors.append(f"{rel} missing matching Chunk 19 begin topic marker")
        if f"<!-- VCB:END_TOPIC id={ident} -->" not in text:
            errors.append(f"{rel} missing matching end topic marker")
        stable_block = text.split("## Stable Core", 1)[1].split("## Volatile Surface", 1)[0] if "## Stable Core" in text and "## Volatile Surface" in text else ""
        for pat in [r"\$\d", r"\b\d+\s*credits\b", r"\b\d+\s*/\s*5h\b", r"GPT-\d[\w.-]*\s+\d+"]:
            if re.search(pat, stable_block, flags=re.I):
                errors.append(f"{rel} appears to hardcode exact pricing/limit/model-rate data in Stable Core")
    if current_chunk_for_chunk19 == "chunk_19":
        allowed_constraint_files = {Path(v).name for v in required.values()} | {".gitkeep"}
        observed = {p.name for p in (ROOT / "topics" / "constraints").glob("*")}
        if observed != allowed_constraint_files:
            errors.append(f"Chunk 19 constraint-card scope drift: expected={sorted(allowed_constraint_files)} observed={sorted(observed)}")
        for disallowed in ["topics/tool-catalog", "topics/shortcuts", "topics/field-practices"]:
            files = [p.name for p in (ROOT / disallowed).glob("*.md")]
            if files:
                errors.append(f"Chunk 19 must not add {disallowed} topic cards: {files}")
        pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md")]
        if pricing_files != ["2026-06-09-openai-codex.md"]:
            errors.append(f"Chunk 19 must not expand pricing snapshots: {pricing_files}")

    required_route_files = [
        "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_BUDGET_PROFILE.md", "indexes/INDEX_BY_CONCEPT.md",
        "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_FOR_AI_COACHES.md", "indexes/PROMPT_LIBRARY.md",
        "indexes/GLOSSARY.md", "indexes/INDEX_BY_SHORTCUT.md", "indexes/INDEX_BY_RISK_LEVEL.md",
        "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_PROJECT_TYPE.md", "indexes/INDEX_BY_CODEX_SURFACE.md",
        "indexes/INDEX_BY_TOOL_CATEGORY.md", "indexes/INDEX_BY_FAILURE_MODE.md",
    ]
    for rel in required_route_files:
        text = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in text:
                errors.append(f"{rel} missing active route for Chunk 19 constraint/budget card: {ident}")
    for rel in ["llms.txt", "llms-full.txt", "README.md"]:
        text = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in text:
                errors.append(f"{rel} missing Chunk 19 source-map/root route: {ident}")
    for idx in (ROOT / "indexes").glob("*.md"):
        text = read(idx)
        for ident in ["vcb.constraints.usage_burn"]:
            if re.search(rf"`{re.escape(ident)}`\s*→\s*planned", text):
                errors.append(f"stale planned Chunk 19 route remains in {idx.relative_to(ROOT)}: {ident}")
    report_text = read(ROOT / "CHUNK_19_REPORT.md") if (ROOT / "CHUNK_19_REPORT.md").exists() else ""
    changelog_text = read(ROOT / "CHANGELOG.md")
    claimed_surfaces = {
        "PROMPT_LIBRARY.md": "indexes/PROMPT_LIBRARY.md",
        "INDEX_FOR_AI_COACHES.md": "indexes/INDEX_FOR_AI_COACHES.md",
        "INDEX_BY_BUDGET_PROFILE.md": "indexes/INDEX_BY_BUDGET_PROFILE.md",
        "INDEX_BY_TASK.md": "indexes/INDEX_BY_TASK.md",
        "INDEX_BY_STABILITY.md": "indexes/INDEX_BY_STABILITY.md",
        "INDEX_BY_CONCEPT.md": "indexes/INDEX_BY_CONCEPT.md",
        "INDEX_BY_SHORTCUT.md": "indexes/INDEX_BY_SHORTCUT.md",
    }
    combined_claims = report_text + "\n" + changelog_text
    for label, rel in claimed_surfaces.items():
        if label in combined_claims and not any(f"`{ident}`" in read(ROOT / rel) for ident in required):
            errors.append(f"Chunk 19 report/changelog claims {label} routing, but the file has no constraint/budget routes")


def validate_no_live_markdown_after_vcb_end_markers(errors: list[str]) -> None:
    """Fail when Markdown contains live content after its final VCB END marker.

    Historical and active chunk reports use a repository-standard terminal
    AUTHOR_STATUS line after END_REPORT, so that exact report tail is allowed.
    Other Markdown artifacts must end at the VCB END marker except whitespace.
    """
    end_re = re.compile(r"<!--\s*VCB:END_[A-Z_]+\b[^>]*-->")
    for path in ROOT.rglob("*.md"):
        if "__pycache__" in path.parts:
            continue
        text = read(path)
        matches = list(end_re.finditer(text))
        if not matches:
            continue
        tail = text[matches[-1].end():].strip()
        if not tail:
            continue
        is_chunk_report = re.fullmatch(r"CHUNK_\d+_REPORT\.md", path.name) is not None
        if is_chunk_report and tail == "AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW":
            continue
        errors.append(f"{path.relative_to(ROOT)} has live content after final VCB END marker: {tail[:120]!r}")


def validate_changelog_end_boundary(manifest: dict[str, Any], errors: list[str]) -> None:
    text = read(ROOT / "CHANGELOG.md")
    end_marker = "<!-- VCB:END_CHANGELOG id=vcb.register.changelog -->"
    if end_marker not in text:
        errors.append("CHANGELOG.md missing VCB:END_CHANGELOG marker")
        return
    tail = text.split(end_marker, 1)[1].strip()
    if tail:
        errors.append("CHANGELOG.md has live content after VCB:END_CHANGELOG")
    if manifest.get("chunk_gate", {}).get("current_chunk") == "chunk_19" and "Chunk 19" in tail:
        errors.append("CHANGELOG.md contains Chunk 19 content after VCB:END_CHANGELOG")


def validate_chunk_19_report_inventory(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_19":
        return
    report_path = ROOT / "CHUNK_19_REPORT.md"
    if not report_path.exists():
        errors.append("CHUNK_19_REPORT.md missing for active Chunk 19")
        return
    text = read(report_path)
    required_inventory_paths = set(CHUNK_19_REQUIRED_IDS.values()) | {
        "CHUNK_19_REPORT.md",
        "chapters/26-ci-non-interactive-codex-github-actions.md",
    }
    for rel in sorted(required_inventory_paths):
        if f"`{rel}`" not in text:
            errors.append(f"CHUNK_19_REPORT.md file inventory omits required Chunk 19 path: {rel}")
    if "related-topic route correction" not in text or "`vcb.constraints.usage_burn`" not in text:
        errors.append("CHUNK_19_REPORT.md missing Chapter 26 route-correction explanation")
    if "## Recommended Next Chunk" not in text or "`chunk_20_shortcut_harm_reduction_topic_cards`" not in text:
        errors.append("CHUNK_19_REPORT.md missing recommended next chunk section")
    if "## Unresolved questions" not in text or "None." not in text:
        errors.append("CHUNK_19_REPORT.md must explicitly state unresolved questions")


CHUNK_19_REQUIRED_CREATED_FILES = set(CHUNK_19_REQUIRED_IDS.values()) | {"CHUNK_19_REPORT.md"}
CHUNK_19_REQUIRED_UPDATED_FILES = {
    "README.md",
    "manifest.json",
    "llms.txt",
    "llms-full.txt",
    "SOURCE_REGISTER.md",
    "CHANGELOG.md",
    "TREE.txt",
    "scripts/validate_repository.py",
    "chapters/26-ci-non-interactive-codex-github-actions.md",
    "indexes/GLOSSARY.md",
    "indexes/INDEX_BY_BUDGET_PROFILE.md",
    "indexes/INDEX_BY_CODEX_SURFACE.md",
    "indexes/INDEX_BY_CONCEPT.md",
    "indexes/INDEX_BY_FAILURE_MODE.md",
    "indexes/INDEX_BY_PROJECT_TYPE.md",
    "indexes/INDEX_BY_RECOVERABILITY.md",
    "indexes/INDEX_BY_RISK_LEVEL.md",
    "indexes/INDEX_BY_SHORTCUT.md",
    "indexes/INDEX_BY_STABILITY.md",
    "indexes/INDEX_BY_TASK.md",
    "indexes/INDEX_BY_TOOL_CATEGORY.md",
    "indexes/INDEX_FOR_AI_COACHES.md",
    "indexes/PROMPT_LIBRARY.md",
}


def report_section_backtick_paths(text: str, heading: str) -> set[str]:
    match = re.search(rf"(?ms)^##\s+{re.escape(heading)}\s*$\n(.*?)(?=^##\s+|\Z)", text)
    if not match:
        return set()
    return set(re.findall(r"`([^`]+)`", match.group(1)))


def validate_chunk_19_report_file_inventory(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_19":
        return
    path = ROOT / "CHUNK_19_REPORT.md"
    if not path.exists():
        errors.append("CHUNK_19_REPORT.md missing for active Chunk 19")
        return
    text = read(path)
    created = report_section_backtick_paths(text, "Files created")
    updated = report_section_backtick_paths(text, "Files updated")
    missing_created = sorted(CHUNK_19_REQUIRED_CREATED_FILES - created)
    missing_updated = sorted(CHUNK_19_REQUIRED_UPDATED_FILES - updated)
    if missing_created:
        errors.append(f"CHUNK_19_REPORT.md Files created omits required current-chunk files: {missing_created}")
    if missing_updated:
        errors.append(f"CHUNK_19_REPORT.md Files updated omits required current-chunk files: {missing_updated}")
    if "## Recommended Next Chunk" not in text or "chunk_20_shortcut_harm_reduction_topic_cards" not in text:
        errors.append("CHUNK_19_REPORT.md missing Recommended Next Chunk section for Chunk 20")
    if "## Unresolved questions" not in text or "None." not in text:
        errors.append("CHUNK_19_REPORT.md must explicitly state unresolved questions status")


CHUNK_19_REPORT_REQUIRED_CLAIMS = {
    "New constraint/budget topic files created in Chunk 19: passed",
    "Required Chunk 19 constraint-budget slice present: passed",
    "Manifest constraint_budget_cards map matches authored Chunk 19 files: passed",
    "Manifest chunk_19_required_topic_ids matches authored Chunk 19 IDs: passed",
    "Primary indexes route active Chunk 19 constraint/budget cards: passed",
    "Prompt library routes active Chunk 19 constraint/budget cards: passed",
    "AI coach index routes active Chunk 19 constraint/budget cards: passed",
    "Budget index routes active Chunk 19 constraint/budget cards: passed",
    "Task index routes active Chunk 19 constraint/budget cards through task-level and aggregate sections: passed",
    "LLM source maps route active Chunk 19 constraint/budget cards: passed",
    "Stale planned constraint routes are absent where active replacements are authored: passed",
    "Constraint/budget cards do not hardcode exact prices, limits, credits, or model-routing recipes into stable prose: passed",
    "Chunk 19 report/changelog routing claims match routed surfaces: passed",
    "Markdown artifacts have no live content after VCB:END markers except report terminal author status lines: passed",
    "Nested manifest source_artifacts.source_files matches top-level manifest source_files and actual package inventory: passed",
    "Manifest source_files_match_manifest is true only when nested source_files is current: passed",
    "Active Chunk 19 report inventory lists current chunk report and touched chapter route correction: passed",
    "CHANGELOG.md has no Chunk 19 content after VCB:END_CHANGELOG: passed",
    "Active Chunk 19 machine-claim catalog matches validator checks: passed",
}


def validate_chunk_19_report_claims(manifest: dict[str, Any], report: Path, errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_19":
        return
    report_path = ROOT / "CHUNK_19_REPORT.md"
    if not report_path.exists():
        errors.append("CHUNK_19_REPORT.md missing for active Chunk 19")
        return
    text = read(report_path)
    for claim in CHUNK_19_REPORT_REQUIRED_CLAIMS:
        if claim not in text:
            errors.append(f"CHUNK_19_REPORT.md missing implemented validation claim: {claim}")



CHUNK_20_SHORTCUT_IDS = {
    "vcb.shortcut.skipping_tests": "topics/shortcuts/skipping-tests.md",
    "vcb.shortcut.accepting_looks_done": "topics/shortcuts/accepting-looks-done.md",
    "vcb.shortcut.broad_agent_permissions": "topics/shortcuts/broad-agent-permissions.md",
    "vcb.shortcut.unattended_long_runs": "topics/shortcuts/unattended-long-runs.md",
    "vcb.shortcut.broad_refactor": "topics/shortcuts/broad-refactor.md",
    "vcb.shortcut.context_dumping": "topics/shortcuts/context-dumping.md",
    "vcb.shortcut.adding_dependencies_fast": "topics/shortcuts/adding-dependencies-fast.md",
    "vcb.shortcut.reviewing_cloud_summary_only": "topics/shortcuts/reviewing-cloud-summary-only.md",
}

CHUNK_20_REQUIRED_INDEXES = [
    "indexes/INDEX_BY_SHORTCUT.md",
    "indexes/INDEX_BY_TASK.md",
    "indexes/INDEX_FOR_AI_COACHES.md",
    "indexes/PROMPT_LIBRARY.md",
    "indexes/GLOSSARY.md",
    "indexes/INDEX_BY_FAILURE_MODE.md",
    "indexes/INDEX_BY_BUDGET_PROFILE.md",
    "indexes/INDEX_BY_RISK_LEVEL.md",
    "indexes/INDEX_BY_RECOVERABILITY.md",
    "indexes/INDEX_BY_CONCEPT.md",
    "indexes/INDEX_BY_STABILITY.md",
    "indexes/INDEX_BY_PROJECT_TYPE.md",
    "indexes/INDEX_BY_CODEX_SURFACE.md",
    "indexes/INDEX_BY_TOOL_CATEGORY.md",
]

CHUNK_20_TASK_SECTION_REQUIREMENTS = {
    "Prompt, plan, context, and done criteria": {
        "vcb.shortcut.context_dumping",
        "vcb.shortcut.accepting_looks_done",
    },
    "Set up Codex safely": {
        "vcb.shortcut.broad_agent_permissions",
    },
    "Write or update tests": {
        "vcb.shortcut.skipping_tests",
    },
    "Review Codex output or a PR": {
        "vcb.shortcut.accepting_looks_done",
        "vcb.shortcut.reviewing_cloud_summary_only",
    },
    "Refactor safely": {
        "vcb.shortcut.broad_refactor",
    },
    "Choose dependencies, packages, or frameworks": {
        "vcb.shortcut.adding_dependencies_fast",
    },
    "Use cloud, subagents, browser, or GUI surfaces": {
        "vcb.shortcut.unattended_long_runs",
        "vcb.shortcut.reviewing_cloud_summary_only",
    },
}

CHUNK_20_REPORT_REQUIRED_CLAIMS = {
    "New shortcut harm-reduction topic files created in Chunk 20: passed",
    "Required Chunk 20 shortcut-card slice present: passed",
    "Manifest shortcut_harm_reduction_cards map matches authored Chunk 20 files: passed",
    "Manifest chunk_20_required_topic_ids matches authored Chunk 20 IDs: passed",
    "Required VCB markers present in new shortcut files: passed",
    "Required sections present in new shortcut files: passed",
    "SHORTCUT_REGISTER marks authored Chunk 20 shortcut IDs active: passed",
    "SHORTCUT_REGISTER shortcut rows are inside declared shortcut tables: passed",
    "Primary indexes route active Chunk 20 shortcut cards: passed",
    "Prompt library routes active Chunk 20 shortcut cards: passed",
    "AI coach index routes active Chunk 20 shortcut cards: passed",
    "LLM source maps route active Chunk 20 shortcut cards: passed",
    "Stale planned routes for authored Chunk 20 shortcuts are absent from indexes and SHORTCUT_REGISTER: passed",
    "Chunk 20 did not start full shortcut expansion or disallowed topic-card families: passed",
    "Chunk 20 report/changelog routing claims match routed surfaces: passed",
    "Active Chunk 20 report inventory lists created shortcut cards and updated routing/governance files: passed",
    "No single index section contains duplicate active Chunk 20 shortcut rows: passed",
    "Active Chunk 20 machine-claim catalog matches validator checks: passed",
}


def shortcut_register_statuses() -> dict[str, str]:
    statuses: dict[str, str] = {}
    path = ROOT / "SHORTCUT_REGISTER.md"
    if not path.exists():
        return statuses
    for line in read(path).splitlines():
        if not line.startswith("| `vcb.shortcut."):
            continue
        cells = [cell.strip() for cell in line.strip().strip("|").split("|")]
        if len(cells) < 8:
            continue
        ident = cells[0].strip("`")
        status = cells[7]
        statuses[ident] = status
    return statuses


def validate_chunk_20_shortcut_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_20":
        return
    required = CHUNK_20_SHORTCUT_IDS
    active = authored_active_ids()
    if manifest.get("shortcut_harm_reduction_cards") != required:
        errors.append("manifest.shortcut_harm_reduction_cards does not match Chunk 20 required card map")
    if manifest.get("chunk_20_required_topic_ids") != list(required):
        errors.append("manifest.chunk_20_required_topic_ids does not match required Chunk 20 IDs")
    topic_cards = manifest.get("topic_cards", {})
    for ident, rel in required.items():
        path = ROOT / rel
        if topic_cards.get(ident) != rel:
            errors.append(f"manifest.topic_cards missing Chunk 20 route: {ident} -> {rel}")
        if ident not in active:
            errors.append(f"Chunk 20 required shortcut ID not authored: {ident}")
        if not path.exists():
            errors.append(f"Chunk 20 required shortcut file missing: {rel}")
            continue
        text = read(path)
        fm = parse_frontmatter(path) or {}
        if fm.get("type") != "shortcut" or fm.get("shortcut_type") != "risk_managed_shortcut":
            errors.append(f"{rel} must use type=shortcut and shortcut_type=risk_managed_shortcut")
        if fm.get("status") != "active":
            errors.append(f"{rel} shortcut status must be active")
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in text:
                errors.append(f"{rel} missing required heading: {heading}")
        if f"<!-- VCB:BEGIN_TOPIC id={ident} version=0.1.0 -->" not in text:
            errors.append(f"{rel} missing matching Chunk 20 begin topic marker")
        if f"<!-- VCB:END_TOPIC id={ident} -->" not in text:
            errors.append(f"{rel} missing matching end topic marker")
        if "## Quick Navigation" not in text:
            errors.append(f"{rel} missing shortcut-card Quick Navigation section")

    allowed_shortcut_files = {Path(v).name for v in required.values()} | {".gitkeep"}
    observed_shortcut_files = {p.name for p in (ROOT / "topics" / "shortcuts").glob("*")}
    if observed_shortcut_files != allowed_shortcut_files:
        errors.append(f"Chunk 20 shortcut-card scope drift: expected={sorted(allowed_shortcut_files)} observed={sorted(observed_shortcut_files)}")
    for disallowed in ["topics/tool-catalog", "topics/field-practices"]:
        files = [p.name for p in (ROOT / disallowed).glob("*.md")]
        if files:
            errors.append(f"Chunk 20 must not add {disallowed} topic cards: {files}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md")]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 20 must not expand pricing snapshots: {pricing_files}")

    statuses = shortcut_register_statuses()
    for ident in required:
        if statuses.get(ident) != "active":
            errors.append(f"SHORTCUT_REGISTER row for {ident} must be active; observed={statuses.get(ident)!r}")
    register_text = read(ROOT / "SHORTCUT_REGISTER.md")
    for ident in required:
        if re.search(rf"`{re.escape(ident)}`[^\n]*\|\s*planned\s*\|", register_text):
            errors.append(f"SHORTCUT_REGISTER still lists authored Chunk 20 shortcut as planned: {ident}")

    for rel in CHUNK_20_REQUIRED_INDEXES:
        body = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing route for Chunk 20 shortcut card: {ident}")
            if re.search(rf"`{re.escape(ident)}`\s*→\s*planned", body):
                errors.append(f"{rel} has stale planned route for authored Chunk 20 shortcut: {ident}")
        for heading, section_body in markdown_h2_sections(body):
            for ident in required:
                count = section_body.count(f"`{ident}`")
                if count > 1 and "intentional duplicate" not in section_body.lower():
                    errors.append(f"{rel} section {heading!r} contains duplicate active Chunk 20 shortcut route: {ident}")

    for rel in ["llms.txt", "llms-full.txt", "README.md"]:
        body = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing Chunk 20 source-map/root route: {ident}")

    sections = {heading: body for heading, body in markdown_h2_sections(read(ROOT / "indexes" / "INDEX_BY_TASK.md"))}
    for heading, required_ids in CHUNK_20_TASK_SECTION_REQUIREMENTS.items():
        body = sections.get(heading)
        if body is None:
            errors.append(f"INDEX_BY_TASK.md missing Chunk 20 semantic shortcut section: {heading}")
            continue
        for ident in required_ids:
            if f"`{ident}`" not in body:
                errors.append(f"INDEX_BY_TASK.md section {heading!r} missing active shortcut route: {ident}")

    report_text = read(ROOT / "CHUNK_20_REPORT.md") if (ROOT / "CHUNK_20_REPORT.md").exists() else ""
    changelog_text = read(ROOT / "CHANGELOG.md")
    combined_claims = report_text + "\n" + changelog_text
    claimed_surfaces = {
        "PROMPT_LIBRARY.md": "indexes/PROMPT_LIBRARY.md",
        "INDEX_FOR_AI_COACHES.md": "indexes/INDEX_FOR_AI_COACHES.md",
        "INDEX_BY_SHORTCUT.md": "indexes/INDEX_BY_SHORTCUT.md",
        "INDEX_BY_TASK.md": "indexes/INDEX_BY_TASK.md",
        "INDEX_BY_FAILURE_MODE.md": "indexes/INDEX_BY_FAILURE_MODE.md",
        "INDEX_BY_BUDGET_PROFILE.md": "indexes/INDEX_BY_BUDGET_PROFILE.md",
        "INDEX_BY_RISK_LEVEL.md": "indexes/INDEX_BY_RISK_LEVEL.md",
        "INDEX_BY_RECOVERABILITY.md": "indexes/INDEX_BY_RECOVERABILITY.md",
        "INDEX_BY_CONCEPT.md": "indexes/INDEX_BY_CONCEPT.md",
        "INDEX_BY_STABILITY.md": "indexes/INDEX_BY_STABILITY.md",
        "INDEX_BY_PROJECT_TYPE.md": "indexes/INDEX_BY_PROJECT_TYPE.md",
        "INDEX_BY_CODEX_SURFACE.md": "indexes/INDEX_BY_CODEX_SURFACE.md",
        "INDEX_BY_TOOL_CATEGORY.md": "indexes/INDEX_BY_TOOL_CATEGORY.md",
        "GLOSSARY.md": "indexes/GLOSSARY.md",
    }
    for label, rel in claimed_surfaces.items():
        if label in combined_claims and not any(f"`{ident}`" in read(ROOT / rel) for ident in required):
            errors.append(f"Chunk 20 report/changelog claims {label} routing, but the file has no Chunk 20 shortcut routes")


def validate_chunk_20_report_inventory(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_20":
        return
    path = ROOT / "CHUNK_20_REPORT.md"
    if not path.exists():
        errors.append("CHUNK_20_REPORT.md missing for active Chunk 20")
        return
    text = read(path)
    required_created = set(CHUNK_20_SHORTCUT_IDS.values()) | {"CHUNK_20_REPORT.md"}
    required_updated = {
        "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SHORTCUT_REGISTER.md", "SOURCE_REGISTER.md",
        "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py",
        "indexes/GLOSSARY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md", "indexes/INDEX_BY_CODEX_SURFACE.md",
        "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/INDEX_BY_PROJECT_TYPE.md",
        "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_RISK_LEVEL.md", "indexes/INDEX_BY_SHORTCUT.md",
        "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_TOOL_CATEGORY.md",
        "indexes/INDEX_FOR_AI_COACHES.md", "indexes/PROMPT_LIBRARY.md",
    }
    for rel in sorted(required_created | required_updated):
        if f"`{rel}`" not in text:
            errors.append(f"CHUNK_20_REPORT.md file inventory omits required Chunk 20 path: {rel}")
    if "## Recommended Next Chunk" not in text:
        errors.append("CHUNK_20_REPORT.md missing recommended next chunk section")
    if "## Unresolved questions" not in text or "None." not in text:
        errors.append("CHUNK_20_REPORT.md must explicitly state unresolved questions")
    claims = extract_machine_report_claims(read(path))
    if not claims:
        errors.append("CHUNK_20_REPORT.md missing validation claims block")
    missing = sorted(CHUNK_20_REPORT_REQUIRED_CLAIMS - claims)
    if missing:
        errors.append(f"CHUNK_20_REPORT.md missing implemented validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_20_REPORT_REQUIRED_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_20_REPORT.md has unsupported validation claims: {unsupported}")


CHUNK_21_SHORTCUT_IDS = {
    "vcb.shortcut.production_console_computer_use": "topics/shortcuts/production-console-computer-use.md",
    "vcb.shortcut.overbroad_ci_permissions": "topics/shortcuts/overbroad-ci-permissions.md",
    "vcb.shortcut.long_lived_ci_secrets": "topics/shortcuts/long-lived-ci-secrets.md",
    "vcb.shortcut.real_secrets_in_prototype": "topics/shortcuts/real-secrets-in-prototype.md",
    "vcb.shortcut.cloud_work_with_real_secrets": "topics/shortcuts/cloud-work-with-real-secrets.md",
    "vcb.shortcut.full_access_automation": "topics/shortcuts/full-access-automation.md",
    "vcb.shortcut.unattended_mutation": "topics/shortcuts/unattended-mutation.md",
    "vcb.shortcut.always_allow_sensitive_apps": "topics/shortcuts/always-allow-sensitive-apps.md",
}

CHUNK_21_REQUIRED_INDEXES = CHUNK_20_REQUIRED_INDEXES

CHUNK_21_TASK_SECTION_REQUIREMENTS = {
    "Set up Codex safely": {"vcb.shortcut.always_allow_sensitive_apps", "vcb.shortcut.full_access_automation"},
    "Do security-sensitive work": {"vcb.shortcut.real_secrets_in_prototype", "vcb.shortcut.cloud_work_with_real_secrets", "vcb.shortcut.production_console_computer_use"},
    "Run CI or non-interactive Codex": {"vcb.shortcut.overbroad_ci_permissions", "vcb.shortcut.long_lived_ci_secrets", "vcb.shortcut.full_access_automation"},
    "Use cloud, subagents, browser, or GUI surfaces": {"vcb.shortcut.unattended_mutation", "vcb.shortcut.always_allow_sensitive_apps", "vcb.shortcut.production_console_computer_use"},
    "Take a shortcut safely": set(CHUNK_21_SHORTCUT_IDS),
}

CHUNK_21_FAILURE_SECTION_REQUIREMENTS = {
    "Security-sensitive behavior is under-specified": {"vcb.shortcut.real_secrets_in_prototype", "vcb.shortcut.cloud_work_with_real_secrets", "vcb.shortcut.production_console_computer_use"},
    "CI or automation mutates too much": {"vcb.shortcut.overbroad_ci_permissions", "vcb.shortcut.long_lived_ci_secrets", "vcb.shortcut.full_access_automation", "vcb.shortcut.unattended_mutation"},
    "Cloud, subagent, or GUI work runs too broadly": {"vcb.shortcut.always_allow_sensitive_apps", "vcb.shortcut.cloud_work_with_real_secrets", "vcb.shortcut.production_console_computer_use"},
}

CHUNK_21_AI_COACH_SECTION_REQUIREMENTS = {
    "Human wants broad permissions, automation, or GUI control": {"vcb.shortcut.full_access_automation", "vcb.shortcut.unattended_mutation", "vcb.shortcut.always_allow_sensitive_apps", "vcb.shortcut.production_console_computer_use"},
    "Human wants to skip planning, tests, review, or security": {"vcb.shortcut.real_secrets_in_prototype", "vcb.shortcut.cloud_work_with_real_secrets"},
    "Human asks what plan or operating mode to use": {"vcb.shortcut.overbroad_ci_permissions", "vcb.shortcut.long_lived_ci_secrets"},
}

CHUNK_21_RISK_SECTION_REQUIREMENTS = {
    "Do-not-do-in-production shortcuts": {
        "vcb.shortcut.production_console_computer_use",
        "vcb.shortcut.full_access_automation",
        "vcb.shortcut.overbroad_ci_permissions",
        "vcb.shortcut.long_lived_ci_secrets",
        "vcb.shortcut.cloud_work_with_real_secrets",
        "vcb.shortcut.unattended_mutation",
        "vcb.shortcut.always_allow_sensitive_apps",
    },
    "Never with real secrets or sensitive user data": {
        "vcb.shortcut.real_secrets_in_prototype",
        "vcb.shortcut.cloud_work_with_real_secrets",
        "vcb.shortcut.long_lived_ci_secrets",
        "vcb.shortcut.production_console_computer_use",
        "vcb.shortcut.always_allow_sensitive_apps",
    },
}

CHUNK_21_SHORTCUT_SECTION_REQUIREMENTS = {
    "Setup, permission, and automation shortcuts": {
        "vcb.shortcut.broad_agent_permissions",
        "vcb.shortcut.overbroad_ci_permissions",
        "vcb.shortcut.long_lived_ci_secrets",
        "vcb.shortcut.real_secrets_in_prototype",
        "vcb.shortcut.unattended_mutation",
        "vcb.shortcut.full_access_automation",
        "vcb.shortcut.always_allow_sensitive_apps",
    },
    "Advanced agentic workflow shortcuts": {
        "vcb.shortcut.unattended_mutation",
        "vcb.shortcut.full_access_automation",
        "vcb.shortcut.always_allow_sensitive_apps",
        "vcb.shortcut.production_console_computer_use",
        "vcb.shortcut.cloud_work_with_real_secrets",
    },
}

CHUNK_21_PLANNED_COMPANION_REQUIREMENTS = [
    (
        "indexes/INDEX_BY_RISK_LEVEL.md",
        "Do-not-do-in-production shortcuts",
        "vcb.shortcut.logged_in_gui_production_actions",
        "vcb.shortcut.production_console_computer_use",
    ),
    (
        "indexes/INDEX_BY_RISK_LEVEL.md",
        "Never with real secrets or sensitive user data",
        "vcb.shortcut.browser_use_with_secrets",
        "vcb.shortcut.cloud_work_with_real_secrets",
    ),
    (
        "indexes/INDEX_BY_SHORTCUT.md",
        "Advanced agentic workflow shortcuts",
        "vcb.shortcut.unattended_cloud_delegation",
        "vcb.shortcut.unattended_mutation",
    ),
    (
        "indexes/INDEX_BY_SHORTCUT.md",
        "Advanced agentic workflow shortcuts",
        "vcb.shortcut.logged_in_gui_production_actions",
        "vcb.shortcut.production_console_computer_use",
    ),
]

CHUNK_21_REPORT_REQUIRED_CLAIMS = {
    "New security/permission shortcut topic files created in Chunk 21: passed",
    "Required Chunk 21 security/permission shortcut-card slice present: passed",
    "Manifest security_permission_shortcut_cards map matches authored Chunk 21 files: passed",
    "Manifest chunk_21_required_topic_ids matches authored Chunk 21 IDs: passed",
    "Required VCB markers present in new Chunk 21 shortcut files: passed",
    "Required sections present in new Chunk 21 shortcut files: passed",
    "SHORTCUT_REGISTER marks authored Chunk 21 shortcut IDs active: passed",
    "SHORTCUT_REGISTER shortcut rows are inside declared shortcut tables: passed",
    "Primary indexes route active Chunk 21 security/permission shortcut cards: passed",
    "Prompt library routes active Chunk 21 security/permission shortcut cards: passed",
    "AI coach index routes active Chunk 21 security/permission shortcut cards: passed",
    "LLM source maps route active Chunk 21 security/permission shortcut cards: passed",
    "Manifest current-chunk validation metadata names Chunk 21: passed",
    "Generic LLM shortcut route covers active Chunk 20 and Chunk 21 shortcut-card slices: passed",
    "Risk-level semantic sections route active Chunk 21 security/permission cards: passed",
    "Shortcut semantic sections route active Chunk 21 cards before planned near-duplicate companions: passed",
    "Task, failure-mode, and AI-coach semantic routes include Chunk 21 cards: passed",
    "Stale planned routes for authored Chunk 21 shortcuts are absent from indexes and SHORTCUT_REGISTER: passed",
    "Chunk 21 did not start full shortcut expansion or disallowed topic-card families: passed",
    "Chunk 21 report/changelog routing claims match routed surfaces: passed",
    "Active Chunk 21 report inventory lists created shortcut cards and updated routing/governance files: passed",
    "No single index section contains duplicate active Chunk 21 shortcut rows: passed",
    "Active Chunk 21 machine-claim catalog matches validator checks: passed",
}


def validate_section_requirements(rel: str, section_requirements: dict[str, set[str]], errors: list[str], label: str) -> None:
    sections = {heading: body for heading, body in markdown_h2_sections(read(ROOT / rel))}
    for heading, required_ids in section_requirements.items():
        body = sections.get(heading)
        if body is None:
            errors.append(f"{rel} missing {label} semantic section: {heading}")
            continue
        for ident in required_ids:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} section {heading!r} missing active Chunk 21 route: {ident}")


def validate_planned_companion_routes(requirements: list[tuple[str, str, str, str]], errors: list[str]) -> None:
    """Require active Chunk 21 routes before planned near-duplicate companion IDs."""
    for rel, heading, planned_id, active_id in requirements:
        sections = {section_heading: body for section_heading, body in markdown_h2_sections(read(ROOT / rel))}
        body = sections.get(heading)
        if body is None:
            errors.append(f"{rel} missing section for planned-companion check: {heading}")
            continue
        planned_pos = body.find(f"`{planned_id}`")
        if planned_pos == -1:
            continue
        active_pos = body.find(f"`{active_id}`")
        if active_pos == -1:
            errors.append(
                f"{rel} section {heading!r} keeps planned near-duplicate {planned_id} "
                f"without active Chunk 21 route {active_id}"
            )
        elif active_pos > planned_pos:
            errors.append(
                f"{rel} section {heading!r} lists planned near-duplicate {planned_id} "
                f"before active Chunk 21 route {active_id}"
            )


def validate_chunk_21_security_permission_shortcut_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_21":
        return
    required = CHUNK_21_SHORTCUT_IDS
    active = authored_active_ids()
    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    if "Chunk 21" not in current_checks or "Chunk 20 shortcut harm-reduction" in current_checks:
        errors.append(
            "manifest.validation_expectations.current_chunk_checks does not name the active Chunk 21 validation scope: "
            f"{current_checks!r}"
        )
    if manifest.get("security_permission_shortcut_cards") != required:
        errors.append("manifest.security_permission_shortcut_cards does not match Chunk 21 required card map")
    if manifest.get("chunk_21_required_topic_ids") != list(required):
        errors.append("manifest.chunk_21_required_topic_ids does not match required Chunk 21 IDs")
    topic_cards = manifest.get("topic_cards", {})
    for ident, rel in required.items():
        path = ROOT / rel
        if topic_cards.get(ident) != rel:
            errors.append(f"manifest.topic_cards missing Chunk 21 route: {ident} -> {rel}")
        if ident not in active:
            errors.append(f"Chunk 21 required shortcut ID not authored: {ident}")
        if not path.exists():
            errors.append(f"Chunk 21 required shortcut file missing: {rel}")
            continue
        text = read(path)
        fm = parse_frontmatter(path) or {}
        if fm.get("type") != "shortcut" or fm.get("shortcut_type") != "risk_managed_shortcut":
            errors.append(f"{rel} must use type=shortcut and shortcut_type=risk_managed_shortcut")
        if fm.get("status") != "active":
            errors.append(f"{rel} shortcut status must be active")
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in text:
                errors.append(f"{rel} missing required heading: {heading}")
        if f"<!-- VCB:BEGIN_TOPIC id={ident} version=0.1.0 -->" not in text:
            errors.append(f"{rel} missing matching Chunk 21 begin topic marker")
        if f"<!-- VCB:END_TOPIC id={ident} -->" not in text:
            errors.append(f"{rel} missing matching end topic marker")
        if "## Quick Navigation" not in text:
            errors.append(f"{rel} missing shortcut-card Quick Navigation section")

    allowed_shortcut_files = {Path(v).name for v in CHUNK_20_SHORTCUT_IDS.values()} | {Path(v).name for v in required.values()} | {".gitkeep"}
    observed_shortcut_files = {p.name for p in (ROOT / "topics" / "shortcuts").glob("*")}
    if observed_shortcut_files != allowed_shortcut_files:
        errors.append(f"Chunk 21 shortcut-card scope drift: expected={sorted(allowed_shortcut_files)} observed={sorted(observed_shortcut_files)}")
    for disallowed in ["topics/tool-catalog", "topics/field-practices"]:
        files = [p.name for p in (ROOT / disallowed).glob("*.md")]
        if files:
            errors.append(f"Chunk 21 must not add {disallowed} topic cards: {files}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md")]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 21 must not expand pricing snapshots: {pricing_files}")

    statuses = shortcut_register_statuses()
    register_text = read(ROOT / "SHORTCUT_REGISTER.md")
    for ident in required:
        if statuses.get(ident) != "active":
            errors.append(f"SHORTCUT_REGISTER row for {ident} must be active; observed={statuses.get(ident)!r}")
        if re.search(rf"`{re.escape(ident)}`[^\n]*\|\s*planned\s*\|", register_text):
            errors.append(f"SHORTCUT_REGISTER still lists authored Chunk 21 shortcut as planned: {ident}")

    for rel in CHUNK_21_REQUIRED_INDEXES:
        body = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing route for Chunk 21 shortcut card: {ident}")
            if re.search(rf"`{re.escape(ident)}`\s*→\s*planned", body):
                errors.append(f"{rel} has stale planned route for authored Chunk 21 shortcut: {ident}")
        for heading, section_body in markdown_h2_sections(body):
            for ident in required:
                count = section_body.count(f"`{ident}`")
                if count > 1 and "intentional duplicate" not in section_body.lower():
                    errors.append(f"{rel} section {heading!r} contains duplicate active Chunk 21 shortcut route: {ident}")

    for rel in ["llms.txt", "llms-full.txt", "README.md"]:
        body = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing Chunk 21 source-map/root route: {ident}")

    stale_generic_shortcut_route = "retrieve the matching active `vcb.shortcut.*` card from Chunk 20 before falling back"
    required_generic_route_terms = ["active shortcut-card slices", "Chunk 20 harm-reduction cards", "Chunk 21 security/permission cards"]
    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        if stale_generic_shortcut_route in body:
            errors.append(f"{rel} generic shortcut safety route still points only to Chunk 20")
        if "User asks to make a shortcut safer" in body:
            if not all(term in body for term in required_generic_route_terms):
                errors.append(f"{rel} generic shortcut safety route does not cover active Chunk 20 and Chunk 21 shortcut-card slices")

    validate_section_requirements("indexes/INDEX_BY_TASK.md", CHUNK_21_TASK_SECTION_REQUIREMENTS, errors, "Chunk 21 task-index")
    validate_section_requirements("indexes/INDEX_BY_FAILURE_MODE.md", CHUNK_21_FAILURE_SECTION_REQUIREMENTS, errors, "Chunk 21 failure-mode-index")
    validate_section_requirements("indexes/INDEX_FOR_AI_COACHES.md", CHUNK_21_AI_COACH_SECTION_REQUIREMENTS, errors, "Chunk 21 AI-coach-index")
    validate_section_requirements("indexes/INDEX_BY_RISK_LEVEL.md", CHUNK_21_RISK_SECTION_REQUIREMENTS, errors, "Chunk 21 risk-index")
    validate_section_requirements("indexes/INDEX_BY_SHORTCUT.md", CHUNK_21_SHORTCUT_SECTION_REQUIREMENTS, errors, "Chunk 21 shortcut-index")
    validate_planned_companion_routes(CHUNK_21_PLANNED_COMPANION_REQUIREMENTS, errors)

    prompt = read(ROOT / "indexes" / "PROMPT_LIBRARY.md")
    if "## Security and permission shortcut selector" not in prompt:
        errors.append("PROMPT_LIBRARY.md missing Chunk 21 security and permission shortcut selector")
    for ident in required:
        if f"`{ident}`" not in prompt:
            errors.append(f"PROMPT_LIBRARY.md missing Chunk 21 shortcut route: {ident}")

    report_text = read(ROOT / "CHUNK_21_REPORT.md") if (ROOT / "CHUNK_21_REPORT.md").exists() else ""
    changelog_text = read(ROOT / "CHANGELOG.md")
    combined_claims = report_text + "\n" + changelog_text
    claimed_surfaces = {
        "PROMPT_LIBRARY.md": "indexes/PROMPT_LIBRARY.md",
        "INDEX_FOR_AI_COACHES.md": "indexes/INDEX_FOR_AI_COACHES.md",
        "INDEX_BY_SHORTCUT.md": "indexes/INDEX_BY_SHORTCUT.md",
        "INDEX_BY_TASK.md": "indexes/INDEX_BY_TASK.md",
        "INDEX_BY_FAILURE_MODE.md": "indexes/INDEX_BY_FAILURE_MODE.md",
        "INDEX_BY_BUDGET_PROFILE.md": "indexes/INDEX_BY_BUDGET_PROFILE.md",
        "INDEX_BY_RISK_LEVEL.md": "indexes/INDEX_BY_RISK_LEVEL.md",
        "INDEX_BY_RECOVERABILITY.md": "indexes/INDEX_BY_RECOVERABILITY.md",
        "INDEX_BY_CONCEPT.md": "indexes/INDEX_BY_CONCEPT.md",
        "INDEX_BY_STABILITY.md": "indexes/INDEX_BY_STABILITY.md",
        "INDEX_BY_PROJECT_TYPE.md": "indexes/INDEX_BY_PROJECT_TYPE.md",
        "INDEX_BY_CODEX_SURFACE.md": "indexes/INDEX_BY_CODEX_SURFACE.md",
        "INDEX_BY_TOOL_CATEGORY.md": "indexes/INDEX_BY_TOOL_CATEGORY.md",
        "GLOSSARY.md": "indexes/GLOSSARY.md",
    }
    for label, rel in claimed_surfaces.items():
        if label in combined_claims and not any(f"`{ident}`" in read(ROOT / rel) for ident in required):
            errors.append(f"Chunk 21 report/changelog claims {label} routing, but the file has no Chunk 21 shortcut routes")


def validate_chunk_21_report_inventory(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_21":
        return
    path = ROOT / "CHUNK_21_REPORT.md"
    if not path.exists():
        errors.append("CHUNK_21_REPORT.md missing for active Chunk 21")
        return
    text = read(path)
    required_created = set(CHUNK_21_SHORTCUT_IDS.values()) | {"CHUNK_21_REPORT.md"}
    required_updated = {
        "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SHORTCUT_REGISTER.md", "SOURCE_REGISTER.md",
        "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py",
        "indexes/GLOSSARY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md", "indexes/INDEX_BY_CODEX_SURFACE.md",
        "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/INDEX_BY_PROJECT_TYPE.md",
        "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_RISK_LEVEL.md", "indexes/INDEX_BY_SHORTCUT.md",
        "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_TOOL_CATEGORY.md",
        "indexes/INDEX_FOR_AI_COACHES.md", "indexes/PROMPT_LIBRARY.md",
    }
    for rel in sorted(required_created | required_updated):
        if f"`{rel}`" not in text:
            errors.append(f"CHUNK_21_REPORT.md file inventory omits required Chunk 21 path: {rel}")
    if "## Recommended Next Chunk" not in text:
        errors.append("CHUNK_21_REPORT.md missing recommended next chunk section")
    if "## Unresolved questions" not in text or "None." not in text:
        errors.append("CHUNK_21_REPORT.md must explicitly state unresolved questions")
    claims = extract_machine_report_claims(read(path))
    if not claims:
        errors.append("CHUNK_21_REPORT.md missing validation claims block")
    missing = sorted(CHUNK_21_REPORT_REQUIRED_CLAIMS - claims)
    if missing:
        errors.append(f"CHUNK_21_REPORT.md missing implemented validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_21_REPORT_REQUIRED_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_21_REPORT.md has unsupported validation claims: {unsupported}")



CHUNK_22_SHORTCUT_IDS = {
    "vcb.shortcut.skipping_setup": "topics/shortcuts/skipping-setup.md",
    "vcb.shortcut.default_config_forever": "topics/shortcuts/default-config-forever.md",
    "vcb.shortcut.skipping_agents_md": "topics/shortcuts/skipping-agents-md.md",
    "vcb.shortcut.overstuffing_agents_md": "topics/shortcuts/overstuffing-agents-md.md",
    "vcb.shortcut.stale_agents_md": "topics/shortcuts/stale-agents-md.md",
    "vcb.shortcut.unofficial_tools": "topics/shortcuts/unofficial-tools.md",
    "vcb.shortcut.hook_overreach": "topics/shortcuts/hook-overreach.md",
    "vcb.shortcut.trusting_external_tool_output": "topics/shortcuts/trusting-external-tool-output.md",
}

CHUNK_22_REQUIRED_INDEXES = [
    "indexes/GLOSSARY.md",
    "indexes/INDEX_BY_BUDGET_PROFILE.md",
    "indexes/INDEX_BY_CODEX_SURFACE.md",
    "indexes/INDEX_BY_CONCEPT.md",
    "indexes/INDEX_BY_FAILURE_MODE.md",
    "indexes/INDEX_BY_PROJECT_TYPE.md",
    "indexes/INDEX_BY_RECOVERABILITY.md",
    "indexes/INDEX_BY_RISK_LEVEL.md",
    "indexes/INDEX_BY_SHORTCUT.md",
    "indexes/INDEX_BY_STABILITY.md",
    "indexes/INDEX_BY_TASK.md",
    "indexes/INDEX_BY_TOOL_CATEGORY.md",
    "indexes/INDEX_FOR_AI_COACHES.md",
    "indexes/PROMPT_LIBRARY.md",
]

CHUNK_22_SECTION_REQUIREMENTS = [
    ("indexes/INDEX_BY_SHORTCUT.md", "Setup/config/process semantic shortcut routes", set(CHUNK_22_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_RISK_LEVEL.md", "Setup/config/process shortcut risk routes", set(CHUNK_22_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_TASK.md", "Setup/config/process shortcut cards", set(CHUNK_22_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_TASK.md", "Configure Codex or AGENTS.md safely", {"vcb.shortcut.default_config_forever", "vcb.shortcut.skipping_agents_md", "vcb.shortcut.overstuffing_agents_md", "vcb.shortcut.stale_agents_md"}),
    ("indexes/INDEX_BY_TASK.md", "Adopt tools, hooks, plugins, or MCP safely", {"vcb.shortcut.unofficial_tools", "vcb.shortcut.hook_overreach", "vcb.shortcut.trusting_external_tool_output"}),
    ("indexes/INDEX_FOR_AI_COACHES.md", "Coaching Routes — Setup and Process Shortcuts", set(CHUNK_22_SHORTCUT_IDS)),
    ("indexes/PROMPT_LIBRARY.md", "Setup/config/process shortcut selector", set(CHUNK_22_SHORTCUT_IDS)),
]

CHUNK_22_REPORT_REQUIRED_CLAIMS = {
    "New setup/config/process shortcut topic files created in Chunk 22: passed",
    "Required Chunk 22 process/setup shortcut-card slice present: passed",
    "Manifest process_setup_shortcut_cards map matches authored Chunk 22 files: passed",
    "Manifest chunk_22_required_topic_ids matches authored Chunk 22 IDs: passed",
    "Required VCB markers present in new Chunk 22 shortcut files: passed",
    "Required sections present in new Chunk 22 shortcut files: passed",
    "SHORTCUT_REGISTER marks authored Chunk 22 shortcut IDs active: passed",
    "SHORTCUT_REGISTER shortcut rows are inside declared shortcut tables: passed",
    "Primary indexes route active Chunk 22 setup/process shortcut cards: passed",
    "Prompt library routes active Chunk 22 setup/process shortcut cards: passed",
    "AI coach index routes active Chunk 22 setup/process shortcut cards: passed",
    "LLM source maps route active Chunk 22 setup/process shortcut cards: passed",
    "Generic LLM shortcut route covers active Chunk 20, Chunk 21, and Chunk 22 shortcut-card slices: passed",
    "Semantic setup/config/process index sections route active Chunk 22 cards: passed",
    "Stale planned routes for authored Chunk 22 shortcuts are absent from indexes and SHORTCUT_REGISTER: passed",
    "Chunk 22 did not start full shortcut expansion or disallowed topic-card families: passed",
    "Active Chunk 22 report inventory lists created shortcut cards and updated routing/governance files: passed",
    "No single index section contains duplicate active Chunk 22 shortcut rows: passed",
    "No primary index contains multiple full-list sections for the Chunk 22 shortcut-card set: passed",
    "llms.txt / llms-full.txt active-chunk status phrases are not repeated: passed",
    "Active Chunk 22 related-topic IDs resolve to active topic cards: passed",
    "CHANGELOG.md has one current-chunk heading for Chunk 22: passed",
    "Chunk 22 report/changelog routing claims match routed surfaces and consolidated index state: passed",
    "Active Chunk 22 machine-claim catalog matches validator checks: passed",
}



def count_full_list_sections_for_ids(path: Path, required_ids: dict[str, str] | list[str] | tuple[str, ...]) -> list[str]:
    """Return H2 headings whose section lists every required ID.

    Repeating an ID in distinct semantic contexts is allowed. Repeating a full
    current-chunk inventory multiple times in the same index is source-map
    clutter and should fail validation.
    """
    if isinstance(required_ids, dict):
        ids = list(required_ids)
    else:
        ids = list(required_ids)
    headings: list[str] = []
    for heading, section_body in markdown_h2_sections(read(path)):
        if all(f"`{ident}`" in section_body for ident in ids):
            headings.append(heading)
    return headings


def validate_chunk_22_full_list_section_consolidation(errors: list[str]) -> None:
    for rel in CHUNK_22_REQUIRED_INDEXES:
        full_sections = count_full_list_sections_for_ids(ROOT / rel, CHUNK_22_SHORTCUT_IDS)
        if len(full_sections) > 1:
            errors.append(
                f"{rel} contains duplicate full-list Chunk 22 shortcut sections: {full_sections}"
            )


def validate_chunk_22_llm_active_phrase(errors: list[str]) -> None:
    variants = [
        "Setup/process shortcut cards from Chunk 22 are active.",
        "Setup/configuration/process shortcut cards from Chunk 22 are active.",
    ]
    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        counts = {phrase: body.count(phrase) for phrase in variants}
        for phrase, count in counts.items():
            if count > 1:
                errors.append(f"{rel} repeats active Chunk 22 status phrase {phrase!r}: {count} times")
        total = sum(counts.values())
        if rel == "llms.txt" and total != 1:
            errors.append(f"llms.txt must contain exactly one active Chunk 22 status phrase; observed={total}")
        if rel == "llms-full.txt" and total > 1:
            errors.append(f"llms-full.txt must not repeat active Chunk 22 status phrases; observed={total}")


def validate_chunk_22_related_topics(manifest: dict[str, Any], errors: list[str]) -> None:
    active_or_declared = set(manifest.get("topic_cards", {}))
    redirects = manifest.get("topic_namespace_policy", {}).get("topic_id_redirects", {})
    if isinstance(redirects, dict):
        active_or_declared.update(redirects)
        active_or_declared.update(str(v) for v in redirects.values())
    # Chapter IDs are active repository objects even though this manifest tracks
    # authored topic cards separately.
    chapter_id_re = re.compile(r"^id:\s*(vcb\.chapter\.[A-Za-z0-9_.-]+)\s*$", re.M)
    for chapter_path in (ROOT / "chapters").glob("*.md"):
        match = chapter_id_re.search(read(chapter_path))
        if match:
            active_or_declared.add(match.group(1))
    # Register and pricing IDs are valid related routes when they are already
    # declared elsewhere in the repository.
    for register in ["SOURCE_REGISTER.md", "TOOL_REGISTER.md", "SHORTCUT_REGISTER.md", "PRICING_SNAPSHOT_REGISTER.md", "DEPRECATION_REGISTER.md"]:
        path = ROOT / register
        if path.exists():
            active_or_declared.update(re.findall(r"`(vcb\.[A-Za-z0-9_.-]+)`", read(path)))
    for ident, rel in CHUNK_22_SHORTCUT_IDS.items():
        fm = parse_frontmatter(ROOT / rel) or {}
        for related in fm.get("related_topics", []) or []:
            if related not in active_or_declared:
                errors.append(f"{rel} has unresolved related_topic ID: {related}")
        body_related_match = re.search(r"(?ms)^## Related Topics\n(.*?)(?=^## |<!-- VCB:STOP_RETRIEVAL|\Z)", read(ROOT / rel))
        if body_related_match:
            for related in re.findall(r"`(vcb\.[A-Za-z0-9_.-]+)`", body_related_match.group(1)):
                if related not in active_or_declared:
                    errors.append(f"{rel} Related Topics section has unresolved ID: {related}")


def validate_chunk_22_changelog_entry(errors: list[str]) -> None:
    path = ROOT / "CHANGELOG.md"
    body = read(path)
    headings = re.findall(r"(?m)^##\s+.*Chunk 22.*$", body)
    if len(headings) != 1:
        errors.append(f"CHANGELOG.md must contain exactly one Chunk 22 heading; observed={headings}")
    stop = body.find('<!-- VCB:STOP_RETRIEVAL reason="changelog_complete" -->')
    if stop != -1:
        before_stop = body[:stop]
        headings_before_stop = re.findall(r"(?m)^##\s+.*Chunk 22.*$", before_stop)
        if len(headings_before_stop) != 1:
            errors.append("CHANGELOG.md must place the single Chunk 22 entry before VCB:STOP_RETRIEVAL")

def validate_chunk_22_process_setup_shortcut_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_22":
        return
    validate_chunk_22_full_list_section_consolidation(errors)
    validate_chunk_22_llm_active_phrase(errors)
    validate_chunk_22_related_topics(manifest, errors)
    validate_chunk_22_changelog_entry(errors)
    required = CHUNK_22_SHORTCUT_IDS
    active = authored_active_ids()
    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    if "Chunk 22" not in current_checks or "Chunk 21 security/permission" in current_checks or "Chunk 20 shortcut" in current_checks:
        errors.append("manifest.validation_expectations.current_chunk_checks does not name the active Chunk 22 validation scope")
    if manifest.get("process_setup_shortcut_cards") != required:
        errors.append("manifest.process_setup_shortcut_cards does not match Chunk 22 required card map")
    if manifest.get("chunk_22_required_topic_ids") != list(required):
        errors.append("manifest.chunk_22_required_topic_ids does not match required Chunk 22 IDs")
    topic_cards = manifest.get("topic_cards", {})
    for ident, rel in required.items():
        path = ROOT / rel
        if topic_cards.get(ident) != rel:
            errors.append(f"manifest.topic_cards missing Chunk 22 route: {ident} -> {rel}")
        if ident not in active:
            errors.append(f"Chunk 22 required shortcut ID not authored: {ident}")
        if not path.exists():
            errors.append(f"Chunk 22 required shortcut file missing: {rel}")
            continue
        text = read(path)
        fm = parse_frontmatter(path) or {}
        if fm.get("type") != "shortcut" or fm.get("shortcut_type") != "risk_managed_shortcut":
            errors.append(f"{rel} must use type=shortcut and shortcut_type=risk_managed_shortcut")
        if fm.get("status") != "active":
            errors.append(f"{rel} shortcut status must be active")
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in text:
                errors.append(f"{rel} missing required heading: {heading}")
        if f"<!-- VCB:BEGIN_TOPIC id={ident} version=0.1.0 -->" not in text:
            errors.append(f"{rel} missing matching Chunk 22 begin topic marker")
        if f"<!-- VCB:END_TOPIC id={ident} -->" not in text:
            errors.append(f"{rel} missing matching end topic marker")
        if "## Quick Navigation" not in text:
            errors.append(f"{rel} missing shortcut-card Quick Navigation section")

    allowed_shortcut_files = {Path(v).name for v in CHUNK_20_SHORTCUT_IDS.values()} | {Path(v).name for v in CHUNK_21_SHORTCUT_IDS.values()} | {Path(v).name for v in required.values()} | {".gitkeep"}
    observed_shortcut_files = {p.name for p in (ROOT / "topics" / "shortcuts").glob("*")}
    if observed_shortcut_files != allowed_shortcut_files:
        errors.append(f"Chunk 22 shortcut-card scope drift: expected={sorted(allowed_shortcut_files)} observed={sorted(observed_shortcut_files)}")
    for disallowed in ["topics/tool-catalog", "topics/field-practices"]:
        files = [p.name for p in (ROOT / disallowed).glob("*.md")]
        if files:
            errors.append(f"Chunk 22 must not add {disallowed} topic cards: {files}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md")]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 22 must not expand pricing snapshots: {pricing_files}")

    statuses = shortcut_register_statuses()
    register_text = read(ROOT / "SHORTCUT_REGISTER.md")
    for ident in required:
        if statuses.get(ident) != "active":
            errors.append(f"SHORTCUT_REGISTER row for {ident} must be active; observed={statuses.get(ident)!r}")
        if re.search(rf"`{re.escape(ident)}`[^\n]*\|\s*planned\s*\|", register_text):
            errors.append(f"SHORTCUT_REGISTER still lists authored Chunk 22 shortcut as planned: {ident}")

    active_vcb_ids = authored_active_ids()
    related_topic_allowed = active_vcb_ids

    for ident, rel in required.items():
        path = ROOT / rel
        text = read(path)
        fm = parse_frontmatter(path) or {}
        fm_related = set(str(value) for value in (fm.get("related_topics") or []) if str(value).startswith("vcb."))
        body_related: set[str] = set()
        related_match = re.search(
            r"(?ms)^## Related Topics\n(.*?)(?=^## |^<!-- VCB:STOP_RETRIEVAL|\Z)",
            text,
        )
        if related_match:
            body_related.update(re.findall(r"`?(vcb\.[A-Za-z0-9_.-]+)`?", related_match.group(1)))
        unresolved_related = sorted((fm_related | body_related) - related_topic_allowed)
        if unresolved_related:
            errors.append(f"{rel} has unresolved related_topics IDs: {unresolved_related}")

    for rel in CHUNK_22_REQUIRED_INDEXES:
        body = read(ROOT / rel)
        duplicate_headings = [h for h, c in Counter(re.findall(r"^## (.+)$", body, flags=re.M)).items() if c > 1 and "Setup" in h and "Shortcut" in h]
        if duplicate_headings:
            errors.append(f"{rel} contains duplicate setup/process shortcut headings: {duplicate_headings}")
        full_list_sections = []
        for heading, section_body in markdown_h2_sections(body):
            section_ids = set(re.findall(r"`(vcb\.shortcut\.[A-Za-z0-9_.-]+)`", section_body))
            if set(required).issubset(section_ids):
                full_list_sections.append(heading)
        if len(full_list_sections) > 1:
            errors.append(f"{rel} contains duplicate full-list Chunk 22 shortcut sections: {full_list_sections}")
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing route for Chunk 22 shortcut card: {ident}")
            if re.search(rf"`{re.escape(ident)}`\s*→\s*planned", body):
                errors.append(f"{rel} has stale planned route for authored Chunk 22 shortcut: {ident}")
        for heading, section_body in markdown_h2_sections(body):
            for ident in required:
                count = section_body.count(f"`{ident}`")
                if count > 1 and "intentional duplicate" not in section_body.lower():
                    errors.append(f"{rel} section {heading!r} contains duplicate active Chunk 22 shortcut route: {ident}")

    for rel in ["README.md", "llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing Chunk 22 source-map/root route: {ident}")
    required_terms = ["active shortcut-card slices", "Chunk 20 harm-reduction cards", "Chunk 21 security/permission cards", "Chunk 22 setup/process cards"]
    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        if "User asks to make a shortcut safer" in body and not all(term in body for term in required_terms):
            errors.append(f"{rel} generic shortcut safety route does not cover active Chunk 20, Chunk 21, and Chunk 22 shortcut-card slices")
        status_sentences = [
            sentence.strip()
            for sentence in re.split(r"(?<=\.)\s+", body)
            if "Chunk 22" in sentence and "are active" in sentence
        ]
        repeated_status = sorted(sentence for sentence, count in Counter(status_sentences).items() if count > 1)
        if repeated_status:
            errors.append(f"{rel} repeats active Chunk 22 source-map status phrase(s): {repeated_status}")

    for rel, heading, ids in CHUNK_22_SECTION_REQUIREMENTS:
        sections = {h: b for h, b in markdown_h2_sections(read(ROOT / rel))}
        if heading not in sections:
            errors.append(f"{rel} missing Chunk 22 semantic section: {heading}")
            continue
        for ident in ids:
            if f"`{ident}`" not in sections[heading]:
                errors.append(f"{rel} section {heading!r} missing active Chunk 22 route: {ident}")

    combined_claims = (read(ROOT / "CHUNK_22_REPORT.md") if (ROOT / "CHUNK_22_REPORT.md").exists() else "") + "\n" + read(ROOT / "CHANGELOG.md")
    claimed_surfaces = {label: rel for label, rel in {
        "PROMPT_LIBRARY.md": "indexes/PROMPT_LIBRARY.md",
        "INDEX_FOR_AI_COACHES.md": "indexes/INDEX_FOR_AI_COACHES.md",
        "INDEX_BY_SHORTCUT.md": "indexes/INDEX_BY_SHORTCUT.md",
        "INDEX_BY_TASK.md": "indexes/INDEX_BY_TASK.md",
        "INDEX_BY_FAILURE_MODE.md": "indexes/INDEX_BY_FAILURE_MODE.md",
        "INDEX_BY_BUDGET_PROFILE.md": "indexes/INDEX_BY_BUDGET_PROFILE.md",
        "INDEX_BY_RISK_LEVEL.md": "indexes/INDEX_BY_RISK_LEVEL.md",
        "INDEX_BY_RECOVERABILITY.md": "indexes/INDEX_BY_RECOVERABILITY.md",
        "INDEX_BY_CONCEPT.md": "indexes/INDEX_BY_CONCEPT.md",
        "INDEX_BY_STABILITY.md": "indexes/INDEX_BY_STABILITY.md",
        "INDEX_BY_PROJECT_TYPE.md": "indexes/INDEX_BY_PROJECT_TYPE.md",
        "INDEX_BY_CODEX_SURFACE.md": "indexes/INDEX_BY_CODEX_SURFACE.md",
        "INDEX_BY_TOOL_CATEGORY.md": "indexes/INDEX_BY_TOOL_CATEGORY.md",
        "GLOSSARY.md": "indexes/GLOSSARY.md",
    }.items()}
    for label, rel in claimed_surfaces.items():
        if label in combined_claims and not any(f"`{ident}`" in read(ROOT / rel) for ident in required):
            errors.append(f"Chunk 22 report/changelog claims {label} routing, but the file has no Chunk 22 shortcut routes")
        if label in combined_claims:
            body = read(ROOT / rel)
            full_list_sections = [
                heading
                for heading, section_body in markdown_h2_sections(body)
                if set(required).issubset(set(re.findall(r"`(vcb\.shortcut\.[A-Za-z0-9_.-]+)`", section_body)))
            ]
            if len(full_list_sections) > 1:
                errors.append(f"Chunk 22 report/changelog claims {label} routing, but duplicate full-list sections remain: {full_list_sections}")

    changelog_text = read(ROOT / "CHANGELOG.md")
    chunk22_headings = re.findall(r"^## .*Chunk 22.*$", changelog_text, flags=re.M)
    if len(chunk22_headings) != 1:
        errors.append(f"CHANGELOG.md must contain exactly one Chunk 22 heading; observed={chunk22_headings}")


def validate_chunk_22_report_inventory(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_22":
        return
    path = ROOT / "CHUNK_22_REPORT.md"
    if not path.exists():
        errors.append("CHUNK_22_REPORT.md missing for active Chunk 22")
        return
    text = read(path)
    required_created = set(CHUNK_22_SHORTCUT_IDS.values()) | {"CHUNK_22_REPORT.md"}
    required_updated = {
        "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SHORTCUT_REGISTER.md", "SOURCE_REGISTER.md",
        "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py",
        "indexes/GLOSSARY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md", "indexes/INDEX_BY_CODEX_SURFACE.md",
        "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/INDEX_BY_PROJECT_TYPE.md",
        "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_RISK_LEVEL.md", "indexes/INDEX_BY_SHORTCUT.md",
        "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_TOOL_CATEGORY.md",
        "indexes/INDEX_FOR_AI_COACHES.md", "indexes/PROMPT_LIBRARY.md",
    }
    for rel in sorted(required_created | required_updated):
        if f"`{rel}`" not in text:
            errors.append(f"CHUNK_22_REPORT.md file inventory omits required Chunk 22 path: {rel}")
    if "## Recommended Next Chunk" not in text:
        errors.append("CHUNK_22_REPORT.md missing recommended next chunk section")
    if "## Unresolved questions" not in text or "None." not in text:
        errors.append("CHUNK_22_REPORT.md must explicitly state unresolved questions")
    claims = extract_machine_report_claims(text)
    if not claims:
        errors.append("CHUNK_22_REPORT.md missing validation claims block")
    missing = sorted(CHUNK_22_REPORT_REQUIRED_CLAIMS - claims)
    if missing:
        errors.append(f"CHUNK_22_REPORT.md missing implemented validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_22_REPORT_REQUIRED_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_22_REPORT.md has unsupported validation claims: {unsupported}")



CHUNK_23_SHORTCUT_IDS = {
    "vcb.shortcut.skill_overkill": "topics/shortcuts/skill-overkill.md",
    "vcb.shortcut.skill_sprawl": "topics/shortcuts/skill-sprawl.md",
    "vcb.shortcut.tool_sprawl": "topics/shortcuts/tool-sprawl.md",
    "vcb.shortcut.tool_sprawl_mcp": "topics/shortcuts/tool-sprawl-mcp.md",
    "vcb.shortcut.brittle_hooks": "topics/shortcuts/brittle-hooks.md",
    "vcb.shortcut.process_overhead_for_tiny_project": "topics/shortcuts/process-overhead-for-tiny-project.md",
    "vcb.shortcut.team_workflow_without_team": "topics/shortcuts/team-workflow-without-team.md",
    "vcb.shortcut.copy_pasting_playbook_blindly": "topics/shortcuts/copy-pasting-playbook-blindly.md",
}

CHUNK_23_REQUIRED_INDEXES = [
    "indexes/GLOSSARY.md",
    "indexes/INDEX_BY_BUDGET_PROFILE.md",
    "indexes/INDEX_BY_CODEX_SURFACE.md",
    "indexes/INDEX_BY_CONCEPT.md",
    "indexes/INDEX_BY_FAILURE_MODE.md",
    "indexes/INDEX_BY_PROJECT_TYPE.md",
    "indexes/INDEX_BY_RECOVERABILITY.md",
    "indexes/INDEX_BY_RISK_LEVEL.md",
    "indexes/INDEX_BY_SHORTCUT.md",
    "indexes/INDEX_BY_STABILITY.md",
    "indexes/INDEX_BY_TASK.md",
    "indexes/INDEX_BY_TOOL_CATEGORY.md",
    "indexes/INDEX_FOR_AI_COACHES.md",
    "indexes/PROMPT_LIBRARY.md",
]

CHUNK_23_SECTION_REQUIREMENTS = [
    ("indexes/INDEX_BY_SHORTCUT.md", "Tool-sprawl, skill, MCP, and reusable workflow shortcut routes", set(CHUNK_23_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_RISK_LEVEL.md", "Tool-sprawl, skill, and reusable process shortcut risk routes", set(CHUNK_23_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_FAILURE_MODE.md", "Tool sprawl, brittle process, and reusable workflow failure modes", set(CHUNK_23_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_TASK.md", "Adopt skills, MCP, plugins, hooks, or reusable process safely", set(CHUNK_23_SHORTCUT_IDS)),
    ("indexes/INDEX_FOR_AI_COACHES.md", "Coaching Routes — Tool-Sprawl, Skill, and Process Shortcuts", set(CHUNK_23_SHORTCUT_IDS)),
    ("indexes/PROMPT_LIBRARY.md", "Tool-sprawl/skill/process shortcut selector", set(CHUNK_23_SHORTCUT_IDS)),
]

CHUNK_23_REPORT_REQUIRED_CLAIMS = {
    "New tool-sprawl/skill/reusable-workflow shortcut topic files created in Chunk 23: passed",
    "Required Chunk 23 tool-sprawl/skill shortcut-card slice present: passed",
    "Manifest tool_sprawl_skill_shortcut_cards map matches authored Chunk 23 files: passed",
    "Manifest chunk_23_required_topic_ids matches authored Chunk 23 IDs: passed",
    "Manifest redirects do not shadow active Chunk 23 canonical IDs: passed",
    "Required VCB markers present in new Chunk 23 shortcut files: passed",
    "Required sections present in new Chunk 23 shortcut files: passed",
    "SHORTCUT_REGISTER marks authored Chunk 23 shortcut IDs active: passed",
    "SHORTCUT_REGISTER shortcut rows are inside declared shortcut tables: passed",
    "Primary indexes route active Chunk 23 tool-sprawl/skill shortcut cards: passed",
    "Prompt library routes active Chunk 23 tool-sprawl/skill shortcut cards: passed",
    "AI coach index routes active Chunk 23 tool-sprawl/skill shortcut cards: passed",
    "LLM source maps route active Chunk 23 tool-sprawl/skill shortcut cards: passed",
    "LLM source maps contain one consolidated Chunk 23 full-list routing section: passed",
    "General Fast Routing includes direct Chunk 23 shortcut-intent routes: passed",
    "Generic LLM shortcut route covers active Chunk 20, Chunk 21, Chunk 22, and Chunk 23 shortcut-card slices: passed",
    "Semantic tool-sprawl/skill/process index sections route active Chunk 23 cards: passed",
    "Stale planned routes for authored Chunk 23 shortcuts are absent from indexes and SHORTCUT_REGISTER: passed",
    "Chunk 23 did not start full shortcut expansion or disallowed topic-card families: passed",
    "Active Chunk 23 report inventory lists created shortcut cards and updated routing/governance files: passed",
    "No single index section contains duplicate active Chunk 23 shortcut rows: passed",
    "No primary index contains multiple full-list sections for the Chunk 23 shortcut-card set: passed",
    "llms.txt / llms-full.txt active-chunk status phrases are not repeated: passed",
    "Active Chunk 23 related-topic IDs resolve to active topic cards: passed",
    "CHANGELOG.md has one current-chunk heading for Chunk 23: passed",
    "Chunk 23 report/changelog routing claims match routed surfaces and consolidated index state: passed",
    "Manifest redirect maps do not redirect active Chunk 23 canonical IDs away from authored cards: passed",
    "LLM source maps contain one compact Chunk 23 full-list section and no duplicate adjacent full-list sections: passed",
    "General Fast Routing includes semantic Chunk 23 shortcut intents before fallback routing: passed",
    "Chunk 23 source-map and stale-route claims are backed by redirect-shadowing and LLM-map validator checks: passed",
    "Active Chunk 23 machine-claim catalog matches validator checks: passed",
}


def validate_chunk_23_tool_sprawl_skill_shortcut_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_23":
        return
    required = CHUNK_23_SHORTCUT_IDS
    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    if "Chunk 23" not in current_checks or "tool-sprawl" not in current_checks:
        errors.append("manifest.validation_expectations.current_chunk_checks must name Chunk 23 tool-sprawl/skill shortcut checks")
    if manifest.get("tool_sprawl_skill_shortcut_cards") != required:
        errors.append("manifest.tool_sprawl_skill_shortcut_cards does not match Chunk 23 required card map")
    if manifest.get("chunk_23_required_topic_ids") != list(required):
        errors.append("manifest.chunk_23_required_topic_ids does not match required Chunk 23 IDs")

    active_ids = authored_active_ids()
    for policy_name in ["topic_namespace_policy", "namespace_policy"]:
        redirects = manifest.get(policy_name, {}).get("topic_id_redirects", {})
        if not isinstance(redirects, dict):
            continue
        for key, value in redirects.items():
            if key in active_ids:
                errors.append(f"manifest.{policy_name}.topic_id_redirects uses active canonical ID as redirect key: {key} -> {value}")
            if key in required:
                errors.append(f"manifest.{policy_name}.topic_id_redirects must not shadow authored Chunk 23 ID: {key} -> {value}")

    topic_cards = manifest.get("topic_cards", {})
    for ident, rel in required.items():
        path = ROOT / rel
        if topic_cards.get(ident) != rel:
            errors.append(f"manifest.topic_cards missing Chunk 23 route: {ident} -> {rel}")
        if not path.exists():
            errors.append(f"missing Chunk 23 shortcut file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != ident or fm.get("type") != "shortcut" or fm.get("status") != "active":
            errors.append(f"frontmatter for {rel} does not declare active shortcut ID {ident}")
        body = read(path)
        if f"<!-- VCB:BEGIN_TOPIC id={ident}" not in body:
            errors.append(f"{rel} missing matching Chunk 23 begin topic marker")
        if f"<!-- VCB:END_TOPIC id={ident} -->" not in body:
            errors.append(f"{rel} missing matching end topic marker")
        if "## Quick Navigation" not in body:
            errors.append(f"{rel} missing shortcut-card Quick Navigation section")

    allowed_shortcut_files = (
        {Path(v).name for v in CHUNK_20_SHORTCUT_IDS.values()}
        | {Path(v).name for v in CHUNK_21_SHORTCUT_IDS.values()}
        | {Path(v).name for v in CHUNK_22_SHORTCUT_IDS.values()}
        | {Path(v).name for v in required.values()}
        | {".gitkeep"}
    )
    observed_shortcut_files = {p.name for p in (ROOT / "topics" / "shortcuts").glob("*")}
    if observed_shortcut_files != allowed_shortcut_files:
        errors.append(f"Chunk 23 shortcut-card scope drift: expected={sorted(allowed_shortcut_files)} observed={sorted(observed_shortcut_files)}")
    for disallowed in ["topics/tool-catalog", "topics/field-practices"]:
        files = [p.name for p in (ROOT / disallowed).glob("*.md")]
        if files:
            errors.append(f"Chunk 23 must not add {disallowed} topic cards: {files}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md")]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 23 must not expand pricing snapshots: {pricing_files}")

    statuses = shortcut_register_statuses()
    register_text = read(ROOT / "SHORTCUT_REGISTER.md")
    for ident in required:
        if statuses.get(ident) != "active":
            errors.append(f"SHORTCUT_REGISTER row for {ident} must be active; observed={statuses.get(ident)!r}")
        if re.search(rf"`{re.escape(ident)}`[^\n]*\|\s*planned\s*\|", register_text):
            errors.append(f"SHORTCUT_REGISTER still lists authored Chunk 23 shortcut as planned: {ident}")

    for rel in CHUNK_23_REQUIRED_INDEXES:
        body = read(ROOT / rel)
        full_list_sections: list[str] = []
        for heading, section_body in markdown_h2_sections(body):
            section_ids = set(re.findall(r"`(vcb\.shortcut\.[A-Za-z0-9_.-]+)`", section_body))
            if set(required).issubset(section_ids):
                full_list_sections.append(heading)
            for ident in required:
                count = section_body.count(f"`{ident}`")
                if count > 1 and "intentional duplicate" not in section_body.lower():
                    errors.append(f"{rel} section {heading!r} contains duplicate active Chunk 23 shortcut route: {ident}")
        if len(full_list_sections) > 1:
            errors.append(f"{rel} contains duplicate full-list Chunk 23 shortcut sections: {full_list_sections}")
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing route for Chunk 23 shortcut card: {ident}")
            if re.search(rf"`{re.escape(ident)}`\s*→\s*planned", body):
                errors.append(f"{rel} has stale planned route for authored Chunk 23 shortcut: {ident}")

    for rel in ["README.md", "llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing Chunk 23 source-map/root route: {ident}")
    required_terms = ["active shortcut-card slices", "Chunk 20 harm-reduction cards", "Chunk 21 security/permission cards", "Chunk 22 setup/process cards", "Chunk 23 tool-sprawl/skill/reusable-workflow cards"]
    semantic_terms = ["too many skills", "MCP", "brittle hooks", "adding tools instead of shipping", "copied playbooks"]
    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        if "User asks to make a shortcut safer" in body and not all(term in body for term in required_terms):
            errors.append(f"{rel} generic shortcut safety route does not cover active Chunk 20, Chunk 21, Chunk 22, and Chunk 23 shortcut-card slices")
        variants = [
            "Tool-sprawl/skill/reusable-workflow shortcut cards from Chunk 23 are active.",
            "Tool-sprawl, skill, MCP, and reusable-workflow shortcut cards from Chunk 23 are active.",
        ]
        total = sum(body.count(v) for v in variants)
        if rel == "llms.txt" and total != 1:
            errors.append(f"llms.txt must contain exactly one active Chunk 23 status phrase; observed={total}")
        if rel == "llms-full.txt" and total > 1:
            errors.append(f"llms-full.txt must not repeat active Chunk 23 status phrases; observed={total}")
        full_list_sections = [heading for heading, section_body in markdown_h2_sections(body) if set(required).issubset(set(re.findall(r"`(vcb\.shortcut\.[A-Za-z0-9_.-]+)`", section_body)))]
        if len(full_list_sections) != 1:
            errors.append(f"{rel} must contain exactly one consolidated full-list section for Chunk 23 shortcut cards; observed={full_list_sections}")
        fast_sections = [section_body for heading, section_body in markdown_h2_sections(body) if heading == "Fast Routing"]
        fast_body = "\n".join(fast_sections)
        fast_lower = fast_body.lower()
        if not fast_body:
            errors.append(f"{rel} missing general Fast Routing section")
        elif not all(term.lower() in fast_lower for term in semantic_terms) or "chunk 23" not in fast_lower or "vcb.shortcut" not in fast_lower:
            errors.append(f"{rel} general Fast Routing lacks direct semantic Chunk 23 shortcut-intent route")
        semantic_pos = min([p for p in (fast_lower.find("too many skills"), fast_lower.find("mcp"), fast_lower.find("brittle hooks")) if p >= 0] or [-1])
        fallback_positions = [p for p in (fast_lower.find("chapter 38"), fast_lower.find("shortcut_register"), fast_lower.find("beyond authored shortcut cards")) if p >= 0]
        if semantic_pos < 0:
            errors.append(f"{rel} general Fast Routing lacks Chunk 23 semantic route anchor terms")
        elif fallback_positions and semantic_pos > min(fallback_positions):
            errors.append(f"{rel} Chunk 23 semantic Fast Routing appears after shortcut fallback")

    for rel, heading, ids in CHUNK_23_SECTION_REQUIREMENTS:
        sections = {h: b for h, b in markdown_h2_sections(read(ROOT / rel))}
        if heading not in sections:
            errors.append(f"{rel} missing Chunk 23 semantic section: {heading}")
            continue
        for ident in ids:
            if f"`{ident}`" not in sections[heading]:
                errors.append(f"{rel} section {heading!r} missing active Chunk 23 route: {ident}")

    active_vcb_ids = authored_active_ids()
    for ident, rel in required.items():
        path = ROOT / rel
        fm = parse_frontmatter(path) or {}
        body = read(path)
        fm_related = set(str(value) for value in (fm.get("related_topics") or []) if str(value).startswith("vcb."))
        body_related: set[str] = set()
        related_match = re.search(r"(?ms)^## Related Topics\n(.*?)(?=^## |^<!-- VCB:STOP_RETRIEVAL|\Z)", body)
        if related_match:
            body_related.update(re.findall(r"`?(vcb\.[A-Za-z0-9_.-]+)`?", related_match.group(1)))
        unresolved = sorted((fm_related | body_related) - active_vcb_ids)
        if unresolved:
            errors.append(f"{rel} has unresolved related_topics IDs: {unresolved}")

    changelog_text = read(ROOT / "CHANGELOG.md")
    chunk23_headings = re.findall(r"^## .*Chunk 23.*$", changelog_text, flags=re.M)
    if len(chunk23_headings) != 1:
        errors.append(f"CHANGELOG.md must contain exactly one Chunk 23 heading; observed={chunk23_headings}")

    combined_claims = (read(ROOT / "CHUNK_23_REPORT.md") if (ROOT / "CHUNK_23_REPORT.md").exists() else "") + "\n" + read(ROOT / "CHANGELOG.md")
    for label, rel in {
        "PROMPT_LIBRARY.md": "indexes/PROMPT_LIBRARY.md",
        "INDEX_FOR_AI_COACHES.md": "indexes/INDEX_FOR_AI_COACHES.md",
        "INDEX_BY_SHORTCUT.md": "indexes/INDEX_BY_SHORTCUT.md",
        "INDEX_BY_TASK.md": "indexes/INDEX_BY_TASK.md",
        "INDEX_BY_FAILURE_MODE.md": "indexes/INDEX_BY_FAILURE_MODE.md",
        "INDEX_BY_BUDGET_PROFILE.md": "indexes/INDEX_BY_BUDGET_PROFILE.md",
        "INDEX_BY_RISK_LEVEL.md": "indexes/INDEX_BY_RISK_LEVEL.md",
        "INDEX_BY_RECOVERABILITY.md": "indexes/INDEX_BY_RECOVERABILITY.md",
        "INDEX_BY_CONCEPT.md": "indexes/INDEX_BY_CONCEPT.md",
        "INDEX_BY_STABILITY.md": "indexes/INDEX_BY_STABILITY.md",
        "INDEX_BY_PROJECT_TYPE.md": "indexes/INDEX_BY_PROJECT_TYPE.md",
        "INDEX_BY_CODEX_SURFACE.md": "indexes/INDEX_BY_CODEX_SURFACE.md",
        "INDEX_BY_TOOL_CATEGORY.md": "indexes/INDEX_BY_TOOL_CATEGORY.md",
        "GLOSSARY.md": "indexes/GLOSSARY.md",
    }.items():
        if label in combined_claims and not any(f"`{ident}`" in read(ROOT / rel) for ident in required):
            errors.append(f"Chunk 23 report/changelog claims {label} routing, but the file has no Chunk 23 shortcut routes")


def validate_chunk_23_report_inventory(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_23":
        return
    path = ROOT / "CHUNK_23_REPORT.md"
    if not path.exists():
        errors.append("CHUNK_23_REPORT.md missing for active Chunk 23")
        return
    text = read(path)
    required_created = set(CHUNK_23_SHORTCUT_IDS.values()) | {"CHUNK_23_REPORT.md"}
    required_updated = {
        "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SHORTCUT_REGISTER.md", "SOURCE_REGISTER.md",
        "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py",
        "indexes/GLOSSARY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md", "indexes/INDEX_BY_CODEX_SURFACE.md",
        "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/INDEX_BY_PROJECT_TYPE.md",
        "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_RISK_LEVEL.md", "indexes/INDEX_BY_SHORTCUT.md",
        "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_TOOL_CATEGORY.md",
        "indexes/INDEX_FOR_AI_COACHES.md", "indexes/PROMPT_LIBRARY.md",
    }
    for rel in sorted(required_created | required_updated):
        if f"`{rel}`" not in text:
            errors.append(f"CHUNK_23_REPORT.md file inventory omits required Chunk 23 path: {rel}")
    if "## Recommended Next Chunk" not in text:
        errors.append("CHUNK_23_REPORT.md missing recommended next chunk section")
    if "## Unresolved questions" not in text or "None." not in text:
        errors.append("CHUNK_23_REPORT.md must explicitly state unresolved questions")
    claims = extract_machine_report_claims(text)
    if not claims:
        errors.append("CHUNK_23_REPORT.md missing validation claims block")
    missing = sorted(CHUNK_23_REPORT_REQUIRED_CLAIMS - claims)
    if missing:
        errors.append(f"CHUNK_23_REPORT.md missing implemented validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_23_REPORT_REQUIRED_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_23_REPORT.md has unsupported validation claims: {unsupported}")


CHUNK_24_SHORTCUT_IDS = {'vcb.shortcut.best_of_n_without_review': 'topics/shortcuts/best-of-n-without-review.md',
 'vcb.shortcut.cherry_picking_ai_answers': 'topics/shortcuts/cherry-picking-ai-answers.md',
 'vcb.shortcut.consensus_as_correctness': 'topics/shortcuts/consensus-as-correctness.md',
 'vcb.shortcut.ignoring_model_biases': 'topics/shortcuts/ignoring-model-biases.md',
 'vcb.shortcut.many_ais_same_files': 'topics/shortcuts/many-ais-same-files.md',
 'vcb.shortcut.model_routing_guesswork': 'topics/shortcuts/model-routing-guesswork.md',
 'vcb.shortcut.parallel_agents_edit_same_files': 'topics/shortcuts/parallel-agents-edit-same-files.md',
 'vcb.shortcut.subagent_swarm': 'topics/shortcuts/subagent-swarm.md',
 'vcb.shortcut.trusting_estimates_before_inspection': 'topics/shortcuts/trusting-estimates-before-inspection.md'}

CHUNK_24_REQUIRED_INDEXES = ['indexes/GLOSSARY.md',
 'indexes/INDEX_BY_BUDGET_PROFILE.md',
 'indexes/INDEX_BY_CODEX_SURFACE.md',
 'indexes/INDEX_BY_CONCEPT.md',
 'indexes/INDEX_BY_FAILURE_MODE.md',
 'indexes/INDEX_BY_PROJECT_TYPE.md',
 'indexes/INDEX_BY_RECOVERABILITY.md',
 'indexes/INDEX_BY_RISK_LEVEL.md',
 'indexes/INDEX_BY_SHORTCUT.md',
 'indexes/INDEX_BY_STABILITY.md',
 'indexes/INDEX_BY_TASK.md',
 'indexes/INDEX_BY_TOOL_CATEGORY.md',
 'indexes/INDEX_FOR_AI_COACHES.md',
 'indexes/PROMPT_LIBRARY.md']

CHUNK_24_SECTION_REQUIREMENTS = [
    ("indexes/INDEX_BY_SHORTCUT.md", "Multi-AI, answer-selection, and model-bias shortcut routes", set(CHUNK_24_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_FAILURE_MODE.md", "Multi-AI and model-bias failure routes", set(CHUNK_24_SHORTCUT_IDS)),
    ("indexes/INDEX_FOR_AI_COACHES.md", "Coaching routes for multi-AI/model-bias shortcuts", set(CHUNK_24_SHORTCUT_IDS)),
    ("indexes/PROMPT_LIBRARY.md", "Multi-AI/model-bias shortcut selector", set(CHUNK_24_SHORTCUT_IDS)),
    ("indexes/INDEX_BY_RISK_LEVEL.md", "High-risk multi-AI and model-bias shortcuts", set(CHUNK_24_SHORTCUT_IDS)),
]

CHUNK_24_SEMANTIC_SECTION_REQUIREMENTS = [
    ("indexes/INDEX_BY_SHORTCUT.md", "Advanced agentic workflow shortcuts", {
        "vcb.shortcut.parallel_agents_edit_same_files",
        "vcb.shortcut.many_ais_same_files",
        "vcb.shortcut.subagent_swarm",
    }),
    ("indexes/INDEX_BY_TASK.md", "Use other AIs with Codex", {
        "vcb.shortcut.many_ais_same_files",
        "vcb.shortcut.parallel_agents_edit_same_files",
        "vcb.shortcut.best_of_n_without_review",
        "vcb.shortcut.cherry_picking_ai_answers",
        "vcb.shortcut.consensus_as_correctness",
        "vcb.shortcut.model_routing_guesswork",
    }),
    ("indexes/INDEX_BY_TASK.md", "Diagnose bad estimates and confident wrong output", {
        "vcb.shortcut.trusting_estimates_before_inspection",
        "vcb.shortcut.ignoring_model_biases",
        "vcb.shortcut.consensus_as_correctness",
        "vcb.shortcut.best_of_n_without_review",
    }),
    ("indexes/INDEX_BY_FAILURE_MODE.md", "Bad estimates and confident wrong summaries", {
        "vcb.shortcut.trusting_estimates_before_inspection",
        "vcb.shortcut.ignoring_model_biases",
        "vcb.shortcut.consensus_as_correctness",
        "vcb.shortcut.best_of_n_without_review",
        "vcb.shortcut.cherry_picking_ai_answers",
    }),
    ("indexes/INDEX_FOR_AI_COACHES.md", "Human is overtrusting estimates or confident model output", {
        "vcb.shortcut.trusting_estimates_before_inspection",
        "vcb.shortcut.ignoring_model_biases",
        "vcb.shortcut.consensus_as_correctness",
        "vcb.shortcut.cherry_picking_ai_answers",
        "vcb.shortcut.best_of_n_without_review",
    }),
    ("indexes/INDEX_BY_CONCEPT.md", "Codex limitations and model biases", {
        "vcb.shortcut.ignoring_model_biases",
        "vcb.shortcut.trusting_estimates_before_inspection",
        "vcb.shortcut.consensus_as_correctness",
        "vcb.shortcut.model_routing_guesswork",
    }),
    ("indexes/INDEX_BY_CONCEPT.md", "Tool stack and multi-AI workflow", {
        "vcb.shortcut.many_ais_same_files",
        "vcb.shortcut.parallel_agents_edit_same_files",
        "vcb.shortcut.best_of_n_without_review",
        "vcb.shortcut.cherry_picking_ai_answers",
        "vcb.shortcut.model_routing_guesswork",
        "vcb.shortcut.subagent_swarm",
    }),
    ("indexes/PROMPT_LIBRARY.md", "Model limitation guardrail prompt", {
        "vcb.shortcut.trusting_estimates_before_inspection",
        "vcb.shortcut.ignoring_model_biases",
        "vcb.shortcut.consensus_as_correctness",
        "vcb.shortcut.best_of_n_without_review",
        "vcb.shortcut.cherry_picking_ai_answers",
    }),
    ("indexes/PROMPT_LIBRARY.md", "Subagent review prompt", {
        "vcb.shortcut.subagent_swarm",
        "vcb.shortcut.parallel_agents_edit_same_files",
    }),
]

CHUNK_24_REPORT_REQUIRED_CLAIMS = {'AI coach index routes active Chunk 24 multi-AI/model-bias shortcut cards: passed',
 'Active Chunk 24 machine-claim catalog matches validator checks: passed',
 'Active Chunk 24 related-topic IDs resolve to active topic cards: passed',
 'Active Chunk 24 report inventory lists created shortcut cards and updated routing/governance files: passed',
 'CHANGELOG.md has one current-chunk heading for Chunk 24: passed',
 'Chunk 24 did not start full shortcut expansion or disallowed topic-card families: passed',
 'Chunk 24 report/changelog routing claims match routed surfaces and consolidated index state: passed',
 'General Fast Routing includes semantic Chunk 24 multi-AI/model-bias shortcut intents before fallback routing: passed',
 'Generic LLM shortcut route covers active Chunk 20, Chunk 21, Chunk 22, Chunk 23, and Chunk 24 shortcut-card slices: '
 'passed',
 'LLM source maps route active Chunk 24 multi-AI/model-bias shortcut cards: passed',
 'Manifest chunk_24_required_topic_ids matches authored Chunk 24 IDs: passed',
 'Manifest multi_ai_model_bias_shortcut_cards map matches authored Chunk 24 files: passed',
 'Manifest redirects do not shadow active Chunk 24 canonical IDs: passed',
 'New multi-AI/model-bias shortcut topic files created in Chunk 24: passed',
 'No primary index contains multiple full-list sections for the Chunk 24 shortcut-card set: passed',
 'No single index section contains duplicate active Chunk 24 shortcut rows: passed',
 'Primary indexes route active Chunk 24 multi-AI/model-bias shortcut cards: passed',
 'Prompt library routes active Chunk 24 multi-AI/model-bias shortcut cards: passed',
 'Failure-mode bad-estimate semantic route covers active Chunk 24 estimate/model-bias cards: passed',
 'README next-chunk scope matches Chunk 25 parallel/cloud/automation scope: passed',
 'Required Chunk 24 multi-AI/model-bias shortcut-card slice present: passed',
 'Required VCB markers present in new Chunk 24 shortcut files: passed',
 'Required sections present in new Chunk 24 shortcut files: passed',
 'SHORTCUT_REGISTER marks authored Chunk 24 shortcut IDs active: passed',
 'Semantic risk/shortcut/task index sections route active Chunk 24 cards: passed',
 'Stale planned routes for authored Chunk 24 shortcuts are absent from indexes and SHORTCUT_REGISTER: passed'}


def validate_chunk_24_multi_ai_model_bias_shortcut_slice(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_24":
        return
    required = CHUNK_24_SHORTCUT_IDS

    readme_sections = {h: b for h, b in markdown_h2_sections(read(ROOT / "README.md"))}
    readme_next = readme_sections.get("Next Chunk", "")
    manifest_next_id = str(manifest.get("next_recommended_chunk", {}).get("id", ""))
    stale_readme_scope_phrases = [
        "bounded multi-AI, model-bias, answer-selection, and estimate-trust shortcut cards",
        "approved multi-AI/model-bias slice",
    ]
    if manifest_next_id and f"`{manifest_next_id}`" not in readme_next:
        errors.append("README.md Next Chunk section does not name manifest.next_recommended_chunk.id")
    if any(phrase in readme_next for phrase in stale_readme_scope_phrases):
        errors.append("README.md Next Chunk section still describes stale Chunk 24 multi-AI/model-bias scope")
    required_readme_next_terms = [
        "bounded parallel cloud/automation shortcut-card risks",
        "unattended cloud delegation",
        "automation overreach",
        "background-agent handoff risk",
        "cloud summary overtrust",
        "browser/GUI automation risk",
        "approved parallel/cloud/automation slice",
    ]
    for term in required_readme_next_terms:
        if term not in readme_next:
            errors.append(f"README.md Next Chunk section lacks Chunk 25 parallel/cloud/automation scope term: {term}")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    if "Chunk 24" not in current_checks or "multi-AI" not in current_checks:
        errors.append("manifest.validation_expectations.current_chunk_checks must name Chunk 24 multi-AI/model-bias shortcut checks")
    if manifest.get("multi_ai_model_bias_shortcut_cards") != required:
        errors.append("manifest.multi_ai_model_bias_shortcut_cards does not match Chunk 24 required card map")
    if manifest.get("chunk_24_required_topic_ids") != list(required):
        errors.append("manifest.chunk_24_required_topic_ids does not match required Chunk 24 IDs")

    active_ids = authored_active_ids()
    for policy_name in ["topic_namespace_policy", "namespace_policy"]:
        redirects = manifest.get(policy_name, {}).get("topic_id_redirects", {})
        if not isinstance(redirects, dict):
            continue
        for key, value in redirects.items():
            if key in active_ids and key != value:
                errors.append(f"manifest.{policy_name}.topic_id_redirects uses active canonical ID as redirect key: {key} -> {value}")
            if key in required and key != value:
                errors.append(f"manifest.{policy_name}.topic_id_redirects must not shadow authored Chunk 24 ID: {key} -> {value}")

    topic_cards = manifest.get("topic_cards", {})
    for ident, rel in required.items():
        path = ROOT / rel
        if topic_cards.get(ident) != rel:
            errors.append(f"manifest.topic_cards missing Chunk 24 route: {ident} -> {rel}")
        if not path.exists():
            errors.append(f"missing Chunk 24 shortcut file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != ident or fm.get("type") != "shortcut" or fm.get("status") != "active":
            errors.append(f"frontmatter for {rel} does not declare active shortcut ID {ident}")
        body = read(path)
        if f"<!-- VCB:BEGIN_TOPIC id={ident}" not in body:
            errors.append(f"{rel} missing matching Chunk 24 begin topic marker")
        if f"<!-- VCB:END_TOPIC id={ident} -->" not in body:
            errors.append(f"{rel} missing matching end topic marker")
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in body:
                errors.append(f"{rel} missing required topic heading {heading}")
        if "## Quick Navigation" not in body:
            errors.append(f"{rel} missing shortcut-card Quick Navigation section")

    allowed_shortcut_files = (
        {Path(v).name for v in CHUNK_20_SHORTCUT_IDS.values()}
        | {Path(v).name for v in CHUNK_21_SHORTCUT_IDS.values()}
        | {Path(v).name for v in CHUNK_22_SHORTCUT_IDS.values()}
        | {Path(v).name for v in CHUNK_23_SHORTCUT_IDS.values()}
        | {Path(v).name for v in required.values()}
        | {".gitkeep"}
    )
    observed_shortcut_files = {p.name for p in (ROOT / "topics" / "shortcuts").glob("*")}
    if observed_shortcut_files != allowed_shortcut_files:
        errors.append(f"Chunk 24 shortcut-card scope drift: expected={sorted(allowed_shortcut_files)} observed={sorted(observed_shortcut_files)}")
    for disallowed in ["topics/tool-catalog", "topics/field-practices"]:
        files = [p.name for p in (ROOT / disallowed).glob("*.md")]
        if files:
            errors.append(f"Chunk 24 must not add {disallowed} topic cards: {files}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md")]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 24 must not expand pricing snapshots: {pricing_files}")

    statuses = shortcut_register_statuses()
    register_text = read(ROOT / "SHORTCUT_REGISTER.md")
    for ident in required:
        if statuses.get(ident) != "active":
            errors.append(f"SHORTCUT_REGISTER row for {ident} must be active; observed={statuses.get(ident)!r}")
        if re.search(rf"`{re.escape(ident)}`[^\n]*\|\s*planned\s*\|", register_text):
            errors.append(f"SHORTCUT_REGISTER still lists authored Chunk 24 shortcut as planned: {ident}")

    for rel in CHUNK_24_REQUIRED_INDEXES:
        body = read(ROOT / rel)
        full_list_sections = []
        for heading, section_body in markdown_h2_sections(body):
            section_ids = set(re.findall(r"`(vcb\.shortcut\.[A-Za-z0-9_.-]+)`", section_body))
            if set(required).issubset(section_ids):
                full_list_sections.append(heading)
            for ident in required:
                if section_body.count(f"`{ident}`") > 1 and "intentional duplicate" not in section_body.lower():
                    errors.append(f"{rel} section {heading!r} contains duplicate active Chunk 24 shortcut route: {ident}")
        if len(full_list_sections) > 1:
            errors.append(f"{rel} contains duplicate full-list Chunk 24 shortcut sections: {full_list_sections}")
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing route for Chunk 24 shortcut card: {ident}")
            if re.search(rf"`{re.escape(ident)}`\s*→\s*planned", body):
                errors.append(f"{rel} has stale planned route for authored Chunk 24 shortcut: {ident}")

    for rel in ["README.md", "llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        for ident in required:
            if f"`{ident}`" not in body:
                errors.append(f"{rel} missing Chunk 24 source-map/root route: {ident}")

    required_terms = ["active shortcut-card slices", "Chunk 20 harm-reduction cards", "Chunk 21 security/permission cards", "Chunk 22 setup/process cards", "Chunk 23 tool-sprawl/skill/reusable-workflow cards", "Chunk 24 multi-AI/model-bias cards"]
    semantic_terms = ["many ais", "model routing", "ai consensus", "cherry-picking", "trusting estimates", "model biases", "subagent swarms"]
    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        if "User asks to make a shortcut safer" in body and not all(term in body for term in required_terms):
            errors.append(f"{rel} generic shortcut safety route does not cover active Chunk 20, Chunk 21, Chunk 22, Chunk 23, and Chunk 24 shortcut-card slices")
        status_phrase = "Multi-AI/model-bias shortcut cards from Chunk 24 are active."
        total = body.count(status_phrase)
        if rel == "llms.txt" and total != 1:
            errors.append(f"llms.txt must contain exactly one active Chunk 24 status phrase; observed={total}")
        if rel == "llms-full.txt" and total != 1:
            errors.append(f"llms-full.txt must contain exactly one active Chunk 24 status phrase; observed={total}")
        full_list_sections = [heading for heading, section_body in markdown_h2_sections(body) if set(required).issubset(set(re.findall(r"`(vcb\.shortcut\.[A-Za-z0-9_.-]+)`", section_body)))]
        if len(full_list_sections) != 1:
            errors.append(f"{rel} must contain exactly one consolidated full-list section for Chunk 24 shortcut cards; observed={full_list_sections}")
        fast_sections = [section_body for heading, section_body in markdown_h2_sections(body) if heading == "Fast Routing"]
        fast_body = "\n".join(fast_sections)
        fast_lower = fast_body.lower()
        if not fast_body:
            errors.append(f"{rel} missing general Fast Routing section")
        elif not all(term in fast_lower for term in semantic_terms) or "chunk 24" not in fast_lower or "vcb.shortcut" not in fast_lower:
            errors.append(f"{rel} general Fast Routing lacks direct semantic Chunk 24 shortcut-intent route")
        semantic_pos = min([p for p in (fast_lower.find("many ais"), fast_lower.find("model routing"), fast_lower.find("ai consensus")) if p >= 0] or [-1])
        fallback_positions = [p for p in (fast_lower.find("user asks to make a shortcut safer"), fast_lower.find("beyond authored shortcut cards")) if p >= 0]
        if semantic_pos < 0:
            errors.append(f"{rel} general Fast Routing lacks Chunk 24 semantic route anchor terms")
        elif fallback_positions and semantic_pos > min(fallback_positions):
            errors.append(f"{rel} Chunk 24 semantic Fast Routing appears after shortcut fallback")

    for rel, heading, ids in CHUNK_24_SECTION_REQUIREMENTS:
        sections = {h: b for h, b in markdown_h2_sections(read(ROOT / rel))}
        if heading not in sections:
            errors.append(f"{rel} missing Chunk 24 semantic section: {heading}")
            continue
        for ident in ids:
            if f"`{ident}`" not in sections[heading]:
                errors.append(f"{rel} section {heading!r} missing active Chunk 24 route: {ident}")

    for rel, heading, ids in CHUNK_24_SEMANTIC_SECTION_REQUIREMENTS:
        sections = {h: b for h, b in markdown_h2_sections(read(ROOT / rel))}
        section_body = sections.get(heading)
        if section_body is None:
            errors.append(f"{rel} missing existing semantic section for Chunk 24 routing: {heading}")
            continue
        if not section_body.strip():
            errors.append(f"{rel} semantic section {heading!r} is empty while active Chunk 24 cards exist")
            continue
        if not any(f"`{ident}`" in section_body for ident in ids):
            errors.append(f"{rel} semantic section {heading!r} routes only to older/planned material while active Chunk 24 cards exist")
        for ident in ids:
            if f"`{ident}`" not in section_body:
                errors.append(f"{rel} semantic section {heading!r} missing active Chunk 24 route: {ident}")

    for rel in CHUNK_24_REQUIRED_INDEXES:
        for heading, section_body in markdown_h2_sections(read(ROOT / rel)):
            heading_lower = heading.lower()
            if ("multi-ai" in heading_lower or "model-bias" in heading_lower or "model biases" in heading_lower) and not section_body.strip():
                errors.append(f"{rel} semantic section {heading!r} is empty while active Chunk 24 cards exist")


    failure_sections = {h: b for h, b in markdown_h2_sections(read(ROOT / "indexes" / "INDEX_BY_FAILURE_MODE.md"))}
    bad_estimate_body = failure_sections.get("Bad estimates and confident wrong summaries", "")
    ordered_bad_estimate_routes = [
        "`vcb.shortcut.trusting_estimates_before_inspection`",
        "`vcb.shortcut.ignoring_model_biases`",
        "`vcb.shortcut.consensus_as_correctness`",
        "`vcb.shortcut.best_of_n_without_review`",
    ]
    for route in ordered_bad_estimate_routes:
        if route not in bad_estimate_body:
            errors.append("indexes/INDEX_BY_FAILURE_MODE.md Bad estimates and confident wrong summaries lacks active Chunk 24 route: " + route.strip("`"))
    first_fallbacks = [pos for token in ["`vcb.failure.done_claim_without_evidence`", "`vcb.chapter.what_codex_is_bad_at`", "`vcb.chapter.model_biases_failure_biases_bad_estimates`"] if (pos := bad_estimate_body.find(token)) >= 0]
    first_fallback = min(first_fallbacks) if first_fallbacks else -1
    if first_fallback >= 0:
        for route in ordered_bad_estimate_routes:
            route_pos = bad_estimate_body.find(route)
            if route_pos < 0 or route_pos > first_fallback:
                errors.append("indexes/INDEX_BY_FAILURE_MODE.md must show active Chunk 24 bad-estimate routes before chapter/failure fallbacks")

    advanced_shortcut_sections = {h: b for h, b in markdown_h2_sections(read(ROOT / "indexes" / "INDEX_BY_SHORTCUT.md"))}
    advanced_body = advanced_shortcut_sections.get("Advanced agentic workflow shortcuts", "")
    planned_same_file = "`vcb.shortcut.parallel_tasks_same_files`"
    active_replacements = ["`vcb.shortcut.parallel_agents_edit_same_files`", "`vcb.shortcut.many_ais_same_files`"]
    if planned_same_file in advanced_body:
        planned_pos = advanced_body.find(planned_same_file)
        for replacement in active_replacements:
            replacement_pos = advanced_body.find(replacement)
            if replacement_pos < 0 or replacement_pos > planned_pos:
                errors.append(
                    "indexes/INDEX_BY_SHORTCUT.md planned near-duplicate route "
                    "vcb.shortcut.parallel_tasks_same_files must show active same-file replacement routes first"
                )

    active_vcb_ids = authored_active_ids()
    for ident, rel in required.items():
        path = ROOT / rel
        fm = parse_frontmatter(path) or {}
        body = read(path)
        fm_related = set(str(value) for value in (fm.get("related_topics") or []) if str(value).startswith("vcb."))
        body_related = set()
        related_match = re.search(r"(?ms)^## Related Topics\n(.*?)(?=^## |^<!-- VCB:STOP_RETRIEVAL|\Z)", body)
        if related_match:
            body_related.update(re.findall(r"`?(vcb\.[A-Za-z0-9_.-]+)`?", related_match.group(1)))
        unresolved = sorted((fm_related | body_related) - active_vcb_ids)
        if unresolved:
            errors.append(f"{rel} has unresolved related_topics IDs: {unresolved}")

    changelog_text = read(ROOT / "CHANGELOG.md")
    chunk24_headings = re.findall(r"^## .*Chunk 24.*$", changelog_text, flags=re.M)
    if len(chunk24_headings) != 1:
        errors.append(f"CHANGELOG.md must contain exactly one Chunk 24 heading; observed={chunk24_headings}")
    combined_claims = (read(ROOT / "CHUNK_24_REPORT.md") if (ROOT / "CHUNK_24_REPORT.md").exists() else "") + "\n" + read(ROOT / "CHANGELOG.md")
    for label, rel in {
        "PROMPT_LIBRARY.md": "indexes/PROMPT_LIBRARY.md", "INDEX_FOR_AI_COACHES.md": "indexes/INDEX_FOR_AI_COACHES.md", "INDEX_BY_SHORTCUT.md": "indexes/INDEX_BY_SHORTCUT.md", "INDEX_BY_TASK.md": "indexes/INDEX_BY_TASK.md", "INDEX_BY_FAILURE_MODE.md": "indexes/INDEX_BY_FAILURE_MODE.md", "INDEX_BY_BUDGET_PROFILE.md": "indexes/INDEX_BY_BUDGET_PROFILE.md", "INDEX_BY_RISK_LEVEL.md": "indexes/INDEX_BY_RISK_LEVEL.md", "INDEX_BY_RECOVERABILITY.md": "indexes/INDEX_BY_RECOVERABILITY.md", "INDEX_BY_CONCEPT.md": "indexes/INDEX_BY_CONCEPT.md", "INDEX_BY_STABILITY.md": "indexes/INDEX_BY_STABILITY.md", "INDEX_BY_PROJECT_TYPE.md": "indexes/INDEX_BY_PROJECT_TYPE.md", "INDEX_BY_CODEX_SURFACE.md": "indexes/INDEX_BY_CODEX_SURFACE.md", "INDEX_BY_TOOL_CATEGORY.md": "indexes/INDEX_BY_TOOL_CATEGORY.md", "GLOSSARY.md": "indexes/GLOSSARY.md"
    }.items():
        if label in combined_claims and not any(f"`{ident}`" in read(ROOT / rel) for ident in required):
            errors.append(f"Chunk 24 report/changelog claims {label} routing, but the file has no Chunk 24 shortcut routes")


def validate_chunk_24_report_inventory(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_24":
        return
    path = ROOT / "CHUNK_24_REPORT.md"
    if not path.exists():
        errors.append("CHUNK_24_REPORT.md missing for active Chunk 24")
        return
    text = read(path)
    required_created = set(CHUNK_24_SHORTCUT_IDS.values()) | {"CHUNK_24_REPORT.md"}
    required_updated = {"README.md", "manifest.json", "llms.txt", "llms-full.txt", "SHORTCUT_REGISTER.md", "SOURCE_REGISTER.md", "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", *CHUNK_24_REQUIRED_INDEXES}
    for rel in sorted(required_created | required_updated):
        if f"`{rel}`" not in text:
            errors.append(f"CHUNK_24_REPORT.md file inventory omits required Chunk 24 path: {rel}")
    if "## Recommended Next Chunk" not in text:
        errors.append("CHUNK_24_REPORT.md missing recommended next chunk section")
    if "## Unresolved questions" not in text or "None." not in text:
        errors.append("CHUNK_24_REPORT.md must explicitly state unresolved questions")
    claims = extract_machine_report_claims(text)
    if not claims:
        errors.append("CHUNK_24_REPORT.md missing validation claims block")
    missing = sorted(CHUNK_24_REPORT_REQUIRED_CLAIMS - claims)
    if missing:
        errors.append(f"CHUNK_24_REPORT.md missing implemented validation claims: {missing}")
    unsupported = sorted(claims - CHUNK_24_REPORT_REQUIRED_CLAIMS)
    if unsupported:
        errors.append(f"CHUNK_24_REPORT.md has unsupported validation claims: {unsupported}")




CHUNK_27_TOOL_CARDS = {
    "tool.codex": "topics/tool-catalog/codex.md",
    "tool.codex_app": "topics/tool-catalog/codex-app.md",
    "tool.codex_cli": "topics/tool-catalog/codex-cli.md",
    "tool.codex_ide_extension": "topics/tool-catalog/codex-ide-extension.md",
    "tool.codex_cloud": "topics/tool-catalog/codex-cloud.md",
    "tool.codex_github_review": "topics/tool-catalog/codex-github-review.md",
    "tool.codex_exec": "topics/tool-catalog/codex-exec.md",
}

CHUNK_27_REQUIRED_SOURCE_IDS = {
    "vcb.register.editor_feedback_chunk_26",
    "openai.codex.overview",
    "openai.codex.app",
    "openai.codex.cli",
    "openai.codex.ide",
    "openai.codex.cloud",
    "openai.codex.github_review",
    "openai.codex.noninteractive",
    "openai.codex.cli_reference",
    "openai.codex.agent_approvals_security",
    "vcb.pricing_snapshot.openai_codex",
}


def extract_markdown_section(text: str, heading: str) -> str:
    pattern = re.compile(rf"^## {re.escape(heading)}\s*$", re.M)
    match = pattern.search(text)
    if not match:
        return ""
    start = match.end()
    next_match = re.search(r"^## ", text[start:], flags=re.M)
    end = start + next_match.start() if next_match else len(text)
    return text[start:end]


def validate_chunk_27_codex_primary_tool_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_27":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_27_codex_primary_tool_cards":
        errors.append("manifest.active_chunk.id must be chunk_27_codex_primary_tool_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_28_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_28_editor_scoped_next_slice for Chunk 27")

    readme = read(ROOT / "README.md")
    readme_next = extract_markdown_section(readme, "Next Chunk")
    required_readme_terms = [
        "chunk_27_codex_primary_tool_cards",
        "bounded first-party OpenAI/Codex tool-card expansion",
        "primary execution surfaces only",
        "no third-party tool cards",
        "no full tool-card expansion",
        "no new shortcut-card expansion",
        "chunk_28_editor_scoped_next_slice",
    ]
    for term in required_readme_terms:
        if term not in readme:
            errors.append(f"README.md missing Chunk 27 governance term: {term}")
    if "Blocked until" not in readme_next and "blocked until" not in readme_next:
        errors.append("README.md Next Chunk section must block Chunk 28 until editor approval")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    tool_rows = {tid: None for tid in CHUNK_27_TOOL_CARDS}
    for line in tool_register.splitlines():
        for tid in CHUNK_27_TOOL_CARDS:
            if f"`{tid}`" in line:
                tool_rows[tid] = line
    for tid, line in tool_rows.items():
        if line is None:
            errors.append(f"TOOL_REGISTER.md missing Chunk 27 tool ID: {tid}")
        elif "| active |" not in line:
            errors.append(f"TOOL_REGISTER.md Chunk 27 tool ID is not active: {tid}")
    if "## Chunk 27 Active Primary OpenAI/Codex Tool Cards" in tool_register:
        errors.append("TOOL_REGISTER.md must not duplicate Chunk 27 tool IDs in a second active table; keep one register declaration per tool ID")

    source_register = read(ROOT / "SOURCE_REGISTER.md")
    for source_id in CHUNK_27_REQUIRED_SOURCE_IDS:
        if f"`{source_id}`" not in source_register:
            errors.append(f"SOURCE_REGISTER.md missing source anchor required by Chunk 27: {source_id}")

    for tid, rel in CHUNK_27_TOOL_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 27 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid:
            errors.append(f"{rel} frontmatter id mismatch: {fm.get('id')} != {tid}")
        if fm.get("type") != "tool_card":
            errors.append(f"{rel} must have type: tool_card")
        if fm.get("status") != "active":
            errors.append(f"{rel} must be active")
        if fm.get("source_status", {}).get("official_openai") is not True:
            errors.append(f"{rel} cites OpenAI sources and must set source_status.official_openai: true")
        if fm.get("source_status", {}).get("official_vendor") is not False:
            errors.append(f"{rel} first-party OpenAI tool cards should not mark official_vendor true separately from official_openai")
        if fm.get("pricing_snapshot_required") is not True or "vcb.pricing_snapshot.openai_codex" not in (fm.get("pricing_snapshot_ids") or []):
            errors.append(f"{rel} must route pricing/limits to vcb.pricing_snapshot.openai_codex")
        for volatile_forbidden in ["$", "credit value", "context window", "token limit"]:
            if volatile_forbidden in read(path):
                errors.append(f"{rel} may contain brittle pricing/limit prose: {volatile_forbidden}")

    topic_catalog_files = sorted(
        p.name for p in (ROOT / "topics" / "tool-catalog").glob("*.md")
        if p.name != ".gitkeep"
    )
    expected_names = sorted(Path(rel).name for rel in CHUNK_27_TOOL_CARDS.values())
    if topic_catalog_files != expected_names:
        errors.append(
            "Chunk 27 tool-catalog scope drift: "
            f"observed={topic_catalog_files} expected={expected_names}"
        )

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        phrase = "First-party OpenAI/Codex primary tool cards from Chunk 27 are active."
        if body.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 27 tool-card phrase; observed={body.count(phrase)}")
        for heading in ["Primary Codex Tool Card Fast Routing", "Active Chunk 27 Primary Codex Tool Cards"]:
            section = extract_markdown_section(body, heading)
            if not section.strip():
                errors.append(f"{rel} missing ## {heading} section")
                continue
            for tid in CHUNK_27_TOOL_CARDS:
                if f"`{tid}`" not in section:
                    errors.append(f"{rel} ## {heading} missing {tid}")

    required_index_surfaces = {
        "indexes/INDEX_BY_TOOL_CATEGORY.md": "Active First-Party OpenAI/Codex Tool Cards",
        "indexes/INDEX_BY_CODEX_SURFACE.md": "Active First-Party OpenAI/Codex Tool Cards",
        "indexes/INDEX_BY_TASK.md": "Active First-Party OpenAI/Codex Tool Cards",
        "indexes/INDEX_FOR_AI_COACHES.md": "Active First-Party OpenAI/Codex Tool Cards",
        "indexes/GLOSSARY.md": "Active First-Party OpenAI/Codex Tool Cards",
    }
    for rel, heading in required_index_surfaces.items():
        body = read(ROOT / rel)
        section = extract_markdown_section(body, heading)
        if not section.strip():
            errors.append(f"{rel} missing ## {heading} section for Chunk 27")
            continue
        for tid in CHUNK_27_TOOL_CARDS:
            if f"`{tid}`" not in section:
                errors.append(f"{rel} ## {heading} missing active Chunk 27 tool route {tid}")
        planned_pos = section.find("→ planned")
        if planned_pos >= 0:
            first_active_missing = [tid for tid in CHUNK_27_TOOL_CARDS if section.find(f"`{tid}`") < 0 or section.find(f"`{tid}`") > planned_pos]
            if first_active_missing:
                errors.append(f"{rel} ## {heading} shows planned routes before active Chunk 27 tool routes: {first_active_missing}")


    # Chunk 27 semantic-route hardening: aggregate tool-card lists are not enough.
    # The common user-intent lookup sections must route to the smallest active tool card
    # before falling back to older chapter or feature-topic material.
    task_index = read(ROOT / "indexes/INDEX_BY_TASK.md")
    orient_section = extract_markdown_section(task_index, "Orient yourself and choose a Codex surface")
    if not orient_section.strip():
        errors.append("INDEX_BY_TASK.md missing ## Orient yourself and choose a Codex surface")
    else:
        first_chapter = orient_section.find("`vcb.chapter.")
        for tid in CHUNK_27_TOOL_CARDS:
            pos = orient_section.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"INDEX_BY_TASK.md ## Orient yourself and choose a Codex surface missing active tool route {tid}")
            elif first_chapter >= 0 and pos > first_chapter:
                errors.append(f"INDEX_BY_TASK.md ## Orient yourself and choose a Codex surface lists {tid} after chapter fallbacks")

    targeted_task_routes = {
        "Run CI or non-interactive Codex": ["tool.codex_exec"],
        "Review Codex output or a PR": ["tool.codex_github_review"],
        "Use cloud, subagents, browser, or GUI surfaces": ["tool.codex_cloud", "tool.codex_app"],
    }
    for heading, required_ids in targeted_task_routes.items():
        section = extract_markdown_section(task_index, heading)
        if not section.strip():
            errors.append(f"INDEX_BY_TASK.md missing ## {heading}")
            continue
        fallback_positions = [
            section.find("`vcb.shortcut."),
            section.find("`vcb.workflow."),
            section.find("`vcb.chapter."),
            section.find("`vcb.codex."),
        ]
        first_fallback = min([pos for pos in fallback_positions if pos >= 0], default=-1)
        for tid in required_ids:
            pos = section.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"INDEX_BY_TASK.md ## {heading} missing active tool route {tid}")
            elif first_fallback >= 0 and pos > first_fallback:
                errors.append(f"INDEX_BY_TASK.md ## {heading} lists {tid} after older fallback routes")

    prompt_library = read(ROOT / "indexes/PROMPT_LIBRARY.md")
    feature_prompt_section = extract_markdown_section(prompt_library, "Codex feature selection prompt")
    if not feature_prompt_section.strip():
        errors.append("PROMPT_LIBRARY.md missing ## Codex feature selection prompt")
    else:
        first_feature_topic = feature_prompt_section.find("`vcb.codex.")
        for tid in CHUNK_27_TOOL_CARDS:
            pos = feature_prompt_section.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"PROMPT_LIBRARY.md ## Codex feature selection prompt missing active tool route {tid}")
            elif first_feature_topic >= 0 and pos > first_feature_topic:
                errors.append(f"PROMPT_LIBRARY.md ## Codex feature selection prompt lists {tid} after vcb.codex.* feature-topic routes")

    llms_short = read(ROOT / "llms.txt")
    for line in llms_short.splitlines():
        if "which Codex surface" in line or "which Codex tool/surface" in line:
            if "tool.codex" not in line:
                errors.append("llms.txt has stale Codex surface routing without tool.codex")
    stale_surface_route = "retrieve `vcb.codex.app`, `vcb.codex.cli`, `vcb.codex.ide_extension`, or `vcb.codex.cloud` by task shape"
    if stale_surface_route in llms_short:
        errors.append("llms.txt still contains stale vcb.codex-only surface-selection route")

    changelog = read(ROOT / "CHANGELOG.md")
    if len(re.findall(r"^## .*Chunk 27", changelog, flags=re.M)) != 1:
        errors.append("CHANGELOG.md must contain exactly one Chunk 27 heading")

    report = ROOT / "CHUNK_27_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_27_REPORT.md missing")
    else:
        report_text = read(report)
        if not report_text.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
            errors.append("CHUNK_27_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")
        for tid, rel in CHUNK_27_TOOL_CARDS.items():
            if f"`{tid}`" not in report_text or f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_27_REPORT.md missing created tool inventory for {tid} / {rel}")
        required_claims = [
            "tool-card schema validation",
            "TOOL_REGISTER active status",
            "LLM source-map routing",
            "semantic index routing",
            "first-party official OpenAI source posture",
            "scope guardrails",
        ]
        for claim in required_claims:
            if claim not in report_text:
                errors.append(f"CHUNK_27_REPORT.md missing validator-backed claim: {claim}")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 27", "first-party", "OpenAI/Codex", "tool-card", "official OpenAI", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 27 term: {term}")


CHUNK_28_TOOL_CARDS = {
    "tool.codex_worktrees": "topics/tool-catalog/codex-worktrees.md",
    "tool.codex_subagents": "topics/tool-catalog/codex-subagents.md",
    "tool.codex_automations": "topics/tool-catalog/codex-automations.md",
    "tool.codex_computer_use": "topics/tool-catalog/codex-computer-use.md",
    "tool.codex_browser": "topics/tool-catalog/codex-browser.md",
    "tool.codex_chrome_extension": "topics/tool-catalog/codex-chrome-extension.md",
}

CHUNK_28_ALLOWED_TOOL_CATALOG_FILES = set(CHUNK_27_TOOL_CARDS.values()) | set(CHUNK_28_TOOL_CARDS.values())

CHUNK_28_REQUIRED_SOURCE_IDS = {
    "vcb.register.editor_feedback_chunk_27",
    "openai.codex.app_worktrees",
    "openai.codex.subagents",
    "openai.codex.subagent_concepts",
    "openai.codex.app_automations",
    "openai.codex.app_computer_use",
    "openai.codex.app_browser",
    "openai.codex.chrome_extension",
    "openai.codex.app_settings",
    "openai.codex.app_features",
    "openai.codex.best_practices",
    "vcb.pricing_snapshot.openai_codex",
}


def first_any_position(section: str, needles: list[str]) -> int:
    positions = [section.find(needle) for needle in needles if section.find(needle) >= 0]
    return min(positions) if positions else -1


def require_ids_before_fallback(
    section: str,
    heading_label: str,
    required_ids: list[str],
    fallback_needles: list[str],
    errors: list[str],
) -> None:
    first_fallback = first_any_position(section, fallback_needles)
    for ident in required_ids:
        pos = section.find(f"`{ident}`")
        if pos < 0:
            errors.append(f"{heading_label} missing active route {ident}")
        elif first_fallback >= 0 and pos > first_fallback:
            errors.append(f"{heading_label} lists {ident} after older fallback routes")


def validate_chunk_28_codex_adjunct_tool_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_28":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_28_codex_adjunct_surface_tool_cards":
        errors.append("manifest.active_chunk.id must be chunk_28_codex_adjunct_surface_tool_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_29_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_29_editor_scoped_next_slice for Chunk 28")

    readme = read(ROOT / "README.md")
    readme_next = extract_markdown_section(readme, "Next Chunk")
    required_readme_terms = [
        "chunk_28_codex_adjunct_surface_tool_cards",
        "bounded first-party OpenAI/Codex adjunct surface/tool-card expansion only",
        "tool.codex_worktrees",
        "tool.codex_subagents",
        "tool.codex_automations",
        "tool.codex_computer_use",
        "tool.codex_browser",
        "tool.codex_chrome_extension",
        "no third-party tool cards",
        "no AGENTS/config/skills/MCP/hooks tool-card expansion",
        "no Codex Security tool-card expansion",
        "no new shortcut-card expansion",
        "chunk_29_editor_scoped_next_slice",
    ]
    for term in required_readme_terms:
        if term not in readme:
            errors.append(f"README.md missing Chunk 28 governance term: {term}")
    if "Blocked until" not in readme_next and "blocked until" not in readme_next:
        errors.append("README.md Next Chunk section must block Chunk 29 until editor approval")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    for tid in CHUNK_28_TOOL_CARDS:
        matching_lines = [line for line in tool_register.splitlines() if f"`{tid}`" in line]
        if len(matching_lines) != 1:
            errors.append(f"TOOL_REGISTER.md must contain exactly one row for Chunk 28 tool ID {tid}; observed={matching_lines}")
        elif "| active |" not in matching_lines[0]:
            errors.append(f"TOOL_REGISTER.md Chunk 28 tool ID is not active: {tid}")

    source_register = read(ROOT / "SOURCE_REGISTER.md")
    for source_id in CHUNK_28_REQUIRED_SOURCE_IDS:
        if f"`{source_id}`" not in source_register:
            errors.append(f"SOURCE_REGISTER.md missing source anchor required by Chunk 28: {source_id}")

    for tid, rel in CHUNK_28_TOOL_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 28 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid:
            errors.append(f"{rel} frontmatter id mismatch: {fm.get('id')} != {tid}")
        if fm.get("type") != "tool_card":
            errors.append(f"{rel} must have type: tool_card")
        if fm.get("status") != "active":
            errors.append(f"{rel} must be active")
        if fm.get("source_status", {}).get("official_openai") is not True:
            errors.append(f"{rel} cites OpenAI sources and must set source_status.official_openai: true")
        if fm.get("source_status", {}).get("official_vendor") is not False:
            errors.append(f"{rel} first-party OpenAI tool cards should not mark official_vendor true separately from official_openai")
        if fm.get("pricing_snapshot_required") is not True or "vcb.pricing_snapshot.openai_codex" not in (fm.get("pricing_snapshot_ids") or []):
            errors.append(f"{rel} must route pricing/limits to vcb.pricing_snapshot.openai_codex")
        body = read(path)
        for volatile_forbidden in ["$", "credit value", "context window", "token limit"]:
            if volatile_forbidden in body:
                errors.append(f"{rel} may contain brittle pricing/limit prose: {volatile_forbidden}")
        source_ids_in_card = evidence_ids(path)
        if not any(sid in source_ids_in_card for sid in CHUNK_28_REQUIRED_SOURCE_IDS if sid.startswith("openai.")):
            errors.append(f"{rel} must cite at least one official OpenAI Chunk 28 source anchor")

    topic_catalog_files = {
        str(p.relative_to(ROOT))
        for p in (ROOT / "topics" / "tool-catalog").glob("*.md")
        if p.name != ".gitkeep"
    }
    if topic_catalog_files != CHUNK_28_ALLOWED_TOOL_CATALOG_FILES:
        errors.append(
            "Chunk 28 tool-catalog scope drift: "
            f"observed={sorted(topic_catalog_files)} expected={sorted(CHUNK_28_ALLOWED_TOOL_CATALOG_FILES)}"
        )

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        phrase = "First-party OpenAI/Codex adjunct surface tool cards from Chunk 28 are active."
        if body.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 28 adjunct tool-card phrase; observed={body.count(phrase)}")
        for heading in ["Adjunct Codex Tool Card Fast Routing", "Active Chunk 28 Adjunct Codex Tool Cards"]:
            section = extract_markdown_section(body, heading)
            if not section.strip():
                errors.append(f"{rel} missing ## {heading} section")
                continue
            for tid in CHUNK_28_TOOL_CARDS:
                if f"`{tid}`" not in section:
                    errors.append(f"{rel} ## {heading} missing {tid}")
        stale_constraint = "Need to choose a Codex surface, autonomy level, or delegation mode → retrieve `vcb.constraints.operating_mode`."
        if stale_constraint in body:
            errors.append(f"{rel} still routes Codex surface choice only to constraints instead of tool.codex first")

    llms_short = read(ROOT / "llms.txt")
    stale_advanced = "User asks about advanced agentic work → retrieve `vcb.codex.automations`, `vcb.codex.subagents`, or `vcb.codex.computer_use`."
    if stale_advanced in llms_short:
        errors.append("llms.txt still contains stale vcb.codex-only advanced agentic work route")
    for line in llms_short.splitlines():
        if "advanced agentic work" in line:
            for tid in ["tool.codex_subagents", "tool.codex_automations", "tool.codex_computer_use"]:
                if f"`{tid}`" not in line:
                    errors.append(f"llms.txt advanced agentic work route missing active adjunct tool card {tid}")

    llms_full = read(ROOT / "llms-full.txt")
    for line in llms_full.splitlines():
        if "Need first-party Codex tool-card guidance" in line:
            for tid in ["tool.codex", *CHUNK_27_TOOL_CARDS.keys(), *CHUNK_28_TOOL_CARDS.keys()]:
                if f"`{tid}`" not in line:
                    errors.append(f"llms-full.txt first-party Codex tool-card guidance route missing {tid}")
            break
    else:
        errors.append("llms-full.txt missing Need first-party Codex tool-card guidance route")

    required_index_surfaces = {
        "indexes/INDEX_BY_TOOL_CATEGORY.md": "Active Adjunct OpenAI/Codex Tool Cards",
        "indexes/INDEX_BY_CODEX_SURFACE.md": "Active Adjunct OpenAI/Codex Tool Cards",
        "indexes/INDEX_BY_TASK.md": "Active Adjunct OpenAI/Codex Tool Cards",
        "indexes/INDEX_FOR_AI_COACHES.md": "Active Adjunct OpenAI/Codex Tool Cards",
        "indexes/PROMPT_LIBRARY.md": "Active Adjunct OpenAI/Codex Tool Cards",
        "indexes/GLOSSARY.md": "Active Adjunct OpenAI/Codex Tool Cards",
    }
    for rel, heading in required_index_surfaces.items():
        section = extract_markdown_section(read(ROOT / rel), heading)
        if not section.strip():
            errors.append(f"{rel} missing ## {heading} section for Chunk 28")
            continue
        for tid in CHUNK_28_TOOL_CARDS:
            if f"`{tid}`" not in section:
                errors.append(f"{rel} ## {heading} missing active Chunk 28 tool route {tid}")

    feature_semantic_sections = {
        "indexes/INDEX_BY_BUDGET_PROFILE.md": "Budget-aware Codex feature selection",
        "indexes/INDEX_BY_RECOVERABILITY.md": "Recoverability by Codex feature",
        "indexes/INDEX_BY_RISK_LEVEL.md": "Codex feature risk routing",
        "indexes/INDEX_BY_FAILURE_MODE.md": "Codex feature misuse",
        "indexes/INDEX_BY_SHORTCUT.md": "Shortcuts around Codex features",
        "indexes/INDEX_BY_CONCEPT.md": "Codex product features and surfaces",
        "indexes/INDEX_BY_PROJECT_TYPE.md": "Codex feature selection by project type",
        "indexes/INDEX_BY_STABILITY.md": "Codex feature cards requiring quarterly/monthly review",
    }
    for rel, heading in feature_semantic_sections.items():
        section = extract_markdown_section(read(ROOT / rel), heading)
        if not section.strip():
            errors.append(f"{rel} missing ## {heading}")
            continue
        require_ids_before_fallback(
            section,
            f"{rel} ## {heading}",
            list(CHUNK_28_TOOL_CARDS),
            ["`vcb.codex.automations`", "`vcb.codex.subagents`", "`vcb.codex.computer_use`", "`vcb.codex."],
            errors,
        )

    glossary_features = extract_markdown_section(read(ROOT / "indexes" / "GLOSSARY.md"), "Codex feature-card terms")
    glossary_pairs = {
        "Codex automation": ("tool.codex_automations", "vcb.codex.automations"),
        "Codex subagent": ("tool.codex_subagents", "vcb.codex.subagents"),
        "Computer Use": ("tool.codex_computer_use", "vcb.codex.computer_use"),
        "Codex worktree": ("tool.codex_worktrees", None),
        "in-app browser": ("tool.codex_browser", None),
        "Codex Chrome extension": ("tool.codex_chrome_extension", None),
    }
    for term, (tool_id, companion_id) in glossary_pairs.items():
        lines = [line for line in glossary_features.splitlines() if line.startswith(f"- `{term}`")]
        if len(lines) != 1:
            errors.append(f"GLOSSARY.md ## Codex feature-card terms must have exactly one term row for {term}")
            continue
        line = lines[0]
        tool_pos = line.find(f"`{tool_id}`")
        if tool_pos < 0:
            errors.append(f"GLOSSARY.md {term} row missing active tool route {tool_id}")
        if companion_id is not None:
            companion_pos = line.find(f"`{companion_id}`")
            if companion_pos < 0:
                errors.append(f"GLOSSARY.md {term} row missing companion mechanics route {companion_id}")
            elif tool_pos >= 0 and companion_pos < tool_pos:
                errors.append(f"GLOSSARY.md {term} row lists companion {companion_id} before active tool {tool_id}")

    codex_surface = read(ROOT / "indexes" / "INDEX_BY_CODEX_SURFACE.md")
    require_ids_before_fallback(
        extract_markdown_section(codex_surface, "Computer Use and browser surfaces"),
        "INDEX_BY_CODEX_SURFACE.md ## Computer Use and browser surfaces",
        ["tool.codex_computer_use", "tool.codex_browser", "tool.codex_chrome_extension"],
        ["`vcb.chapter.", "`vcb.codex."],
        errors,
    )
    require_ids_before_fallback(
        extract_markdown_section(codex_surface, "Codex Cloud and worktrees"),
        "INDEX_BY_CODEX_SURFACE.md ## Codex Cloud and worktrees",
        ["tool.codex_worktrees", "tool.codex_subagents"],
        ["`vcb.chapter.", "`vcb.codex."],
        errors,
    )
    require_ids_before_fallback(
        extract_markdown_section(codex_surface, "Codex App and local orchestration"),
        "INDEX_BY_CODEX_SURFACE.md ## Codex App and local orchestration",
        ["tool.codex_worktrees", "tool.codex_automations", "tool.codex_browser", "tool.codex_computer_use"],
        ["`vcb.chapter.", "`vcb.codex."],
        errors,
    )

    task_index = read(ROOT / "indexes" / "INDEX_BY_TASK.md")
    require_ids_before_fallback(
        extract_markdown_section(task_index, "Use cloud, subagents, browser, or GUI surfaces"),
        "INDEX_BY_TASK.md ## Use cloud, subagents, browser, or GUI surfaces",
        list(CHUNK_28_TOOL_CARDS),
        ["`vcb.shortcut.", "`vcb.chapter.", "`vcb.codex."],
        errors,
    )
    require_ids_before_fallback(
        extract_markdown_section(task_index, "Add external tools or recurring workflows"),
        "INDEX_BY_TASK.md ## Add external tools or recurring workflows",
        ["tool.codex_automations"],
        ["`vcb.shortcut.", "`vcb.chapter.", "`vcb.codex."],
        errors,
    )
    feature_section = extract_markdown_section(task_index, "Choose or use a Codex feature")
    require_ids_before_fallback(
        feature_section,
        "INDEX_BY_TASK.md ## Choose or use a Codex feature",
        list(CHUNK_28_TOOL_CARDS),
        ["`vcb.codex."],
        errors,
    )
    choose_adjunct_section = extract_markdown_section(task_index, "Choose a Codex adjunct surface")
    if not choose_adjunct_section.strip():
        errors.append("INDEX_BY_TASK.md missing ## Choose a Codex adjunct surface")
    else:
        for tid in CHUNK_28_TOOL_CARDS:
            if f"`{tid}`" not in choose_adjunct_section:
                errors.append(f"INDEX_BY_TASK.md ## Choose a Codex adjunct surface missing {tid}")

    prompt_library = read(ROOT / "indexes" / "PROMPT_LIBRARY.md")
    prompt_requirements = {
        "Cloud delegation prompt": ["tool.codex_worktrees"],
        "Subagent review prompt": ["tool.codex_subagents"],
        "Automation design prompt": ["tool.codex_automations"],
        "Browser/GUI task prompt": ["tool.codex_browser", "tool.codex_computer_use", "tool.codex_chrome_extension"],
        "Codex feature selection prompt": list(CHUNK_28_TOOL_CARDS),
    }
    for heading, required_ids in prompt_requirements.items():
        section = extract_markdown_section(prompt_library, heading)
        if not section.strip():
            errors.append(f"PROMPT_LIBRARY.md missing ## {heading}")
            continue
        require_ids_before_fallback(
            section,
            f"PROMPT_LIBRARY.md ## {heading}",
            required_ids,
            ["`vcb.shortcut.", "`vcb.codex.", "`vcb.chapter."],
            errors,
        )

    coach_index = read(ROOT / "indexes" / "INDEX_FOR_AI_COACHES.md")
    coach_section = extract_markdown_section(coach_index, "Human asks which adjunct Codex surface to use")
    if not coach_section.strip():
        errors.append("INDEX_FOR_AI_COACHES.md missing ## Human asks which adjunct Codex surface to use")
    else:
        for tid in CHUNK_28_TOOL_CARDS:
            if f"`{tid}`" not in coach_section:
                errors.append(f"INDEX_FOR_AI_COACHES.md adjunct-surface section missing {tid}")

    changelog = read(ROOT / "CHANGELOG.md")
    if len(re.findall(r"^## .*Chunk 28", changelog, flags=re.M)) != 1:
        errors.append("CHANGELOG.md must contain exactly one Chunk 28 heading")

    report = ROOT / "CHUNK_28_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_28_REPORT.md missing")
    else:
        report_text = read(report)
        if not report_text.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
            errors.append("CHUNK_28_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")
        for tid, rel in CHUNK_28_TOOL_CARDS.items():
            if f"`{tid}`" not in report_text or f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_28_REPORT.md missing created tool inventory for {tid} / {rel}")
        for rel in [
            "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md",
            "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", "indexes/INDEX_BY_TOOL_CATEGORY.md",
            "indexes/INDEX_BY_CODEX_SURFACE.md", "indexes/INDEX_BY_TASK.md", "indexes/PROMPT_LIBRARY.md",
            "indexes/INDEX_FOR_AI_COACHES.md", "indexes/GLOSSARY.md",
        ]:
            if f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_28_REPORT.md updated-file inventory omits {rel}")
        required_claims = [
            "tool-card schema validation",
            "TOOL_REGISTER active status",
            "LLM source-map routing",
            "semantic index routing",
            "first-party official OpenAI source posture",
            "scope guardrails",
        ]
        for claim in required_claims:
            if claim not in report_text:
                errors.append(f"CHUNK_28_REPORT.md missing validator-backed claim: {claim}")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 28", "adjunct", "OpenAI/Codex", "tool-card", "official OpenAI", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 28 term: {term}")



CHUNK_29_TOOL_CARDS = {
    "tool.codex_agents_md": "topics/tool-catalog/codex-agents-md.md",
    "tool.codex_config": "topics/tool-catalog/codex-config.md",
    "tool.codex_skills": "topics/tool-catalog/codex-skills.md",
    "tool.codex_mcp": "topics/tool-catalog/codex-mcp.md",
    "tool.codex_hooks": "topics/tool-catalog/codex-hooks.md",
}

CHUNK_29_ALLOWED_TOOL_CATALOG_FILES = CHUNK_28_ALLOWED_TOOL_CATALOG_FILES | set(CHUNK_29_TOOL_CARDS.values())

CHUNK_29_REQUIRED_SOURCE_IDS = {
    "vcb.register.editor_feedback_chunk_28",
    "openai.codex.agents_md",
    "openai.codex.config_basic",
    "openai.codex.config_reference",
    "openai.codex.config_advanced",
    "openai.codex.skills",
    "openai.codex.mcp",
    "openai.codex.hooks",
    "openai.codex.customization",
    "openai.codex.plugins",
    "openai.codex.agent_approvals_security",
    "openai.codex.best_practices",
    "vcb.pricing_snapshot.openai_codex",
}


def validate_chunk_29_codex_customization_control_tool_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_29":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_29_codex_customization_control_tool_cards":
        errors.append("manifest.active_chunk.id must be chunk_29_codex_customization_control_tool_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_30_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_30_editor_scoped_next_slice for Chunk 29")

    readme = read(ROOT / "README.md")
    readme_next = extract_markdown_section(readme, "Next Chunk")
    required_readme_terms = [
        "chunk_29_codex_customization_control_tool_cards",
        "bounded first-party OpenAI/Codex customization and control tool-card expansion only",
        "tool.codex_agents_md",
        "tool.codex_config",
        "tool.codex_skills",
        "tool.codex_mcp",
        "tool.codex_hooks",
        "no third-party tool cards",
        "no Codex Security tool-card expansion",
        "no feature-maturity/changelog-monitoring cards",
        "no new shortcut-card expansion",
        "chunk_30_editor_scoped_next_slice",
    ]
    for term in required_readme_terms:
        if term not in readme:
            errors.append(f"README.md missing Chunk 29 governance term: {term}")
    if "Blocked until" not in readme_next and "blocked until" not in readme_next:
        errors.append("README.md Next Chunk section must block Chunk 30 until editor approval")
    if "no AGENTS/config/skills/MCP/hooks tool-card expansion" in readme:
        errors.append("README.md still says AGENTS/config/skills/MCP/hooks tool-card expansion is non-scope after Chunk 29 authored those cards")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    for tid in CHUNK_29_TOOL_CARDS:
        rows = [line for line in tool_register.splitlines() if f"`{tid}`" in line]
        if len(rows) != 1:
            errors.append(f"TOOL_REGISTER.md must contain exactly one row for Chunk 29 tool ID {tid}; observed={len(rows)}")
        elif "| active |" not in rows[0]:
            errors.append(f"TOOL_REGISTER.md Chunk 29 tool ID is not active: {tid}")
    if "no pricing snapshot needed" in tool_register:
        errors.append("TOOL_REGISTER.md still contains stale no-pricing-snapshot note for Codex customization/control tool cards")

    source_register = read(ROOT / "SOURCE_REGISTER.md")
    for source_id in CHUNK_29_REQUIRED_SOURCE_IDS:
        if f"`{source_id}`" not in source_register:
            errors.append(f"SOURCE_REGISTER.md missing source anchor required by Chunk 29: {source_id}")

    for tid, rel in CHUNK_29_TOOL_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 29 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid:
            errors.append(f"{rel} frontmatter id mismatch: {fm.get('id')} != {tid}")
        if fm.get("type") != "tool_card":
            errors.append(f"{rel} must have type: tool_card")
        if fm.get("status") != "active":
            errors.append(f"{rel} must be active")
        if fm.get("source_status", {}).get("official_openai") is not True:
            errors.append(f"{rel} cites OpenAI sources and must set source_status.official_openai: true")
        if fm.get("source_status", {}).get("official_vendor") is not False:
            errors.append(f"{rel} first-party OpenAI tool cards should not mark official_vendor true separately from official_openai")
        if fm.get("pricing_snapshot_required") is not True or "vcb.pricing_snapshot.openai_codex" not in (fm.get("pricing_snapshot_ids") or []):
            errors.append(f"{rel} must route pricing/limits to vcb.pricing_snapshot.openai_codex")
        body = read(path)
        for volatile_forbidden in ["$", "credit value", "token limit"]:
            if volatile_forbidden in body:
                errors.append(f"{rel} may contain brittle pricing/limit prose: {volatile_forbidden}")

    topic_catalog_files = sorted(
        str(p.relative_to(ROOT)) for p in (ROOT / "topics" / "tool-catalog").glob("*.md")
        if p.name != ".gitkeep"
    )
    expected_names = sorted(CHUNK_29_ALLOWED_TOOL_CATALOG_FILES)
    if topic_catalog_files != expected_names:
        errors.append(
            "Chunk 29 tool-catalog scope drift: "
            f"observed={topic_catalog_files} expected={expected_names}"
        )

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        phrase = "First-party OpenAI/Codex customization and control tool cards from Chunk 29 are active."
        if body.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 29 tool-card phrase; observed={body.count(phrase)}")
        for heading in ["Customization and Control Codex Tool Card Fast Routing", "Active Chunk 29 Customization and Control Codex Tool Cards"]:
            section = extract_markdown_section(body, heading)
            if not section.strip():
                errors.append(f"{rel} missing ## {heading} section")
                continue
            for tid in CHUNK_29_TOOL_CARDS:
                if f"`{tid}`" not in section:
                    errors.append(f"{rel} ## {heading} missing {tid}")
        if rel == "llms.txt":
            persistent_line = next((line for line in body.splitlines() if "persistent guidance/config/tooling" in line), "")
            for tid in CHUNK_29_TOOL_CARDS:
                if f"`{tid}`" not in persistent_line:
                    errors.append(f"llms.txt persistent guidance/config/tooling route omits Chunk 29 card {tid}")
            first_fallback = min([pos for pos in [persistent_line.find("`vcb.codex."), persistent_line.find("`vcb.chapter.")] if pos >= 0], default=-1)
            for tid in CHUNK_29_TOOL_CARDS:
                pos = persistent_line.find(f"`{tid}`")
                if pos < 0 or (first_fallback >= 0 and pos > first_fallback):
                    errors.append(f"llms.txt persistent guidance/config/tooling route must list {tid} before vcb.codex/chapter fallbacks")
        if rel == "llms-full.txt":
            guidance_line = next((line for line in body.splitlines() if "Need first-party Codex tool-card guidance" in line), "")
            for tid in CHUNK_29_TOOL_CARDS:
                if f"`{tid}`" not in guidance_line:
                    errors.append(f"llms-full.txt first-party Codex tool-card guidance omits Chunk 29 card {tid}")

    required_index_surfaces = {
        "indexes/INDEX_BY_TOOL_CATEGORY.md": "Active Customization and Control OpenAI/Codex Tool Cards",
        "indexes/INDEX_BY_CODEX_SURFACE.md": "Active Customization and Control OpenAI/Codex Tool Cards",
        "indexes/INDEX_BY_TASK.md": "Active Customization and Control OpenAI/Codex Tool Cards",
        "indexes/INDEX_FOR_AI_COACHES.md": "Active Customization and Control OpenAI/Codex Tool Cards",
        "indexes/GLOSSARY.md": "Active Customization and Control OpenAI/Codex Tool Cards",
        "indexes/PROMPT_LIBRARY.md": "Active Customization and Control OpenAI/Codex Tool Cards",
    }
    for rel, heading in required_index_surfaces.items():
        body = read(ROOT / rel)
        section = extract_markdown_section(body, heading)
        if not section.strip():
            errors.append(f"{rel} missing ## {heading} section for Chunk 29")
            continue
        for tid in CHUNK_29_TOOL_CARDS:
            if f"`{tid}`" not in section:
                errors.append(f"{rel} ## {heading} missing active Chunk 29 tool route {tid}")

    # Semantic route checks: active tool cards must appear before older vcb.codex.* feature-topic fallbacks.
    semantic_sections = {
        "indexes/INDEX_BY_TOOL_CATEGORY.md": ["Persistent guidance and customization tools", "Codex feature/topic anchors"],
        "indexes/INDEX_BY_CODEX_SURFACE.md": ["Persistent customization surfaces", "Active Codex Feature Cards"],
        "indexes/INDEX_BY_CONCEPT.md": ["Persistent guidance and customization concepts", "Codex product features and surfaces"],
        "indexes/INDEX_BY_BUDGET_PROFILE.md": ["Budget-aware Codex feature selection"],
        "indexes/INDEX_BY_RECOVERABILITY.md": ["Recoverability by Codex feature"],
        "indexes/INDEX_BY_RISK_LEVEL.md": ["Codex feature risk routing"],
        "indexes/INDEX_BY_FAILURE_MODE.md": ["Codex feature misuse"],
        "indexes/INDEX_BY_PROJECT_TYPE.md": ["Codex feature selection by project type"],
        "indexes/INDEX_BY_STABILITY.md": ["Quarterly review — Codex feature families", "Codex feature cards requiring quarterly/monthly review"],
        "indexes/INDEX_BY_SHORTCUT.md": ["Shortcuts around Codex features", "Tool-sprawl, skill, MCP, and reusable workflow shortcut routes"],
        "indexes/INDEX_BY_TASK.md": ["Choose or use a Codex feature"],
        "indexes/PROMPT_LIBRARY.md": ["Codex feature selection prompt"],
        "indexes/INDEX_FOR_AI_COACHES.md": ["Human asks how to choose or use a Codex feature"],
    }
    fallback_needles = ["`vcb.codex.agents_md`", "`vcb.codex.config`", "`vcb.codex.skills`", "`vcb.codex.mcp`", "`vcb.codex.hooks`"]
    for rel, headings in semantic_sections.items():
        body = read(ROOT / rel)
        for heading in headings:
            section = extract_markdown_section(body, heading)
            if not section.strip():
                errors.append(f"{rel} missing ## {heading}")
                continue
            require_ids_before_fallback(
                section,
                f"{rel} ## {heading}",
                list(CHUNK_29_TOOL_CARDS),
                fallback_needles + ["`vcb.chapter."],
                errors,
            )

    targeted_task_routes = {
        "Set up Codex safely": ["tool.codex_config", "tool.codex_agents_md"],
        "Make guidance durable": ["tool.codex_agents_md", "tool.codex_config", "tool.codex_skills", "tool.codex_hooks"],
        "Add external tools or recurring workflows": ["tool.codex_mcp", "tool.codex_hooks", "tool.codex_config"],
        "Set up or configure Codex for a repo": ["tool.codex_agents_md", "tool.codex_config"],
        "Configure Codex or AGENTS.md safely": ["tool.codex_agents_md", "tool.codex_config"],
        "Use hooks, MCP, skills, or external tools": ["tool.codex_skills", "tool.codex_mcp", "tool.codex_hooks"],
        "Add hooks, tools, or external context": ["tool.codex_mcp", "tool.codex_hooks", "tool.codex_skills"],
        "Adopt skills, MCP, plugins, hooks, or reusable process safely": ["tool.codex_skills", "tool.codex_mcp", "tool.codex_hooks"],
        "Turn prompts into team workflow": [
            "tool.codex_agents_md",
            "tool.codex_config",
            "tool.codex_skills",
            "tool.codex_hooks",
            "tool.codex_mcp",
        ],
        "Adopt tools, hooks, plugins, or MCP safely": [
            "tool.codex_skills",
            "tool.codex_mcp",
            "tool.codex_hooks",
            "tool.codex_config",
            "tool.codex_agents_md",
        ],
    }
    task_index = read(ROOT / "indexes" / "INDEX_BY_TASK.md")
    for heading, ids in targeted_task_routes.items():
        section = extract_markdown_section(task_index, heading)
        if not section.strip():
            errors.append(f"INDEX_BY_TASK.md missing ## {heading}")
            continue
        require_ids_before_fallback(
            section,
            f"INDEX_BY_TASK.md ## {heading}",
            ids,
            ["`vcb.shortcut.", "`vcb.codex.", "`vcb.chapter."],
            errors,
        )

    prompt_library = read(ROOT / "indexes" / "PROMPT_LIBRARY.md")
    team_workflow_prompt = extract_markdown_section(prompt_library, "Team workflow promotion prompt")
    if not team_workflow_prompt.strip():
        errors.append("PROMPT_LIBRARY.md missing ## Team workflow promotion prompt")
    else:
        require_ids_before_fallback(
            team_workflow_prompt,
            "PROMPT_LIBRARY.md ## Team workflow promotion prompt",
            [
                "tool.codex_agents_md",
                "tool.codex_config",
                "tool.codex_skills",
                "tool.codex_hooks",
                "tool.codex_mcp",
                "tool.codex_automations",
                "tool.codex_github_review",
                "tool.codex_exec",
            ],
            ["`vcb.chapter.prompt_library_to_team_workflow`", "`vcb.chapter.", "`vcb.codex."],
            errors,
        )

    glossary = read(ROOT / "indexes" / "GLOSSARY.md")
    feature_terms = extract_markdown_section(glossary, "Codex feature-card terms")
    expected_glossary_routes = {
        "AGENTS.md": "tool.codex_agents_md",
        "Codex config": "tool.codex_config",
        "Codex skill": "tool.codex_skills",
        "MCP": "tool.codex_mcp",
        "Codex hook": "tool.codex_hooks",
    }
    for term, tid in expected_glossary_routes.items():
        term_line = next((line for line in feature_terms.splitlines() if f"`{term}`" in line), "")
        if f"`{tid}`" not in term_line:
            errors.append(f"GLOSSARY.md Codex feature-card term {term!r} does not route first to {tid}")
        if "companion mechanics" not in term_line and term not in {"MCP"}:
            errors.append(f"GLOSSARY.md Codex feature-card term {term!r} should retain companion mechanics wording")

    changelog = read(ROOT / "CHANGELOG.md")
    if len(re.findall(r"^## .*Chunk 29", changelog, flags=re.M)) != 1:
        errors.append("CHANGELOG.md must contain exactly one Chunk 29 heading")

    report = ROOT / "CHUNK_29_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_29_REPORT.md missing")
    else:
        report_text = read(report)
        if not report_text.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
            errors.append("CHUNK_29_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")
        for tid, rel in CHUNK_29_TOOL_CARDS.items():
            if f"`{tid}`" not in report_text or f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_29_REPORT.md missing created tool inventory for {tid} / {rel}")
        for rel in [
            "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md",
            "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", "indexes/INDEX_BY_TOOL_CATEGORY.md",
            "indexes/INDEX_BY_CODEX_SURFACE.md", "indexes/INDEX_BY_TASK.md", "indexes/PROMPT_LIBRARY.md",
            "indexes/INDEX_FOR_AI_COACHES.md", "indexes/GLOSSARY.md",
        ]:
            if f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_29_REPORT.md updated-file inventory omits {rel}")
        required_claims = [
            "tool-card schema validation",
            "TOOL_REGISTER active status",
            "LLM source-map routing",
            "semantic index routing",
            "first-party official OpenAI source posture",
            "scope guardrails",
        ]
        for claim in required_claims:
            if claim not in report_text:
                errors.append(f"CHUNK_29_REPORT.md missing validator-backed claim: {claim}")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 29", "customization", "control", "OpenAI/Codex", "tool-card", "official OpenAI", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 29 term: {term}")


CHUNK_30_TOOL_CARDS = {
    "tool.codex_security": "topics/tool-catalog/codex-security.md",
}

CHUNK_30_ALLOWED_TOOL_CATALOG_FILES = CHUNK_29_ALLOWED_TOOL_CATALOG_FILES | set(CHUNK_30_TOOL_CARDS.values())

CHUNK_30_REQUIRED_SOURCE_IDS = {
    "vcb.register.editor_feedback_chunk_29",
    "openai.codex.security",
    "openai.codex.security_plugin",
    "openai.codex.security_setup",
    "openai.codex.security_threat_model",
    "openai.codex.security_faq",
    "openai.codex.agent_approvals_security",
    "vcb.pricing_snapshot.openai_codex",
}


def validate_chunk_30_codex_security_tool_card(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_30":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_30_codex_security_tool_card":
        errors.append("manifest.active_chunk.id must be chunk_30_codex_security_tool_card")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_31_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_31_editor_scoped_next_slice for Chunk 30")

    readme = read(ROOT / "README.md")
    readme_next = extract_markdown_section(readme, "Next Chunk")
    required_readme_terms = [
        "chunk_30_codex_security_tool_card",
        "bounded first-party OpenAI/Codex Security tool-card expansion only",
        "tool.codex_security",
        "no third-party tool cards",
        "no feature-maturity/changelog-monitoring",
        "no broad security/secrets topic expansion",
        "no new shortcut-card expansion",
        "chunk_31_editor_scoped_next_slice",
    ]
    for term in required_readme_terms:
        if term not in readme:
            errors.append(f"README.md missing Chunk 30 governance term: {term}")
    if "Blocked until" not in readme_next and "blocked until" not in readme_next:
        errors.append("README.md Next Chunk section must block Chunk 31 until editor approval")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    for tid in CHUNK_30_TOOL_CARDS:
        rows = [line for line in tool_register.splitlines() if f"`{tid}`" in line]
        if len(rows) != 1:
            errors.append(f"TOOL_REGISTER.md must contain exactly one row for Chunk 30 tool ID {tid}; observed={len(rows)}")
        elif "| active |" not in rows[0]:
            errors.append(f"TOOL_REGISTER.md Chunk 30 tool ID is not active: {tid}")
    if "## Chunk 30 Codex Security Tool Card Activation Note" not in tool_register:
        errors.append("TOOL_REGISTER.md missing Chunk 30 Codex Security activation note")

    source_register = read(ROOT / "SOURCE_REGISTER.md")
    for source_id in CHUNK_30_REQUIRED_SOURCE_IDS:
        if f"`{source_id}`" not in source_register:
            errors.append(f"SOURCE_REGISTER.md missing source anchor required by Chunk 30: {source_id}")

    for tid, rel in CHUNK_30_TOOL_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 30 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid:
            errors.append(f"{rel} frontmatter id mismatch: {fm.get('id')} != {tid}")
        if fm.get("type") != "tool_card":
            errors.append(f"{rel} must have type: tool_card")
        if fm.get("status") != "active":
            errors.append(f"{rel} must be active")
        if fm.get("source_status", {}).get("official_openai") is not True:
            errors.append(f"{rel} cites OpenAI sources and must set source_status.official_openai: true")
        if fm.get("source_status", {}).get("official_vendor") is not False:
            errors.append(f"{rel} first-party OpenAI tool card should not mark official_vendor true separately from official_openai")
        if fm.get("pricing_snapshot_required") is not True or "vcb.pricing_snapshot.openai_codex" not in (fm.get("pricing_snapshot_ids") or []):
            errors.append(f"{rel} must route pricing/limits to vcb.pricing_snapshot.openai_codex")
        body = read(path)
        for volatile_forbidden in ["$", "credit value", "token limit"]:
            if volatile_forbidden in body:
                errors.append(f"{rel} may contain brittle pricing/limit prose: {volatile_forbidden}")
        for sid in [
            "openai.codex.security",
            "openai.codex.security_plugin",
            "openai.codex.security_setup",
            "openai.codex.security_threat_model",
            "openai.codex.security_faq",
            "openai.codex.agent_approvals_security",
        ]:
            if f"`{sid}`" not in body:
                errors.append(f"{rel} missing Evidence and Sources route for {sid}")

    topic_catalog_files = sorted(
        str(p.relative_to(ROOT)) for p in (ROOT / "topics" / "tool-catalog").glob("*.md")
        if p.name != ".gitkeep"
    )
    expected_names = sorted(CHUNK_30_ALLOWED_TOOL_CATALOG_FILES)
    if topic_catalog_files != expected_names:
        errors.append(
            "Chunk 30 tool-catalog scope drift: "
            f"observed={topic_catalog_files} expected={expected_names}"
        )

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        phrase = "First-party OpenAI/Codex Security tool card from Chunk 30 is active."
        if body.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 30 tool-card phrase; observed={body.count(phrase)}")
        for heading in ["Codex Security Tool Card Fast Routing", "Active Chunk 30 Codex Security Tool Card"]:
            section = extract_markdown_section(body, heading)
            if not section.strip():
                errors.append(f"{rel} missing ## {heading} section")
                continue
            if "`tool.codex_security`" not in section:
                errors.append(f"{rel} ## {heading} missing tool.codex_security")
        security_line = next((line for line in body.splitlines() if "Codex Security" in line and "security review" in line and "retrieve" in line), "")
        if "`tool.codex_security`" not in security_line:
            errors.append(f"{rel} security-review fast route must retrieve tool.codex_security first for Codex Security intents")
        if rel == "llms-full.txt":
            first_party_line = next((line for line in body.splitlines() if "Need first-party Codex tool-card guidance" in line), "")
            if not first_party_line:
                errors.append("llms-full.txt missing Need first-party Codex tool-card guidance route")
            elif "`tool.codex_security`" not in first_party_line:
                errors.append("llms-full.txt Need first-party Codex tool-card guidance route omits tool.codex_security")

    # Editor-reported semantic route checks for Chunk 30: generic feature/tool-selection
    # paths must route Codex Security to the active tool card before older fallbacks.
    task_feature_section = extract_markdown_section(read(ROOT / "indexes" / "INDEX_BY_TASK.md"), "Choose or use a Codex feature")
    if not task_feature_section.strip():
        errors.append("INDEX_BY_TASK.md missing ## Choose or use a Codex feature")
    else:
        require_ids_before_fallback(
            task_feature_section,
            "INDEX_BY_TASK.md ## Choose or use a Codex feature",
            ["tool.codex_security"],
            ["`vcb.codex.", "`vcb.chapter."],
            errors,
        )

    prompt_library = read(ROOT / "indexes" / "PROMPT_LIBRARY.md")
    feature_prompt_section = extract_markdown_section(prompt_library, "Codex feature selection prompt")
    if not feature_prompt_section.strip():
        errors.append("PROMPT_LIBRARY.md missing ## Codex feature selection prompt")
    else:
        require_ids_before_fallback(
            feature_prompt_section,
            "PROMPT_LIBRARY.md ## Codex feature selection prompt",
            ["tool.codex_security"],
            ["`vcb.codex.", "`vcb.chapter."],
            errors,
        )

    auth_prompt_section = extract_markdown_section(prompt_library, "Auth-sensitive hardening prompt")
    if not auth_prompt_section.strip():
        errors.append("PROMPT_LIBRARY.md missing ## Auth-sensitive hardening prompt")
    else:
        require_ids_before_fallback(
            auth_prompt_section,
            "PROMPT_LIBRARY.md ## Auth-sensitive hardening prompt",
            ["tool.codex_security"],
            ["`vcb.safety.", "`vcb.chapter."],
            errors,
        )
        if "`vcb.safety.security_review`" not in auth_prompt_section:
            errors.append("PROMPT_LIBRARY.md ## Auth-sensitive hardening prompt must include vcb.safety.security_review companion route")

    coach_feature_section = extract_markdown_section(read(ROOT / "indexes" / "INDEX_FOR_AI_COACHES.md"), "Human asks how to choose or use a Codex feature")
    if not coach_feature_section.strip():
        errors.append("INDEX_FOR_AI_COACHES.md missing ## Human asks how to choose or use a Codex feature")
    else:
        require_ids_before_fallback(
            coach_feature_section,
            "INDEX_FOR_AI_COACHES.md ## Human asks how to choose or use a Codex feature",
            ["tool.codex_security"],
            ["`vcb.codex.", "`vcb.chapter."],
            errors,
        )

    required_index_surfaces = {
        "indexes/INDEX_BY_TOOL_CATEGORY.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_CODEX_SURFACE.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_TASK.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_RISK_LEVEL.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_FAILURE_MODE.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_CONCEPT.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_BUDGET_PROFILE.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_RECOVERABILITY.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_PROJECT_TYPE.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_STABILITY.md": "Active Codex Security Tool Card",
        "indexes/INDEX_BY_SHORTCUT.md": "Active Codex Security Tool Card",
        "indexes/INDEX_FOR_AI_COACHES.md": "Active Codex Security Tool Card",
        "indexes/GLOSSARY.md": "Active Codex Security Tool Card",
        "indexes/PROMPT_LIBRARY.md": "Active Codex Security Tool Card",
    }
    for rel, heading in required_index_surfaces.items():
        section = extract_markdown_section(read(ROOT / rel), heading)
        if not section.strip():
            errors.append(f"{rel} missing ## {heading} section for Chunk 30")
            continue
        if "`tool.codex_security`" not in section:
            errors.append(f"{rel} ## {heading} missing active Chunk 30 tool route tool.codex_security")

    semantic_sections = {
        "indexes/INDEX_BY_TOOL_CATEGORY.md": ["Review, security, and CI tools"],
        "indexes/INDEX_BY_CODEX_SURFACE.md": ["Surface selection", "Codex Security and security review surfaces"],
        "indexes/INDEX_BY_TASK.md": ["Do security-sensitive work", "Run Codex Security scan or review findings", "Harden auth-sensitive code", "Review Codex output or a PR"],
        "indexes/INDEX_BY_RISK_LEVEL.md": ["High-risk production work", "Codex feature risk routing", "Never with real secrets or sensitive user data"],
        "indexes/INDEX_BY_FAILURE_MODE.md": ["Security-sensitive behavior is under-specified", "Codex feature misuse", "CI passes but does not prove the risk"],
        "indexes/INDEX_BY_CONCEPT.md": ["Review, security, and automation concepts", "Codex product features and surfaces"],
        "indexes/INDEX_BY_BUDGET_PROFILE.md": ["Production-quality path", "Budget-aware Codex feature selection"],
        "indexes/INDEX_BY_RECOVERABILITY.md": ["Hard to recover", "Recoverability by Codex feature"],
        "indexes/INDEX_BY_PROJECT_TYPE.md": ["Auth/payment/data-sensitive system", "Codex feature selection by project type"],
        "indexes/INDEX_BY_STABILITY.md": ["Quarterly review — Codex feature families", "Monthly review — volatile Codex surfaces, commands, and economics", "Codex feature cards requiring quarterly/monthly review"],
        "indexes/INDEX_BY_SHORTCUT.md": ["Setup, permission, and automation shortcuts", "Shortcuts around Codex features"],
        "indexes/INDEX_FOR_AI_COACHES.md": ["Human wants to skip planning, tests, review, or security", "Human asks whether Codex Security can replace security review"],
        "indexes/PROMPT_LIBRARY.md": ["Security review prompt"],
    }
    fallback_needles = ["`vcb.safety.", "`vcb.workflow.", "`vcb.chapter.", "`vcb.codex.", "`vcb.shortcut."]
    for rel, headings in semantic_sections.items():
        body = read(ROOT / rel)
        for heading in headings:
            section = extract_markdown_section(body, heading)
            if not section.strip():
                errors.append(f"{rel} missing ## {heading}")
                continue
            require_ids_before_fallback(
                section,
                f"{rel} ## {heading}",
                ["tool.codex_security"],
                fallback_needles,
                errors,
            )

    glossary = read(ROOT / "indexes" / "GLOSSARY.md")
    feature_terms = extract_markdown_section(glossary, "Codex feature-card terms")
    lines = [line for line in feature_terms.splitlines() if line.startswith("- `Codex Security`")]
    if len(lines) != 1:
        errors.append("GLOSSARY.md ## Codex feature-card terms must have exactly one Codex Security term row")
    elif "`tool.codex_security`" not in lines[0]:
        errors.append("GLOSSARY.md Codex Security term row must route to tool.codex_security")

    changelog = read(ROOT / "CHANGELOG.md")
    if len(re.findall(r"^## .*Chunk 30", changelog, flags=re.M)) != 1:
        errors.append("CHANGELOG.md must contain exactly one Chunk 30 heading")

    report = ROOT / "CHUNK_30_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_30_REPORT.md missing")
    else:
        report_text = read(report)
        if not report_text.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
            errors.append("CHUNK_30_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")
        for tid, rel in CHUNK_30_TOOL_CARDS.items():
            if f"`{tid}`" not in report_text or f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_30_REPORT.md missing created tool inventory for {tid} / {rel}")
        for rel in [
            "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md",
            "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", "indexes/INDEX_BY_TOOL_CATEGORY.md",
            "indexes/INDEX_BY_CODEX_SURFACE.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_RISK_LEVEL.md",
            "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/PROMPT_LIBRARY.md", "indexes/INDEX_FOR_AI_COACHES.md",
            "indexes/GLOSSARY.md",
        ]:
            if f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_30_REPORT.md updated-file inventory omits {rel}")
        required_claims = [
            "tool-card schema validation",
            "TOOL_REGISTER active status",
            "LLM source-map routing",
            "semantic index routing",
            "first-party official OpenAI source posture",
            "scope guardrails",
        ]
        for claim in required_claims:
            if claim not in report_text:
                errors.append(f"CHUNK_30_REPORT.md missing validator-backed claim: {claim}")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 30", "Codex Security", "OpenAI/Codex", "tool-card", "official OpenAI", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 30 term: {term}")


CHUNK_31_TOOL_CARDS = {
    "tool.codex_feature_maturity": "topics/tool-catalog/codex-feature-maturity.md",
    "tool.codex_changelog_monitoring": "topics/tool-catalog/codex-changelog-monitoring.md",
}

CHUNK_31_ALLOWED_TOOL_CATALOG_FILES = CHUNK_30_ALLOWED_TOOL_CATALOG_FILES | set(CHUNK_31_TOOL_CARDS.values())

CHUNK_31_REQUIRED_SOURCE_IDS = {
    "vcb.register.editor_feedback_chunk_30",
    "openai.codex.feature_maturity",
    "openai.codex.changelog",
    "openai.codex.overview",
    "openai.codex.use_cases.update_documentation",
    "vcb.pricing_snapshot.openai_codex",
}



def source_row_checked_date(source_register: str, source_id: str) -> str | None:
    for line in source_register.splitlines():
        if line.strip().startswith(f"| `{source_id}` "):
            match = re.search(r"anchor checked (\d{4}-\d{2}-\d{2})", line)
            return match.group(1) if match else None
    return None


def chunk31_refresh_overclaim_sentences() -> list[str]:
    texts: list[str] = []
    source_register = read(ROOT / "SOURCE_REGISTER.md")
    texts.extend(line for line in source_register.splitlines() if "Chunk 31" in line)
    changelog = extract_markdown_section(read(ROOT / "CHANGELOG.md"), "2026-06-11 — Chunk 31 Codex governance/maintenance tool-card expansion")
    texts.append(changelog)
    report = read(ROOT / "CHUNK_31_REPORT.md") if (ROOT / "CHUNK_31_REPORT.md").exists() else ""
    texts.append(report)
    joined = "\n".join(texts)
    return [s.strip() for s in re.split(r"(?<=[.!?])\s+|\n", joined) if s.strip()]


def sentence_claims_refresh(sentence: str, labels: list[str]) -> bool:
    if not re.search(r"(?<![-A-Za-z0-9_])refresh(?:ed|es|ing)?\b", sentence, flags=re.I):
        return False
    lowered = sentence.lower()
    return any(label.lower() in lowered for label in labels)

def validate_chunk_31_codex_governance_tool_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_31":
        return

    required_ids = list(CHUNK_31_TOOL_CARDS)
    if manifest.get("active_chunk", {}).get("id") != "chunk_31_codex_governance_tool_cards":
        errors.append("manifest.active_chunk.id must be chunk_31_codex_governance_tool_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_32_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_32_editor_scoped_next_slice for Chunk 31")

    readme = read(ROOT / "README.md")
    readme_next = extract_markdown_section(readme, "Next Chunk")
    required_readme_terms = [
        "chunk_31_codex_governance_tool_cards",
        "bounded first-party OpenAI/Codex governance and maintenance tool-card expansion only",
        "tool.codex_feature_maturity",
        "tool.codex_changelog_monitoring",
        "no third-party tool cards",
        "no broad tool-card expansion",
        "no new shortcut-card expansion",
        "chunk_32_editor_scoped_next_slice",
    ]
    for term in required_readme_terms:
        if term not in readme:
            errors.append(f"README.md missing Chunk 31 governance term: {term}")
    if "Blocked until" not in readme_next and "blocked until" not in readme_next:
        errors.append("README.md Next Chunk section must block Chunk 32 until editor approval")
    if "Codex Security" in readme_next or "security tool-card" in readme_next.lower():
        errors.append("README.md Next Chunk section must not carry stale Chunk 30 security scope into Chunk 32")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    for tid in required_ids:
        rows = [line for line in tool_register.splitlines() if f"`{tid}`" in line]
        if len(rows) != 1:
            errors.append(f"TOOL_REGISTER.md must contain exactly one row for Chunk 31 tool ID {tid}; observed={len(rows)}")
        elif "| active |" not in rows[0]:
            errors.append(f"TOOL_REGISTER.md Chunk 31 tool ID is not active: {tid}")
    if "## Chunk 31 Codex Governance and Maintenance Tool Card Activation Note" not in tool_register:
        errors.append("TOOL_REGISTER.md missing Chunk 31 governance/maintenance activation note")

    source_register = read(ROOT / "SOURCE_REGISTER.md")
    for source_id in CHUNK_31_REQUIRED_SOURCE_IDS:
        if f"`{source_id}`" not in source_register:
            errors.append(f"SOURCE_REGISTER.md missing source anchor required by Chunk 31: {source_id}")

    readme_governance_section = extract_markdown_section(readme, "Active Codex Governance and Maintenance Tool Cards")
    if not readme_governance_section.strip():
        errors.append("README.md missing ## Active Codex Governance and Maintenance Tool Cards section")
    else:
        for tid in required_ids:
            if f"`{tid}`" not in readme_governance_section:
                errors.append(f"README.md active governance/maintenance tool-card section missing {tid}")

    refresh_claim_sentences = chunk31_refresh_overclaim_sentences()
    stale_refreshed_sources = {
        "openai.codex.overview": ["openai.codex.overview", "Codex overview"],
        "openai.codex.use_cases.update_documentation": ["openai.codex.use_cases.update_documentation", "documentation-update", "documentation update", "Keep documentation up-to-date"],
    }
    for sid, labels in stale_refreshed_sources.items():
        row_date = source_row_checked_date(source_register, sid)
        if row_date != "2026-06-11" and any(sentence_claims_refresh(sentence, labels) for sentence in refresh_claim_sentences):
            errors.append(
                f"Chunk 31 report/changelog/source-register claims {sid} was refreshed, "
                f"but SOURCE_REGISTER row checked date is {row_date!r}"
            )

    for tid, rel in CHUNK_31_TOOL_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 31 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid:
            errors.append(f"{rel} frontmatter id mismatch: {fm.get('id')} != {tid}")
        if fm.get("type") != "tool_card":
            errors.append(f"{rel} must have type: tool_card")
        if fm.get("status") != "active":
            errors.append(f"{rel} must be active")
        if fm.get("source_status", {}).get("official_openai") is not True:
            errors.append(f"{rel} cites OpenAI sources and must set source_status.official_openai: true")
        if fm.get("source_status", {}).get("official_vendor") is not False:
            errors.append(f"{rel} first-party OpenAI tool card should not mark official_vendor true separately from official_openai")
        if fm.get("pricing_snapshot_required") is not True or "vcb.pricing_snapshot.openai_codex" not in (fm.get("pricing_snapshot_ids") or []):
            errors.append(f"{rel} must route pricing/limits to vcb.pricing_snapshot.openai_codex")
        body = read(path)
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in body:
                errors.append(f"{rel} missing required heading: {heading}")
        for volatile_forbidden in ["$", "credit value", "token limit"]:
            if volatile_forbidden in body:
                errors.append(f"{rel} may contain brittle pricing/limit prose: {volatile_forbidden}")
        expected_sources = ["openai.codex.feature_maturity", "openai.codex.changelog", "openai.codex.overview", "vcb.pricing_snapshot.openai_codex", "vcb.register.editor_feedback_chunk_30"]
        if tid == "tool.codex_changelog_monitoring":
            expected_sources.append("openai.codex.use_cases.update_documentation")
        for sid in expected_sources:
            if f"`{sid}`" not in body:
                errors.append(f"{rel} missing Evidence and Sources route for {sid}")

    topic_catalog_files = sorted(
        str(p.relative_to(ROOT)) for p in (ROOT / "topics" / "tool-catalog").glob("*.md")
        if p.name != ".gitkeep"
    )
    expected_names = sorted(CHUNK_31_ALLOWED_TOOL_CATALOG_FILES)
    if topic_catalog_files != expected_names:
        errors.append(
            "Chunk 31 tool-catalog scope drift: "
            f"observed={topic_catalog_files} expected={expected_names}"
        )
    source_artifacts = manifest.get("source_artifacts", {}) if isinstance(manifest.get("source_artifacts"), dict) else {}
    listed_tool_catalog = sorted(source_artifacts.get("tool_catalog_files", []))
    if listed_tool_catalog != topic_catalog_files:
        errors.append(
            "manifest.source_artifacts.tool_catalog_files omits or adds tool-catalog files: "
            f"listed={listed_tool_catalog} actual={topic_catalog_files}"
        )
    if int(source_artifacts.get("tool_catalog_files_count", -1)) != len(topic_catalog_files):
        errors.append(
            "manifest.source_artifacts.tool_catalog_files_count does not match actual non-placeholder tool-catalog files: "
            f"{source_artifacts.get('tool_catalog_files_count')!r} != {len(topic_catalog_files)}"
        )

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        phrase = "First-party OpenAI/Codex governance and maintenance tool cards from Chunk 31 are active."
        if body.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 31 tool-card phrase; observed={body.count(phrase)}")
        for heading in ["Codex Governance and Maintenance Tool Card Fast Routing", "Active Chunk 31 Codex Governance and Maintenance Tool Cards"]:
            section = extract_markdown_section(body, heading)
            if not section.strip():
                errors.append(f"{rel} missing ## {heading} section")
                continue
            for tid in required_ids:
                if f"`{tid}`" not in section:
                    errors.append(f"{rel} ## {heading} missing {tid}")
        current_line = next((line for line in body.splitlines() if "current/deprecation review" in line or "feature maturity review" in line), "")
        if current_line and not all(f"`{tid}`" in current_line for tid in required_ids):
            errors.append(f"{rel} current/deprecation review route must retrieve Chunk 31 governance tool cards first")

    required_index_surfaces = {
        "indexes/INDEX_BY_TOOL_CATEGORY.md": "Active Codex Governance and Maintenance Tool Cards",
        "indexes/INDEX_BY_CODEX_SURFACE.md": "Codex governance and maintenance surfaces",
        "indexes/INDEX_BY_TASK.md": "Active Codex Governance and Maintenance Tool Cards",
        "indexes/INDEX_BY_STABILITY.md": "Active Codex Governance and Maintenance Tool Cards",
        "indexes/INDEX_FOR_AI_COACHES.md": "Active Codex Governance and Maintenance Tool Cards",
        "indexes/GLOSSARY.md": "Active Codex Governance and Maintenance Tool Cards",
        "indexes/PROMPT_LIBRARY.md": "Active Codex Governance and Maintenance Tool Cards",
    }
    for rel, heading in required_index_surfaces.items():
        section = extract_markdown_section(read(ROOT / rel), heading)
        if not section.strip():
            errors.append(f"{rel} missing ## {heading} section for Chunk 31")
            continue
        for tid in required_ids:
            if f"`{tid}`" not in section:
                errors.append(f"{rel} ## {heading} missing active Chunk 31 tool route {tid}")

    semantic_sections = {
        "indexes/INDEX_BY_TOOL_CATEGORY.md": ["Source/update maintenance tools", "Codex feature/topic anchors"],
        "indexes/INDEX_BY_CODEX_SURFACE.md": ["Codex governance and maintenance surfaces", "Active Codex Feature Cards"],
        "indexes/INDEX_BY_TASK.md": ["Maintain or update the Bible", "Choose or use a Codex feature", "Monitor Codex maturity, changelog, or deprecations"],
        "indexes/INDEX_BY_STABILITY.md": ["Monthly review — volatile Codex surfaces, commands, and economics", "Codex feature cards requiring quarterly/monthly review"],
        "indexes/INDEX_FOR_AI_COACHES.md": ["Human is updating Bible/source guidance", "Human asks how to choose or use a Codex feature", "Human asks about Codex maturity, changelog, or deprecation watch"],
        "indexes/PROMPT_LIBRARY.md": ["Bible update prompt", "Codex feature selection prompt", "Codex maturity and changelog review prompt"],
        "indexes/INDEX_BY_CONCEPT.md": ["Deprecation and update hygiene", "Codex product features and surfaces"],
        "indexes/INDEX_BY_FAILURE_MODE.md": ["Bible guidance became stale", "Codex feature misuse"],
        "indexes/INDEX_BY_BUDGET_PROFILE.md": ["Maintenance budget and update hygiene", "Budget-aware Codex feature selection"],
        "indexes/INDEX_BY_RECOVERABILITY.md": ["Recover from stale or bad guidance", "Recoverability by Codex feature"],
        "indexes/INDEX_BY_RISK_LEVEL.md": ["Codex feature risk routing"],
        "indexes/INDEX_BY_PROJECT_TYPE.md": ["Codex feature selection by project type"],
        "indexes/INDEX_BY_SHORTCUT.md": ["Update-maintenance shortcuts", "Shortcuts around Codex features"],
    }
    fallback_needles = ["`vcb.codex.", "`vcb.chapter.", "SOURCE_REGISTER.md", "DEPRECATION_REGISTER.md", "`vcb.workflow.", "`vcb.shortcut."]
    for rel, headings in semantic_sections.items():
        body = read(ROOT / rel)
        for heading in headings:
            section = extract_markdown_section(body, heading)
            if not section.strip():
                errors.append(f"{rel} missing ## {heading}")
                continue
            require_ids_before_fallback(section, f"{rel} ## {heading}", required_ids, fallback_needles, errors)

    concept_mental_model = extract_markdown_section(read(ROOT / "indexes" / "INDEX_BY_CONCEPT.md"), "Codex mental model concepts")
    if "`tool.codex_feature_maturity`" not in concept_mental_model:
        errors.append("INDEX_BY_CONCEPT.md ## Codex mental model concepts missing tool.codex_feature_maturity")
    else:
        tool_pos = concept_mental_model.find("`tool.codex_feature_maturity`")
        old_pos = concept_mental_model.find("`vcb.codex.feature_maturity`")
        if old_pos >= 0 and old_pos < tool_pos:
            errors.append("INDEX_BY_CONCEPT.md ## Codex mental model concepts routes vcb.codex.feature_maturity before tool.codex_feature_maturity")

    llms_feature_fast = extract_markdown_section(read(ROOT / "llms.txt"), "Codex Feature Card Fast Routing")
    feature_pairs = [
        ("tool.codex_feature_maturity", "vcb.codex.feature_maturity"),
        ("tool.codex_changelog_monitoring", "vcb.codex.changelog_monitoring"),
    ]
    for tool_id, companion_id in feature_pairs:
        tool_pos = llms_feature_fast.find(f"`{tool_id}`")
        companion_pos = llms_feature_fast.find(f"`{companion_id}`")
        if tool_pos < 0:
            errors.append(f"llms.txt ## Codex Feature Card Fast Routing missing active tool-card route {tool_id}")
        if companion_pos >= 0 and (tool_pos < 0 or companion_pos < tool_pos):
            errors.append(f"llms.txt ## Codex Feature Card Fast Routing routes {companion_id} without {tool_id} first")

    glossary_terms = extract_markdown_section(read(ROOT / "indexes" / "GLOSSARY.md"), "Codex feature-card terms")
    for term, tid in [("feature maturity", "tool.codex_feature_maturity"), ("Codex changelog", "tool.codex_changelog_monitoring")]:
        lines = [line for line in glossary_terms.splitlines() if line.startswith(f"- `{term}`")]
        if len(lines) != 1:
            errors.append(f"GLOSSARY.md ## Codex feature-card terms must have exactly one {term} term row")
        elif f"`{tid}`" not in lines[0]:
            errors.append(f"GLOSSARY.md {term} term row must route to {tid}")

    changelog = read(ROOT / "CHANGELOG.md")
    if len(re.findall(r"^## .*Chunk 31", changelog, flags=re.M)) != 1:
        errors.append("CHANGELOG.md must contain exactly one Chunk 31 heading")

    report = ROOT / "CHUNK_31_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_31_REPORT.md missing")
    else:
        report_text = read(report)
        if not report_text.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
            errors.append("CHUNK_31_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")
        for tid, rel in CHUNK_31_TOOL_CARDS.items():
            if f"`{tid}`" not in report_text or f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_31_REPORT.md missing created tool inventory for {tid} / {rel}")
        for rel in [
            "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md",
            "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", "indexes/INDEX_BY_TOOL_CATEGORY.md",
            "indexes/INDEX_BY_CODEX_SURFACE.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_STABILITY.md",
            "indexes/PROMPT_LIBRARY.md", "indexes/INDEX_FOR_AI_COACHES.md", "indexes/GLOSSARY.md",
        ]:
            if f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_31_REPORT.md updated-file inventory omits {rel}")
        required_claims = [
            "tool-card schema validation",
            "TOOL_REGISTER active status",
            "LLM source-map routing",
            "semantic index routing",
            "first-party official OpenAI source posture",
            "scope guardrails",
            "nested manifest",
            "source overclaim",
        ]
        for claim in required_claims:
            if claim not in report_text:
                errors.append(f"CHUNK_31_REPORT.md missing validator-backed claim: {claim}")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 31", "governance", "maintenance", "feature maturity", "changelog", "OpenAI/Codex", "tool-card", "official OpenAI", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 31 term: {term}")


CHUNK_32_TOOL_CARDS = {
    "tool.github": "topics/tool-catalog/github.md",
    "tool.github_actions": "topics/tool-catalog/github-actions.md",
    "tool.github_dependabot": "topics/tool-catalog/github-dependabot.md",
    "tool.npm": "topics/tool-catalog/npm.md",
    "tool.playwright": "topics/tool-catalog/playwright.md",
    "tool.openssf_scorecard": "topics/tool-catalog/openssf-scorecard.md",
}


def validate_chunk_32_repo_ci_dependency_quality_tool_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_32":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_32_repo_ci_dependency_quality_tool_cards":
        errors.append("manifest.active_chunk.id must be chunk_32_repo_ci_dependency_quality_tool_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_33_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_33_editor_scoped_next_slice for Chunk 32")

    readme = read(ROOT / "README.md")
    for term in ["chunk_32_repo_ci_dependency_quality_tool_cards", "bounded repository, CI, dependency, and quality-assurance tool-card expansion", "no AI IDE/tool cards", "no pricing expansion"]:
        if term not in readme:
            errors.append(f"README.md missing Chunk 32 scope term: {term}")
    readme_section = extract_markdown_section(readme, "Active Repository, CI, Dependency, and QA Tool Cards")
    for tid, rel in CHUNK_32_TOOL_CARDS.items():
        if f"`{tid}`" not in readme_section or f"`{rel}`" not in readme_section:
            errors.append(f"README.md active Chunk 32 tool section missing {tid} / {rel}")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    for tid in CHUNK_32_TOOL_CARDS:
        rows = [line for line in tool_register.splitlines() if line.startswith(f"| `{tid}` ")]
        if len(rows) != 1:
            errors.append(f"TOOL_REGISTER.md must contain exactly one row for Chunk 32 tool ID {tid}; observed={len(rows)}")
        elif "| active |" not in rows[0]:
            errors.append(f"TOOL_REGISTER.md Chunk 32 tool ID is not active: {tid}")
    if "## Chunk 32 Repository, CI, Dependency, and QA Tool Card Activation Note" not in tool_register:
        errors.append("TOOL_REGISTER.md missing Chunk 32 activation note")

    required_sources = [
        "github.docs.repositories", "github.docs.actions_workflow_syntax", "github.docs.dependabot_quickstart",
        "npm.docs.package_json", "npm.docs.scripts", "playwright.docs.intro", "playwright.docs.ci",
        "openssf.scorecard", "openssf.scorecard_checks", "openssf.scorecard_action",
    ]
    source_text = read(ROOT / "SOURCE_REGISTER.md")
    for sid in required_sources:
        if f"`{sid}`" not in source_text:
            errors.append(f"SOURCE_REGISTER.md missing source anchor required by Chunk 32: {sid}")
    if "Chunk 32 adds the editor-feedback gate source" not in source_text:
        errors.append("SOURCE_REGISTER.md missing Chunk 32 source note")

    active_ids = authored_active_ids()
    for tid, rel in CHUNK_32_TOOL_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 32 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid or fm.get("type") != "tool_card" or fm.get("status") != "active":
            errors.append(f"{rel} frontmatter must identify active tool card {tid}")
        if tid not in active_ids:
            errors.append(f"{tid} is not in authored active IDs")
        ss = fm.get("source_status", {}) if isinstance(fm.get("source_status"), dict) else {}
        if ss.get("official_vendor") is not True:
            errors.append(f"{rel} must mark source_status.official_vendor true")
        if ss.get("official_openai") is not False:
            errors.append(f"{rel} non-OpenAI infrastructure tool should not mark official_openai true")
        ids = evidence_ids(path)
        if not any(sid.startswith(("github.", "npm.", "playwright.", "openssf.")) for sid in ids):
            errors.append(f"{rel} must cite at least one official vendor/project source ID")
        forbidden = ["exact price", "exact plan", "credit value", "context-window", "current UI label"]
        body = read(path).lower()
        if any(term in body and "volatile" not in body for term in forbidden):
            errors.append(f"{rel} may contain stable exact pricing/limit/UI wording without volatile framing")

    for rel in ["llms.txt", "llms-full.txt"]:
        text = read(ROOT / rel)
        phrase = "Repository, CI, dependency, and quality-assurance tool cards from Chunk 32 are active."
        if text.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 32 tool-card phrase; observed={text.count(phrase)}")
        for heading in ["Repository, CI, Dependency, and QA Tool Card Fast Routing", "Active Chunk 32 Repository, CI, Dependency, and QA Tool Cards"]:
            sec = extract_markdown_section(text, heading)
            if not sec:
                errors.append(f"{rel} missing ## {heading} section for Chunk 32")
            for tid in CHUNK_32_TOOL_CARDS:
                if f"`{tid}`" not in sec:
                    errors.append(f"{rel} ## {heading} missing active Chunk 32 tool route {tid}")

    section_requirements = [
        ("indexes/INDEX_BY_TASK.md", "Choose dependencies, packages, or frameworks", ["tool.npm", "tool.github_dependabot", "tool.openssf_scorecard"], ["vcb.workflow.dependency_decisions", "vcb.chapter.dependency_package_framework_decisions"]),
        ("indexes/INDEX_BY_TASK.md", "Run CI or non-interactive Codex", ["tool.github_actions"], ["tool.codex_exec", "vcb.workflow.ci_noninteractive"]),
        ("indexes/INDEX_BY_TASK.md", "Write or update tests", ["tool.playwright", "tool.github_actions"], ["vcb.workflow.testing", "vcb.chapter.writing_updating_tests"]),
        ("indexes/INDEX_BY_TASK.md", "Migrate a dependency", ["tool.github_dependabot", "tool.npm", "tool.openssf_scorecard"], ["vcb.workflow.dependency_update_review"]),
        ("indexes/INDEX_BY_TASK.md", "Choose a tool stack", list(CHUNK_32_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog", "vcb.shortcut.tool_sprawl"]),
        ("indexes/INDEX_BY_TOOL_CATEGORY.md", "Review, security, and CI tools", ["tool.github", "tool.github_actions", "tool.github_dependabot", "tool.openssf_scorecard"], ["tool.codex_github_review", "vcb.workflow.ci_noninteractive"]),
        ("indexes/INDEX_FOR_AI_COACHES.md", "Human asks for CI, GitHub, dependency, or supply-chain tool choice", list(CHUNK_32_TOOL_CARDS), ["vcb."]),
        ("indexes/PROMPT_LIBRARY.md", "Repository/CI/dependency/QA tool-selection prompt", list(CHUNK_32_TOOL_CARDS), ["vcb."]),
    ]
    for rel, heading, required, fallbacks in section_requirements:
        sec = extract_markdown_section(read(ROOT / rel), heading)
        if not sec:
            errors.append(f"{rel} missing ## {heading} section")
            continue
        for tid in required:
            pos = sec.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"{rel} ## {heading} missing active Chunk 32 route {tid}")
                continue
            for fb in fallbacks:
                fb_pos = sec.find(f"`{fb}`") if fb.startswith("tool.") or fb.startswith("vcb.") else sec.find(fb)
                if fb_pos >= 0 and fb_pos < pos:
                    errors.append(f"{rel} ## {heading} routes fallback {fb} before active Chunk 32 route {tid}")

    for rel in ["indexes/INDEX_BY_PROJECT_TYPE.md", "indexes/INDEX_BY_RISK_LEVEL.md", "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_CODEX_SURFACE.md", "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/INDEX_BY_STABILITY.md", "indexes/GLOSSARY.md"]:
        text = read(ROOT / rel)
        for tid in CHUNK_32_TOOL_CARDS:
            if f"`{tid}`" not in text:
                errors.append(f"{rel} missing active Chunk 32 route {tid}")

    # Editor-required Chunk 32 revision checks: reject stale semantic routes that bypass active tool cards.
    tool_category_dev = extract_markdown_section(read(ROOT / "indexes/INDEX_BY_TOOL_CATEGORY.md"), "Development-stack and verification tools")
    for tid in ["tool.playwright", "tool.npm", "tool.github_dependabot", "tool.openssf_scorecard"]:
        if re.search(rf"`{re.escape(tid)}`\s*→\s*(registered|planned)", tool_category_dev):
            errors.append(f"INDEX_BY_TOOL_CATEGORY.md ## Development-stack and verification tools labels active Chunk 32 tool as registered/planned: {tid}")
        if not has_active_route(tool_category_dev, tid):
            errors.append(f"INDEX_BY_TOOL_CATEGORY.md ## Development-stack and verification tools missing active route for {tid}")

    # No active Chunk 32 infrastructure tool should remain marked registered/planned anywhere in the tool-category index.
    tool_category_text = read(ROOT / "indexes/INDEX_BY_TOOL_CATEGORY.md")
    for tid in CHUNK_32_TOOL_CARDS:
        if re.search(rf"`{re.escape(tid)}`\s*→\s*(registered|planned)", tool_category_text):
            errors.append(f"INDEX_BY_TOOL_CATEGORY.md labels active Chunk 32 tool as registered/planned somewhere in the index: {tid}")

    chunk32_revision_section_requirements = [
        ("indexes/INDEX_BY_FAILURE_MODE.md", "Codex adds unnecessary dependencies", ["tool.npm", "tool.github_dependabot", "tool.openssf_scorecard"], ["vcb.failure.dependency_bloat", "vcb.chapter.dependency_package_framework_decisions", "vcb.chapter.security_for_vibe_coders"]),
        ("indexes/INDEX_BY_FAILURE_MODE.md", "CI passes but does not prove the risk", ["tool.github_actions"], ["vcb.failure.ci_false_confidence", "vcb.workflow.ci_triage", "vcb.workflow.ci_noninteractive"]),
        ("indexes/INDEX_BY_FAILURE_MODE.md", "CI or automation mutates too much", ["tool.github_actions"], ["vcb.shortcut.automation_mutation_without_review", "vcb.shortcut.automation_spam", "vcb.chapter.ci_noninteractive_github_actions", "vcb.failure.ci_false_confidence"]),
        ("indexes/PROMPT_LIBRARY.md", "PR review prompt", ["tool.github"], ["vcb.chapter.github_pr_review_with_codex", "vcb.workflow.github_pr_review"]),
        ("indexes/PROMPT_LIBRARY.md", "Dependency migration prompt", ["tool.github_dependabot", "tool.npm", "tool.openssf_scorecard"], ["vcb.workflow.dependency_update_review", "vcb.workflow.dependency_decisions", "vcb.chapter.codex_playbooks", "vcb.chapter.dependency_package_framework_decisions"]),
        ("indexes/PROMPT_LIBRARY.md", "Frontend state-matrix prompt", ["tool.playwright"], ["vcb.workflow.frontend_work", "vcb.workflow.visual_qa", "vcb.workflow.accessibility_review", "vcb.chapter.frontend_work", "vcb.chapter.computer_use_browser_gui_tasks"]),
        ("indexes/INDEX_BY_CODEX_SURFACE.md", "GitHub review and PR surfaces", ["tool.github"], ["vcb.chapter.github_pr_review_with_codex", "vcb.codex.github_review"]),
        ("indexes/INDEX_BY_CODEX_SURFACE.md", "Non-interactive and CI surfaces", ["tool.github_actions"], ["vcb.chapter.ci_noninteractive_github_actions", "vcb.codex.github_action"]),
    ]
    for rel, heading, required, fallbacks in chunk32_revision_section_requirements:
        sec = extract_markdown_section(read(ROOT / rel), heading)
        if not sec:
            errors.append(f"{rel} missing ## {heading} section for Chunk 32 revision route checks")
            continue
        for tid in required:
            pos = sec.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"{rel} ## {heading} missing active Chunk 32 route {tid}")
                continue
            for fb in fallbacks:
                fb_pos = sec.find(f"`{fb}`")
                if fb_pos >= 0 and fb_pos < pos:
                    errors.append(f"{rel} ## {heading} routes fallback {fb} before active Chunk 32 route {tid}")

    llms_fast = extract_markdown_section(read(ROOT / "llms.txt"), "Fast Routing")
    stale_llms_lines = [
        "User asks to review Codex output, local diffs, or PRs → retrieve `vcb.workflow.codex_output_review`",
        "User asks about frontend behavior, screenshots, visual QA, or accessibility → retrieve `vcb.workflow.frontend_work`",
        "User asks about safe refactoring or dependency changes → retrieve `vcb.workflow.refactoring`",
    ]
    for stale in stale_llms_lines:
        if stale in llms_fast:
            errors.append(f"llms.txt ## Fast Routing still contains stale Chunk 32 route line: {stale}")
    llms_required_groups = [
        ("review/GitHub PR route", ["tool.github", "tool.github_actions", "tool.codex_github_review"]),
        ("frontend/browser evidence route", ["tool.playwright"]),
        ("dependency/package/supply-chain route", ["tool.npm", "tool.github_dependabot", "tool.openssf_scorecard"]),
    ]
    for label, required_ids in llms_required_groups:
        for tid in required_ids:
            if f"`{tid}`" not in llms_fast:
                errors.append(f"llms.txt ## Fast Routing missing {tid} in {label}")

    changelog = read(ROOT / "CHANGELOG.md")
    if len(re.findall(r"^## .*Chunk 32", changelog, flags=re.M)) != 1:
        errors.append("CHANGELOG.md must contain exactly one Chunk 32 heading")

    report = ROOT / "CHUNK_32_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_32_REPORT.md missing")
    else:
        report_text = read(report)
        if not report_text.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
            errors.append("CHUNK_32_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")
        for tid, rel in CHUNK_32_TOOL_CARDS.items():
            if f"`{tid}`" not in report_text or f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_32_REPORT.md missing created tool inventory for {tid} / {rel}")
        for rel in [
            "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md",
            "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", "indexes/INDEX_BY_TOOL_CATEGORY.md",
            "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_PROJECT_TYPE.md", "indexes/INDEX_BY_RISK_LEVEL.md",
            "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/PROMPT_LIBRARY.md", "indexes/INDEX_FOR_AI_COACHES.md",
            "indexes/INDEX_BY_CODEX_SURFACE.md", "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_FAILURE_MODE.md",
            "indexes/INDEX_BY_STABILITY.md", "indexes/GLOSSARY.md",
        ]:
            if f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_32_REPORT.md updated-file inventory omits {rel}")
        for claim in ["tool-card schema validation", "TOOL_REGISTER active status", "LLM source-map routing", "semantic index routing", "official vendor source posture", "scope guardrails"]:
            if claim not in report_text:
                errors.append(f"CHUNK_32_REPORT.md missing validator-backed claim: {claim}")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 32", "repository", "CI", "dependency", "QA", "tool-card", "official GitHub", "npm", "Playwright", "OpenSSF", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 32 term: {term}")



CHUNK_33_TOOL_CARDS = {
    "tool.chatgpt": "topics/tool-catalog/chatgpt.md",
    "tool.claude": "topics/tool-catalog/claude.md",
    "tool.cursor": "topics/tool-catalog/cursor.md",
    "tool.github_copilot": "topics/tool-catalog/github-copilot.md",
    "tool.windsurf": "topics/tool-catalog/windsurf.md",
}


def validate_chunk_33_ai_coding_ide_planning_tool_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_33":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_33_ai_coding_ide_planning_tool_cards":
        errors.append("manifest.active_chunk.id must be chunk_33_ai_coding_ide_planning_tool_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_34_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_34_editor_scoped_next_slice for Chunk 33")

    readme = read(ROOT / "README.md")
    for term in [
        "chunk_33_ai_coding_ide_planning_tool_cards",
        "bounded AI coding, AI IDE, and AI planning tool-card expansion",
        "no app-builder cards",
        "no pricing expansion",
    ]:
        if term not in readme:
            errors.append(f"README.md missing Chunk 33 scope term: {term}")
    readme_section = extract_markdown_section(readme, "Active AI Coding, AI IDE, and AI Planning Tool Cards")
    for tid, rel in CHUNK_33_TOOL_CARDS.items():
        if f"`{tid}`" not in readme_section or f"`{rel}`" not in readme_section:
            errors.append(f"README.md active Chunk 33 tool section missing {tid} / {rel}")

    manifest_map = manifest.get("ai_coding_ide_planning_tool_cards", {})
    if manifest_map != CHUNK_33_TOOL_CARDS:
        errors.append(
            "manifest.ai_coding_ide_planning_tool_cards does not match Chunk 33 required card map: "
            f"observed={manifest_map!r}"
        )
    if set(manifest.get("chunk_33_required_tool_ids", []) or []) != set(CHUNK_33_TOOL_CARDS):
        errors.append("manifest.chunk_33_required_tool_ids mismatch")
    if set(manifest.get("chunk_33_required_tool_files", []) or []) != set(CHUNK_33_TOOL_CARDS.values()):
        errors.append("manifest.chunk_33_required_tool_files mismatch")
    tool_cards = manifest.get("tool_cards", {})
    for tid, rel in CHUNK_33_TOOL_CARDS.items():
        if tool_cards.get(tid) != rel:
            errors.append(f"manifest.tool_cards missing active Chunk 33 mapping {tid} -> {rel}")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    for tid in CHUNK_33_TOOL_CARDS:
        rows = [line for line in tool_register.splitlines() if line.startswith(f"| `{tid}` ")]
        if len(rows) != 1:
            errors.append(f"TOOL_REGISTER.md must contain exactly one row for Chunk 33 tool ID {tid}; observed={len(rows)}")
        elif "| active |" not in rows[0]:
            errors.append(f"TOOL_REGISTER.md Chunk 33 tool ID is not active: {tid}")
    if "## Chunk 33 AI Coding, AI IDE, and AI Planning Tool Card Activation Note" not in tool_register:
        errors.append("TOOL_REGISTER.md missing Chunk 33 activation note")

    required_sources = [
        "openai.help.chatgpt_capabilities", "openai.help.chatgpt_projects", "openai.help.chatgpt_data_analysis",
        "anthropic.docs.claude_intro", "anthropic.docs.claude_code_overview", "anthropic.docs.prompt_engineering_overview", "anthropic.support.claude_projects",
        "cursor.docs.agent_overview", "cursor.docs.plan_mode", "cursor.docs.agent_review", "cursor.security",
        "github.docs.copilot_overview", "github.docs.copilot_code_suggestions", "github.docs.copilot_best_practices", "github.docs.copilot_cloud_agent",
        "windsurf.docs.getting_started", "windsurf.docs.cascade", "windsurf.docs.plugins", "windsurf.docs.admin_controls", "windsurf.docs.cascade_hooks",
    ]
    source_text = read(ROOT / "SOURCE_REGISTER.md")
    for sid in required_sources:
        if f"`{sid}`" not in source_text:
            errors.append(f"SOURCE_REGISTER.md missing source anchor required by Chunk 33: {sid}")
    if "Chunk 33 adds the editor-feedback gate source" not in source_text:
        errors.append("SOURCE_REGISTER.md missing Chunk 33 source note")

    active_ids = authored_active_ids()
    expected_sources = {
        "tool.chatgpt": ("openai.help.", True, False),
        "tool.claude": ("anthropic.", False, True),
        "tool.cursor": ("cursor.", False, True),
        "tool.github_copilot": ("github.docs.copilot", False, True),
        "tool.windsurf": ("windsurf.", False, True),
    }
    for tid, rel in CHUNK_33_TOOL_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 33 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid or fm.get("type") != "tool_card" or fm.get("status") != "active":
            errors.append(f"{rel} frontmatter must identify active tool card {tid}")
        if tid not in active_ids:
            errors.append(f"{tid} is not in authored active IDs")
        ss = fm.get("source_status", {}) if isinstance(fm.get("source_status"), dict) else {}
        prefix, openai_expected, vendor_expected = expected_sources[tid]
        if ss.get("official_openai") is not openai_expected:
            errors.append(f"{rel} source_status.official_openai mismatch for {tid}")
        if ss.get("official_vendor") is not vendor_expected:
            errors.append(f"{rel} source_status.official_vendor mismatch for {tid}")
        ids = evidence_ids(path)
        if not any(sid.startswith(prefix) for sid in ids):
            errors.append(f"{rel} must cite at least one official source ID with prefix {prefix!r}")
        body = read(path).lower()
        for forbidden in ["exact price", "exact plan", "quota limit", "context-window", "current ui label", "default permission"]:
            if forbidden in body and "volatile" not in body:
                errors.append(f"{rel} may contain stable exact pricing/limit/UI/permission wording without volatile framing")

    for rel in ["llms.txt", "llms-full.txt"]:
        text = read(ROOT / rel)
        phrase = "AI coding, AI IDE, and AI planning tool cards from Chunk 33 are active."
        if text.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 33 tool-card phrase; observed={text.count(phrase)}")
        for heading in ["AI Coding, AI IDE, and AI Planning Tool Card Fast Routing", "Active Chunk 33 AI Coding, AI IDE, and AI Planning Tool Cards"]:
            sec = extract_markdown_section(text, heading)
            if not sec:
                errors.append(f"{rel} missing ## {heading} section for Chunk 33")
            for tid in CHUNK_33_TOOL_CARDS:
                if f"`{tid}`" not in sec:
                    errors.append(f"{rel} ## {heading} missing active Chunk 33 tool route {tid}")

    section_requirements = [
        ("indexes/INDEX_BY_TOOL_CATEGORY.md", "AI coding and planning tools", list(CHUNK_33_TOOL_CARDS), ["tool.replit", "tool.lovable", "tool.bolt", "tool.v0"]),
        ("indexes/INDEX_BY_TASK.md", "Choose an AI coding, AI IDE, or planning tool", list(CHUNK_33_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog", "vcb.chapter.when_to_use_other_ais"]),
        ("indexes/INDEX_BY_TASK.md", "Use other AIs with Codex", list(CHUNK_33_TOOL_CARDS), ["vcb.shortcut.many_ais_same_files", "vcb.chapter.when_to_use_other_ais"]),
        ("indexes/INDEX_BY_TASK.md", "Choose a tool stack", list(CHUNK_33_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog", "vcb.shortcut.tool_sprawl"]),
        ("indexes/PROMPT_LIBRARY.md", "AI coding/IDE/planning tool-selection prompt", list(CHUNK_33_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog"]),
        ("indexes/PROMPT_LIBRARY.md", "Tool cost-benefit prompt", list(CHUNK_33_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog"]),
        ("indexes/PROMPT_LIBRARY.md", "Multi-AI/model-bias shortcut selector", list(CHUNK_33_TOOL_CARDS), ["vcb.shortcut.many_ais_same_files", "vcb.shortcut.consensus_as_correctness"]),
        ("indexes/INDEX_FOR_AI_COACHES.md", "Human asks which AI coding, AI IDE, or planning tool to use", list(CHUNK_33_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog"]),
        ("indexes/INDEX_FOR_AI_COACHES.md", "Human is buying tools instead of solving milestone risk", list(CHUNK_33_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog", "vcb.shortcut.tool_sprawl"]),
        ("indexes/INDEX_BY_CONCEPT.md", "Tool stack and multi-AI workflow", list(CHUNK_33_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog"]),
        ("indexes/INDEX_BY_CONCEPT.md", "AI coding and IDE tool concepts", list(CHUNK_33_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog"]),
    ]
    for rel, heading, required, fallbacks in section_requirements:
        sec = extract_markdown_section(read(ROOT / rel), heading)
        if not sec:
            errors.append(f"{rel} missing ## {heading} section")
            continue
        for tid in required:
            pos = sec.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"{rel} ## {heading} missing active Chunk 33 route {tid}")
                continue
            if re.search(rf"`{re.escape(tid)}`\s*→\s*(registered|planned)", sec):
                errors.append(f"{rel} ## {heading} labels active Chunk 33 route as registered/planned: {tid}")
            for fb in fallbacks:
                fb_pos = sec.find(f"`{fb}`")
                if fb_pos >= 0 and fb_pos < pos:
                    errors.append(f"{rel} ## {heading} routes fallback {fb} before active Chunk 33 route {tid}")

    for rel in [
        "indexes/GLOSSARY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md", "indexes/INDEX_BY_CODEX_SURFACE.md",
        "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/INDEX_BY_PROJECT_TYPE.md", "indexes/INDEX_BY_RECOVERABILITY.md",
        "indexes/INDEX_BY_RISK_LEVEL.md", "indexes/INDEX_BY_STABILITY.md",
    ]:
        text = read(ROOT / rel)
        for tid in CHUNK_33_TOOL_CARDS:
            if f"`{tid}`" not in text:
                errors.append(f"{rel} missing active Chunk 33 route {tid}")

    glossary_constraint = extract_markdown_section(read(ROOT / "indexes/GLOSSARY.md"), "Constraint and tool-stack terms")
    if "Independent AI review" not in glossary_constraint:
        errors.append("indexes/GLOSSARY.md Constraint and tool-stack terms missing Independent AI review route")
    else:
        line = next((ln for ln in glossary_constraint.splitlines() if "Independent AI review" in ln), "")
        chapter_pos = line.find("`vcb.chapter.when_to_use_other_ais`")
        claude_pos = line.find("`tool.claude`")
        chatgpt_pos = line.find("`tool.chatgpt`")
        if claude_pos < 0 and chatgpt_pos < 0:
            errors.append("indexes/GLOSSARY.md Independent AI review must route to tool.claude or tool.chatgpt before chapter fallback")
        for tid, pos in [("tool.claude", claude_pos), ("tool.chatgpt", chatgpt_pos)]:
            if pos >= 0 and chapter_pos >= 0 and chapter_pos < pos:
                errors.append(f"indexes/GLOSSARY.md Independent AI review routes chapter fallback before active {tid}")

    ai_tool_chaos = extract_markdown_section(read(ROOT / "indexes/INDEX_BY_FAILURE_MODE.md"), "Tool sprawl and AI-tool chaos")
    if not ai_tool_chaos:
        errors.append("indexes/INDEX_BY_FAILURE_MODE.md missing ## Tool sprawl and AI-tool chaos")
    else:
        first_fallback_positions = [
            ai_tool_chaos.find("`vcb.chapter.tool_stack_catalog`"),
            ai_tool_chaos.find("`vcb.chapter.cost_benefit_analysis`"),
            ai_tool_chaos.find("`vcb.chapter.when_to_use_other_ais`"),
            ai_tool_chaos.find("`vcb.shortcut.tool_sprawl`"),
            ai_tool_chaos.find("`vcb.shortcut.unofficial_tools`"),
            ai_tool_chaos.find("`vcb.shortcut.trusting_external_tool_output`"),
            ai_tool_chaos.find("`vcb.shortcut.hook_overreach`"),
        ]
        first_fallback = min((pos for pos in first_fallback_positions if pos >= 0), default=-1)
        for tid in CHUNK_33_TOOL_CARDS:
            pos = ai_tool_chaos.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"INDEX_BY_FAILURE_MODE.md Tool sprawl and AI-tool chaos missing active Chunk 33 route {tid}")
            elif first_fallback >= 0 and first_fallback < pos:
                errors.append(f"INDEX_BY_FAILURE_MODE.md Tool sprawl and AI-tool chaos routes fallback before active Chunk 33 route {tid}")

    for rel in ["topics/tool-catalog/replit.md", "topics/tool-catalog/lovable.md", "topics/tool-catalog/bolt.md", "topics/tool-catalog/v0.md"]:
        if (ROOT / rel).exists():
            errors.append(f"Chunk 33 must not create app-builder/browser-dev tool card outside scope: {rel}")
    if sorted(p.name for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep") != ["2026-06-09-openai-codex.md"]:
        errors.append("Chunk 33 must not expand pricing snapshots")

    report = ROOT / "CHUNK_33_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_33_REPORT.md missing")
    else:
        report_text = read(report)
        for rel in ["CHUNK_33_REPORT.md", *CHUNK_33_TOOL_CARDS.values()]:
            if f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_33_REPORT.md created-file inventory omits {rel}")
        for rel in [
            "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md",
            "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", "indexes/INDEX_BY_TOOL_CATEGORY.md",
            "indexes/INDEX_BY_TASK.md", "indexes/PROMPT_LIBRARY.md", "indexes/INDEX_FOR_AI_COACHES.md",
            "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_PROJECT_TYPE.md", "indexes/INDEX_BY_RISK_LEVEL.md",
            "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_CODEX_SURFACE.md", "indexes/INDEX_BY_FAILURE_MODE.md",
            "indexes/INDEX_BY_SHORTCUT.md", "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md", "indexes/GLOSSARY.md",
        ]:
            if f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_33_REPORT.md updated-file inventory omits {rel}")
        for md in ROOT.rglob("*.md"):
            if "__pycache__" in md.parts:
                continue
            rel = str(md.relative_to(ROOT))
            body = read(md)
            if "version: 0.34.0-draft.chunk33" in body or "status: chunk_33_updated" in body:
                if f"`{rel}`" not in report_text:
                    errors.append(f"CHUNK_33_REPORT.md inventory omits current-chunk version/status Markdown artifact {rel}")
        for claim in ["tool-card schema validation", "TOOL_REGISTER active status", "official OpenAI source posture", "official vendor source posture", "LLM source-map routing", "semantic index routing", "scope guardrails"]:
            if claim not in report_text:
                errors.append(f"CHUNK_33_REPORT.md missing validator-backed claim: {claim}")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 33", "AI coding", "AI IDE", "AI planning", "ChatGPT", "Claude", "Cursor", "GitHub Copilot", "Windsurf", "official vendor", "official OpenAI", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 33 term: {term}")




CHUNK_35_TOOL_CARDS = {
    "tool.vercel": "topics/tool-catalog/vercel.md",
    "tool.supabase": "topics/tool-catalog/supabase.md",
    "tool.clerk": "topics/tool-catalog/clerk.md",
    "tool.auth0": "topics/tool-catalog/auth0.md",
    "tool.stripe": "topics/tool-catalog/stripe.md",
    "tool.sentry": "topics/tool-catalog/sentry.md",
    "tool.posthog": "topics/tool-catalog/posthog.md",
}

CHUNK_35_SOURCE_IDS = {
    "vercel.docs.overview", "vercel.docs.deployments", "vercel.docs.observability", "vercel.docs.analytics",
    "supabase.docs.overview", "supabase.docs.database", "supabase.docs.auth", "supabase.docs.edge_functions", "supabase.docs.secrets",
    "clerk.docs.overview", "clerk.docs.user_management", "clerk.docs.session_tokens", "clerk.docs.organizations", "clerk.docs.restrictions",
    "auth0.docs.get_started", "auth0.docs.flows", "auth0.docs.universal_login", "auth0.docs.apis", "auth0.docs.organizations",
    "stripe.docs.billing_quickstart", "stripe.docs.webhooks", "stripe.docs.subscriptions", "stripe.docs.checkout",
    "sentry.docs.overview", "sentry.docs.product", "sentry.docs.performance", "sentry.docs.session_replay",
    "posthog.docs.overview", "posthog.docs.product_analytics", "posthog.docs.events", "posthog.docs.feature_flags", "posthog.docs.session_replay",
}

CHUNK_34_TOOL_CARDS = {
    "tool.replit": "topics/tool-catalog/replit.md",
    "tool.lovable": "topics/tool-catalog/lovable.md",
    "tool.bolt": "topics/tool-catalog/bolt.md",
    "tool.v0": "topics/tool-catalog/v0.md",
}

CHUNK_34_REQUIRED_SOURCE_IDS = {
    "vcb.register.editor_feedback_chunk_33",
    "replit.docs.build_welcome", "replit.docs.agent_overview", "replit.docs.first_app", "replit.docs.publish", "replit.docs.effective_prompting",
    "lovable.docs.welcome", "lovable.docs.getting_started", "lovable.docs.cloud", "lovable.docs.best_practice", "lovable.docs.integrations",
    "bolt.docs.intro", "bolt.docs.quickstart", "bolt.docs.plan_app", "bolt.docs.tokens", "bolt.docs.glossary",
    "v0.docs.what_is_v0", "v0.docs.design_systems", "v0.docs.figma", "v0.docs.platform_api",
}


def validate_chunk_34_browser_app_builder_ui_tool_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_34":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_34_browser_app_builder_ui_prototyping_tool_cards":
        errors.append("manifest.active_chunk.id must be chunk_34_browser_app_builder_ui_prototyping_tool_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_35_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_35_editor_scoped_next_slice for Chunk 34")

    readme = read(ROOT / "README.md")
    for term in [
        "chunk_34_browser_app_builder_ui_prototyping_tool_cards",
        "bounded browser-dev, app-builder, and UI-generation tool-card expansion",
        "no hosting/database/auth/payment/observability cards",
        "no pricing expansion",
    ]:
        if term not in readme:
            errors.append(f"README.md missing Chunk 34 scope term: {term}")
    readme_section = extract_markdown_section(readme, "Active Browser-Dev, App-Builder, and UI-Generation Tool Cards")
    for tid, rel in CHUNK_34_TOOL_CARDS.items():
        if f"`{tid}`" not in readme_section or f"`{rel}`" not in readme_section:
            errors.append(f"README.md active Chunk 34 tool section missing {tid} / {rel}")

    if manifest.get("browser_app_builder_ui_prototyping_tool_cards", {}) != CHUNK_34_TOOL_CARDS:
        errors.append("manifest.browser_app_builder_ui_prototyping_tool_cards mismatch")
    if set(manifest.get("chunk_34_required_tool_ids", []) or []) != set(CHUNK_34_TOOL_CARDS):
        errors.append("manifest.chunk_34_required_tool_ids mismatch")
    if set(manifest.get("chunk_34_required_tool_files", []) or []) != set(CHUNK_34_TOOL_CARDS.values()):
        errors.append("manifest.chunk_34_required_tool_files mismatch")
    for tid, rel in CHUNK_34_TOOL_CARDS.items():
        if manifest.get("tool_cards", {}).get(tid) != rel:
            errors.append(f"manifest.tool_cards missing active Chunk 34 mapping {tid} -> {rel}")

    source_text = read(ROOT / "SOURCE_REGISTER.md")
    for sid in CHUNK_34_REQUIRED_SOURCE_IDS:
        if f"`{sid}`" not in source_text:
            errors.append(f"SOURCE_REGISTER.md missing source anchor required by Chunk 34: {sid}")
    if "Chunk 34 adds the editor-feedback gate source" not in source_text:
        errors.append("SOURCE_REGISTER.md missing Chunk 34 source note")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    for tid in CHUNK_34_TOOL_CARDS:
        rows = [line for line in tool_register.splitlines() if line.startswith(f"| `{tid}` ")]
        if len(rows) != 1:
            errors.append(f"TOOL_REGISTER.md must contain exactly one row for Chunk 34 tool ID {tid}; observed={len(rows)}")
        elif "| active |" not in rows[0]:
            errors.append(f"TOOL_REGISTER.md Chunk 34 tool ID is not active: {tid}")
    if "## Chunk 34 Browser-Dev, App-Builder, and UI-Generation Tool Card Activation Note" not in tool_register:
        errors.append("TOOL_REGISTER.md missing Chunk 34 activation note")

    prefixes = {
        "tool.replit": "replit.",
        "tool.lovable": "lovable.",
        "tool.bolt": "bolt.",
        "tool.v0": "v0.",
    }
    active_ids = authored_active_ids()
    for tid, rel in CHUNK_34_TOOL_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 34 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid or fm.get("type") != "tool_card" or fm.get("status") != "active":
            errors.append(f"{rel} frontmatter must identify active tool card {tid}")
        if tid not in active_ids:
            errors.append(f"{tid} is not in authored active IDs")
        ss = fm.get("source_status", {}) if isinstance(fm.get("source_status"), dict) else {}
        if ss.get("official_openai") is not False or ss.get("official_vendor") is not True:
            errors.append(f"{rel} source_status must be official_vendor true and official_openai false")
        ids = evidence_ids(path)
        if not any(sid.startswith(prefixes[tid]) for sid in ids):
            errors.append(f"{rel} must cite at least one official source ID with prefix {prefixes[tid]!r}")
        body = read(path).lower()
        for forbidden in ["exact pricing", "plan limits", "quota limits", "context-window", "current ui labels", "default permissions"]:
            if forbidden in body and "volatile" not in body:
                errors.append(f"{rel} may contain stable pricing/limit/UI/permission wording without volatile framing")

    phrase = "Browser-dev, app-builder, and UI-generation tool cards from Chunk 34 are active."
    for rel in ["llms.txt", "llms-full.txt"]:
        text = read(ROOT / rel)
        if text.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 34 tool-card phrase; observed={text.count(phrase)}")
        for heading in ["Browser-Dev, App-Builder, and UI-Generation Tool Card Fast Routing", "Active Chunk 34 Browser-Dev, App-Builder, and UI-Generation Tool Cards"]:
            sec = extract_markdown_section(text, heading)
            if not sec:
                errors.append(f"{rel} missing ## {heading} section for Chunk 34")
                continue
            for tid in CHUNK_34_TOOL_CARDS:
                if f"`{tid}`" not in sec:
                    errors.append(f"{rel} ## {heading} missing active Chunk 34 tool route {tid}")

    requirements = [
        ("indexes/INDEX_BY_TOOL_CATEGORY.md", "AI coding and planning tools", list(CHUNK_34_TOOL_CARDS), []),
        ("indexes/INDEX_BY_TOOL_CATEGORY.md", "Browser-dev, app-builder, and UI-generation tools", list(CHUNK_34_TOOL_CARDS), []),
        ("indexes/INDEX_BY_TASK.md", "Build an MVP prototype", list(CHUNK_34_TOOL_CARDS), ["vcb.chapter.codex_playbooks", "vcb.chapter.first_serious_app"]),
        ("indexes/INDEX_BY_TASK.md", "Improve frontend UI", ["tool.v0", "tool.playwright"], ["vcb.chapter.frontend_work"]),
        ("indexes/INDEX_BY_TASK.md", "Choose a tool stack", list(CHUNK_34_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog", "vcb.shortcut.tool_sprawl"]),
        ("indexes/INDEX_BY_TASK.md", "Choose a browser-dev, app-builder, or UI-generation tool", list(CHUNK_34_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog"]),
        ("indexes/INDEX_BY_PROJECT_TYPE.md", "Throwaway prototype", list(CHUNK_34_TOOL_CARDS), ["vcb.chapter.first_serious_app"]),
        ("indexes/INDEX_BY_RISK_LEVEL.md", "Cost and tool risk", list(CHUNK_34_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog"]),
        ("indexes/INDEX_BY_RECOVERABILITY.md", "Browser-dev, app-builder, and UI-generation recoverability routes", list(CHUNK_34_TOOL_CARDS), ["vcb.concepts.recoverability"]),
        ("indexes/INDEX_BY_FAILURE_MODE.md", "UI works but has poor taste, states, or accessibility", ["tool.v0", "tool.playwright"], ["vcb.failure.ui_taste_gap"]),
        ("indexes/INDEX_BY_FAILURE_MODE.md", "Generated prototype becomes production foundation", list(CHUNK_34_TOOL_CARDS), ["vcb.chapter.first_serious_app"]),
        ("indexes/PROMPT_LIBRARY.md", "MVP prototype prompt", list(CHUNK_34_TOOL_CARDS), ["vcb.chapter.codex_playbooks"]),
        ("indexes/PROMPT_LIBRARY.md", "Browser-dev/app-builder/UI-generation tool-selection prompt", list(CHUNK_34_TOOL_CARDS), ["vcb.chapter.tool_stack_catalog"]),
        ("indexes/INDEX_FOR_AI_COACHES.md", "Human wants to prototype a UI or app quickly", list(CHUNK_34_TOOL_CARDS), ["vcb.constraints.build_vs_maintenance"]),
        ("indexes/INDEX_BY_CONCEPT.md", "AI app-builder and UI-generation concepts", list(CHUNK_34_TOOL_CARDS), ["vcb.concepts.frontend_backend"]),
        ("indexes/GLOSSARY.md", "Browser-dev, app-builder, and UI-generation tool terms", list(CHUNK_34_TOOL_CARDS), []),
        ("indexes/INDEX_BY_STABILITY.md", "Quarterly review — browser-dev, app-builder, and UI-generation tools", list(CHUNK_34_TOOL_CARDS), []),
    ]
    for rel, heading, required, fallbacks in requirements:
        sec = extract_markdown_section(read(ROOT / rel), heading)
        if not sec:
            errors.append(f"{rel} missing ## {heading} section")
            continue
        for tid in required:
            pos = sec.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"{rel} ## {heading} missing active Chunk 34 route {tid}")
                continue
            if re.search(rf"`{re.escape(tid)}`\s*→\s*(registered|planned)", sec):
                errors.append(f"{rel} ## {heading} labels active Chunk 34 route as registered/planned: {tid}")
            for fb in fallbacks:
                fb_pos = sec.find(f"`{fb}`")
                if fb_pos >= 0 and fb_pos < pos:
                    errors.append(f"{rel} ## {heading} routes fallback {fb} before active Chunk 34 route {tid}")

    # Chunk 34 revision semantic-route hardening for disposable prototype lookup paths.
    budget_profile = read(ROOT / "indexes" / "INDEX_BY_BUDGET_PROFILE.md")
    if "version: 0.35.0-draft.chunk34" not in budget_profile or "status: chunk_34_updated" not in budget_profile:
        errors.append("INDEX_BY_BUDGET_PROFILE.md must be version/status-bumped for Chunk 34 disposable-prototype routing edits")
    disposable_budget = extract_markdown_section(budget_profile, "Disposable prototype path")
    if not disposable_budget.strip():
        errors.append("INDEX_BY_BUDGET_PROFILE.md missing ## Disposable prototype path")
    else:
        require_ids_before_fallback(
            disposable_budget,
            "INDEX_BY_BUDGET_PROFILE.md ## Disposable prototype path",
            ["tool.replit", "tool.lovable", "tool.bolt", "tool.v0"],
            ["`vcb.chapter.", "`vcb.shortcut.one_big_prompt`", "`vcb.shortcut.generated_prototype_as_production_foundation`"],
            errors,
        )
        for companion in ["vcb.constraints.build_vs_maintenance", "vcb.shortcut.real_secrets_in_prototype"]:
            if f"`{companion}`" not in disposable_budget:
                errors.append(f"INDEX_BY_BUDGET_PROFILE.md ## Disposable prototype path missing active companion route {companion}")

    project_type = read(ROOT / "indexes" / "INDEX_BY_PROJECT_TYPE.md")
    constraint_section = extract_markdown_section(project_type, "Project type constraint routing")
    if not constraint_section.strip():
        errors.append("INDEX_BY_PROJECT_TYPE.md missing ## Project type constraint routing")
    else:
        throwaway_lines = [line for line in constraint_section.splitlines() if line.strip().startswith("- Throwaway prototype")]
        if not throwaway_lines:
            errors.append("INDEX_BY_PROJECT_TYPE.md ## Project type constraint routing missing Throwaway prototype route")
        else:
            throwaway = throwaway_lines[0]
            require_ids_before_fallback(
                throwaway,
                "INDEX_BY_PROJECT_TYPE.md ## Project type constraint routing Throwaway prototype",
                ["tool.replit", "tool.lovable", "tool.bolt", "tool.v0"],
                ["`vcb.chapter.", "`vcb.shortcut.generated_prototype_as_production_foundation`"],
                errors,
            )
            if "active first" not in throwaway:
                errors.append("INDEX_BY_PROJECT_TYPE.md Throwaway prototype route must label Chunk 34 tools as active first")
            if "`vcb.constraints.build_vs_maintenance`" not in throwaway:
                errors.append("INDEX_BY_PROJECT_TYPE.md Throwaway prototype route missing build_vs_maintenance companion")

    risk_level = read(ROOT / "indexes" / "INDEX_BY_RISK_LEVEL.md")
    low_risk = extract_markdown_section(risk_level, "Low-risk local or disposable work")
    if not low_risk.strip():
        errors.append("INDEX_BY_RISK_LEVEL.md missing ## Low-risk local or disposable work")
    else:
        require_ids_before_fallback(
            low_risk,
            "INDEX_BY_RISK_LEVEL.md ## Low-risk local or disposable work",
            ["tool.v0", "tool.replit", "tool.lovable", "tool.bolt"],
            ["`vcb.chapter.", "`vcb.shortcut.one_big_prompt`", "`vcb.shortcut.eyeballing_ui`"],
            errors,
        )

    # Stale planned labels for activated cards must not remain in indexes or LLM maps.
    for rel in ["llms.txt", "llms-full.txt", *[str(p.relative_to(ROOT)) for p in (ROOT / "indexes").glob("*.md")]]:
        text = read(ROOT / rel)
        for tid in CHUNK_34_TOOL_CARDS:
            if re.search(rf"`{re.escape(tid)}`\s*→\s*(registered|planned)", text):
                errors.append(f"{rel} still labels active Chunk 34 tool as registered/planned: {tid}")

    for rel in [
        "topics/tool-catalog/vercel.md", "topics/tool-catalog/supabase.md", "topics/tool-catalog/stripe.md", "topics/tool-catalog/clerk.md", "topics/tool-catalog/auth0.md", "topics/tool-catalog/sentry.md", "topics/tool-catalog/posthog.md", "topics/tool-catalog/docker.md", "topics/tool-catalog/figma.md", "topics/tool-catalog/linear.md",
    ]:
        if (ROOT / rel).exists():
            errors.append(f"Chunk 34 must not create non-scoped tool card outside scope: {rel}")
    if sorted(p.name for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep") != ["2026-06-09-openai-codex.md"]:
        errors.append("Chunk 34 must not expand pricing snapshots")

    report = ROOT / "CHUNK_34_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_34_REPORT.md missing")
    else:
        report_text = read(report)
        if not report_text.rstrip().splitlines()[-3].strip() == "AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW":
            # tolerate marker lines after report status but require status text in report
            if "AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW" not in report_text:
                errors.append("CHUNK_34_REPORT.md must include AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")
        for rel in ["CHUNK_34_REPORT.md", *CHUNK_34_TOOL_CARDS.values()]:
            if f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_34_REPORT.md created-file inventory omits {rel}")
        for rel in [
            "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md",
            "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", "indexes/GLOSSARY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md", "indexes/INDEX_BY_TOOL_CATEGORY.md",
            "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_PROJECT_TYPE.md", "indexes/INDEX_BY_RISK_LEVEL.md",
            "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/PROMPT_LIBRARY.md",
            "indexes/INDEX_FOR_AI_COACHES.md", "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_CODEX_SURFACE.md",
        ]:
            if f"`{rel}`" not in report_text:
                errors.append(f"CHUNK_34_REPORT.md updated-file inventory omits {rel}")
        for claim in ["tool-card schema validation", "TOOL_REGISTER", "official vendor source posture", "LLM source-map routing", "semantic index routing", "scope guardrails"]:
            if claim not in report_text:
                errors.append(f"CHUNK_34_REPORT.md missing validator-backed claim: {claim}")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 34", "browser-dev", "app-builder", "UI-generation", "Replit", "Lovable", "Bolt", "v0", "official vendor", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 34 term: {term}")


def validate_chunk_35_hosting_backend_auth_payment_observability_tool_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_35":
        return
    if manifest.get("active_chunk", {}).get("id") != "chunk_35_hosting_backend_auth_payment_observability_tool_cards":
        errors.append("manifest.active_chunk.id must be chunk_35_hosting_backend_auth_payment_observability_tool_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_36_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_36_editor_scoped_next_slice for Chunk 35")
    required = CHUNK_35_TOOL_CARDS
    readme = read(ROOT / "README.md")
    for term in ["chunk_35_hosting_backend_auth_payment_observability_tool_cards", "tool.vercel", "tool.supabase", "tool.clerk", "tool.auth0", "tool.stripe", "tool.sentry", "tool.posthog"]:
        if term not in readme:
            errors.append(f"README.md missing Chunk 35 term: {term}")
    active_section = extract_markdown_section(readme, "Active Hosting, Backend/Auth, Payment, Observability, and Product-Analytics Tool Cards")
    for tid, rel in required.items():
        if f"`{tid}`" not in active_section or f"`{rel}`" not in active_section:
            errors.append(f"README.md active Chunk 35 section missing {tid} / {rel}")
    if manifest.get("hosting_backend_auth_payment_observability_tool_cards") != required:
        errors.append("manifest.hosting_backend_auth_payment_observability_tool_cards mismatch")
    if set(manifest.get("chunk_35_required_tool_ids", []) or []) != set(required):
        errors.append("manifest.chunk_35_required_tool_ids mismatch")
    if set(manifest.get("chunk_35_required_tool_files", []) or []) != set(required.values()):
        errors.append("manifest.chunk_35_required_tool_files mismatch")
    for tid, rel in required.items():
        if manifest.get("tool_cards", {}).get(tid) != rel:
            errors.append(f"manifest.tool_cards missing Chunk 35 mapping {tid} -> {rel}")
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 35 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid or fm.get("type") != "tool_card" or fm.get("status") != "active":
            errors.append(f"frontmatter for {rel} must declare active tool_card ID {tid}")
        if not fm.get("source_status", {}).get("official_vendor"):
            errors.append(f"{rel} must declare source_status.official_vendor: true")
        body = read(path)
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in body:
                errors.append(f"{rel} missing required topic heading {heading}")
        if f"<!-- VCB:BEGIN_TOPIC id={tid}" not in body or f"<!-- VCB:END_TOPIC id={tid} -->" not in body:
            errors.append(f"{rel} missing matching VCB topic markers")
        if "pricing" not in body.lower() or "Volatile Surface" not in body:
            errors.append(f"{rel} missing pricing/volatile posture")
    source_text = read(ROOT / "SOURCE_REGISTER.md")
    for sid in CHUNK_35_SOURCE_IDS:
        if f"`{sid}`" not in source_text:
            errors.append(f"SOURCE_REGISTER.md missing Chunk 35 source ID {sid}")
    if "Chunk 35 adds the editor-feedback gate source" not in source_text:
        errors.append("SOURCE_REGISTER.md missing Chunk 35 source note")
    tool_register = read(ROOT / "TOOL_REGISTER.md")
    for tid in required:
        rows = [line for line in tool_register.splitlines() if f"`{tid}`" in line and line.startswith("|")]
        if len(rows) != 1:
            errors.append(f"TOOL_REGISTER.md must contain exactly one row for Chunk 35 tool ID {tid}; observed={len(rows)}")
        elif "| active |" not in rows[0]:
            errors.append(f"TOOL_REGISTER.md Chunk 35 tool ID is not active: {tid}")
    if "## Chunk 35 Hosting, Backend/Auth, Payment, Observability, and Product-Analytics Tool Card Activation Note" not in tool_register:
        errors.append("TOOL_REGISTER.md missing Chunk 35 activation note")
    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        phrase = "Hosting, backend/database/auth, payment, observability, and product-analytics tool cards from Chunk 35 are active."
        if body.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 35 phrase; observed={body.count(phrase)}")
        for heading in ["Hosting, Backend/Auth, Payment, Observability, and Product-Analytics Tool Card Fast Routing", "Active Chunk 35 Hosting, Backend/Auth, Payment, Observability, and Product-Analytics Tool Cards"]:
            sec = extract_markdown_section(body, heading)
            if not sec.strip():
                errors.append(f"{rel} missing ## {heading} section")
            for tid in required:
                if f"`{tid}`" not in sec:
                    errors.append(f"{rel} ## {heading} missing {tid}")
    semantic_sections = [
        ("indexes/INDEX_BY_TOOL_CATEGORY.md", "Hosting backend auth payments and observability", list(required), ["registered", "planned"]),
        ("indexes/INDEX_BY_TASK.md", "Build a first serious app", list(required), ["vcb.chapter.first_serious_app"]),
        ("indexes/INDEX_BY_TASK.md", "Investigate production errors", ["tool.sentry", "tool.posthog", "tool.vercel"], ["vcb.chapter.debugging_with_reproduction"]),
        ("indexes/INDEX_BY_TASK.md", "Add an API endpoint", ["tool.supabase", "tool.auth0", "tool.clerk", "tool.stripe"], ["vcb.chapter.codex_playbooks"]),
        ("indexes/INDEX_BY_TASK.md", "Harden auth-sensitive code", ["tool.clerk", "tool.auth0", "tool.supabase", "tool.stripe"], ["vcb.chapter.security_for_vibe_coders"]),
        ("indexes/INDEX_BY_PROJECT_TYPE.md", "Public app with users", list(required), ["vcb.chapter.security_for_vibe_coders"]),
        ("indexes/INDEX_BY_PROJECT_TYPE.md", "Auth/payment/data-sensitive system", ["tool.clerk", "tool.auth0", "tool.supabase", "tool.stripe"], ["vcb.chapter.security_for_vibe_coders"]),
        ("indexes/INDEX_BY_RISK_LEVEL.md", "High-risk production work", list(required), ["vcb.chapter.security_for_vibe_coders"]),
        ("indexes/INDEX_BY_RISK_LEVEL.md", "Never with real secrets or sensitive user data", ["tool.supabase", "tool.clerk", "tool.auth0", "tool.stripe", "tool.sentry", "tool.posthog"], ["vcb.chapter.security_for_vibe_coders"]),
        ("indexes/INDEX_BY_RECOVERABILITY.md", "Hard to recover", ["tool.stripe", "tool.supabase", "tool.clerk", "tool.auth0"], ["vcb.safety.production_red_lines"]),
        ("indexes/INDEX_BY_FAILURE_MODE.md", "Security-sensitive behavior is under-specified", ["tool.clerk", "tool.auth0", "tool.supabase", "tool.stripe"], ["vcb.chapter.security_for_vibe_coders"]),
        ("indexes/PROMPT_LIBRARY.md", "New project bootstrap prompt", list(required), ["vcb.chapter.codex_playbooks"]),
        ("indexes/PROMPT_LIBRARY.md", "Auth-sensitive hardening prompt", ["tool.clerk", "tool.auth0", "tool.supabase", "tool.stripe", "tool.sentry", "tool.posthog"], ["vcb.chapter.security_for_vibe_coders"]),
        ("indexes/INDEX_FOR_AI_COACHES.md", "Human asks for a giant app or first serious app", list(required), ["vcb.chapter.first_serious_app"]),
        ("indexes/INDEX_FOR_AI_COACHES.md", "Human asks which hosting, backend/auth, payment, observability, or analytics tool to use", list(required), ["vcb.chapter.tool_stack_catalog"]),
    ]
    for rel, heading, ids, fallbacks in semantic_sections:
        sec = extract_markdown_section(read(ROOT / rel), heading)
        if not sec.strip():
            errors.append(f"{rel} missing semantic section {heading}")
            continue
        for tid in ids:
            if f"`{tid}`" not in sec:
                errors.append(f"{rel} ## {heading} missing active Chunk 35 route {tid}")
        for tid in ids:
            pos = sec.find(f"`{tid}`")
            for fb in fallbacks:
                fb_pos = sec.find(f"`{fb}`")
                if pos >= 0 and fb_pos >= 0 and fb_pos < pos:
                    errors.append(f"{rel} ## {heading} routes fallback {fb} before active Chunk 35 route {tid}")
        if rel.endswith("INDEX_BY_TOOL_CATEGORY.md"):
            for tid in ids:
                line = next((line for line in sec.splitlines() if f"`{tid}`" in line), "")
                if "registered" in line or "planned" in line:
                    errors.append(f"{rel} ## {heading} labels active Chunk 35 route as registered/planned: {tid}")
    # Editor-reported Chunk 35 production-readiness route coverage.
    def require_chunk35_ids_before_fallbacks(rel: str, heading: str, ids: list[str], fallbacks: list[str]) -> None:
        sec = extract_markdown_section(read(ROOT / rel), heading)
        if not sec.strip():
            errors.append(f"{rel} missing Chunk 35 semantic section {heading}")
            return
        for tid in ids:
            pos = sec.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"{rel} ## {heading} missing required Chunk 35 production/platform route {tid}")
                continue
            for fb in fallbacks:
                fb_pos = sec.find(f"`{fb}`")
                if fb_pos >= 0 and fb_pos < pos:
                    errors.append(f"{rel} ## {heading} routes fallback {fb} before required Chunk 35 route {tid}")

    require_chunk35_ids_before_fallbacks(
        "indexes/INDEX_BY_BUDGET_PROFILE.md",
        "Production-quality path",
        list(required),
        [
            "vcb.chapter.git_discipline",
            "vcb.chapter.writing_updating_tests",
            "vcb.chapter.reviewing_codex_output",
            "vcb.chapter.security_for_vibe_coders",
            "vcb.chapter.senior_engineer_checklist",
            "vcb.constraints.production_quality",
        ],
    )
    require_chunk35_ids_before_fallbacks(
        "indexes/INDEX_BY_TASK.md",
        "Run the senior checklist",
        list(required),
        [
            "vcb.chapter.senior_engineer_checklist",
            "vcb.chapter.reviewing_codex_output",
            "vcb.chapter.git_discipline",
            "vcb.constraints.production_quality",
            "vcb.constraints.recovery_budget",
        ],
    )
    require_chunk35_ids_before_fallbacks(
        "indexes/PROMPT_LIBRARY.md",
        "Production-error investigation prompt",
        ["tool.sentry", "tool.posthog", "tool.vercel"],
        ["vcb.workflow.bug_repro", "vcb.chapter.codex_playbooks", "vcb.chapter.debugging_with_reproduction"],
    )
    api_sec = extract_markdown_section(read(ROOT / "indexes/PROMPT_LIBRARY.md"), "API endpoint prompt")
    if not api_sec.strip():
        errors.append("indexes/PROMPT_LIBRARY.md missing ## API endpoint prompt")
    else:
        supabase_pos = api_sec.find("`tool.supabase`")
        if supabase_pos < 0:
            errors.append("PROMPT_LIBRARY.md ## API endpoint prompt missing tool.supabase")
        if "`tool.auth0`" not in api_sec and "`tool.clerk`" not in api_sec:
            errors.append("PROMPT_LIBRARY.md ## API endpoint prompt must include tool.auth0 or tool.clerk")
        first_auth = min([pos for pos in [api_sec.find("`tool.auth0`"), api_sec.find("`tool.clerk`")] if pos >= 0] or [-1])
        for fb in ["vcb.chapter.codex_playbooks", "vcb.chapter.security_for_vibe_coders"]:
            fb_pos = api_sec.find(f"`{fb}`")
            if fb_pos >= 0 and supabase_pos >= 0 and fb_pos < supabase_pos:
                errors.append(f"PROMPT_LIBRARY.md ## API endpoint prompt routes fallback {fb} before tool.supabase")
            if fb_pos >= 0 and first_auth >= 0 and fb_pos < first_auth:
                errors.append(f"PROMPT_LIBRARY.md ## API endpoint prompt routes fallback {fb} before auth tool route")
    require_chunk35_ids_before_fallbacks(
        "indexes/PROMPT_LIBRARY.md",
        "Senior checklist prompt",
        list(required),
        ["vcb.chapter.senior_engineer_checklist", "vcb.constraints.production_quality", "vcb.constraints.recovery_budget"],
    )

    # Project-type line-specific constraint routing.
    ptype = extract_markdown_section(read(ROOT / "indexes/INDEX_BY_PROJECT_TYPE.md"), "Project type constraint routing")
    for label, ids in [("Public app with users", ["tool.vercel", "tool.supabase", "tool.sentry", "tool.posthog"]), ("Auth/payment/data-sensitive system", ["tool.clerk", "tool.auth0", "tool.supabase", "tool.stripe"] )]:
        line = next((line for line in ptype.splitlines() if label in line), "")
        for tid in ids:
            if f"`{tid}`" not in line:
                errors.append(f"INDEX_BY_PROJECT_TYPE.md Project type constraint routing line {label!r} missing {tid}")
    # Scope guardrails.
    allowed_new = set(CHUNK_27_TOOL_CARDS.values()) | set(CHUNK_28_TOOL_CARDS.values()) | set(CHUNK_29_TOOL_CARDS.values()) | set(CHUNK_30_TOOL_CARDS.values()) | set(CHUNK_31_TOOL_CARDS.values()) | set(CHUNK_32_TOOL_CARDS.values()) | set(CHUNK_33_TOOL_CARDS.values()) | set(CHUNK_34_TOOL_CARDS.values()) | set(required.values())
    tool_files = {str(p.relative_to(ROOT)) for p in (ROOT / "topics" / "tool-catalog").glob("*.md")}
    extra = sorted(tool_files - allowed_new)
    if extra:
        errors.append(f"Chunk 35 must not create non-scoped tool card outside known active sets: {extra}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md")]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 35 must not expand pricing snapshots: {pricing_files}")
    report = ROOT / "CHUNK_35_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_35_REPORT.md missing")
        return
    report_text = read(report)
    for rel in list(required.values()) + ["CHUNK_35_REPORT.md", "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md", "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", "indexes/GLOSSARY.md", "indexes/INDEX_BY_TOOL_CATEGORY.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_PROJECT_TYPE.md", "indexes/INDEX_BY_RISK_LEVEL.md", "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/PROMPT_LIBRARY.md", "indexes/INDEX_FOR_AI_COACHES.md", "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md"]:
        if f"`{rel}`" not in report_text:
            errors.append(f"CHUNK_35_REPORT.md inventory missing {rel}")
    if not report_text.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_35_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")


CHUNK_36_TOOL_CARDS = {
    "tool.docker": "topics/tool-catalog/docker.md",
    "tool.figma": "topics/tool-catalog/figma.md",
    "tool.linear": "topics/tool-catalog/linear.md",
}

CHUNK_36_SOURCE_IDS = {
    "vcb.register.editor_feedback_chunk_35",
    "docker.docs.overview", "docker.docs.compose", "docker.docs.dockerfile", "docker.docs.security", "docker.pricing",
    "figma.docs.design", "figma.help.prototyping", "figma.help.components", "figma.help.dev_mode", "figma.pricing",
    "linear.docs.concepts", "linear.docs.projects", "linear.docs.teams", "linear.docs.issue_status", "linear.docs.cycles", "linear.pricing",
}


def validate_chunk_36_local_dev_design_project_management_tool_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_36":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_36_local_dev_design_project_management_tool_cards":
        errors.append("manifest.active_chunk.id must be chunk_36_local_dev_design_project_management_tool_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_37_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_37_editor_scoped_next_slice for Chunk 36")

    required = CHUNK_36_TOOL_CARDS
    readme = read(ROOT / "README.md")
    for term in ["chunk_36_local_dev_design_project_management_tool_cards", "tool.docker", "tool.figma", "tool.linear", "no category placeholder cards", "no pricing expansion"]:
        if term not in readme:
            errors.append(f"README.md missing Chunk 36 term: {term}")
    active_section = extract_markdown_section(readme, "Active Local Dev, Design, and Project-Management Tool Cards")
    for tid, rel in required.items():
        if f"`{tid}`" not in active_section or f"`{rel}`" not in active_section:
            errors.append(f"README.md active Chunk 36 section missing {tid} / {rel}")

    if manifest.get("local_dev_design_project_management_tool_cards") != required:
        errors.append("manifest.local_dev_design_project_management_tool_cards mismatch")
    if set(manifest.get("chunk_36_required_tool_ids", []) or []) != set(required):
        errors.append("manifest.chunk_36_required_tool_ids mismatch")
    if set(manifest.get("chunk_36_required_tool_files", []) or []) != set(required.values()):
        errors.append("manifest.chunk_36_required_tool_files mismatch")
    for tid, rel in required.items():
        if manifest.get("tool_cards", {}).get(tid) != rel:
            errors.append(f"manifest.tool_cards missing Chunk 36 mapping {tid} -> {rel}")
        path = ROOT / rel
        if not path.exists():
            errors.append(f"missing Chunk 36 tool card file: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid or fm.get("type") != "tool_card" or fm.get("status") != "active":
            errors.append(f"frontmatter for {rel} must declare active tool_card ID {tid}")
        ss = fm.get("source_status", {}) if isinstance(fm.get("source_status"), dict) else {}
        if ss.get("official_vendor") is not True or ss.get("official_openai") is not False:
            errors.append(f"{rel} must declare official vendor/non-OpenAI source status")
        ids = evidence_ids(path)
        prefix = {"tool.docker": "docker.", "tool.figma": "figma.", "tool.linear": "linear."}[tid]
        if not any(sid.startswith(prefix) for sid in ids):
            errors.append(f"{rel} must cite at least one official {prefix.rstrip('.')} source ID")
        redirects = manifest.get("topic_namespace_policy", {}).get("topic_id_redirects", {})
        shortcut_profiles = fm.get("shortcut_profiles", []) if isinstance(fm.get("shortcut_profiles", []), list) else []
        for profile_id in shortcut_profiles:
            if profile_id in redirects:
                errors.append(
                    f"{rel} shortcut_profiles contains redirected alias {profile_id}; "
                    f"use canonical {redirects[profile_id]}"
                )
        body = read(path)
        for heading in REQUIRED_TOPIC_HEADINGS:
            if heading not in body:
                errors.append(f"{rel} missing required topic heading {heading}")
        if f"<!-- VCB:BEGIN_TOPIC id={tid}" not in body or f"<!-- VCB:END_TOPIC id={tid} -->" not in body:
            errors.append(f"{rel} missing matching VCB topic markers")
        for phrase in ["pricing", "Volatile Surface", "official vendor"]:
            if phrase not in body:
                errors.append(f"{rel} missing {phrase!r} source/volatile posture")

    source_text = read(ROOT / "SOURCE_REGISTER.md")
    for sid in CHUNK_36_SOURCE_IDS:
        if f"`{sid}`" not in source_text:
            errors.append(f"SOURCE_REGISTER.md missing Chunk 36 source ID {sid}")
    if "Chunk 36 adds the editor-feedback gate source" not in source_text:
        errors.append("SOURCE_REGISTER.md missing Chunk 36 source note")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    for tid in required:
        rows = [line for line in tool_register.splitlines() if line.startswith(f"| `{tid}` ")]
        if len(rows) != 1:
            errors.append(f"TOOL_REGISTER.md must contain exactly one row for Chunk 36 tool ID {tid}; observed={len(rows)}")
        elif "| active |" not in rows[0]:
            errors.append(f"TOOL_REGISTER.md Chunk 36 tool ID is not active: {tid}")
    if "## Chunk 36 Local Dev, Design, and Project-Management Tool Card Activation Note" not in tool_register:
        errors.append("TOOL_REGISTER.md missing Chunk 36 activation note")

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        phrase = "Docker/container, Figma/design, and Linear/project-management tool cards from Chunk 36 are active."
        if body.count(phrase) != 1:
            errors.append(f"{rel} must contain exactly one active Chunk 36 phrase; observed={body.count(phrase)}")
        for heading in ["Local Dev, Design, and Project-Management Tool Card Fast Routing", "Active Chunk 36 Local Dev, Design, and Project-Management Tool Cards"]:
            sec = extract_markdown_section(body, heading)
            if not sec.strip():
                errors.append(f"{rel} missing ## {heading} section")
            for tid in required:
                if f"`{tid}`" not in sec:
                    errors.append(f"{rel} ## {heading} missing {tid}")

    def require_ids_before(rel: str, heading: str, ids: list[str], fallbacks: list[str]) -> None:
        sec = extract_markdown_section(read(ROOT / rel), heading)
        if not sec.strip():
            errors.append(f"{rel} missing Chunk 36 semantic section {heading}")
            return
        for tid in ids:
            pos = sec.find(f"`{tid}`")
            if pos < 0:
                errors.append(f"{rel} ## {heading} missing active Chunk 36 route {tid}")
                continue
            if re.search(rf"`{re.escape(tid)}`\s*→\s*(registered|planned)", sec):
                errors.append(f"{rel} ## {heading} labels active Chunk 36 route as registered/planned: {tid}")
            for fb in fallbacks:
                fb_pos = sec.find(f"`{fb}`")
                if fb_pos >= 0 and fb_pos < pos:
                    errors.append(f"{rel} ## {heading} routes fallback {fb} before active Chunk 36 route {tid}")

    all_ids = list(required)
    require_ids_before("indexes/INDEX_BY_TOOL_CATEGORY.md", "Local dev design and project management", all_ids, ["registered", "planned"])
    require_ids_before("indexes/INDEX_BY_TASK.md", "Bootstrap a new project", all_ids, ["vcb.chapter.codex_playbooks", "vcb.chapter.first_serious_app"])
    require_ids_before("indexes/INDEX_BY_TASK.md", "Improve frontend UI", ["tool.figma"], ["vcb.workflow.frontend_work", "vcb.chapter.frontend_work"])
    require_ids_before("indexes/INDEX_BY_TASK.md", "Choose a tool stack", all_ids, ["vcb.chapter.tool_stack_catalog", "vcb.shortcut.tool_sprawl"])
    require_ids_before("indexes/INDEX_BY_TASK.md", "Run the senior checklist", all_ids, ["vcb.chapter.senior_engineer_checklist", "vcb.constraints.production_quality"])
    require_ids_before("indexes/INDEX_BY_TASK.md", "Build an MVP prototype", all_ids, ["vcb.chapter.first_serious_app", "vcb.chapter.codex_playbooks"])
    require_ids_before("indexes/INDEX_BY_TASK.md", "Choose a Docker, Figma, or Linear tool path", all_ids, ["vcb.chapter.tool_stack_catalog"])
    require_ids_before("indexes/INDEX_BY_TASK.md", "Turn prompts into team workflow", ["tool.linear"], ["vcb.chapter.prompt_library_to_team_workflow", "vcb.chapter.agents_md_operating_manual", "vcb.chapter.skills_reusable_workflows", "vcb.chapter.hooks_deterministic_guardrails"])
    require_ids_before("indexes/INDEX_BY_PROJECT_TYPE.md", "Personal local tool", ["tool.docker"], ["vcb.concepts.git_branch", "vcb.concepts.diff", "vcb.concepts.rollback", "vcb.chapter.git_discipline", "vcb.chapter.feature_slicing"])
    require_ids_before("indexes/INDEX_BY_PROJECT_TYPE.md", "Team or shared repo", all_ids, ["vcb.chapter.git_discipline"])
    ptype = extract_markdown_section(read(ROOT / "indexes/INDEX_BY_PROJECT_TYPE.md"), "Project type constraint routing")
    throwaway = next((line for line in ptype.splitlines() if "Throwaway prototype" in line), "")
    for tid in all_ids:
        if f"`{tid}`" not in throwaway:
            errors.append(f"INDEX_BY_PROJECT_TYPE.md Throwaway prototype constraint route missing {tid}")
    require_ids_before("indexes/INDEX_BY_PROJECT_TYPE.md", "Local dev, design, and project-management routes by project type", all_ids, ["vcb.chapter.tool_stack_catalog"])
    require_ids_before("indexes/INDEX_BY_RISK_LEVEL.md", "Low-risk local or disposable work", all_ids, ["vcb.chapter.codex_playbooks", "vcb.shortcut.one_big_prompt"])
    require_ids_before("indexes/INDEX_BY_RISK_LEVEL.md", "Cost and tool risk", all_ids, ["vcb.chapter.tool_stack_catalog", "vcb.shortcut.tool_sprawl"])
    require_ids_before("indexes/INDEX_BY_RISK_LEVEL.md", "Local dev, design, and project-management tool risk routes", all_ids, ["vcb.chapter.tool_stack_catalog"])
    require_ids_before("indexes/INDEX_BY_RECOVERABILITY.md", "Recoverability routes for tool-sprawl and process shortcuts", all_ids, ["vcb.shortcut.tool_sprawl"])
    require_ids_before("indexes/INDEX_BY_RECOVERABILITY.md", "Local dev, design, and project-management recoverability routes", all_ids, ["vcb.concepts.recoverability"])
    require_ids_before("indexes/INDEX_BY_FAILURE_MODE.md", "Tool sprawl and AI-tool chaos", all_ids, ["vcb.chapter.tool_stack_catalog", "vcb.shortcut.tool_sprawl"])
    require_ids_before("indexes/INDEX_BY_FAILURE_MODE.md", "UI works but has poor taste, states, or accessibility", ["tool.figma"], ["tool.v0", "tool.playwright", "vcb.failure.ui_taste_gap", "vcb.workflow.frontend_work", "vcb.workflow.visual_qa", "vcb.workflow.accessibility_review"])
    require_ids_before("indexes/INDEX_BY_FAILURE_MODE.md", "Team workflow creates ceremony without reducing risk", ["tool.linear"], ["vcb.chapter.prompt_library_to_team_workflow", "vcb.chapter.codex_playbooks", "vcb.shortcut.team_workflow_without_team"])
    require_ids_before("indexes/INDEX_BY_FAILURE_MODE.md", "Generated prototype becomes production foundation", ["tool.figma", "tool.docker", "tool.linear"], ["vcb.chapter.first_serious_app"])
    require_ids_before("indexes/INDEX_BY_FAILURE_MODE.md", "Local environment, design-handoff, and planning-tool failures", all_ids, ["vcb.chapter.tool_stack_catalog"])
    prompt_requirements = [
        ("New project bootstrap prompt", all_ids),
        ("Frontend state-matrix prompt", ["tool.figma"]),
        ("Team workflow promotion prompt", ["tool.linear"]),
        ("MVP prototype prompt", all_ids),
        ("Senior checklist prompt", all_ids),
        ("Tool cost-benefit prompt", all_ids),
        ("Local dev/design/project-management tool-selection prompt", all_ids),
    ]
    for heading, ids in prompt_requirements:
        require_ids_before("indexes/PROMPT_LIBRARY.md", heading, ids, ["vcb.chapter.tool_stack_catalog", "vcb.chapter.codex_playbooks", "vcb.chapter.senior_engineer_checklist"])
    require_ids_before("indexes/INDEX_FOR_AI_COACHES.md", "Human is buying tools instead of solving milestone risk", all_ids, ["vcb.chapter.tool_stack_catalog", "vcb.shortcut.tool_sprawl"])
    require_ids_before("indexes/INDEX_FOR_AI_COACHES.md", "Human wants to prototype a UI or app quickly", ["tool.figma", "tool.docker", "tool.linear"], ["vcb.constraints.build_vs_maintenance"])
    require_ids_before("indexes/INDEX_FOR_AI_COACHES.md", "Human asks which local-dev, design, or project-management tool to use", all_ids, ["vcb.chapter.tool_stack_catalog"])
    require_ids_before("indexes/INDEX_BY_BUDGET_PROFILE.md", "Disposable prototype path", all_ids, ["vcb.chapter.first_serious_app", "vcb.chapter.codex_playbooks"])
    require_ids_before("indexes/INDEX_BY_BUDGET_PROFILE.md", "Budget-aware local-dev, design, and project-management tool routes", all_ids, ["vcb.constraints.build_vs_maintenance"])
    require_ids_before("indexes/GLOSSARY.md", "Constraint and tool-stack terms", all_ids, ["vcb.chapter.tool_stack_catalog"])
    require_ids_before("indexes/INDEX_BY_CONCEPT.md", "Tool stack and multi-AI workflow", all_ids, ["vcb.chapter.tool_stack_catalog"])
    require_ids_before("indexes/INDEX_BY_STABILITY.md", "Stability routes for local-dev, design, and project-management tools", all_ids, [])

    # Scope guardrails: only the three Chunk 36 tool-card files may be newly outside known prior active sets.
    allowed_tool_files = set(CHUNK_27_TOOL_CARDS.values()) | set(CHUNK_28_TOOL_CARDS.values()) | set(CHUNK_29_TOOL_CARDS.values()) | set(CHUNK_30_TOOL_CARDS.values()) | set(CHUNK_31_TOOL_CARDS.values()) | set(CHUNK_32_TOOL_CARDS.values()) | set(CHUNK_33_TOOL_CARDS.values()) | set(CHUNK_34_TOOL_CARDS.values()) | set(CHUNK_35_TOOL_CARDS.values()) | set(required.values())
    tool_files = {str(p.relative_to(ROOT)) for p in (ROOT / "topics" / "tool-catalog").glob("*.md")}
    extra = sorted(tool_files - allowed_tool_files)
    if extra:
        errors.append(f"Chunk 36 must not create non-scoped tool card outside known active sets: {extra}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep"]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 36 must not expand pricing snapshots: {pricing_files}")

    report = ROOT / "CHUNK_36_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_36_REPORT.md missing")
        return
    report_text = read(report)
    for rel in ["CHUNK_36_REPORT.md", *required.values()]:
        if f"`{rel}`" not in report_text:
            errors.append(f"CHUNK_36_REPORT.md created-file inventory omits {rel}")
    for rel in [
        "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md", "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py",
        "indexes/GLOSSARY.md", "indexes/INDEX_BY_TOOL_CATEGORY.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_PROJECT_TYPE.md", "indexes/INDEX_BY_RISK_LEVEL.md",
        "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/PROMPT_LIBRARY.md", "indexes/INDEX_FOR_AI_COACHES.md",
        "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md",
    ]:
        if f"`{rel}`" not in report_text:
            errors.append(f"CHUNK_36_REPORT.md updated-file inventory omits {rel}")
    for claim in ["tool-card schema validation", "TOOL_REGISTER active status", "official vendor source posture", "LLM source-map routing", "semantic index routing", "scope guardrails", "report inventory"]:
        if claim not in report_text:
            errors.append(f"CHUNK_36_REPORT.md missing validator-backed claim: {claim}")
    if not report_text.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_36_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 36", "Docker", "Figma", "Linear", "local dev", "design", "project-management", "official vendor", "tool-card", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 36 term: {term}")


CHUNK_37_OLD_TOOL_INVENTORY_HEADINGS = [
    "Active Codex Security Tool Card",
    "Active First-Party OpenAI/Codex Tool Cards",
    "Active Adjunct OpenAI/Codex Tool Cards",
    "Active Customization and Control OpenAI/Codex Tool Cards",
    "Active Codex Governance and Maintenance Tool Cards",
    "Active AI Coding, AI IDE, and AI Planning Tool Cards",
    "Active Repository, CI, Dependency, and QA Tool Cards",
    "Active Hosting, Backend/Auth, Payment, Observability, and Product-Analytics Tool Cards",
    "Active Browser-Dev, App-Builder, and UI-Generation Tool Cards",
    "Active Local Dev, Design, and Project-Management Tool Cards",
]

CHUNK_37_REDIRECTED_SOURCE_URLS = [
    "https://docs.windsurf.com/windsurf/getting-started",
    "https://docs.windsurf.com/windsurf/cascade",
    "https://docs.windsurf.com/plugins/getting-started",
    "https://docs.windsurf.com/windsurf/guide-for-admins",
    "https://docs.windsurf.com/windsurf/cascade/hooks",
    "https://v0.dev/docs",
    "https://v0.dev/docs/design-systems",
    "https://v0.dev/docs/figma",
    "https://v0.dev/docs/api/platform",
]

CHUNK_37_CANONICAL_SOURCE_URLS = [
    "https://docs.devin.ai/desktop/getting-started",
    "https://docs.devin.ai/desktop/cascade/cascade",
    "https://docs.devin.ai/windsurf/plugins/getting-started",
    "https://docs.devin.ai/desktop/guide-for-admins",
    "https://docs.devin.ai/desktop/cascade/hooks",
    "https://v0.app/docs",
    "https://v0.app/docs/design-systems",
    "https://v0.app/docs/figma",
    "https://v0.app/docs/api/platform/overview",
]


def active_tool_ids_from_register() -> set[str]:
    tool_register = read(ROOT / "TOOL_REGISTER.md")
    ids: set[str] = set()
    for line in tool_register.splitlines():
        if line.startswith("| `tool.") and "| active |" in line:
            m = re.match(r"\| `(tool\.[^`]+)`", line)
            if m:
                ids.add(m.group(1))
    return ids


def section_has_ids(section: str, ids: list[str]) -> bool:
    return all(f"`{ident}`" in section for ident in ids)


def validate_chunk_37_tool_catalog_routing_cleanup(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_37":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_37_tool_catalog_routing_consolidation_cleanup":
        errors.append("manifest.active_chunk.id must be chunk_37_tool_catalog_routing_consolidation_cleanup")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_38_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_38_editor_scoped_next_slice for Chunk 37")

    expected_tool_files = (
        set(CHUNK_27_TOOL_CARDS.values())
        | set(CHUNK_28_TOOL_CARDS.values())
        | set(CHUNK_29_TOOL_CARDS.values())
        | set(CHUNK_30_TOOL_CARDS.values())
        | set(CHUNK_31_TOOL_CARDS.values())
        | set(CHUNK_32_TOOL_CARDS.values())
        | set(CHUNK_33_TOOL_CARDS.values())
        | set(CHUNK_34_TOOL_CARDS.values())
        | set(CHUNK_35_TOOL_CARDS.values())
        | set(CHUNK_36_TOOL_CARDS.values())
    )
    actual_tool_files = {str(p.relative_to(ROOT)) for p in (ROOT / "topics" / "tool-catalog").glob("*.md") if p.name != ".gitkeep"}
    if actual_tool_files != expected_tool_files:
        errors.append(f"Chunk 37 cleanup must not add/remove tool cards: actual={sorted(actual_tool_files)} expected={sorted(expected_tool_files)}")
    pricing_files = [p.name for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep"]
    if pricing_files != ["2026-06-09-openai-codex.md"]:
        errors.append(f"Chunk 37 cleanup must not expand pricing snapshots: {pricing_files}")

    readme = read(ROOT / "README.md")
    for term in [
        "chunk_37_tool_catalog_routing_consolidation_cleanup",
        "bounded repository-contract cleanup only",
        "no new tool cards",
        "chunk_38_editor_scoped_next_slice",
    ]:
        if term not in readme:
            errors.append(f"README.md missing Chunk 37 governance term: {term}")
    readme_tool_section = extract_markdown_section(readme, "Active Tool Cards")
    if not readme_tool_section.strip():
        errors.append("README.md missing consolidated ## Active Tool Cards section")
    active_tool_ids = active_tool_ids_from_register()
    for tid in sorted(active_tool_ids):
        if f"`{tid}`" not in readme_tool_section:
            errors.append(f"README.md consolidated tool-card inventory missing active tool ID {tid}")
        rel = manifest.get("tool_cards", {}).get(tid)
        if rel and f"`{rel}`" not in readme_tool_section:
            errors.append(f"README.md consolidated tool-card inventory missing path for {tid}: {rel}")
    for heading in CHUNK_37_OLD_TOOL_INVENTORY_HEADINGS:
        if f"## {heading}" in readme:
            errors.append(f"README.md still contains generation-specific tool inventory heading ## {heading}")

    for index_path in (ROOT / "indexes").glob("*.md"):
        body = read(index_path)
        for heading in CHUNK_37_OLD_TOOL_INVENTORY_HEADINGS:
            if f"## {heading}" in body:
                errors.append(f"{index_path.relative_to(ROOT)} still contains generation-specific aggregate tool inventory heading ## {heading}")
    tool_category = read(ROOT / "indexes" / "INDEX_BY_TOOL_CATEGORY.md")
    policy = extract_markdown_section(tool_category, "Tool-Card Inventory Policy")
    for term in ["TOOL_REGISTER.md", "README.md", "semantic category routes", "generation-specific aggregate inventory blocks"]:
        if term not in policy:
            errors.append(f"INDEX_BY_TOOL_CATEGORY.md Tool-Card Inventory Policy missing term: {term}")

    glossary = read(ROOT / "indexes" / "GLOSSARY.md")
    review_terms = extract_markdown_section(glossary, "Review, security, and shipping terms")
    required_glossary_routes = {
        "Codex PR review": ["tool.codex_github_review", "tool.github"],
        "non-interactive Codex": ["tool.codex_exec", "tool.github_actions"],
        "CI": ["tool.github_actions", "tool.codex_exec"],
    }
    for label, ids in required_glossary_routes.items():
        line = next((line for line in review_terms.splitlines() if label in line), "")
        for tid in ids:
            if f"`{tid}`" not in line:
                errors.append(f"GLOSSARY.md Review/security term {label!r} missing active companion {tid}")

    security_review_rows = []
    for line in review_terms.splitlines():
        stripped = line.strip()
        if not stripped.startswith("-"):
            continue
        m = re.match(r"^-\s*`?([^`→—-]+?)`?\s*(?:→|—|-)", stripped)
        if m and m.group(1).strip().lower() == "security review":
            security_review_rows.append(stripped)
    if len(security_review_rows) != 1:
        errors.append(
            "GLOSSARY.md ## Review, security, and shipping terms must contain exactly one normalized security review entry; "
            f"observed={len(security_review_rows)}"
        )
    else:
        security_line = security_review_rows[0]
        for tid in ["vcb.safety.security_review", "tool.codex_security", "vcb.chapter.security_for_vibe_coders"]:
            if f"`{tid}`" not in security_line:
                errors.append(f"GLOSSARY.md merged security review route missing {tid}")
        if security_line.find("`vcb.chapter.security_for_vibe_coders`") < security_line.find("`vcb.safety.security_review`"):
            errors.append("GLOSSARY.md merged security review route must place vcb.safety.security_review before chapter fallback")
        if security_line.find("`vcb.chapter.security_for_vibe_coders`") < security_line.find("`tool.codex_security`"):
            errors.append("GLOSSARY.md merged security review route must place tool.codex_security before chapter fallback")

    prompting_concepts = extract_markdown_section(read(ROOT / "indexes" / "INDEX_BY_CONCEPT.md"), "Prompting and work-order concepts")
    acceptance_rows = [
        line.strip()
        for line in prompting_concepts.splitlines()
        if line.strip().startswith("- `vcb.prompting.acceptance_criteria`")
    ]
    if len(acceptance_rows) != 1:
        errors.append(
            "INDEX_BY_CONCEPT.md ## Prompting and work-order concepts must contain exactly one "
            f"vcb.prompting.acceptance_criteria route row; observed={len(acceptance_rows)}"
        )
    elif "evidence-backed done-when criteria" not in acceptance_rows[0]:
        errors.append("INDEX_BY_CONCEPT.md acceptance criteria route must keep descriptive evidence-backed wording")

    concept_terms = extract_markdown_section(glossary, "Foundational concept terms")
    concept_requirements = {
        "Authentication": ["tool.clerk", "tool.auth0", "tool.supabase"],
        "Authorization": ["tool.auth0", "tool.clerk", "tool.supabase"],
        "CI": ["tool.github_actions", "tool.codex_exec", "tool.github"],
        "Observability": ["tool.sentry", "tool.posthog", "tool.vercel"],
    }
    for label, ids in concept_requirements.items():
        line = next((line for line in concept_terms.splitlines() if label in line), "")
        for tid in ids:
            if f"`{tid}`" not in line:
                errors.append(f"GLOSSARY.md Foundational concept term {label!r} missing companion {tid}")

    team_section = extract_markdown_section(read(ROOT / "indexes" / "INDEX_BY_PROJECT_TYPE.md"), "Team or shared repo")
    for tid in ["tool.github", "tool.github_actions"]:
        count = team_section.count(f"`{tid}`")
        if count != 1:
            errors.append(f"INDEX_BY_PROJECT_TYPE.md ## Team or shared repo must contain exactly one {tid} route; observed={count}")

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        if "Tool-catalog routing consolidation and source-map hygiene cleanup from Chunk 37 is active." not in body:
            errors.append(f"{rel} missing Chunk 37 active-content phrase")
        cleanup = extract_markdown_section(body, "Tool-Catalog Cleanup Fast Routing")
        for term in ["canonical active tool-card inventory", "Codex execution surface", "prototype phase", "production readiness", "canonical official destination"]:
            if term not in cleanup:
                errors.append(f"{rel} Tool-Catalog Cleanup Fast Routing missing term: {term}")
        if "User asks which Codex tool/surface to use" in body:
            errors.append(f"{rel} still uses ambiguous 'which Codex tool/surface' route; use execution-surface language")
        if "Need to judge production readiness → retrieve `vcb.constraints.production_quality`." in body:
            errors.append(f"{rel} production readiness route still omits active platform tool-card companions")
        if "Need to adapt behavior for prototype, MVP, production build, maintenance, refactor, or hotfix phase → retrieve `vcb.constraints.build_vs_maintenance`." in body:
            errors.append(f"{rel} prototype/phase route still omits app-builder tool-card companions")

    source_register = read(ROOT / "SOURCE_REGISTER.md")
    for old in CHUNK_37_REDIRECTED_SOURCE_URLS:
        if old in source_register:
            errors.append(f"SOURCE_REGISTER.md still contains redirected URL that should be canonicalized: {old}")
    for url in CHUNK_37_CANONICAL_SOURCE_URLS:
        if url not in source_register:
            errors.append(f"SOURCE_REGISTER.md missing canonical URL: {url}")
    if "vcb.register.editor_feedback_chunk_36" not in source_register:
        errors.append("SOURCE_REGISTER.md missing Chunk 37 editor-feedback source row")
    if "canonicalizes official redirecting Windsurf/Devin and v0 source URLs" not in source_register:
        errors.append("SOURCE_REGISTER.md missing Chunk 37 source hygiene note")

    report = ROOT / "CHUNK_37_REPORT.md"
    if not report.exists():
        errors.append("CHUNK_37_REPORT.md missing")
        return
    report_text = read(report)
    for rel in [
        "CHUNK_37_REPORT.md", "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md", "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py",
        "indexes/GLOSSARY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md", "indexes/INDEX_BY_CODEX_SURFACE.md", "indexes/INDEX_BY_CONCEPT.md", "indexes/INDEX_BY_FAILURE_MODE.md", "indexes/INDEX_BY_PROJECT_TYPE.md", "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_RISK_LEVEL.md", "indexes/INDEX_BY_SHORTCUT.md", "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_TOOL_CATEGORY.md", "indexes/INDEX_FOR_AI_COACHES.md", "indexes/PROMPT_LIBRARY.md",
    ]:
        if f"`{rel}`" not in report_text:
            errors.append(f"CHUNK_37_REPORT.md inventory missing {rel}")
    for claim in ["no new tool-card", "README consolidated", "indexes contain no generation-specific", "duplicate semantic route", "glossary companion routes", "LLM source-map", "SOURCE_REGISTER.md rejects old redirected"]:
        if claim not in report_text:
            errors.append(f"CHUNK_37_REPORT.md missing validator-backed claim: {claim}")
    if not report_text.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_37_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 37", "README", "consolidated", "tool-card inventory", "duplicate", "source-register canonical URLs", "scope"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 37 term: {term}")



CHUNK_38_FIELD_PRACTICE_CARDS = {
    "vcb.field.chatgpt_pm_codex_implementer": "topics/field-practices/chatgpt-pm-codex-implementer.md",
    "vcb.field.fresh_agent_review": "topics/field-practices/fresh-agent-review.md",
    "vcb.field.context_reset_between_tasks": "topics/field-practices/context-reset-between-tasks.md",
    "vcb.field.agents_md_first": "topics/field-practices/agents-md-first.md",
    "vcb.field.skeleton_todo_first": "topics/field-practices/skeleton-todo-first.md",
    "vcb.field.strict_typecheck_lint_gates": "topics/field-practices/strict-typecheck-lint-gates.md",
    "vcb.field.greenfield_vs_production_rule": "topics/field-practices/greenfield-vs-production-rule.md",
    "vcb.field.lessons_file_loop": "topics/field-practices/lessons-file-loop.md",
    "vcb.field.multi_agent_review_consensus": "topics/field-practices/multi-agent-review-consensus.md",
}

CHUNK_38_REQUIRED_UPDATED_FILES = {
    "README.md",
    "manifest.json",
    "llms.txt",
    "llms-full.txt",
    "FIELD_PRACTICES.md",
    "SOURCE_REGISTER.md",
    "CHANGELOG.md",
    "TREE.txt",
    "scripts/validate_repository.py",
    "indexes/GLOSSARY.md",
    "indexes/INDEX_BY_BUDGET_PROFILE.md",
    "indexes/INDEX_BY_CODEX_SURFACE.md",
    "indexes/INDEX_BY_CONCEPT.md",
    "indexes/INDEX_BY_FAILURE_MODE.md",
    "indexes/INDEX_BY_PROJECT_TYPE.md",
    "indexes/INDEX_BY_RECOVERABILITY.md",
    "indexes/INDEX_BY_RISK_LEVEL.md",
    "indexes/INDEX_BY_SHORTCUT.md",
    "indexes/INDEX_BY_STABILITY.md",
    "indexes/INDEX_BY_TASK.md",
    "indexes/INDEX_BY_TOOL_CATEGORY.md",
    "indexes/INDEX_FOR_AI_COACHES.md",
    "indexes/PROMPT_LIBRARY.md",
}


def _section_line(section: str, needle: str) -> str:
    return next((line for line in section.splitlines() if needle in line), "")


def _require_ids_before_fallback(
    errors: list[str],
    rel_path: str,
    heading: str,
    ids: list[str],
    fallback_ids: list[str],
    context: str,
) -> None:
    body = read(ROOT / rel_path)
    section = extract_markdown_section(body, heading)
    if not section.strip():
        errors.append(f"{rel_path} missing ## {heading} section for {context}")
        return
    for ident in ids:
        if f"`{ident}`" not in section:
            errors.append(f"{rel_path} ## {heading} missing {ident} for {context}")
    positions = [section.find(f"`{ident}`") for ident in ids if f"`{ident}`" in section]
    if positions:
        first_active = min(positions)
        for fallback in fallback_ids:
            pos = section.find(f"`{fallback}`")
            if pos != -1 and pos < first_active:
                errors.append(f"{rel_path} ## {heading} places fallback {fallback} before active field-practice route for {context}")


def _require_all_ids_before_any_fallback(
    errors: list[str],
    rel_path: str,
    heading: str,
    ids: list[str],
    fallback_ids: list[str],
    context: str,
) -> None:
    body = read(ROOT / rel_path)
    section = extract_markdown_section(body, heading)
    if not section.strip():
        errors.append(f"{rel_path} missing ## {heading} section for {context}")
        return
    for ident in ids:
        token = f"`{ident}`"
        pos = section.find(token)
        if pos == -1:
            errors.append(f"{rel_path} ## {heading} missing {ident} for {context}")
            continue
        for fallback in fallback_ids:
            fb_pos = section.find(f"`{fallback}`")
            if fb_pos != -1 and fb_pos < pos:
                errors.append(f"{rel_path} ## {heading} places fallback {fallback} before required active route {ident} for {context}")


def validate_chunk_38_field_practice_candidate_cards(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_38":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_38_field_practice_candidate_cards":
        errors.append("manifest.active_chunk.id must be chunk_38_field_practice_candidate_cards")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_39_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_39_editor_scoped_next_slice for Chunk 38")

    current_scope = " ".join(map(str, manifest.get("active_chunk", {}).get("scope", [])))
    for term in ["bounded field-practice candidate card expansion", "existing candidate IDs", "No field practice was promoted"]:
        if term not in current_scope and term not in read(ROOT / "README.md"):
            errors.append(f"Chunk 38 scope/governance missing term: {term}")

    for ident, rel in CHUNK_38_FIELD_PRACTICE_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"Chunk 38 field-practice card missing: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != ident:
            errors.append(f"{rel} frontmatter id mismatch: {fm.get('id')!r} != {ident!r}")
        if fm.get("type") != "field_practice":
            errors.append(f"{rel} type must be field_practice")
        if fm.get("status") != "active":
            errors.append(f"{rel} status must be active")
        if fm.get("field_practice_status") != "candidate":
            errors.append(f"{rel} field_practice_status must remain candidate")
        if str(fm.get("officially_endorsed")) != "false":
            errors.append(f"{rel} officially_endorsed must remain string false")
        if fm.get("evidence_level") not in {"E4_COMMUNITY_FIELD_REPORT", "E5_SPECULATIVE"}:
            errors.append(f"{rel} evidence_level must be conservative candidate evidence, observed {fm.get('evidence_level')!r}")
        source_status = fm.get("source_status", {}) or {}
        if source_status.get("community_field_practice") is not True:
            errors.append(f"{rel} source_status.community_field_practice must be true")
        if "E2_REPRODUCED_LOCALLY" in read(path):
            errors.append(f"{rel} must not claim local reproduction in Chunk 38 candidate slice")
        required_terms = [
            "candidate field practice",
            "not official guidance",
            "official best practice",
            "has not been promoted",
        ]
        lower = read(path).lower()
        for term in required_terms:
            if term not in lower:
                errors.append(f"{rel} missing conservative candidate language: {term}")

    field_register = read(ROOT / "FIELD_PRACTICES.md")
    active_section = extract_markdown_section(field_register, "Active Candidate Field Practice Cards")
    if not active_section.strip():
        errors.append("FIELD_PRACTICES.md missing ## Active Candidate Field Practice Cards section")
    for ident, rel in CHUNK_38_FIELD_PRACTICE_CARDS.items():
        if f"`{ident}`" not in field_register:
            errors.append(f"FIELD_PRACTICES.md missing field-practice ID {ident}")
        if f"`{ident}`" not in active_section or f"`{rel}`" not in active_section:
            errors.append(f"FIELD_PRACTICES.md active candidate section missing {ident} / {rel}")
    table_header = []
    status_idx = None
    for line in field_register.splitlines():
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if "Field practice ID" in cells and "Current register status" in cells:
            table_header = cells
            status_idx = cells.index("Current register status")
            continue
        if "vcb.field." not in line:
            continue
        for ident in CHUNK_38_FIELD_PRACTICE_CARDS:
            if f"`{ident}`" in line:
                if status_idx is None or status_idx >= len(cells):
                    errors.append(f"FIELD_PRACTICES.md row for {ident} cannot be checked for Current register status")
                elif cells[status_idx] != "candidate":
                    errors.append(f"FIELD_PRACTICES.md row for {ident} must remain candidate, observed {cells[status_idx]!r}")

    # Chunk 38 revision: field-practice evidence in the candidate routing table must
    # state the current practice evidence first and must not use shorthand, slash-combined,
    # or prematurely promoted evidence labels. Official docs may support product mechanics
    # or surrounding principles, but not the candidate ritual itself.
    candidate_table = extract_markdown_section(field_register, "Candidate Field Practice Routing Table")
    header = None
    evidence_rows: dict[str, str] = {}
    for line in candidate_table.splitlines():
        s = line.strip()
        if not s.startswith("|") or set(s.replace("|", "").strip()) <= {"-", ":"}:
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if header is None:
            header = cells
            continue
        if not header or len(cells) != len(header):
            continue
        if "Field practice ID" not in header or "Evidence starting status" not in header:
            continue
        field_id = cells[header.index("Field practice ID")].strip().strip("`")
        if field_id not in CHUNK_38_FIELD_PRACTICE_CARDS:
            continue
        evidence = cells[header.index("Evidence starting status")]
        evidence_rows[field_id] = evidence
        if not evidence.startswith("E4_COMMUNITY_FIELD_REPORT"):
            errors.append(f"FIELD_PRACTICES.md row for {field_id} must begin with current E4_COMMUNITY_FIELD_REPORT evidence, observed {evidence!r}")
        if re.search(r"\bE[0-5](?:_[A-Z_]+)?\s*/\s*E[0-5](?:_[A-Z_]+)?", evidence):
            errors.append(f"FIELD_PRACTICES.md row for {field_id} uses slash-combined evidence labels: {evidence!r}")
        if re.search(r"\bE[0-5]\b", evidence):
            errors.append(f"FIELD_PRACTICES.md row for {field_id} uses bare evidence shorthand instead of canonical labels: {evidence!r}")
        if ("E2_REPRODUCED_LOCALLY" in evidence or "E3_EXPERT_REPORT" in evidence) and not ("may become" in evidence and "only after" in evidence):
            errors.append(f"FIELD_PRACTICES.md row for {field_id} implies E2/E3 evidence without future-promotion-only wording: {evidence!r}")
        if "E0_OFFICIAL_DOCS" in evidence and not ("supports" in evidence and "only" in evidence):
            errors.append(f"FIELD_PRACTICES.md row for {field_id} must label official docs as mechanics/principle support only: {evidence!r}")
    for ident in CHUNK_38_FIELD_PRACTICE_CARDS:
        if ident not in evidence_rows:
            errors.append(f"FIELD_PRACTICES.md candidate routing table missing evidence row for {ident}")

    readme = read(ROOT / "README.md")
    for term in [
        "chunk_38_field_practice_candidate_cards",
        "bounded field-practice candidate card expansion only",
        "No field practice was promoted beyond candidate status",
        "chunk_39_editor_scoped_next_slice",
    ]:
        if term not in readme:
            errors.append(f"README.md missing Chunk 38 governance term: {term}")
    readme_section = extract_markdown_section(readme, "Active Field Practice Candidate Cards")
    if not readme_section.strip():
        errors.append("README.md missing ## Active Field Practice Candidate Cards section")
    for ident, rel in CHUNK_38_FIELD_PRACTICE_CARDS.items():
        if f"`{ident}`" not in readme_section or f"`{rel}`" not in readme_section:
            errors.append(f"README.md active field-practice inventory missing {ident} / {rel}")

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        for term in ["Field-practice candidate cards from Chunk 38 are active", "Field Practice Candidate Fast Routing", "Active Chunk 38 Field Practice Candidate Cards"]:
            if term not in body:
                errors.append(f"{rel} missing Chunk 38 LLM routing term: {term}")
        for ident, card_path in CHUNK_38_FIELD_PRACTICE_CARDS.items():
            if f"`{ident}`" not in body or f"`{card_path}`" not in body:
                errors.append(f"{rel} missing active Chunk 38 field-practice route for {ident}")

    all_ids = list(CHUNK_38_FIELD_PRACTICE_CARDS)
    _require_ids_before_fallback(
        errors,
        "indexes/INDEX_BY_TASK.md",
        "Evaluate or adopt an unofficial Codex practice",
        all_ids,
        ["vcb.chapter.field_notes_unofficial_practices"],
        "field-practice adoption/evaluation",
    )
    _require_ids_before_fallback(
        errors,
        "indexes/INDEX_BY_STABILITY.md",
        "Review monthly: field practice and volatile advice",
        all_ids,
        ["vcb.chapter.field_notes_unofficial_practices"],
        "field-practice review cadence",
    )
    _require_ids_before_fallback(
        errors,
        "indexes/INDEX_FOR_AI_COACHES.md",
        "Human cites an unofficial Codex tactic",
        all_ids,
        ["vcb.chapter.field_notes_unofficial_practices"],
        "AI-coach field-practice triage",
    )
    _require_ids_before_fallback(
        errors,
        "indexes/INDEX_BY_FAILURE_MODE.md",
        "Community tactic treated as official guidance",
        all_ids,
        ["vcb.chapter.field_notes_unofficial_practices"],
        "community tactic overpromotion",
    )
    prompt_section = extract_markdown_section(read(ROOT / "indexes" / "PROMPT_LIBRARY.md"), "Field-practice assessment prompt")
    for ident in all_ids:
        if f"`{ident}`" not in prompt_section:
            errors.append(f"PROMPT_LIBRARY.md field-practice assessment prompt missing {ident}")
    if "test/narrow/promote locally/retire" not in prompt_section and "promote locally" not in prompt_section:
        errors.append("PROMPT_LIBRARY.md field-practice assessment prompt must preserve local promotion/retirement decision language")
    glossary_section = extract_markdown_section(read(ROOT / "indexes" / "GLOSSARY.md"), "Field practice candidate terms")
    for ident in all_ids:
        if f"`{ident}`" not in glossary_section:
            errors.append(f"GLOSSARY.md Field practice candidate terms missing {ident}")

    source_register = read(ROOT / "SOURCE_REGISTER.md")
    for term in ["vcb.register.editor_feedback_chunk_37", "candidate/community-reported", "No new external source IDs are required"]:
        if term not in source_register:
            errors.append(f"SOURCE_REGISTER.md missing Chunk 38 source/register note: {term}")

    report_path = ROOT / "CHUNK_38_REPORT.md"
    if not report_path.exists():
        errors.append("CHUNK_38_REPORT.md missing")
        return
    report = read(report_path)
    created = report_section_backtick_paths(report, "Files created")
    updated = report_section_backtick_paths(report, "Files updated")
    required_created = set(CHUNK_38_FIELD_PRACTICE_CARDS.values()) | {"CHUNK_38_REPORT.md"}
    missing_created = sorted(required_created - created)
    missing_updated = sorted(CHUNK_38_REQUIRED_UPDATED_FILES - updated)
    if missing_created:
        errors.append(f"CHUNK_38_REPORT.md Files created omits required files: {missing_created}")
    if missing_updated:
        errors.append(f"CHUNK_38_REPORT.md Files updated omits required files: {missing_updated}")
    for term in [
        "No field practice was promoted beyond candidate status",
        "candidate/anecdotal/reproduced/promoted/deprecated taxonomy preserved",
        "validator coverage tightened",
        "No new tool cards",
        "No pricing snapshots",
    ]:
        if term not in report:
            errors.append(f"CHUNK_38_REPORT.md missing required claim: {term}")
    if not report.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_38_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 38", "field-practice", "candidate", "FIELD_PRACTICES", "evidence", "LLM", "semantic route"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 38 term: {term}")



CHUNK_39_REQUIRED_UPDATED_FILES = {
    "README.md",
    "manifest.json",
    "llms.txt",
    "llms-full.txt",
    "FIELD_PRACTICES.md",
    "chapters/36-field-notes-unofficial-practices.md",
    "CHANGELOG.md",
    "TREE.txt",
    "scripts/validate_repository.py",
}

CHUNK_39_ACTIVE_TOOL_LIST_HEADING_RE = re.compile(
    r"^## Active Chunk (?:27|28|29|30|31|32|33|34|35|36) .*Tool Card",
    flags=re.M,
)


def _no_bare_or_slash_evidence_labels(text: str, label: str, errors: list[str]) -> None:
    if re.search(r"\bE[0-5]\b", text):
        errors.append(f"{label} contains bare evidence shorthand; use canonical labels such as E4_COMMUNITY_FIELD_REPORT")
    if re.search(r"\bE[0-5](?:_[A-Z_]+)?\s*/\s*E[0-5](?:_[A-Z_]+)?", text):
        errors.append(f"{label} contains slash-combined evidence labels")


def validate_chunk_39_field_practice_llm_cleanup(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_39":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_39_field_practice_evidence_and_llm_map_cleanup":
        errors.append("manifest.active_chunk.id must be chunk_39_field_practice_evidence_and_llm_map_cleanup")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_40_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_40_editor_scoped_next_slice for Chunk 39")

    expected_package = manifest.get("package", {}).get("canonical_review_package")
    source_artifacts = manifest.get("source_artifacts", {}) if isinstance(manifest.get("source_artifacts"), dict) else {}
    for alias_key in ("package_file", "review_package"):
        alias_value = source_artifacts.get(alias_key)
        if alias_value != expected_package:
            errors.append(
                f"manifest.source_artifacts.{alias_key} must match manifest.package.canonical_review_package: "
                f"{alias_value!r} != {expected_package!r}"
            )
        if isinstance(alias_value, str) and "chunk-39" not in alias_value:
            errors.append(f"manifest.source_artifacts.{alias_key} does not point to a Chunk 39 package: {alias_value!r}")

    scope_boundary = str(manifest.get("validation_expectations", {}).get("current_chunk_scope_boundaries", ""))
    if "Chunk 39" not in scope_boundary:
        errors.append("manifest.validation_expectations.current_chunk_scope_boundaries must mention Chunk 39")
    for term in [
        "No new field-practice cards",
        "tool cards",
        "shortcut cards",
        "pricing snapshots",
        "narrative chapters",
        "field-practice promotion/reproduction/retirement",
    ]:
        if term not in scope_boundary:
            errors.append(f"manifest.validation_expectations.current_chunk_scope_boundaries missing term: {term}")
    if "Chunk 38" in scope_boundary:
        errors.append("manifest.validation_expectations.current_chunk_scope_boundaries still names Chunk 38")

    scope_text = " ".join(map(str, manifest.get("active_chunk", {}).get("scope", [])))
    for term in ["field-practice evidence-label hygiene", "LLM source-map consolidation", "no new field-practice cards", "no new tool cards"]:
        if term not in scope_text and term not in read(ROOT / "README.md"):
            errors.append(f"Chunk 39 scope/governance missing term: {term}")

    field_register = read(ROOT / "FIELD_PRACTICES.md")
    for section_name in ["Status Labels", "Promotion Rules"]:
        section = extract_markdown_section(field_register, section_name)
        if not section.strip():
            errors.append(f"FIELD_PRACTICES.md missing ## {section_name} section")
        _no_bare_or_slash_evidence_labels(section, f"FIELD_PRACTICES.md ## {section_name}", errors)
    for canonical in ["E4_COMMUNITY_FIELD_REPORT", "E2_REPRODUCED_LOCALLY", "E3_EXPERT_REPORT"]:
        if canonical not in field_register:
            errors.append(f"FIELD_PRACTICES.md missing canonical evidence label {canonical}")
    status_section = extract_markdown_section(field_register, "Status Labels")
    if "treat as E4_COMMUNITY_FIELD_REPORT" not in status_section:
        errors.append("FIELD_PRACTICES.md status-label prose must normalize anecdotal evidence to E4_COMMUNITY_FIELD_REPORT")

    chapter = read(ROOT / "chapters/36-field-notes-unofficial-practices.md")
    chapter_fm = parse_frontmatter(ROOT / "chapters/36-field-notes-unofficial-practices.md") or {}
    evidence_scope = str(chapter_fm.get("evidence_scope", ""))
    for canonical in ["E4_COMMUNITY_FIELD_REPORT", "E2_REPRODUCED_LOCALLY", "E3_EXPERT_REPORT"]:
        if canonical not in evidence_scope:
            errors.append(f"Chapter 36 evidence_scope missing canonical label {canonical}")
    if re.search(r"remain E4/E2/E3|E4 community field report", chapter, flags=re.I):
        errors.append("Chapter 36 still contains shorthand field-practice evidence wording")
    coaching_section = extract_markdown_section(chapter, "2. For the AI Coach: How to Teach This to Your Human")
    if "E4_COMMUNITY_FIELD_REPORT" not in coaching_section or "E0_OFFICIAL_DOCS" not in coaching_section:
        errors.append("Chapter 36 AI-coach section must use canonical evidence labels and distinguish official docs mechanics from ritual promotion")

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        if body.count("Field-practice evidence-label and LLM source-map cleanup from Chunk 39 is active.") != 1:
            errors.append(f"{rel} must contain exactly one Chunk 39 current-active phrase")
        stale_headings = CHUNK_39_ACTIVE_TOOL_LIST_HEADING_RE.findall(body)
        if stale_headings:
            errors.append(f"{rel} still contains generation-specific active tool-card list headings: {stale_headings}")
        if "Consolidated Tool-Card Inventory Policy" not in body:
            errors.append(f"{rel} missing consolidated tool-card inventory policy")
        if "generation-specific LLM-map or index inventory blocks" not in body:
            errors.append(f"{rel} must warn against generation-specific tool inventory blocks")
        if "preserve candidate status and E4_COMMUNITY_FIELD_REPORT posture" not in body:
            errors.append(f"{rel} field-practice route must preserve candidate/E4 evidence posture")
        if "tool choice" not in body or "smallest active tool card" not in body:
            errors.append(f"{rel} must clarify active tool-card selection for generic tool choice")
        proto_line = _section_line(extract_markdown_section(body, "Tool-Catalog Cleanup Fast Routing"), "prototype")
        for tid in ["tool.replit", "tool.lovable", "tool.bolt", "tool.v0"]:
            if f"`{tid}`" not in proto_line:
                errors.append(f"{rel} prototype/app-builder route missing {tid}")
        prod_line = _section_line(extract_markdown_section(body, "Tool-Catalog Cleanup Fast Routing"), "production readiness")
        for tid in ["tool.vercel", "tool.supabase", "tool.clerk", "tool.auth0", "tool.stripe", "tool.sentry", "tool.posthog"]:
            if f"`{tid}`" not in prod_line:
                errors.append(f"{rel} production-readiness route missing {tid}")
        if "vcb.constraints.build_vs_maintenance" not in proto_line:
            errors.append(f"{rel} prototype route must keep phase concept companion vcb.constraints.build_vs_maintenance")
        if "vcb.constraints.production_quality" not in prod_line:
            errors.append(f"{rel} production readiness route must keep production-quality concept companion")

    # Chunk 38 candidates stay candidates and remain the only active field-practice cards.
    field_cards = sorted(str(p.relative_to(ROOT)) for p in (ROOT / "topics" / "field-practices").glob("*.md"))
    expected_field_cards = sorted(CHUNK_38_FIELD_PRACTICE_CARDS.values())
    if field_cards != expected_field_cards:
        errors.append(f"Chunk 39 must not add/remove field-practice cards: observed={field_cards} expected={expected_field_cards}")
    for rel in expected_field_cards:
        fm = parse_frontmatter(ROOT / rel) or {}
        if fm.get("field_practice_status") != "candidate":
            errors.append(f"{rel} must remain candidate during Chunk 39 cleanup")

    report_path = ROOT / "CHUNK_39_REPORT.md"
    if not report_path.exists():
        errors.append("CHUNK_39_REPORT.md missing")
        return
    report = read(report_path)
    created = report_section_backtick_paths(report, "Files created")
    updated = report_section_backtick_paths(report, "Files updated")
    if "CHUNK_39_REPORT.md" not in created:
        errors.append("CHUNK_39_REPORT.md Files created must list CHUNK_39_REPORT.md")
    missing_updated = sorted(CHUNK_39_REQUIRED_UPDATED_FILES - updated)
    if missing_updated:
        errors.append(f"CHUNK_39_REPORT.md Files updated omits required files: {missing_updated}")
    for term in [
        "FIELD_PRACTICES.md evidence shorthand normalized",
        "Chapter 36 evidence_scope normalized",
        "LLM generation-specific active tool-card lists consolidated",
        "No new field-practice cards",
        "No new tool cards",
        "stale nested manifest package references repaired",
        "current_chunk_scope_boundaries",
        "validator coverage tightened",
    ]:
        if term not in report:
            errors.append(f"CHUNK_39_REPORT.md missing required claim: {term}")
    if not report.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_39_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 39", "field-practice evidence", "LLM source-map", "generation-specific active tool-card", "canonical evidence labels", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 39 term: {term}")



CHUNK_40_TOOL_CARDS = {
    "tool.cloudflare": "topics/tool-catalog/cloudflare.md",
    "tool.netlify": "topics/tool-catalog/netlify.md",
    "tool.neon": "topics/tool-catalog/neon.md",
    "tool.resend": "topics/tool-catalog/resend.md",
    "tool.vitest": "topics/tool-catalog/vitest.md",
    "tool.storybook": "topics/tool-catalog/storybook.md",
}

CHUNK_40_SOURCE_IDS = {
    "vcb.register.editor_feedback_chunk_39",
    "cloudflare.docs.developer_overview",
    "cloudflare.docs.workers",
    "cloudflare.docs.pages",
    "cloudflare.docs.dns",
    "netlify.docs.overview",
    "netlify.docs.deploy_overview",
    "netlify.docs.functions_overview",
    "netlify.docs.environment_variables",
    "neon.docs.introduction",
    "neon.docs.connect",
    "neon.docs.branching",
    "resend.docs.introduction",
    "resend.docs.send_email",
    "resend.docs.templates",
    "vitest.docs.guide",
    "vitest.docs.browser_component_testing",
    "vitest.docs.api_test",
    "storybook.docs.overview",
    "storybook.docs.get_started",
    "storybook.docs.writing_tests",
    "storybook.docs.test_runner",
}

CHUNK_40_DEFERRED_TOOL_IDS = [
    "tool.render", "tool.railway", "tool.fly_io", "tool.firebase", "tool.aws", "tool.gcp", "tool.azure", "tool.digitalocean",
    "tool.postmark", "tool.sendgrid", "tool.mailgun", "tool.notion", "tool.google_docs", "tool.jira",
    "tool.onepassword", "tool.doppler", "tool.infisical", "tool.better_stack", "tool.datadog",
    "tool.paddle", "tool.lemon_squeezy", "tool.jest", "tool.cypress",
]

CHUNK_40_REQUIRED_UPDATED_FILES = {
    "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "TOOL_REGISTER.md",
    "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py", "indexes/GLOSSARY.md",
    "indexes/INDEX_BY_TOOL_CATEGORY.md", "indexes/INDEX_BY_TASK.md", "indexes/INDEX_BY_PROJECT_TYPE.md",
    "indexes/INDEX_BY_RISK_LEVEL.md", "indexes/INDEX_BY_RECOVERABILITY.md", "indexes/INDEX_BY_FAILURE_MODE.md",
    "indexes/PROMPT_LIBRARY.md", "indexes/INDEX_FOR_AI_COACHES.md", "indexes/INDEX_BY_CONCEPT.md",
    "indexes/INDEX_BY_STABILITY.md", "indexes/INDEX_BY_BUDGET_PROFILE.md",
}

def _tool_register_row_for(tool_register: str, tid: str) -> str:
    return next((line for line in tool_register.splitlines() if line.strip().startswith(f"| `{tid}` |")), "")

def validate_chunk_40_tool_catalog_coverage_gap_audit(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_40":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_40_tool_catalog_coverage_gap_audit":
        errors.append("manifest.active_chunk.id must be chunk_40_tool_catalog_coverage_gap_audit")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_41_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_41_editor_scoped_next_slice for Chunk 40")

    readme = read(ROOT / "README.md")
    readme_current = extract_markdown_section(readme, "Current Chunk")
    for term in ["chunk_40_tool_catalog_coverage_gap_audit", "bounded tool-catalog coverage-gap audit", "no broad shortcut-card expansion", "no pricing expansion"]:
        if term not in readme_current and term not in readme:
            errors.append(f"README.md missing Chunk 40 scope/governance term: {term}")
    if "## Deferred Ecosystem Coverage" not in readme:
        errors.append("README.md missing Deferred Ecosystem Coverage section")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    if "## Chunk 40 Tool-Catalog Coverage-Gap Audit Note" not in tool_register:
        errors.append("TOOL_REGISTER.md missing Chunk 40 coverage-gap audit note")
    for tid, rel in CHUNK_40_TOOL_CARDS.items():
        path = ROOT / rel
        if not path.exists():
            errors.append(f"Chunk 40 active tool card missing: {rel}")
            continue
        fm = parse_frontmatter(path) or {}
        if fm.get("id") != tid:
            errors.append(f"{rel} frontmatter id mismatch: {fm.get('id')!r} != {tid!r}")
        if fm.get("type") != "tool_card" or fm.get("status") != "active":
            errors.append(f"{rel} must be an active tool_card")
        if fm.get("source_status", {}).get("official_vendor") is not True:
            errors.append(f"{rel} must mark source_status.official_vendor true")
        if fm.get("evidence_level") != "E0_OFFICIAL_DOCS":
            errors.append(f"{rel} must use E0_OFFICIAL_DOCS evidence level")
        if fm.get("pricing_snapshot_required") is not False:
            errors.append(f"{rel} should not require pricing snapshot unless exact prices/limits are hardcoded")
        for sid in evidence_ids(path):
            if sid not in source_register_ids():
                errors.append(f"{rel} evidence source ID missing from SOURCE_REGISTER: {sid}")
        row = _tool_register_row_for(tool_register, tid)
        if not row:
            errors.append(f"TOOL_REGISTER.md missing Chunk 40 active row for {tid}")
        elif "| active |" not in row:
            errors.append(f"TOOL_REGISTER.md Chunk 40 row for {tid} is not active: {row}")
        if f"`{tid}`" not in readme:
            errors.append(f"README.md Active Tool Cards inventory missing {tid}")

    for tid in CHUNK_40_DEFERRED_TOOL_IDS:
        row = _tool_register_row_for(tool_register, tid)
        if not row:
            errors.append(f"TOOL_REGISTER.md missing deferred/planned ecosystem row for {tid}")
        elif "deferred_planned" not in row:
            errors.append(f"TOOL_REGISTER.md row for {tid} must be deferred_planned, observed: {row}")
    if tool_register.count("deferred_planned") < len(CHUNK_40_DEFERRED_TOOL_IDS):
        errors.append("TOOL_REGISTER.md must contain nonzero deferred_planned ecosystem coverage rows after Chunk 40 audit")
    for term in ["GitHub Issues", "GitHub Secrets", "explicit_exclusion_for_now", "Every AWS/GCP/Azure service"]:
        if term not in tool_register:
            errors.append(f"TOOL_REGISTER.md coverage audit missing alias/exclusion term: {term}")

    source_register = read(ROOT / "SOURCE_REGISTER.md")
    for sid in CHUNK_40_SOURCE_IDS:
        if f"`{sid}`" not in source_register:
            errors.append(f"SOURCE_REGISTER.md missing Chunk 40 source ID: {sid}")
    if "Chunk 40 Source Records" not in source_register:
        errors.append("SOURCE_REGISTER.md missing Chunk 40 Source Records section")

    # Semantic route checks for active and deferred ecosystem coverage.
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_TOOL_CATEGORY.md", "Hosting backend auth payments and observability", ["tool.cloudflare", "tool.netlify", "tool.neon", "tool.resend"], ["vcb.chapter.tool_stack_catalog"], "Chunk 40 hosting/backend/email routes")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_TOOL_CATEGORY.md", "Development-stack and verification tools", ["tool.vitest", "tool.storybook"], ["vcb.chapter.writing_updating_tests"], "Chunk 40 testing/UI verification routes")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_TASK.md", "Bootstrap a new project", ["tool.cloudflare", "tool.netlify", "tool.neon", "tool.resend"], ["vcb.chapter.codex_playbooks", "vcb.chapter.first_serious_app"], "Chunk 40 bootstrap coverage routes")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_TASK.md", "Write or update tests", ["tool.vitest"], ["vcb.chapter.writing_updating_tests"], "Chunk 40 Vitest testing route")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_TASK.md", "Improve frontend UI", ["tool.storybook"], ["vcb.chapter.frontend_work"], "Chunk 40 Storybook frontend route")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_TASK.md", "Audit a missing ecosystem tool", list(CHUNK_40_TOOL_CARDS.keys()), ["vcb.chapter.tool_stack_catalog"], "Chunk 40 coverage audit route")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_PROJECT_TYPE.md", "Ecosystem coverage by project type", list(CHUNK_40_TOOL_CARDS.keys()), ["vcb.chapter.tool_stack_catalog"], "Chunk 40 project-type coverage routes")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_RISK_LEVEL.md", "Ecosystem coverage and deferred-tool risk", list(CHUNK_40_TOOL_CARDS.keys()), ["vcb.chapter.tool_stack_catalog"], "Chunk 40 risk routes")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_RECOVERABILITY.md", "Ecosystem tool recoverability", list(CHUNK_40_TOOL_CARDS.keys()), ["vcb.chapter.tool_stack_catalog"], "Chunk 40 recoverability routes")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_FAILURE_MODE.md", "Ecosystem coverage failure modes", list(CHUNK_40_TOOL_CARDS.keys()), ["vcb.chapter.tool_stack_catalog"], "Chunk 40 failure-mode routes")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_CONCEPT.md", "Ecosystem tool concepts", list(CHUNK_40_TOOL_CARDS.keys()), ["vcb.chapter.tool_stack_catalog"], "Chunk 40 concept routes")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_STABILITY.md", "Coverage-gap tools requiring source review", list(CHUNK_40_TOOL_CARDS.keys()), ["vcb.chapter.tool_stack_catalog"], "Chunk 40 stability routes")
    _require_ids_before_fallback(errors, "indexes/INDEX_BY_BUDGET_PROFILE.md", "Coverage-gap budget routes", list(CHUNK_40_TOOL_CARDS.keys()), ["vcb.chapter.tool_stack_catalog"], "Chunk 40 budget routes")

    chunk40_platform_ids = ["tool.cloudflare", "tool.netlify", "tool.neon", "tool.resend"]
    chunk40_all_ids = ["tool.cloudflare", "tool.netlify", "tool.neon", "tool.resend", "tool.vitest", "tool.storybook"]
    _require_all_ids_before_any_fallback(errors, "indexes/INDEX_BY_BUDGET_PROFILE.md", "Production-quality path", chunk40_all_ids, ["vcb.chapter.git_discipline", "vcb.chapter.writing_updating_tests", "vcb.chapter.reviewing_codex_output", "vcb.chapter.security_for_vibe_coders", "vcb.chapter.senior_engineer_checklist"], "Chunk 40 production-quality budget route repair")
    _require_all_ids_before_any_fallback(errors, "indexes/INDEX_BY_TASK.md", "Choose a tool stack", chunk40_all_ids, ["vcb.chapter.tool_stack_catalog", "vcb.chapter.cost_benefit_analysis", "vcb.shortcut.tool_sprawl"], "Chunk 40 tool-stack route repair")
    _require_all_ids_before_any_fallback(errors, "indexes/INDEX_BY_TASK.md", "Build a first serious app", chunk40_platform_ids, ["vcb.chapter.first_serious_app", "vcb.chapter.senior_engineer_checklist", "vcb.chapter.dependency_package_framework_decisions"], "Chunk 40 first-serious-app platform route repair")
    _require_all_ids_before_any_fallback(errors, "indexes/INDEX_BY_TASK.md", "Choose a hosting, backend/auth, payment, observability, or analytics tool", chunk40_platform_ids, ["vcb.chapter.tool_stack_catalog"], "Chunk 40 platform-selection route repair")
    _require_all_ids_before_any_fallback(errors, "indexes/INDEX_FOR_AI_COACHES.md", "Human asks for a giant app or first serious app", chunk40_platform_ids, ["vcb.chapter.first_serious_app", "vcb.chapter.codex_playbooks", "vcb.chapter.feature_slicing"], "Chunk 40 AI-coach serious-app route repair")
    _require_all_ids_before_any_fallback(errors, "indexes/INDEX_FOR_AI_COACHES.md", "Human asks which hosting, backend/auth, payment, observability, or analytics tool to use", chunk40_platform_ids, ["vcb.chapter.tool_stack_catalog"], "Chunk 40 AI-coach platform-selection route repair")
    _require_all_ids_before_any_fallback(errors, "indexes/PROMPT_LIBRARY.md", "Production platform readiness prompt", chunk40_platform_ids, ["vcb.chapter.first_serious_app", "vcb.chapter.senior_engineer_checklist"], "Chunk 40 production platform readiness prompt route repair")
    _require_all_ids_before_any_fallback(errors, "indexes/PROMPT_LIBRARY.md", "Hosting/backend/auth/payment/observability tool-selection prompt", chunk40_platform_ids, ["vcb.chapter.tool_stack_catalog"], "Chunk 40 platform tool-selection prompt route repair")
    prompt_section = extract_markdown_section(read(ROOT / "indexes/PROMPT_LIBRARY.md"), "Tool-catalog coverage audit prompt")
    for tid in CHUNK_40_TOOL_CARDS:
        if f"`{tid}`" not in prompt_section:
            errors.append(f"PROMPT_LIBRARY.md tool-catalog coverage audit prompt missing {tid}")
    coach_section = extract_markdown_section(read(ROOT / "indexes/INDEX_FOR_AI_COACHES.md"), "Human asks about a missing or undercovered ecosystem tool")
    for tid in CHUNK_40_TOOL_CARDS:
        if f"`{tid}`" not in coach_section:
            errors.append(f"INDEX_FOR_AI_COACHES.md missing Chunk 40 coach route for {tid}")

    for rel in ["llms.txt", "llms-full.txt"]:
        body = read(ROOT / rel)
        if body.count("Tool-catalog coverage-gap audit and ecosystem expansion from Chunk 40 is active.") != 1:
            errors.append(f"{rel} must contain exactly one Chunk 40 current-active phrase")
        route = extract_markdown_section(body, "Tool-Catalog Coverage Gap Fast Routing")
        for tid in list(CHUNK_40_TOOL_CARDS.keys()) + ["TOOL_REGISTER.md"]:
            token = f"`{tid}`" if tid.startswith("tool.") else tid
            if token not in route:
                errors.append(f"{rel} coverage-gap route missing {tid}")
        if "do not imply the active cards are exhaustive" not in route:
            errors.append(f"{rel} must warn that active tool cards are not exhaustive")
        for tid in ["tool.render", "tool.railway", "tool.firebase", "tool.aws", "tool.cypress"]:
            if f"`{tid}`" not in route:
                errors.append(f"{rel} deferred-tool route missing {tid}")

        if "smallest active Chunk 35 tool card" in body:
            errors.append(f"{rel} contains stale Chunk 35-only generic platform routing after Chunk 40")
        fast_route = extract_markdown_section(body, "Fast Routing")
        hosting_route_tokens = ["tool.cloudflare", "tool.netlify", "tool.neon", "tool.resend"]
        for tid in hosting_route_tokens:
            if f"`{tid}`" not in fast_route:
                errors.append(f"{rel} generic Fast Routing missing Chunk 40 platform/email/database card {tid}")
        platform_fast = extract_markdown_section(body, "Hosting, Backend/Auth, Payment, Observability, and Product-Analytics Tool Card Fast Routing")
        for tid in ["tool.cloudflare", "tool.netlify", "tool.neon", "tool.resend", "tool.vitest", "tool.storybook"]:
            if f"`{tid}`" not in platform_fast:
                errors.append(f"{rel} hosting/backend fast route missing Chunk 40 active card {tid}")

    # Scope guardrails and report inventory.
    for forbidden_glob in ["topics/field-practices/*.md", "pricing-snapshots/*"]:
        # These may exist from earlier chunks; do not use this as a count check. Scope is enforced through report/created files below.
        pass
    report_path = ROOT / "CHUNK_40_REPORT.md"
    if not report_path.exists():
        errors.append("CHUNK_40_REPORT.md missing")
        return
    report = read(report_path)
    created = report_section_backtick_paths(report, "Files created")
    updated = report_section_backtick_paths(report, "Files updated")
    expected_created = set(CHUNK_40_TOOL_CARDS.values()) | {"CHUNK_40_REPORT.md"}
    missing_created = sorted(expected_created - created)
    if missing_created:
        errors.append(f"CHUNK_40_REPORT.md Files created omits required files: {missing_created}")
    missing_updated = sorted(CHUNK_40_REQUIRED_UPDATED_FILES - updated)
    if missing_updated:
        errors.append(f"CHUNK_40_REPORT.md Files updated omits required files: {missing_updated}")
    for term in [
        "coverage-gap audit", "deferred/planned ecosystem", "six active ecosystem tool cards",
        "TOOL_REGISTER.md no longer implies exhaustive coverage", "validator coverage tightened",
        "No pricing snapshots", "No shortcut cards", "No field-practice promotion"
    ]:
        if term not in report:
            errors.append(f"CHUNK_40_REPORT.md missing required claim: {term}")
    if not report.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_40_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 40", "coverage-gap audit", "deferred/planned ecosystem", "active ecosystem tool cards", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 40 term: {term}")
    boundaries = str(manifest.get("validation_expectations", {}).get("current_chunk_scope_boundaries", ""))
    for term in ["Chunk 40", "No broad shortcut-card expansion", "No field-practice promotion", "No pricing expansion", "No narrative chapters"]:
        if term not in boundaries:
            errors.append(f"manifest.validation_expectations.current_chunk_scope_boundaries missing term: {term}")



def _register_status_counts(path: Path, id_prefix: str) -> Counter:
    counts: Counter = Counter()
    for line in read(path).splitlines():
        if not line.strip().startswith(f"| `{id_prefix}"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        for cell in cells[1:]:
            if cell in {"active", "planned", "deferred_planned", "candidate", "promoted", "deprecated", "retired", "active_snapshot", "deferred"}:
                counts[cell] += 1
                break
    return counts


def _planned_tool_category_count() -> int:
    text = read(ROOT / "TOOL_REGISTER.md")
    sections = {heading: body for heading, body in markdown_h2_sections(text)}
    body = sections.get("Planned Tool Categories", "")
    return len(re.findall(r"\|[^|]+\|\s*`tool\.[^`]+`\s*\|", body))


def _pricing_snapshot_status_counts() -> Counter:
    counts: Counter = Counter()
    for line in read(ROOT / "PRICING_SNAPSHOT_REGISTER.md").splitlines():
        if not line.strip().startswith("| `vcb.pricing_snapshot."):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if cells:
            status = cells[-1]
            counts[status] += 1
    return counts


def validate_chunk_41_finalization_readiness_audit(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_41":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_41_finalization_readiness_audit":
        errors.append("manifest.active_chunk.id must be chunk_41_finalization_readiness_audit")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_42_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_42_editor_scoped_next_slice for Chunk 41")

    scope_text = " ".join(map(str, manifest.get("active_chunk", {}).get("scope", [])))
    for term in ["bounded finalization-readiness", "repository-contract audit", "no new tool cards", "no pricing snapshots", "no narrative chapters"]:
        if term not in scope_text:
            errors.append(f"manifest.active_chunk.scope missing Chunk 41 term: {term}")

    scope_boundary = str(manifest.get("validation_expectations", {}).get("current_chunk_scope_boundaries", ""))
    for term in [
        "Chunk 41",
        "No new tool cards",
        "No field-practice cards",
        "No shortcut cards",
        "No pricing snapshots",
        "No broad workflow expansion",
        "No broad security/secrets expansion",
        "No broad tool-catalog expansion",
        "No narrative chapters",
    ]:
        if term not in scope_boundary:
            errors.append(f"manifest.validation_expectations.current_chunk_scope_boundaries missing term: {term}")
    if "Chunk 40 boundary" in scope_boundary:
        errors.append("manifest.validation_expectations.current_chunk_scope_boundaries still names Chunk 40")

    expected_package = manifest.get("package", {}).get("canonical_review_package")
    source_artifacts = manifest.get("source_artifacts", {}) if isinstance(manifest.get("source_artifacts"), dict) else {}
    for alias_key in ("package_file", "review_package"):
        alias_value = source_artifacts.get(alias_key)
        if alias_value != expected_package:
            errors.append(
                f"manifest.source_artifacts.{alias_key} must match manifest.package.canonical_review_package: "
                f"{alias_value!r} != {expected_package!r}"
            )
        if isinstance(alias_value, str) and "chunk-41" not in alias_value:
            errors.append(f"manifest.source_artifacts.{alias_key} does not point to a Chunk 41 package: {alias_value!r}")

    tool_counts = _register_status_counts(ROOT / "TOOL_REGISTER.md", "tool.")
    shortcut_counts = _register_status_counts(ROOT / "SHORTCUT_REGISTER.md", "vcb.shortcut.")
    field_counts = _register_status_counts(ROOT / "FIELD_PRACTICES.md", "vcb.field.")
    pricing_counts = _pricing_snapshot_status_counts()
    planned_tool_categories = _planned_tool_category_count()

    expected_counts = {
        "active_tool_cards": int(tool_counts.get("active", 0)),
        "deferred_planned_tool_ids": int(tool_counts.get("deferred_planned", 0)),
        "planned_tool_categories": planned_tool_categories,
        "active_shortcut_cards": int(shortcut_counts.get("active", 0)),
        "planned_shortcut_cards": int(shortcut_counts.get("planned", 0)),
        "candidate_field_practices": int(field_counts.get("candidate", 0)),
        "active_pricing_snapshots": int(pricing_counts.get("active_snapshot", 0)),
        "deferred_pricing_snapshots": int(pricing_counts.get("deferred", 0)),
    }
    required_values = {
        "active_tool_cards": 52,
        "deferred_planned_tool_ids": 23,
        "planned_tool_categories": 14,
        "active_shortcut_cards": 50,
        "planned_shortcut_cards": 48,
        "candidate_field_practices": 9,
        "active_pricing_snapshots": 1,
        "deferred_pricing_snapshots": 4,
    }
    for key, required in required_values.items():
        if expected_counts.get(key) != required:
            errors.append(f"Chunk 41 register count mismatch for {key}: {expected_counts.get(key)!r} != {required}")

    readiness = manifest.get("finalization_readiness_audit", {}) if isinstance(manifest.get("finalization_readiness_audit"), dict) else {}
    if readiness.get("status") != "audit_complete_waiting_for_editor_review":
        errors.append("manifest.finalization_readiness_audit.status must be audit_complete_waiting_for_editor_review")
    for key, observed in expected_counts.items():
        if readiness.get(key) != observed:
            errors.append(f"manifest.finalization_readiness_audit.{key} does not match registers: {readiness.get(key)!r} != {observed}")
    gaps = readiness.get("release_candidate_gaps", []) if isinstance(readiness.get("release_candidate_gaps"), list) else []
    for term in ["No release-candidate package", "pricing", "deferred/planned", "candidate", "changelog"]:
        if not any(term in str(gap) for gap in gaps):
            errors.append(f"manifest.finalization_readiness_audit.release_candidate_gaps missing term: {term}")

    readme = read(ROOT / "README.md")
    if "## Finalization Readiness Audit" not in readme:
        errors.append("README.md missing Finalization Readiness Audit section")
    for term in ["52 active tool cards", "23 deferred/planned ecosystem IDs", "50 active shortcut cards", "48 planned shortcut rows", "9 active field-practice", "1 active pricing snapshot", "4 deferred pricing snapshot", "Release-candidate gap list"]:
        if term not in readme:
            errors.append(f"README.md Finalization Readiness Audit missing term: {term}")

    for rel in ["llms.txt", "llms-full.txt"]:
        llm = read(ROOT / rel)
        if "## Finalization Readiness Fast Routing" not in llm:
            errors.append(f"{rel} missing Finalization Readiness Fast Routing section")
        for term in ["CHUNK_41_REPORT.md", "TOOL_REGISTER.md", "FIELD_PRACTICES.md", "PRICING_SNAPSHOT_REGISTER.md"]:
            if term not in llm:
                errors.append(f"{rel} finalization routing missing {term}")
        if re.search(r"^## Active Chunk \d+ .*Tool Card", llm, flags=re.M):
            errors.append(f"{rel} still contains generation-specific active tool-card list heading")

    for rel, term in [
        ("TOOL_REGISTER.md", "52 active authored tool cards"),
        ("SHORTCUT_REGISTER.md", "50 active shortcut rows"),
        ("FIELD_PRACTICES.md", "All 9 active field-practice retrieval cards remain `candidate`"),
        ("PRICING_SNAPSHOT_REGISTER.md", "1 active pricing snapshot"),
    ]:
        if term not in read(ROOT / rel):
            errors.append(f"{rel} missing Chunk 41 finalization note term: {term}")

    topic_files = sorted(p for p in (ROOT / "topics").rglob("*.md") if p.name != ".gitkeep")
    tool_catalog_files = sorted(p for p in (ROOT / "topics" / "tool-catalog").glob("*.md") if p.name != ".gitkeep")
    pricing_files = sorted(p for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep")
    if len(topic_files) != 189:
        errors.append(f"Chunk 41 must not add topic cards: observed topic file count {len(topic_files)} != 189")
    if len(tool_catalog_files) != 52:
        errors.append(f"Chunk 41 must not add tool cards: observed tool-catalog file count {len(tool_catalog_files)} != 52")
    if len(pricing_files) != 1:
        errors.append(f"Chunk 41 must not add pricing snapshots: observed pricing file count {len(pricing_files)} != 1")

    report_path = ROOT / "CHUNK_41_REPORT.md"
    if not report_path.exists():
        errors.append("CHUNK_41_REPORT.md missing")
        return
    report = read(report_path)
    required_created = {"CHUNK_41_REPORT.md"}
    required_updated = {
        "README.md",
        "manifest.json",
        "llms.txt",
        "llms-full.txt",
        "SOURCE_REGISTER.md",
        "TOOL_REGISTER.md",
        "SHORTCUT_REGISTER.md",
        "FIELD_PRACTICES.md",
        "PRICING_SNAPSHOT_REGISTER.md",
        "CHANGELOG.md",
        "TREE.txt",
        "scripts/validate_repository.py",
    }
    created = report_section_backtick_paths(report, "Files created")
    updated = report_section_backtick_paths(report, "Files updated")
    missing_created = sorted(required_created - created)
    missing_updated = sorted(required_updated - updated)
    if missing_created:
        errors.append(f"CHUNK_41_REPORT.md Files created omits required files: {missing_created}")
    if missing_updated:
        errors.append(f"CHUNK_41_REPORT.md Files updated omits required files: {missing_updated}")
    for term in ["## Finalization Gap List", "No release-candidate package", "Non-OpenAI pricing", "23 concrete deferred/planned ecosystem IDs", "candidate-only", "validator"]:
        if term not in report:
            errors.append(f"CHUNK_41_REPORT.md missing finalization audit term: {term}")
    if not report.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_41_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")



def validate_chunk_42_release_candidate_disposition_cleanup(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_42":
        return

    if manifest.get("active_chunk", {}).get("id") != "chunk_42_release_candidate_scope_disposition_cleanup":
        errors.append("manifest.active_chunk.id must be chunk_42_release_candidate_scope_disposition_cleanup")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_43_release_candidate_packaging":
        errors.append("manifest.next_recommended_chunk.id must be chunk_43_release_candidate_packaging for Chunk 42")

    scope_text = " ".join(map(str, manifest.get("active_chunk", {}).get("scope", [])))
    for term in [
        "release-candidate scope/disposition",
        "final governance cleanup",
        "no release-candidate package",
        "no new tool cards",
        "no pricing snapshots",
        "no source-map migration",
        "no narrative chapters",
    ]:
        if term not in scope_text:
            errors.append(f"manifest.active_chunk.scope missing Chunk 42 term: {term}")

    scope_boundary = str(manifest.get("validation_expectations", {}).get("current_chunk_scope_boundaries", ""))
    for term in [
        "Chunk 42",
        "No release-candidate package",
        "No new tool cards",
        "No field-practice cards",
        "No shortcut cards",
        "No pricing snapshots",
        "No broad workflow expansion",
        "No broad security/secrets expansion",
        "No broad tool-catalog expansion",
        "No source-map migration",
        "No narrative chapters",
    ]:
        if term not in scope_boundary:
            errors.append(f"manifest.validation_expectations.current_chunk_scope_boundaries missing term: {term}")
    if "Chunk 41 boundary" in scope_boundary:
        errors.append("manifest.validation_expectations.current_chunk_scope_boundaries still names Chunk 41")

    expected_package = manifest.get("package", {}).get("canonical_review_package")
    for alias_owner in [manifest, manifest.get("package", {}), manifest.get("artifact_hygiene", {}), manifest.get("source_artifacts", {}), manifest.get("active_chunk", {})]:
        if not isinstance(alias_owner, dict):
            continue
        if "canonical_review_package" in alias_owner and alias_owner.get("canonical_review_package") != expected_package:
            errors.append(f"canonical review package alias mismatch: {alias_owner.get('canonical_review_package')!r} != {expected_package!r}")
    source_artifacts = manifest.get("source_artifacts", {}) if isinstance(manifest.get("source_artifacts"), dict) else {}
    for alias_key in ("package_file", "review_package"):
        alias_value = source_artifacts.get(alias_key)
        if alias_value != expected_package:
            errors.append(
                f"manifest.source_artifacts.{alias_key} must match manifest.package.canonical_review_package: "
                f"{alias_value!r} != {expected_package!r}"
            )
        if isinstance(alias_value, str) and "chunk-42" not in alias_value:
            errors.append(f"manifest.source_artifacts.{alias_key} does not point to a Chunk 42 package: {alias_value!r}")
    if isinstance(expected_package, str):
        if "release-candidate" in expected_package.lower() or "rc" in expected_package.lower():
            errors.append("Chunk 42 canonical package must not be named as a release-candidate package")
        if "chunk-42" not in expected_package:
            errors.append(f"Chunk 42 canonical package must point to a chunk-42 package: {expected_package!r}")

    readiness = manifest.get("finalization_readiness_audit", {}) if isinstance(manifest.get("finalization_readiness_audit"), dict) else {}
    if readiness.get("status") != "audit_complete_dispositioned_in_chunk_42":
        errors.append("manifest.finalization_readiness_audit.status must remain audit_complete_dispositioned_in_chunk_42 for Chunk 42")
    manifest_text = json.dumps(manifest, sort_keys=True)
    stale_prior_review_terms = [
        "Chunk 41 is an author audit package waiting for editor review",
        "Chunk 41 waiting for editor review",
    ]
    for term in stale_prior_review_terms:
        if term in manifest_text:
            errors.append(f"manifest contains stale prior-review-state wording: {term}")

    tool_counts = _register_status_counts(ROOT / "TOOL_REGISTER.md", "tool.")
    shortcut_counts = _register_status_counts(ROOT / "SHORTCUT_REGISTER.md", "vcb.shortcut.")
    field_counts = _register_status_counts(ROOT / "FIELD_PRACTICES.md", "vcb.field.")
    pricing_counts = _pricing_snapshot_status_counts()
    observed_counts = {
        "active_tool_cards": int(tool_counts.get("active", 0)),
        "deferred_planned_tool_ids": int(tool_counts.get("deferred_planned", 0)),
        "active_shortcut_cards": int(shortcut_counts.get("active", 0)),
        "planned_shortcut_cards": int(shortcut_counts.get("planned", 0)),
        "candidate_field_practices": int(field_counts.get("candidate", 0)),
        "active_pricing_snapshots": int(pricing_counts.get("active_snapshot", 0)),
        "deferred_pricing_snapshots": int(pricing_counts.get("deferred", 0)),
    }
    expected_counts = {
        "active_tool_cards": 52,
        "deferred_planned_tool_ids": 23,
        "active_shortcut_cards": 50,
        "planned_shortcut_cards": 48,
        "candidate_field_practices": 9,
        "active_pricing_snapshots": 1,
        "deferred_pricing_snapshots": 4,
    }
    for key, expected in expected_counts.items():
        if observed_counts.get(key) != expected:
            errors.append(f"Chunk 42 register count mismatch for {key}: {observed_counts.get(key)!r} != {expected}")

    disposition = manifest.get("release_candidate_scope_disposition_cleanup", {}) if isinstance(manifest.get("release_candidate_scope_disposition_cleanup"), dict) else {}
    if disposition.get("status") != "disposition_complete_waiting_for_editor_review":
        errors.append("manifest.release_candidate_scope_disposition_cleanup.status must be disposition_complete_waiting_for_editor_review")
    if disposition.get("current_package_status") != "author_review_package_not_release_candidate":
        errors.append("manifest.release_candidate_scope_disposition_cleanup.current_package_status must state author_review_package_not_release_candidate")
    if disposition.get("release_candidate_package_produced") is not False:
        errors.append("manifest.release_candidate_scope_disposition_cleanup.release_candidate_package_produced must be false")
    if disposition.get("release_candidate_allowed_next") is not True:
        errors.append("manifest.release_candidate_scope_disposition_cleanup.release_candidate_allowed_next must be true")
    if disposition.get("recommended_next_chunk") != "chunk_43_release_candidate_packaging":
        errors.append("manifest.release_candidate_scope_disposition_cleanup.recommended_next_chunk must be chunk_43_release_candidate_packaging")
    snapshot = disposition.get("register_snapshot", {}) if isinstance(disposition.get("register_snapshot"), dict) else {}
    for key, expected in expected_counts.items():
        if snapshot.get(key) != expected:
            errors.append(f"manifest.release_candidate_scope_disposition_cleanup.register_snapshot.{key} mismatch: {snapshot.get(key)!r} != {expected}")

    matrix = disposition.get("disposition_matrix", []) if isinstance(disposition.get("disposition_matrix"), list) else []
    required_gaps = {
        "no_release_candidate_package_has_been_produced",
        "non_openai_exact_pricing_snapshots_deferred",
        "tool_catalog_curated_not_exhaustive",
        "field_practices_candidate_only",
        "changelog_chronology_not_strictly_normalized",
    }
    observed_gaps = {str(row.get("gap")) for row in matrix if isinstance(row, dict)}
    missing_gaps = sorted(required_gaps - observed_gaps)
    if missing_gaps:
        errors.append(f"release-candidate disposition matrix missing gaps: {missing_gaps}")
    for row in matrix:
        if not isinstance(row, dict):
            continue
        gap = str(row.get("gap"))
        if gap != "no_release_candidate_package_has_been_produced" and row.get("blocks_release_candidate_packaging_next") is not False:
            errors.append(f"release-candidate disposition gap {gap} must not block next packaging unless explicitly rescoped")
    no_rc_row = next((row for row in matrix if isinstance(row, dict) and row.get("gap") == "no_release_candidate_package_has_been_produced"), {})
    if no_rc_row.get("blocks_this_author_package_as_rc") is not True:
        errors.append("no_release_candidate_package_has_been_produced must block treating this author package as RC")
    if no_rc_row.get("blocks_release_candidate_packaging_next") is not False:
        errors.append("no_release_candidate_package_has_been_produced must not block a future editor-approved packaging chunk")

    readme = read(ROOT / "README.md")
    for term in [
        "## Release-Candidate Scope Disposition",
        "Release-Candidate Disposition Matrix",
        "This package is **not** a release-candidate package",
        "Release candidate allowed next?",
        "Yes, after editor approval",
        "52 active tool cards and 23 deferred/planned ecosystem IDs",
        "50 active shortcut cards and 48 planned shortcut rows",
        "9 active field-practice retrieval cards",
        "1 active pricing snapshot and 4 deferred pricing snapshot categories",
        "Changelog chronology",
        "CHUNK_42_REPORT.md",
    ]:
        if term not in readme:
            errors.append(f"README.md release-candidate disposition missing term: {term}")
    if "release-candidate package has been produced" in readme.lower() and "No release-candidate package has been produced" not in readme:
        errors.append("README.md may imply a release-candidate package exists")

    for rel in ["llms.txt", "llms-full.txt"]:
        llm = read(ROOT / rel)
        if llm.count("Release-candidate scope/disposition and final governance cleanup from Chunk 42 is active.") != 1:
            errors.append(f"{rel} must contain exactly one Chunk 42 current-active phrase")
        for term in [
            "## Release Candidate Disposition Fast Routing",
            "CHUNK_42_REPORT.md",
            "not a release-candidate package",
            "release-candidate packaging is allowed next",
            "packaging-only next chunk",
            "TOOL_REGISTER.md",
            "FIELD_PRACTICES.md",
            "PRICING_SNAPSHOT_REGISTER.md",
            "CHANGELOG.md",
        ]:
            if term not in llm:
                errors.append(f"{rel} release-candidate disposition routing missing term: {term}")
        if re.search(r"^## Active Chunk \d+ .*Tool Card", llm, flags=re.M):
            errors.append(f"{rel} still contains generation-specific active tool-card list heading")

    changelog = read(ROOT / "CHANGELOG.md")
    for term in ["## Changelog Ordering Convention", "Current and recent governance/chunk entries appear near the top", "older historical entries may preserve", "review trail"]:
        if term not in changelog:
            errors.append(f"CHANGELOG.md missing ordering convention term: {term}")
    if "## Chunk 42 — Release-Candidate Scope Disposition Cleanup" not in changelog:
        errors.append("CHANGELOG.md missing Chunk 42 entry")

    for rel, term in [
        ("TOOL_REGISTER.md", "## Chunk 42 Release-Candidate Disposition Note"),
        ("TOOL_REGISTER.md", "52 active authored tool cards and 23 deferred/planned concrete ecosystem IDs"),
        ("SHORTCUT_REGISTER.md", "50 active shortcut rows and 48 planned shortcut rows"),
        ("FIELD_PRACTICES.md", "all 9 active field-practice retrieval cards remain `candidate`"),
        ("PRICING_SNAPSHOT_REGISTER.md", "non-OpenAI pricing categories remain deferred documented limitations"),
        ("SOURCE_REGISTER.md", "## Chunk 42 Source Records"),
    ]:
        if term not in read(ROOT / rel):
            errors.append(f"{rel} missing Chunk 42 synchronization term: {term}")

    topic_files = sorted(p for p in (ROOT / "topics").rglob("*.md") if p.name != ".gitkeep")
    tool_catalog_files = sorted(p for p in (ROOT / "topics" / "tool-catalog").glob("*.md") if p.name != ".gitkeep")
    field_cards = sorted(p for p in (ROOT / "topics" / "field-practices").glob("*.md") if p.name != ".gitkeep")
    pricing_files = sorted(p for p in (ROOT / "pricing-snapshots").glob("*.md") if p.name != ".gitkeep")
    if len(topic_files) != 189:
        errors.append(f"Chunk 42 must not add topic cards: observed topic file count {len(topic_files)} != 189")
    if len(tool_catalog_files) != 52:
        errors.append(f"Chunk 42 must not add tool cards: observed tool-catalog file count {len(tool_catalog_files)} != 52")
    if len(field_cards) != 9:
        errors.append(f"Chunk 42 must not add field-practice cards: observed field-practice card count {len(field_cards)} != 9")
    if len(pricing_files) != 1:
        errors.append(f"Chunk 42 must not add pricing snapshots: observed pricing file count {len(pricing_files)} != 1")

    report_path = ROOT / "CHUNK_42_REPORT.md"
    if not report_path.exists():
        errors.append("CHUNK_42_REPORT.md missing")
        return
    report = read(report_path)
    required_created = {"CHUNK_42_REPORT.md"}
    required_updated = {
        "README.md",
        "manifest.json",
        "llms.txt",
        "llms-full.txt",
        "SOURCE_REGISTER.md",
        "TOOL_REGISTER.md",
        "SHORTCUT_REGISTER.md",
        "FIELD_PRACTICES.md",
        "PRICING_SNAPSHOT_REGISTER.md",
        "CHANGELOG.md",
        "TREE.txt",
        "scripts/validate_repository.py",
    }
    created = report_section_backtick_paths(report, "Files created")
    updated = report_section_backtick_paths(report, "Files updated")
    missing_created = sorted(required_created - created)
    missing_updated = sorted(required_updated - updated)
    if missing_created:
        errors.append(f"CHUNK_42_REPORT.md Files created omits required files: {missing_created}")
    if missing_updated:
        errors.append(f"CHUNK_42_REPORT.md Files updated omits required files: {missing_updated}")
    for term in [
        "Release-Candidate Disposition Matrix",
        "Release Candidate Allowed Next?",
        "Yes, release-candidate packaging is allowed next",
        "not a release candidate",
        "documented limitation",
        "changelog ordering convention",
        "validator",
    ]:
        if term not in report:
            errors.append(f"CHUNK_42_REPORT.md missing disposition term: {term}")
    if not report.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_42_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")

    current_checks = str(manifest.get("validation_expectations", {}).get("current_chunk_checks", ""))
    for term in ["Chunk 42", "release-candidate disposition", "no-premature-RC", "changelog", "register-count", "scope guardrails"]:
        if term not in current_checks:
            errors.append(f"manifest.validation_expectations.current_chunk_checks missing Chunk 42 term: {term}")


CHUNK_43_REQUIRED_UPDATED_FILES = {
    "README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md",
    "TOOL_REGISTER.md", "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py",
}


def _chunk_43_actual_source_paths() -> list[str]:
    return actual_source_paths()


def _chunk_43_manifest_inventory_sha256(paths: list[str]) -> str:
    return hashlib.sha256(("\n".join(paths) + "\n").encode("utf-8")).hexdigest()


def _chunk_43_source_content_manifest_sha256(exclude: set[str]) -> str:
    lines: list[str] = []
    for rel in _chunk_43_actual_source_paths():
        if rel in exclude:
            continue
        digest = hashlib.sha256((ROOT / rel).read_bytes()).hexdigest()
        lines.append(f"{digest}  {rel}")
    return hashlib.sha256(("\n".join(lines) + "\n").encode("utf-8")).hexdigest()


def _chunk_43_integrity_table_value(text: str, key: str) -> str | None:
    pattern = rf"`{re.escape(key)}`\s*\|\s*`?([^`|\n]+)`?"
    match = re.search(pattern, text)
    return match.group(1).strip() if match else None


def validate_chunk_43_release_candidate_packaging(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_43":
        return

    expected_package = "vibe-coding-bible-release-candidate-1-revision-2-20260612T040000Z-authoritative.zip"
    if manifest.get("active_chunk", {}).get("id") != "chunk_43_release_candidate_packaging":
        errors.append("manifest.active_chunk.id must be chunk_43_release_candidate_packaging")
    if manifest.get("next_recommended_chunk", {}).get("id") != "chunk_44_editor_scoped_next_slice":
        errors.append("manifest.next_recommended_chunk.id must be chunk_44_editor_scoped_next_slice for Chunk 43")

    canonical = manifest.get("package", {}).get("canonical_review_package")
    if canonical != expected_package:
        errors.append(f"manifest.package.canonical_review_package must be {expected_package!r}: {canonical!r}")
    for alias_owner_name, alias_owner in [
        ("manifest", manifest),
        ("manifest.package", manifest.get("package", {})),
        ("manifest.artifact_hygiene", manifest.get("artifact_hygiene", {})),
        ("manifest.source_artifacts", manifest.get("source_artifacts", {})),
        ("manifest.active_chunk", manifest.get("active_chunk", {})),
    ]:
        if isinstance(alias_owner, dict) and "canonical_review_package" in alias_owner and alias_owner.get("canonical_review_package") != expected_package:
            errors.append(f"{alias_owner_name}.canonical_review_package must point to RC package: {alias_owner.get('canonical_review_package')!r}")
    source_artifacts = manifest.get("source_artifacts", {}) if isinstance(manifest.get("source_artifacts"), dict) else {}
    for alias_key in ("package_file", "review_package"):
        if source_artifacts.get(alias_key) != expected_package:
            errors.append(f"manifest.source_artifacts.{alias_key} must point to RC package: {source_artifacts.get(alias_key)!r}")

    readme = read(ROOT / "README.md")
    llms = read(ROOT / "llms.txt")
    llms_full = read(ROOT / "llms-full.txt")
    report_path = ROOT / "CHUNK_43_REPORT.md"
    report = read(report_path) if report_path.exists() else ""
    integrity_rel = "RELEASE_CANDIDATE_1_INTEGRITY.md"
    integrity_path = ROOT / integrity_rel
    expected_sidecar = expected_package + ".sha256"
    for rel, text in [("README.md", readme), ("llms.txt", llms), ("llms-full.txt", llms_full), ("CHUNK_43_REPORT.md", report)]:
        for term in ["Release Candidate 1", "awaiting editor review"]:
            if term not in text:
                errors.append(f"{rel} missing RC status term: {term}")
    if "## Release-Candidate Package Status" not in readme:
        errors.append("README.md missing Release-Candidate Package Status section")
    if "## Release Candidate Package Fast Routing" not in llms or "## Release Candidate Package Fast Routing" not in llms_full:
        errors.append("llms.txt and llms-full.txt must include Release Candidate Package Fast Routing")

    manifest_text = json.dumps(manifest, sort_keys=True)
    stale_terms = [
        "not_release_candidate_yet",
        "author_review_package_not_release_candidate",
        "No release-candidate package has been produced",
        "Chunk 42 does not produce the RC package",
        "Chunk 41 is an author audit package waiting for editor review",
    ]
    for term in stale_terms:
        if term in manifest_text:
            errors.append(f"manifest contains stale pre-RC wording: {term}")
    for rel, text in [("README.md", readme), ("llms.txt", llms), ("llms-full.txt", llms_full)]:
        if "not a release-candidate package" in text or "not a release candidate" in text:
            errors.append(f"{rel} still says the current package is not a release candidate")

    tool_register = read(ROOT / "TOOL_REGISTER.md")
    if re.search(r"This author package is not a release[- ]candidate package", tool_register, flags=re.I):
        errors.append("TOOL_REGISTER.md contains stale current-package non-RC wording")
    expected_tool_disposition = (
        "The Chunk 42 author package was not a release-candidate package; "
        "Release Candidate 1 was later produced by Chunk 43 as a packaging-only artifact."
    )
    if expected_tool_disposition not in tool_register:
        errors.append("TOOL_REGISTER.md missing historical Chunk 42 to Chunk 43 RC disposition wording")

    stale_checksum_claims = [
        "checksum generated and reported in the submission response",
        "release-candidate packaging verification, checksum, package hygiene",
        "submitted as external sidecar",
        "submitted beside the authoritative zip",
        "provided in the submitted sidecar",
        "the submitted `.sha256` sidecar",
        "submitted `.sha256` sidecar",
    ]
    for rel, text in [("README.md", readme), ("CHUNK_43_REPORT.md", report), (integrity_rel, read(integrity_path) if integrity_path.exists() else "")]:
        lowered = text.lower()
        for stale_claim in stale_checksum_claims:
            if stale_claim.lower() in lowered:
                errors.append(f"{rel} contains stale/false sidecar or checksum wording: {stale_claim}")
        if "checksum" in lowered and (integrity_rel not in text or expected_sidecar not in text):
            errors.append(f"{rel} mentions checksum but does not name both {integrity_rel} and {expected_sidecar}")
    if "source-tree integrity" not in readme or integrity_rel not in readme or expected_sidecar not in readme or "external sidecar convention" not in readme:
        errors.append("README.md must name source-tree integrity file, external checksum separation, and .sha256 sidecar convention")
    if "## Package Integrity Mechanism" not in report or integrity_rel not in report or expected_sidecar not in report or "separates three verification targets" not in report:
        errors.append("CHUNK_43_REPORT.md must distinguish source-tree integrity, final zip checksum, and sidecar convention")

    actual_paths = _chunk_43_actual_source_paths()
    if not integrity_path.exists():
        errors.append(f"{integrity_rel} missing")
    else:
        integrity = read(integrity_path)
        for term in [expected_package, expected_sidecar, "manifest_inventory_sha256", "source_content_manifest_sha256_excluding_this_file", "validator_output"]:
            if term not in integrity:
                errors.append(f"{integrity_rel} missing required integrity term: {term}")
        if "sorted lines of `<file_sha256>  <package_relative_path>`" in integrity:
            errors.append(f"{integrity_rel} uses stale hash-input wording; must describe path-ordered hashing")
        if "iterating package-relative source-file paths in ascending lexicographic order" not in integrity:
            errors.append(f"{integrity_rel} must describe source-content hash input as path-ordered")
        if "checksum_sidecar_convention" not in integrity:
            errors.append(f"{integrity_rel} must label the sidecar as a convention, not a submitted internal artifact")
        expected_inventory_hash = _chunk_43_manifest_inventory_sha256(actual_paths)
        observed_inventory_hash = _chunk_43_integrity_table_value(integrity, "manifest_inventory_sha256")
        if observed_inventory_hash != expected_inventory_hash:
            errors.append(
                f"{integrity_rel} manifest_inventory_sha256 mismatch: "
                f"{observed_inventory_hash!r} != {expected_inventory_hash}"
            )
        expected_content_hash = _chunk_43_source_content_manifest_sha256({integrity_rel})
        observed_content_hash = _chunk_43_integrity_table_value(integrity, "source_content_manifest_sha256_excluding_this_file")
        if observed_content_hash != expected_content_hash:
            errors.append(
                f"{integrity_rel} source_content_manifest_sha256_excluding_this_file mismatch: "
                f"{observed_content_hash!r} != {expected_content_hash}"
            )
        observed_count = _chunk_43_integrity_table_value(integrity, "source_file_count")
        if observed_count != str(len(actual_paths)):
            errors.append(f"{integrity_rel} source_file_count mismatch: {observed_count!r} != {len(actual_paths)}")

    tree_lines = set(read(ROOT / "TREE.txt").splitlines()) if (ROOT / "TREE.txt").exists() else set()
    manifest_source_files = set(manifest.get("source_files", []) or [])
    for list_name, values in [
        ("manifest.source_files", manifest_source_files),
        ("manifest.source_artifacts.source_files", set(source_artifacts.get("source_files", []) or [])),
        ("manifest.source_artifacts.all_tracked_files", set(source_artifacts.get("all_tracked_files", []) or [])),
        ("manifest.source_artifacts.root_artifacts", set(source_artifacts.get("root_artifacts", []) or [])),
        ("manifest.source_artifacts.root_files", set(source_artifacts.get("root_files", []) or [])),
        ("TREE.txt", tree_lines),
    ]:
        if integrity_rel not in values:
            errors.append(f"{list_name} missing {integrity_rel}")

    hygiene = manifest.get("artifact_hygiene", {}) if isinstance(manifest.get("artifact_hygiene"), dict) else {}
    if hygiene.get("integrity_report") != integrity_rel:
        errors.append("manifest.artifact_hygiene.integrity_report must point to RELEASE_CANDIDATE_1_INTEGRITY.md")
    if hygiene.get("checksum_sidecar") != expected_sidecar:
        errors.append("manifest.artifact_hygiene.checksum_sidecar must point to expected .sha256 sidecar")
    if hygiene.get("checksum_sidecar_status") != "external_convention_not_embedded_in_zip":
        errors.append("manifest.artifact_hygiene.checksum_sidecar_status must clarify external convention/not embedded in zip")

    rc = manifest.get("release_candidate_packaging", {}) if isinstance(manifest.get("release_candidate_packaging"), dict) else {}
    if rc.get("status") != "release_candidate_package_produced_waiting_for_editor_review":
        errors.append("manifest.release_candidate_packaging.status must be release_candidate_package_produced_waiting_for_editor_review")
    if rc.get("release_candidate_package") != expected_package:
        errors.append("manifest.release_candidate_packaging.release_candidate_package must match canonical package")
    if rc.get("integrity_report") != integrity_rel:
        errors.append("manifest.release_candidate_packaging.integrity_report must point to RELEASE_CANDIDATE_1_INTEGRITY.md")
    if rc.get("checksum_sidecar") != expected_sidecar:
        errors.append("manifest.release_candidate_packaging.checksum_sidecar must point to expected .sha256 sidecar")
    if rc.get("checksum_sidecar_status") != "external_convention_not_embedded_in_zip":
        errors.append("manifest.release_candidate_packaging.checksum_sidecar_status must clarify external convention/not embedded in zip")
    if rc.get("revision") != "revision_2":
        errors.append("manifest.release_candidate_packaging.revision must be revision_2")
    if rc.get("final_release_approved") is not False:
        errors.append("manifest.release_candidate_packaging.final_release_approved must be false")
    if rc.get("packaging_only") is not True:
        errors.append("manifest.release_candidate_packaging.packaging_only must be true")

    readiness = manifest.get("finalization_readiness_audit", {}) if isinstance(manifest.get("finalization_readiness_audit"), dict) else {}
    if readiness.get("release_candidate_status") != "release_candidate_packaged_waiting_for_editor_review":
        errors.append("manifest.finalization_readiness_audit.release_candidate_status must indicate packaged RC awaiting editor review")
    if readiness.get("status") != "audit_complete_release_candidate_packaged_in_chunk_43":
        errors.append("manifest.finalization_readiness_audit.status must be audit_complete_release_candidate_packaged_in_chunk_43")

    limits_terms = [
        "exact non-OpenAI pricing",
        "curated",
        "52 active tool cards",
        "23 deferred/planned ecosystem IDs",
        "candidate-only",
        "changelog ordering",
    ]
    for term in limits_terms:
        if term not in readme and term not in report and term not in manifest_text:
            errors.append(f"RC documented limitation missing across README/report/manifest: {term}")

    tool_counts = _register_status_counts(ROOT / "TOOL_REGISTER.md", "tool.")
    shortcut_counts = _register_status_counts(ROOT / "SHORTCUT_REGISTER.md", "vcb.shortcut.")
    field_counts = _register_status_counts(ROOT / "FIELD_PRACTICES.md", "vcb.field.")
    pricing_counts = _pricing_snapshot_status_counts()
    expected_counts = {
        "active_tool_cards": 52,
        "deferred_planned_tool_ids": 23,
        "active_shortcut_cards": 50,
        "planned_shortcut_cards": 48,
        "candidate_field_practices": 9,
        "active_pricing_snapshots": 1,
        "deferred_pricing_snapshots": 4,
    }
    observed_counts = {
        "active_tool_cards": int(tool_counts.get("active", 0)),
        "deferred_planned_tool_ids": int(tool_counts.get("deferred_planned", 0)),
        "active_shortcut_cards": int(shortcut_counts.get("active", 0)),
        "planned_shortcut_cards": int(shortcut_counts.get("planned", 0)),
        "candidate_field_practices": int(field_counts.get("candidate", 0)),
        "active_pricing_snapshots": int(pricing_counts.get("active_snapshot", 0)),
        "deferred_pricing_snapshots": int(pricing_counts.get("deferred", 0)),
    }
    for key, expected in expected_counts.items():
        if observed_counts.get(key) != expected:
            errors.append(f"Chunk 43 register count mismatch for {key}: {observed_counts.get(key)} != {expected}")
        if rc.get("register_snapshot", {}).get(key) != expected:
            errors.append(f"manifest.release_candidate_packaging.register_snapshot.{key} mismatch: {rc.get('register_snapshot', {}).get(key)!r} != {expected}")

    scope_boundary = str(manifest.get("validation_expectations", {}).get("current_chunk_scope_boundaries", ""))
    for term in [
        "Chunk 43",
        "Release Candidate 1 packaging only",
        "No new tool cards",
        "No field-practice cards",
        "No shortcut cards",
        "No pricing snapshots",
        "No broad workflow expansion",
        "No broad security/secrets expansion",
        "No broad tool-catalog expansion",
        "No source-map migration",
        "No narrative chapters",
    ]:
        if term not in scope_boundary:
            errors.append(f"manifest.validation_expectations.current_chunk_scope_boundaries missing Chunk 43 term: {term}")

    if not report_path.exists():
        errors.append("CHUNK_43_REPORT.md missing")
        return
    created = report_section_backtick_paths(report, "Files created")
    updated = report_section_backtick_paths(report, "Files updated")
    if "CHUNK_43_REPORT.md" not in created:
        errors.append("CHUNK_43_REPORT.md Files created must list CHUNK_43_REPORT.md")
    if "RELEASE_CANDIDATE_1_INTEGRITY.md" not in created:
        errors.append("CHUNK_43_REPORT.md Files created must list RELEASE_CANDIDATE_1_INTEGRITY.md")
    missing_updated = sorted(CHUNK_43_REQUIRED_UPDATED_FILES - updated)
    if missing_updated:
        errors.append(f"CHUNK_43_REPORT.md Files updated omits required files: {missing_updated}")
    for term in [
        "Release-Candidate Packaging Result",
        "Documented Release-Candidate Limitations",
        "Artifact Hygiene",
        expected_package,
        "AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW",
    ]:
        if term not in report:
            errors.append(f"CHUNK_43_REPORT.md missing required term: {term}")
    if not report.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_43_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")



def validate_chunk_44_final_release_packaging(manifest: dict[str, Any], errors: list[str]) -> None:
    if manifest.get("chunk_gate", {}).get("current_chunk") != "chunk_44":
        return

    expected_package = "vibe-coding-bible-final-release-1-20260612T050000Z-authoritative.zip"
    expected_sidecar = expected_package + ".sha256"
    integrity_rel = "FINAL_RELEASE_1_INTEGRITY.md"
    rc_integrity_rel = "RELEASE_CANDIDATE_1_INTEGRITY.md"
    rc_package = "vibe-coding-bible-release-candidate-1-revision-2-20260612T040000Z-authoritative.zip"

    if manifest.get("active_chunk", {}).get("id") != "chunk_44_final_release_packaging":
        errors.append("manifest.active_chunk.id must be chunk_44_final_release_packaging")
    if manifest.get("next_recommended_chunk", {}).get("id") != "post_release_maintenance_requires_editor_scope":
        errors.append("manifest.next_recommended_chunk.id must be post_release_maintenance_requires_editor_scope for Chunk 44")

    canonical = manifest.get("package", {}).get("canonical_review_package")
    if canonical != expected_package:
        errors.append(f"manifest.package.canonical_review_package must be {expected_package!r}: {canonical!r}")
    for alias_owner_name, alias_owner in [
        ("manifest", manifest),
        ("manifest.package", manifest.get("package", {})),
        ("manifest.artifact_hygiene", manifest.get("artifact_hygiene", {})),
        ("manifest.source_artifacts", manifest.get("source_artifacts", {})),
        ("manifest.active_chunk", manifest.get("active_chunk", {})),
    ]:
        if isinstance(alias_owner, dict) and "canonical_review_package" in alias_owner and alias_owner.get("canonical_review_package") != expected_package:
            errors.append(f"{alias_owner_name}.canonical_review_package must point to final package: {alias_owner.get('canonical_review_package')!r}")
    source_artifacts = manifest.get("source_artifacts", {}) if isinstance(manifest.get("source_artifacts"), dict) else {}
    for alias_key in ("package_file", "review_package"):
        if source_artifacts.get(alias_key) != expected_package:
            errors.append(f"manifest.source_artifacts.{alias_key} must point to final package: {source_artifacts.get(alias_key)!r}")

    readme = read(ROOT / "README.md")
    llms = read(ROOT / "llms.txt")
    llms_full = read(ROOT / "llms-full.txt")
    report_path = ROOT / "CHUNK_44_REPORT.md"
    report = read(report_path) if report_path.exists() else ""
    integrity_path = ROOT / integrity_rel
    integrity = read(integrity_path) if integrity_path.exists() else ""

    for rel, text in [("README.md", readme), ("llms.txt", llms), ("llms-full.txt", llms_full), ("CHUNK_44_REPORT.md", report)]:
        for term in ["Final Release 1", "approved RC gate"]:
            if term not in text:
                errors.append(f"{rel} missing final-release status term: {term}")
    if "## Final Release Package Status" not in readme:
        errors.append("README.md missing Final Release Package Status section")
    if "## Final Release Package Fast Routing" not in llms or "## Final Release Package Fast Routing" not in llms_full:
        errors.append("llms.txt and llms-full.txt must include Final Release Package Fast Routing")
    for rel, text in [("README.md", readme), ("llms.txt", llms), ("llms-full.txt", llms_full)]:
        stale_current_phrases = [
            "This package is **Release Candidate 1**",
            "Release Candidate 1** and is awaiting editor review",
            "it is not a final release",
            "Final release state:** not final",
            "blocked until the editor reviews this Release Candidate 1 package",
        ]
        for phrase in stale_current_phrases:
            if phrase in text:
                errors.append(f"{rel} contains stale current-facing RC/final-release wording: {phrase}")

    final = manifest.get("final_release_packaging", {}) if isinstance(manifest.get("final_release_packaging"), dict) else {}
    if final.get("status") != "final_release_package_produced_waiting_for_editor_review":
        errors.append("manifest.final_release_packaging.status must be final_release_package_produced_waiting_for_editor_review")
    if final.get("final_release_package") != expected_package:
        errors.append("manifest.final_release_packaging.final_release_package must match canonical package")
    if final.get("approved_source_baseline") != rc_package:
        errors.append("manifest.final_release_packaging.approved_source_baseline must point to approved RC package")
    if final.get("integrity_report") != integrity_rel:
        errors.append("manifest.final_release_packaging.integrity_report must point to FINAL_RELEASE_1_INTEGRITY.md")
    if final.get("checksum_sidecar") != expected_sidecar:
        errors.append("manifest.final_release_packaging.checksum_sidecar must point to final .sha256 sidecar")
    if final.get("checksum_sidecar_status") != "external_convention_not_embedded_in_zip":
        errors.append("manifest.final_release_packaging.checksum_sidecar_status must clarify external convention/not embedded in zip")
    if final.get("packaging_only") is not True:
        errors.append("manifest.final_release_packaging.packaging_only must be true")

    rc = manifest.get("release_candidate_packaging", {}) if isinstance(manifest.get("release_candidate_packaging"), dict) else {}
    if rc.get("release_candidate_package") != rc_package:
        errors.append("manifest.release_candidate_packaging.release_candidate_package must preserve approved RC baseline package")
    if rc.get("status") != "release_candidate_1_revision_2_approved_for_final_release_packaging":
        errors.append("manifest.release_candidate_packaging.status must indicate RC approved for final-release packaging")
    if rc.get("final_release_packaging_authorized") is not True:
        errors.append("manifest.release_candidate_packaging.final_release_packaging_authorized must be true")

    hygiene = manifest.get("artifact_hygiene", {}) if isinstance(manifest.get("artifact_hygiene"), dict) else {}
    if hygiene.get("integrity_report") != integrity_rel:
        errors.append("manifest.artifact_hygiene.integrity_report must point to FINAL_RELEASE_1_INTEGRITY.md")
    if hygiene.get("checksum_sidecar") != expected_sidecar:
        errors.append("manifest.artifact_hygiene.checksum_sidecar must point to final .sha256 sidecar")
    if hygiene.get("checksum_sidecar_status") != "external_convention_not_embedded_in_zip":
        errors.append("manifest.artifact_hygiene.checksum_sidecar_status must clarify external convention/not embedded in zip")

    if not integrity_path.exists():
        errors.append(f"{integrity_rel} missing")
    else:
        for term in [expected_package, expected_sidecar, rc_package, "manifest_inventory_sha256", "source_content_manifest_sha256_excluding_this_file", "validator_output"]:
            if term not in integrity:
                errors.append(f"{integrity_rel} missing required integrity term: {term}")
        if "iterating package-relative source-file paths in ascending lexicographic order" not in integrity:
            errors.append(f"{integrity_rel} must describe source-content hash input as path-ordered")
        if "checksum_sidecar_convention" not in integrity:
            errors.append(f"{integrity_rel} must label the sidecar as a convention, not a submitted internal artifact")
        if "submitted sidecar" in integrity.lower() or "submitted `.sha256` sidecar" in integrity.lower():
            errors.append(f"{integrity_rel} must not claim the external sidecar is embedded or submitted inside the source tree")
        governance = manifest.get("public_repository_governance", {}) if isinstance(manifest.get("public_repository_governance"), dict) else {}
        compatibility = governance.get("validator_compatibility", {}) if isinstance(governance.get("validator_compatibility"), dict) else {}
        historical_final_record = compatibility.get("final_release_integrity_records_preserved_as_historical") is True
        observed_inventory_hash = _chunk_43_integrity_table_value(integrity, "manifest_inventory_sha256")
        observed_content_hash = _chunk_43_integrity_table_value(integrity, "source_content_manifest_sha256_excluding_this_file")
        observed_count = _chunk_43_integrity_table_value(integrity, "source_file_count")
        if historical_final_record:
            if observed_inventory_hash != FINAL_RELEASE_1_HISTORICAL_INVENTORY_SHA256:
                errors.append(
                    f"{integrity_rel} historical manifest_inventory_sha256 changed: "
                    f"{observed_inventory_hash!r} != {FINAL_RELEASE_1_HISTORICAL_INVENTORY_SHA256}"
                )
            if observed_content_hash != FINAL_RELEASE_1_HISTORICAL_CONTENT_SHA256:
                errors.append(
                    f"{integrity_rel} historical source_content_manifest_sha256_excluding_this_file changed: "
                    f"{observed_content_hash!r} != {FINAL_RELEASE_1_HISTORICAL_CONTENT_SHA256}"
                )
            if observed_count != FINAL_RELEASE_1_HISTORICAL_SOURCE_FILE_COUNT:
                errors.append(
                    f"{integrity_rel} historical source_file_count changed: "
                    f"{observed_count!r} != {FINAL_RELEASE_1_HISTORICAL_SOURCE_FILE_COUNT}"
                )
        else:
            actual_paths = _chunk_43_actual_source_paths()
            expected_inventory_hash = _chunk_43_manifest_inventory_sha256(actual_paths)
            if observed_inventory_hash != expected_inventory_hash:
                errors.append(
                    f"{integrity_rel} manifest_inventory_sha256 mismatch: "
                    f"{observed_inventory_hash!r} != {expected_inventory_hash}"
                )
            expected_content_hash = _chunk_43_source_content_manifest_sha256({integrity_rel})
            if observed_content_hash != expected_content_hash:
                errors.append(
                    f"{integrity_rel} source_content_manifest_sha256_excluding_this_file mismatch: "
                    f"{observed_content_hash!r} != {expected_content_hash}"
                )
            if observed_count != str(len(actual_paths)):
                errors.append(f"{integrity_rel} source_file_count mismatch: {observed_count!r} != {len(actual_paths)}")

    tree_lines = set(read(ROOT / "TREE.txt").splitlines()) if (ROOT / "TREE.txt").exists() else set()
    manifest_source_files = set(manifest.get("source_files", []) or [])
    for list_name, values in [
        ("manifest.source_files", manifest_source_files),
        ("manifest.source_artifacts.source_files", set(source_artifacts.get("source_files", []) or [])),
        ("manifest.source_artifacts.all_tracked_files", set(source_artifacts.get("all_tracked_files", []) or [])),
        ("manifest.source_artifacts.root_artifacts", set(source_artifacts.get("root_artifacts", []) or [])),
        ("manifest.source_artifacts.root_files", set(source_artifacts.get("root_files", []) or [])),
        ("TREE.txt", tree_lines),
    ]:
        if integrity_rel not in values:
            errors.append(f"{list_name} missing {integrity_rel}")
    if rc_integrity_rel not in manifest_source_files:
        errors.append("approved RC integrity record must remain in manifest.source_files")

    limits_terms = [
        "exact non-OpenAI pricing",
        "curated",
        "52 active tool cards",
        "23 deferred/planned ecosystem IDs",
        "candidate-only",
        "changelog ordering",
    ]
    manifest_text = json.dumps(manifest, sort_keys=True)
    for term in limits_terms:
        if term not in readme and term not in report and term not in manifest_text:
            errors.append(f"final-release documented limitation missing across README/report/manifest: {term}")

    tool_counts = _register_status_counts(ROOT / "TOOL_REGISTER.md", "tool.")
    shortcut_counts = _register_status_counts(ROOT / "SHORTCUT_REGISTER.md", "vcb.shortcut.")
    field_counts = _register_status_counts(ROOT / "FIELD_PRACTICES.md", "vcb.field.")
    pricing_counts = _pricing_snapshot_status_counts()
    expected_counts = {
        "active_tool_cards": 52,
        "deferred_planned_tool_ids": 23,
        "active_shortcut_cards": 50,
        "planned_shortcut_cards": 48,
        "candidate_field_practices": 9,
        "active_pricing_snapshots": 1,
        "deferred_pricing_snapshots": 4,
    }
    observed_counts = {
        "active_tool_cards": int(tool_counts.get("active", 0)),
        "deferred_planned_tool_ids": int(tool_counts.get("deferred_planned", 0)),
        "active_shortcut_cards": int(shortcut_counts.get("active", 0)),
        "planned_shortcut_cards": int(shortcut_counts.get("planned", 0)),
        "candidate_field_practices": int(field_counts.get("candidate", 0)),
        "active_pricing_snapshots": int(pricing_counts.get("active_snapshot", 0)),
        "deferred_pricing_snapshots": int(pricing_counts.get("deferred", 0)),
    }
    # The final-release register snapshot is historical; post-release
    # maintenance may change the live register counts without mutating that
    # frozen release record.
    for key, expected in expected_counts.items():
        if final.get("register_snapshot", {}).get(key) != expected:
            errors.append(f"manifest.final_release_packaging.register_snapshot.{key} mismatch: {final.get('register_snapshot', {}).get(key)!r} != {expected}")

    scope_boundary = str(manifest.get("validation_expectations", {}).get("current_chunk_scope_boundaries", ""))
    for term in [
        "Chunk 44",
        "Final Release 1 packaging only",
        "No new tool cards",
        "No field-practice cards",
        "No shortcut cards",
        "No pricing snapshots",
        "No broad workflow expansion",
        "No broad security/secrets expansion",
        "No broad tool-catalog expansion",
        "No source-map migration",
        "No narrative chapters",
    ]:
        if term not in scope_boundary:
            errors.append(f"manifest.validation_expectations.current_chunk_scope_boundaries missing Chunk 44 term: {term}")

    if not report_path.exists():
        errors.append("CHUNK_44_REPORT.md missing")
        return
    created = report_section_backtick_paths(report, "Files created")
    updated = report_section_backtick_paths(report, "Files updated")
    if "CHUNK_44_REPORT.md" not in created:
        errors.append("CHUNK_44_REPORT.md Files created must list CHUNK_44_REPORT.md")
    if integrity_rel not in created:
        errors.append("CHUNK_44_REPORT.md Files created must list FINAL_RELEASE_1_INTEGRITY.md")
    required_updated = {"README.md", "manifest.json", "llms.txt", "llms-full.txt", "SOURCE_REGISTER.md", "CHANGELOG.md", "TREE.txt", "scripts/validate_repository.py"}
    missing_updated = sorted(required_updated - updated)
    if missing_updated:
        errors.append(f"CHUNK_44_REPORT.md Files updated omits required files: {missing_updated}")
    for term in [
        "Final-Release Packaging Result",
        "Documented Final-Release Limitations",
        "Artifact Hygiene",
        expected_package,
        rc_package,
        "AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW",
    ]:
        if term not in report:
            errors.append(f"CHUNK_44_REPORT.md missing required term: {term}")
    if not report.rstrip().endswith("AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW"):
        errors.append("CHUNK_44_REPORT.md must end with AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW")


def main() -> int:
    errors: list[str] = []

    manifest = json.loads(read(ROOT / "manifest.json"))
    actual = actual_source_paths()
    listed = manifest_source_paths(manifest)
    if actual != listed:
        missing = sorted(set(actual) - set(listed))
        extra = sorted(set(listed) - set(actual))
        errors.append(f"manifest inventory mismatch: actual={len(actual)} listed={len(listed)} missing={missing} extra={extra}")
    validate_nested_manifest_inventory(manifest, actual, listed, errors)
    validate_manifest_package_counts(manifest, actual, listed, errors)
    validate_canonical_package_references(manifest, errors)
    validate_current_chunk_status_metadata(manifest, errors)

    declared_roots = set(manifest["topic_namespace_policy"].get("canonical_topic_namespaces", {}))
    declared_roots |= set(manifest["topic_namespace_policy"].get("non_topic_namespaces", {}))
    active_ids = authored_active_ids()
    for path in (ROOT / "indexes").glob("*.md"):
        text = read(path)
        for ident in VCB_INDEX_ID_RE.findall(text):
            if id_root(ident) not in declared_roots:
                errors.append(f"undeclared namespace root for index ID {ident} in {path.relative_to(ROOT)}")
        for line in text.splitlines():
            if re.search(r"→\s*active(?:\s|$|:)", line):
                for ident in VCB_INDEX_ID_RE.findall(line):
                    if ident not in active_ids:
                        errors.append(f"active index route does not point to authored ID: {ident} in {path.relative_to(ROOT)}")

    schemas: dict[Path, dict[str, Any]] = {}
    for p in (ROOT / "schemas").glob("*.schema.json"):
        schema = resolve_schema(p)
        jsonschema.Draft202012Validator.check_schema(schema)
        schemas[p] = schema

    for path in active_topic_files():
        fm = parse_frontmatter(path)
        if fm is None:
            errors.append(f"missing frontmatter: {path.relative_to(ROOT)}")
            continue
        for schema_path in schema_paths_for(fm):
            schema = schemas[schema_path]
            validator_schema = local_overlay_schema(schema) if schema_path.name == "chapter.schema.json" else schema
            jsonschema.Draft202012Validator(validator_schema).validate(fm)
        validate_markdown_contract(path, fm, errors)

    shortcut_ids = shortcut_register_ids()
    for path in active_topic_files():
        fm = parse_frontmatter(path) or {}
        for shortcut_id in fm.get("shortcut_profiles", []) or []:
            if shortcut_id not in shortcut_ids:
                errors.append(f"unregistered shortcut profile {shortcut_id} in {path.relative_to(ROOT)}")

    index_shortcuts = set()
    for path in (ROOT / "indexes").glob("*.md"):
        index_shortcuts.update(re.findall(r"`(vcb\.shortcut\.[A-Za-z0-9_.-]+)`", read(path)))
    missing_shortcuts = sorted(index_shortcuts - shortcut_ids)
    if missing_shortcuts:
        errors.append(f"shortcut index routes missing from register: {missing_shortcuts}")

    if not table_shape_ok():
        errors.append("SHORTCUT_REGISTER table row shape failed")
    validate_shortcut_register_table_placement(errors)

    source_ids = source_register_ids()
    for path in active_topic_files():
        for sid in evidence_ids(path):
            if sid not in source_ids:
                errors.append(f"evidence source ID not in SOURCE_REGISTER: {sid} in {path.relative_to(ROOT)}")

    tool_ids = tool_register_ids()
    unresolved_index_tools = sorted(index_tool_ids() - tool_ids)
    if unresolved_index_tools:
        errors.append(f"tool IDs in indexes missing from TOOL_REGISTER: {unresolved_index_tools}")

    noncanonical_browser_tool = "tool." + "codex_app_browser"
    current_report_candidate = ROOT / f"CHUNK_{chunk_number_from(manifest.get('chunk_gate', {}).get('current_chunk', ''))}_REPORT.md"
    if noncanonical_browser_tool in index_tool_ids() or noncanonical_browser_tool in report_tool_ids(current_report_candidate):
        errors.append("noncanonical app-browser tool ID is present; use tool.codex_browser or declare an alias policy")

    current_chunk, report = validate_root_governance(manifest, errors)
    validate_readme_next_chunk_route(manifest, errors)
    validate_manifest_redirect_consistency(manifest, errors)
    validate_markdown_begin_marker_frontmatter_versions(errors)
    validate_vcb_marker_pairing_and_index_terminals(errors)
    validate_vcb_begin_end_pairs(errors)
    validate_index_terminal_signposts(errors)
    validate_source_register_table_placement(errors)
    validate_markdown_terminal_end_content(manifest, errors)
    validate_no_live_markdown_after_vcb_end_markers(errors)
    validate_changelog_end_boundary(manifest, errors)
    validate_duplicate_codex_feature_full_list_sections(errors)
    validate_duplicate_workflow_prompting_full_list_sections(errors)
    validate_duplicate_review_safety_full_list_sections(errors)
    validate_duplicate_frontend_refactor_dependency_full_list_sections(errors)
    validate_duplicate_failure_mode_full_list_sections(errors)
    validate_chunk_18_per_index_route_surfaces(manifest, errors)
    validate_chunk_18_failure_mode_index_semantics(manifest, errors)
    validate_chunk_18_source_map_and_report_truth(manifest, errors)
    validate_index_status_and_chunk_headings(manifest, errors)
    validate_llms_source_maps(manifest, errors)
    validate_chapter_33_playbooks(errors)
    unresolved_report_sources = sorted(report_source_ids(report) - source_ids)
    if unresolved_report_sources:
        errors.append(f"source IDs in active chunk report missing from SOURCE_REGISTER: {unresolved_report_sources}")
    unresolved_report_tools = sorted(report_tool_ids(report) - tool_ids)
    if unresolved_report_tools:
        errors.append(f"tool IDs in active chunk report missing from TOOL_REGISTER: {unresolved_report_tools}")

    source_dupes = duplicate_register_ids(ROOT / "SOURCE_REGISTER.md")
    shortcut_dupes = duplicate_register_ids(ROOT / "SHORTCUT_REGISTER.md")
    tool_dupes = duplicate_register_ids(ROOT / "TOOL_REGISTER.md")
    if source_dupes:
        errors.append(f"duplicate source IDs in SOURCE_REGISTER: {sorted(source_dupes)}")
    if shortcut_dupes:
        errors.append(f"duplicate shortcut IDs in SHORTCUT_REGISTER: {sorted(shortcut_dupes)}")
    if tool_dupes:
        errors.append(f"duplicate tool IDs in TOOL_REGISTER: {sorted(tool_dupes)}")

    duplicate_urls = duplicate_source_urls()
    if duplicate_urls:
        errors.append(f"duplicate source URLs in SOURCE_REGISTER: {duplicate_urls}")

    validate_pricing_snapshot_routes(manifest, errors)
    validate_pricing_snapshots(errors)
    validate_source_status_official_vendor(errors)
    validate_source_status_official_openai(errors)
    validate_source_register_chunk13_table(errors)
    validate_feature_flag_metadata(errors)
    validate_field_practice_register(errors)
    validate_chunk_13_concept_slice(manifest, errors)
    validate_chunk_14_codex_feature_slice(manifest, errors)
    validate_chunk_15_workflow_prompting_slice(manifest, errors)
    validate_chunk_16_review_safety_slice(manifest, errors)
    validate_chunk_17_frontend_refactor_dependency_slice(manifest, errors)
    validate_chunk_18_failure_mode_slice(manifest, errors)
    validate_chunk_19_constraint_budget_slice(manifest, errors)
    validate_chunk_20_shortcut_slice(manifest, errors)
    validate_chunk_21_security_permission_shortcut_slice(manifest, errors)
    validate_chunk_22_process_setup_shortcut_slice(manifest, errors)
    validate_chunk_23_tool_sprawl_skill_shortcut_slice(manifest, errors)
    validate_chunk_24_multi_ai_model_bias_shortcut_slice(manifest, errors)
    validate_chunk_25_parallel_cloud_automation_shortcut_slice(manifest, errors)
    validate_chunk_26_repository_contract_cleanup(manifest, errors)
    validate_chunk_27_codex_primary_tool_cards(manifest, errors)
    validate_chunk_28_codex_adjunct_tool_cards(manifest, errors)
    validate_chunk_29_codex_customization_control_tool_cards(manifest, errors)
    validate_chunk_30_codex_security_tool_card(manifest, errors)
    validate_chunk_31_codex_governance_tool_cards(manifest, errors)
    validate_chunk_32_repo_ci_dependency_quality_tool_cards(manifest, errors)
    validate_chunk_33_ai_coding_ide_planning_tool_cards(manifest, errors)
    validate_chunk_34_browser_app_builder_ui_tool_cards(manifest, errors)
    validate_chunk_35_hosting_backend_auth_payment_observability_tool_cards(manifest, errors)
    validate_chunk_36_local_dev_design_project_management_tool_cards(manifest, errors)
    validate_chunk_37_tool_catalog_routing_cleanup(manifest, errors)
    validate_chunk_38_field_practice_candidate_cards(manifest, errors)
    validate_chunk_39_field_practice_llm_cleanup(manifest, errors)
    validate_chunk_40_tool_catalog_coverage_gap_audit(manifest, errors)
    validate_chunk_41_finalization_readiness_audit(manifest, errors)
    validate_chunk_42_release_candidate_disposition_cleanup(manifest, errors)
    validate_chunk_43_release_candidate_packaging(manifest, errors)
    validate_chunk_44_final_release_packaging(manifest, errors)
    validate_chunk_19_report_inventory(manifest, errors)
    validate_chunk_20_report_inventory(manifest, errors)
    validate_chunk_21_report_inventory(manifest, errors)
    validate_chunk_22_report_inventory(manifest, errors)
    validate_chunk_23_report_inventory(manifest, errors)
    validate_chunk_24_report_inventory(manifest, errors)
    validate_chunk_25_report_inventory(manifest, errors)
    # Chunk 26 report claims and inventory are validated inside its repository-contract cleanup check.
    validate_chunk_17_task_index_atomic_routes(manifest, errors)
    validate_chunk_18_task_index_atomic_routes(manifest, errors)
    validate_chunk_14_report_claims(manifest, report, errors)
    validate_chunk_15_report_claims(manifest, report, errors)
    validate_chunk_16_report_claims(manifest, report, errors)
    validate_chunk_17_report_claims(manifest, report, errors)
    validate_chunk_18_report_claims(manifest, report, errors)
    validate_chunk_19_report_claims(manifest, report, errors)
    validate_chunk_19_report_file_inventory(manifest, errors)
    # Chunk 20 and Chunk 21 report claims are validated inside their report-inventory checks.

    report_name = report.name
    if not report.exists():
        errors.append(f"{report_name} missing")
    elif read(report).splitlines()[-1] != "AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW":
        errors.append(f"{report_name} missing terminal author marker")

    if errors:
        for err in errors:
            print(f"ERROR: {err}")
        return 1

    print("VCB validation passed")
    print(f"active chapter/topic files validated: {len(active_topic_files())}")
    print(f"shortcut IDs registered: {len(shortcut_ids)}")
    print(f"tool IDs registered: {len(tool_ids)}")
    print(f"pricing snapshots active: {len(manifest.get('active_pricing_snapshot_ids', []) or [])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
