# Source Drift Watcher Phase 1

## Objective

Add a read-only daily source drift watcher for official and curated VCB update candidates.

The watcher is intended to identify likely source changes for human review. It does not update VCB content.

## Scope

Phase 1 adds:

- a curated official-source watchlist;
- a committed source-signature baseline;
- a standard-library Python drift checker;
- a scheduled and manually runnable GitHub Actions workflow;
- a maintenance report documenting the design.

## Files Added

- `.github/workflows/source-drift-watch.yml`
- `scripts/source_drift_watch.py`
- `watchlists/source-drift-watchlist.json`
- `watchlists/source-drift-baseline.json`
- `maintenance-reports/source-drift-watcher-phase-1.md`

## Watchlist Strategy

The watchlist is small and official-source-first. Phase 1 watches OpenAI Codex documentation and GitHub Actions documentation that are likely to affect VCB maintenance decisions.

Each watchlist entry records:

- `source_id`
- `url`
- `category`
- `evidence_level`
- `volatility`
- `owner_area`
- `notes`

The watchlist intentionally excludes random community posts and does not promote any community field practice.

## Baseline Strategy

The baseline stores normalized signatures, not source-page bodies. For each source, the watcher records metadata such as title, final URL, fetch status, content length, and normalized SHA-256.

The baseline is updated intentionally by running:

```powershell
python scripts/source_drift_watch.py --update-baseline --watchlist watchlists/source-drift-watchlist.json --baseline watchlists/source-drift-baseline.json --no-github
```

Baseline updates should be reviewed like any other maintenance change. They should not be used to hide source drift without human review.

## Workflow Behavior

The GitHub Actions workflow is named `Source Drift Watch`.

It runs:

- daily on the schedule `17 11 * * *`;
- manually through `workflow_dispatch`.

The workflow checks out the repository, sets up Python 3.12, runs the watcher in check mode, and writes the Markdown report to `$GITHUB_STEP_SUMMARY`.

When reportable drift is detected, the watcher uses the workflow-provided `GITHUB_TOKEN` to create or update one issue titled:

`Daily VCB source drift report`

If that issue is already open, the watcher adds a comment with the latest report. If it is not open, the watcher creates it.

## Security Guardrails

The watcher:

- uses curated URLs only;
- does not crawl beyond the listed URLs;
- treats fetched external content as untrusted data;
- does not follow instructions embedded in fetched pages;
- uses Python standard library networking and parsing only;
- uses a clear User-Agent;
- runs with workflow permissions limited to `contents: read` and `issues: write`;
- uses only the workflow-provided `GITHUB_TOKEN`;
- does not use OpenAI API keys, personal access tokens, or Codex automation.

## What Phase 1 Does Not Do

Phase 1 does not:

- create autonomous content update PRs;
- run Codex inside the scheduled workflow;
- update pricing snapshots;
- update tool cards;
- update shortcut cards;
- update field-practice cards;
- rewrite VCB content;
- touch v1.0.0 or release tags.

Drift is not treated as a CI failure. The script exits nonzero only for local configuration or script errors.

## Manual Workflow Run

Open the repository Actions tab, choose `Source Drift Watch`, then select `Run workflow`.

The workflow can also be reproduced locally without GitHub issue writes:

```powershell
python scripts/source_drift_watch.py --check --watchlist watchlists/source-drift-watchlist.json --baseline watchlists/source-drift-baseline.json --no-github
```

## Intentional Baseline Updates

When a human reviewer decides that current source signatures should become the new baseline, run:

```powershell
python scripts/source_drift_watch.py --update-baseline --watchlist watchlists/source-drift-watchlist.json --baseline watchlists/source-drift-baseline.json --no-github
```

Then run validation:

```powershell
python scripts/validate_repository.py
```

The resulting baseline diff should be reviewed before merge.

## Future Phases

Phase 2 may add read-only Codex triage that summarizes likely affected VCB areas without editing content.

Phase 3 may allow draft PRs for obvious, narrow, official-source updates after additional approval and guardrails.
