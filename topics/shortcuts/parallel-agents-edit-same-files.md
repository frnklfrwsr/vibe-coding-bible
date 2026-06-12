<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.parallel_agents_edit_same_files version=0.25.0-draft.chunk24 -->
---
version: 0.25.0-draft.chunk24
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI/Codex guidance on prompting, best practices, subagents, model/current-source volatility, and truthfulness/hallucination caveats; VCB maintainer synthesis for multi-AI, answer-selection, model-bias, estimate, and integration harm reduction
budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget
cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- production_quality
- disposable_prototype
project_phases:
- prototype
- mvp
- production_build
- maintenance
- major_refactor
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.shortcut.parallel_agents_edit_same_files
title: Parallel Agents Editing the Same Files
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- parallel agents
- cloud tasks
- worktrees
- same-file edits
- integration
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- multi_ai
- parallel_agents
- file_ownership
- integration
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: HIGH_RISK_SHORTCUT
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- file-ownership map
- no overlapping write scopes
- one integrator
- post-merge tests and diff review
shortcut_profiles:
- vcb.shortcut.parallel_agents_edit_same_files
durable_principles:
- parallelism needs ownership
- semantic conflicts are worse than textual conflicts
- integration is its own task
likely_to_change:
- subagent orchestration UX
- worktree automation behavior
- agent thread visibility
obsolete_when:
- agent platforms enforce path-level write locks, semantic conflict checks, and post-merge verification automatically
related_topics:
- vcb.codex.subagents
- vcb.codex.cloud
- vcb.workflow.reviewing_diffs
- vcb.constraints.scope_budget
- vcb.shortcut.many_ais_same_files
---

# Parallel Agents Editing the Same Files

> Summary:
> This shortcut is letting multiple agents mutate overlapping files at the same time and hoping the merge will be obvious later.

## Quick Navigation

- 1. For the Human: Plain-Language Concept
- 2. For the AI Coach: How to Teach This to Your Human
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.parallel_agents_edit_same_files.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Parallel agents are not a problem by themselves. The shortcut is giving two or more write-capable agents overlapping file ownership.

### Why it matters

Two agents can each produce internally coherent patches that are mutually incompatible. The merge conflict is only the visible part; the worse risk is semantic conflict that passes a shallow check.

### What good looks like

Good: “Split by non-overlapping boundaries, such as frontend component review versus backend contract review, or keep one agent read-only.”

### What bad looks like

Bad: “Tell one agent to refactor a component and another to add behavior to that same component, then accept whichever patch lands last.”

### Minimal example

Agent A may edit `src/billing/*`; Agent B may inspect but not edit those files. Agent B may edit only docs or tests after Agent A finishes.

### Checklist

- define file ownership before agents start
- forbid overlapping write scopes
- use separate branches/worktrees
- merge through one integrator
- rerun checks after integration

<!-- VCB:END_SECTION id=vcb.shortcut.parallel_agents_edit_same_files.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.parallel_agents_edit_same_files.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that parallelism needs boundaries, not just enthusiasm.

### Diagnostic questions

- Which files can each agent edit?
- What files are shared or forbidden?
- Can the agents run in separate worktrees?
- What check proves the integrated result?

### Coaching tactics

- draw a file-ownership map
- make write access opt-in by path
- turn ambiguous agents into reviewers
- merge one branch at a time

### Red flags

- agents are both told “fix whatever you see”
- same component appears in multiple task briefs
- conflict resolution happens by copy-paste
- checks run before integration but not after

### Prompt pattern

```text
Before spawning agents, produce a file-ownership plan. Each agent must have allowed files, forbidden files, output format, and whether it is read-only or write-capable. Reject overlapping write ownership unless one agent is the integrator.
```

<!-- VCB:END_SECTION id=vcb.shortcut.parallel_agents_edit_same_files.ai_coach -->

## Shortcut Reality

### Ideal practice

Parallel agents operate on disjoint scopes, or only one agent mutates while others produce evidence-backed review.

### What people often do instead

People ask several agents to “take a pass” at the same area because parallel work feels faster.

### When the shortcut may be acceptable

Acceptable when all but one agent are read-only, or when branches are isolated and one integrator reviews the merged diff.

### When it becomes a bad trade

Bad when two agents can change the same files, schema, API contract, tests, or dependency lockfile without a strict integrator.

### Risk profile

- Probability: medium/high when subagents or cloud tasks are easy to start.
- Impact: high for semantic conflicts and hidden regressions.
- Recoverability: medium with isolated branches; low if patches are pasted together.

### Blast radius

The blast radius includes each overlapping file plus any contracts, tests, imports, or generated artifacts touched by either agent.

### Minimum guardrails

- file-ownership map
- no overlapping write scopes
- one integrator
- post-merge tests and diff review

### Recovery plan

- Freeze all parallel runs.
- Create a touched-file matrix.
- Choose a canonical branch.
- Revert or isolate conflicting edits.
- Integrate one change at a time with checks after each merge.

## Budget and Constraint Notes

### Cheapest reliable path

Use one AI/tool/agent first, require one evidence packet, and spend the smallest amount of model usage needed to inspect the actual project before accepting or comparing answers.

### Fastest high-usage path

High-throughput users can run parallel analysis, but only with role separation, read-only reviewers where possible, explicit output schemas, and one final integration gate.

### Low-attention path

Low-attention delegation should default to report-only or read-only work. Do not let many agents, model guesses, or consensus summaries mutate code before a human reviews evidence.

### Production-quality path

Production-quality use requires current-source checks for volatile product/model facts, file-level evidence, changed-file review, tests or checks, rollback, and a record of why one AI answer was accepted over alternatives.

### Prototype versus production

A disposable prototype may use rough model choice, loose estimates, or multiple brainstormed answers. Persistent or production-bound work needs evidence, one owner, and guardrails before mutation.

### Maintenance phase

In maintenance, multi-AI shortcuts compound because stale assumptions survive across docs, config, prompts, and team habits. Revisit role boundaries, model-routing advice, and answer-selection rubrics after repeated failures or phase changes.

## Stable Core

- parallelism needs ownership
- semantic conflicts are worse than textual conflicts
- integration is its own task

## Volatile Surface

- subagent orchestration UX
- worktree automation behavior
- agent thread visibility

## Obsolescence Watch

This card should be revised if:

- agent platforms enforce path-level write locks, semantic conflict checks, and post-merge verification automatically

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for task context, constraints, done-when criteria, plan-first work, review, and verification.
- `openai.codex.subagents` — Official OpenAI Codex guidance for subagent workflows, parallel agents, orchestration, sandbox inheritance, and token-use caveats.
- `openai.codex.subagent_concepts` — Official OpenAI Codex concept guidance for context pollution, context rot, parallel analysis, and write-heavy workflow cautions.
- `openai.codex.models` — Official OpenAI Codex model source for volatile model-availability and model-configuration watchlist routing.
- `openai.help.truthfulness` — Official OpenAI Help Center truthfulness caveat for treating fluent answers as fallible and requiring verification.
- `openai.hallucinations` — Official OpenAI hallucination explainer for confident wrong-answer and guessing-incentive framing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, evidence, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.subagents`
- `vcb.codex.cloud`
- `vcb.workflow.reviewing_diffs`
- `vcb.constraints.scope_budget`
- `vcb.shortcut.many_ais_same_files`

<!-- VCB:STOP_RETRIEVAL reason="parallel-agents-edit-same-files_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.parallel_agents_edit_same_files -->
