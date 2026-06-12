---
id: vcb.chunk_report.chunk_6
artifact_type: chunk_report
version: 0.7.0-draft.chunk6
status: waiting_for_editor_review
created_on: 2026-06-08
last_verified: 2026-06-08
review_cadence: chunk_gate
---

<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_6 version=0.7.0-draft.chunk6 -->

# Chunk 6 Report — Frontend, Refactoring, and Dependencies

## Scope

Chunk 6 covers only:

- Chapter 15 — Frontend Work: Screenshots, Browser Checks, and Taste
- Chapter 16 — Refactoring Without Breaking Everything
- Chapter 17 — Dependency, Package, and Framework Decisions

Explicit non-scope: AGENTS.md deep dive, config deep dive, skills, MCP, hooks, CI/non-interactive automation, review/security/shipping chapters, cloud delegation, subagents, automations, computer-use chapter, tool catalog, pricing snapshots, and full shortcut cards.

## Canonical Review Package

Canonical review package: `vibe-coding-bible-chunk-6-20260608T185355Z-authoritative.zip`.

## Files Created

```text
CHUNK_6_REPORT.md
chapters/15-frontend-work.md
chapters/16-refactoring-without-breaking-everything.md
chapters/17-dependency-package-framework-decisions.md
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

- Added `vcb.chapter.frontend_work`.
- Added `vcb.chapter.refactoring_without_breaking_everything`.
- Added `vcb.chapter.dependency_package_framework_decisions`.
- Updated routing indexes for frontend/browser checks, UI taste, safe refactoring, characterization tests, package/dependency review, and framework decisions.
- Updated `PROMPT_LIBRARY.md` with frontend screenshot/browser-check prompts, UI state matrix prompt, refactor plan/refactor-one-boundary prompts, and dependency decision/no-new-dependency prompts.
- Registered planned shortcut IDs for `vcb.shortcut.eyeballing_ui`, `vcb.shortcut.broad_refactor`, and `vcb.shortcut.framework_churn`.
- Added source anchors for current official Codex frontend/browser/computer-use workflows, W3C accessibility guidance, MDN responsive design guidance, Fowler refactoring guidance, GitHub dependency review/Dependabot, and npm package auditing.
- Extended repository validation to check required Markdown headings and VCB section marker pairing.
- Kept exact pricing, current usage limits, model routing, current package recommendations, and volatile UI command details out of stable prose.

## Sources Checked

- `openai.codex.use_cases.web_development` — official current anchor for Codex web-development workflows that build responsive UI from designs/prompts and verify UI in browser-oriented loops.
- `openai.codex.use_cases.frontend_designs` — official current anchor for translating screenshots/design briefs into responsive UI with visual checks and Playwright/browser verification.
- `openai.codex.use_cases.make_granular_ui_changes` — official current anchor for one-small-change-at-a-time UI iteration with browser verification.
- `openai.codex.use_cases.qa_computer_use` — official current anchor for browser/flow QA reports with repro steps, expected result, actual result, severity, and triage summary.
- `openai.codex.use_cases.refactor_your_codebase` — official current anchor for behavior-preserving refactor passes, dead-code removal, duplicated-logic cleanup, and splitting migrations/dependency upgrades out of refactors.
- `openai.codex.workflows` — official current anchor for explicit context, clear definition of done, context notes, and verification in Codex workflows.
- `openai.codex.agents_md` — official current anchor for persistent dependency-related working agreements such as asking before adding production dependencies.
- `openai.codex.use_cases.dependency_incident_audits` — official current anchor for read-only dependency incident audits over manifests, lockfiles, CI, scripts, and untrusted-code boundaries.
- `w3c.wcag_overview` — W3C anchor for WCAG principles and testable success criteria.
- `playwright.docs.visual_comparisons` and `playwright.docs.screenshots` — official Playwright anchors for screenshot capture and visual comparison checks.
- `npm.docs.package_json`, `npm.docs.package_lock`, and `npm.docs.security_audit` — official npm anchors for package dependency metadata, lockfiles, and dependency security audits.
- `github.docs.dependency_graph`, `github.docs.dependency_review`, `github.docs.dependabot_alerts`, and `openssf.scorecard` — official/vendor anchors for dependency graph/review, vulnerable dependency detection, and package health/security scoring.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for durable frontend/refactoring/dependency-control framing; not an evidence level.

## Validation Summary

```text
VCB validation passed
Actual source files tracked in manifest: 80
Manifest source-file inventory matches actual package files: yes
source_files rich objects preserved: yes
Markdown files: 56
Markdown files with frontmatter/metadata fences: 56 / 56
Markdown files with VCB markers: 56 / 56
JSON files: 8
JSON parse check: passed
JSON Schema draft compile check: passed
Active chapter/topic files validated: 24
Active chapter/topic frontmatter schema validation: passed
Required Markdown headings present in active chapter/topic files: passed
VCB section marker pairing in active chapter/topic files: passed
New chapter files created in Chunk 6: 3
New chapter frontmatter schema validation: passed, 3 / 3
Required Chunk 6 files present: passed
Required chapter sections present: passed
Required VCB markers present in new chapter files: passed
README next-chunk route checked against manifest: passed
Index namespace drift scan covers active and planned index routes: passed
Active index routes point to authored active IDs: passed
Active shortcut_profiles resolve to SHORTCUT_REGISTER: passed
Planned shortcut index routes resolve to SHORTCUT_REGISTER or approved future shortcut IDs: passed
Evidence source IDs resolve to SOURCE_REGISTER or declared synthesis IDs: passed
SHORTCUT_REGISTER table row shape: passed
evidence_basis/source_kind values validated against schemas: passed
No exact pricing, limits, model-routing, package-version recommendations, or context-window numbers added to stable prose: passed
Canonical review package policy: one timestamped authoritative zip
Report final line: AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
```

Known exception: `.gitkeep` files are structural placeholders and intentionally contain no frontmatter or VCB markers.

## Design Decisions

1. **Frontend work is visual-evidence driven.** Chapter 15 teaches screenshots, state matrices, browser checks, responsiveness, accessibility basics, and taste constraints without treating exact Codex browser/computer-use mechanics as stable.
2. **Refactoring is behavior-preservation first.** Chapter 16 separates refactor, rewrite, and feature change, and treats broad cleanup as a risk-managed shortcut.
3. **Dependencies are framed as liabilities plus capability.** Chapter 17 uses “no-new-dependency first” and requires explicit package/framework justification before installs or lockfile changes.
4. **Shortcut handling stays harm-reduction based.** Risky behaviors are not moralized; the chapters explain when shortcuts are acceptable and what guardrails reduce blast radius.
5. **Source IDs are explicit.** New Evidence sections use registered source IDs and avoid unresolved source aliases.

## Unresolved Questions

1. Whether frontend work should later split into separate topic cards for screenshots, state matrices, accessibility checks, browser automation, and visual regression.
2. Whether refactoring should later split into characterization tests, behavior-preserving moves, public API preservation, and rewrite-vs-refactor decision cards.
3. Whether dependency decisions should later split into package audit, lockfile review, framework decision, license review, and supply-chain incident-response cards.
4. Whether the validator should later validate source-register duplicate URLs and source aliases.

## Next Recommended Chunk

Chunk 7, only after editor approval:

- Chapter 18 — `AGENTS.md`: Your Repo’s Operating Manual for Codex
- Chapter 19 — Codex Config: Making Good Defaults Automatic
- Chapter 20 — Skills: Reusable Workflows for Repeated Tasks
- Chapter 21 — MCP: Giving Codex External Tools Without Creating Chaos
- Chapter 22 — Hooks and Deterministic Guardrails

Do not start Chunk 8 review/security/shipping material yet.

<!-- VCB:STOP_RETRIEVAL reason="chunk_6_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_6 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
