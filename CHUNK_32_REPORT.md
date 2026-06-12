<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_32 version=0.33.0-draft.chunk32 -->
---
id: vcb.chunk_report.chunk_32
title: Chunk 32 Report — Repository, CI, Dependency, and QA Tool Cards
artifact_type: chunk_report
version: 0.33.0-draft.chunk32
status: waiting_for_editor_review
chunk_id: chunk_32_repo_ci_dependency_quality_tool_cards
last_verified: '2026-06-11'
---

# Chunk 32 Report — Repository, CI, Dependency, and QA Tool Cards

## Scope

Chunk 32 authored a bounded repository, CI, dependency, and quality-assurance tool-card slice only. The approved cards are `tool.github`, `tool.github_actions`, `tool.github_dependabot`, `tool.npm`, `tool.playwright`, and `tool.openssf_scorecard`.

No AI IDE/tool cards, app-builder cards, hosting/database/auth/payment/observability cards, design/project-management cards, Docker/container cards, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters were authored.

## Created files

- `CHUNK_32_REPORT.md`
- `topics/tool-catalog/github.md` for `tool.github`
- `topics/tool-catalog/github-actions.md` for `tool.github_actions`
- `topics/tool-catalog/github-dependabot.md` for `tool.github_dependabot`
- `topics/tool-catalog/npm.md` for `tool.npm`
- `topics/tool-catalog/playwright.md` for `tool.playwright`
- `topics/tool-catalog/openssf-scorecard.md` for `tool.openssf_scorecard`

## Updated files

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
- `TOOL_REGISTER.md`
- `CHANGELOG.md`
- `TREE.txt`
- `indexes/GLOSSARY.md`
- `indexes/INDEX_BY_CODEX_SURFACE.md`
- `indexes/INDEX_BY_CONCEPT.md`
- `indexes/INDEX_BY_FAILURE_MODE.md`
- `indexes/INDEX_BY_PROJECT_TYPE.md`
- `indexes/INDEX_BY_RECOVERABILITY.md`
- `indexes/INDEX_BY_RISK_LEVEL.md`
- `indexes/INDEX_BY_STABILITY.md`
- `indexes/INDEX_BY_TASK.md`
- `indexes/INDEX_BY_TOOL_CATEGORY.md`
- `indexes/INDEX_FOR_AI_COACHES.md`
- `indexes/PROMPT_LIBRARY.md`
- `scripts/validate_repository.py`

## Tool cards authored

- `tool.github` — repository collaboration, PRs, branch protection, and review source of truth.
- `tool.github_actions` — CI workflows, automation evidence, secrets, token permissions, and check artifacts.
- `tool.github_dependabot` — dependency alerts, version/security update PRs, and maintenance queue review.
- `tool.npm` — JavaScript package manifests, scripts, lockfiles, installs, and audit evidence.
- `tool.playwright` — browser/end-to-end tests, screenshots, traces, and UI verification evidence.
- `tool.openssf_scorecard` — supply-chain health signals and repository hardening checklist.

## Source posture

Chunk 32 uses official vendor/project source anchors for GitHub, GitHub Actions, Dependabot, npm, Playwright, and OpenSSF Scorecard facts. It adds `github.docs.repositories`, `github.docs.actions_workflow_syntax`, `github.docs.dependabot_quickstart`, `playwright.docs.intro`, `playwright.docs.writing_tests`, `playwright.docs.ci`, `openssf.scorecard_checks`, and `openssf.scorecard_action`, and refreshes reused GitHub, npm, Playwright, and OpenSSF anchors used by the cards.

Exact pricing, plan limits, quota limits, current UI labels, command flags, policy defaults, permission defaults, vulnerability/scoring details, setup mechanics, and package-manager/browser-runner defaults stay out of stable prose unless routed to volatile/source-checked sections or dated snapshots.

## Routing updates

- `README.md`, `manifest.json`, `llms.txt`, and `llms-full.txt` now identify Chunk 32 as the active repository/CI/dependency/QA infrastructure tool-card slice.
- `TOOL_REGISTER.md` keeps one declaration per Chunk 32 tool ID and marks all six tool cards active.
- Task, tool-category, project-type, risk, recoverability, prompt-library, AI-coach, Codex-surface companion, concept, failure-mode, stability, and glossary indexes now expose active Chunk 32 tool-card routes.
- GitHub, GitHub Actions, Dependabot, npm, Playwright, and OpenSSF Scorecard intents route to active tool cards before older workflow, chapter, shortcut, or concept fallbacks where those tools are the smallest active card.

## Revision Note

- Repaired `INDEX_BY_TOOL_CATEGORY.md` stale `registered` / `planned` labels for active Chunk 32 infrastructure tool rows.
- Repaired `INDEX_BY_FAILURE_MODE.md` dependency/CI semantic routes so `tool.npm`, `tool.github_dependabot`, `tool.openssf_scorecard`, `tool.github_actions`, and `tool.playwright` appear before older workflow/chapter/shortcut/failure fallbacks where relevant.
- Repaired `PROMPT_LIBRARY.md` PR review, dependency migration, and frontend state-matrix routes so `tool.github`, `tool.github_actions`, `tool.github_dependabot`, `tool.npm`, `tool.openssf_scorecard`, and `tool.playwright` route before chapter/workflow fallbacks.
- Repaired `INDEX_BY_CODEX_SURFACE.md` GitHub/PR and non-interactive/CI companion routes so `tool.github` and `tool.github_actions` are exposed before older Codex/workflow fallbacks.
- Repaired the later `llms.txt` Fast Routing block so PR/repository-review evidence, frontend/browser evidence, and dependency/package/supply-chain intents retrieve the active Chunk 32 tool cards before workflow fallbacks.
- Tightened `scripts/validate_repository.py` for stale `registered` / `planned` labels, dependency/CI failure-mode routes, PR/dependency/frontend prompt routes, Codex-surface companion routes, and the later LLM Fast Routing lines.

## Validation

### Machine-enforced checks

- tool-card schema validation: passed
- TOOL_REGISTER active status for Chunk 32 infrastructure tool cards: passed
- LLM source-map routing for repository/CI/dependency/QA tool-card intent: passed
- semantic index routing for GitHub, GitHub Actions, Dependabot, npm, Playwright, and OpenSSF Scorecard before workflow/chapter fallbacks: passed
- semantic route priority checks for tool-category labels, dependency/CI failure modes, PR/dependency/frontend prompt routes, Codex-surface companion routes, and later LLM Fast Routing lines: passed
- official vendor source posture and pricing volatility guardrails: passed
- scope guardrails blocking AI IDE/tool cards, app-builder cards, hosting/database/auth/payment/observability cards, design/project-management cards, Docker/container cards, field-practice expansion, pricing expansion, shortcut expansion, workflow expansion, and narrative chapters: passed
- README, manifest, report, changelog, and package-inventory governance for Chunk 32: passed
- Active Chunk 32 report inventory lists all created and updated files: passed

## Scope boundary

Chunk 32 did not create AI IDE/tool cards, app-builder cards, hosting/database/auth/payment/observability cards, design/project-management cards, Docker/container cards, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_33_editor_scoped_next_slice`.

Exact scope must be set by the editor.

## Unresolved questions

None.

<!-- VCB:STOP_RETRIEVAL reason="chunk_32_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_32 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
