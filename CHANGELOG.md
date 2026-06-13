---
id: vcb.register.changelog
title: The Vibe Coding Bible Changelog
artifact_type: changelog
version: 1.0.1-post-release.issue23.chunk45
status: chunk_45_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: monthly
---

<!-- VCB:BEGIN_CHANGELOG id=vcb.register.changelog version=1.0.1-post-release.issue23.chunk45 -->

# CHANGELOG

## Chunk 45 - Issue #23 Usage-Insight Triage

- Triaged Issue #23 as a sanitized usage-insight contribution.
- Added one candidate field-practice/workflow-pattern card: `vcb.field.contract_first_segmented_handoffs`.
- Kept the evidence level at `E4_COMMUNITY_FIELD_REPORT`; the card is not official guidance, not reproduced locally, and not promoted.
- Updated live field-practice registers, LLM maps, semantic route indexes, source records, manifest inventory, `TREE.txt`, and docs navigation for the new candidate route.
- Preserved historical Final Release 1 package metadata by treating the Chunk 45 review artifact as the live source tree and the Final Release 1 zip as historical reference only.
- Preserved non-scope boundaries: no field-practice promotion, reproduction claim, new tool cards, shortcut cards, pricing snapshots, broad workflow expansion, broad security/secrets expansion, broad tool-catalog expansion, source-map migration, or narrative chapter rewrite beyond the narrow Chapter 36 candidate-inventory row required for route consistency.

## Chunk 44 — Final Release 1 Packaging

- Packaged Final Release 1 as a packaging-only artifact from approved Release Candidate 1 revision 2.
- Updated README, manifest, LLM maps, changelog, final report, package references, package-integrity references, and validator coverage for final-release identity/status.
- Added `CHUNK_44_REPORT.md` and `FINAL_RELEASE_1_INTEGRITY.md` for final-release packaging verification and source-tree integrity reporting.
- Preserved documented limitations: exact non-OpenAI pricing remains deferred; tool catalog is curated rather than exhaustive; all nine field-practice cards remain candidate-only; changelog ordering follows the documented convention.
- Preserved non-scope boundaries: no new tool cards, field-practice cards, shortcut cards, pricing snapshots, broad workflow expansion, broad security/secrets expansion, broad tool-catalog expansion, source-map migration, or narrative chapters.

## Chunk 43 — Release Candidate 1 Packaging

- Produced Release Candidate 1 as a packaging-only artifact.
- Updated README, manifest, LLM maps, changelog, package references, validator coverage, and this report for release-candidate identity/status.
- Verified package inventory, manifest aliases, root governance metadata, register counts, `TREE.txt`, validator output, zip hygiene, source-tree integrity reporting, and checksum sidecar convention.
- Preserved documented limitations: exact non-OpenAI pricing remains deferred; tool catalog is curated rather than exhaustive; all nine field-practice cards remain candidate-only; changelog ordering follows the documented convention.
- Preserved non-scope boundaries: no new tool cards, field-practice cards, shortcut cards, pricing snapshots, broad workflow expansion, broad security/secrets expansion, broad tool-catalog expansion, source-map migration, or narrative chapters.
- Revision 1: repaired stale non-RC wording in `TOOL_REGISTER.md`, added auditable `RELEASE_CANDIDATE_1_INTEGRITY.md` source-tree integrity reporting, documented the `.sha256` sidecar convention, updated package aliases to the revised RC1 package, and tightened validator coverage for RC status and integrity-reporting defects.
- Revision 2: removed false submitted-sidecar wording, distinguished source-tree integrity from final zip checksum and external sidecar convention, aligned deterministic source-content hash prose with the validator's path-ordered algorithm, and updated package aliases to the revised RC1 package.

## Chunk 42 — Release-Candidate Scope Disposition Cleanup

- Converted the Chunk 41 finalization gap list into an explicit release-candidate disposition matrix: future editor-scoped packaging, documented pricing limitation, documented curated-tool limitation, documented candidate field-practice limitation, and changelog-order convention.
- Stated that the Chunk 42 author package was not a release-candidate package and that release-candidate packaging was allowed next only after editor approval as a packaging-only chunk.
- Synchronized release-candidate status and active/deferred/planned/candidate/pricing count state across README, manifest, registers, and LLM maps without adding new cards or pricing snapshots.
- Documented the changelog ordering convention instead of reorganizing historical entries.
- Tightened `scripts/validate_repository.py` for release-candidate disposition, no-premature-RC claims, changelog convention, register-count agreement, package-reference aliases, and no-new-card/no-pricing scope guardrails.
- Revision: repaired root-level `manifest.actual_package_inventory_count` to match the 329-file package inventory and tightened validator coverage for root-level manifest count alias drift.
- Revision 2: repaired stale Chunk 41 review-state wording in `manifest.finalization_readiness_audit.release_candidate_gaps` and tightened validator coverage for stale prior-review-state text in manifest governance metadata.

## Changelog Ordering Convention

Current and recent governance/chunk entries appear near the top for active review. older historical entries may preserve their original authoring/revision order instead of strict newest-first chronological order. Treat this changelog as a review trail, not a release-note feed, unless a future editor-scoped packaging or release-maintenance chunk normalizes it further.

## Chunk 41 — Finalization Readiness Audit

- Audited root governance, registers, indexes, LLM maps, schemas, reports, manifest inventories, and package metadata for release-candidate readiness.
- Added finalization-readiness state to README, manifest, LLM maps, and core registers without adding new cards or pricing snapshots.
- Confirmed explicit catalog states: 52 active tool cards, 23 deferred/planned concrete ecosystem IDs, 50 active shortcut cards, 48 planned shortcuts, 9 candidate field-practice cards, 1 active pricing snapshot, and 4 deferred pricing snapshot categories.
- Identified release-candidate gaps: no RC package yet, non-OpenAI pricing snapshots deferred, tool catalog curated rather than exhaustive, field-practice cards candidate-only, and changelog chronological ordering not normalized.
- Tightened `scripts/validate_repository.py` for finalization-critical register counts, README/manifest/LLM finalization routes, package-reference aliases, no-new-card scope guardrails, and finalization gap-list presence.

## Chunk 40 — Tool Catalog Coverage-Gap Audit and Ecosystem Expansion

- Added six active ecosystem tool cards: `tool.cloudflare`, `tool.netlify`, `tool.neon`, `tool.resend`, `tool.vitest`, and `tool.storybook`.
- Added deferred/planned ecosystem tool IDs and alias/companion coverage decisions to `TOOL_REGISTER.md` so the active catalog no longer implies exhaustive ecosystem coverage.
- Added official vendor/project source rows for the six active Chunk 40 cards.
- Updated README, LLM maps, and semantic indexes so new active tools and deferred coverage routes surface before broad chapter/tool-stack fallbacks.
- Tightened validator coverage for active Chunk 40 card/schema/source routing, deferred ecosystem register coverage, LLM/source-map routing, report inventory, package-count aliases, and scope guardrails.
- Revision: repaired stale production-quality budget, task-index tool-stack/serious-app/platform-selection, AI-coach platform/serious-app, prompt-library production-platform, and generic LLM platform routes so active Chunk 40 platform/email/database/testing/UI-documentation cards surface before older fallbacks; tightened validator coverage for those exact paths.

## 2026-06-11 — Chunk 39 field-practice evidence and LLM source-map cleanup

- Normalized remaining field-practice evidence shorthand in `FIELD_PRACTICES.md` status-label and promotion-policy prose to canonical labels such as `E4_COMMUNITY_FIELD_REPORT`, `E2_REPRODUCED_LOCALLY`, and `E3_EXPERT_REPORT`.
- Canonicalized Chapter 36 field-practice `evidence_scope` and coaching evidence-label language so official docs support product mechanics/principles without promoting candidate rituals.
- Consolidated `llms.txt` and `llms-full.txt` by removing generation-specific active tool-card list sections while preserving fast semantic tool-routing paths.
- Clarified LLM routing for field-practice adoption, tool choice, prototype/app-builder choice, and production-readiness evidence.
- Tightened `scripts/validate_repository.py` for canonical field-practice evidence labels, Chapter 36 evidence-scope hygiene, generation-specific LLM tool-list clutter, LLM route freshness, report inventory, package counts, and scope guardrails.
- Preserved non-scope boundaries: no new field-practice cards, tool cards, category placeholder cards, pricing snapshots, shortcut cards, broad workflow expansion, broad security/secrets expansion, or narrative chapters.
- Revision: repaired stale `manifest.source_artifacts.package_file` / `review_package` aliases, updated Chunk 39 scope-boundary metadata, and tightened validator coverage for package-reference aliases and current-chunk scope-boundary metadata.

## 2026-06-11 — Chunk 36 local dev, design, and project-management tool-card expansion

- Added three active third-party infrastructure/process tool cards for `tool.docker`, `tool.figma`, and `tool.linear`.
- Updated `TOOL_REGISTER.md` so the existing Docker/container, Figma/design, and Linear/project-management anchors are active and routable.
- Added official vendor/project source rows for Docker, Figma, and Linear while keeping exact pricing, plan limits, seat limits, quota limits, Docker Desktop licensing details, current UI labels, command flags, setup mechanics, defaults, and feature availability out of stable prose.
- Updated README, LLM maps, and semantic indexes so local reproducibility, Docker services, design handoff, Figma prototypes/specs/components, issue tracking, project planning, Linear workflows, and team execution hygiene route to active tool cards before older chapter/workflow/tool-stack fallbacks.
- Tightened `scripts/validate_repository.py` for Chunk 36 tool-card schema/status, official vendor source posture, semantic routing, manifest/package inventory, report inventory, and scope guardrails.
- Revision: repaired Chunk 36 semantic routes for Figma UI-state/design-code drift, Linear team-workflow ceremony and task promotion, Docker personal-local-tool project routing, and the Figma redirected shortcut-profile alias; tightened validator coverage for those exact defects.

## 2026-06-11 — Chunk 35 hosting, backend/auth, payment, observability, and product-analytics tool-card expansion

- Added seven active third-party platform tool cards for `tool.vercel`, `tool.supabase`, `tool.clerk`, `tool.auth0`, `tool.stripe`, `tool.sentry`, and `tool.posthog`.
- Updated `TOOL_REGISTER.md` so the existing hosting/backend/auth/payment/observability/product-analytics anchors are active and routable.
- Added official vendor source rows for Vercel, Supabase, Clerk, Auth0, Stripe, Sentry, and PostHog while keeping exact pricing, limits, quotas, UI labels, setup mechanics, defaults, and feature availability out of stable prose.
- Updated README, LLM maps, and primary semantic indexes so hosting, database/backend/auth, payments, production monitoring, product analytics, feature flags, serious-app, and production-readiness intents route to active tool cards before older chapter/workflow fallbacks.
- Tightened `scripts/validate_repository.py` for Chunk 35 tool-card schema/status, official vendor source posture, semantic routing, manifest/package inventory, and scope guardrails.
- Revision: repaired production-quality budget routing, senior-checklist task routing, production-error prompt routing, API-endpoint prompt routing, and senior-checklist prompt routing so active Chunk 35 platform/tool cards appear before older workflow/chapter/constraint fallbacks; tightened validator coverage for those exact paths.

## 2026-06-11 — Chunk 34 browser-dev, app-builder, and UI-generation tool-card expansion

- Added four active tool cards for `tool.replit`, `tool.lovable`, `tool.bolt`, and `tool.v0`.
- Updated `TOOL_REGISTER.md` so the existing browser-dev/app-builder/UI-generation anchors are active and routable while keeping non-scoped hosting/database/auth/payment/observability/design/project-management/Docker rows planned.
- Added official Replit, Lovable, Bolt, and v0/Vercel source anchors in `SOURCE_REGISTER.md` and kept exact pricing, plan limits, quota limits, hosting/runtime limits, app-generation mechanics, deployment mechanics, integration limits, export behavior, UI labels, model availability, and current capability claims out of stable prose.
- Routed the new active tool cards through README, manifest, LLM maps, tool-category/task/project/risk/recoverability/failure/prompt/AI-coach/concept/stability/glossary indexes, and validator coverage.
- Extended `scripts/validate_repository.py` with Chunk 34 tool-card schema/status/source posture, semantic routing, report inventory, package-count, and scope-boundary checks.
- Preserved non-scope boundaries: no hosting/database/auth/payment/observability cards, design/project-management cards, Docker/container cards, field-practice expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, broad security/secrets expansion, or narrative chapters.
- Revision: repaired disposable-prototype budget routing, throwaway-prototype project-type constraint routing, and low-risk/disposable-work risk routing so active Chunk 34 app-builder/browser-dev/UI-generation tool cards appear before chapter/planned-shortcut fallbacks; tightened validator coverage for those exact paths.


## 2026-06-11 — Chunk 31 Codex governance/maintenance tool-card expansion

- Added two active first-party OpenAI/Codex governance and maintenance tool cards for `tool.codex_feature_maturity` and `tool.codex_changelog_monitoring`.
- Updated `TOOL_REGISTER.md` so the existing governance anchors are active and routable while keeping non-scoped tool cards planned.
- Routed the new tool cards through README, manifest, LLM maps, tool-category and Codex-surface indexes, task routing, stability routing, prompt-library routes, AI-coach routes, glossary routes, source-register gate metadata, and validator coverage.
- Refreshed official OpenAI/Codex Feature Maturity and Codex Changelog source anchors.
- Reused existing Codex overview and documentation-update anchors without changing their older checked dates.
- Kept exact maturity labels, current feature statuses, release dates, UI labels, availability, model availability, pricing, plan limits, credit values, command/config details, and context-window values out of stable prose.
- Extended `scripts/validate_repository.py` with Chunk 31 tool-card coverage, register status, source-map routing, semantic routing before older `vcb.codex.*`, source-register, deprecation-register, or chapter fallbacks, report inventory, package-count, and scope-boundary checks.
- Preserved non-scope boundaries: no third-party tool cards, broad tool-card expansion, field-practice expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, broad security/secrets expansion, or narrative chapters.

- Revision: repaired nested manifest `source_artifacts` report/topic/tool-catalog inventories; added README active governance/maintenance tool-card routing; corrected source wording for reused overview/documentation-update anchors; repaired `INDEX_BY_CONCEPT.md` feature-maturity routing and `llms.txt` feature-card fast routing; tightened validator coverage for those exact defects.
- Second revision: repaired root-level manifest `source_file_count` / `source_files_count` aliases to match the 278-file package inventory and tightened validator coverage for root-level manifest count drift.

## 2026-06-11 — Chunk 30 first-party OpenAI/Codex Security tool-card expansion

- Added one active first-party OpenAI/Codex Security tool card for `tool.codex_security`.
- Updated `TOOL_REGISTER.md` so the existing Codex Security anchor is active and routable while keeping non-scoped tool cards planned.
- Routed the new tool card through README, manifest, LLM maps, tool/category and Codex-surface indexes, task routing, risk/failure routing, prompt-library routes, AI-coach routes, glossary/concept/budget/recoverability/project/stability routes, source-register gate metadata, and validator coverage.
- Reused and refreshed official OpenAI/Codex Security source anchors for plugin workflows, cloud setup, threat-model tuning, validation/FAQ limits, and Codex approvals/security posture.
- Kept exact availability, feature maturity, UI labels, setup mechanics, scan behavior, pricing, plan limits, credit values, model availability, command/config details, and context-window values out of stable prose.
- Extended `scripts/validate_repository.py` with Chunk 30 tool-card coverage, register status, source-map routing, semantic routing before older safety/chapter fallbacks, report inventory, package-count, and scope-boundary checks.
- Revision: repaired stale generic first-party tool-card and feature-selection routes in `llms-full.txt`, `indexes/INDEX_BY_TASK.md`, `indexes/PROMPT_LIBRARY.md`, and `indexes/INDEX_FOR_AI_COACHES.md` so `tool.codex_security` appears before older `vcb.codex.*`, safety, workflow, or chapter fallbacks; tightened validator coverage for those exact paths.
- Preserved non-scope boundaries: no third-party tool cards, no feature-maturity/changelog-monitoring cards, no broad security/secrets topic expansion, no field-practice expansion, no pricing expansion, no broad workflow expansion, no broad shortcut expansion, no new shortcut-card expansion, and no narrative chapters.

## 2026-06-10 — Chunk 29 Codex customization/control tool-card expansion

- Added five active first-party OpenAI/Codex customization/control tool cards for `tool.codex_agents_md`, `tool.codex_config`, `tool.codex_skills`, `tool.codex_mcp`, and `tool.codex_hooks`.
- Updated `TOOL_REGISTER.md` so the authored customization/control Codex tool cards are active and routable while keeping non-scoped tool cards planned.
- Routed the new tool cards through README, manifest, LLM maps, tool/category and Codex-surface indexes, task routing, prompt-library routes, AI-coach routes, glossary routes, source-register gate metadata, and validator coverage.
- Reused official OpenAI/Codex AGENTS.md, config, skills, MCP, hooks, customization, plugins, approvals/security, and best-practices anchors.
- Kept exact config keys, hook event names, command flags, UI labels, setup mechanics, model availability, context-window numbers, pricing, plan limits, and credit values out of stable prose.
- Extended `scripts/validate_repository.py` with Chunk 29 tool-card coverage, register status, source-map routing, semantic routing before older `vcb.codex.*` feature fallbacks, report inventory, package-count, and scope-boundary checks.
- Revision: repaired stale semantic routes in `indexes/INDEX_BY_TASK.md` and `indexes/PROMPT_LIBRARY.md` so team-workflow promotion and tool/hook/plugin/MCP adoption intents route to active Chunk 29 tool cards before older chapter or shortcut fallbacks; tightened validator coverage for those exact paths.
- Preserved non-scope boundaries: no third-party tool cards, no Codex Security tool card, no feature-maturity/changelog-monitoring cards, no field-practice expansion, no pricing expansion, no broad workflow expansion, no broad shortcut expansion, no new shortcut-card expansion, and no narrative chapters.

## 2026-06-10 — Chunk 27 first-party OpenAI/Codex primary tool-card expansion

- Added seven active first-party OpenAI/Codex tool cards for `tool.codex`, `tool.codex_app`, `tool.codex_cli`, `tool.codex_ide_extension`, `tool.codex_cloud`, `tool.codex_github_review`, and `tool.codex_exec`.
- Updated `TOOL_REGISTER.md` so the authored primary Codex tool cards are active and routable while keeping non-primary and third-party tool cards planned.
- Routed the new tool cards through README, manifest, llms maps, tool-category and Codex-surface indexes, plus primary semantic routing indexes.
- Reused official OpenAI/Codex source anchors and kept exact pricing, plan limits, model availability, commands, flags, UI labels, and context-window values out of stable prose.
- Extended `scripts/validate_repository.py` with Chunk 27 tool-card coverage, register status, source-map, semantic routing, scope-boundary, and report-inventory checks.
- Revision: repaired stale semantic routes in `indexes/INDEX_BY_TASK.md`, `indexes/PROMPT_LIBRARY.md`, and `llms.txt` so Codex surface-selection, non-interactive, PR-review, and cloud/browser/GUI intents route to active `tool.codex*` cards before older fallbacks; tightened validator coverage for those exact lookup paths.

## 2026-06-09 — Chunk 20 shortcut harm-reduction topic-card expansion

- Added eight active shortcut harm-reduction cards for skipping tests, accepting “looks done,” broad agent permissions, unattended long runs, broad refactor, context dumping, adding dependencies fast, and reviewing cloud summaries only.
- Updated `SHORTCUT_REGISTER.md` so the authored shortcut cards are active and routable.
- Routed the new shortcut cards through README, manifest, llms maps, prompt library, AI-coach index, shortcut index, and primary risk/budget/stability/task indexes.
- Extended `scripts/validate_repository.py` with Chunk 20 shortcut-card coverage, active-register status, per-index routing, stale planned-route, scope-boundary, and report-claim checks.
- Revision: repaired dangling planned shortcut rows in `SHORTCUT_REGISTER.md` by placing them inside a declared shortcut-route table and added validator coverage for shortcut-register table placement.


## 2026-06-09 — Chunk 18 second revision: failure-mode index semantic routing

- Patched `indexes/INDEX_BY_FAILURE_MODE.md` so unsupported completion summaries, unreproduced bug-fix claims, and confident wrong summaries route to active `vcb.failure.done_claim_without_evidence`.
- Removed duplicate active `vcb.failure.ci_false_confidence`, `vcb.failure.hallucinated_apis`, and `vcb.failure.weakened_tests` rows from semantic failure-mode sections.
- Extended `scripts/validate_repository.py` with semantic-section checks for `INDEX_BY_FAILURE_MODE.md` and duplicate active failure-mode row detection inside single index sections.

## 2026-06-09 — Chunk 18 revision: failure-mode routing hygiene

- Added missing active `vcb.failure.*` routes to `indexes/PROMPT_LIBRARY.md`, `indexes/INDEX_FOR_AI_COACHES.md`, `indexes/INDEX_BY_STABILITY.md`, `indexes/INDEX_BY_CONCEPT.md`, and `indexes/INDEX_BY_SHORTCUT.md`.
- Completed full-list failure-mode sections in `indexes/GLOSSARY.md`, `indexes/INDEX_BY_BUDGET_PROFILE.md`, `indexes/INDEX_BY_RECOVERABILITY.md`, and `indexes/INDEX_BY_RISK_LEVEL.md` so `vcb.failure.done_claim_without_evidence` is routable.
- Cleaned `llms.txt` repeated Chunk 18 active-status text and normalized `topics/failure-modes/done-claim-without-evidence.md` Quick Navigation heading.
- Reverted unintended `CHUNK_2_REPORT.md` historical drift while preserving the intentional `topics/concepts/diff.md` related-topic migration to `vcb.failure.done_claim_without_evidence`.
- Extended `scripts/validate_repository.py` with per-index Chunk 18 routing checks, full-list completeness checks, report/changelog route-claim checks, and repeated source-map phrase checks.

## 2026-06-09 — Chunk 18 failure-mode topic-card expansion

- Added eight bounded failure-mode topic cards for hallucinated APIs, context pollution, weakened tests, broad-refactor drift, dependency bloat, UI taste gaps, CI false-confidence loops, and done claims without evidence.
- Routed new failure-mode cards through README, llms maps, task/failure/risk/recoverability/budget/project/shortcut/stability/AI-coach indexes, glossary, and prompt library.
- Extended `scripts/validate_repository.py` with Chunk 18 failure-mode slice, task-route, stale planned-route, duplicate full-list, and per-routing-surface checks.
- Preserved scope: no tool-card expansion, shortcut-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.

## 2026-06-09 — Chunk 17 revision: redirect-map and task-index routing hygiene

- Normalized manifest topic-namespace and namespace-policy redirect maps so Chunk 17 aliases resolve to the same active cards.
- Updated `indexes/INDEX_BY_TASK.md` task sections to route release notes, dependency migration, dead-code removal, documentation, visual QA, and accessibility work to active atomic Chunk 17 cards.
- Removed the stale planned `vcb.workflow.documentation_update` route now that `vcb.workflow.documentation_updates` is active.
- Extended `scripts/validate_repository.py` to catch redirect-map conflicts, stale planned-route replacements, and aggregate-only Chunk 17 task-index routing.

## 2026-06-09 — Chunk 17 frontend/refactor/dependency workflow topic-card expansion

- Added 8 active workflow topic cards under `topics/workflows/` for frontend verification, visual QA, accessibility review, safe refactoring, dependency decisions, dependency update review, release notes, and documentation updates.
- Updated LLM source maps, primary indexes, README, source register, manifest, and validator expectations for active Chunk 17 workflow routing.
- Anchored frontend, refactor, dependency, release-note, and documentation workflows to official OpenAI/Codex, GitHub, npm, MDN, W3C/WAI, Playwright, and named practitioner sources.
- Preserved non-scope: no full tool-card expansion, shortcut-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion beyond the approved slice, or new narrative chapters.

## 2026-06-09 — Chunk 16 revision: index/source-register signpost hygiene

- Added missing retrieval stop and `END_INDEX` markers to updated routing indexes.
- Moved Chunk 16 source records into a declared source-register table section.
- Extended repository validation for index terminal markers, VCB begin/end marker pairing, and source-register table placement.
- Added explicit maintenance-phase budget notes to the eight Chunk 16 review/safety workflow cards.

## 2026-06-09 — Chunk 16 revision: marker and source-register hygiene

- Added missing `VCB:STOP_RETRIEVAL` and `VCB:END_INDEX` signposts to updated routing indexes.
- Moved Chunk 16 source records into a declared `SOURCE_REGISTER.md` table section and removed source-table blank-line breaks that produced dangling rows.
- Extended `scripts/validate_repository.py` to enforce index terminal markers, cross-artifact VCB begin/end pairing, and source-register table placement.
- Added explicit maintenance-phase notes to the eight Chunk 16 review/safety workflow cards without expanding Chunk 16 scope.

## 2026-06-09 — Chunk 16 review/safety workflow topic-card expansion

- Added 8 active review, safety, and verification workflow topic cards under `topics/workflows/` and `topics/safety/`.
- Updated LLM source maps, primary indexes, README, source register, manifest, and validator expectations for active review/safety workflow routing.
- Anchored Codex output review, PR review, security review, secrets, CI triage, non-interactive CI, and production red-line guidance to official OpenAI/Codex, Git/GitHub, and OWASP sources.
- Preserved non-scope: no full tool-card expansion, shortcut-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion beyond the approved slice, or new narrative chapters.

## 2026-06-09 — Chunk 15 workflow/prompting topic-card expansion

- Added 8 active workflow/prompting topic cards under `topics/prompting/` and `topics/workflows/`.
- Updated LLM source maps, primary indexes, README, source register, manifest, and validator expectations for active `vcb.prompting.*` and `vcb.workflow.*` card routing.
- Anchored prompt/workflow guidance to official OpenAI Codex prompt, best-practice, workflow, onboarding, bug-triage, QA, goal-following, difficult-problem iteration, and AI-native engineering sources.
- Preserved non-scope: no full tool-card expansion, shortcut-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion beyond the approved slice, or new narrative chapters.

## 2026-06-09 — Chunk 14 revision: validator parser and report-claim hygiene

- Hardened `scripts/validate_repository.py` frontmatter parsing so marker-prefixed topic/report files validate while body horizontal-rule lines are ignored.
- Reworked `CHUNK_14_REPORT.md` validation wording into machine-enforced and manual/editorial checks.
- Added validator enforcement for the Chunk 14 machine-claim catalog so report claims cannot drift beyond implemented checks.
- Updated canonical review package references for the Chunk 14-only governance revision.

## 2026-06-09 — Chunk 13 Revision: LLM source-map and source-metadata hygiene

- Fixed `llms.txt` / `llms-full.txt` begin-marker versions and stale visible chunk headings.
- Moved Chunk 13 source rows into a valid `SOURCE_REGISTER.md` table section and added missing Jest, Node.js, and OpenFeature source records.
- Updated feature-flag evidence metadata to use OpenFeature as the E0 definition anchor and Martin Fowler as E3 support.
- Corrected `source_status.official_openai` metadata for concept cards citing OpenAI sources.
- Extended repository validation for LLM source maps, active-report source resolution across new prefixes, OpenAI source-status drift, source-register table placement, and feature-flag metadata.


## 2026-06-09 — Chunk 14 revision: governance/signpost hygiene

- Normalized root next-chunk routing to `chunk_15_workflow_prompting_topic_cards` across `README.md` and `manifest.json`.
- Updated routing/register VCB begin-marker versions to match frontmatter versions.
- Removed duplicate Codex feature full-list routing sections from primary indexes.
- Expanded `scripts/validate_repository.py` to enforce next-chunk route agreement, begin-marker/frontmatter agreement, duplicate Codex feature full-list detection, and active Chunk 14 report validation-claim coverage.

## 2026-06-09 — Chunk 12 revision: pricing-snapshot routing and source-status hygiene

- Fixed `vcb.pricing_snapshot.openai_codex` manifest routing to `pricing-snapshots/2026-06-09-openai-codex.md`.
- Split pricing snapshots into active and planned/deferred status lists.
- Removed conflicting planned/snapshot stability-index route for the OpenAI/Codex pricing snapshot.
- Updated `openai.codex.pricing` source-register wording to point to the active dated snapshot.
- Normalized `source_status.official_vendor` metadata where evidence sections cite or do not cite non-OpenAI vendor/security sources.
- Expanded validation coverage for pricing-snapshot routing and source-status consistency.

## 2026-06-09 — Chunk 12 pricing/source-status routing revision

- Corrected `vcb.pricing_snapshot.openai_codex` manifest routing to `pricing-snapshots/2026-06-09-openai-codex.md`.
- Moved the OpenAI/Codex pricing snapshot from planned to active snapshot status across manifest policy mirrors and stability index routing.
- Updated `openai.codex.pricing` source-register language to point to the active snapshot instead of saying exact values are deferred.
- Fixed Chapter 43 and Chapter 44 `source_status.official_vendor` metadata to match their Evidence and Sources sections.
- Extended repository validation for pricing-snapshot routing, pricing status drift, source-register pricing rows, and official-vendor source-status consistency.


## 2026-06-09 — Chunk 11 revision: manifest and field-practice register hygiene

- Rebuilt nested `manifest.source_artifacts` inventory for Chunk 11.
- Updated all manifest canonical-review-package references to the Chunk 11 revision package.
- Normalized `FIELD_PRACTICES.md` status values and separated promotion path from current status.
- Added validator checks for nested manifest inventory, canonical package consistency, and field-practice status/table validation.



## 2026-06-09 — Chunk 11 field practices, updating, and shortcut expansion

- Added Chapter 36 — Field Notes: Unofficial and User-Discovered Codex Practices.
- Added Chapter 37 — Maintaining and Updating the Bible.
- Added Chapter 38 — Risk-Managed Shortcuts: When Users Ignore Best Practices.
- Expanded FIELD_PRACTICES.md with field-practice status labels, promotion rules, and candidate routing table.
- Expanded SHORTCUT_REGISTER.md with shortcut expansion policy, production red-line shortcut families, and guardrail escalation rule.
- Updated UPDATE_PROTOCOL.md with field-practice promotion and shortcut-update rules.
- Updated indexes, llms.txt, manifest, and report for Chunk 11.


## 2026-06-09 — Chunk 10 new-project-bootstrap playbook revision

- Added the missing Chapter 33 `new project bootstrap` playbook.
- Added matching routes in `indexes/INDEX_BY_TASK.md` and `indexes/PROMPT_LIBRARY.md`.
- Updated `scripts/validate_repository.py` so Chapter 33 coverage includes the full blueprint playbook list and the bootstrap routes.
- Updated `CHUNK_10_REPORT.md` validation language.



## 2026-06-09 — Chunk 10 revision: index hygiene and playbook coverage

- Replaced visible index status lines with chunk-neutral routing text.
- Rebuilt primary indexes to remove append-only historical chunk sections and duplicate Chunk 9 routing blocks.
- Expanded Chapter 33 with compact blueprint playbooks for release notes, production-error investigation, API endpoints, dependency migration, dead-code removal, documentation improvement, MVP prototype build, and auth-sensitive hardening.
- Updated `INDEX_BY_TASK.md` and `PROMPT_LIBRARY.md` to route the expanded playbook set.
- Extended `scripts/validate_repository.py` to check visible index status, historical chunk headings, and Chapter 33 playbook coverage.

## 2026-06-09 — Chunk 10: Project operating system and playbooks

- Added Chapter 31 — From Prompt Library to Team Workflow (`vcb.chapter.prompt_library_to_team_workflow`).
- Added Chapter 32 — Failure Modes: How Codex Work Goes Wrong (`vcb.chapter.failure_modes_codex_work`).
- Added Chapter 33 — The Codex Playbooks (`vcb.chapter.codex_playbooks`).
- Added Chapter 34 — Building Your First Serious App with Codex (`vcb.chapter.first_serious_app`).
- Added Chapter 35 — The Senior Engineer Checklist for Vibe Coders (`vcb.chapter.senior_engineer_checklist`).
- Updated routing indexes for workflow compounding, failure modes, playbook selection, first serious app sequencing, and senior-engineer review gates.
- Registered planned shortcut IDs for process overhead, stale durable guidance, failure-mode avoidance, blind playbook use, prototype-as-production, first-app overbuilding, checklist skipping, and checklist theater.
- Added official OpenAI/Codex source anchors for AI-native engineering, goal-following, proof-of-concept, internal apps, documentation updates, and hallucination/truthfulness framing.
- Kept field-practice expansion, update protocols, full shortcut cards, constraints/pricing/tool-stack chapters, other-AI material, and limitations/biases chapters out of Chunk 10 scope.


## 2026-06-08 — Chunk 8: Review, security, and CI/non-interactive automation

- Added Chapter 23 — Reviewing Codex Output Like a Senior Engineer (`vcb.chapter.reviewing_codex_output`).
- Added Chapter 24 — GitHub PR Review with Codex (`vcb.chapter.github_pr_review_with_codex`).
- Added Chapter 25 — Security for Vibe Coders (`vcb.chapter.security_for_vibe_coders`).
- Added Chapter 26 — CI, Non-Interactive Codex, and GitHub Actions (`vcb.chapter.ci_noninteractive_github_actions`).
- Updated routing indexes for diff review, GitHub PR review, security review, secrets, prompt injection, non-interactive Codex, CI automation, and GitHub Actions.
- Registered planned shortcut IDs for skipping PR review, treating Codex review as approval, skipping security review, using real secrets in prototypes, unattended mutation, overbroad CI permissions, and long-lived CI secrets.
- Added official OpenAI/Codex, GitHub Actions, and OWASP source anchors for Chunk 8 claims.
- Kept cloud delegation, subagents, automations, computer use deep dive, operating-system/playbook chapters, pricing snapshots, tool catalog expansion, and full shortcut cards out of Chunk 8 scope.



## 2026-06-08 — Chunk 7 revision: root governance metadata hygiene

- Fixed `README.md` root frontmatter status for Chunk 7.
- Fixed `manifest.json` editor-gate approval transition text.
- Added validator checks for README/manifest/report chunk-governance drift.
- Updated `CHUNK_7_REPORT.md` validation lines for root-governance metadata.


## 2026-06-08 — Chunk 6: Frontend, refactoring, dependencies

- Added Chapter 15 — Frontend Work: Screenshots, Browser Checks, and Taste (`vcb.chapter.frontend_work`).
- Added Chapter 16 — Refactoring Without Breaking Everything (`vcb.chapter.refactoring_without_breaking_everything`).
- Added Chapter 17 — Dependency, Package, and Framework Decisions (`vcb.chapter.dependency_package_framework_decisions`).
- Updated routing indexes for frontend UI work, behavior-preserving refactoring, package/dependency decisions, dependency bloat, UI taste gaps, and broad-refactor shortcuts.
- Registered planned shortcut IDs for `vcb.shortcut.eyeballing_ui` and `vcb.shortcut.broad_refactor`.
- Added official OpenAI source anchors for frontend design, in-app browser, refactoring, and dependency incident audits.
- Added official GitHub/W3C/npm/OpenSSF source anchors for dependency review, accessibility, package scripts, and open-source security posture.
- Extended `scripts/validate_repository.py` with required-heading and VCB section-pair validation.
- Kept AGENTS.md/config/skills/MCP/hooks, security/CI review chapters, cloud delegation, automations, computer use deep dive, pricing snapshots, tool catalog expansion, and full shortcut cards out of Chunk 6 scope.

## 2026-06-08 — Chunk 6 submitted

- Added Chapter 15 — Frontend Work: Screenshots, Browser Checks, and Taste.
- Added Chapter 16 — Refactoring Without Breaking Everything.
- Added Chapter 17 — Dependency, Package, and Framework Decisions.
- Updated indexes, source register, shortcut register, tool register, manifest, `llms.txt`, and compact `llms-full.txt` routing.
- Extended repository validator to include current source prefixes and required Markdown heading/section checks.


## 2026-06-08 — Chunk 5: Core workflows

- Added Chapter 11 — Understanding an Unknown Codebase (`vcb.chapter.understanding_unknown_codebase`).
- Added Chapter 12 — Building a Feature in Small Slices (`vcb.chapter.feature_slicing`).
- Added Chapter 13 — Debugging with Reproduction, Not Guessing (`vcb.chapter.debugging_with_reproduction`).
- Added Chapter 14 — Writing and Updating Tests with Codex (`vcb.chapter.writing_updating_tests`).
- Updated routing indexes for unknown-repo work, feature slicing, repro-first debugging, and testing workflows.
- Registered planned shortcut IDs for `vcb.shortcut.editing_before_understanding` and `vcb.shortcut.debugging_without_repro`.
- Added official OpenAI source anchors for codebase onboarding, bug triage, QA with Computer Use, and AI-native engineering/testing guidance.
- Updated `scripts/validate_repository.py` to resolve the current chunk report dynamically from the manifest.
- Kept frontend, refactoring, dependency decisions, CI automation, pricing snapshots, and full shortcut cards out of Chunk 5 scope.


## 2026-06-08 — Chunk 4 routing/source hygiene revision

- Canonical review package: `vibe-coding-bible-chunk-4-revision-20260608T165625Z-authoritative.zip`.
- Normalized plan-skipping shortcut routes to `vcb.shortcut.skipping_plan`.
- Reconciled Chapter 4 setup shortcut profiles with `SHORTCUT_REGISTER.md`.
- Registered `vcb.shortcut.using_existing_local_setup` as a planned shortcut profile.
- Repaired malformed shortcut-register rows for `vcb.shortcut.vague_prompt` and `vcb.shortcut.accepting_looks_done`.
- Resolved Git evidence source IDs with registered official Git source IDs.
- Added Chunk 4 validation coverage for shortcut-profile resolution, shortcut index routes, evidence source IDs, and shortcut-register table shape.

## 2026-06-08 — Chunk 3 schema/frontmatter consistency revision

- Normalized `source_kind` in `chapters/06-git-discipline.md` and `topics/concepts/blast-radius.md` to the schema-supported `official_docs_plus_maintainer_synthesis` value.
- Preserved vendor distinction through `source_status.official_vendor: true` instead of creating an unsupported `source_kind` enum value.
- Updated `CHUNK_3_REPORT.md` validation wording to include active chapter/topic frontmatter instance validation.
- Repackaged Chunk 3 as `vibe-coding-bible-chunk-3-revision-20260608T154703Z-authoritative.zip`.


## 2026-06-08 — Chunk 3: Setup, sandbox/approvals, and Git discipline

### Added

- Added `chapters/04-installing-and-configuring-codex.md` — `vcb.chapter.installing_and_configuring_codex`.
- Added `chapters/05-sandboxing-and-approvals.md` — `vcb.chapter.sandboxing_and_approvals`.
- Added `chapters/06-git-discipline.md` — `vcb.chapter.git_discipline`.
- Added official OpenAI source anchors for Codex config basics/reference/advanced, sandboxing, approvals/security, and CLI reference.
- Added official Git source anchors for status, worktree, restore, reset, and reflog.
- Added prompt-library seeds for setup inspection, permission-mode selection, Git preflight, small reviewable diffs, and low-attention guardrails.

### Changed

- Updated README, manifest, `llms.txt`, and `llms-full.txt` to route to Chunk 3 active content and Chunk 4 next scope.
- Updated task, concept, Codex surface, failure mode, stability, budget profile, project type, recoverability, risk, shortcut, tool category, AI-coach, glossary, and prompt-library indexes.
- Added a literal `### Useful metaphors` subsection to Chapter 3’s AI-coach section.
- Added optional `evidence_basis` and `source_kind` support to `topic.schema.json` and `chapter.schema.json`.

### Deferred

- Four-part prompting, plan-first, context management, and acceptance criteria remain Chunk 4 scope.
- Full `AGENTS.md`, config, skills, MCP, hooks, and automation chapters remain later scope.

## 2026-06-08 — Chunk 2 routing/source-hygiene revision

- Corrected `indexes/INDEX_BY_STABILITY.md` pricing snapshot route from the undeclared pricing namespace to canonical `vcb.pricing_snapshot.openai_codex`.
- Added planned pricing snapshot IDs to `PRICING_SNAPSHOT_REGISTER.md` and `manifest.json`.
- Restored `E3_EXPERT_REPORT` definition to named expert/blog/course/talk/public practitioner only.
- Separated maintainer synthesis from evidence levels using `evidence_basis` / `source_kind` language.
- Declared `vcb.synthesis.*` as a non-topic source namespace in `manifest.json`.
- Updated Chapter 2 metadata so maintainer synthesis is not presented as E3 expert evidence.
- Aligned `vcb.concepts.blast_radius` evidence metadata with the restored E3 definition by using official vendor/OpenAI anchors plus synthesis basis.

## 2026-06-08 — Chunk 2 draft

- Added `chapters/01-codex-mental-model.md` — `vcb.chapter.codex_mental_model`.
- Added `chapters/02-vibe-coder-advantage-and-risk.md` — `vcb.chapter.vibe_coder_advantage_and_risk`.
- Added `chapters/03-codex-surfaces.md` — `vcb.chapter.codex_surfaces`.
- Updated routing indexes for Codex mental model, vibe-coder risk, surface selection, AI-coach interventions, project types, budget profiles, stability, risk, and recoverability.
- Added official OpenAI/Codex source anchors for app, app features, IDE, CLI, cloud/web, GitHub review, SDK, GitHub Action, feature maturity, hallucination/truthfulness, and changelog monitoring.
- Added VCB synthesis convention for stable engineering-practice synthesis where no product-behavior claim is being made.
- Kept setup/config, sandbox/approvals, and Git discipline out of Chunk 2 scope.

## 2026-06-08 — Chunk 1 routing-hygiene revision

- Corrected `README.md` next-chunk route from Chunk 1 back-reference to `chunk_2_codex_mental_model_and_surfaces`.
- Updated `indexes/INDEX_BY_PROJECT_TYPE.md` to mark Chunk 1 concept cards active where relevant.
- Added Chunk 1 validation lines for project-type index status and README/manifest route agreement.

## 2026-06-08 — Chunk 1: Chapter 0 and Core Concept Cards

- Added `chapters/00-how-to-use-this-bible.md` as `vcb.chapter.how_to_use_this_bible`.
- Added concept cards: `vcb.concepts.diff`, `vcb.concepts.blast_radius`, `vcb.concepts.recoverability`, `vcb.concepts.rollback`, `vcb.concepts.git_branch`, and `vcb.concepts.pull_request`.
- Added official Git and GitHub source anchors to `SOURCE_REGISTER.md`.
- Updated indexes for active Chunk 1 routes.
- Updated artifact-hygiene wording to: canonical review package is one timestamped authoritative zip.

## 2026-06-08 — Chunk 0 revision after editor review

- Added mandatory terminal author gate marker to `CHUNK_0_REPORT.md`.
- Expanded `manifest.json` to register all created source artifacts.
- Added canonical topic namespace policy to `manifest.json` and `AUTHORING_PROTOCOL.md`.
- Normalized planned IDs in indexes to avoid undeclared topic domains.
- Added `attention_modes` taxonomy to manifest and schema expectations.
- Fixed `topic.schema.json` and `chapter.schema.json` to require both `human` and `ai_coach` audiences.
- Resolved shortcut typing: shortcut cards use `type: shortcut` plus `shortcut_type: risk_managed_shortcut`.
- Changed `openai.codex.pricing` source status to `anchor verified; exact pricing snapshot deferred`.
- Added Chunk 0 validation section.

## 2026-06-08 — Chunk 0 initial skeleton

- Created repository skeleton, registers, protocols, indexes, and schema drafts.
- No full chapters or topic cards authored.

## 2026-06-08 — Chunk 3 submitted

- Added Chapter 4: `vcb.chapter.installing_and_configuring_codex`.
- Added Chapter 5: `vcb.chapter.sandboxing_and_approvals`.
- Added Chapter 6: `vcb.chapter.git_discipline`.
- Updated routing indexes for setup/config, sandbox/approval, permissions, Git discipline, dirty-tree handling, and broad-access shortcuts.
- Added official OpenAI/Codex source anchors for config, sandboxing, approvals, permissions, rules, and CLI features.
- Added official Git source anchors for status, worktree, stash, reflog, restore, and reset.
- Added optional `evidence_basis` and `source_kind` support to topic/chapter schema drafts.
- Kept exact pricing, usage limits, UI-specific commands, and model-specific defaults out of stable prose.

## 2026-06-08 — Chunk 4

- Added Chapter 7 — The Four-Part Prompt: Goal, Context, Constraints, Done When.
- Added Chapter 8 — Plan First, Code Second.
- Added Chapter 9 — Context Management: Enough Context, Not Everything.
- Added Chapter 10 — Acceptance Criteria: The Difference Between “Looks Done” and Done.
- Updated routing indexes, prompt library, glossary, source register, shortcut register, manifest, and LLM source maps for Chunk 4.
- Checked official Codex best-practices, prompting, workflows, and execution-plan anchors.
- Kept exact pricing, model limits, context-window numbers, and unstable UI mechanics out of stable chapter prose.

## 2026-06-08 — Chunk 6 authored

- Added Chapter 15 frontend/browser/screenshot/taste guidance.
- Added Chapter 16 behavior-preserving refactoring guidance.
- Added Chapter 17 dependency/package/framework decision guidance.
- Updated indexes, source register, shortcut register, LLM routing files, manifest, and validator.

## 2026-06-08 — Chunk 6

- Added Chapter 15 — `vcb.chapter.frontend_work`.
- Added Chapter 16 — `vcb.chapter.refactoring_without_breaking_everything`.
- Added Chapter 17 — `vcb.chapter.dependency_package_framework_decisions`.
- Updated routing indexes for frontend work, visual acceptance, browser checks, safe refactoring, dependency review, package decisions, framework churn, and supply-chain risk.
- Added shortcut-register routes for `vcb.shortcut.eyeballing_ui`, `vcb.shortcut.broad_refactor`, and `vcb.shortcut.framework_churn`.
- Added official OpenAI/Codex source anchors for frontend workflows, granular UI changes, refactoring, and intentional non-change lists.
- Added official npm and GitHub source anchors for dependency manifests, lockfiles, audits, Dependabot alerts, dependency graph, and dependency review.
- Extended `scripts/validate_repository.py` with required-heading and section-marker checks for active topic/chapter files.
- Kept AGENTS.md/config/skills/MCP/hooks, review/security/shipping, CI/non-interactive automation, cloud delegation, subagents, automations, computer-use deep dive, exact pricing/limits, and full shortcut cards out of scope.


## 2026-06-08 — Chunk 7

- Added Chapter 18 — `vcb.chapter.agents_md_operating_manual`.
- Added Chapter 19 — `vcb.chapter.codex_config_defaults`.
- Added Chapter 20 — `vcb.chapter.skills_reusable_workflows`.
- Added Chapter 21 — `vcb.chapter.mcp_external_tools`.
- Added Chapter 22 — `vcb.chapter.hooks_deterministic_guardrails`.
- Updated routing indexes for persistent guidance, config defaults, skills, MCP, hooks, deterministic guardrails, and customization shortcuts.
- Added official OpenAI/Codex source anchors for skills, reusable skills, MCP, hooks, and customization.
- Added shortcut-register routes for AGENTS.md, config, skill, MCP/tool, and hook shortcuts.
- Kept review/security/shipping, CI/non-interactive automation, cloud delegation, subagents, automations, computer-use deep dive, exact pricing/limits, and full shortcut cards out of scope.

## 2026-06-08 — Chunk 9: Advanced agentic workflows

- Added Chapters 27–30 for cloud delegation, subagents, automations, and computer/browser/GUI tasks.
- Updated source, shortcut, and tool registers for Chunk 9 official anchors and planned shortcut/tool routes.
- Updated indexes, `llms.txt`, `llms-full.txt`, README, manifest, and TREE inventory.
- Kept Chunk 10 operating-system/playbook material out of scope.


## 2026-06-08 — Chunk 9 authored

- Added Chapters 27–30 on cloud delegation, subagents, automations, and computer/browser/GUI work.
- Updated indexes, source register, shortcut register, tool register, llms maps, manifest, and validation report.
- Preserved exact pricing/limits/model routing outside stable prose.


## 2026-06-09 — Chunk 12: Constraints, Costs, Tool Stacks, Limitations, Biases

- Added Chapters 39–46.
- Added first dated OpenAI/Codex pricing snapshot.
- Expanded tool, shortcut, source, task, budget, failure-mode, and AI-coach routing for constraints and cost-aware workflows.
- Added schema support for `evidence_scope` and validator duplicate-source-URL detection.
- Kept exact current pricing and limits out of stable chapter prose.


## 2026-06-09 — Chunk 12 pricing/source-status revision

- Fixed active OpenAI/Codex pricing snapshot routing and active/deferred manifest metadata.
- Removed conflicting planned/snapshot status for `vcb.pricing_snapshot.openai_codex` in `INDEX_BY_STABILITY.md`.
- Updated `openai.codex.pricing` source-register wording to point to the dated snapshot.
- Fixed Chapter 43/44 `source_status.official_vendor` metadata.
- Extended repository validation for pricing snapshot and source-status consistency.


## 2026-06-09 — Chunk 12 pricing-snapshot routing revision

- Fixed active OpenAI/Codex pricing snapshot routing from stale planned/path metadata to `pricing-snapshots/2026-06-09-openai-codex.md`.
- Removed conflicting stability-index pricing snapshot statuses.
- Updated `SOURCE_REGISTER.md` pricing language to point to the active snapshot.
- Aligned `source_status.official_vendor` metadata with Evidence and Sources sections.
- Expanded repository validation for pricing snapshot routes and source-status consistency.

## 2026-06-09 — Chunk 13 foundational concept-card expansion

- Added 17 foundational concept cards for API basics, frontend/backend, database schema, authentication, authorization, state, async, dependency, test, typecheck, lint, migration, environment variables, build steps, CI, feature flags, and observability.
- Updated source register with official/vendor/expert anchors for the new concept cards.
- Updated routing indexes and prompt library for concept-card retrieval.
- Added validator coverage for the bounded Chunk 13 concept-card slice.

## 2026-06-09 — Chunk 14 Codex feature-card expansion

- Added 15 active Codex feature cards under `topics/codex/`.
- Updated LLM source maps, indexes, manifest, source register, and validation expectations for active `vcb.codex.*` topic-card routing.
- Kept tool-card, shortcut-card, field-practice-card, and broad workflow-card expansion out of scope.

## 2026-06-09 — Chunk 14 submitted

- Added 15 Codex feature/topic cards under `topics/codex/`.
- Updated LLM source maps and indexes for Codex surface/feature routing.
- Rechecked official OpenAI anchors for app, CLI, IDE extension, cloud, GitHub review, config, AGENTS.md, skills, MCP, hooks, automations, subagents, computer use, feature maturity, and changelog monitoring.
- Preserved non-scope: no tool-card expansion, shortcut-card expansion, field-practice cards, or broad workflow-card expansion.

## 2026-06-09 — Chunk 19 constraint/budget topic-card expansion

- Added 8 active constraint/budget cards under `topics/constraints/` for operating mode, attention budget, usage burn/API budgeting, recovery budget, build-versus-maintenance phase, production-quality constraints, cheapest reliable workflows, and high-throughput workflows.
- Routed Chunk 19 cards through README, manifest, LLM maps, prompt library, glossary, budget, task, concept, stability, AI coach, shortcut, recoverability, risk, project-type, Codex-surface, tool-category, and failure-mode indexes.
- Updated validator checks for Chunk 19 required topic IDs, per-index routing coverage, planned-route replacement, report claim coverage, pricing-snapshot discipline, and source-map clutter.
- Revision: moved the Chunk 19 changelog entry inside the VCB changelog boundary, repaired nested manifest source-file inventory, listed the Chapter 26 route correction, and extended validator governance checks.
- Preserved scope boundary: no full tool-card expansion, no full shortcut-card expansion, no field-practice cards, no pricing expansion beyond source/snapshot routing, no broad workflow expansion, and no new narrative chapters.
- Revision: moved this live changelog entry inside the VCB changelog boundary.
- Revision: repaired nested manifest inventory and Chunk 19 report inventory governance.
- Revision: tightened validator coverage for changelog terminal content, nested manifest inventory, and active report file inventories.

## 2026-06-10 — Chunk 21 security/permission shortcut topic-card expansion

- Added eight active security and permission shortcut harm-reduction cards for production GUI actions, overbroad CI permissions, long-lived CI secrets, real secrets in prototypes, real secrets in cloud work, full-access automation, unattended mutation, and Always Allow sensitive apps.
- Updated `SHORTCUT_REGISTER.md` to mark the authored Chunk 21 shortcut rows active and add an active Chunk 21 shortcut-card route section.
- Updated root/LLM maps, primary indexes, source register, manifest, and validator coverage for the bounded Chunk 21 slice.
- Preserved scope boundaries: no full shortcut-card expansion, tool-card expansion, field-practice expansion, pricing expansion, broad workflow expansion, or new narrative chapters.
- Revision: fixed stale Chunk 20 validation expectation metadata in `manifest.json`, expanded generic LLM shortcut routing to active Chunk 20 and Chunk 21 slices, routed semantic risk/shortcut sections to active Chunk 21 cards before planned near-duplicates, and tightened validator coverage.

## 2026-06-10 — Chunk 22 setup/config/process shortcut-card expansion

- Added eight bounded setup/config/process shortcut harm-reduction topic cards: `vcb.shortcut.skipping_setup`, `vcb.shortcut.default_config_forever`, `vcb.shortcut.skipping_agents_md`, `vcb.shortcut.overstuffing_agents_md`, `vcb.shortcut.stale_agents_md`, `vcb.shortcut.unofficial_tools`, `vcb.shortcut.hook_overreach`, and `vcb.shortcut.trusting_external_tool_output`.
- Updated shortcut register statuses, README, manifest, LLM maps, prompt library, AI-coach index, and primary routing indexes for the new active shortcut-card slice.
- Added validator coverage for Chunk 22 card coverage, register status, LLM generic shortcut routing, semantic setup/config/process routes, stale planned shadow routes, and report inventory.
- Revision: consolidated duplicate Chunk 22 full-list index sections, fixed repeated LLM source-map status text, resolved undeclared plugin related-topic drift, collapsed duplicate Chunk 22 changelog entries, and tightened validator coverage for these defects.
- Preserved scope boundary: no full shortcut expansion, tool-card expansion, field-practice expansion, pricing expansion, broad workflow expansion, or narrative chapter work.

## 2026-06-10 — Chunk 23 tool-sprawl/skill/reusable-process shortcut-card expansion

- Added eight bounded shortcut harm-reduction topic cards for skill overkill, skill sprawl, general tool sprawl, MCP tool sprawl, brittle hooks, tiny-project process overhead, team workflow without a team, and blind playbook reuse.
- Updated `SHORTCUT_REGISTER.md` to mark the authored Chunk 23 shortcut rows active and add active Chunk 23 shortcut-card routes.
- Updated README, manifest, LLM source maps, prompt library, AI-coach index, primary routing indexes, source register, and validator coverage for the bounded Chunk 23 slice.
- Revision: removed active Chunk 23 canonical IDs from manifest redirect maps, consolidated duplicate Chunk 23 LLM source-map full-list sections, added semantic Fast Routing for skill/tool/MCP/hook/process shortcut intents, and tightened validator coverage for active-ID redirect shadowing and source-map hygiene.
- Preserved scope boundary: no full shortcut expansion, tool-card expansion, field-practice expansion, pricing expansion, broad workflow expansion, or narrative chapter work.

## 2026-06-10 — Chunk 24 multi-AI/model-bias shortcut-card expansion

- Added bounded multi-AI/model-bias shortcut cards for many AIs on same files, parallel agents editing same files, best-of-N without review, cherry-picking AI answers, consensus as correctness, trusting estimates before inspection, ignoring model biases, model-routing guesswork, and subagent swarms.
- Updated README, manifest, LLM maps, shortcut register, source register, primary indexes, prompt library, AI-coach routing, and validator checks for active Chunk 24 routing.
- Revision: repaired README next-chunk scope, failure-mode bad-estimate/confident-output semantic routing, and validator checks for both defects.
- Preserved non-scope boundaries: no tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.

## 2026-06-10 — Chunk 25 parallel/cloud/automation shortcut-card expansion

- Added bounded parallel/cloud/automation shortcut cards for unattended cloud delegation, ambiguous cloud tasks, cloud tasks without context, parallel cloud sprawl, conflicting parallel agents, automation spam, automation mutation without review, browser clicking without repro, and logged-in browser secrets.
- Updated README, manifest, LLM maps, shortcut register, source register, primary indexes, prompt library, AI-coach routing, and validator checks for active Chunk 25 routing.
- Rechecked official OpenAI/Codex cloud, cloud-environment, automations, worktree, non-interactive, browser, Chrome extension, Computer Use, approvals/security, and best-practices source anchors.
- Revision: repaired `INDEX_BY_SHORTCUT.md` verification shortcut routing for `vcb.shortcut.screenshot_only_verification` by showing active `vcb.shortcut.browser_clicking_without_repro` first, and tightened validator coverage for that alias path.
- Preserved non-scope boundaries: no full shortcut expansion, tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.


## 2026-06-10 — Chunk 26 repository-contract cleanup

- Hardened glossary limitation/bias routes so optimism, completion, plausibility, consensus, and answer-shopping terms route to active atomic model-bias and estimate/answer-selection shortcut cards instead of chapter-only fallbacks.
- Added shortcut alias/deprecation routing policy to `SHORTCUT_REGISTER.md` and `DEPRECATION_REGISTER.md`, including active replacements for planned aliases such as `vcb.shortcut.using_global_config_for_everything`, `vcb.shortcut.parallel_agents_same_files`, and `vcb.shortcut.screenshot_only_verification`.
- Repaired redirected shortcut aliases in active chapter/topic metadata so existing active cards route through canonical active shortcut IDs where replacements exist.
- Updated README, manifest, LLM maps, validator checks, and report inventory for the bounded repository-contract cleanup slice.
- Revision: replaced false self-redirect rows in `DEPRECATION_REGISTER.md` with manifest-backed redirect rows and tightened validator coverage for deprecation-register self-redirect and manifest-match checks.
- Preserved non-scope boundaries: no new topic-card expansion, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, or new narrative chapters.


## 2026-06-10 — Chunk 28 Codex adjunct surface tool-card expansion

- Added six bounded first-party OpenAI/Codex adjunct surface tool cards for worktrees, subagents, automations, Computer Use, the in-app browser, and the Chrome extension.
- Updated `TOOL_REGISTER.md` to activate the adjunct Codex surface rows already declared in earlier tool anchors.
- Updated README, manifest, LLM maps, tool/category and Codex-surface indexes, task routing, prompt-library routes, AI-coach routes, glossary routes, source-register gate metadata, and validator coverage for active Chunk 28 routing.
- Rechecked official OpenAI/Codex worktrees, subagents, automations, Computer Use, in-app browser, Chrome extension, app settings, app features, and best-practices anchors.
- Revision: repaired stale LLM and semantic Codex-feature lookup paths so advanced-agentic-work, first-party tool guidance, feature-risk/budget/recoverability/failure/shortcut/concept/project/glossary/stability routes surface active Chunk 28 adjunct tool cards before older `vcb.codex.*` feature-card fallbacks; tightened validator coverage for those exact paths.
- Preserved non-scope boundaries: no third-party tool cards, no AGENTS/config/skills/MCP/hooks tool cards, no Codex Security tool card, no field-practice expansion, no pricing expansion, no broad workflow expansion, no broad shortcut expansion, no new shortcut-card expansion, and no narrative chapters.

## 2026-06-11 — Chunk 32 repository/CI/dependency/QA tool-card expansion

- Authored bounded non-AI developer infrastructure tool cards: `tool.github`, `tool.github_actions`, `tool.github_dependabot`, `tool.npm`, `tool.playwright`, and `tool.openssf_scorecard`.
- Activated the six planned tool rows in `TOOL_REGISTER.md` and added a Chunk 32 activation note.
- Added/refreshed official GitHub, npm, Playwright, and OpenSSF source anchors in `SOURCE_REGISTER.md`; exact prices, plan limits, quotas, command flags, permission defaults, vulnerability/scoring details, and UI/setup mechanics remain volatile or snapshot-only.
- Updated README, manifest, LLM source maps, and semantic indexes so GitHub, GitHub Actions, Dependabot, npm, Playwright, and OpenSSF Scorecard intents route to active tool cards before workflow/chapter fallbacks.
- Tightened `scripts/validate_repository.py` for Chunk 32 tool-card schema/status/source posture, semantic routing, manifest/package inventory, report inventory, and scope guardrails.
- Revision: repaired stale Chunk 32 semantic routes in `INDEX_BY_TOOL_CATEGORY.md`, `INDEX_BY_FAILURE_MODE.md`, `PROMPT_LIBRARY.md`, `INDEX_BY_CODEX_SURFACE.md`, and the later `llms.txt` Fast Routing block so active infrastructure tool cards appear before workflow/chapter/shortcut/concept fallbacks; tightened validator coverage for those exact paths.

## Chunk 33 — AI Coding, AI IDE, and AI Planning Tool Cards

- Activated bounded tool-card slice `chunk_33_ai_coding_ide_planning_tool_cards`.
- Added active tool cards for `tool.chatgpt`, `tool.claude`, `tool.cursor`, `tool.github_copilot`, and `tool.windsurf`.
- Updated README, manifest, TOOL_REGISTER, SOURCE_REGISTER, llms maps, primary indexes, and prompt/coaching routes so AI planning, AI IDE choice, alternate AI review, autocomplete, agentic IDE work, and multi-AI comparison route to the smallest active tool card first.
- Tightened `scripts/validate_repository.py` for Chunk 33 active tool-card schema, official vendor/OpenAI source posture, TOOL_REGISTER active status, LLM source-map routing, semantic routing, report inventory, package counts, and scope guardrails.
- Revision: repaired `indexes/INDEX_BY_SHORTCUT.md` report inventory, `indexes/GLOSSARY.md` independent-AI-review routing, `indexes/INDEX_BY_FAILURE_MODE.md` AI-tool-chaos routing, and validator coverage for those exact defects.


## Chunk 37 — Tool-Catalog Routing Consolidation Cleanup

- Consolidated README active tool-card inventory into one canonical active-tool section instead of generation-specific tool-card blocks.
- Removed repetitive generation-specific aggregate tool-card inventory sections from primary indexes while preserving semantic smallest-active-card routes.
- Repaired glossary companion routes for CI, Codex PR review, non-interactive Codex, authentication, authorization, and observability.
- Removed duplicate `tool.github` / `tool.github_actions` rows from `INDEX_BY_PROJECT_TYPE.md` / `## Team or shared repo`.
- Clarified `llms.txt` and `llms-full.txt` routing for Codex execution surfaces, prototype/app-builder choice, production readiness, and canonical source URLs.
- Canonicalized redirected Windsurf/Devin and v0 source URLs in `SOURCE_REGISTER.md` while preserving stable source IDs.
- Tightened `scripts/validate_repository.py` for Chunk 37 cleanup scope, README/index inventory consolidation, duplicate semantic route rows, glossary companion routes, LLM route clarification, and source-register canonical URL hygiene.
- Revision: merged the duplicate `security review` glossary route, removed the duplicate `vcb.prompting.acceptance_criteria` concept route, and tightened validator coverage for duplicate glossary labels and duplicate route IDs in the affected sections.


## Chunk 38 — Field-Practice Candidate Card Expansion

- Authored nine bounded field-practice candidate cards from existing `FIELD_PRACTICES.md` candidate IDs: `vcb.field.chatgpt_pm_codex_implementer`, `vcb.field.fresh_agent_review`, `vcb.field.context_reset_between_tasks`, `vcb.field.agents_md_first`, `vcb.field.skeleton_todo_first`, `vcb.field.strict_typecheck_lint_gates`, `vcb.field.greenfield_vs_production_rule`, `vcb.field.lessons_file_loop`, and `vcb.field.multi_agent_review_consensus`.
- Preserved candidate status, `officially_endorsed: false`, and evidence caveats; no field practice was promoted to official best practice or local reproduction.
- Revised `FIELD_PRACTICES.md` evidence-status wording to use canonical `E4_COMMUNITY_FIELD_REPORT` current-state labels first and tightened validator checks for field-practice evidence taxonomy.
- Updated `FIELD_PRACTICES.md`, README, LLM maps, prompt library, AI-coach routing, primary semantic indexes, source register, manifest, and validator coverage for active candidate-card routing.
- Reused/refreshed selected official OpenAI/Codex sources as principle support while keeping exact product mechanics, model behavior, and feature availability out of stable field-practice claims.
- Preserved non-scope boundaries: no new tool cards, pricing snapshots, shortcut-card expansion, broad workflow expansion, broad security/secrets expansion, or narrative chapters.

<!-- VCB:STOP_RETRIEVAL reason="changelog_complete" -->
<!-- VCB:END_CHANGELOG id=vcb.register.changelog -->
