---
id: vcb.chunk_report.9
chunk_id: chunk_9_advanced_agentic_workflows
title: "Chunk 9 Report — Advanced Agentic Workflows"
artifact_type: chunk_report
version: 0.1.0
status: waiting_for_editor_review
created_on: 2026-06-08
last_verified: 2026-06-08
next_review_due: 2026-09-08
review_cadence: monthly
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.9 version=0.1.0 -->

# Chunk 9 Report — Advanced Agentic Workflows

## Chunk ID and Scope

**Chunk ID:** `chunk_9_advanced_agentic_workflows`

**Scope completed:**

- Chapter 27 — Cloud Delegation and Parallel Work
- Chapter 28 — Subagents: Parallel Thinking Without Parallel Chaos
- Chapter 29 — Automations: Recurring Work Without Recurring Prompts
- Chapter 30 — Computer Use, Browser Work, and GUI Tasks

**Explicit non-scope respected:** team workflow chapters, failure-mode catalog, playbooks, first serious app, senior checklist, field-practice expansion, updating chapter, full risk-managed shortcut chapter, constraints/cost/tool-stack chapters, other-AI chapter, limitations/biases chapters, pricing snapshots, and full shortcut cards beyond register references.

## Files Created

```text
vibe-coding-bible/
  CHUNK_9_REPORT.md
  chapters/
    27-cloud-delegation-parallel-work.md
    28-subagents-parallel-thinking.md
    29-automations-recurring-work.md
    30-computer-use-browser-gui-tasks.md
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

- Added `vcb.chapter.cloud_delegation_parallel_work`.
- Added `vcb.chapter.subagents_parallel_thinking`.
- Added `vcb.chapter.automations_recurring_work`.
- Added `vcb.chapter.computer_use_browser_gui_tasks`.
- Updated routing indexes for cloud delegation, parallel work, subagents, recurring automations, browser work, GUI safety, signed-in app risk, worktree isolation, and low-attention/background guardrails.
- Registered planned shortcut IDs used by Chunk 9 chapters and routing, including cloud-task context gaps, cloud work with real secrets, same-file parallel tasks, best-of-N without review, subagent swarms, parallel editing, unstable automations, automation spam, production GUI actions, browser use with secrets, unattended GUI work, and sensitive screen-context exposure.
- Added/verified tool-register anchors for `tool.codex_cloud`, `tool.codex_subagents`, `tool.codex_automations`, `tool.codex_computer_use`, `tool.codex_browser`, and `tool.codex_chrome_extension`.
- Normalized browser tool routing: `tool.codex_browser` is the canonical in-app browser tool ID; `tool.codex_chrome_extension` is a distinct signed-in Chrome workflow tool ID; the old noncanonical app-browser tool route is not used.
- Added official OpenAI source records for subagents, subagent concepts, cloud environments, Chrome extension, remote connections, proactive teammate automations, and computer-use workflows.
- Kept exact pricing, model routing, plan limits, exact UI command recipes, and context-window numbers out of stable prose.

## Routing and Source-Hygiene Revision

- Replaced the noncanonical app-browser tool route with `tool.codex_browser`.
- Registered `tool.codex_chrome_extension` in `TOOL_REGISTER.md` as a distinct signed-in Chrome workflow tool.
- Added `openai.codex.chrome_extension` and `openai.codex.remote_connections` to `SOURCE_REGISTER.md`.
- Updated Chapter 27 evidence to cite `openai.codex.remote_connections` for remote host/session behavior.
- Updated Chapter 30 evidence to cite `openai.codex.chrome_extension` and `openai.codex.remote_connections` for signed-in Chrome and remote GUI/browser context.
- Updated `scripts/validate_repository.py` to validate tool IDs in indexes, tool IDs in the active chunk report, source IDs in the active chunk report, and browser/Chrome tool namespace consistency.

## Sources Checked

- `openai.codex.cloud` — official Codex web/cloud source for background tasks, parallel work, GitHub connection, and PR-capable delegated work.
- `openai.codex.cloud_environments` — official source for cloud environment setup, setup/maintenance scripts, cached containers, task checks, diffs, environment variables, and secrets behavior.
- `openai.codex.cloud_internet_access` — official source for internet-access default posture, prompt-injection/exfiltration risk, allowlists, and network controls.
- `openai.codex.workflows` — official source for local-to-cloud workflow patterns and reviewable cloud diffs.
- `openai.codex.subagents` and `openai.codex.subagent_concepts` — official sources for subagent spawning, orchestration, custom agents, context pollution/rot, and read-heavy versus write-heavy tradeoffs.
- `openai.codex.app_automations`, `openai.codex.best_practices`, `openai.codex.use_cases.automation_bug_triage`, and `openai.codex.use_cases.proactive_teammate` — official sources for recurring tasks, stable workflow promotion, inbox/signal reports, and schedule-based Codex work.
- `openai.codex.app_computer_use`, `openai.codex.app_browser`, `openai.codex.chrome_extension`, `openai.codex.remote_connections`, and `openai.codex.use_cases.qa_computer_use` — official sources for Computer Use, in-app browser/browser use, signed-in Chrome context, remote connected hosts, app approvals, sensitive-flow cautions, and GUI bug reports.

## Validation Summary

```text
VCB validation passed
Actual source files tracked in manifest: 96
Manifest source-file inventory matches actual package files: yes
source_files rich objects preserved: yes
Markdown files: 72
Markdown files with frontmatter/metadata fences: 72 / 72
Markdown files with VCB markers: 72 / 72
JSON files: 8
JSON parse check: passed
JSON Schema draft compile check: passed
Active chapter/topic files validated: 37
Active chapter/topic frontmatter schema validation: passed
Shortcut IDs registered: 77
Tool IDs registered: 20
Required Markdown headings present in active chapter/topic files: passed
VCB section marker pairing in active chapter/topic files: passed
New chapter files created in Chunk 9: 4
New chapter frontmatter schema validation: passed, 4 / 4
Required Chunk 9 files present: passed
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
Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed
Planned shortcut index routes resolve to SHORTCUT_REGISTER or approved future shortcut IDs: passed
Evidence source IDs resolve to SOURCE_REGISTER or declared synthesis IDs: passed
Planned tool IDs in indexes resolve to TOOL_REGISTER: passed
Active chunk report source IDs resolve to SOURCE_REGISTER: passed
Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed
Browser/Chrome tool namespace consistency check: passed
SHORTCUT_REGISTER table row shape: passed
Duplicate shortcut IDs in SHORTCUT_REGISTER: none
Duplicate source IDs in SOURCE_REGISTER: none
Duplicate tool IDs in TOOL_REGISTER: none
evidence_basis/source_kind values validated against schemas: passed
Official-source anchors checked for cloud/subagents/automations/computer-use claims: passed
No exact pricing, limits, model-routing, current UI command recipes, or context-window numbers added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

Known exception: `.gitkeep` files are structural placeholders and intentionally contain no frontmatter or VCB markers.

## Design Decisions

1. **Cloud delegation is scoped delegation, not unattended trust.** Chapter 27 centers task packets, branch/worktree isolation, diff review, and local verification.
2. **Subagents are specialists, not swarms.** Chapter 28 defaults to bounded analysis/review roles and keeps one main agent responsible for synthesis.
3. **Automations start report-only.** Chapter 29 treats schedules as a multiplier for workflow stability; manual dry runs and no-op behavior come first.
4. **Computer Use is capability plus account blast radius.** Chapter 30 uses a tool ladder: structured tools/API/MCP first, in-app browser for local/public pages, signed-in browser only when needed, and production GUI actions only with supervision.
5. **Product mechanics stayed volatile.** Exact UI flows, invocation syntax, model controls, plan access, pricing, limits, and platform-specific behavior are not treated as stable principles.

## Unresolved Questions

1. Whether cloud delegation should later split into separate topic cards for cloud environment setup, internet access, GitHub delegation, local-change handoff, and PR creation.
2. Whether subagents should later split into analysis-only subagents, custom agent configuration, subagent review boards, and parallel implementation guardrails.
3. Whether automations should later split into thread automations, standalone/project automations, worktree cleanup, and automation-noise control.
4. Whether Computer Use should later split into in-app browser, Chrome extension, desktop Computer Use, signed-in browser risk, remote connections, and GUI QA reports.
5. Whether duplicate-source-URL detection should become a hard validator check after source-register cleanup.

## Next Recommended Chunk

**Chunk 10**, only after editor approval:

- Chapter 31 — From Prompt Library to Team Workflow
- Chapter 32 — Failure Modes: How Codex Work Goes Wrong
- Chapter 33 — The Codex Playbooks
- Chapter 34 — Building Your First Serious App with Codex
- Chapter 35 — The Senior Engineer Checklist for Vibe Coders

Do not start Chunk 11 field-practice/updating/shortcut-chapter material yet.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.9 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
