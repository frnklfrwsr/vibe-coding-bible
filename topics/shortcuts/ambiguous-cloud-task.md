<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.ambiguous_cloud_task version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex guidance plus VCB maintainer synthesis for risk-managed
  parallel, cloud, automation, and GUI/browser shortcut harm reduction
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
id: vcb.shortcut.ambiguous_cloud_task
title: Ambiguous Cloud Task
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex Cloud
- Codex App
- Codex Automations
- Codex CLI non-interactive mode
- Computer Use
- browser/GUI tasks
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- parallel_cloud_automation
- delegation
- automation
- browser_gui
- blast_radius
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: false
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- plan-only first
- explicit acceptance criteria
- forbidden-area list
- small first slice
- review gate before edits
shortcut_profiles:
- vcb.shortcut.ambiguous_cloud_task
durable_principles:
- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
likely_to_change:
- cloud delegation interfaces
- plan/review controls
- task summary and follow-up mechanics
obsolete_when:
- background agents can reliably infer project intent and enforce non-scope boundaries better
  than a human-written brief
related_topics:
- vcb.codex.cloud
- vcb.prompting.acceptance_criteria
- vcb.prompting.plan_first
- vcb.shortcut.context_dumping
- vcb.failure.broad_refactor_drift
- vcb.constraints.scope_budget
---

# Ambiguous Cloud Task

> Summary:
> Ambiguous Cloud Task means delegating vague background work such as “clean this up” or “make it better” before the goal, boundaries, and done criteria are defined.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.ambiguous_cloud_task.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut sends unclear work to the cloud because the agent can “figure it out.” Cloud agents can inspect and propose, but ambiguity makes them choose the scope for you. That is where accidental rewrites, unrelated edits, and summary-driven confidence come from.

### Why it matters

Cloud tasks are less interactive than local pair-work. If the request is vague, the agent may spend many steps on the wrong interpretation before you see the result.

### What good looks like

Good: “First produce a plan with assumptions, target files, risks, and acceptance criteria. Do not edit until I approve the plan.”

### What bad looks like

Bad: “Improve the dashboard and make the code cleaner.”

### Minimal example

If the task is “make onboarding better,” start with a plan that defines the exact user flow, files, states, and verification evidence before any background edits.

### Checklist

- state the user-visible goal
- name target files or areas
- state forbidden areas
- define done-when evidence
- use plan-only mode if the goal is still fuzzy

<!-- VCB:END_SECTION id=vcb.shortcut.ambiguous_cloud_task.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.ambiguous_cloud_task.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach that ambiguity must be resolved before background mutation. If the human cannot describe done, the cloud task should plan, not edit.

### Diagnostic questions

- Can you write one sentence for done?
- Which files or product flow are in scope?
- What should remain unchanged?
- Should Codex ask questions or produce a plan first?
- What output would be reviewable?

### Coaching tactics

- force a plan-only first pass
- ask for assumptions and unknowns
- turn “make it better” into one visible behavior change
- require an explicit non-scope list
- delay cloud mutation until acceptance criteria exist

### Red flags

- prompt uses “clean up,” “improve,” “optimize,” or “make better” without boundaries
- task spans product, design, tests, dependencies, and docs at once
- no acceptance criteria
- no forbidden areas
- human wants to review only the final summary

### Prompt pattern

```text
Before editing, turn this into a bounded cloud delegation brief. List goal, context, target files, forbidden areas, assumptions, unknowns, acceptance criteria, verification commands, and stop conditions. Do not change files until the brief is approved.
```

<!-- VCB:END_SECTION id=vcb.shortcut.ambiguous_cloud_task.ai_coach -->

## Shortcut Reality

### Ideal practice

Resolve ambiguity with a brief or plan-only pass before starting mutating cloud work.

### What people often do instead

They outsource the hard thinking to the background task, then inherit a large diff shaped by the agent’s assumptions.

### When the shortcut may be acceptable

Acceptable as a read-only exploration or plan-generation task, especially when the agent is asked to surface questions rather than edit.

### When it becomes a bad trade

Bad when the vague instruction can mutate user flows, architecture, auth, billing, dependencies, or shared team code.

### Risk profile

- Probability: high whenever the cloud task starts from vague language.
- Impact: medium for prototypes; high for production or shared repos.
- Recoverability: medium if edits stay on a branch; low if the vague task causes broad refactor drift.

### Blast radius

The shortcut can convert one unclear request into many unrelated files, hidden design decisions, weakened tests, and review debt.

### Minimum guardrails

- plan-only first
- explicit acceptance criteria
- forbidden-area list
- small first slice
- review gate before edits

### Recovery plan

1. Stop further edits.
2. Ask for a task reconstruction: assumptions made, files touched, and decisions taken.
3. Compare the diff to the intended goal and revert unrelated changes.
4. Rewrite the brief with a single outcome and smaller scope.
5. Restart as plan-only or one-slice implementation.

## Budget and Constraint Notes

### Cheapest reliable path

Write the smallest task packet, isolation rule, and review packet requirement before launching the agent. This costs less than reconciling a broad or unsafe background result.

### Fastest high-usage path

Fast users should standardize a cloud-delegation brief. It saves more time than cleaning up one vague background branch.

### Low-attention path

Low-attention users should not delegate ambiguous mutation. Use a plan-only task that returns questions and a proposed scope.

### Production-quality path

Production work requires human ownership of sensitive actions, branch/worktree isolation, least privilege, explicit evidence, and rollback or revocation planning.

### Prototype versus production

Prototype shortcuts are acceptable only when the environment, accounts, credentials, and data are fake or disposable. Production shortcuts need hard gates or refusal.

### Maintenance phase

Maintenance should remove stale automations, prune approvals, archive obsolete branches, update task templates, and encode safer defaults when the same shortcut repeats.

## Stable Core

- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
- the minimum guardrail should move the user at least one level up the guardrail ladder

## Volatile Surface

- cloud delegation interfaces
- plan/review controls
- task summary and follow-up mechanics

## Obsolescence Watch

This card should be revised if:

- background agents can reliably infer project intent and enforce non-scope boundaries better than a human-written brief

## Evidence and Sources

- `openai.codex.cloud` — Official OpenAI Codex cloud guidance for delegated background and parallel cloud task shape.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for context, constraints, done-when criteria, planning, validation, and review.
- `openai.codex.cloud_environments` — Official OpenAI Codex cloud-environment guidance for containers, branch checkout, setup, environment variables, secrets, and task loop behavior.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.cloud`
- `vcb.prompting.acceptance_criteria`
- `vcb.prompting.plan_first`
- `vcb.shortcut.context_dumping`
- `vcb.failure.broad_refactor_drift`
- `vcb.constraints.scope_budget`

<!-- VCB:STOP_RETRIEVAL reason="ambiguous_cloud_task_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.ambiguous_cloud_task -->
