---
id: vcb.report.chunk_13
chunk_id: chunk_13_foundational_concept_cards
title: Chunk 13 Report — Foundational Concept Cards
artifact_type: chunk_report
version: 0.14.0-draft.chunk13
status: waiting_for_editor_review
last_verified: 2026-06-09
next_review_due: 2026-09-09
review_cadence: quarterly
---

<!-- VCB:BEGIN_REPORT id=vcb.report.chunk_13 version=0.14.0-draft.chunk13 -->

# Chunk 13 Report — Foundational Concept Cards

## Chunk ID and Scope

**Chunk ID:** `chunk_13_foundational_concept_cards`

**Scope completed:** individual topic-card expansion for the first bounded foundational concept slice:

- `vcb.concepts.api_basics` — API Basics
- `vcb.concepts.frontend_backend` — Frontend vs Backend
- `vcb.concepts.database_schema` — Database Schema
- `vcb.concepts.authentication` — Authentication
- `vcb.concepts.authorization` — Authorization
- `vcb.concepts.state` — State
- `vcb.concepts.async` — Async and Timing
- `vcb.concepts.dependency` — Dependency
- `vcb.concepts.test` — Test
- `vcb.concepts.typecheck` — Typecheck
- `vcb.concepts.lint` — Lint
- `vcb.concepts.migration` — Migration
- `vcb.concepts.environment_variable` — Environment Variable
- `vcb.concepts.build_step` — Build Step
- `vcb.concepts.ci` — CI
- `vcb.concepts.feature_flag` — Feature Flag
- `vcb.concepts.observability` — Observability

**Explicit non-scope:** full tool-card expansion, full shortcut-card expansion, field-practice cards, Codex feature cards, workflow cards, and new narrative chapters.

## Revision Fixes Applied

- Updated `llms.txt` and `llms-full.txt` begin-marker versions to `0.14.0-draft.chunk13`.
- Replaced stale Chunk 10/12 visible source-map headings with current/chunk-neutral routing sections.
- Moved Chunk 13 concept-card fast routing before the retrieval rule in `llms.txt`.
- Added missing source-register rows for `jest.docs_getting_started`, `nodejs.docs_environment_variables`, and `openfeature.docs_intro`.
- Moved Chunk 13 source rows into a valid `SOURCE_REGISTER.md` source table above `## Notes`.
- Fixed `vcb.concepts.feature_flag` evidence metadata to use OpenFeature as the official definition anchor and Martin Fowler as supporting expert evidence.
- Set `source_status.official_openai: true` on active concept cards whose Evidence and Sources sections cite `openai.*` source IDs.
- Extended `scripts/validate_repository.py` to catch stale LLM source-map markers/headings, source-register placement issues, report source-ID drift across all prefixes, official OpenAI metadata drift, and feature-flag source metadata drift.

## Files Created

```text
topics/concepts/api-basics.md
topics/concepts/frontend-backend.md
topics/concepts/database-schema.md
topics/concepts/authentication.md
topics/concepts/authorization.md
topics/concepts/state.md
topics/concepts/async.md
topics/concepts/dependency.md
topics/concepts/test.md
topics/concepts/typecheck.md
topics/concepts/lint.md
topics/concepts/migration.md
topics/concepts/environment-variable.md
topics/concepts/build-step.md
topics/concepts/ci.md
topics/concepts/feature-flag.md
topics/concepts/observability.md
CHUNK_13_REPORT.md
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

## Design Decisions

1. **Concept cards stayed atomic.** Each card teaches one reusable software concept and links to higher-level chapters rather than becoming a workflow chapter.
2. **Official/vendor sources anchor definitions.** MDN, OWASP, PostgreSQL, Prisma, React, npm, Jest, Node.js, TypeScript, ESLint, Liquibase, Flyway, Vite, webpack, GitHub, OpenFeature, Martin Fowler, and OpenTelemetry sources were added where appropriate.
3. **Codex-specific advice is labeled as synthesis.** The cards use official/vendor/expert sources for definitions and `vcb.synthesis.stable_engineering_practice` for Codex coaching/risk posture.
4. **No tool-card expansion.** Tool mentions stay as concept anchors. Full tool cards remain future work.
5. **No exact pricing or current limits.** Chunk 13 contains stable concept material only.

## Sources Checked

Official source anchors were checked for this bounded foundational concept-card slice. The new cards use stable concept sources rather than current pricing, plan limits, model routing, or UI-command recipes. OpenFeature official docs were checked for feature-flag definitions; Jest official docs were checked for a concrete test-file/test-command example; Node.js official docs were checked for `process.env` and `.env` environment-variable concepts.

Source IDs added or used in the new concept cards include:

- `mdn.glossary.api`
- `mdn.learn_web_apis`
- `mdn.learn_web_development`
- `mdn.curriculum_frontend`
- `owasp.rest_security`
- `postgres.docs.schemas`
- `prisma.docs.schema`
- `prisma.docs.models`
- `owasp.authentication_cheat_sheet`
- `owasp.session_management`
- `owasp.authorization_cheat_sheet`
- `react.docs.state_memory`
- `react.docs.managing_state`
- `mdn.js.promises`
- `mdn.async_javascript`
- `npm.docs.package_json`
- `npm.docs.package_dependencies`
- `github.docs.dependency_review`
- `openai.codex.guide_ai_native_engineering_team`
- `jest.docs_getting_started`
- `typescript.docs.home`
- `typescript.docs.basic_types`
- `eslint.docs.home`
- `eslint.docs.latest`
- `nodejs.docs_environment_variables`
- `twelve_factor.config`
- `vite.docs.build`
- `webpack.docs.concepts`
- `github.docs.actions_overview`
- `github.docs.actions_ci`
- `github.docs.actions_secure_use`
- `openfeature.docs_intro`
- `martin_fowler.feature_toggles`
- `opentelemetry.docs.what_is_opentelemetry`
- `opentelemetry.docs.observability_primer`
- `sentry.docs.platform`

## Validation Summary

```text
VCB validation passed
active chapter/topic files validated: 70
shortcut IDs registered: 98
tool IDs registered: 41
pricing snapshots active: 1
Manifest source-file inventory matches actual package files: yes
Manifest source_artifacts inventory matches actual package files: passed
Manifest all_tracked_files matches source_files and actual package files: passed
Canonical review package references are consistent across manifest fields: passed
New concept topic files created in Chunk 13: 17
New concept frontmatter schema validation: passed, 17 / 17
Required Chunk 13 concept-card slice present: passed
Required topic sections present: passed
Required VCB markers present in new concept files: passed
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
Active chunk report source IDs resolve to SOURCE_REGISTER across all source prefixes: passed
Active chunk report tool-anchor claims resolve to TOOL_REGISTER: passed
source_status.official_vendor matches Evidence and Sources sections: passed
source_status.official_openai matches Evidence and Sources sections: passed
llms.txt begin marker version matches frontmatter/current chunk: passed
llms-full.txt begin marker version matches frontmatter/current chunk: passed
LLM source-map visible active-chunk headings are current or chunk-neutral: passed
Feature-flag concept source metadata matches cited evidence: passed
SOURCE_REGISTER Chunk 13 rows are inside a valid source table: passed
Duplicate source URL detection: passed
No exact pricing, limits, model-routing, context-window numbers, or unstable UI-command recipes added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```


## Unresolved Questions

1. Whether Chunk 14 should expand Codex feature cards first or workflow topic cards first. Recommended: Codex feature cards, because many existing chapters already reference them as retrieval targets.
2. Whether `vcb.concepts.authentication` and `vcb.concepts.authorization` should later receive security-specific companion workflow cards for threat modeling, policy testing, and production red lines.
3. Whether `vcb.concepts.database_schema` should later split relational schema, ORM schema, and data-modeling pitfalls into separate cards.
4. Whether `vcb.concepts.observability` should later split into logs, metrics, traces, errors, and audit events.

## Next Recommended Chunk

**Chunk 14**, only after editor approval:

- `vcb.codex.app`
- `vcb.codex.cli`
- `vcb.codex.ide_extension`
- `vcb.codex.cloud`
- `vcb.codex.github_review`
- `vcb.codex.config`
- `vcb.codex.agents_md`
- `vcb.codex.skills`
- `vcb.codex.mcp`
- `vcb.codex.hooks`
- `vcb.codex.automations`
- `vcb.codex.subagents`
- `vcb.codex.computer_use`
- `vcb.codex.feature_maturity`
- `vcb.codex.changelog_monitoring`

Do not start full tool-card expansion, shortcut-card expansion, or field-practice cards in Chunk 14.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.report.chunk_13 -->

AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
