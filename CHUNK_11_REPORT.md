---
id: vcb.chunk_report.chunk_11
chunk_id: chunk_11_field_practices_updating_shortcuts
title: "Chunk 11 Report — Field Practices, Updating, and Risk-Managed Shortcuts"
artifact_type: chunk_report
version: 0.12.0-draft.chunk11
status: waiting_for_editor_review
created_on: 2026-06-09
last_verified: 2026-06-09
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_11 version=0.12.0-draft.chunk11 -->

# Chunk 11 Report — Field Practices, Updating, and Risk-Managed Shortcuts

## Scope Completed

Chunk 11 only:

- Chapter 36 — Field Notes: Unofficial and User-Discovered Codex Practices
- Chapter 37 — Maintaining and Updating the Bible
- Chapter 38 — Risk-Managed Shortcuts: When Users Ignore Best Practices

No Chunk 12 material was started. Constraints/cost/plans/tool-catalog/other-AI/limitations/biases chapters remain non-scope.

## Files Created

```text
vibe-coding-bible/
  CHUNK_11_REPORT.md
  chapters/
    36-field-notes-unofficial-practices.md
    37-maintaining-and-updating-the-bible.md
    38-risk-managed-shortcuts.md
```

## Files Updated

```text
README.md
manifest.json
llms.txt
llms-full.txt
SOURCE_REGISTER.md
FIELD_PRACTICES.md
SHORTCUT_REGISTER.md
UPDATE_PROTOCOL.md
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

- Added `vcb.chapter.field_notes_unofficial_practices`.
- Added `vcb.chapter.maintaining_updating_bible`.
- Added `vcb.chapter.risk_managed_shortcuts`.
- Expanded `FIELD_PRACTICES.md` with status labels, promotion rules, candidate practice routing, review triggers, and a field-practice evaluation prompt.
- Expanded `SHORTCUT_REGISTER.md` with shortcut expansion policy, production red-line shortcut families, and guardrail escalation rule.
- Updated `UPDATE_PROTOCOL.md` with field-practice promotion and shortcut-update rules.
- Updated routing indexes for field-practice evaluation, Bible maintenance, deprecation hygiene, risk-managed shortcuts, and shortcut guardrail prompts.
- Kept exact pricing, plan limits, model-routing rules, context-window numbers, UI recipes, and Chunk 12 topics out of stable prose.

## Sources Checked

- `openai.codex.best_practices` — official OpenAI source for reusable guidance, plan-first work, validation, review, and durable project instructions.
- `openai.codex.customization` — official OpenAI source for updating durable guidance such as AGENTS.md when Codex makes repeated assumptions.
- `openai.codex.use_cases.reusable_codex_skills` — official OpenAI use-case anchor for turning repeated workflows into skills.
- `openai.codex.changelog` — official OpenAI source for product-change monitoring.
- `openai.codex.feature_maturity` — official OpenAI source for maturity/volatility labels.
- `openai.codex.llms_txt` and `openai.codex.llms_full` — official OpenAI source-map anchors for LLM-ingestible documentation.
- `openai.codex.use_cases.update_documentation` — official OpenAI example for keeping documentation aligned with source changes.
- `openai.codex.security` and `openai.codex.cloud_internet_access` — official OpenAI anchors for security-sensitive shortcut red lines.
- `aws.well_architected.design_principles` — official vendor anchor for small reversible changes and blast-radius reduction.

## Revision Fixes

- Rebuilt `manifest.source_artifacts` so nested report/chapter/index/schema/register/protocol buckets match the actual package inventory.
- Updated all manifest canonical-review-package references to the current Chunk 11 revision package.
- Normalized `FIELD_PRACTICES.md` status values so `Current register status` uses declared labels only.
- Added a separate `Promotion path` column instead of slash-combining status values such as `candidate/promotable`.
- Added validator checks for nested manifest inventory, canonical package consistency, field-practice table shape, and declared field-practice statuses.
- Added `evidence_scope` to Chapter 36 frontmatter to clarify that official evidence supports the policy framework while individual field practices keep their own E4/E2/E3 labels.

## Validation Summary

```text
VCB validation passed
active chapter/topic files validated: 45
shortcut IDs registered: 88
tool IDs registered: 20
Manifest source-file inventory matches actual package files: yes
Manifest source_artifacts inventory matches actual package files: passed
Manifest all_tracked_files matches source_files and actual package files: passed
Canonical review package references are consistent across manifest fields: passed
Field-practice register statuses match declared Status Labels: passed
FIELD_PRACTICES table row shape: passed
New chapter files created in Chunk 11: 3
New chapter frontmatter schema validation: passed, 3 / 3
Required Chunk 11 files present: passed
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
SHORTCUT_REGISTER table row shape: passed
evidence_basis/source_kind values validated against schemas: passed
Field-practice register expanded without promoting anecdotal practices to official guidance: passed
Shortcut expansion policy added without authoring full shortcut cards: passed
No exact pricing, limits, model-routing, context-window numbers, or unstable UI-command recipes added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

## Design Decisions

1. **Field practices are candidate records, not official guidance.** Chapter 36 and `FIELD_PRACTICES.md` label practices conservatively and require reproduction, named evidence, or official support before promotion.
2. **Shortcut expansion stayed at chapter/register level.** Chunk 11 expanded the shortcut policy and overview without creating individual shortcut topic cards, preserving the approved chapter-only scope.
3. **Update guidance treats metadata as content.** Chapter 37 emphasizes metadata, source registers, indexes, deprecation, and validator checks before prose cleanup.
4. **No exact pricing or volatile product recipes.** Product-specific commands, prices, limits, model advice, and UI flows remain volatile or deferred.
5. **No Chunk 12 drift.** Operating-mode, plan/budget, tool-stack, other-AI, limitation, and bias chapters are left for Chunk 12.

## Unresolved Questions

1. Which field practices should become full topic cards first after the core chapter sequence completes.
2. Whether the validator should eventually enforce field-practice table shape and promotion-state transitions.
3. Whether duplicate source URL detection should become strict validation or a report-only warning because some duplicate official anchors are intentional aliases.
4. Whether Chapter 38 should later split into one topic card per high-value shortcut family.

## Next Recommended Chunk

**Chunk 12**, only after editor approval:

- Chapter 39 — Choosing Your Codex Operating Mode
- Chapter 40 — Plus vs Pro vs API vs Team: Budget-Aware Codex Workflows
- Chapter 41 — Build Phase vs Maintenance Phase
- Chapter 42 — The Tool Stack Catalog
- Chapter 43 — Cost-Benefit Analysis for Vibe Coders
- Chapter 44 — When to Use Other AIs With Codex
- Chapter 45 — What Codex Is Bad At
- Chapter 46 — Model Biases, Failure Biases, and Bad Estimates

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_11 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
