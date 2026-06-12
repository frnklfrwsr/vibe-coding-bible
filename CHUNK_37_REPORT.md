<!-- VCB:BEGIN_REPORT id=vcb.report.chunk_37 version=0.38.0-draft.chunk37 -->
---
id: vcb.report.chunk_37
title: Chunk 37 Report — Tool-Catalog Routing Consolidation Cleanup
artifact_type: chunk_report
version: 0.38.0-draft.chunk37
status: waiting_for_editor_review
chunk_id: chunk_37_tool_catalog_routing_consolidation_cleanup
last_verified: '2026-06-11'
---

# Chunk 37 Report — Tool-Catalog Routing Consolidation Cleanup

## Scope

Chunk 37 performed bounded repository-contract cleanup only after the tool-card expansion run.

In scope:

- consolidate/normalize active tool-card inventories;
- preserve semantic routes that point to the smallest active tool card before chapter/workflow/fallback routes;
- repair duplicate semantic route rows in targeted sections;
- clarify generic LLM tool-routing lines where “tool/surface,” “prototype,” or “production readiness” could otherwise bypass active tool cards;
- add missing glossary companion routes for generic CI, Codex PR review, non-interactive Codex, auth, authorization, and observability terms;
- canonicalize source-register URLs that redirect to official vendor destinations;
- tighten validator checks for these repository-contract classes.

Out of scope and not started:

- new tool cards;
- category placeholder cards;
- email/documentation/security-secrets tool-category cards;
- field-practice-card expansion;
- pricing snapshots or pricing expansion;
- shortcut-card expansion;
- broad workflow expansion;
- broad security/secrets expansion;
- narrative chapters.

## Created files

- `CHUNK_37_REPORT.md`

## Updated files

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
- `TOOL_REGISTER.md`
- `CHANGELOG.md`
- `TREE.txt`
- `scripts/validate_repository.py`
- `indexes/GLOSSARY.md`
- `indexes/INDEX_BY_BUDGET_PROFILE.md`
- `indexes/INDEX_BY_CODEX_SURFACE.md`
- `indexes/INDEX_BY_CONCEPT.md`
- `indexes/INDEX_BY_FAILURE_MODE.md`
- `indexes/INDEX_BY_PROJECT_TYPE.md`
- `indexes/INDEX_BY_RECOVERABILITY.md`
- `indexes/INDEX_BY_RISK_LEVEL.md`
- `indexes/INDEX_BY_SHORTCUT.md`
- `indexes/INDEX_BY_STABILITY.md`
- `indexes/INDEX_BY_TASK.md`
- `indexes/INDEX_BY_TOOL_CATEGORY.md`
- `indexes/INDEX_FOR_AI_COACHES.md`
- `indexes/PROMPT_LIBRARY.md`

## Source posture

Chunk 37 added no new product facts, pricing facts, feature-availability claims, or tool cards. It added the Chunk 37 editor-gate source row and canonicalized existing official-source URLs that had begun redirecting:

- Windsurf/Devin source rows now use official docs.devin.ai destinations while preserving stable `windsurf.docs.*` source IDs.
- v0 source rows now use official v0.app destinations while preserving stable `v0.docs.*` source IDs.

Existing source IDs remain stable so authored cards do not need evidence-ID churn.

## Repository routing and governance changes

- `README.md` now exposes one consolidated `## Active Tool Cards` section instead of generation-specific active tool-card inventory blocks.
- Primary indexes no longer keep append-only generation-specific aggregate tool-card inventory blocks; semantic routes remain in place and `INDEX_BY_TOOL_CATEGORY.md` now states the tool-card inventory policy.
- `indexes/GLOSSARY.md` now adds active tool-card companions for CI, Codex PR review, non-interactive Codex, authentication, authorization, and observability while preserving concept-first routing where appropriate.
- `indexes/INDEX_BY_PROJECT_TYPE.md` / `## Team or shared repo` no longer repeats `tool.github` and `tool.github_actions` route rows.
- `llms.txt` and `llms-full.txt` now clarify when “Codex surface” means execution surface, when prototype phase should route to app-builder tools, and when production readiness should route to platform evidence tools.
- `SOURCE_REGISTER.md` now records canonical official redirect destinations for Windsurf/Devin and v0 docs.
- `manifest.json` records Chunk 37 cleanup scope, canonical package metadata, source inventory, and next-chunk gate state.

## Validator coverage added

`scripts/validate_repository.py` was tightened for Chunk 37 repository-contract coverage, including:

- no new tool-card or pricing-snapshot expansion in cleanup-only scope;
- README consolidated active tool-card inventory contains all active tool IDs and no generation-specific tool-card inventory headings;
- indexes contain no generation-specific aggregate active tool-card inventory blocks;
- `INDEX_BY_TOOL_CATEGORY.md` contains the new inventory policy;
- targeted duplicate semantic route rows are rejected;
- glossary companion routes for CI, Codex PR review, non-interactive Codex, authentication, authorization, and observability are checked;
- LLM source-map routes distinguish Codex execution-surface selection, prototype/app-builder choice, and production-readiness tool evidence;
- SOURCE_REGISTER.md rejects old redirected Windsurf/Devin and v0 URLs in favor of verified canonical official destinations;
- report inventory coverage and package counts.

## Revision notes

- Merged duplicate `security review` glossary routes into one smallest-active-route line with `vcb.safety.security_review`, `tool.codex_security`, and `vcb.chapter.security_for_vibe_coders` fallback routing.
- Removed the duplicate bare `vcb.prompting.acceptance_criteria` route in `indexes/INDEX_BY_CONCEPT.md` while preserving the descriptive evidence-backed route.
- Tightened `scripts/validate_repository.py` so duplicate security-review glossary labels and duplicate acceptance-criteria concept route rows fail validation.

## Validation

Final validator result:

```text
VCB validation passed
active chapter/topic files validated: 221
shortcut IDs registered: 98
tool IDs registered: 46
pricing snapshots active: 1
```

## Package hygiene

Authoritative package:

```text
vibe-coding-bible-chunk-37-revision-20260611T190000Z-authoritative.zip
```

Package hygiene:

```text
zip entries: 309
unique entries: 309
duplicates: 0
directory-only entries: 0
__pycache__ / .pyc entries: 0
files extracted: 309
```

## Notes for editor

Chunk 37 deliberately avoids new content-card expansion. The cleanup converts append-only tool-card inventory behavior into a repository-contract pattern: canonical inventory lives in `TOOL_REGISTER.md` and `README.md`, while indexes are responsible for semantic smallest-active-card routing.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.report.chunk_37 -->

AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
