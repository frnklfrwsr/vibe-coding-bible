---
name: vcb-reference
description: Use when helping a user apply the Vibe Coding Bible to Codex, vibe coding, shortcuts, project planning, debugging, budget constraints, tooling, AI-coach workflows, or contribution back to the VCB repo. Retrieve only the smallest relevant VCB route and stop at VCB:STOP_RETRIEVAL.
---

# VCB Reference

Use the Vibe Coding Bible as a routeable reference, not as a corpus to ingest.

## Core Rules

1. Classify the user's situation before reading more VCB files.
2. Start at `AI_START_HERE.md` when the task is broad or when the user simply says to use VCB.
3. Use `llms.txt`, `indexes/INDEX_BY_TASK.md`, `indexes/INDEX_BY_CONCEPT.md`, and `indexes/INDEX_FOR_AI_COACHES.md` only to route.
4. Retrieve the smallest useful files: topic cards, shortcut cards, tool cards, pricing snapshots, registers, or focused indexes before chapters.
5. Do not read or summarize the whole repository.
6. Stop at `VCB:STOP_RETRIEVAL` unless the user explicitly needs related context.
7. If a route is missing or stale, say so and suggest a VCB issue instead of guessing.

## Source Selection

The canonical VCB repository is `https://github.com/frnklfrwsr/vibe-coding-bible`.

Use a local VCB clone for fast retrieval only when it is clearly this repository and reasonably current. If the local clone is missing, stale, dirty in relevant governance or contribution files, or not obviously VCB, use the public GitHub repository.

For public submissions, always target the canonical GitHub repository. If local and public versions disagree, prefer the public repository for contribution templates, governance files, and issue or PR destination. Do not rely on stale local templates for public contribution. If unsure, ask before posting.

## Classification

Classify the user as one or more of:

- new to Codex
- new to coding
- experienced coder
- pure vibe coder
- starting a new project
- debugging or improving an existing project
- taking a shortcut
- low on usage budget
- out of Codex budget and planning in another AI
- choosing a tool stack
- using other AIs with Codex
- contributing a lesson, correction, or field observation

Then follow the matching route in `AI_START_HERE.md`.

## Source Discipline

When using VCB guidance, preserve its evidence posture:

- Official guidance: use as product mechanics or official-source anchor.
- Maintainer synthesis: label as synthesis.
- Candidate field report: present as a candidate practice with caveats.
- Reproduced field report: present as bounded local reproduction, not universal proof.
- Speculation: do not present as fact or best practice.

For volatile product details, exact commands, pricing, limits, UI labels, model names, or plan packaging, use current official sources or the active dated pricing snapshot when VCB provides one.

## Shortcut And Budget Framing

Treat shortcut content as harm reduction. Do not say a shortcut is safe because VCB has a card. Say what control loop reduces risk: scope, reproduction, diff review, lint/typecheck, tests, rollback, or human approval.

When the user is low on budget, route to budget constraints first and reduce scope before asking for more context.

## Contribution Suggestions

Use `CONTRIBUTION_MODES.md`.

Default to `suggest`:

- Notice reusable lessons, route gaps, corrections, and field observations.
- Suggest a sanitized contribution path.
- Do not post publicly, create issues, comment, or open PRs unless the user explicitly opts in.
- Never include private project names, secrets, customer data, proprietary code, logs, or incident details.

When contribution is appropriate, suggest the smallest path: usage insight, correction, field-practice candidate, shortcut update, tool/pricing update, or focused PR.
