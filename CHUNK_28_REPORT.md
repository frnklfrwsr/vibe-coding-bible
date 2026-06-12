<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_28 version=0.29.0-draft.chunk28 -->
---
id: vcb.chunk_report.chunk_28
title: Chunk 28 Report — First-Party OpenAI/Codex Adjunct Surface Tool Cards
artifact_type: chunk_report
version: 0.29.0-draft.chunk28
status: waiting_for_editor_review
chunk_id: chunk_28_codex_adjunct_surface_tool_cards
last_verified: '2026-06-10'
---

# Chunk 28 Report — First-Party OpenAI/Codex Adjunct Surface Tool Cards

## Scope

Chunk 28 authored a bounded first-party OpenAI/Codex adjunct surface tool-card slice only. The approved adjunct cards are Codex Worktrees, Codex Subagents, Codex Automations, Codex Computer Use, Codex In-App Browser, and Codex Chrome Extension.

No third-party tool cards, AGENTS/config/skills/MCP/hooks tool-card expansion, Codex Security tool-card expansion, pricing expansion, field-practice-card expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters were authored.

## Created files

- `CHUNK_28_REPORT.md`
- `topics/tool-catalog/codex-worktrees.md` for `tool.codex_worktrees`
- `topics/tool-catalog/codex-subagents.md` for `tool.codex_subagents`
- `topics/tool-catalog/codex-automations.md` for `tool.codex_automations`
- `topics/tool-catalog/codex-computer-use.md` for `tool.codex_computer_use`
- `topics/tool-catalog/codex-browser.md` for `tool.codex_browser`
- `topics/tool-catalog/codex-chrome-extension.md` for `tool.codex_chrome_extension`

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
- `indexes/INDEX_BY_BUDGET_PROFILE.md`
- `indexes/INDEX_BY_CODEX_SURFACE.md`
- `indexes/INDEX_BY_CONCEPT.md`
- `indexes/INDEX_BY_FAILURE_MODE.md`
- `indexes/INDEX_BY_PROJECT_TYPE.md`
- `indexes/INDEX_BY_RECOVERABILITY.md`
- `indexes/INDEX_BY_RISK_LEVEL.md`
- `indexes/INDEX_BY_SHORTCUT.md`
- `indexes/INDEX_BY_STABILITY.md`
- `indexes/INDEX_BY_TASK.md`
- `indexes/INDEX_BY_TOOL_CATEGORY.md`
- `indexes/INDEX_FOR_AI_COACHES.md`
- `indexes/PROMPT_LIBRARY.md`
- `scripts/validate_repository.py`

## Tool cards authored

- `tool.codex_worktrees` — worktree isolation for parallel local/app work and automation change separation.
- `tool.codex_subagents` — parallel specialist agents for bounded analysis and disjoint implementation work.
- `tool.codex_automations` — recurring/report-first Codex background work with review owner and stop conditions.
- `tool.codex_computer_use` — desktop GUI operation with app permissions and human supervision.
- `tool.codex_browser` — in-app rendered-page preview, comments, screenshots, and browser verification.
- `tool.codex_chrome_extension` — signed-in Chrome browser workflows with website approvals and account-risk controls.

## Source posture

Chunk 28 uses official OpenAI/Codex source anchors for OpenAI/Codex product facts and preserves the volatile-source rule: exact prices, plan limits, usage-credit quantities, model availability, UI mechanics, command flags, and context-window numbers stay out of stable prose unless routed to dated pricing or volatile snapshots.

The new cards cite/reuse official OpenAI/Codex anchors including `openai.codex.app_worktrees`, `openai.codex.subagents`, `openai.codex.subagent_concepts`, `openai.codex.app_automations`, `openai.codex.app_computer_use`, `openai.codex.app_browser`, `openai.codex.chrome_extension`, `openai.codex.app_settings`, `openai.codex.app_features`, `openai.codex.best_practices`, and `openai.codex.sandboxing`. Pricing-sensitive facts route to `vcb.pricing_snapshot.openai_codex`.

## Routing updates

- `README.md`, `manifest.json`, `llms.txt`, and `llms-full.txt` now identify Chunk 28 as the active first-party OpenAI/Codex adjunct surface tool-card slice.
- `TOOL_REGISTER.md` keeps one declaration per tool ID and marks the six adjunct Codex surfaces active.
- Codex-surface, tool-category, task, prompt-library, glossary, AI-coach, concept, shortcut, stability, risk, recoverability, project-type, budget, and failure-mode indexes now expose the active Chunk 28 adjunct tool cards.
- Semantic routes for worktrees, subagents, automations, browser, Chrome, GUI, Computer Use, and Codex feature/surface selection route active tool cards before older `vcb.codex.*` feature-topic fallbacks.

## Revision note — editor review routing repair

- Repaired the stale `llms.txt` advanced-agentic-work route so subagent, automation, Computer Use, browser/GUI, and parallel adjunct-surface intent routes to active Chunk 28 `tool.codex_*` cards before older `vcb.codex.*` companion mechanics.
- Expanded the `llms-full.txt` first-party Codex tool-card guidance route so it includes both primary Chunk 27 and adjunct Chunk 28 tool cards.
- Patched Codex feature/risk/budget/recoverability/failure/shortcut/concept/project/glossary/stability semantic sections so active adjunct tool cards appear before older `vcb.codex.*` feature-card fallbacks.
- Tightened `scripts/validate_repository.py` to fail on those stale LLM routes and on Codex-feature semantic sections that omit active adjunct tool cards or place them after older feature-topic fallbacks.

## Validation

### Machine-enforced checks

- tool-card schema validation: passed
- TOOL_REGISTER active status for the six adjunct Codex surfaces: passed
- LLM source-map routing for the Chunk 28 adjunct tool-card slice: passed
- semantic index routing for adjunct Codex surface lookup, task-index cloud/subagent/browser/GUI routes, prompt-library adjunct prompts, and Codex-surface feature fallback ordering: passed
- first-party official OpenAI source posture and pricing snapshot routing: passed
- scope guardrails blocking third-party tool cards, Codex customization/security tool-card expansion, pricing expansion, field-practice expansion, shortcut expansion, workflow expansion, and narrative chapters: passed
- README, manifest, report, changelog, and package-inventory governance for Chunk 28: passed
- Active Chunk 28 report inventory lists all created and updated files: passed

## Scope boundary

Chunk 28 did not create third-party tool cards, AGENTS/config/skills/MCP/hooks tool cards, Codex Security tool cards, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_29_editor_scoped_next_slice`.

Exact scope must be set by the editor.

## Unresolved questions

None.

<!-- VCB:STOP_RETRIEVAL reason="chunk_28_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_28 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
