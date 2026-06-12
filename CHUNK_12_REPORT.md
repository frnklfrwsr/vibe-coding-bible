---
id: vcb.chunk_report.chunk_12
title: CHUNK_12_REPORT
artifact_type: chunk_report
version: 0.13.0-draft.chunk12
status: waiting_for_editor_review
chunk_id: chunk_12_constraints_costs_tools_limitations
created_on: 2026-06-09
last_verified: 2026-06-09
next_review_due: 2026-07-09
review_cadence: monthly
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_12 version=0.13.0-draft.chunk12 -->

# CHUNK_12_REPORT

## Scope Completed

Chunk 12 only:

- Chapter 39 — Choosing Your Codex Operating Mode
- Chapter 40 — Plus vs Pro vs API vs Team: Budget-Aware Codex Workflows
- Chapter 41 — Build Phase vs Maintenance Phase
- Chapter 42 — The Tool Stack Catalog
- Chapter 43 — Cost-Benefit Analysis for Vibe Coders
- Chapter 44 — When to Use Other AIs With Codex
- Chapter 45 — What Codex Is Bad At
- Chapter 46 — Model Biases, Failure Biases, and Bad Estimates

No Chunk 13 individual topic-card expansion was started.


## Revision Fixes Applied

- Corrected `manifest.pricing_snapshot_ids` so `vcb.pricing_snapshot.openai_codex` routes to `pricing-snapshots/2026-06-09-openai-codex.md`.
- Added active/deferred pricing-snapshot split: `vcb.pricing_snapshot.openai_codex` is active; non-OpenAI tool/hosting/database/observability snapshots remain deferred.
- Removed the stale planned route for the active OpenAI pricing snapshot from `indexes/INDEX_BY_STABILITY.md`; the remaining route is `active_snapshot`.
- Updated `SOURCE_REGISTER.md` so `openai.codex.pricing` points to the accepted dated snapshot instead of saying the snapshot is deferred.
- Fixed Chapter 43 source-status metadata to `official_vendor: true` because it cites non-OpenAI vendor anchors.
- Fixed Chapter 44 source-status metadata to `official_vendor: false` because vendor-specific non-OpenAI AI claims are deferred to future tool cards.
- Removed the duplicate “Assign one implementer” bullet in Chapter 44.
- Extended `scripts/validate_repository.py` to check pricing snapshot routing/status consistency and `source_status.official_vendor` consistency.

## Files Created

```text
CHUNK_12_REPORT.md
chapters/39-choosing-codex-operating-mode.md
chapters/40-budget-aware-codex-workflows.md
chapters/41-build-phase-vs-maintenance-phase.md
chapters/42-tool-stack-catalog.md
chapters/43-cost-benefit-analysis-for-vibe-coders.md
chapters/44-when-to-use-other-ais-with-codex.md
chapters/45-what-codex-is-bad-at.md
chapters/46-model-biases-failure-biases-bad-estimates.md
pricing-snapshots/2026-06-09-openai-codex.md
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
PRICING_SNAPSHOT_REGISTER.md
CHANGELOG.md
TREE.txt
scripts/validate_repository.py
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

- Added constraint and operating-mode chapters for workflow selection by budget, attention, phase, risk, and recoverability.
- Added budget-aware Codex workflow guidance without hardcoding exact pricing in stable chapter prose.
- Added the first dated exact pricing snapshot: `vcb.pricing_snapshot.openai_codex`.
- Added the tool-stack catalog chapter and cost-benefit chapter.
- Added multi-AI coordination guidance.
- Added Codex limitation and model-bias chapters.
- Expanded source, shortcut, tool, task, budget, failure-mode, risk, recoverability, glossary, prompt, and AI-coach routing.
- Added duplicate-source-URL detection to the repository validator.
- Added `evidence_scope` to chapter/topic schemas.
- Revision fixed pricing-snapshot routing/status metadata, source-register pricing wording, and source-status flags found during editor review.
- Revision expanded the validator to check pricing snapshot file resolution, active/planned snapshot drift, stability-index snapshot status conflicts, source-register pricing language, and `source_status.official_vendor` consistency.
- Revised pricing-snapshot routing so active OpenAI/Codex snapshot metadata points to `pricing-snapshots/2026-06-09-openai-codex.md`.
- Moved `vcb.pricing_snapshot.openai_codex` from planned to active snapshot status across manifest and stability index routes.
- Aligned `source_status.official_vendor` metadata with Evidence and Sources sections.
- Revision: corrected active pricing-snapshot routing/status, pricing source-register language, Chapter 43/44 official-vendor source-status metadata, and validator coverage for those checks.

## Sources Checked

- `openai.codex.pricing` — official Codex pricing and plan-limit anchor.
- `openai.help.codex_chatgpt_plan` — official Help Center source for plan-based Codex usage.
- `openai.help.codex_rate_card` — official Help Center token-based Codex credit rate card.
- `openai.chatgpt.pricing` — official ChatGPT plan-packaging source.
- `openai.codex.best_practices` — official Codex source for planning, validation, and durable workflow guidance.
- `openai.help.truthfulness` and `openai.hallucinations` — official OpenAI anchors for wrong/confident model-output caveats.
- Official vendor anchors were added for Vercel, Supabase, Stripe, GitHub Actions billing, Clerk, Auth0, Sentry, and PostHog.

## Validation Summary

```text
VCB validation passed
active chapter/topic files validated: 53
shortcut IDs registered: 98
tool IDs registered: 41
pricing snapshots active: 1
Manifest source-file inventory matches actual package files: yes
Manifest source_artifacts inventory matches actual package files: passed
Manifest all_tracked_files matches source_files and actual package files: passed
Canonical review package references are consistent across manifest fields: passed
New chapter files created in Chunk 12: 8
New chapter frontmatter schema validation: passed, 8 / 8
Required Chunk 12 files present: passed
Required chapter sections present: passed
Required VCB markers present in new chapter files: passed
Pricing snapshot created for OpenAI/Codex exact volatile values: passed
Active pricing snapshot IDs resolve to existing pricing-snapshot files: passed
Planned pricing snapshot IDs are explicitly deferred: passed
Pricing snapshot IDs resolve to existing pricing-snapshot files or explicit deferred entries: passed
Active pricing snapshot IDs are not listed as planned: passed
Stability index pricing-snapshot routes have one canonical status: passed
Source-register pricing rows reflect current snapshot status: passed
Pricing snapshot frontmatter validates against pricing-snapshot schema: passed
Duplicate source URL detection: passed
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
Planned tool IDs in indexes resolve to TOOL_REGISTER: passed
Evidence source IDs resolve to SOURCE_REGISTER or declared synthesis IDs: passed
Active chunk report source IDs resolve to SOURCE_REGISTER: passed
Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed
SHORTCUT_REGISTER table row shape: passed
FIELD_PRACTICES table row shape: passed
evidence_basis/source_kind/evidence_scope values validated against schemas: passed
source_status.official_vendor matches Evidence and Sources sections: passed
No exact non-OpenAI pricing, current model-routing recipes, or context-window numbers added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

## Design Decisions

1. Chapter 42 is a catalog overview, not a complete tool-card expansion. Full tool-card work belongs to future topic-card chunks.
2. Chapter 40 separates durable cost strategy from volatile current plan facts. Exact OpenAI/Codex rate-card values live in the dated snapshot.
3. Other vendor pricing anchors were registered, but their exact prices were not copied into stable prose or snapshot files.
4. Chapter 45 and Chapter 46 overlap intentionally: Chapter 45 names capability limits; Chapter 46 names predictable cognitive/model failure patterns and guardrails.
5. The validator now rejects duplicate source URLs to reduce future source-register ambiguity.
6. The active OpenAI/Codex pricing snapshot is now treated as `active_snapshot`; other exact vendor pricing snapshots remain explicit deferred future work.

## Unresolved Questions

1. Which Chunk 13 topic-card slice should come first: remaining concept cards, tool cards, shortcut cards, or limitation/failure-mode cards.
2. Whether each tool category in Chapter 42 should get its own tool-card batch before or after remaining concept-card expansion.
3. Whether non-OpenAI vendor pricing snapshots should be captured category-by-category or only when a tool card becomes active.
4. Whether plan/usage advice should later split into separate cards for subscription, API, team/workspace, and temporary-upgrade strategies.

## Next Recommended Chunk

**Chunk 13**, only after editor approval:

- Expand individual topic cards until coverage is complete.
- Recommended first slice: missing foundational concept cards such as API basics, frontend/backend, database schema, authentication, authorization, state, async, dependency, test, typecheck, lint, migration, environment variables, build step, CI, feature flags, and observability.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_12 -->

AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
