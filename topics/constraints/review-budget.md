<!-- VCB:BEGIN_TOPIC id=vcb.constraints.review_budget version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: true
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
id: vcb.constraints.review_budget
title: Review Budget
type: concept
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- diff review
- PR review
- Codex App
- GitHub review
- team workflows
- maintenance
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.reviewing_cloud_summary_only
- vcb.shortcut.checklist_theater
- vcb.shortcut.accepting_codex_review_as_approval
durable_principles:
- review capacity must shape task size
- review should prioritize risk and evidence, not merely line count
- AI review is a signal, not an approval authority
likely_to_change:
- Codex review UI behavior
- GitHub integration features
- review-command behavior
- team PR policy and branch protections
obsolete_when:
- generated diffs can be accepted safely without human or policy review across production contexts
related_topics:
- vcb.workflow.codex_output_review
- vcb.workflow.reviewing_diffs
- vcb.workflow.github_pr_review
- vcb.concepts.diff
- vcb.concepts.pull_request
- vcb.constraints.attention_budget
- vcb.constraints.scope_budget
- vcb.failure.done_claim_without_evidence
---

# Review Budget

> Summary:
> Review budget is the human and automated inspection capacity available before accepting Codex output. It determines diff size, risk gates, and what evidence the agent must return.

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

<!-- VCB:BEGIN_SECTION id=vcb.constraints.review_budget.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Review budget is how much inspection you can afford before accepting a change. It includes human diff reading, PR review, test review, AI review, security review, and time to ask follow-up questions.

### Why it matters

A change that is cheap to generate can be expensive to review. If the diff is larger than the review budget, you do not have a finished task; you have unreviewed risk.

### The mental model

Review budget is the gate width. If the truck is too wide, shrink the load instead of breaking the gate.

### What good looks like

Good: “Keep the diff small enough for a 15-minute review. Return changed files, risky hunks, checks run, and suggested review order.”

### What bad looks like

Bad: “This is a 2,000-line generated diff, but Codex reviewed it, so merge.”

### Minimal example

Before work starts, decide who or what will review the diff and how large/risky the diff may be.

### Checklist

- review owner is named
- diff size is reviewable
- high-risk files are highlighted
- AI review is not treated as approval
- checks and “not verified” notes are included

<!-- VCB:END_SECTION id=vcb.constraints.review_budget.human -->

<!-- VCB:BEGIN_SECTION id=vcb.constraints.review_budget.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to budget review as part of the task, not as an optional afterthought. If review capacity is low, shrink the task.

### Diagnostic questions

- Who will review this?
- How long can they spend?
- What files need senior review?
- What can automated review catch and what can it not catch?
- Is the diff small enough for available attention?

### Coaching tactics

- ask Codex to prepare a review packet
- make Codex order hunks by risk
- use PR/AI review as a supplement
- split diffs that exceed review capacity
- reject merges based only on summaries

### Red flags

- large diff with no review owner
- Codex review treated as human approval
- summary-only review
- tests changed without review
- security-sensitive code reviewed by checklist theater

### Prompt pattern

```text
Prepare this change for my review budget of [time/person]. Keep the diff within that budget or split it. Return changed files, risky hunks, generated tests to inspect, checks run, unchecked areas, and a recommended review order.
```

<!-- VCB:END_SECTION id=vcb.constraints.review_budget.ai_coach -->

## Shortcut Reality

### Ideal practice

Size the task so the available reviewer can inspect it properly.

### What people often do instead

Users generate a large diff, run a superficial AI review, and merge because the change looks organized.

### When the shortcut may be acceptable

Acceptable for low-risk generated docs, throwaway prototypes, or isolated local changes with trivial rollback.

### When it becomes a bad trade

Bad for security, data, auth, dependencies, tests, refactors, production behavior, or release/public docs.

### Risk profile

- Probability: high when diff size exceeds reviewer attention.
- Impact: medium for internal cleanup; high for production and security.
- Recoverability: good before merge; worse after dependent work builds on the unreviewed change.

### Blast radius

Underfunded review lets wrong assumptions, weak tests, broad refactors, and unsupported done claims enter the codebase.

### Minimum guardrails

- cap diff size
- require review packet
- separate generated tests for inspection
- flag risky files
- block AI review from being sole approval

### Recovery plan

1. Do not merge.
2. Ask Codex to split or summarize by risk.
3. Review highest-risk hunks first.
4. Revert unrelated or unreviewable chunks.
5. Add a review-budget limit to future prompts.

## Budget and Constraint Notes

### Cheapest reliable path

shrink diffs until review is affordable.

### Fastest high-usage path

generate review packets automatically, but keep human approval where risk is high.

### Low-attention path

low-attention review requires tiny diffs and strong evidence summaries.

### Production-quality path

review budget includes code, tests, security-sensitive paths, docs, and rollback.

### Prototype versus production

prototype review can be lightweight; production review cannot be summary-only.

### Maintenance phase

review budget protects future maintainers by keeping intent, scope, and risk readable.

## Stable Core

- review capacity must shape task size
- review should prioritize risk and evidence, not merely line count
- AI review is a signal, not an approval authority

## Volatile Surface

- Codex review UI behavior
- GitHub integration features
- review-command behavior
- team PR policy and branch protections

Review volatile details against official sources or dated pricing snapshots before freezing commands, UI labels, model choices, plan packaging, context limits, feature availability, exact prices, or exact limits.

## Obsolescence Watch

- generated diffs can be accepted safely without human or policy review across production contexts

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for constraints, done-when criteria, planning, reusable guidance, testing, review, permissions, and validation.
- `openai.codex.app_review` — Official OpenAI Codex app review guidance for diff-centered review and feedback loops.
- `openai.codex.github_review` — Official OpenAI Codex GitHub review guidance for AI-assisted PR review as a signal, not authority.
- `github.docs.pull_requests` — Official GitHub pull-request documentation for review, checks, and merge context.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable engineering control loops, risk, review, recovery, and constraint management.

## Related Topics

- `vcb.workflow.codex_output_review`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.github_pr_review`
- `vcb.concepts.diff`
- `vcb.concepts.pull_request`
- `vcb.constraints.attention_budget`
- `vcb.constraints.scope_budget`
- `vcb.failure.done_claim_without_evidence`

<!-- VCB:STOP_RETRIEVAL reason="constraint_topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.constraints.review_budget -->
