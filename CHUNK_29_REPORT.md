<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_29 version=0.30.0-draft.chunk29 -->
---
id: vcb.chunk_report.chunk_29
title: Chunk 29 Report — First-Party OpenAI/Codex Customization and Control Tool Cards
artifact_type: chunk_report
version: 0.30.0-draft.chunk29
status: waiting_for_editor_review
chunk_id: chunk_29_codex_customization_control_tool_cards
last_verified: '2026-06-10'
---

# Chunk 29 Report — First-Party OpenAI/Codex Customization and Control Tool Cards

## Scope

Chunk 29 authored a bounded first-party OpenAI/Codex customization and control tool-card slice only. The approved cards are Codex AGENTS.md, Codex Config, Codex Skills, Codex MCP, and Codex Hooks.

No third-party tool cards, Codex Security tool-card expansion, feature-maturity/changelog-monitoring tool cards, pricing expansion, field-practice-card expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters were authored.

## Created files

- `CHUNK_29_REPORT.md`
- `topics/tool-catalog/codex-agents-md.md` for `tool.codex_agents_md`
- `topics/tool-catalog/codex-config.md` for `tool.codex_config`
- `topics/tool-catalog/codex-skills.md` for `tool.codex_skills`
- `topics/tool-catalog/codex-mcp.md` for `tool.codex_mcp`
- `topics/tool-catalog/codex-hooks.md` for `tool.codex_hooks`

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

- `tool.codex_agents_md` — durable repo/project guidance for repeated Codex expectations and local conventions.
- `tool.codex_config` — user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior.
- `tool.codex_skills` — reusable workflow packages with scoped instructions, resources, and optional scripts.
- `tool.codex_mcp` — external tool/context connections with server scope, auth, and provenance guardrails.
- `tool.codex_hooks` — deterministic lifecycle scripts for narrow guardrails, logging, and validation checks.

## Source posture

Chunk 29 uses official OpenAI/Codex source anchors for OpenAI/Codex product facts and preserves the volatile-source rule: exact config keys, hook event names, command flags, UI labels, setup mechanics, model availability, context-window numbers, exact prices, plan limits, usage-credit quantities, and current defaults stay out of stable prose unless routed to official sources or dated volatile snapshots.

The new cards cite/reuse official OpenAI/Codex anchors including `openai.codex.agents_md`, `openai.codex.config_basic`, `openai.codex.config_reference`, `openai.codex.config_advanced`, `openai.codex.skills`, `openai.codex.mcp`, `openai.codex.hooks`, `openai.codex.customization`, `openai.codex.plugins`, `openai.codex.agent_approvals_security`, and `openai.codex.best_practices`. Pricing-sensitive facts route to `vcb.pricing_snapshot.openai_codex`.

## Routing updates

- `README.md`, `manifest.json`, `llms.txt`, and `llms-full.txt` now identify Chunk 29 as the active first-party OpenAI/Codex customization/control tool-card slice.
- `TOOL_REGISTER.md` keeps one declaration per tool ID and marks the five customization/control Codex surfaces active.
- Codex-surface, tool-category, task, prompt-library, glossary, AI-coach, concept, shortcut, stability, risk, recoverability, project-type, budget, and failure-mode indexes now expose the active Chunk 29 customization/control tool cards.
- Semantic routes for AGENTS.md, config, skills, MCP, hooks, persistent customization, external tools, repeatable workflows, and deterministic guardrails route active tool cards before older `vcb.codex.*` feature-topic fallbacks.

## Revision note — editor review

- `indexes/INDEX_BY_TASK.md` team-workflow promotion route repaired so repeated-prompt-to-durable-workflow intent routes to active `tool.codex_agents_md`, `tool.codex_config`, `tool.codex_skills`, `tool.codex_hooks`, and `tool.codex_mcp` before chapter fallbacks.
- `indexes/PROMPT_LIBRARY.md` team-workflow promotion prompt routing repaired so AGENTS.md, config, skill, hook, MCP, automation, PR guidance, and CI-style check intents route to active tool cards before the chapter fallback.
- `indexes/INDEX_BY_TASK.md` tool/hook/plugin/MCP adoption route repaired so skills, MCP, hooks, config, and AGENTS.md tool-card guidance appears before shortcut fallbacks.
- Validator coverage tightened for those exact semantic paths.

## Validation

### Machine-enforced checks

- tool-card schema validation: passed
- TOOL_REGISTER active status for the five customization/control Codex surfaces: passed
- LLM source-map routing for the Chunk 29 customization/control tool-card slice: passed
- semantic index routing for customization/control lookup, task-index setup/config/external-tool routes, team-workflow promotion routes, tool/hook/plugin/MCP adoption routes, prompt-library routes, glossary term routes, and Codex-surface feature fallback ordering: passed
- first-party official OpenAI source posture and pricing snapshot routing: passed
- scope guardrails blocking third-party tool cards, Codex Security tool-card expansion, feature-maturity/changelog-monitoring cards, pricing expansion, field-practice expansion, shortcut expansion, workflow expansion, and narrative chapters: passed
- README, manifest, report, changelog, and package-inventory governance for Chunk 29: passed
- Active Chunk 29 report inventory lists all created and updated files: passed

## Scope boundary

Chunk 29 did not create third-party tool cards, Codex Security tool cards, feature-maturity/changelog-monitoring cards, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_30_editor_scoped_next_slice`.

Exact scope must be set by the editor.

## Unresolved questions

None.

<!-- VCB:STOP_RETRIEVAL reason="chunk_29_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_29 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
