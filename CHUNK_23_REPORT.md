<!-- VCB:BEGIN_REPORT id=vcb.chunk_report.chunk_23 version=0.24.0-draft.chunk23 -->
---
id: vcb.chunk_report.chunk_23
title: CHUNK_23_REPORT
artifact_type: chunk_report
chunk_id: chunk_23_tool_sprawl_skill_shortcut_topic_cards
version: 0.24.0-draft.chunk23
status: waiting_for_editor_review
created_on: '2026-06-10'
last_verified: '2026-06-10'
next_review_due: '2026-07-10'
review_cadence: monthly
---

# Chunk 23 Report — Tool-Sprawl, Skill, and Reusable-Process Shortcut Topic Cards

## Chunk ID

`chunk_23_tool_sprawl_skill_shortcut_topic_cards`

## Scope completed

Bounded tool-sprawl, skills, MCP, plugin, hook, and reusable-workflow shortcut-card expansion focused on skill overkill, skill sprawl, general tool sprawl, MCP tool sprawl, brittle hooks, tiny-project process overhead, team workflow without a team, and blind playbook reuse.

## Revision note — editor changes required

This revision fixes Chunk 23-only repository-governance defects reported by the editor: active canonical Chunk 23 IDs no longer redirect to older cards in `manifest.json`; `llms.txt` and `llms-full.txt` now keep one compact Chunk 23 full-list routing section; general Fast Routing now routes direct skill/tool/MCP/hook/process shortcut intents to active Chunk 23 cards before fallback; and validator coverage now fails active-ID redirect shadowing and duplicate current-chunk LLM source-map sections.


## Files created

- `CHUNK_23_REPORT.md`
- `topics/shortcuts/skill-overkill.md`
- `topics/shortcuts/skill-sprawl.md`
- `topics/shortcuts/tool-sprawl.md`
- `topics/shortcuts/tool-sprawl-mcp.md`
- `topics/shortcuts/brittle-hooks.md`
- `topics/shortcuts/process-overhead-for-tiny-project.md`
- `topics/shortcuts/team-workflow-without-team.md`
- `topics/shortcuts/copy-pasting-playbook-blindly.md`

## Files updated

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `SOURCE_REGISTER.md`
- `SHORTCUT_REGISTER.md`
- `CHANGELOG.md`
- `TREE.txt`
- `scripts/validate_repository.py`
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

## Source posture

Chunk 23 adds the editor-feedback gate source `vcb.register.editor_feedback_chunk_22` and reuses existing official OpenAI/Codex source IDs for skills, MCP, plugins, hooks, config, agent approvals/security, workflows, and best practices, plus OWASP anchors where external tool/context or supply-chain risk is discussed. Maintainer synthesis remains labeled as `VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE`. Product mechanics, skill discovery behavior, MCP/tool controls, plugin behavior, hook runtime details, UI labels, and permission defaults remain volatile and source-checked.

## Validation summary

Ran `python scripts/validate_repository.py` before packaging and again after extracting the submitted package.

### Machine-enforced checks

- New tool-sprawl/skill/reusable-workflow shortcut topic files created in Chunk 23: passed
- Required Chunk 23 tool-sprawl/skill shortcut-card slice present: passed
- Manifest tool_sprawl_skill_shortcut_cards map matches authored Chunk 23 files: passed
- Manifest chunk_23_required_topic_ids matches authored Chunk 23 IDs: passed
- Manifest redirects do not shadow active Chunk 23 canonical IDs: passed
- Required VCB markers present in new Chunk 23 shortcut files: passed
- Required sections present in new Chunk 23 shortcut files: passed
- SHORTCUT_REGISTER marks authored Chunk 23 shortcut IDs active: passed
- SHORTCUT_REGISTER shortcut rows are inside declared shortcut tables: passed
- Primary indexes route active Chunk 23 tool-sprawl/skill shortcut cards: passed
- Prompt library routes active Chunk 23 tool-sprawl/skill shortcut cards: passed
- AI coach index routes active Chunk 23 tool-sprawl/skill shortcut cards: passed
- LLM source maps route active Chunk 23 tool-sprawl/skill shortcut cards: passed
- LLM source maps contain one consolidated Chunk 23 full-list routing section: passed
- General Fast Routing includes direct Chunk 23 shortcut-intent routes: passed
- Generic LLM shortcut route covers active Chunk 20, Chunk 21, Chunk 22, and Chunk 23 shortcut-card slices: passed
- Manifest redirect maps do not redirect active Chunk 23 canonical IDs away from authored cards: passed
- LLM source maps contain one compact Chunk 23 full-list section and no duplicate adjacent full-list sections: passed
- General Fast Routing includes semantic Chunk 23 shortcut intents before fallback routing: passed
- Chunk 23 source-map and stale-route claims are backed by redirect-shadowing and LLM-map validator checks: passed
- Semantic tool-sprawl/skill/process index sections route active Chunk 23 cards: passed
- Stale planned routes for authored Chunk 23 shortcuts are absent from indexes and SHORTCUT_REGISTER: passed
- Chunk 23 did not start full shortcut expansion or disallowed topic-card families: passed
- Active Chunk 23 report inventory lists created shortcut cards and updated routing/governance files: passed
- No single index section contains duplicate active Chunk 23 shortcut rows: passed
- No primary index contains multiple full-list sections for the Chunk 23 shortcut-card set: passed
- llms.txt / llms-full.txt active-chunk status phrases are not repeated: passed
- Active Chunk 23 related-topic IDs resolve to active topic cards: passed
- CHANGELOG.md has one current-chunk heading for Chunk 23: passed
- Chunk 23 report/changelog routing claims match routed surfaces and consolidated index state: passed
- Active Chunk 23 machine-claim catalog matches validator checks: passed

## Scope boundary

Chunk 23 did not start full shortcut-card expansion, full tool-card expansion, field-practice-card expansion, pricing expansion, broad workflow expansion, or new narrative chapters.

## Recommended Next Chunk

Recommended next chunk after approval: `chunk_24_multi_ai_model_bias_shortcut_topic_cards`.

## Unresolved questions

None.

<!-- VCB:STOP_RETRIEVAL reason="chunk_23_report_complete" -->
<!-- VCB:END_REPORT id=vcb.chunk_report.chunk_23 -->
AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
