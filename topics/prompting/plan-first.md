<!-- VCB:BEGIN_TOPIC id=vcb.prompting.plan_first version=0.1.0 -->
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
evidence_scope: official OpenAI Codex prompting/workflow anchors plus VCB maintainer synthesis
  for risk, budget, and coaching guidance
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
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.prompting.plan_first
title: Plan First
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- Complex repo tasks
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.skipping_plan
- vcb.shortcut.one_big_prompt
- vcb.shortcut.broad_refactor
durable_principles:
- planning reveals assumptions before they become code
- complex tasks need an inspect step before mutation
- plans are disposable working agreements, not sacred documents
likely_to_change:
- Plan mode availability
- surface-specific planning UX
- how Codex persists plans
- model ability to decompose tasks
obsolete_when:
- Codex can safely make complex multi-file changes without explicit planning, review, or assumption
  surfacing
related_topics:
- vcb.chapter.plan_first_code_second
- vcb.prompting.four_part_prompt
- vcb.prompting.context_management
- vcb.workflow.unknown_codebase
- vcb.workflow.feature_slicing
- vcb.codex.cli
- vcb.codex.cloud
---

> Summary:
> Plan-first prompting asks Codex to inspect, propose a path, and surface assumptions before it edits code.

## Quick Navigation
- For the Human
- For the AI Coach
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=vcb.prompting.plan_first.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Plan-first means you ask Codex to understand and outline the work before changing code. The plan names files, steps, risks, assumptions, and checks.

### Why it matters

Skipping the plan feels faster but often turns one coding session into three cleanup sessions. A plan catches wrong files, broad scope, and missing tests before they are buried in a diff.

### The mental model

Plan-first is “measure twice, cut once” for agentic coding. It is not bureaucracy; it is cheap risk discovery.

### What good looks like

Good: “Inspect the auth flow and propose a plan before editing. Include files to touch, assumptions, tests to run, and risks. Wait for confirmation.”

### What bad looks like

Bad: “Refactor auth and make it cleaner.” Codex may start moving code before it understands the flow.

### Minimal example

Plan first: 1) inspect relevant files, 2) summarize current behavior, 3) propose smallest viable change, 4) list tests/checks, 5) wait before editing.

### Checklist

- ask for a plan when task spans files or behavior
- force Codex to name assumptions
- reject plans that are just generic steps
- approve only a small first slice
- turn the plan into acceptance criteria before coding
<!-- VCB:END_SECTION id=vcb.prompting.plan_first.human -->

<!-- VCB:BEGIN_SECTION id=vcb.prompting.plan_first.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use planning as a safety boundary between understanding and mutation.

### Diagnose the human’s current model

- Does the task cross module boundaries?
- Would a wrong edit be expensive to unwind?
- Does the user know which files matter?
- Are tests unclear or missing?
- Is Codex about to refactor before proving behavior?

### Explanation strategy

Require plan-first for ambiguous, multi-file, high-blast-radius, or unfamiliar-codebase work. Keep the plan short and actionable. Reject plans that do not cite concrete repo evidence.

### Useful metaphor

A plan is scaffolding. You remove it after the work, but without it the construction can fall into the street.

### Coaching tactics

- separate “inspect” from “edit” phases
- ask Codex to cite files and flows in the plan
- have the user approve or edit the plan
- convert plan steps into small commits or tasks
- update the plan when discovery changes reality

### Prompt patterns

```text
Do not edit yet. Inspect [area] and propose a plan with files, assumptions, risks, checks, and the smallest first slice.
Here is the plan. Implement step 1 only. Stop before step 2 and report results.
If the plan requires broad refactor, propose a smaller reversible slice first.
```

### Red flags to call out directly

- plan names no files
- plan says “update tests” without naming which tests
- plan starts with broad cleanup
- user asks for unattended production work with no inspection phase
- Codex edits before confirming assumptions

### Exercises

- Ask the human to classify tasks as no-plan, quick-plan, or formal-plan.
- Give a fake broad task and have the human cut the plan to one reversible slice.
- Review a Codex plan and mark every unsupported assumption.
<!-- VCB:END_SECTION id=vcb.prompting.plan_first.ai_coach -->

## Shortcut Reality

### The ideal practice

Use plan-first for complex, ambiguous, unfamiliar, or high-risk work.

### What users often do instead

Users often ask Codex to implement immediately because planning feels slower.

### When the shortcut may be fine

Skipping a plan can be fine for tiny local edits, docs wording, one-test additions, or disposable prototypes.

### When the shortcut is a bad idea

Skipping the plan is a bad trade for auth, payments, data migrations, broad refactors, dependency changes, or unknown codebases.

### Risk profile

- Probability of failure: Low on tiny edits; medium to high on multi-file work.
- Impact if it fails: Impact grows with scope and with the number of assumptions Codex has to invent.
- Ease of recovery: Good when changes are on a branch and small; poor when an unplanned refactor touches many files.
- Blast radius: The blast radius is the number of files and behaviors changed before anyone checks the reasoning.
- Skill needed to recover: Medium; recovery requires reading diffs and restoring intent.
- Hidden cost: Review fatigue, merge conflicts, test churn, and plausible architecture drift.

### Minimum guardrails

- plan before edits on risky work
- cap the first implementation slice
- require file-specific reasoning
- approve the plan explicitly
- make the plan produce verification steps

### Recovery plan

- Stop further edits.
- Ask Codex to describe current diff and original assumptions.
- Revert or stash if too broad.
- Create a plan from the clean baseline.
- Re-implement the smallest safe slice.

## Budget and Constraint Notes

### Cheapest reliable path

Use a short plan for any task where cleanup would cost more than two minutes.

### Fastest high-usage path

High-throughput users should batch planning for several independent tasks, then implement selected slices.

### Low-attention path

Low-attention delegation requires a plan plus stop conditions; otherwise Codex may optimize the wrong path for a long time.

### Production-quality path

Production plans should name rollback, tests, data impact, and review owner.

### Prototype versus production

Prototype plans can be lightweight. Production plans must be explicit enough for someone else to audit. Build work tolerates discovery; maintenance work needs stricter boundaries. 

## Stable Core

- inspect before mutate when risk is high
- plans must be grounded in repository evidence
- planning saves cost when wrong changes are expensive

## Volatile Surface

- Codex Plan mode mechanics
- whether a surface can persist plan files
- model decomposition quality
- UI affordances for approving plans
- cloud task planning features

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- official Codex surfaces change plan-mode behavior
- plan artifacts become automatically enforced
- Codex can reliably infer safe plans without explicit prompting in complex repos

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, review, and verification.
- `openai.codex.prompting` — Official OpenAI Codex prompting guidance for goals, context, success criteria, and interaction patterns.
- `openai.codex.exec_plans_cookbook` — Official/OpenAI cookbook-style execution-plan guidance for plan-oriented agent work.
- `vcb.synthesis.prompting_operator_practice` — VCB maintainer synthesis for prompt operating patterns, guardrails, and coaching tactics.

## Related Topics

- `vcb.chapter.plan_first_code_second`
- `vcb.prompting.four_part_prompt`
- `vcb.prompting.context_management`
- `vcb.workflow.unknown_codebase`
- `vcb.workflow.feature_slicing`
- `vcb.codex.cli`
- `vcb.codex.cloud`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.prompting.plan_first -->
