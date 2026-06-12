---
id: vcb.chunk_report.chunk_5
artifact_type: chunk_report
version: 0.6.0-draft.chunk5
status: waiting_for_editor_review
created_on: 2026-06-08
last_verified: 2026-06-08
review_cadence: chunk_gate
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_5 version=0.6.0-draft.chunk5 -->

# Chunk 5 Report — Core Workflows

## Scope

Chunk 5 covers only:

- Chapter 11 — Understanding an Unknown Codebase
- Chapter 12 — Building a Feature in Small Slices
- Chapter 13 — Debugging with Reproduction, Not Guessing
- Chapter 14 — Writing and Updating Tests with Codex

Explicit non-scope: frontend work, refactoring, dependency/package decisions, AGENTS.md deep dive, config deep dive, skills, MCP, hooks, CI/non-interactive automation, pricing snapshots, tool catalog, and full shortcut cards.

## Canonical Review Package

Canonical review package: `vibe-coding-bible-chunk-5-20260608T180527Z-authoritative.zip`.

## Files Created

```text
CHUNK_5_REPORT.md
chapters/11-understanding-an-unknown-codebase.md
chapters/12-building-feature-small-slices.md
chapters/13-debugging-with-reproduction.md
chapters/14-writing-updating-tests.md
```

## Files Updated

```text
README.md
manifest.json
llms.txt
llms-full.txt
SOURCE_REGISTER.md
SHORTCUT_REGISTER.md
CHANGELOG.md
TREE.txt
scripts/validate_repository.py

indexes/INDEX_BY_TASK.md
indexes/INDEX_BY_CONCEPT.md
indexes/INDEX_BY_CODEX_SURFACE.md
indexes/INDEX_BY_FAILURE_MODE.md
indexes/INDEX_BY_STABILITY.md
indexes/INDEX_BY_BUDGET_PROFILE.md
indexes/INDEX_FOR_AI_COACHES.md
indexes/INDEX_BY_PROJECT_TYPE.md
indexes/INDEX_BY_RECOVERABILITY.md
indexes/INDEX_BY_RISK_LEVEL.md
indexes/INDEX_BY_SHORTCUT.md
indexes/INDEX_BY_TOOL_CATEGORY.md
indexes/GLOSSARY.md
indexes/PROMPT_LIBRARY.md
```

## What Changed

- Added `vcb.chapter.understanding_unknown_codebase`.
- Added `vcb.chapter.feature_slicing`.
- Added `vcb.chapter.debugging_with_reproduction`.
- Added `vcb.chapter.writing_updating_tests`.
- Updated routing indexes for unknown-codebase exploration, feature slicing, repro-first debugging, and testing workflows.
- Registered planned shortcut IDs for `vcb.shortcut.editing_before_understanding` and `vcb.shortcut.debugging_without_repro`.
- Added official OpenAI source anchors for codebase onboarding, bug triage, QA with Computer Use, and AI-native engineering/testing guidance.
- Updated the validator to check the current chunk report dynamically from `manifest.json` instead of hardcoding the previous report.
- Kept exact pricing, current usage limits, model routing, frontend/browser chapter material, refactoring chapter material, and dependency-decision material out of stable Chunk 5 prose.

## Sources Checked

- `openai.codex.use_cases.codebase_onboarding` — official current anchor for mapping unfamiliar codebases, modules, data flow, and next files before editing.
- `openai.codex.workflows` — official current anchor for explicit context, definition of done, bug-fix repro workflow, write-a-test workflow, and verification.
- `openai.codex.prompting` — official current anchor for prompt task loops, context, file references, focused steps, validation, and review.
- `openai.codex.use_cases.automation_bug_triage` — official current anchor for triaging alerts, issues, failed checks, logs, and reports.
- `openai.codex.use_cases.qa_computer_use` — official current anchor for QA flows that report repro steps, expected result, actual result, and severity.
- `openai.codex.guide_ai_native_engineering_team` — official current anchor for tests as a source of truth when agents generate code quickly.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for durable workflow framing; not an evidence level.

## Validation Summary

```text
VCB validation passed
Actual source files tracked in manifest: 76
Manifest source-file inventory matches actual package files: yes
source_files rich objects preserved: yes
Markdown files: 52
Markdown files with frontmatter/metadata fences: 52 / 52
Markdown files with VCB markers: 52 / 52
JSON files: 8
JSON parse check: passed
JSON Schema draft compile check: passed
Active chapter/topic files validated: 21
Active chapter/topic frontmatter schema validation: passed
New chapter files created in Chunk 5: 4
New chapter frontmatter schema validation: passed, 4 / 4
Required Chunk 5 files present: passed
Required chapter sections present: passed
Required VCB markers present in new chapter files: passed
README next-chunk route checked against manifest: passed
Index namespace drift scan covers active and planned index routes: passed
Active index routes point to authored active IDs: passed
Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed
Planned shortcut index routes resolve to SHORTCUT_REGISTER or approved future shortcut IDs: passed
Evidence source IDs resolve to SOURCE_REGISTER or declared synthesis IDs: passed
SHORTCUT_REGISTER table row shape: passed
evidence_basis/source_kind values validated against schemas: passed
No exact pricing, limits, model-routing, or context-window numbers added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

Known exception: `.gitkeep` files are structural placeholders and intentionally contain no frontmatter or VCB markers.

## Design Decisions

1. **Chapter 11 starts read-only.** Unknown-codebase work is framed as mapping before patching.
2. **Chapter 12 keeps feature work bounded.** It teaches slice plans and implementation of one slice only.
3. **Chapter 13 makes reproduction the center.** Root cause and rerun checks are required before accepting bug fixes.
4. **Chapter 14 treats tests as behavior evidence.** The content explicitly warns against weak tests, over-mocking, deleted assertions, and tests that only prove implementation details.
5. **Shortcut handling stays harm-reduction based.** Risky shortcuts are not moralized; they are bounded by blast radius, recoverability, guardrails, and recovery plans.

## Unresolved Questions

1. Whether future workflow topic cards should split from the narrative chapters immediately after Chunk 13 or wait until the first full chapter pass is complete.
2. Whether the validator should next enforce required section headings and VCB begin/end pairs, not only metadata/schema/source/shortcut/index routing.
3. Whether testing should later split into separate topic cards for regression tests, unit tests, integration tests, E2E tests, and test-quality review.
4. Whether codebase understanding should later include a dedicated read-only subagent pattern once Chunk 9 subagents are authored.

## Next Recommended Chunk

Chunk 6, only after editor approval:

- Chapter 15 — Frontend Work: Screenshots, Browser Checks, and Taste
- Chapter 16 — Refactoring Without Breaking Everything
- Chapter 17 — Dependency, Package, and Framework Decisions

Do not start Chunk 7 persistent-guidance/customization material yet.

<!-- VCB:STOP_RETRIEVAL reason="chunk_5_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_5 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
