---
id: vcb.chunk_report.chunk_4
title: Chunk 4 Report — Prompting Codex Like an Operator
artifact_type: chunk_report
version: 0.5.1-draft.chunk4_revision
status: revision_waiting_for_editor_review
created_on: 2026-06-08
last_verified: 2026-06-08
next_review_due: 2026-07-08
review_cadence: event_driven
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_4 version=0.5.1-draft.chunk4_revision -->

# Chunk 4 Report — Prompting Codex Like an Operator

## Chunk ID and Scope

**Chunk ID:** `chunk_4_prompting_codex_like_an_operator`

**Scope completed:**

- Chapter 7 — The Four-Part Prompt: Goal, Context, Constraints, Done When
- Chapter 8 — Plan First, Code Second
- Chapter 9 — Context Management: Enough Context, Not Everything
- Chapter 10 — Acceptance Criteria: The Difference Between “Looks Done” and Done

**Explicit non-scope preserved:** unknown-codebase workflow, feature slicing, debugging/reproduction, testing chapter, frontend work, refactoring, dependencies, AGENTS.md/config deep dives, security, CI/non-interactive automation, pricing snapshots, and tool catalog expansion.

## Revision Scope

This revision fixes Chunk 4 routing/source hygiene only: shortcut ID consistency, shortcut-register table shape, source-ID resolution, validation wording, and package metadata. No Chunk 5 material was authored.

## Canonical Review Package

Canonical review package: `vibe-coding-bible-chunk-4-revision-20260608T165625Z-authoritative.zip`.

## Files Created

```text
CHUNK_4_REPORT.md
chapters/07-four-part-prompt.md
chapters/08-plan-first-code-second.md
chapters/09-context-management.md
chapters/10-acceptance-criteria.md
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

- Added `vcb.chapter.four_part_prompt`.
- Added `vcb.chapter.plan_first_code_second`.
- Added `vcb.chapter.context_management`.
- Added `vcb.chapter.acceptance_criteria`.
- Updated routing indexes so prompting, planning, context management, and acceptance criteria are discoverable by task, concept, Codex surface, failure mode, stability, budget profile, AI-coach intervention, project type, recoverability, risk level, shortcut, tool category, glossary term, and prompt pattern.
- Updated `PROMPT_LIBRARY.md` with four-part prompt, plan-only prompt, read-only context discovery, acceptance criteria generator, and final verification prompts.
- Added source-register anchors for official Codex prompting, workflows, goal-following, and execution-plan cookbook guidance.
- Kept exact pricing, current plan limits, context-window numbers, exact model routing, and unstable UI details out of stable prose.

## Revision Fixes

- Normalized the plan-skipping shortcut to canonical `vcb.shortcut.skipping_plan` across Chapter 8 and routing indexes.
- Reconciled Chapter 4 setup shortcuts by using registered `vcb.shortcut.skipping_setup` and registering `vcb.shortcut.using_existing_local_setup` as a planned shortcut.
- Repaired `SHORTCUT_REGISTER.md` so `vcb.shortcut.vague_prompt` and `vcb.shortcut.accepting_looks_done` are valid rows with `planned` status.
- Resolved missing Git evidence IDs by using registered `git.docs.home`, `git.docs.branch_book`, `git.docs.restore`, `git.docs.reset`, and `git.docs.revert` records instead of unresolved source aliases.
- Extended validation to check shortcut-profile resolution, planned shortcut route resolution, source-ID resolution, and shortcut-register table shape.

## Sources Checked

Official OpenAI/Codex anchors checked:

- `openai.codex.best_practices`
- `openai.codex.prompting`
- `openai.codex.workflows`
- `openai.codex.follow_goals`
- `openai.codex.exec_plans_cookbook`
- `openai.codex.agents_md`
- `openai.codex.changelog`

No community/user-discovered practice was promoted to official guidance. Maintainer synthesis remains separated under `evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE` and `source_kind`, not as an evidence level.

## Validation Summary

```text
Actual source files tracked in manifest: 71
Manifest source-file inventory matches actual package files: yes
source_files rich objects preserved: yes
Markdown files: 47
Markdown files with frontmatter/metadata fences: 47 / 47
Markdown files with VCB markers: 47 / 47
JSON files: 8
JSON parse check: passed
JSON Schema draft compile check: passed
Active chapter/topic files validated: 17
Active chapter/topic frontmatter schema validation: passed
New chapter files created in Chunk 4: 4
New chapter frontmatter schema validation: passed, 4 / 4
Required Chunk 4 files present: passed
Required chapter sections present: passed
Required VCB markers present in new chapter files: passed
README next-chunk route checked against manifest: passed
Index namespace drift scan covers active and planned index routes: passed
Active index routes point to authored active IDs: passed
evidence_basis/source_kind values validated against schemas: passed
Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed
Planned shortcut index routes resolve to SHORTCUT_REGISTER or approved future shortcut IDs: passed
Evidence source IDs resolve to SOURCE_REGISTER or declared synthesis IDs: passed
SHORTCUT_REGISTER table row shape: passed
Lightweight validation script run: passed
Official-source anchors checked for prompting/planning/context/acceptance: passed
No exact pricing, limits, or context-window numbers added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

Known exception: `.gitkeep` files are structural placeholders and intentionally contain no frontmatter or VCB markers.

## Design Decisions

1. **Chunk 4 stayed scoped.** No unknown-codebase, feature slicing, debugging, or testing chapter material was authored beyond cross-links and prompt routes.
2. **Prompt structure is framed as a work order, not magic syntax.** The four-part prompt is useful because it encodes target, evidence, boundaries, and proof.
3. **Plan-first is risk-calibrated.** The chapter says trivial changes do not need ceremony, while broad/risky/ambiguous work does.
4. **Context is treated as evidence.** The context chapter emphasizes relevance and freshness rather than token volume or context-window size.
5. **Acceptance criteria are evidence contracts.** The acceptance chapter separates Codex summary claims from checks, diffs, logs, tests, and manual behavior.
6. **Volatile product mechanics are isolated.** Goal mode, Plan mode, slash commands, context features, and exact UI mechanics are marked volatile.

## Unresolved Questions

1. Whether future prompt topic cards should duplicate chapter examples or extract reusable smaller cards under `topics/prompting/`.
2. Whether execution-plan guidance should become a separate workflow card before the first serious app/playbook chunks.
3. Whether context-management guidance should eventually split into local context, external context/MCP, and stale-context recovery.
4. Whether the lightweight validation script should expand later to include full schema reference resolution and redirect-map validation.

## Next Recommended Chunk

**Chunk 5**, only after editor approval:

- Chapter 11 — Understanding an Unknown Codebase
- Chapter 12 — Building a Feature in Small Slices
- Chapter 13 — Debugging with Reproduction, Not Guessing
- Chapter 14 — Writing and Updating Tests with Codex

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_4 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
