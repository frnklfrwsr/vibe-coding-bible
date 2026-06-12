<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_27 version=0.28.0-draft.chunk27 -->
---
id: vcb.chunk_report.chunk_27
title: Chunk 27 Report — First-Party OpenAI/Codex Primary Tool Cards
artifact_type: chunk_report
version: 0.28.0-draft.chunk27
status: waiting_for_editor_review
chunk_id: chunk_27_codex_primary_tool_cards
last_verified: '2026-06-10'
---

# Chunk 27 Report — First-Party OpenAI/Codex Primary Tool Cards

## Scope

Chunk 27 authored a bounded first-party OpenAI/Codex primary tool-card slice only. The approved execution-surface cards are Codex umbrella, Codex App, Codex CLI, Codex IDE Extension, Codex Cloud, Codex GitHub Review, and `codex exec`.

No third-party tool cards, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters were authored.

## Created files

- `CHUNK_27_REPORT.md`
- `topics/tool-catalog/codex.md` for `tool.codex`
- `topics/tool-catalog/codex-app.md` for `tool.codex_app`
- `topics/tool-catalog/codex-cli.md` for `tool.codex_cli`
- `topics/tool-catalog/codex-ide-extension.md` for `tool.codex_ide_extension`
- `topics/tool-catalog/codex-cloud.md` for `tool.codex_cloud`
- `topics/tool-catalog/codex-github-review.md` for `tool.codex_github_review`
- `topics/tool-catalog/codex-exec.md` for `tool.codex_exec`

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

- `tool.codex` — primary Codex family and surface-selection hub.
- `tool.codex_app` — desktop/local command-center surface.
- `tool.codex_cli` — terminal-native Codex surface.
- `tool.codex_ide_extension` — IDE-context Codex surface.
- `tool.codex_cloud` — cloud/background delegation surface.
- `tool.codex_github_review` — GitHub pull-request review surface.
- `tool.codex_exec` — non-interactive CLI/script/CI-style execution surface.

## Source posture

Chunk 27 uses official OpenAI/Codex source anchors for OpenAI/Codex product facts and preserves the existing volatile-source rule: exact prices, plan limits, credit values, model availability, UI mechanics, command flags, and context-window numbers stay out of stable prose unless routed to dated pricing or volatile snapshots.

The new cards cite/reuse official OpenAI/Codex anchors including `openai.codex.overview`, `openai.codex.app`, `openai.codex.cli`, `openai.codex.ide`, `openai.codex.cloud`, `openai.codex.github_review`, `openai.codex.noninteractive`, `openai.codex.cli_reference`, `openai.codex.agent_approvals_security`, `openai.codex.best_practices`, and `openai.codex.feature_maturity`. Pricing-sensitive facts route to `vcb.pricing_snapshot.openai_codex`.

## Routing updates

- `README.md`, `manifest.json`, `llms.txt`, and `llms-full.txt` now identify Chunk 27 as the active first-party OpenAI/Codex primary tool-card slice.
- `TOOL_REGISTER.md` keeps one declaration per tool ID and marks the seven primary Codex execution surfaces active.
- Primary routing indexes now expose the active Chunk 27 tool cards before lower-level fallbacks where relevant.
- LLM source maps include fast routes for surface-selection, app, CLI, IDE, cloud, GitHub review, and non-interactive execution intents.

## Revision note

Revision after editor review repaired semantic routing drift for active Chunk 27 tool cards. `indexes/INDEX_BY_TASK.md` now routes surface-selection, non-interactive/CI, PR review, and cloud/browser/GUI task intents to the smallest active `tool.codex*` cards before chapter, workflow, shortcut, or feature-topic fallbacks. `indexes/PROMPT_LIBRARY.md` now routes the Codex feature/surface-selection prompt to active tool cards before companion `vcb.codex.*` mechanics routes. `llms.txt` no longer routes “which Codex surface to use” only to `vcb.codex.*` feature topics; it retrieves `tool.codex` first and then the smallest active surface-specific tool card. `scripts/validate_repository.py` now fails these exact stale-route defects.

## Validation

### Machine-enforced checks
- tool-card schema validation: passed
- TOOL_REGISTER active status for the seven primary Codex execution surfaces: passed
- LLM source-map routing for the Chunk 27 tool-card slice: passed
- semantic index routing for primary Codex execution-surface lookup, task-index surface selection, prompt-library feature selection, and LLM fast-routing fallback repair: passed
- first-party official OpenAI source posture and pricing snapshot routing: passed
- scope guardrails blocking third-party tool cards, pricing expansion, field-practice expansion, shortcut expansion, workflow expansion, and narrative chapters: passed
- README, manifest, report, changelog, and package-inventory governance for Chunk 27: passed
- Active Chunk 27 report inventory lists all created and updated files: passed

## Scope boundary

Chunk 27 did not create third-party tool cards, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or new narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_28_editor_scoped_next_slice`.

Exact scope must be set by the editor.

## Unresolved questions

None.

<!-- VCB:STOP_RETRIEVAL reason="chunk_27_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_27 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
