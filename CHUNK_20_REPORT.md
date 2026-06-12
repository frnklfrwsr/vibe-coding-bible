<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_20 version=0.21.0-draft.chunk20 -->
---
id: vcb.chunk_report.chunk_20
title: CHUNK_20_REPORT
artifact_type: chunk_report
chunk_id: chunk_20_shortcut_harm_reduction_topic_cards
version: 0.21.0-draft.chunk20
status: waiting_for_editor_review
created_on: '2026-06-09'
last_verified: '2026-06-09'
next_review_due: '2026-07-09'
review_cadence: monthly
---

# Chunk 20 Report — Shortcut Harm-Reduction Topic Cards

## Chunk ID

`chunk_20_shortcut_harm_reduction_topic_cards`

## Scope completed

Bounded shortcut harm-reduction topic-card expansion for the highest-risk registered shortcuts approved for this slice: skipping tests, accepting “looks done,” broad agent permissions, unattended long runs, broad refactor, context dumping, adding dependencies fast, and reviewing cloud summaries only.

## Revision note

Revision 1 repairs `SHORTCUT_REGISTER.md` table placement by moving the dangling planned shortcut rows into a declared shortcut-route table with a full header. The validator now fails if any `vcb.shortcut.*` register row appears outside a declared shortcut table, if shortcut table rows have the wrong cell count, or if shortcut rows resume after a blank/prose break without a new heading and table header.

## Files created

- `CHUNK_20_REPORT.md` — current chunk report for bounded shortcut harm-reduction topic-card expansion
- `topics/shortcuts/skipping-tests.md` — `vcb.shortcut.skipping_tests`
- `topics/shortcuts/accepting-looks-done.md` — `vcb.shortcut.accepting_looks_done`
- `topics/shortcuts/broad-agent-permissions.md` — `vcb.shortcut.broad_agent_permissions`
- `topics/shortcuts/unattended-long-runs.md` — `vcb.shortcut.unattended_long_runs`
- `topics/shortcuts/broad-refactor.md` — `vcb.shortcut.broad_refactor`
- `topics/shortcuts/context-dumping.md` — `vcb.shortcut.context_dumping`
- `topics/shortcuts/adding-dependencies-fast.md` — `vcb.shortcut.adding_dependencies_fast`
- `topics/shortcuts/reviewing-cloud-summary-only.md` — `vcb.shortcut.reviewing_cloud_summary_only`

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

## Source anchors used

- `vcb.register.editor_feedback_chunk_19`
- `openai.codex.best_practices`
- `openai.codex.workflows`
- `openai.codex.app_review`
- `openai.codex.agent_approvals_security`
- `openai.codex.sandboxing`
- `openai.codex.noninteractive`
- `openai.codex.app_worktrees`
- `openai.codex.use_cases.follow_goals`
- `openai.codex.use_cases.refactor_your_codebase`
- `openai.codex.prompting`
- `openai.codex.subagent_concepts`
- `openai.codex.use_cases.dependency_incident_audits`
- `openai.codex.cloud`
- `martin_fowler.refactoring`
- `vcb.synthesis.stable_engineering_practice`

### Machine-enforced checks

- New shortcut harm-reduction topic files created in Chunk 20: passed
- Required Chunk 20 shortcut-card slice present: passed
- Manifest shortcut_harm_reduction_cards map matches authored Chunk 20 files: passed
- Manifest chunk_20_required_topic_ids matches authored Chunk 20 IDs: passed
- Required VCB markers present in new shortcut files: passed
- Required sections present in new shortcut files: passed
- SHORTCUT_REGISTER marks authored Chunk 20 shortcut IDs active: passed
- SHORTCUT_REGISTER shortcut rows are inside declared shortcut tables: passed
- Primary indexes route active Chunk 20 shortcut cards: passed
- Prompt library routes active Chunk 20 shortcut cards: passed
- AI coach index routes active Chunk 20 shortcut cards: passed
- LLM source maps route active Chunk 20 shortcut cards: passed
- Stale planned routes for authored Chunk 20 shortcuts are absent from indexes and SHORTCUT_REGISTER: passed
- Chunk 20 did not start full shortcut expansion or disallowed topic-card families: passed
- Chunk 20 report/changelog routing claims match routed surfaces: passed
- Active Chunk 20 report inventory lists created shortcut cards and updated routing/governance files: passed
- No single index section contains duplicate active Chunk 20 shortcut rows: passed
- Active Chunk 20 machine-claim catalog matches validator checks: passed

## Scope boundaries preserved

Chunk 20 did not start full shortcut-card expansion, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_21_security_permission_shortcut_topic_cards`.

## Unresolved questions

None.

## Packaging expectation

Submit one timestamped authoritative zip and checksum after validator and extracted-package verification.

<!-- VCB:STOP_RETRIEVAL reason="chunk_20_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_20 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
