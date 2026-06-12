<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_17 version=0.1.0 -->
---
id: vcb.chunk_report.chunk_17
artifact_type: chunk_report
version: 0.1.0
chunk_id: chunk_17_frontend_refactor_dependency_workflow_topic_cards
status: waiting_for_editor_review
created_on: '2026-06-09'
last_verified: '2026-06-09'
canonical_review_package: vibe-coding-bible-chunk-17-revision-20260609T192045Z-authoritative.zip
---

# Chunk 17 Report — Frontend, Refactor, Dependency, Release, and Documentation Workflow Topic Cards

Chunk 17 authored a bounded workflow topic-card slice after Chunk 16 approval. The slice expands frontend verification, visual QA, accessibility review, safe refactoring, dependency decisions, dependency update review, release notes, and documentation updates. It stays tied to approved narrative chapters and active Codex feature cards without starting full workflow expansion.

## Scope Authored

Created 8 active topic cards:

- `vcb.workflow.frontend_work` — `topics/workflows/frontend-work.md`
- `vcb.workflow.visual_qa` — `topics/workflows/visual-qa.md`
- `vcb.workflow.accessibility_review` — `topics/workflows/accessibility-review.md`
- `vcb.workflow.refactoring` — `topics/workflows/refactoring.md`
- `vcb.workflow.dependency_decisions` — `topics/workflows/dependency-decisions.md`
- `vcb.workflow.dependency_update_review` — `topics/workflows/dependency-update-review.md`
- `vcb.workflow.release_notes` — `topics/workflows/release-notes.md`
- `vcb.workflow.documentation_updates` — `topics/workflows/documentation-updates.md`

## Explicit Non-Scope Preserved

Chunk 17 did not start:

- full tool-card expansion;
- full shortcut-card expansion;
- field-practice-card expansion;
- pricing snapshot expansion;
- broad workflow expansion outside the approved frontend/refactor/dependency/documentation slice;
- new narrative chapters.

## Revision Summary

Chunk 17 revision addressed editor-blocking routing/governance defects only:

- normalized the manifest topic-namespace redirect map and namespace-policy redirect map so aliases resolve identically;
- patched `indexes/INDEX_BY_TASK.md` task sections to route to active atomic Chunk 17 workflow cards instead of relying only on the aggregate Chunk 17 inventory;
- replaced the stale planned `vcb.workflow.documentation_update` route with active `vcb.workflow.documentation_updates`;
- extended `scripts/validate_repository.py` to fail on those redirect-map and task-index defects.

## Files Created

- `CHUNK_17_REPORT.md`
- `topics/workflows/frontend-work.md`
- `topics/workflows/visual-qa.md`
- `topics/workflows/accessibility-review.md`
- `topics/workflows/refactoring.md`
- `topics/workflows/dependency-decisions.md`
- `topics/workflows/dependency-update-review.md`
- `topics/workflows/release-notes.md`
- `topics/workflows/documentation-updates.md`

## Files Updated

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
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

## Source Review

Official OpenAI/Codex sources checked or reused as anchors:

- `openai.codex.use_cases.frontend_designs`
- `openai.codex.use_cases.qa_computer_use`
- `openai.codex.use_cases.web_development`
- `openai.codex.use_cases.refactor_your_codebase`
- `openai.codex.use_cases.update_documentation`
- `openai.codex.best_practices`

Official vendor sources checked or reused as anchors:

- `mdn.css.media_queries`
- `w3c.wcag_overview`
- `w3c.wai.wcag22_quickref`
- `playwright.docs.visual_comparisons`
- `playwright.docs.screenshots`
- `playwright.docs.accessibility_testing`
- `github.docs.dependency_review`
- `github.docs.dependency_graph`
- `github.docs.dependency_maintenance_best_practices`
- `github.docs.dependabot_security_updates`
- `github.docs.dependabot_version_updates`
- `github.docs.release_notes_generated`
- `npm.docs.package_json`
- `npm.docs.package_lock`
- `npm.docs.security_audit`

Named practitioner/expert source checked:

- `martin_fowler.refactoring`
- `keepachangelog.v1_1_0`

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
active chapter/topic files validated: 109
shortcut IDs registered: 98
tool IDs registered: 46
pricing snapshots active: 1
```

### Machine-enforced checks

- Manifest source-file inventory matches actual package files: passed
- Manifest source_artifacts inventory matches actual package files: passed
- Manifest all_tracked_files matches source_files and actual package files: passed
- Canonical review package references are consistent across manifest fields: passed
- New frontend/refactor/dependency workflow topic files created in Chunk 17: passed
- Required Chunk 17 frontend/refactor/dependency workflow-card slice present: passed
- Manifest frontend_refactor_dependency_workflow_cards map matches authored Chunk 17 files: passed
- Manifest chunk_17_required_topic_ids matches authored Chunk 17 IDs: passed
- Required topic sections present: passed
- Required VCB markers present in new frontend/refactor/dependency workflow files: passed
- llms.txt / llms-full.txt source-map versions match current chunk: passed
- README root frontmatter status matches current chunk: passed
- README body current chunk matches manifest current chunk: passed
- README and manifest next-chunk IDs match exactly: passed
- Index/register VCB begin-marker versions match frontmatter versions: passed
- Index files include STOP_RETRIEVAL and matching END_INDEX markers: passed
- VCB begin/end marker pairs exist across Markdown artifacts: passed
- SOURCE_REGISTER source rows are inside declared Source ID tables: passed
- Duplicate frontend/refactor/dependency full-list sections removed from primary indexes: passed
- Manifest topic_namespace_policy and namespace_policy redirect maps match exactly: passed
- INDEX_BY_TASK routes active Chunk 17 cards through task-level sections: passed
- Stale documentation_update planned route is absent from indexes: passed
- Planned-route replacements do not shadow authored active Chunk 17 cards: passed
- Active Chunk 17 machine-claim catalog matches validator checks: passed
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

- Scope stayed within the approved bounded frontend/refactor/dependency/documentation workflow slice.
- Human sections use plain language, examples, good/bad contrasts, and checklists.
- AI coach sections include diagnostic questions, coaching tactics, red flags, and prompt patterns.
- Shortcut Reality sections include acceptable cases, bad-idea cases, probability/impact/recoverability, blast radius, minimum guardrails, and recovery plans.
- Budget and Constraint Notes distinguish cheapest reliable, fastest high-usage, low-attention, production-quality, prototype, and maintenance postures.
- Stable Core, Volatile Surface, and Obsolescence Watch separate durable control-loop practice from product, UI, CI, dependency, documentation, and vendor-tool drift.

## Design Decisions

- Frontend workflow cards require browser or screenshot evidence instead of code-only plausibility.
- Accessibility is separated from visual QA because visual correctness does not prove keyboard, semantic, or assistive-technology behavior.
- Refactoring is framed as behavior preservation, not cleanup aesthetics.
- Dependency cards separate choosing a new dependency from reviewing a dependency update because their risks and rollback paths differ.
- Release-note and documentation cards require source-grounded output and explicitly reject invented user impact.
- Exact pricing, plan limits, model routing, and feature availability were not frozen into stable prose.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_18_failure_mode_topic_cards`.

Scope: bounded failure-mode topic-card expansion tied to hallucinated APIs, context pollution, weakened tests, broad-refactor drift, dependency bloat, UI taste gaps, and CI false-confidence loops.

Do not start full tool-card expansion, full shortcut-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_17 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
