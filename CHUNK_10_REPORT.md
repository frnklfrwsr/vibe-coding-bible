---
id: vcb.report.chunk_10
chunk_id: chunk_10_operating_system_and_playbooks
title: Chunk 10 Report — Project Operating System and Playbooks
artifact_type: chunk_report
version: 0.11.0-draft.chunk10
status: waiting_for_editor_review
created_on: 2026-06-09
last_verified: 2026-06-09
review_cadence: per_chunk
---

<!-- VCB:BEGIN_REPORT id=vcb.report.chunk_10 version=0.11.0-draft.chunk10 -->

# Chunk 10 Report — Project Operating System and Playbooks

## Scope Completed

Chunk 10 only:

- Chapter 31 — From Prompt Library to Team Workflow
- Chapter 32 — Failure Modes: How Codex Work Goes Wrong
- Chapter 33 — The Codex Playbooks
- Chapter 34 — Building Your First Serious App with Codex
- Chapter 35 — The Senior Engineer Checklist for Vibe Coders

No Chunk 11 field-practice/updating/shortcut-expansion material was authored.

## Files Created

```text
CHUNK_10_REPORT.md
chapters/31-from-prompt-library-to-team-workflow.md
chapters/32-failure-modes-codex-work-goes-wrong.md
chapters/33-codex-playbooks.md
chapters/34-building-first-serious-app-with-codex.md
chapters/35-senior-engineer-checklist.md
```

## Files Updated

```text
README.md
manifest.json
llms.txt
llms-full.txt
SOURCE_REGISTER.md
SHORTCUT_REGISTER.md
TOOL_REGISTER.md
CHANGELOG.md
TREE.txt

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
scripts/validate_repository.py
```

## What Changed

- Added `vcb.chapter.prompt_library_to_team_workflow`.
- Added `vcb.chapter.failure_modes_codex_work`.
- Added `vcb.chapter.codex_playbooks`.
- Added `vcb.chapter.first_serious_app`.
- Added `vcb.chapter.senior_engineer_checklist`.
- Updated routing indexes for prompt-library maturation, failure-mode diagnosis, playbook selection, first serious app sequencing, and senior-engineer acceptance gates.
- Registered planned shortcut IDs for process overhead, team-process overbuild, stale durable guidance, failure-mode avoidance, symptom patching, blind playbook copy/paste, prototype-as-production, first-app overbuild, checklist skipping, and checklist theater.
- Added official OpenAI source anchors for AI-native engineering team guidance, goal-following, proof-of-concept, internal apps, documentation updates, browser-game prototype flow, and hallucination/truthfulness framing.
- Kept field-practice expansion, update protocol chapter, full shortcut cards, constraints/cost/tool-stack chapters, other-AI material, explicit limitations/bias chapters, pricing snapshots, and full topic-card expansion out of scope.

## Revision Fixes Applied

- Replaced visible index status lines with chunk-neutral routing text across all primary indexes.
- Rebuilt primary indexes as clean routing maps instead of append-only chunk logs.
- Removed historical `Chunk 9` routing sections/headings from indexes.
- Added the missing `new project bootstrap` Chapter 33 playbook and kept it distinct from the MVP prototype playbook.
- Expanded Chapter 33 with compact blueprint playbooks for release notes, production-error investigation, API endpoint work, dependency migration, dead-code removal, documentation improvement, MVP prototype build, and auth-sensitive hardening.
- Updated `PROMPT_LIBRARY.md` and `INDEX_BY_TASK.md` so the expanded Chapter 33 playbooks are retrievable by task and prompt pattern.
- Extended `scripts/validate_repository.py` to catch stale visible index status lines, historical chunk headings in indexes, and Chapter 33 playbook coverage gaps.

## Sources Checked

- `openai.codex.best_practices` — official OpenAI anchor for four-part prompting, durable guidance, config, MCP, skills, and automations.
- `openai.codex.workflows` — official OpenAI anchor for teammate-style workflows, explicit context, definition of done, workflow examples, and verification.
- `openai.codex.prompting` — official OpenAI anchor for context handling, file/image references, goal mode, and verifiable completion criteria.
- `openai.codex.guide_ai_native_engineering_team` — official OpenAI anchor for agentic engineering-team workflow, planning artifacts, AGENTS.md feedback loops, and testing as source of truth.
- `openai.codex.use_cases.follow_goals` — official OpenAI anchor for long-running work with a clear success condition and validation loop.
- `openai.codex.use_cases.idea_to_proof_of_concept` — official OpenAI anchor for turning rough product ideas into smallest useful browser-verified prototypes.
- `openai.codex.use_cases.build_and_deploy_internal_apps` — official OpenAI anchor for focused internal-app build/deploy workflows.
- `openai.codex.use_cases.update_documentation` — official OpenAI anchor for documentation/release-note workflow support.
- `openai.help.truthfulness` and `openai.hallucinations` — official OpenAI anchors for confident-wrong and hallucination caveats.

## Validation Summary

```text
VCB validation passed
Actual source files tracked in manifest: 102
Manifest source-file inventory matches actual package files: yes
source_files rich objects preserved: yes
Markdown files: 78
Markdown files with frontmatter/metadata fences: 78 / 78
Markdown files with VCB markers: 78 / 78
JSON files: 8
JSON parse check: passed
JSON Schema draft compile check: passed
Active chapter/topic files validated: 42
Active chapter/topic frontmatter schema validation: passed
Shortcut IDs registered: 88
Tool IDs registered: 20
Required Markdown headings present in active chapter/topic files: passed
VCB section marker pairing in active chapter/topic files: passed
New chapter files created in Chunk 10: 5
New chapter frontmatter schema validation: passed, 5 / 5
Required Chunk 10 files present: passed
Required chapter sections present: passed
Required VCB markers present in new chapter files: passed
README root frontmatter status matches current chunk: passed
README body current chunk matches manifest current chunk: passed
README next-chunk route checked against manifest: passed
Manifest editor_gate approval_applied matches current chunk transition: passed
Current chunk report chunk_id matches manifest active chunk: passed
Root governance metadata drift scan: passed
Index namespace drift scan covers active and planned index routes: passed
Active index routes point to authored active IDs: passed
Visible index status lines match current chunk or are chunk-neutral: passed
Historical chunk-addition sections deduplicated in primary indexes: passed
Chapter 33 playbook coverage checked against full blueprint list: passed
New project bootstrap playbook route present in INDEX_BY_TASK and PROMPT_LIBRARY: passed
Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed
Planned shortcut index routes resolve to SHORTCUT_REGISTER or approved future shortcut IDs: passed
Evidence source IDs resolve to SOURCE_REGISTER or declared synthesis IDs: passed
Tool IDs in indexes and active report resolve to TOOL_REGISTER: passed
SHORTCUT_REGISTER table row shape: passed
evidence_basis/source_kind values validated against schemas: passed
No exact pricing, limits, model-routing, context-window numbers, or unstable UI-command recipes added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

Known exception: `.gitkeep` files are structural placeholders and intentionally contain no frontmatter or VCB markers.

## Design Decisions

1. Chapter 31 is a workflow-compounding chapter, not a process-maximalism chapter. It tells users to promote repeated prompts into durable artifacts only after repeated friction.
2. Chapter 32 stays as a failure-mode router. It does not fully expand every failure card; those remain future topic cards.
3. Chapter 33 now covers the blueprint playbook set in compact form while keeping exact commands surface-neutral and reviewable.
4. Chapter 34 treats generated prototypes as discovery artifacts, not automatic production foundations.
5. Chapter 35 is a compact risk-scaled checklist rather than a full security/release checklist.
6. No exact pricing, plan packaging, current model routing, context-window numbers, or current UI command recipes were frozen into stable prose.

## Unresolved Questions

1. Which failure modes should become first-class cards first: hallucinated APIs, weakened tests, unreviewed large diffs, dependency bloat, or context pollution.
2. Whether the first-serious-app chapter should later split into app-spec, vertical-slice, auth, database, UI-state, release, and post-launch loop cards.
3. Whether the playbook library should become a generated artifact assembled from topic-card prompt patterns.
4. Whether duplicate OpenAI source URLs should be normalized into aliases in Chunk 11 or deferred to maintenance.

## Next Recommended Chunk

**Chunk 11**, only after editor approval:

- Chapter 36 — Field Notes: Unofficial and User-Discovered Codex Practices
- Chapter 37 — Maintaining and Updating the Bible
- Chapter 38 — Risk-Managed Shortcuts: When Users Ignore Best Practices

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.report.chunk_10 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
