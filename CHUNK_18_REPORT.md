<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_18 version=0.1.2 -->
---
id: vcb.chunk_report.chunk_18
artifact_type: chunk_report
version: 0.1.2
chunk_id: chunk_18_failure_mode_topic_cards
status: waiting_for_editor_review
created_on: '2026-06-09'
last_verified: '2026-06-09'
canonical_review_package: vibe-coding-bible-chunk-18-revision2-20260609T220000Z-authoritative.zip
---

# Chunk 18 Report — Failure-Mode Topic Cards Revision

Chunk 18 authored and revised a bounded failure-mode topic-card slice after Chunk 17 approval. The slice expands hallucinated APIs, context pollution, weakened tests, broad-refactor drift, dependency bloat, UI taste gaps, CI false-confidence loops, and done claim without evidence. This revision fixes routing/index governance defects only. It does not start Chunk 19.

## Scope Authored

Created 8 active failure-mode topic cards:

- `vcb.failure.hallucinated_apis` — `topics/failure-modes/hallucinated-apis.md` — Hallucinated APIs and Fake Interfaces
- `vcb.failure.context_pollution` — `topics/failure-modes/context-pollution.md` — Context Pollution
- `vcb.failure.weakened_tests` — `topics/failure-modes/weakened-tests.md` — Weakened Tests
- `vcb.failure.broad_refactor_drift` — `topics/failure-modes/broad-refactor-drift.md` — Broad-Refactor Drift
- `vcb.failure.dependency_bloat` — `topics/failure-modes/dependency-bloat.md` — Dependency Bloat
- `vcb.failure.ui_taste_gap` — `topics/failure-modes/ui-taste-gap.md` — UI Taste Gap
- `vcb.failure.ci_false_confidence` — `topics/failure-modes/ci-false-confidence.md` — CI False-Confidence Loop
- `vcb.failure.done_claim_without_evidence` — `topics/failure-modes/done-claim-without-evidence.md` — Done Claim Without Evidence

## Explicit Non-Scope Preserved

Chunk 18 did not start:

- full tool-card expansion;
- full shortcut-card expansion;
- field-practice-card expansion;
- pricing snapshot expansion;
- broad workflow expansion outside the approved failure-mode slice;
- new narrative chapters;
- Chunk 19 constraint/budget topic cards.

## Files Created

- `CHUNK_18_REPORT.md`
- `topics/failure-modes/hallucinated-apis.md`
- `topics/failure-modes/context-pollution.md`
- `topics/failure-modes/weakened-tests.md`
- `topics/failure-modes/broad-refactor-drift.md`
- `topics/failure-modes/dependency-bloat.md`
- `topics/failure-modes/ui-taste-gap.md`
- `topics/failure-modes/ci-false-confidence.md`
- `topics/failure-modes/done-claim-without-evidence.md`

## Files Updated

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
- `CHANGELOG.md`
- `TREE.txt`
- `scripts/validate_repository.py`
- `topics/concepts/diff.md`
- `topics/failure-modes/done-claim-without-evidence.md`
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

## Revision Edits After Editor Review

- Added active `vcb.failure.*` routes to `indexes/PROMPT_LIBRARY.md`, `indexes/INDEX_FOR_AI_COACHES.md`, `indexes/INDEX_BY_STABILITY.md`, `indexes/INDEX_BY_CONCEPT.md`, and `indexes/INDEX_BY_SHORTCUT.md`.
- Completed full-list failure-mode sections so `vcb.failure.done_claim_without_evidence` is included in `indexes/GLOSSARY.md`, `indexes/INDEX_BY_BUDGET_PROFILE.md`, `indexes/INDEX_BY_RECOVERABILITY.md`, and `indexes/INDEX_BY_RISK_LEVEL.md`.
- Replaced the repeated `llms.txt` Chunk 18 active-status phrase with one clean statement.
- Normalized `topics/failure-modes/done-claim-without-evidence.md` from `## Required sections in this topic` to `## Quick Navigation`.
- Reverted unintended historical drift in `CHUNK_2_REPORT.md`; the file now matches the last approved Chunk 17 package.
- Kept the intentional `topics/concepts/diff.md` migration from old done-claim naming to `vcb.failure.done_claim_without_evidence`.
- Tightened `scripts/validate_repository.py` so these routing omissions and report/source-map clutter now fail validation.

## Second Revision Edits After Editor Review

- Patched `indexes/INDEX_BY_FAILURE_MODE.md` semantic sections so unsupported completion summaries, unreproduced bug-fix claims, and confident wrong summaries route directly to `vcb.failure.done_claim_without_evidence`.
- Removed duplicate active failure-mode rows from `## CI or automation mutates too much` and `## Plausible APIs, weak tests, and hidden gaps`.
- Extended `scripts/validate_repository.py` so semantic failure-mode lookup sections and duplicate active failure-mode rows fail validation.


## Source Review

Official OpenAI/Codex sources checked or reused as anchors:

- `openai.codex.prompting`
- `openai.codex.workflows`
- `openai.codex.best_practices`
- `openai.codex.agents_md`
- `openai.codex.app_review`
- `openai.codex.noninteractive`
- `openai.codex.github_action`
- `openai.codex.use_cases.codebase_onboarding`
- `openai.codex.use_cases.qa_computer_use`
- `openai.codex.use_cases.refactor_your_codebase`
- `openai.codex.use_cases.dependency_incident_audits`
- `openai.codex.use_cases.frontend_designs`
- `openai.codex.use_cases.make_granular_ui_changes`

Official vendor sources checked or reused as anchors:

- `mdn.glossary.api`
- `mdn.learn_web_apis`
- `typescript.docs.home`
- `jest.docs_getting_started`
- `npm.docs.package_json`
- `npm.docs.package_lock`
- `github.docs.dependency_maintenance_best_practices`
- `playwright.docs.visual_comparisons`
- `w3c.wai.web_accessibility_intro`
- `github.docs.actions_ci`
- `github.docs.github_token`

Named practitioner/expert sources reused as anchors:

- `martin_fowler.refactoring`
- `martin_fowler.preparatory_refactoring`

Maintainer synthesis used only as synthesis:

- `vcb.synthesis.stable_engineering_practice`

## Validation Summary

Command run from repository root:

```text
python scripts/validate_repository.py
```

Expected result for the submitted package:

```text
VCB validation passed
active chapter/topic files validated: 117
shortcut IDs registered: 98
tool IDs registered: 46
pricing snapshots active: 1
```

### Machine-enforced checks

- Manifest source-file inventory matches actual package files: passed
- Manifest source_artifacts inventory matches actual package files: passed
- Manifest all_tracked_files matches source_files and actual package files: passed
- Canonical review package references are consistent across manifest fields: passed
- New failure-mode topic files created in Chunk 18: passed
- Required Chunk 18 failure-mode-card slice present: passed
- Manifest failure_mode_cards map matches authored Chunk 18 files: passed
- Manifest chunk_18_required_topic_ids matches authored Chunk 18 IDs: passed
- Required topic sections present: passed
- Required VCB markers present in new failure-mode files: passed
- llms.txt / llms-full.txt source-map versions match current chunk: passed
- README root frontmatter status matches current chunk: passed
- README body current chunk matches manifest current chunk: passed
- README and manifest next-chunk IDs match exactly: passed
- Index/register VCB begin-marker versions match frontmatter versions: passed
- Index files include STOP_RETRIEVAL and matching END_INDEX markers: passed
- VCB begin/end marker pairs exist across Markdown artifacts: passed
- SOURCE_REGISTER source rows are inside declared Source ID tables: passed
- Duplicate failure-mode full-list sections removed from primary indexes: passed
- PROMPT_LIBRARY routes active Chunk 18 failure-mode cards: passed
- INDEX_FOR_AI_COACHES routes active Chunk 18 failure-mode cards: passed
- INDEX_BY_STABILITY routes active Chunk 18 failure-mode cards: passed
- INDEX_BY_CONCEPT routes active Chunk 18 failure-mode cards: passed
- INDEX_BY_SHORTCUT routes active Chunk 18 failure-mode cards: passed
- Full-list Chunk 18 failure-mode sections include all required IDs: passed
- llms.txt active-chunk status phrases are not repeated: passed
- Chunk 18 report/changelog routing claims match routed surfaces: passed
- INDEX_BY_TASK routes active Chunk 18 failure-mode cards through task-level sections: passed
- Stale planned failure-mode routes are absent from indexes: passed
- INDEX_BY_FAILURE_MODE semantic sections route done-claim failures to the active atomic card: passed
- INDEX_BY_FAILURE_MODE has no duplicate active failure-mode rows inside a single section: passed
- Active Chunk 18 machine-claim catalog matches validator checks: passed
- Manifest editor_gate approval_applied matches current chunk transition: passed
- Current chunk report chunk_id matches manifest active chunk: passed
- Root governance metadata drift scan: passed
- Index namespace drift scan covers active and planned index routes: passed
- Active index routes point to authored active IDs: passed
- Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed
- Index shortcut routes resolve to SHORTCUT_REGISTER: passed
- Index tool IDs resolve to TOOL_REGISTER: passed
- Evidence source IDs resolve to SOURCE_REGISTER: passed
- Active chunk report source IDs resolve to SOURCE_REGISTER: passed
- Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed
- source_status.official_openai matches Evidence and Sources sections: passed
- source_status.official_vendor matches Evidence and Sources sections: passed
- Duplicate source URL detection: passed
- Frontmatter parser accepts marker-prefixed files and ignores body horizontal rules: passed
- Report final line is AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW: passed

### Manual/editorial checks

- Scope stayed within the approved bounded failure-mode topic-card slice.
- Routing indexes now prefer active atomic failure-mode cards where they exist.
- Human sections use plain language, examples, good/bad contrasts, and checklists.
- AI coach sections include diagnostic questions, coaching tactics, red flags, and prompt patterns.
- Shortcut Reality sections include acceptable cases, bad-idea cases, probability/impact/recoverability, blast radius, minimum guardrails, and recovery plans.
- Budget and Constraint Notes distinguish cheapest reliable, fastest high-usage, low-attention, production-quality, prototype, and maintenance postures.
- Stable Core, Volatile Surface, and Obsolescence Watch separate durable control-loop practice from product, vendor-tool, package, UI, CI, and source-drift details.

## Design Decisions

- Failure-mode cards use the `vcb.failure.*` namespace rather than broad workflow or shortcut namespaces.
- Cards are diagnostic and recovery-oriented; they do not replace shortcut cards or workflow cards.
- Hallucinated APIs and done claim without evidence are separated because fake-contract risk and unsupported-completion risk require different evidence checks.
- Dependency bloat is separated from dependency update review because one is an adoption failure mode and the other is an update workflow.
- UI taste gap is separated from visual QA because the failure includes taste, state, responsiveness, accessibility, and design-system consistency.
- Exact pricing, plan limits, model routing, and feature availability were not frozen into stable prose.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_19_constraint_budget_topic_cards`.

Scope: bounded constraint and budget topic-card expansion tied to operating modes, attention constraints, build versus maintenance phase, and usage-budget decisions.

Do not start full tool-card expansion, full shortcut-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_18 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
