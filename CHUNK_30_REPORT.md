<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_30 version=0.31.0-draft.chunk30 -->
---
id: vcb.chunk_report.chunk_30
title: Chunk 30 Report — First-Party OpenAI/Codex Security Tool Card
artifact_type: chunk_report
version: 0.31.0-draft.chunk30
status: waiting_for_editor_review
chunk_id: chunk_30_codex_security_tool_card
last_verified: '2026-06-11'
---

# Chunk 30 Report — First-Party OpenAI/Codex Security Tool Card

## Scope

Chunk 30 authored a bounded first-party OpenAI/Codex Security tool-card slice only. The approved card is `tool.codex_security`.

No third-party tool cards, feature-maturity/changelog-monitoring tool cards, broad security/secrets topic expansion, pricing expansion, field-practice-card expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters were authored.

## Created files

- `CHUNK_30_REPORT.md`
- `topics/tool-catalog/codex-security.md` for `tool.codex_security`

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

## Tool card authored

- `tool.codex_security` — Codex Security plugin/cloud security review, security scan/diff review, finding validation, threat-model-informed triage, and reviewed fix preparation.

## Source posture

Chunk 30 uses official OpenAI/Codex source anchors for OpenAI/Codex Security product facts and preserves the volatile-source rule: exact availability, feature maturity, UI labels, setup mechanics, scan behavior, workflow names, pricing, plan limits, credit values, command/config details, model availability, and current defaults stay out of stable prose unless routed to official sources or dated volatile snapshots.

The new card cites/reuses official OpenAI/Codex anchors including `openai.codex.security`, `openai.codex.security_plugin`, `openai.codex.security_setup`, `openai.codex.security_threat_model`, `openai.codex.security_faq`, and `openai.codex.agent_approvals_security`. Pricing-sensitive facts route to `vcb.pricing_snapshot.openai_codex`.

## Routing updates

- `README.md`, `manifest.json`, `llms.txt`, and `llms-full.txt` now identify Chunk 30 as the active first-party OpenAI/Codex Security tool-card slice.
- `TOOL_REGISTER.md` keeps one declaration for `tool.codex_security` and marks the Codex Security tool card active.
- Codex-surface, tool-category, task, prompt-library, glossary, AI-coach, concept, shortcut, stability, risk, recoverability, project-type, budget, and failure-mode indexes now expose the active Chunk 30 Codex Security tool card.
- Semantic routes for Codex Security, security scans, security diff scans, finding validation, threat-model tuning, vulnerability backlog/fix-loop work, security review, security-sensitive work, and production/auth/data risk route `tool.codex_security` before older safety, workflow, chapter, or `vcb.codex.*` fallbacks when the user intent is specifically Codex Security tooling.

## Revision Note — Editor Review

- Repaired `llms-full.txt` generic first-party Codex tool-card routing so `tool.codex_security` is included with primary, adjunct, customization/control, and security cards.
- Repaired `indexes/INDEX_BY_TASK.md` / `## Choose or use a Codex feature` so Codex Security feature-selection intent routes to `tool.codex_security` before older `vcb.codex.*` fallbacks.
- Repaired `indexes/PROMPT_LIBRARY.md` / `## Codex feature selection prompt` and `## Auth-sensitive hardening prompt` so Codex Security and auth-sensitive hardening prompts route to `tool.codex_security` first, with `vcb.safety.security_review` as companion review guidance.
- Repaired `indexes/INDEX_FOR_AI_COACHES.md` / `## Human asks how to choose or use a Codex feature` so coaches route Codex Security selection to `tool.codex_security` before older feature-topic fallbacks.
- Tightened `scripts/validate_repository.py` so those exact Chunk 30 routing paths fail validation if `tool.codex_security` is missing or appears after older fallbacks.

## Validation

### Machine-enforced checks

- tool-card schema validation: passed
- TOOL_REGISTER active status for `tool.codex_security`: passed
- LLM source-map routing for the Chunk 30 Codex Security tool-card slice, including generic first-party tool-card routing in `llms-full.txt`: passed
- semantic index routing for Codex Security lookup, generic Codex feature selection, auth-sensitive hardening, security-sensitive task routes, security review prompt routes, risk/failure routes, AI-coach routes, glossary term routes, and Codex-surface/tool-category routes before older fallbacks: passed
- first-party official OpenAI source posture and pricing snapshot routing: passed
- scope guardrails blocking third-party tool cards, feature-maturity/changelog-monitoring cards, broad security/secrets topic expansion, pricing expansion, field-practice expansion, shortcut expansion, workflow expansion, and narrative chapters: passed
- README, manifest, report, changelog, and package-inventory governance for Chunk 30: passed
- Active Chunk 30 report inventory lists all created and updated files: passed

## Scope boundary

Chunk 30 did not create third-party tool cards, feature-maturity/changelog-monitoring cards, broad security/secrets topic expansion, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, or narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_31_editor_scoped_next_slice`.

Exact scope must be set by the editor.

## Unresolved questions

None.

<!-- VCB:STOP_RETRIEVAL reason="chunk_30_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_30 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
