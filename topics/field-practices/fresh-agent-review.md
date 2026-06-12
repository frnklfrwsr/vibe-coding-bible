<!-- VCB:BEGIN_TOPIC id=vcb.field.fresh_agent_review version=1.0.1-post-release.issue7 -->
---
version: 1.0.1-post-release.issue7
last_verified: '2026-06-12'
last_reviewed: '2026-06-12'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: true
  speculative: false
evidence_level: E2_REPRODUCED_LOCALLY
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: local_reproduction
evidence_scope: bounded local reproduction in VCB PR #18 review gate; official sources support review mechanics, but the practice is not promoted as universal guidance
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
id: vcb.field.fresh_agent_review
title: Fresh Agent Review
type: field_practice
status: active
field_practice_status: reproduced
local_reproduction_basis: 'PR #18 Codex Review independently found an actionable validator issue; bounded to GitHub PR review workflow.'
officially_endorsed: 'false'
review_cadence: monthly
next_review_due: '2026-07-12'
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
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.consensus_as_correctness
durable_principles:
- Independent review catches different mistakes because it is not anchored to the implementation
  path.
- Evidence labels must travel with unofficial practices until they are reproduced, promoted,
  or retired.
likely_to_change:
- current Codex product behavior, model behavior, available surfaces, local team workflow,
  and the amount of benefit from this practice
obsolete_when:
- Native review surfaces become reliable and auditable enough that a separate fresh-session
  ritual adds no marginal value.
related_topics:
- tool.codex_github_review
- tool.github
- vcb.workflow.reviewing_diffs
- vcb.workflow.codex_output_review
- vcb.shortcut.consensus_as_correctness
- vcb.field.multi_agent_review_consensus
---

# Fresh Agent Review

> Summary:
> Reproduced field practice (bounded): Ask a fresh session, agent, or review surface to inspect a diff before commit so it sees the work without the original conversation’s assumptions. This card labels the practice, gives safe trial conditions, and prevents the tactic from being treated as official best practice before evidence supports promotion.

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

<!-- VCB:BEGIN_SECTION id=vcb.field.fresh_agent_review.human -->
## 1. For the Human: Plain-Language Concept

### What this practice is

Ask a fresh session, agent, or review surface to inspect a diff before commit so it sees the work without the original conversation’s assumptions.

### Evidence status

This field practice is marked `reproduced` only for the bounded VCB workflow documented in the Issue #7 audit. It is not official guidance and it has not been promoted. The evidence label is `E2_REPRODUCED_LOCALLY` for the local reproduction note; official documentation supports nearby mechanics, not universal adoption of the ritual.

### Why people try it

The practice tries to reduce a recurring vibe-coding failure: vague work orders, stale context, weak verification, broad unreviewable diffs, repeated corrections, or overtrust in confident model output.

### What good looks like

Good: The fresh reviewer receives the diff, task goal, acceptance criteria, risk areas, and asks for concrete defects rather than praise.

### What bad looks like

Bad: The same agent that wrote the patch is asked “does this look good?” and its confidence is treated as approval.

### Safe trial

Use it on one PR-sized diff. Compare fresh-review findings against human diff review and track whether it found real defects or only style noise.

### Checklist

- keep the practice labeled as candidate until local evidence exists
- define the exact project type and risk level before trying it
- run it on one bounded task first
- record benefit, failure, cost, and false-confidence risk
- decide whether to promote, keep testing, narrow, or retire it

<!-- VCB:END_SECTION id=vcb.field.fresh_agent_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.field.fresh_agent_review.ai_coach -->
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
Practice: Fresh Agent Review
Claim: Ask a fresh session, agent, or review surface to inspect a diff before commit so it sees the work without the original conversation’s assumptions.
Project risk: [prototype/MVP/production/maintenance]
Trial task: [small bounded task]
Evidence to collect: [defects found, review time, checks, false positives]
Decision options: promote locally, keep testing, narrow scope, or retire.
```

<!-- VCB:END_SECTION id=vcb.field.fresh_agent_review.ai_coach -->

## Shortcut Reality

### Ideal practice

Start from the durable principle: Independent review catches different mistakes because it is not anchored to the implementation path.

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

- fresh review is a second signal, not merge authority
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

- The durable principle is stable: Independent review catches different mistakes because it is not anchored to the implementation path.
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

- Native review surfaces become reliable and auditable enough that a separate fresh-session ritual adds no marginal value.
- the practice no longer improves local outcomes
- the practice creates more review noise than defects prevented
- official behavior or team tooling changes the underlying risk

## Evidence and Sources

Evidence level for the practice ritual: `E2_REPRODUCED_LOCALLY` in the bounded VCB audit context. It remains unpromoted; do not present it as official best practice or universal proof.

Source anchors and principle support:

- `openai.codex.github_review`
- `openai.codex.use_cases.github_code_reviews`
- `openai.help.truthfulness`

Notes:

- Official sources support product behavior or related engineering principles, not automatic promotion of the field ritual.
- Issue #7 audit: Bounded local reproduction is based on PR #18, where independent Codex Review found an actionable validator issue after the initial branch push.
- Promotion requires the local evidence rule stated in the field-practice register.

## Related Topics

- `tool.codex_github_review`
- `tool.github`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.codex_output_review`
- `vcb.shortcut.consensus_as_correctness`
- `vcb.field.multi_agent_review_consensus`

<!-- VCB:STOP_RETRIEVAL reason="field_practice_card_complete" -->
<!-- VCB:END_TOPIC id=vcb.field.fresh_agent_review -->
