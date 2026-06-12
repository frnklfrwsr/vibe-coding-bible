<!-- VCB:BEGIN_TOPIC id=vcb.constraints.recovery_budget version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
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
evidence_scope: official Codex guidance on prompts, constraints, usage/pricing volatility,
  sandboxed execution, and VCB maintainer synthesis for budget-aware operating constraints
budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget
cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- unattended_high_throughput
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
id: vcb.constraints.recovery_budget
title: Recovery Budget
type: concept
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Git branches
- Codex App
- Codex CLI
- refactoring
- data changes
- production work
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.coding_on_main
- vcb.shortcut.broad_refactor
- vcb.shortcut.unattended_mutation
durable_principles:
- constraints are design inputs, not excuses to skip evidence
- task shape should determine Codex surface, permission, review, and verification
  level
- budget decisions should account for usage, attention, recovery, and maintenance
  cost
likely_to_change:
- current Codex worktree/revert UI
- Git integration behavior in product surfaces
- platform-specific rollback tooling
obsolete_when:
- Every Codex change is automatically isolated, reversible, testable, and semantically
  rolled back with reliable safety guarantees.
related_topics:
- vcb.concepts.recoverability
- vcb.concepts.rollback
- vcb.workflow.reviewing_diffs
- vcb.failure.broad_refactor_drift
- vcb.constraints.operating_mode
aliases:
- recoverability constraint
---

# Recovery Budget

<!-- VCB:BEGIN_SECTION id=vcb.constraints.recovery_budget.structure_notice -->
> This is an atomic constraint/budget card. Prefer it over broad budget chapters when the user needs to choose an operating constraint, budget posture, or Codex delegation level for one concrete task.
<!-- VCB:END_SECTION id=vcb.constraints.recovery_budget.structure_notice -->

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

<!-- VCB:BEGIN_SECTION id=vcb.constraints.recovery_budget.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Recovery budget is the time, expertise, rollback path, and confidence you have available to recover from a bad Codex change.

### Why it matters

Fast work is only cheap when rollback is cheap. A risky change without a recovery path is not a shortcut; it is debt with interest.

### What good looks like

Good: “Make this change on a branch, keep the diff under five files, avoid migrations, and include rollback steps.”

### What bad looks like

Bad: letting Codex rewrite config, migrations, auth, and UI together with no checkpoint and no revert plan.

### Minimal example

Ask Codex: “Before editing, estimate recovery cost. Identify rollback path, data risk, files touched, migration risk, and the smallest reversible slice. If recovery is hard, reduce scope.”

### Checklist

- Name the constraint before asking Codex to act.
- Pick the smallest useful task slice.
- Decide whether the work is read-only, write-capable, or blocked until approval.
- Define what evidence must exist before the work counts as done.
- Check whether the recovery path is cheaper than another round of planning.
- Do not quote exact prices, limits, or credits from memory; use the dated pricing snapshot or current official source.

<!-- VCB:END_SECTION id=vcb.constraints.recovery_budget.human -->

<!-- VCB:BEGIN_SECTION id=vcb.constraints.recovery_budget.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Coaching stance

Teach the human to treat constraints as workflow inputs. The answer is not “use more AI” or “use less AI.” The answer is to match Codex surface, task size, permission, attention, and verification to the actual constraint.

### Diagnostic questions

- What is the limiting resource: money, usage, time, attention, review skill, recovery path, or production risk?
- Is the task exploratory, implementation-heavy, review-heavy, or release-critical?
- What is the blast radius if Codex changes the wrong thing?
- What evidence would make acceptance cheap?
- What exact product fact or pricing fact must be checked against current official sources?

### Coaching tactics

- Convert vague budget anxiety into a task budget: context budget, edit budget, review budget, and recovery budget.
- Ask for a plan-only pass before permitting edits when constraints are tight.
- Use read-only investigation for low-attention or high-uncertainty work.
- Require an explicit “not checked” line in completion summaries.
- Move exact pricing, limits, credits, and feature availability to snapshots or official-source checks.

### Red flags

- The human wants high throughput but has no review bandwidth.
- The human wants cheapest possible but keeps using vague prompts and retries.
- The task touches production, auth, billing, data, or dependencies with no recovery plan.
- The answer assumes a specific Codex limit or model route without checking current official docs.
- A broad task is justified only by “I do not have time to review.”

### Prompt pattern

```text
Before editing, estimate recovery cost. Identify rollback path, data risk, files touched, migration risk, and the smallest reversible slice. If recovery is hard, reduce scope.
Return:
1. recommended Codex surface and permission level
2. task slice
3. human attention needed
4. expected usage/retry risk without exact prices
5. required evidence
6. recovery plan
7. what should stay out of scope
```

<!-- VCB:END_SECTION id=vcb.constraints.recovery_budget.ai_coach -->

## Shortcut Reality

### Ideal practice

Choose the Codex workflow from the constraint first, then ask Codex to work inside that boundary.

### What people often do instead

They pick a tool, model, plan, or automation mode by habit, then try to force every task through it.

### When the shortcut may be acceptable

A looser constraint choice may be acceptable for disposable prototypes, throwaway experiments, small local cleanup, or read-only investigation where rollback is trivial and no real secrets, users, money, or production state are involved.

### When it becomes a bad trade

It is a bad trade when the shortcut hides the real cost: review debt, usage burn, merge conflict recovery, production rollback, security exposure, or maintenance work.

### Risk profile

- Probability: medium when prompts omit constraints; high when the task is broad or unattended.
- Impact: low for throwaway demos; high for production, dependencies, auth, data, CI, or team workflows.
- Recoverability: good with small branches and explicit evidence; poor with broad edits, shared state, or missing rollback.

### Blast radius

A poor constraint decision can spread across code, docs, tests, dependencies, CI, release notes, and future prompts that inherit the wrong assumption.

### Minimum guardrails

- Declare the constraint in the prompt.
- Use branches or worktrees for write work.
- Prefer read-only investigation when attention or recovery budget is low.
- Require evidence before accepting done claims.
- Check current official pricing/limits when economics matter.

### Recovery plan

1. Stop expanding the task.
2. Ask Codex to summarize changed files, assumptions, checks, and missing evidence.
3. Reduce the task to the smallest reversible slice.
4. Run the cheapest relevant verification.
5. Revert, isolate, or re-plan if the work exceeds the constraint.

## Budget and Constraint Notes

### Cheapest reliable path

The cheapest reliable path is the one you can undo. Recovery cost should be estimated before throughput is increased. The cheap path is not “skip checks”; it is “pay only for the context, edits, and verification that prove the current slice.”

### Fastest high-usage path

Use higher throughput only after task boundaries, file ownership, and review evidence are clear. More runs are useful when they are independent; they are waste when they create conflicting diffs or duplicate analysis.

### Low-attention path

Low-attention work should be read-only, narrowly scoped, or isolated. If Codex can edit while the human is unavailable, the task needs stronger guardrails and a clear evidence report.

### Production-quality path

Production work needs explicit acceptance criteria, diff review, verification, security/data review where relevant, and rollback notes. Do not treat model confidence as a production gate.

### Prototype versus production

Prototype: trade polish for learning, but keep fake data and easy rollback. Production: trade speed for evidence, traceability, and recovery.

### Maintenance phase

In maintenance, constraint mistakes compound because future work inherits them. Prefer small diffs, lower surprise, documented decisions, and durable guidance updates over one-off speed.

## Stable Core

- Constraints should be named before Codex acts.
- Smaller scopes reduce usage burn, review cost, and recovery cost.
- Evidence is the bridge between fast AI output and trustworthy engineering work.
- Exact pricing, plan packaging, and limits are volatile and belong in snapshots or source checks.
- Recovery budget is part of cost, not an afterthought.

## Volatile Surface

- Codex plan packaging, usage limits, credit behavior, feature availability, model routing, speed modes, and dashboards can change.
- Product UI names for surfaces, permissions, review panes, cloud tasks, and automation settings can change.
- Official guidance on usage optimization and model selection can change.
- Organization policies, admin controls, and data controls can change.

## Obsolescence Watch

Re-check this card if Codex changes its pricing model, usage-limit system, plan packaging, operating surfaces, automation permission model, or official budget-optimization guidance.

## Evidence and Sources

- `openai.codex.best_practices` — official guidance for prompt context, constraints, done-when criteria, planning, and reusable guidance.
- `openai.codex.pricing` — official volatile pricing and usage source; exact values belong in dated pricing snapshots, not stable card prose.
- `openai.help.codex_chatgpt_plan` — official Help Center guidance that Codex usage varies by plan, task size, complexity, and execution surface.
- `openai.codex.noninteractive` — official guidance for `codex exec`, scripts/CI, read-only defaults, explicit sandbox settings, and structured output.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for constraint-aware task shaping, blast-radius control, and recovery budgeting.

## Related Topics

- `vcb.concepts.recoverability`
- `vcb.concepts.rollback`
- `vcb.workflow.reviewing_diffs`
- `vcb.failure.broad_refactor_drift`
- `vcb.constraints.operating_mode`

<!-- VCB:STOP_RETRIEVAL reason="constraint_budget_card_complete" -->
<!-- VCB:END_TOPIC id=vcb.constraints.recovery_budget -->
