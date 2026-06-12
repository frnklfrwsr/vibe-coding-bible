<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_15 version=0.1.0 -->
---
id: vcb.chunk_report.chunk_15
artifact_type: chunk_report
version: 0.1.0
chunk_id: chunk_15_workflow_prompting_topic_cards
status: waiting_for_editor_review
created_on: '2026-06-09'
last_verified: '2026-06-09'
canonical_review_package: vibe-coding-bible-chunk-15-20260609T161524Z-authoritative.zip
---

# Chunk 15 Report — Workflow/Prompting Topic Cards

Chunk 15 authored a bounded workflow/prompting topic-card slice tied to approved foundational concepts and Codex feature cards.

## Scope Authored

Created 8 active topic cards:

- `vcb.prompting.four_part_prompt` — `topics/prompting/four-part-prompt.md`
- `vcb.prompting.acceptance_criteria` — `topics/prompting/acceptance-criteria.md`
- `vcb.prompting.plan_first` — `topics/prompting/plan-first.md`
- `vcb.prompting.context_management` — `topics/prompting/context-management.md`
- `vcb.workflow.unknown_codebase` — `topics/workflows/unknown-codebase.md`
- `vcb.workflow.feature_slicing` — `topics/workflows/feature-slicing.md`
- `vcb.workflow.bug_repro` — `topics/workflows/bug-repro.md`
- `vcb.workflow.testing` — `topics/workflows/testing.md`

## Explicit Non-Scope Preserved

Chunk 15 did not start:

- full tool-card expansion;
- full shortcut-card expansion;
- field-practice-card expansion;
- pricing snapshot expansion;
- broad workflow expansion outside the approved 8-card slice;
- new narrative chapters.

## Files Created

- `CHUNK_15_REPORT.md`
- `topics/prompting/four-part-prompt.md`
- `topics/prompting/acceptance-criteria.md`
- `topics/prompting/plan-first.md`
- `topics/prompting/context-management.md`
- `topics/workflows/unknown-codebase.md`
- `topics/workflows/feature-slicing.md`
- `topics/workflows/bug-repro.md`
- `topics/workflows/testing.md`

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

- `openai.codex.best_practices`
- `openai.codex.prompting`
- `openai.codex.workflows`
- `openai.codex.exec_plans_cookbook`
- `openai.codex.use_cases.codebase_onboarding`
- `openai.codex.use_cases.automation_bug_triage`
- `openai.codex.use_cases.qa_computer_use`
- `openai.codex.guide_ai_native_engineering_team`
- `openai.api.prompt_engineering`
- `openai.api.reasoning_best_practices`

Maintainer synthesis used only as synthesis:

- `vcb.synthesis.prompting_operator_practice`
- `vcb.synthesis.stable_engineering_practice`

## Validation Summary

Command run from repository root:

```text
python scripts/validate_repository.py
```

Expected result for the submitted package:

```text
VCB validation passed
active chapter/topic files validated: 93
shortcut IDs registered: 98
tool IDs registered: 46
pricing snapshots active: 1
```

### Machine-enforced checks

- Manifest source-file inventory matches actual package files: passed
- Manifest source_artifacts inventory matches actual package files: passed
- Manifest all_tracked_files matches source_files and actual package files: passed
- Canonical review package references are consistent across manifest fields: passed
- New workflow/prompting topic files created in Chunk 15: passed
- Required Chunk 15 workflow/prompting-card slice present: passed
- Manifest workflow_prompting_cards map matches authored Chunk 15 files: passed
- Manifest chunk_15_required_topic_ids matches authored Chunk 15 IDs: passed
- Required topic sections present: passed
- Required VCB markers present in new workflow/prompting files: passed
- llms.txt / llms-full.txt source-map versions match current chunk: passed
- README root frontmatter status matches current chunk: passed
- README body current chunk matches manifest current chunk: passed
- README and manifest next-chunk IDs match exactly: passed
- Index/register VCB begin-marker versions match frontmatter versions: passed
- Duplicate workflow/prompting full-list sections removed from primary indexes: passed
- Active Chunk 15 machine-claim catalog matches validator checks: passed
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

- Scope stayed within the approved bounded workflow/prompting slice.
- Human sections use plain language, examples, good/bad contrasts, and checklists.
- AI coach sections include diagnostic questions, coaching tactics, red flags, and prompt patterns.
- Shortcut Reality sections include acceptable cases, bad-idea cases, risk profile, blast radius, recoverability, guardrails, and recovery plans.
- Budget and Constraint Notes distinguish cheapest reliable, fastest high-usage, low-attention, production-quality, prototype, and maintenance postures.
- Stable Core, Volatile Surface, and Obsolescence Watch separate durable practice from product/mechanics drift.

## Design Decisions

- Workflow/prompting cards point back to the existing narrative chapters instead of replacing them.
- Index routes were updated as routing surfaces, not append-only mirrors; duplicate full-list workflow/prompting sections were removed.
- Shortcut IDs remain registered shortcut routes, not authored shortcut topic cards.
- Exact pricing, plan limits, model routing, and feature availability were not frozen into stable prose.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_16_review_safety_workflow_topic_cards`.

Scope: bounded review, safety, and verification workflow topic-card expansion tied to Codex output review, PR review, secrets/security checks, CI triage, and production-risk gates.

Do not start full tool-card expansion, full shortcut-card expansion, field-practice-card expansion, pricing expansion, or new narrative chapters.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_15 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
