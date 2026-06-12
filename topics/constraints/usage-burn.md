<!-- VCB:BEGIN_TOPIC id=vcb.constraints.usage_burn version=0.1.0 -->
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
id: vcb.constraints.usage_burn
title: Usage Burn
type: concept
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex Cloud
- API-key usage
- team budgets
- pricing snapshots
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.context_dumping
- vcb.shortcut.defaulting_to_high_throughput
- vcb.shortcut.model_routing_guesswork
- vcb.shortcut.parallel_cloud_sprawl
- vcb.shortcut.over_optimizing_for_price
durable_principles:
- usage cost is controlled by task shape before it is controlled by plan choice
- context dumping and speculative retries burn budget without increasing certainty
- exact limits and rates are volatile and belong in snapshots
likely_to_change:
- current Codex plan limits
- credit rates and token accounting
- model availability and speed settings
- usage dashboard behavior
- shared-limit policy across agentic features
obsolete_when:
- Codex cost becomes negligible or fully predictable across all surfaces and plans
related_topics:
- vcb.chapter.budget_aware_codex_workflows
- vcb.chapter.cost_benefit_analysis
- vcb.pricing_snapshot.openai_codex
- vcb.constraints.operating_mode
- vcb.constraints.scope_budget
- vcb.constraints.attention_budget
- vcb.prompting.context_management
- vcb.failure.context_pollution
---

# Usage Burn

> Summary:
> Usage burn is how quickly Codex work consumes messages, credits, tokens, rate limits, or team budget. It is driven by task size, context size, model/speed choice, retries, parallelism, and verification loops.

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

<!-- VCB:BEGIN_SECTION id=vcb.constraints.usage_burn.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Usage burn is the budget you spend while Codex works. It includes visible limits, credits, token-based usage, and the hidden cost of retries caused by vague prompts, bloated context, or oversized tasks.

### Why it matters

A high plan does not make bad task design free. Broad prompts, long stale threads, unnecessary screenshots/images, parallel cloud tasks, and repeated “try again” loops can burn through budget while producing less reviewable work.

### The mental model

Think of usage burn like fuel. A bigger tank helps, but a wrong route and idling engine still waste fuel.

### What good looks like

Good: “Use a small context packet, make a plan, implement one slice, run the targeted check, and stop if the result is ambiguous.”

### What bad looks like

Bad: “Here is the whole repo and every error I remember. Fix everything. Try until it works.”

### Minimal example

Track the burn drivers: context size, task size, number of retries, number of parallel agents, model/speed choice, and verification commands.

### Checklist

- exact prices/limits are checked in the pricing snapshot or official source
- prompt has a stop condition
- context is curated, not dumped
- parallelism is justified by independent work
- retry loops are capped

<!-- VCB:END_SECTION id=vcb.constraints.usage_burn.human -->

<!-- VCB:BEGIN_SECTION id=vcb.constraints.usage_burn.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat cost as a workflow property. The cheapest reliable path is usually smaller prompts, better context, and stronger stopping rules, not merely a cheaper model.

### Diagnostic questions

- What is causing spend: context, model, retries, parallelism, images, or cloud tasks?
- Is the task too broad for one run?
- What evidence will stop the loop?
- Can a smaller read-only pass reduce implementation waste?
- Is the user hardcoding volatile limit numbers into stable prose?

### Coaching tactics

- replace context dumps with file lists and excerpts
- set a maximum number of implementation attempts
- require the model to ask before broadening scope
- separate exploration from mutation
- send exact pricing questions to snapshots or current official sources

### Red flags

- user asks for exact current limits in stable guidance
- agent keeps retrying after the same failure
- multiple cloud tasks work on overlapping scope
- large screenshots or browser runs are used for simple text tasks
- cheap model choice causes repeated wrong attempts

### Prompt pattern

```text
Optimize this task for usage burn. Use only necessary context, state the smallest useful slice, name a stop condition, and tell me when you need more context instead of guessing. Do not include exact plan limits or prices; point to the dated pricing snapshot for volatile values.
```

<!-- VCB:END_SECTION id=vcb.constraints.usage_burn.ai_coach -->

## Shortcut Reality

### Ideal practice

Control usage by narrowing context, slicing work, and defining stop conditions before implementation.

### What people often do instead

Users buy more capacity or launch more runs instead of fixing vague prompts and bloated context.

### When the shortcut may be acceptable

Acceptable when a short-lived spike unlocks a high-value release and the work remains reviewable and bounded.

### When it becomes a bad trade

Bad when spend hides wrong scope, weak evidence, repeated speculative fixes, or permanent dependence on high-usage modes.

### Risk profile

- Probability: medium for disciplined workflows; high for ambiguous tasks and parallel cloud work.
- Impact: low for occasional prototypes; high for teams, APIs, automations, and usage-based workspaces.
- Recoverability: budget is not recoverable; code changes may be recoverable if isolated.

### Blast radius

Usage burn can create sunk-cost pressure: users keep accepting poor outputs because they already spent credits, time, or team quota.

### Minimum guardrails

- use dated pricing snapshots for exact values
- cap retries
- split exploration from implementation
- avoid context dumps
- review burn after repeated failures

### Recovery plan

1. Stop the loop.
2. Summarize what has been tried and what evidence exists.
3. Shrink context to the smallest relevant packet.
4. Switch to read-only diagnosis or a smaller slice.
5. Update prompt templates to include burn controls.

## Budget and Constraint Notes

### Cheapest reliable path

use curated context and targeted checks before buying more attempts.

### Fastest high-usage path

spend on high-confidence, well-sliced work; do not parallelize ambiguity.

### Low-attention path

low-attention tasks need stop conditions so they do not quietly run broad loops.

### Production-quality path

budget for verification and review, not just code generation.

### Prototype versus production

prototypes can spend to explore; production should spend to reduce risk.

### Maintenance phase

keep recurring burn low by encoding stable commands, repo rules, and review packets in reusable guidance.

## Stable Core

- usage cost is controlled by task shape before it is controlled by plan choice
- context dumping and speculative retries burn budget without increasing certainty
- exact limits and rates are volatile and belong in snapshots

## Volatile Surface

- current Codex plan limits
- credit rates and token accounting
- model availability and speed settings
- usage dashboard behavior
- shared-limit policy across agentic features

Review volatile details against official sources or dated pricing snapshots before freezing commands, UI labels, model choices, plan packaging, context limits, feature availability, exact prices, or exact limits.

## Obsolescence Watch

- Codex cost becomes negligible or fully predictable across all surfaces and plans

## Evidence and Sources

- `openai.codex.pricing` — Official OpenAI Codex pricing and usage-limit anchor; exact values are volatile and belong in snapshots.
- `openai.help.codex_rate_card` — Official OpenAI Help Center rate-card anchor for token/credit usage mechanics; exact values are volatile.
- `vcb.pricing_snapshot.openai_codex` — Dated VCB pricing snapshot for exact OpenAI/Codex pricing and limit observations captured on 2026-06-09.
- `openai.codex.best_practices` — Official OpenAI Codex guidance for constraints, done-when criteria, planning, reusable guidance, testing, review, permissions, and validation.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable engineering control loops, risk, review, recovery, and constraint management.

## Related Topics

- `vcb.chapter.budget_aware_codex_workflows`
- `vcb.chapter.cost_benefit_analysis`
- `vcb.pricing_snapshot.openai_codex`
- `vcb.constraints.operating_mode`
- `vcb.constraints.scope_budget`
- `vcb.constraints.attention_budget`
- `vcb.prompting.context_management`
- `vcb.failure.context_pollution`

<!-- VCB:STOP_RETRIEVAL reason="constraint_topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.constraints.usage_burn -->
