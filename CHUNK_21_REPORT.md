<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_21 version=0.22.0-draft.chunk21 -->
---
id: vcb.chunk_report.chunk_21
title: CHUNK_21_REPORT
artifact_type: chunk_report
chunk_id: chunk_21_security_permission_shortcut_topic_cards
version: 0.22.0-draft.chunk21
status: waiting_for_editor_review
created_on: '2026-06-10'
last_verified: '2026-06-10'
next_review_due: '2026-07-10'
review_cadence: monthly
---

# Chunk 21 Report — Security and Permission Shortcut Topic Cards

## Chunk ID

`chunk_21_security_permission_shortcut_topic_cards`

## Scope completed

Bounded security and permission shortcut harm-reduction topic-card expansion focused on production GUI actions, broad CI permissions, secrets-adjacent shortcuts, approval bypasses, unattended mutation, and real credentials in prototypes/cloud work.

## Files created

- `CHUNK_21_REPORT.md`
- `topics/shortcuts/production-console-computer-use.md`
- `topics/shortcuts/overbroad-ci-permissions.md`
- `topics/shortcuts/long-lived-ci-secrets.md`
- `topics/shortcuts/real-secrets-in-prototype.md`
- `topics/shortcuts/cloud-work-with-real-secrets.md`
- `topics/shortcuts/full-access-automation.md`
- `topics/shortcuts/unattended-mutation.md`
- `topics/shortcuts/always-allow-sensitive-apps.md`

## Files updated

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
- `SHORTCUT_REGISTER.md`
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

Chunk 21 uses existing official OpenAI/Codex, GitHub Actions, OWASP, and VCB synthesis source IDs, plus the editor-feedback gate source `vcb.register.editor_feedback_chunk_20`. Product mechanics, UI labels, permission defaults, and secret-management behavior are treated as volatile.

## Validation summary

Ran `python scripts/validate_repository.py` before packaging and again after extracting the submitted package.

### Machine-enforced checks

- New security/permission shortcut topic files created in Chunk 21: passed
- Required Chunk 21 security/permission shortcut-card slice present: passed
- Manifest security_permission_shortcut_cards map matches authored Chunk 21 files: passed
- Manifest chunk_21_required_topic_ids matches authored Chunk 21 IDs: passed
- Required VCB markers present in new Chunk 21 shortcut files: passed
- Required sections present in new Chunk 21 shortcut files: passed
- SHORTCUT_REGISTER marks authored Chunk 21 shortcut IDs active: passed
- SHORTCUT_REGISTER shortcut rows are inside declared shortcut tables: passed
- Primary indexes route active Chunk 21 security/permission shortcut cards: passed
- Prompt library routes active Chunk 21 security/permission shortcut cards: passed
- AI coach index routes active Chunk 21 security/permission shortcut cards: passed
- LLM source maps route active Chunk 21 security/permission shortcut cards: passed
- Manifest current-chunk validation metadata names Chunk 21: passed
- Generic LLM shortcut route covers active Chunk 20 and Chunk 21 shortcut-card slices: passed
- Risk-level semantic sections route active Chunk 21 security/permission cards: passed
- Shortcut semantic sections route active Chunk 21 cards before planned near-duplicate companions: passed
- Task, failure-mode, and AI-coach semantic routes include Chunk 21 cards: passed
- Stale planned routes for authored Chunk 21 shortcuts are absent from indexes and SHORTCUT_REGISTER: passed
- Chunk 21 did not start full shortcut expansion or disallowed topic-card families: passed
- Chunk 21 report/changelog routing claims match routed surfaces: passed
- Active Chunk 21 report inventory lists created shortcut cards and updated routing/governance files: passed
- No single index section contains duplicate active Chunk 21 shortcut rows: passed
- Active Chunk 21 machine-claim catalog matches validator checks: passed


## Revision note

Chunk 21 revision repaired stale root and retrieval governance defects: manifest.validation_expectations.current_chunk_checks now names Chunk 21; generic shortcut retrieval in `llms.txt` and `llms-full.txt` now routes across active Chunk 20 and Chunk 21 shortcut-card slices; `INDEX_BY_RISK_LEVEL.md` and `INDEX_BY_SHORTCUT.md` now route security/permission lookup paths to active Chunk 21 cards before planned near-duplicate companion routes; validator coverage was tightened for all four defect classes.

## Scope boundaries preserved

Chunk 21 did not start full shortcut-card expansion, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_22_process_setup_shortcut_topic_cards`.

## Unresolved questions

None.

## Packaging expectation

Submit one timestamped authoritative zip and checksum after validator and extracted-package verification.

<!-- VCB:STOP_RETRIEVAL reason="chunk_21_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_21 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
