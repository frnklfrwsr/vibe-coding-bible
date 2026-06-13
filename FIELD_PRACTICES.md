---
id: vcb.register.field_practices
title: FIELD_PRACTICES
artifact_type: register
version: 1.0.1-post-release.issue23
status: issue_23_usage_insight_triage
created_on: 2026-06-08
last_verified: '2026-06-12'
next_review_due: '2026-07-12'
review_cadence: monthly
---

<!-- VCB:BEGIN_REGISTER id=vcb.register.field_practices version=1.0.1-post-release.issue23 -->

# FIELD_PRACTICES

**Purpose:** Track unofficial, user-discovered, practitioner-reported, or locally reproduced Codex practices without presenting them as official best practice.

## Field Practice Policy

- Official docs win for product behavior.
- Local repo tests win for local truth.
- Community wisdom is allowed only when labeled.
- Speculation must have an obsolescence trigger.
- Model-specific claims require review dates.
- A field practice can be useful before it is official, but it must not be promoted to stable guidance without evidence.

## Status Labels

| Status | Meaning |
|---|---|
| candidate | Useful enough to keep as an active retrieval target, but not yet reproduced or promoted. |
| needs_more_evidence | Plausible but too broad, risky, or under-evidenced for local reproduction or promotion. |
| reproduced | Tested by maintainers in a bounded repo/workflow; can use E2_REPRODUCED_LOCALLY with stated limits. |
| promoted | Promoted into stable guidance only when the exact claim is backed by E0_OFFICIAL_DOCS, E2_REPRODUCED_LOCALLY evidence, or strong E3_EXPERT_REPORT support. |
| deferred | Intentionally left for later evidence collection or project-fit testing. |
| retired | No longer recommended; retained only with replacement and reason. |
| anecdotal | Legacy label for community reports only; treat as E4_COMMUNITY_FIELD_REPORT unless independently verified. |
| deprecated | Legacy label; prefer `retired` for Issue #7 and later audits. |

## Promotion Rules

A field practice may move up the ladder only when one of these is true:

1. It is supported by E0_OFFICIAL_DOCS for the exact documented behavior.
2. It is reproduced locally in a controlled repo and labeled E2_REPRODUCED_LOCALLY with stated limits.
3. It is supported by a named expert/practitioner and labeled E3_EXPERT_REPORT only when the expert source supports the exact practice.
4. It has multiple independent community reports and remains E4_COMMUNITY_FIELD_REPORT until tested or otherwise promoted by qualifying evidence.

## Candidate Field Practice Routing Table

This table preserves the original candidate-card set while recording the live Issue #7 status in `Current register status`; post-release Issue #23 adds one additional live candidate route.

| Field practice ID | Planned file | Claim | Durable principle | Evidence starting status | Current register status | Promotion path | Review trigger |
|---|---|---|---|---|---|---|---|
| `vcb.field.chatgpt_pm_codex_implementer` | `topics/field-practices/chatgpt-pm-codex-implementer.md` | Use ChatGPT for product/PM thinking and Codex for repo-aware implementation. | Separate planning, implementation, and verification. | E4_COMMUNITY_FIELD_REPORT; official docs support product mechanics/principles only, not this split workflow | needs_more_evidence | requires bounded local reproduction or multiple independent reports | Codex gains stronger native PM/task-decomposition workflow. |
| `vcb.field.fresh_agent_review` | `topics/field-practices/fresh-agent-review.md` | Ask a fresh session/agent to review a diff before commit. | Independent review catches different mistakes. | E2_REPRODUCED_LOCALLY in bounded VCB PR-review workflow; E0_OFFICIAL_DOCS supports GitHub review mechanics only | reproduced | promotable only after repeated local reproductions or named-practitioner support | Native review surfaces become reliable enough to replace manual fresh review. |
| `vcb.field.context_reset_between_tasks` | `topics/field-practices/context-reset-between-tasks.md` | Reset or summarize context between unrelated tasks. | Context hygiene reduces stale assumptions. | E4_COMMUNITY_FIELD_REPORT; official docs support context/product mechanics only | candidate | promotable after local fit check and repeatable reduction in stale-context failures | Context compaction/retrieval becomes robust and transparent. |
| `vcb.field.agents_md_first` | `topics/field-practices/agents-md-first.md` | Add minimal `AGENTS.md` early in durable repos. | Persistent project context reduces repeated instructions. | E4_COMMUNITY_FIELD_REPORT for the ritual; E0_OFFICIAL_DOCS supports AGENTS.md mechanics and principle only | candidate | promotable after local fit check | Official discovery/loading behavior changes. |
| `vcb.field.skeleton_todo_first` | `topics/field-practices/skeleton-todo-first.md` | Human sketches skeleton/TODOs before Codex fills implementation. | Constrain solution shape before implementation. | E4_COMMUNITY_FIELD_REPORT; no bounded local reproduction in this audit | candidate | promotable after local reproduction in comparable project type | Codex planning/scaffolding improves enough to make manual stubbing less useful. |
| `vcb.field.strict_typecheck_lint_gates` | `topics/field-practices/strict-typecheck-lint-gates.md` | Enforce typecheck/lint/test gates after agent changes. | Machine-verifiable constraints reduce uncertainty. | E2_REPRODUCED_LOCALLY for VCB validator gate; official vendor docs support check mechanics only | reproduced | promotable after repeated non-noisy gate evidence across comparable repos | Project toolchain changes or checks become flaky/noisy. |
| `vcb.field.greenfield_vs_production_rule` | `topics/field-practices/greenfield-vs-production-rule.md` | Tell Codex whether backward compatibility matters. | Project phase changes implementation choices. | E4_COMMUNITY_FIELD_REPORT; official docs support prompt constraints/principles only | candidate | promotable after local reproduction or named-practitioner support | Model reliably infers compatibility needs from repo context. |
| `vcb.field.lessons_file_loop` | `topics/field-practices/lessons-file-loop.md` | Capture repeated corrections in a lessons file or durable guidance. | Repeated mistakes should become persistent instructions. | E4_COMMUNITY_FIELD_REPORT for the ritual; E0_OFFICIAL_DOCS supports durable-guidance mechanisms only | candidate | promotable after local fit check | Memories/AGENTS/skills make separate lessons files obsolete. |
| `vcb.field.multi_agent_review_consensus` | `topics/field-practices/multi-agent-review-consensus.md` | Use multiple agents for independent review/analysis. | Independent perspectives can reduce blind spots. | E4_COMMUNITY_FIELD_REPORT for the ritual; official subagent/review docs support mechanics only, not consensus reliability | needs_more_evidence | requires controlled comparison against single-review baseline | Parallel-agent review becomes natively scored/deduplicated. |
| `vcb.field.contract_first_segmented_handoffs` | `topics/field-practices/contract-first-segmented-handoffs.md` | Give Codex one reconciled segment contract instead of unreconciled research notes. | Resolve implementation ambiguity before repository mutation. | E4_COMMUNITY_FIELD_REPORT from one sanitized public usage insight; official docs support adjacent mechanics/principles only | candidate | requires bounded local reproduction or multiple independent reports | Codex reliably reconciles contracts, tests, and review threads without explicit segmented packages. |


## Active Field Practice Cards After Issue #7 and Issue #23

Issue #7 reviewed the original nine active field-practice retrieval cards. Issue #23 adds one sanitized usage-insight candidate. None are official best practice and none are promoted. Current live status: 2 reproduced with bounded local evidence, 6 candidate, 2 needs_more_evidence, 0 promoted, 0 deferred, 0 retired.

- `vcb.field.chatgpt_pm_codex_implementer` - `topics/field-practices/chatgpt-pm-codex-implementer.md` - active needs_more_evidence: ChatGPT PM / Codex implementer split remains too broad for bounded local reproduction.
- `vcb.field.fresh_agent_review` - `topics/field-practices/fresh-agent-review.md` - active reproduced: bounded local reproduction through PR review gate; not promoted as universal proof.
- `vcb.field.context_reset_between_tasks` - `topics/field-practices/context-reset-between-tasks.md` - active candidate: reset or summarize context between unrelated tasks.
- `vcb.field.agents_md_first` - `topics/field-practices/agents-md-first.md` - active candidate: minimal AGENTS.md early in durable repos.
- `vcb.field.skeleton_todo_first` - `topics/field-practices/skeleton-todo-first.md` - active candidate: human skeleton/TODOs before agent implementation.
- `vcb.field.strict_typecheck_lint_gates` - `topics/field-practices/strict-typecheck-lint-gates.md` - active reproduced: bounded local reproduction through VCB validator gate; not promoted as universal proof.
- `vcb.field.greenfield_vs_production_rule` - `topics/field-practices/greenfield-vs-production-rule.md` - active candidate: explicit project phase and compatibility posture.
- `vcb.field.lessons_file_loop` - `topics/field-practices/lessons-file-loop.md` - active candidate: temporary lessons loop before durable guidance promotion.
- `vcb.field.multi_agent_review_consensus` - `topics/field-practices/multi-agent-review-consensus.md` - active needs_more_evidence: multi-agent review must not treat agreement as proof.
- `vcb.field.contract_first_segmented_handoffs` - `topics/field-practices/contract-first-segmented-handoffs.md` - active candidate: contract-first segmented Codex handoffs based on one sanitized usage insight.

## Issue #7 Status Audit Note

- `reproduced` means bounded local reproduction only; it is not official endorsement or general proof.
- `candidate` means useful enough to keep as an active retrieval target with guardrails.
- `needs_more_evidence` means the exact ritual needs controlled local testing or stronger independent reports before adoption as a rule.

## Field-Practice Evaluation Prompt

```text
Evaluate this field practice before adoption.

Practice:
Source type:
Project risk:
Expected benefit:
What could go wrong:
How to test safely:
Promotion rule:
Obsolescence trigger:
```

## Non-Promotion Rule

Do not put a field practice into `AGENTS.md`, config, skills, hooks, CI, or a stable workflow chapter until it has a clear evidence label, risk profile, and local fit.


## Chunk 42 Release-Candidate Disposition Note

Chunk 42 does not add, promote, reproduce, retire, or deprecate field practices. It confirms the release-candidate disposition: all 9 active field-practice retrieval cards remain `candidate` and `E4_COMMUNITY_FIELD_REPORT`; candidate-only status is a documented release limitation, not a hidden blocker, as long as no practice is presented as official, reproduced, promoted, retired, or deprecated without later evidence review. Issue #7 is that later evidence review and updates live source statuses without mutating the historical Final Release 1 package record.

## Chunk 41 Finalization Readiness Audit Note

Chunk 41 does not add, promote, reproduce, retire, or deprecate field practices. All 9 active field-practice retrieval cards remain `candidate`; their current practice evidence remains `E4_COMMUNITY_FIELD_REPORT` unless a future controlled reproduction or qualifying expert/community evidence review changes that status.

<!-- VCB:STOP_RETRIEVAL reason="field_practices_register_complete" -->
<!-- VCB:END_REGISTER id=vcb.register.field_practices -->
