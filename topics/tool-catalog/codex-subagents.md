<!-- VCB:BEGIN_TOPIC id=tool.codex_subagents version=0.1.0 -->
---
version: 0.1.0
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
evidence_scope: official OpenAI/Codex tool documentation plus VCB maintainer synthesis for
  setup, risk, budget, and coaching guidance
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
type: tool_card
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
id: tool.codex_subagents
title: Codex Subagents
name: Codex Subagents
category: codex_parallel_agents
setup_effort: 'medium: requires clear subtask boundaries, role prompts, synthesis criteria,
  and review expectations'
maintenance_effort: 'medium: subagent patterns need pruning as project risks and model behavior
  change'
debugging_effort: 'medium to high: failures may be hidden in subagent scope, stale context,
  synthesis bias, or conflicting recommendations'
lock_in_risk: 'moderate: subagent orchestration and custom-agent behavior are Codex-specific
  workflow conventions'
hidden_cost_risk: 'high: parallel reasoning can burn usage and attention faster than a focused
  single-thread review'
codex_integration_value: strong for bounded parallel thinking when the main agent remains
  the integrator and reviewer
best_for:
- parallel codebase exploration
- specialist review passes
- large context distillation
- bounded independent implementation slices
not_for:
- one tiny task that a single thread can solve
- uncoordinated edits to the same files
- delegating final product judgment
- using agreement as correctness without verification
integrates_with_codex:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- custom agent instructions
hidden_costs:
- more prompts and context packets
- synthesis review time
- duplicated exploration
- false confidence from multiple similar answers
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
shortcut_profiles:
- vcb.shortcut.subagent_swarm
- vcb.shortcut.consensus_as_correctness
- vcb.shortcut.parallel_agents_edit_same_files
- vcb.shortcut.best_of_n_without_review
durable_principles:
- Parallel agents need independent scopes and a single integration point.
- Subagent findings are evidence candidates, not final truth.
- More agents increase coordination and review cost.
likely_to_change:
- subagent configuration, supported surfaces, model-routing options, custom-agent mechanics,
  and UI labels
obsolete_when:
- OpenAI removes subagent workflows or replaces them with a materially different parallel-agent
  orchestration model.
related_topics:
- tool.codex
- tool.codex_cloud
- vcb.codex.subagents
- vcb.shortcut.subagent_swarm
- vcb.shortcut.consensus_as_correctness
- vcb.failure.context_pollution
---

# Codex Subagents

> Summary:
> Codex Subagents split bounded analysis or implementation work across specialized agents, then return synthesized findings to the main thread.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_subagents.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex Subagents are a parallel-agent control surface. The main thread can delegate bounded concerns to specialist agents and then collect their results instead of stuffing every concern into one context.

### Why it matters

Subagents matter when a task has separable questions: tests, security, performance, docs, architecture, migration risk, or codebase exploration. They are not a replacement for a deciding owner.

### What good looks like

Use subagents for independent analysis, codebase exploration, review passes, or disjoint implementation slices with explicit ownership and a synthesis step.

### What bad looks like

Do not create a swarm of agents with overlapping write authority and then accept the combined answer because it sounds comprehensive.

### Minimal example

Ask one subagent to inspect tests, one to inspect security-sensitive paths, and one to inspect migration risk. The main thread should merge the findings, cite evidence, and choose next action.

### Best-fit cases

- parallel codebase exploration
- specialist review passes
- large context distillation
- bounded independent implementation slices

### Not-fit cases

- one tiny task that a single thread can solve
- uncoordinated edits to the same files
- delegating final product judgment
- using agreement as correctness without verification

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: requires clear subtask boundaries, role prompts, synthesis criteria, and review expectations |
| Maintenance effort | medium: subagent patterns need pruning as project risks and model behavior change |
| Debugging effort | medium to high: failures may be hidden in subagent scope, stale context, synthesis bias, or conflicting recommendations |
| Lock-in risk | moderate: subagent orchestration and custom-agent behavior are Codex-specific workflow conventions |
| Hidden cost risk | high: parallel reasoning can burn usage and attention faster than a focused single-thread review |

### Checklist

- choose this adjunct surface only when the task shape requires it
- write the task boundary, allowed actions, and forbidden zones before use
- prefer read-only or report-only output until the workflow is proven
- require evidence before accepting a summary
- check official OpenAI docs for current mechanics before relying on product behavior

<!-- VCB:END_SECTION id=tool.codex_subagents.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_subagents.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach this as an adjunct control surface, not a generic productivity boost. The primary lesson is: pick the smallest surface that fits, isolate risk, and demand evidence.

### Diagnostic questions

- What primary Codex surface is this adjunct attached to?
- Is the task read-only, mutating, recurring, parallel, browser-based, or GUI-based?
- What permission boundary prevents the wrong files, windows, sites, or accounts from being touched?
- What artifact proves success: diff, report, screenshot with repro, test output, or review note?
- What must stop the run immediately?

### Coaching tactics

- route surface-choice questions through `tool.codex` first, then this adjunct card if relevant
- translate vague delegation into a task packet with scope, allowed actions, and done-when evidence
- keep product mechanics, UI labels, current feature availability, and pricing in volatile-source review
- pair every shortcut warning with the smallest reliable guardrail
- require human review when secrets, account authority, production state, or persistent data are involved

### Prompt pattern

```text
Use subagents only for independent concerns. Assign each subagent one bounded question, require cited repo evidence, and have the main thread merge findings into one decision with risks and verification steps.
```

### Red flags

- the human asks for many agents before defining the problem
- all subagents receive the same vague instruction
- subagents are allowed to edit the same files
- agreement is treated as proof

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_subagents.ai_coach -->

## Shortcut Reality

### The ideal practice

Use this tool only after the task, context, permission boundary, evidence requirement, and review owner are clear.

### What users often do instead

Users often reach for the powerful adjunct surface because it feels faster, then discover that parallelism, browser state, GUI control, or recurrence has multiplied the review problem.

### When the shortcut may be acceptable

The shortcut can be acceptable for read-only inspection, disposable prototypes, isolated worktrees, report-only automation, local visual checks, or account-safe flows where rollback is trivial and no sensitive state is exposed.

### When it becomes a bad trade

It becomes a bad trade when the surface can mutate broad code, touch signed-in accounts, hide environment assumptions, operate sensitive apps, run repeatedly, or produce polished summaries without artifacts.

### Relevant shortcut cards

- `vcb.shortcut.subagent_swarm`
- `vcb.shortcut.consensus_as_correctness`
- `vcb.shortcut.parallel_agents_edit_same_files`
- `vcb.shortcut.best_of_n_without_review`

### Minimum guardrails

- one bounded task per run/thread/automation
- explicit allowed actions and forbidden zones
- isolation through branch, worktree, sandbox, account boundary, or read-only mode where possible
- evidence packet before acceptance
- human review before merge, deploy, account action, credential use, or production action

### Recovery plan

Stop the run, preserve the transcript and generated artifacts, inspect diffs or account actions, revert unsafe changes, rotate exposed secrets if needed, remove broad approvals, and restart with a narrower task packet.

## Budget and Constraint Notes

### Cheapest reliable path

Use the narrowest Codex surface and the smallest context packet that can produce reviewable evidence. Avoid parallel, recurring, browser, or GUI control until a simpler surface fails.

### Fastest high-usage path

Use this adjunct surface only when independence, isolation, and review capacity are already planned. Otherwise it creates speed theater: more activity with less confidence.

### Low-attention path

Low-attention use requires isolation, stop conditions, and report-only or review-later output. Low attention does not justify broad mutation, signed-in account action, or production access.

### Production-quality path

Production use requires least privilege, explicit scope, checks, security review where relevant, and human acceptance based on artifacts rather than summaries.

### Hidden costs to watch

- context rot across parallel reports
- model-bias convergence
- unreviewed synthesis errors

## Stable Core

- Parallel agents need independent scopes and a single integration point.
- Subagent findings are evidence candidates, not final truth.
- More agents increase coordination and review cost.

## Volatile Surface

- subagent configuration, supported surfaces, model-routing options, custom-agent mechanics, and UI labels

Exact prices, plan packaging, usage-credit quantities, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI removes subagent workflows or replaces them with a materially different parallel-agent orchestration model.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.subagents` — official/synthesis source anchor for this tool card.
- `openai.codex.subagent_concepts` — official/synthesis source anchor for this tool card.
- `openai.codex.best_practices` — official/synthesis source anchor for this tool card.
- `openai.codex.customization` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex`
- `tool.codex_cloud`
- `vcb.codex.subagents`
- `vcb.shortcut.subagent_swarm`
- `vcb.shortcut.consensus_as_correctness`
- `vcb.failure.context_pollution`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_subagents -->
