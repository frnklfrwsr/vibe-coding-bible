<!-- VCB:BEGIN_REPORT id=vcb.report.chunk_38 version=0.39.0-draft.chunk38 -->
---
id: vcb.report.chunk_38
title: Chunk 38 Report — Field-Practice Candidate Card Expansion
artifact_type: chunk_report
version: 0.39.0-draft.chunk38
status: waiting_for_editor_review
chunk_id: chunk_38_field_practice_candidate_cards
last_verified: '2026-06-11'
---

# Chunk 38 Report — Field-Practice Candidate Card Expansion

## Scope

Chunk 38 authored bounded field-practice candidate cards from the existing candidate IDs already present in `FIELD_PRACTICES.md`.

In scope:

- candidate field-practice card expansion only;
- conservative evidence labels and field-practice status preservation;
- active card routing for field-practice adoption, evaluation, promotion, local reproduction, and retirement decisions;
- `FIELD_PRACTICES.md` active candidate-card routing;
- README, LLM map, primary semantic index, prompt-library, AI-coach, source-register, manifest, changelog, and validator updates.

Out of scope and not started:

- No new tool cards;
- category placeholder cards;
- No pricing snapshots or pricing expansion;
- shortcut-card expansion;
- broad workflow expansion;
- broad security/secrets expansion;
- narrative chapters;
- promotion of any candidate field practice beyond candidate status.

## Files created

- `CHUNK_38_REPORT.md`
- `topics/field-practices/chatgpt-pm-codex-implementer.md`
- `topics/field-practices/fresh-agent-review.md`
- `topics/field-practices/context-reset-between-tasks.md`
- `topics/field-practices/agents-md-first.md`
- `topics/field-practices/skeleton-todo-first.md`
- `topics/field-practices/strict-typecheck-lint-gates.md`
- `topics/field-practices/greenfield-vs-production-rule.md`
- `topics/field-practices/lessons-file-loop.md`
- `topics/field-practices/multi-agent-review-consensus.md`

## Files updated

- `README.md`
- `manifest.json`
- `llms.txt`
- `llms-full.txt`
- `FIELD_PRACTICES.md`
- `SOURCE_REGISTER.md`
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


## Scope guardrail notes

No new tool cards were created. No pricing snapshots were created. No shortcut cards, workflow expansions, broad security expansions, or narrative chapters were created.

## Authored field-practice candidate cards

- `vcb.field.chatgpt_pm_codex_implementer` — ChatGPT PM, Codex Implementer
- `vcb.field.fresh_agent_review` — Fresh Agent Review
- `vcb.field.context_reset_between_tasks` — Context Reset Between Tasks
- `vcb.field.agents_md_first` — AGENTS.md First
- `vcb.field.skeleton_todo_first` — Skeleton/TODO First
- `vcb.field.strict_typecheck_lint_gates` — Strict Typecheck/Lint Gates
- `vcb.field.greenfield_vs_production_rule` — Greenfield vs Production Rule
- `vcb.field.lessons_file_loop` — Lessons File Loop
- `vcb.field.multi_agent_review_consensus` — Multi-Agent Review Consensus

## Evidence and promotion posture

No field practice was promoted beyond candidate status. The candidate/anecdotal/reproduced/promoted/deprecated taxonomy preserved across cards and register routes.

Every authored Chunk 38 field-practice card is an active retrieval target but keeps:

- `field_practice_status: candidate`;
- `officially_endorsed: 'false'`;
- conservative practice evidence labeling;
- explicit language that official documentation may support surrounding product behavior or engineering principles, but does not prove the community tactic itself;
- monthly review cadence and obsolescence criteria.

Chunk 38 uses selected official OpenAI/Codex source anchors as principle support and source-check context, including Codex best practices, prompting, AGENTS.md, customization, skills, subagents, subagent concepts, Codex overview, and ChatGPT truthfulness guidance. These source anchors do not convert any field practice into official best practice or `E2_REPRODUCED_LOCALLY` evidence.

## Repository routing and governance changes

- `FIELD_PRACTICES.md` now exposes an `## Active Candidate Field Practice Cards` route section for the nine authored candidates while keeping their register status as candidate.
- `README.md` now exposes `## Active Field Practice Candidate Cards` after the active tool-card inventory.
- `llms.txt` and `llms-full.txt` now include field-practice candidate fast routing and active Chunk 38 field-practice card lists.
- Primary semantic indexes now route field-practice adoption, unofficial-practice evaluation, volatile practice review, AI-coach intervention, candidate evidence assessment, and community-tactic overpromotion to active candidate cards before broad chapter/register fallbacks.
- `indexes/PROMPT_LIBRARY.md` now includes field-practice assessment routing and a prompt that asks whether a tactic should be tested, narrowed, promoted locally, or retired.
- `SOURCE_REGISTER.md` records the Chunk 38 editor gate and explains that Chunk 38 reuses/refreshed selected official anchors while preserving candidate/community-reported evidence status.
- `manifest.json` records Chunk 38 scope, canonical package metadata, source inventory, and next-chunk gate state.

## Validator coverage added

`scripts/validate_repository.py` validator coverage tightened for Chunk 38 coverage, including:

- field-practice schema validation via `schemas/field-practice.schema.json`;
- existence and frontmatter checks for all nine active candidate cards;
- `field_practice_status: candidate`, `officially_endorsed: 'false'`, and conservative evidence-level checks;
- rejection of Chunk 38 local-reproduction overclaims;
- `FIELD_PRACTICES.md` active candidate route coverage and register-status preservation;
- README, LLM map, glossary, prompt-library, task, stability, failure-mode, AI-coach, and source-register route checks;
- report inventory coverage;
- package counts and scope guardrails.

## Revision notes

- Repaired `FIELD_PRACTICES.md` candidate-table evidence wording so the current practice evidence uses canonical `E4_COMMUNITY_FIELD_REPORT` labels first.
- Clarified that official documentation supports product mechanics or surrounding principles only; it does not promote candidate rituals to official best practice.
- Removed shorthand, slash-combined, and conditionally promoted evidence phrasing from the candidate routing table.
- Tightened `scripts/validate_repository.py` to reject non-canonical field-practice evidence labels, slash-combined evidence labels, premature E2/E3 promotion wording, and missing current `E4_COMMUNITY_FIELD_REPORT` evidence for the nine Chunk 38 candidate rows.

## Validation

Final validator result:

```text
VCB validation passed
active chapter/topic files validated: 230
shortcut IDs registered: 98
tool IDs registered: 46
pricing snapshots active: 1
```

## Package hygiene

Authoritative package:

```text
vibe-coding-bible-chunk-38-revision-20260611T211500Z-authoritative.zip
```

Package hygiene:

```text
zip entries: 319
unique entries: 319
duplicates: 0
directory-only entries: 0
__pycache__ / .pyc entries: 0
files extracted: 319
```

## Notes for editor

Chunk 38 intentionally treats navigability as part of evidence discipline: the cards are active retrieval targets, but every route labels the practice as candidate and avoids presenting it as official or locally reproduced guidance.

<!-- VCB:STOP_RETRIEVAL reason="chunk_report_complete" -->
<!-- VCB:END_REPORT id=vcb.report.chunk_38 -->

AUTHOR_STATUS: WAITING_FOR_EDITOR_REVIEW
