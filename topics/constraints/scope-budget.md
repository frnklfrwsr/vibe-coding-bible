<!-- VCB:BEGIN_TOPIC id=vcb.constraints.scope_budget version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex constraint, planning, review, and pricing anchors plus VCB
  maintainer synthesis for budget, attention, recovery, and phase-control guidance
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
id: vcb.constraints.scope_budget
title: Scope Budget
type: concept
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- prompting
- feature slicing
- refactoring
- cloud tasks
- PRs
- maintenance
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.one_big_prompt
- vcb.shortcut.broad_refactor
- vcb.shortcut.ambiguous_cloud_task
- vcb.shortcut.overbuilding_first_app
durable_principles:
- scope is a budget because every extra concern increases review and recovery cost
- one task should have one primary outcome
- broad prompts should be converted into plans or slices before coding
likely_to_change:
- surface-specific task limits
- current Plan mode affordances
- cloud task and worktree behavior
- model ability to maintain large-scope intent
obsolete_when:
- agentic tools can make large multi-concern changes with the same reviewability and recoverability
  as small changes
related_topics:
- vcb.workflow.feature_slicing
- vcb.prompting.plan_first
- vcb.prompting.four_part_prompt
- vcb.workflow.refactoring
- vcb.failure.broad_refactor_drift
- vcb.constraints.usage_burn
- vcb.constraints.recovery_budget
- vcb.constraints.review_budget
---

# Scope Budget

> Summary:
> Scope budget is how much change a single Codex task is allowed to contain. Small scope makes review, testing, recovery, and cost control possible.

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

<!-- VCB:BEGIN_SECTION id=vcb.constraints.scope_budget.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Scope budget is the amount of change you allow in one task. It limits files, behaviors, user flows, dependencies, cleanup, and verification expectations.

### Why it matters

Codex can handle large requests, but humans still need to understand the result. Too much scope creates big diffs, vague testing, hidden behavior changes, and expensive rollback.

### The mental model

A small slice is a receipt you can audit. A huge task is a grocery cart dumped on the floor.

### What good looks like

Good: “Implement only server-side email validation. Do not redesign signup. Do not change auth/session flow. Stop after tests for valid and invalid email.”

### What bad looks like

Bad: “Fix signup, improve validation, clean up auth, modernize the UI, and add tests.”

### Minimal example

Give every task a scope boundary: files or folders in, files or folders out, behavior in, behavior out, and stop condition.

### Checklist

- one primary outcome
- explicit non-goals
- file/folder boundaries
- no opportunistic cleanup
- verification fits the slice

<!-- VCB:END_SECTION id=vcb.constraints.scope_budget.human -->

<!-- VCB:BEGIN_SECTION id=vcb.constraints.scope_budget.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to make scope small enough that review and recovery remain affordable. Broad ideas should become plans, not immediate implementation prompts.

### Diagnostic questions

- How many concerns are inside this request?
- Can the user review the diff in one sitting?
- What cleanup should be deferred?
- Which files are explicitly out of bounds?
- What is the smallest slice that proves value?

### Coaching tactics

- convert broad prompts into a slice plan
- require non-goals in the prompt
- ask Codex to stop if scope expands
- separate refactor from behavior change
- prefer one failing/relevant check per slice before broad suites

### Red flags

- “while you are there” cleanup
- feature plus refactor plus dependency update in one task
- many files changed without a stated boundary
- agent touches unrelated modules
- acceptance criteria do not mention what is out of scope

### Prompt pattern

```text
Shrink this request into the smallest reviewable slice. List in-scope behavior, out-of-scope behavior, allowed files, forbidden files, verification, and the next slice. Do not implement unrelated cleanup or dependency changes.
```

<!-- VCB:END_SECTION id=vcb.constraints.scope_budget.ai_coach -->

## Shortcut Reality

### Ideal practice

Keep one Codex task small enough to review, verify, and revert.

### What people often do instead

Users put the entire desired end state into one prompt because it feels efficient.

### When the shortcut may be acceptable

Acceptable for disposable prototypes or read-only planning where output is not merged as-is.

### When it becomes a bad trade

Bad for production, refactors, dependency changes, security-sensitive code, and unfamiliar codebases.

### Risk profile

- Probability: high when prompts include multiple verbs and no non-goals.
- Impact: medium for prototypes; high for maintenance and production.
- Recoverability: better for one concern; worse for mixed diffs.

### Blast radius

Oversized scope creates unreviewable diffs, weaker tests, hidden regressions, and budget burn from repeated broad corrections.

### Minimum guardrails

- state non-goals
- cap files or modules
- forbid opportunistic cleanup
- split feature/refactor/dependency work
- ask for a plan when scope exceeds one slice

### Recovery plan

1. Stop the task before accepting the diff.
2. Ask Codex to classify changes by concern.
3. Keep or reapply only the target slice.
4. Revert unrelated changes.
5. Create separate follow-up tickets for legitimate extra work.

## Budget and Constraint Notes

### Cheapest reliable path

pay for one slice and one targeted check before expanding.

### Fastest high-usage path

run parallel slices only when they do not touch overlapping files or behavior.

### Low-attention path

low-attention tasks must be tiny and evidence-structured.

### Production-quality path

scope boundaries are a production control, not bureaucracy.

### Prototype versus production

prototypes can explore broad ideas; production merges narrow slices.

### Maintenance phase

small scope protects future bisects, reviews, and rollback.

## Stable Core

- scope is a budget because every extra concern increases review and recovery cost
- one task should have one primary outcome
- broad prompts should be converted into plans or slices before coding

## Volatile Surface

- surface-specific task limits
- current Plan mode affordances
- cloud task and worktree behavior
- model ability to maintain large-scope intent

Review volatile details against official sources or dated pricing snapshots before freezing commands, UI labels, model choices, plan packaging, context limits, feature availability, exact prices, or exact limits.

## Obsolescence Watch

- agentic tools can make large multi-concern changes with the same reviewability and recoverability as small changes

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for constraints, done-when criteria, planning, reusable guidance, testing, review, permissions, and validation.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples for explicit context, validation, and done definitions.
- `openai.codex.use_cases.follow_goals` — Official OpenAI Codex goal-following use case for long-running goals, validation, and stopping conditions.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable engineering control loops, risk, review, recovery, and constraint management.

## Related Topics

- `vcb.workflow.feature_slicing`
- `vcb.prompting.plan_first`
- `vcb.prompting.four_part_prompt`
- `vcb.workflow.refactoring`
- `vcb.failure.broad_refactor_drift`
- `vcb.constraints.usage_burn`
- `vcb.constraints.recovery_budget`
- `vcb.constraints.review_budget`

<!-- VCB:STOP_RETRIEVAL reason="constraint_topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.constraints.scope_budget -->
