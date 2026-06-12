<!-- VCB:BEGIN_TOPIC id=vcb.field.skeleton_todo_first version=0.39.0-draft.chunk38 -->
---
version: 0.39.0-draft.chunk38
last_verified: '2026-06-11'
last_reviewed: '2026-06-11'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: true
  speculative: false
evidence_level: E4_COMMUNITY_FIELD_REPORT
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: community_field_report
evidence_scope: candidate field-practice card; official sources support underlying product
  behavior or engineering principle, but the specific ritual remains unpromoted until locally
  reproduced or otherwise strengthened
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
id: vcb.field.skeleton_todo_first
title: Skeleton/TODO First
type: field_practice
status: active
field_practice_status: candidate
officially_endorsed: 'false'
review_cadence: monthly
next_review_due: '2026-07-11'
applies_to:
- Codex field practice
- AI-assisted software development
- practice evaluation
- workflow adoption
stability:
  principle: COMMUNITY_HACK
  surface: MODERATE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.one_big_prompt
- vcb.shortcut.accepting_looks_done
durable_principles:
- Constrain solution shape before implementation when architecture, interfaces, or user flow
  matters more than raw generation speed.
- Evidence labels must travel with unofficial practices until they are reproduced, promoted,
  or retired.
likely_to_change:
- current Codex product behavior, model behavior, available surfaces, local team workflow,
  and the amount of benefit from this practice
obsolete_when:
- Codex planning/scaffolding becomes reliable enough in the project that manual skeletons
  no longer reduce review cost.
related_topics:
- vcb.prompting.plan_first
- vcb.prompting.acceptance_criteria
- vcb.workflow.feature_slicing
- vcb.shortcut.one_big_prompt
- vcb.field.greenfield_vs_production_rule
---

# Skeleton/TODO First

> Summary:
> Candidate field practice: Have the human sketch a file/function/component skeleton or TODO outline before Codex fills in implementation details. This card labels the practice, gives safe trial conditions, and prevents the tactic from being treated as official best practice before evidence supports promotion.

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

<!-- VCB:BEGIN_SECTION id=vcb.field.skeleton_todo_first.human -->
## 1. For the Human: Plain-Language Concept

### What this practice is

Have the human sketch a file/function/component skeleton or TODO outline before Codex fills in implementation details.

### Evidence status

This is an authored candidate field-practice card. It is useful enough to evaluate, but it is not official guidance and it has not been promoted. The evidence label is `E4_COMMUNITY_FIELD_REPORT` for the practice ritual itself. Official documentation may support nearby product behavior or engineering principles, but that does not prove this ritual works in your repo.

### Why people try it

The practice tries to reduce a recurring vibe-coding failure: vague work orders, stale context, weak verification, broad unreviewable diffs, repeated corrections, or overtrust in confident model output.

### What good looks like

Good: The human writes interfaces, empty functions, route names, component boundaries, TODOs, and acceptance criteria; Codex fills the smallest slice and explains deviations.

### What bad looks like

Bad: The human asks for a whole implementation from a vague prompt, then tries to review a large generated structure they never chose.

### Safe trial

Use it on a feature that has known boundaries but uncertain implementation details. Review whether the skeleton reduced diff size and design drift.

### Checklist

- keep the practice labeled as candidate until local evidence exists
- define the exact project type and risk level before trying it
- run it on one bounded task first
- record benefit, failure, cost, and false-confidence risk
- decide whether to promote, keep testing, narrow, or retire it

<!-- VCB:END_SECTION id=vcb.field.skeleton_todo_first.human -->

<!-- VCB:BEGIN_SECTION id=vcb.field.skeleton_todo_first.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach this as a field-practice evaluation loop, not as a rule. The human should understand the durable principle, the unproven ritual, the evidence label, and the safest local test.

### Diagnostic questions

- What problem is the practice supposed to solve in this repo?
- What is the smallest task where it can be tested safely?
- What would count as success: fewer defects, smaller diffs, faster review, clearer prompts, or lower recovery cost?
- What could the practice make worse?
- Who owns the decision to promote, narrow, or retire it?

### Coaching tactics

- keep the evidence label visible in every recommendation
- ask for a local trial plan before making it durable
- distinguish official product behavior from the community ritual
- require before/after comparison where possible
- never let the practice bypass diff, test, source, security, or production review

### Red flags

- the human says “everyone does this” without a source or local test
- the practice is added to AGENTS.md, hooks, skills, CI, or team process after one success
- the evidence label disappears from prompts or docs
- the practice changes production, auth, payment, data, or dependency behavior without review

### Prompt pattern

```text
Evaluate this field practice as a candidate, not a rule.
Practice: Skeleton/TODO First
Claim: Have the human sketch a file/function/component skeleton or TODO outline before Codex fills in implementation details.
Project risk: [prototype/MVP/production/maintenance]
Trial task: [small bounded task]
Evidence to collect: [defects found, review time, checks, false positives]
Decision options: promote locally, keep testing, narrow scope, or retire.
```

<!-- VCB:END_SECTION id=vcb.field.skeleton_todo_first.ai_coach -->

## Shortcut Reality

### Ideal practice

Start from the durable principle: Constrain solution shape before implementation when architecture, interfaces, or user flow matters more than raw generation speed.

### What people often do instead

People turn the tactic into a blanket rule because it worked once, sounded plausible, or matched a community anecdote.

### When the shortcut may be acceptable

It may be acceptable for a small, reversible task where the practice is explicitly labeled, review evidence remains mandatory, and no durable repo rule changes until the practice survives local testing.

### When it becomes a bad trade

It becomes a bad trade when it changes production behavior, security posture, dependency decisions, team process, or durable Codex configuration before the practice is proven.

### Risk profile

- Probability: medium until the team has local evidence.
- Impact: low for throwaway tasks; high when promoted into durable guidance, CI, hooks, skills, or production workflow.
- Recoverability: medium if the trial is bounded and logged; low if the practice silently changes team defaults.

### Blast radius

The blast radius is the set of tasks, prompts, agents, repo files, and humans that start following the practice as if it were proven.

### Minimum guardrails

- skeletons are constraints, not fake completeness
- bounded trial task
- visible evidence label
- explicit owner
- rollback or retirement path

### Recovery plan

Remove the practice from prompts, docs, AGENTS.md, skills, hooks, CI, and team process. Re-run the affected task with the normal VCB control loop: context, plan, patch, verification, review, and recovery notes.

## Budget and Constraint Notes

### Cheapest reliable path

Try the practice once on a low-risk task and use existing checks or review artifacts. Do not add a new tool, skill, hook, or process just to evaluate it.

### Fastest high-usage path

Batch several similar tasks only after the first trial shows value. Keep a short comparison log so usage burn does not masquerade as progress.

### Low-attention path

Use the practice only for report-first work unless a human can review the diff, source evidence, checks, and failure modes before mutation or merge.

### Production-quality path

Treat the practice as advisory until it has local evidence, owner approval, rollback, and compatibility with production-quality constraints.

### Prototype versus production

Prototype use can be lighter if fake data, throwaway code, and easy rollback are guaranteed. Production use needs documented evidence and a promotion decision.

### Build versus maintenance

During build, the practice may reduce ambiguity. During maintenance, it must preserve compatibility, tests, and existing user behavior.

## Stable Core

- The durable principle is stable: Constrain solution shape before implementation when architecture, interfaces, or user flow matters more than raw generation speed.
- Field practices need explicit evidence labels.
- Local reproduction beats generic community confidence.
- Official docs define product behavior; field practice cards define evaluation posture.

## Volatile Surface

- Codex features, model behavior, product UI, and context handling may change.
- Community tactics can become stale or harmful as tools improve.
- The value of this practice depends on repo size, team skill, checks, and review budget.
- Re-check official sources before turning a field ritual into durable configuration.

## Obsolescence Watch

Review this card monthly. Retire, narrow, or rewrite it when:

- Codex planning/scaffolding becomes reliable enough in the project that manual skeletons no longer reduce review cost.
- the practice no longer improves local outcomes
- the practice creates more review noise than defects prevented
- official behavior or team tooling changes the underlying risk

## Evidence and Sources

Evidence level for the practice ritual: `E4_COMMUNITY_FIELD_REPORT`. It remains a candidate field practice; do not present it as official best practice.

Source anchors and principle support:

- `openai.codex.best_practices`
- `openai.codex.prompting`

Notes:

- Official sources support product behavior or related engineering principles, not automatic promotion of the field ritual.
- No local reproduction claim is made in this card.
- Promotion requires the local evidence rule stated in the field-practice register.

## Related Topics

- `vcb.prompting.plan_first`
- `vcb.prompting.acceptance_criteria`
- `vcb.workflow.feature_slicing`
- `vcb.shortcut.one_big_prompt`
- `vcb.field.greenfield_vs_production_rule`

<!-- VCB:STOP_RETRIEVAL reason="field_practice_card_complete" -->
<!-- VCB:END_TOPIC id=vcb.field.skeleton_todo_first -->
