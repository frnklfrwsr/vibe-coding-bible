<!-- VCB:BEGIN_REPORT id=vcb.report.chunk_36 version=0.37.0-draft.chunk36 -->
---
id: vcb.report.chunk_36
title: Chunk 36 Report — Local Dev, Design, and Project-Management Tool Cards
artifact_type: chunk_report
version: 0.37.0-draft.chunk36
status: waiting_for_editor_review
chunk_id: chunk_36_local_dev_design_project_management_tool_cards
last_verified: '2026-06-11'
---

# Chunk 36 Report — Local Dev, Design, and Project-Management Tool Cards

## Scope

Chunk 36 authored a bounded Docker/container, design/prototyping, and project-management tool-card slice only.

Active tool cards created:

- `tool.docker`
- `tool.figma`
- `tool.linear`

Out of scope and not started:

- category placeholder cards;
- email/documentation/security-secrets tool-category cards;
- new AI-tool cards;
- new app-builder cards;
- new hosting/database/auth/payment/observability cards;
- field-practice-card expansion;
- pricing expansion;
- broad workflow expansion;
- broad shortcut expansion;
- new shortcut-card expansion;
- broad security/secrets expansion;
- narrative chapters.

## Created files

- `CHUNK_36_REPORT.md`
- `topics/tool-catalog/docker.md`
- `topics/tool-catalog/figma.md`
- `topics/tool-catalog/linear.md`

## Updated files

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
- `TOOL_REGISTER.md`
- `CHANGELOG.md`
- `TREE.txt`
- `scripts/validate_repository.py`
- `indexes/GLOSSARY.md`
- `indexes/INDEX_BY_TOOL_CATEGORY.md`
- `indexes/INDEX_BY_TASK.md`
- `indexes/INDEX_BY_PROJECT_TYPE.md`
- `indexes/INDEX_BY_RISK_LEVEL.md`
- `indexes/INDEX_BY_RECOVERABILITY.md`
- `indexes/INDEX_BY_FAILURE_MODE.md`
- `indexes/PROMPT_LIBRARY.md`
- `indexes/INDEX_FOR_AI_COACHES.md`
- `indexes/INDEX_BY_CONCEPT.md`
- `indexes/INDEX_BY_STABILITY.md`
- `indexes/INDEX_BY_BUDGET_PROFILE.md`

## Source posture

Chunk 36 added official vendor source rows for Docker, Figma, and Linear plus the editor-feedback gate source for the approved Chunk 36 scope. The cards use official vendor documentation for stable product framing and keep exact pricing, plan limits, seat limits, quota limits, Docker Desktop licensing details, current UI labels, command flags, Compose/build/runtime defaults, container/security defaults, Figma feature availability, export/dev-mode mechanics, Linear workflow/status mechanics, integrations, automation behavior, and current capability claims out of stable prose unless they are explicitly routed to volatile/source-checked posture.

## Repository routing and governance changes

- `README.md` now identifies `chunk_36_local_dev_design_project_management_tool_cards` as the current chunk and exposes the active Docker, Figma, and Linear tool-card routes.
- `TOOL_REGISTER.md` marks `tool.docker`, `tool.figma`, and `tool.linear` active and records the Chunk 36 activation note.
- `SOURCE_REGISTER.md` records official Docker, Figma, and Linear source anchors.
- `llms.txt` and `llms-full.txt` now include Chunk 36 active-content statements, fast-routing sections, and active Chunk 36 tool-card lists.
- Primary indexes now route Docker/container/local reproducibility, Figma/design handoff/prototyping, and Linear/project-management intent to the active tool cards before older chapter, workflow, shortcut, or concept fallbacks.
- `manifest.json` now records Chunk 36 active scope, active tool-card mappings, canonical review package metadata, source inventory, and next-chunk gate state.

## Validator coverage added

`scripts/validate_repository.py` was tightened for Chunk 36 repository-contract coverage, including:

- tool-card schema validation;
- TOOL_REGISTER active status;
- official vendor source posture;
- `SOURCE_REGISTER.md` source-anchor coverage;
- `README.md` active tool-card routing;
- LLM source-map routing;
- semantic index routing for task, project-type, risk, recoverability, failure, prompt-library, AI-coach, glossary, concept, stability, and budget lookup paths;
- scope guardrails preventing unrelated tool-card, pricing, field-practice, shortcut, or narrative expansion;
- report inventory coverage.

## Revision Notes

- Revision after editor review repaired `indexes/INDEX_BY_FAILURE_MODE.md` / `## UI works but has poor taste, states, or accessibility` so `tool.figma` appears before UI-generation, browser-test, workflow, and failure-mode fallbacks.
- Revision after editor review repaired `indexes/INDEX_BY_FAILURE_MODE.md` / `## Team workflow creates ceremony without reducing risk` so `tool.linear` appears before chapter and shortcut fallbacks.
- Revision after editor review repaired `indexes/INDEX_BY_TASK.md` / `## Turn prompts into team workflow` so `tool.linear` routes repeated work into issues, projects, workflow status, ownership, cycles, or team execution hygiene before chapter fallbacks.
- Revision after editor review repaired `indexes/INDEX_BY_PROJECT_TYPE.md` / `## Personal local tool` so `tool.docker` routes local containers, services, reproducible setup, Dockerized checks, and resettable isolation evidence before concept/chapter fallbacks.
- Revision after editor review repaired `topics/tool-catalog/figma.md` by replacing redirected shortcut-profile alias `vcb.shortcut.screenshot_only_verification` with canonical active shortcut `vcb.shortcut.browser_clicking_without_repro`.
- Revision after editor review tightened `scripts/validate_repository.py` for those exact semantic sections and for redirected shortcut-profile aliases in current-chunk tool cards.

## Validation

Final validator result:

```text
VCB validation passed
active chapter/topic files validated: 221
shortcut IDs registered: 98
tool IDs registered: 46
pricing snapshots active: 1
```

## Package hygiene

Authoritative package:

```text
vibe-coding-bible-chunk-36-revision-20260611T163000Z-authoritative.zip
```

Package hygiene:

```text
zip entries: 308
unique entries: 308
duplicates: 0
directory-only entries: 0
__pycache__ / .pyc entries: 0
files extracted: 308
```

## Notes for editor

Chunk 36 deliberately kept the slice small because it includes three third-party/vendor tool cards with source-register, register, LLM-map, semantic-index, manifest, and validator updates. No broader tool family or pricing/source-map cleanup was combined with the slice.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.report.chunk_36 -->

AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
