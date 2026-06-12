<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_31 version=0.32.0-draft.chunk31 -->
---
id: vcb.chunk_report.chunk_31
title: Chunk 31 Report — First-Party OpenAI/Codex Governance and Maintenance Tool Cards
artifact_type: chunk_report
version: 0.32.0-draft.chunk31
status: waiting_for_editor_review
chunk_id: chunk_31_codex_governance_tool_cards
last_verified: '2026-06-11'
---

# Chunk 31 Report — First-Party OpenAI/Codex Governance and Maintenance Tool Cards

## Scope

Chunk 31 authored a bounded first-party OpenAI/Codex governance and maintenance tool-card slice only. The approved cards are `tool.codex_feature_maturity` and `tool.codex_changelog_monitoring`.

No third-party tool cards, broad tool-card expansion, Codex Security expansion, feature/security expansion, pricing expansion, field-practice-card expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, broad security/secrets expansion, or narrative chapters were authored.

## Created files

- `CHUNK_31_REPORT.md`
- `topics/tool-catalog/codex-feature-maturity.md` for `tool.codex_feature_maturity`
- `topics/tool-catalog/codex-changelog-monitoring.md` for `tool.codex_changelog_monitoring`

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

- `tool.codex_feature_maturity` — Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence.
- `tool.codex_changelog_monitoring` — official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes.

## Source posture

Chunk 31 uses official OpenAI/Codex source anchors for OpenAI/Codex governance and maintenance facts. It refreshes `openai.codex.feature_maturity` and `openai.codex.changelog`. It reuses the existing `openai.codex.overview` and `openai.codex.use_cases.update_documentation` anchors without changing their older checked dates. Pricing-sensitive material routes to the active pricing snapshot `vcb.pricing_snapshot.openai_codex`.

Exact maturity labels, current feature statuses, release dates, UI labels, availability, model availability, prices, plan limits, credit values, context-window numbers, and brittle command/config mechanics stay out of stable prose unless routed to volatile/source-checked sections or dated snapshots.

## Routing updates

- `README.md`, `manifest.json`, `llms.txt`, and `llms-full.txt` now identify Chunk 31 as the active first-party OpenAI/Codex governance and maintenance tool-card slice.
- `TOOL_REGISTER.md` keeps one declaration per Chunk 31 tool ID and marks `tool.codex_feature_maturity` and `tool.codex_changelog_monitoring` active.
- Codex-surface, tool-category, task, stability, prompt-library, glossary, AI-coach, concept, shortcut, risk, recoverability, project-type, budget, and failure-mode indexes now expose the active Chunk 31 governance/maintenance tool cards.
- Semantic routes for feature maturity, currentness, production-readiness posture, official Codex release monitoring, deprecation watch, source-register updates, and stale guidance repair route the new tool cards before older `vcb.codex.*`, source-register, deprecation-register, or chapter fallbacks.


## Revision note

- Nested manifest source-artifacts report/topic/tool-catalog inventories were repaired so derived counts and listed tool-catalog files match the actual package files.
- `README.md` now exposes an active Codex governance and maintenance tool-card section for `tool.codex_feature_maturity` and `tool.codex_changelog_monitoring`.
- Source wording was repaired so only Feature Maturity and Changelog anchors are described as refreshed.
- Codex overview and documentation-update anchors are explicitly described as reused without changing their older checked dates.
- `indexes/INDEX_BY_CONCEPT.md` now routes Codex mental-model feature-maturity intent to `tool.codex_feature_maturity` before the companion `vcb.codex.feature_maturity` mechanics card.
- `llms.txt` Codex Feature Card Fast Routing now routes feature-maturity and changelog-monitoring intents to active governance/maintenance tool cards before companion `vcb.codex.*` mechanics.
- `scripts/validate_repository.py` was tightened for nested manifest derived counts, README active governance/maintenance routing, source overclaim detection, concept-index feature-maturity routing, and LLM feature-card fast-routing checks.
- Root-level manifest `source_file_count` and `source_files_count` aliases were repaired to match the 278-file package inventory and the top-level manifest source_files length.
- `scripts/validate_repository.py` was further tightened so root-level manifest count aliases fail validation when stale or inconsistent with the manifest source_files list.

## Validation

### Machine-enforced checks

- tool-card schema validation: passed
- TOOL_REGISTER active status for `tool.codex_feature_maturity` and `tool.codex_changelog_monitoring`: passed
- LLM source-map routing for the Chunk 31 governance/maintenance tool-card slice: passed
- semantic index routing for feature-maturity, changelog, current/deprecation review, Bible update, Codex feature selection, AI-coach update guidance, stability routing, and glossary term routes before older fallbacks: passed
- first-party official OpenAI source posture and pricing snapshot routing: passed
- scope guardrails blocking third-party tool cards, broad tool-card expansion, field-practice expansion, pricing expansion, shortcut expansion, workflow expansion, broad security/secrets expansion, and narrative chapters: passed
- README, manifest, report, changelog, and package-inventory governance for Chunk 31: passed
- root-level manifest source_file_count and source_files_count aliases match the package inventory and source_files length: passed
- Active Chunk 31 report inventory lists all created and updated files: passed

## Scope boundary

Chunk 31 did not create third-party tool cards, broad tool-card expansion, Codex Security expansion, feature/security expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, broad shortcut expansion, new shortcut-card expansion, broad security/secrets expansion, or narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_32_editor_scoped_next_slice`.

Exact scope must be set by the editor.

## Unresolved questions

None.

<!-- VCB:STOP_RETRIEVAL reason="chunk_31_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_31 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
