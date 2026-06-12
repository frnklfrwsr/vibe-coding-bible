<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_19 version=0.20.0-draft.chunk19 -->
---
id: vcb.chunk_report.chunk_19
title: CHUNK_19_REPORT
artifact_type: chunk_report
chunk_id: chunk_19_constraint_budget_topic_cards
version: 0.20.0-draft.chunk19
status: waiting_for_editor_review
created_on: '2026-06-09'
last_verified: '2026-06-09'
next_review_due: '2026-07-09'
review_cadence: monthly
---

# Chunk 19 Report — Constraint and Budget Topic Cards

## Chunk ID

`chunk_19_constraint_budget_topic_cards`

## Scope completed

Bounded constraint/budget topic-card expansion tied to operating modes, attention constraints, usage burn, recovery budget, build versus maintenance phase, production-quality constraints, scope budget, and review budget.

## Revision notes

- Fixed `CHANGELOG.md` so the Chunk 19 changelog entry appears inside the declared changelog artifact before VCB:STOP_RETRIEVAL and VCB:END_CHANGELOG.
- Fixed nested manifest.source_artifacts.source_files so it matches top-level manifest.source_files, manifest.source_artifacts.all_tracked_files, and actual package inventory.
- Expanded this report’s file inventory to include the active chunk report and the Chapter 26 related-topic route correction.
- Added validator checks for live Markdown content after VCB:END_* markers, stale nested manifest source-file inventory, false source_files_match_manifest, Chunk 19 report inventory omissions, and Chunk 19 changelog content after VCB:END_CHANGELOG.

## Files created

- `CHUNK_19_REPORT.md` — current chunk report for bounded constraint/budget topic-card expansion
- `topics/constraints/operating-mode.md` — `vcb.constraints.operating_mode`
- `topics/constraints/attention-budget.md` — `vcb.constraints.attention_budget`
- `topics/constraints/usage-burn.md` — `vcb.constraints.usage_burn`
- `topics/constraints/recovery-budget.md` — `vcb.constraints.recovery_budget`
- `topics/constraints/build-vs-maintenance.md` — `vcb.constraints.build_vs_maintenance`
- `topics/constraints/production-quality-constraints.md` — `vcb.constraints.production_quality`
- `topics/constraints/scope-budget.md` — `vcb.constraints.scope_budget`
- `topics/constraints/review-budget.md` — `vcb.constraints.review_budget`

## Files updated

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
- `CHANGELOG.md`
- `TREE.txt`
- `scripts/validate_repository.py`
- `chapters/26-ci-non-interactive-codex-github-actions.md` — related-topic route correction from stale `vcb.constraints.api_budgeting` to active `vcb.constraints.usage_burn`
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

- `vcb.register.editor_feedback_chunk_18`
- `openai.codex.best_practices`
- `openai.codex.pricing`
- `openai.help.codex_chatgpt_plan`
- `openai.help.codex_rate_card`
- `vcb.pricing_snapshot.openai_codex`
- `openai.codex.noninteractive`
- `openai.codex.use_cases.refactor_your_codebase`
- `openai.codex.use_cases.update_documentation`
- `openai.codex.security_threat_model`
- `openai.codex.workflows`
- `openai.codex.feature_maturity`
- `openai.codex.app_review`
- `openai.codex.github_review`
- `github.docs.pull_requests`
- `openai.codex.use_cases.follow_goals`
- `vcb.synthesis.stable_engineering_practice`

## Validation claims implemented in `scripts/validate_repository.py`

- New constraint/budget topic files created in Chunk 19: passed
- Required Chunk 19 constraint-budget slice present: passed
- Manifest constraint_budget_cards map matches authored Chunk 19 files: passed
- Manifest chunk_19_required_topic_ids matches authored Chunk 19 IDs: passed
- Required VCB markers present in new constraint/budget files: passed
- Required sections present in new constraint/budget files: passed
- Primary indexes route active Chunk 19 constraint/budget cards: passed
- Prompt library routes active Chunk 19 constraint/budget cards: passed
- AI coach index routes active Chunk 19 constraint/budget cards: passed
- Budget index routes active Chunk 19 constraint/budget cards: passed
- Task index routes active Chunk 19 constraint/budget cards through task-level and aggregate sections: passed
- Stability, concept, shortcut, glossary, risk, recoverability, project-type, Codex-surface, tool-category, and failure-mode indexes route active Chunk 19 constraint/budget cards: passed
- LLM source maps route active Chunk 19 constraint/budget cards: passed
- Stale planned constraint routes are absent where active replacements are authored: passed
- Constraint/budget cards do not hardcode exact prices, limits, credits, or model-routing recipes into stable prose: passed
- Chunk 19 report/changelog routing claims match routed surfaces: passed
- Markdown artifacts have no live content after VCB:END markers except report terminal author status lines: passed
- Nested manifest source_artifacts.source_files matches top-level manifest source_files and actual package inventory: passed
- Manifest source_files_match_manifest is true only when nested source_files is current: passed
- Active Chunk 19 report inventory lists current chunk report and touched chapter route correction: passed
- CHANGELOG.md has no Chunk 19 content after VCB:END_CHANGELOG: passed
- Active Chunk 19 machine-claim catalog matches validator checks: passed

## Scope boundaries preserved

Chunk 19 did not start full tool-card expansion, full shortcut-card expansion, field-practice-card expansion, pricing expansion beyond source/snapshot routing, broad workflow expansion, or new narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_20_shortcut_harm_reduction_topic_cards`.

## Unresolved questions

None.

## Packaging expectation

Submit one timestamped authoritative zip and checksum after validator and extracted-package verification.

<!-- VCB:STOP_RETRIEVAL reason="chunk_19_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_19 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
