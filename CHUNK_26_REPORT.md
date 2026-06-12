<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_26 version=0.27.0-draft.chunk26 -->
---
id: vcb.chunk_report.chunk_26
title: Chunk 26 Report — Repository-Contract Cleanup
artifact_type: chunk_report
version: 0.27.0-draft.chunk26
status: waiting_for_editor_review
chunk_id: chunk_26_editor_scoped_next_slice
last_verified: '2026-06-10'
---

# Chunk 26 Report — Repository-Contract Cleanup

## Scope

Chunk 26 performed repository-contract cleanup only. The bounded scope was glossary route hardening plus planned-alias/deprecation policy cleanup for existing active cards. No new topic cards, tool cards, field-practice cards, pricing snapshots, broad workflow expansion, broad shortcut expansion, or narrative chapters were authored.

## Created files

- `CHUNK_26_REPORT.md`

## Updated files

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SHORTCUT_REGISTER.md`
- `DEPRECATION_REGISTER.md`
- `CHANGELOG.md`
- `TREE.txt`
- `chapters/19-codex-config.md`
- `chapters/27-cloud-delegation-parallel-work.md`
- `chapters/30-computer-use-browser-gui-tasks.md`
- `topics/codex/app.md`
- `topics/codex/cloud.md`
- `topics/codex/config.md`
- `topics/codex/computer-use.md`
- `topics/codex/subagents.md`
- `topics/failure-modes/ui-taste-gap.md`
- `topics/workflows/frontend-work.md`
- `topics/workflows/visual-qa.md`
- `indexes/GLOSSARY.md`
- `indexes/INDEX_BY_SHORTCUT.md`
- `scripts/validate_repository.py`

## Cleanup performed

- Repaired glossary limitation/bias routes so optimism bias, completion bias, plausibility bias, AI agreement, answer-shopping, done claims, and hallucinated APIs route to active atomic cards before chapter fallbacks.
- Added explicit shortcut alias/deprecation routing policy to `SHORTCUT_REGISTER.md` and `DEPRECATION_REGISTER.md`.
- Hardened planned alias replacements for existing active cards, including `vcb.shortcut.using_global_config_for_everything` → `vcb.shortcut.default_config_forever`, `vcb.shortcut.parallel_agents_same_files` → `vcb.shortcut.many_ais_same_files`, `vcb.shortcut.parallel_tasks_same_files` → `vcb.shortcut.parallel_agents_edit_same_files`, and `vcb.shortcut.screenshot_only_verification` → `vcb.shortcut.browser_clicking_without_repro`.
- Replaced redirected shortcut aliases in active chapter/topic metadata with canonical active shortcut IDs for the hardened alias set.
- Updated LLM maps so alias/deprecation and glossary-bias retrieval has a current Chunk 26 route.

## Revision note — reserved redirect repair

- Replaced false self-redirect rows in `DEPRECATION_REGISTER.md` with manifest-backed old-ID → canonical-ID redirects.
- Verified reserved redirect rows now match the manifest redirect map and do not redirect an ID to itself.
- Tightened `scripts/validate_repository.py` to reject deprecation-register self-redirect rows and reserved redirect rows that are missing from or contradictory to the manifest redirect map.

## Source posture

Chunk 26 added no new product facts and no new external source claims. No source-register rows were added. Existing source posture from prior chunks is preserved.

## Validation

### Machine-enforced checks
- Chunk 26 repository-contract cleanup scope is active: passed
- README and manifest identify Chunk 26 cleanup and block Chunk 27 until editor scope: passed
- Glossary limitation/bias terms route to active atomic shortcut/failure cards: passed
- Shortcut alias/deprecation register policy covers manifest shortcut redirects to active cards: passed
- Deprecation-register reserved redirect rows are non-self and manifest-backed: passed
- Active routing surfaces show canonical active shortcut replacements before redirected planned aliases: passed
- Active chapter/topic metadata avoids redirected shortcut aliases for the hardened alias set: passed
- LLM maps expose current Chunk 26 repository-contract cleanup routing: passed
- Chunk 26 did not add topic-card, tool-card, field-practice, pricing, broad workflow, broad shortcut, or narrative-chapter expansion: passed
- CHANGELOG.md has one current-chunk heading for Chunk 26: passed
- Active Chunk 26 report inventory lists created and updated repository-contract files: passed
- Active Chunk 26 machine-claim catalog matches validator checks: passed

## Scope boundary

Chunk 26 did not start new topic-card expansion, full shortcut-card expansion, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_27_editor_scoped_next_slice`.

## Unresolved questions

None.

<!-- VCB:STOP_RETRIEVAL reason="chunk_26_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_26 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
