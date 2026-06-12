<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.skipping_plan version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-12'
last_reviewed: '2026-06-12'
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
evidence_scope: official OpenAI/Codex prompting and workflow guidance plus VCB maintainer synthesis for risk-managed shortcut harm reduction
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
id: vcb.shortcut.skipping_plan
title: Skipping Plan
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-12'
applies_to:
- planning
- Codex App
- Codex CLI
- Codex IDE
- Codex Cloud
- risky changes
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- planning
- scope
- risk control
risk_level:
  prototype: LOW_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- ask for likely files
- name risky areas
- define checks
- define rollback
shortcut_profiles:
- vcb.shortcut.skipping_plan
durable_principles:
- planning is cheapest before edits exist
- bigger blast radius needs a plan gate
- plan detail should scale with risk, not with ceremony
likely_to_change:
- current Codex planning UI affordances
- surface-specific plan mode behavior
- project-specific verification commands
obsolete_when:
- agents can safely infer scope, risk, checks, and rollback before mutation without explicit user framing
related_topics:
- vcb.prompting.plan_first
- vcb.workflow.feature_slicing
- vcb.workflow.unknown_codebase
- vcb.constraints.scope_budget
- vcb.constraints.recovery_budget
- vcb.chapter.plan_first_code_second
---

# Skipping Plan

> Summary:
> Skipping plan is asking Codex to start changing code before the likely files, risks, checks, and rollback path are named.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skipping_plan.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Skipping plan means you ask Codex to edit first and figure out the route while it is already moving. It feels fast because the first diff appears sooner.

### Why it matters

The dangerous part is hidden scope. Without a short plan, Codex may touch the wrong files, skip the nearest check, mix cleanup with behavior change, or create a diff that is harder to review than the original problem.

### What good looks like

Good: "Before editing, list likely files, risky areas, verification commands, and rollback plan. Then wait."

### What bad looks like

Bad: "Just fix it. Start coding."

### Minimal example

For an auth bug, ask for a plan that names the affected route, tests, session/auth files, and rollback checkpoint before letting Codex patch anything.

### Checklist

- ask for likely files before edits
- name what must not change
- identify the smallest useful check
- require a rollback or branch plan
- skip the plan only when the work is tiny and disposable

<!-- VCB:END_SECTION id=vcb.shortcut.skipping_plan.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skipping_plan.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that a plan is not process overhead; it is a cheap way to keep the first edit aligned with the actual risk.

### Diagnostic questions

- Is the task broad, unfamiliar, production-facing, or security-sensitive?
- Does the user know which files are likely involved?
- Is there a check that can prove the change?
- What would make rollback expensive?
- Is Codex about to mix planning and mutation?

### Coaching tactics

- ask for a plan-only pass on risky work
- keep plans short and reviewable
- ask for files, checks, risks, and rollback, not a long essay
- let disposable prototype work use a lighter plan
- turn repeated plan misses into a reusable prompt pattern

### Red flags

- "start coding" before scope is known
- no verification path named
- no branch or checkpoint for shared work
- production/auth/data work treated like a prototype
- plan and implementation mixed in one unreviewed run

### Prompt pattern

```text
Plan first. Do not edit files yet. Return likely files, intended behavior, risky areas, checks to run, forbidden changes, and rollback path. Keep it short enough to review before implementation.
```

<!-- VCB:END_SECTION id=vcb.shortcut.skipping_plan.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They start the coding run immediately because planning feels slower than seeing a diff.

### When the shortcut may be acceptable

Acceptable for disposable prototypes, throwaway local experiments, or tiny isolated edits where rollback is trivial and no real users, secrets, production data, or shared branches are involved.

### When it becomes a bad trade

Bad when the task touches production, auth, payments, data deletion, secrets, CI permissions, public documentation, dependency supply chain, unfamiliar code, or a diff too broad for available review.

### Risk profile

- Probability: medium for small known tasks; high when the repo is unfamiliar or the user wants a broad fix.
- Impact: low for throwaway local work; high for shared, production, security-sensitive, or data-bearing systems.
- Recoverability: good with a branch and clean checkpoint; poor after broad unplanned edits accumulate.

### Blast radius

Skipping the plan can turn one unclear request into wrong files, wrong checks, unrelated cleanup, and a review packet that no one can honestly audit.

### Minimum guardrails

- ask for likely files
- name risky areas
- define checks
- define rollback

### Recovery plan

1. Stop mutation and save the current diff.
2. Ask Codex to summarize changed files and classify intended versus suspect changes.
3. Create or restore a Git checkpoint.
4. Ask for a plan-only pass from the current state.
5. Split or revert anything outside the plan.
6. Run the smallest relevant check before continuing.

## Budget and Constraint Notes

### Cheapest reliable path

Use a four-line plan before spending tokens or human time on a wrong diff.

### Fastest high-usage path

High-throughput users can run implementation quickly after the plan, but the plan still defines what should be reviewed.

### Low-attention path

Low-attention work needs stricter planning because the human will not catch scope drift in real time.

### Production-quality path

Production work requires plan, rollback, review, and verification before merge or deploy.

### Prototype versus production

Prototype planning can be lightweight. Production planning must cover blast radius and recovery.

### Maintenance phase

Maintenance planning should name old behavior, intended behavior, nearest checks, and files that must not be touched.

## Stable Core

- planning is cheapest before edits exist
- bigger blast radius needs a plan gate
- plan detail should scale with risk, not with ceremony

## Volatile Surface

- current Codex planning UI affordances
- surface-specific plan mode behavior
- project-specific verification commands

## Obsolescence Watch

This card should be revised if:

- agents can safely infer scope, risk, checks, and rollback before mutation without explicit user framing

## Evidence and Sources

- `openai.codex.best_practices` - Official OpenAI Codex guidance for prompt goals, context, constraints, done-when criteria, validation, and review.
- `openai.codex.workflows` - Official OpenAI Codex workflow guidance for planning patterns, context, and verification loops.
- `openai.codex.prompting` - Official OpenAI Codex prompting guidance for focused task loops and context.
- `vcb.synthesis.stable_engineering_practice` - VCB maintainer synthesis for durable risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.prompting.plan_first`
- `vcb.workflow.feature_slicing`
- `vcb.workflow.unknown_codebase`
- `vcb.constraints.scope_budget`
- `vcb.constraints.recovery_budget`
- `vcb.chapter.plan_first_code_second`

<!-- VCB:STOP_RETRIEVAL reason="skipping_plan_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.skipping_plan -->
