<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_33 version=0.34.0-draft.chunk33 -->
---
id: vcb.chunk_report.chunk_33
title: Chunk 33 Report — AI Coding, AI IDE, and AI Planning Tool Cards
artifact_type: chunk_report
version: 0.34.0-draft.chunk33
status: waiting_for_editor_review
chunk_id: chunk_33_ai_coding_ide_planning_tool_cards
last_verified: '2026-06-11'
---

# Chunk 33 Report — AI Coding, AI IDE, and AI Planning Tool Cards

## Scope

Chunk 33 authored a bounded AI coding, AI IDE, and AI planning tool-card slice only. The approved cards are `tool.chatgpt`, `tool.claude`, `tool.cursor`, `tool.github_copilot`, and `tool.windsurf`.

No app-builder cards, Replit/browser-dev cards, hosting/database/auth/payment/observability cards, design/project-management cards, Docker/container cards, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters were authored.

## Created files

- `CHUNK_33_REPORT.md`
- `topics/tool-catalog/chatgpt.md` for `tool.chatgpt`
- `topics/tool-catalog/claude.md` for `tool.claude`
- `topics/tool-catalog/cursor.md` for `tool.cursor`
- `topics/tool-catalog/github-copilot.md` for `tool.github_copilot`
- `topics/tool-catalog/windsurf.md` for `tool.windsurf`

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

- `tool.chatgpt` — planning, explanation, product thinking, source-backed research synthesis, and data/document analysis.
- `tool.claude` — alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis.
- `tool.cursor` — AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows.
- `tool.github_copilot` — GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance.
- `tool.windsurf` — agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support.

## Source posture

Chunk 33 uses official vendor/OpenAI source anchors for ChatGPT, Claude, Cursor, GitHub Copilot, and Windsurf/Devin facts. It adds `openai.help.chatgpt_capabilities`, `openai.help.chatgpt_projects`, `openai.help.chatgpt_data_analysis`, `anthropic.docs.claude_intro`, `anthropic.docs.claude_code_overview`, `anthropic.docs.prompt_engineering_overview`, `anthropic.support.claude_projects`, `cursor.docs.agent_overview`, `cursor.docs.plan_mode`, `cursor.docs.agent_review`, `cursor.security`, `github.docs.copilot_overview`, `github.docs.copilot_code_suggestions`, `github.docs.copilot_best_practices`, `github.docs.copilot_cloud_agent`, `windsurf.docs.getting_started`, `windsurf.docs.cascade`, `windsurf.docs.plugins`, `windsurf.docs.admin_controls`, and `windsurf.docs.cascade_hooks`.

Exact pricing, plan limits, quota limits, current UI labels, IDE-extension mechanics, model availability, context-window values, feature names, default permissions, and current capability claims stay out of stable prose unless routed to volatile/source-checked sections or dated snapshots.

## Routing updates

- `README.md`, `manifest.json`, `llms.txt`, and `llms-full.txt` now identify Chunk 33 as the active AI coding, AI IDE, and AI planning tool-card slice.
- `TOOL_REGISTER.md` keeps one declaration per Chunk 33 tool ID and marks all five tool cards active.
- Task, tool-category, project-type, risk, recoverability, prompt-library, AI-coach, Codex-surface companion, concept, failure-mode, stability, budget-profile, and glossary indexes now expose active Chunk 33 tool-card routes.
- AI planning, AI IDE choice, alternate AI review, autocomplete, agentic IDE work, and multi-AI comparison intents route to active tool cards before older chapter, workflow, shortcut, or tool-stack fallbacks where those tools are the smallest active card.

## Revision note — Chunk 33 editor feedback

- Repaired updated-file inventory so `indexes/INDEX_BY_SHORTCUT.md` is listed after its Chunk 33 version/status metadata change.
- Repaired `indexes/GLOSSARY.md` independent-AI-review routing so it points to active `tool.claude` and `tool.chatgpt` routes before the chapter fallback.
- Repaired `indexes/INDEX_BY_FAILURE_MODE.md` / `## Tool sprawl and AI-tool chaos` so active Chunk 33 AI-tool cards appear before shortcut and chapter fallbacks.
- Tightened `scripts/validate_repository.py` to catch current-chunk version/status artifacts missing from the Chunk 33 report inventory, stale independent-AI-review routing, and stale AI-tool-chaos failure-mode routing.

## Validation

### Machine-enforced checks

- tool-card schema validation: passed
- TOOL_REGISTER active status for Chunk 33 AI coding / IDE / planning tool cards: passed
- official OpenAI source posture for `tool.chatgpt`: passed
- official vendor source posture for `tool.claude`, `tool.cursor`, `tool.github_copilot`, and `tool.windsurf`: passed
- LLM source-map routing for AI planning, alternate AI review, AI IDE, Copilot, Windsurf, and multi-AI comparison intent: passed
- semantic index routing for ChatGPT, Claude, Cursor, GitHub Copilot, and Windsurf before chapter/workflow/tool-stack/shortcut fallbacks: passed
- glossary independent-AI-review route to active ChatGPT/Claude tool cards before chapter fallback: passed
- failure-mode AI-tool-chaos route to active Chunk 33 tool cards before shortcut/chapter fallbacks: passed
- current-chunk version/status report-inventory coverage: passed
- scope guardrails blocking app-builder cards, Replit/browser-dev cards, hosting/database/auth/payment/observability cards, design/project-management cards, Docker/container cards, field-practice expansion, pricing expansion, shortcut expansion, workflow expansion, and narrative chapters: passed
- README, manifest, report, changelog, and package-inventory governance for Chunk 33: passed
- Active Chunk 33 report inventory lists all created and updated files: passed

## Scope boundary

Chunk 33 did not create app-builder cards, Replit/browser-dev cards, hosting/database/auth/payment/observability cards, design/project-management cards, Docker/container cards, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_34_editor_scoped_next_slice`.

Exact scope must be set by the editor.

## Unresolved questions

None.

<!-- VCB:STOP_RETRIEVAL reason="chunk_33_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_33 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
