---
id: vcb.chunk_report.chunk_3
title: Chunk 3 Report — Setup, Sandboxes, Approvals, and Git Discipline
artifact_type: chunk_report
version: 0.4.1-draft.chunk3-revision
status: waiting_for_editor_review
created_on: 2026-06-08
last_verified: 2026-06-08
next_review_due: 2026-07-08
review_cadence: event_driven
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_3 version=0.4.1-draft.chunk3-revision -->

# Chunk 3 Report — Setup, Sandboxes, Approvals, and Git Discipline

## Chunk ID and Scope

**Chunk ID:** `chunk_3_setup_safety_git_discipline`

**Scope completed:**

- Chapter 4 — Installing and Configuring Codex Without Creating a Mess
- Chapter 5 — Sandboxes, Approvals, and Why Full Access Is Usually a Bad Default
- Chapter 6 — Git Discipline for Vibe Coders

**Explicit non-scope preserved:** four-part prompt, plan-first prompting, context management, acceptance criteria, workflow playbooks, full Codex feature cards, pricing snapshots, tool catalog, and shortcut-card expansion.

## Canonical Review Package

Canonical review package: `vibe-coding-bible-chunk-3-revision-20260608T154703Z-authoritative.zip`.

## Files Created

```text
CHUNK_3_REPORT.md
chapters/04-installing-and-configuring-codex.md
chapters/05-sandboxing-and-approvals.md
chapters/06-git-discipline.md
```

## Files Updated

```text
README.md
manifest.json
llms.txt
llms-full.txt
SOURCE_REGISTER.md
CHANGELOG.md
TREE.txt
chapters/06-git-discipline.md
topics/concepts/blast-radius.md
schemas/topic.schema.json
schemas/chapter.schema.json
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

- Added `vcb.chapter.installing_and_configuring_codex`.
- Added `vcb.chapter.sandboxing_and_approvals`.
- Added `vcb.chapter.git_discipline`.
- Updated routing indexes so setup/config, permissions/sandboxing, and Git discipline are discoverable by task, concept, Codex surface, failure mode, stability, budget profile, project type, recoverability, risk level, glossary terms, prompt library, and AI-coach intervention.
- Added official OpenAI source anchors for Codex config basics, advanced config, sandboxing, approvals/security, permission profiles, rules, auto-review, and Windows setup.
- Added official Git source anchors for status, branch, commit, restore, reset, reflog, and worktree.
- Added `evidence_basis` and `source_kind` support to schema drafts, matching the Chunk 2 source-hygiene cleanup.
- Added the editor-suggested `### Useful metaphors` subsection to Chapter 3’s AI coach section.
- Kept exact pricing, current plan limits, exact model routing, and unstable UI details out of stable prose.
- Revision fix: normalized `source_kind` in `chapters/06-git-discipline.md` and `topics/concepts/blast-radius.md` to the schema-supported `official_docs_plus_maintainer_synthesis` value.
- Revision fix: ran active chapter/topic frontmatter instance validation against current schemas and updated validation wording to distinguish schema compile from instance validation.

## Sources Checked

Official OpenAI/Codex anchors checked:

- `openai.codex.cli`
- `openai.codex.config_basic`
- `openai.codex.config_advanced`
- `openai.codex.agents_md`
- `openai.codex.sandboxing`
- `openai.codex.agent_approvals_security`
- `openai.codex.permissions`
- `openai.codex.rules`
- `openai.codex.auto_review`
- `openai.codex.windows`
- `openai.codex.changelog`

Official Git/GitHub anchors checked:

- `git.docs.status`
- `git.docs.diff`
- `git.docs.branch_book`
- `git.docs.commit`
- `git.docs.restore`
- `git.docs.reset`
- `git.docs.revert`
- `git.docs.reflog`
- `git.docs.worktree`
- `github.docs.pull_requests`

No community/user-discovered practice was promoted to official guidance. Maintainer synthesis remains separated under `evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE` and `source_kind`, not as an evidence level.

## Validation Summary

```text
Actual source files tracked in manifest: 65
Manifest source-file inventory matches actual package files: yes
Markdown files: 42
Markdown files with frontmatter/metadata fences: 42 / 42
Markdown files with VCB markers: 42 / 42
JSON files: 8
JSON parse check: passed
JSON Schema draft compile check: passed
Active chapter/topic frontmatter schema validation: passed
Active chapter/topic files validated: 13
Active chapter/topic frontmatter validates against current schemas: passed
evidence_basis/source_kind values validated against schemas: passed
New chapter files created in Chunk 3: 3
New chapter frontmatter schema validation: passed, 3 / 3
Required Chunk 3 files present: passed
Required chapter sections present: passed
Required VCB markers present in new chapter files: passed
README next-chunk route checked against manifest: passed
Index namespace drift scan covers active and planned index routes: passed
Active index routes point to authored active IDs: passed
Official Codex setup/config/sandbox/approval source anchors checked: passed
E3 evidence definition remains blueprint-aligned: passed
No vcb.pricing.* drift remains: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

Known exception: `.gitkeep` files are structural placeholders and intentionally contain no frontmatter or VCB markers.

## Design Decisions

1. **Setup chapter focuses on setup discipline, not an install-command manual.** Exact install commands and config keys are volatile and remain anchored to official docs.
2. **Sandbox/approval chapter uses bounded autonomy, not blanket denial.** Broad permissions are treated through harm reduction: isolate, remove secrets, use fake data, and keep rollback.
3. **Git discipline is intentionally conceptual.** The chapter teaches status, diff, commit, branch, worktree, restore, reset, revert, and reflog as safety concepts without becoming a full Git manual.
4. **Prompting material was kept out of scope.** Chunk 4 owns four-part prompt, plan-first, context management, and acceptance criteria.
5. **Schema cleanup stayed lightweight but verified.** `evidence_basis` and `source_kind` are supported by the schemas, and active chapter/topic frontmatter now validates against those schemas. Broader validation tooling remains deferred.

## Unresolved Questions

1. Whether Chapter 4 should later split into separate topic cards for `vcb.codex.config`, `vcb.codex.agents_md`, and setup audit workflows.
2. Whether Chapter 5 should later split into safety cards for sandboxing, permissions, secrets, and broad-access shortcuts.
3. Whether Chapter 6 should later split into a full `vcb.workflow.git_discipline` card plus command-specific concept cards for restore/reset/reflog/worktree.
4. Whether exact Codex install/config instructions should ever appear in chapter prose or only in volatile topic cards.
5. Whether a machine validation script should be added after Chunk 4 or deferred until more topic-card volume exists.

## Next Recommended Chunk

**Chunk 4**, only after editor approval:

- Chapter 7 — The Four-Part Prompt: Goal, Context, Constraints, Done When
- Chapter 8 — Plan First, Code Second
- Chapter 9 — Context Management: Enough Context, Not Everything
- Chapter 10 — Acceptance Criteria: The Difference Between “Looks Done” and Done

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_3 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
