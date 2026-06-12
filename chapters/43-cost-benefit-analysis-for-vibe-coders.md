<!-- VCB:BEGIN_TOPIC id=vcb.chapter.cost_benefit_analysis version=0.1.0 -->
---
id: vcb.chapter.cost_benefit_analysis
title: "Chapter 43 — Cost-Benefit Analysis for Vibe Coders"
type: chapter
chapter_number: 43
version: 0.1.0
last_verified: '2026-06-09'
next_review_due: '2026-09-09'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- all project types

source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE

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

shortcut_profiles:
- vcb.shortcut.buying_tools_as_progress
- vcb.shortcut.tool_sprawl
- vcb.shortcut.over_optimizing_for_price
- vcb.shortcut.skipping_maintenance_cleanup

durable_principles:
- Total cost includes time, attention, maintenance, debugging, migration, and recovery.
- A tool must help a milestone or reduce repeated pain.
- Cheap tools can be expensive if they create debugging or migration burden.

likely_to_change:
- product packaging
- current pricing and limits
- model-specific behavior

obsolete_when:
- Codex product behavior or pricing model materially changes.

related_topics:
- vcb.chapter.tool_stack_catalog
- vcb.chapter.budget_aware_codex_workflows
- vcb.chapter.build_phase_vs_maintenance_phase
---

> Summary:
> Cost is not just the monthly invoice. For vibe coders, the real bill includes setup, debugging, maintenance, lock-in, migration, security, review, and recovery.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.cost_benefit_analysis.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Cost-benefit analysis means asking whether a tool, workflow, plan, or shortcut is worth what it will cost you.

The visible price is only one part. The real cost includes:

- monthly bill;
- setup time;
- learning curve;
- debugging time;
- maintenance work;
- lock-in;
- migration pain;
- security risk;
- review burden;
- recovery cost after mistakes.

### The useful question

Do not ask:

```text
Is this tool good?
```

Ask:

```text
What milestone does this tool help me reach, and what new burden does it add?
```

### Cost-benefit table

| Factor | Ask this |
|---|---|
| Monthly cost | What happens at 10x users or 10x usage? |
| Setup cost | Can I set this up without losing a day? |
| Maintenance cost | Who updates it when it breaks? |
| Debugging cost | Can Codex and I inspect failures clearly? |
| Migration cost | How hard is it to leave? |
| Lock-in risk | Is the data/config portable? |
| Hidden cost | Are usage spikes, seats, logs, bandwidth, or API calls billed? |
| Security cost | Does it touch secrets, auth, user data, or payments? |
| Codex integration value | Can Codex use logs, docs, APIs, or config to help? |

### Three decisions

1. **Buy now:** the tool unlocks the next milestone or removes repeated pain.
2. **Delay:** the tool might help later, but not yet.
3. **Avoid:** the tool adds more burden than value for this project.

### Cost-benefit prompt

```text
Evaluate whether I should add this tool/workflow.

Tool/workflow:
Milestone it should help:
Current pain:
Budget:
Team size:
Production risk:
Alternatives:

Return:
- buy now / delay / avoid,
- setup cost,
- maintenance cost,
- debugging cost,
- lock-in risk,
- hidden cost risk,
- safer cheaper alternative,
- what would make the decision change.
```

<!-- VCB:END_SECTION id=vcb.chapter.cost_benefit_analysis.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.cost_benefit_analysis.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Move the human from feature desire to total-cost reasoning.

### Diagnostic questions

- What problem repeats often enough to justify a tool?
- Is the current pain bigger than the setup and maintenance cost?
- Can the user afford the human attention cost, not just the subscription?
- Does the tool create data, secrets, auth, billing, or deploy risk?

### Useful metaphor

A cheap printer with expensive ink is not cheap. Many developer tools work the same way.

### Coaching tactics

- Push for delay when the milestone is vague.
- Recommend manual/Markdown/local alternatives for early prototypes.
- Recommend paid tooling when it removes repeated operational pain or reduces production risk.
- Ask for exit criteria: when will the user remove or replace the tool?

### Red flags

- “Everyone uses this stack.”
- “It has a free tier” as the only reason.
- “Codex can wire it up” with no maintenance plan.
- “We might need scale later” before one user path works.

<!-- VCB:END_SECTION id=vcb.chapter.cost_benefit_analysis.ai_coach -->

## Shortcut Reality

### The ideal practice

Evaluate total cost before adding a paid tool, integration, workflow, or AI plan.

### What users often do instead

They buy tools because the monthly price looks small or because a dashboard makes progress feel tangible.

### When the shortcut may be fine

Impulse tool use can be acceptable in throwaway demos or learning projects where the outcome is knowledge, not maintainable infrastructure.

### When the shortcut is a bad idea

It is a bad idea when the tool becomes part of auth, payments, user data, deployments, CI secrets, or core architecture before the milestone is proven.

### Risk profile

- Probability of failure: medium.
- Impact if it fails: recurring cost, migration pain, production instability.
- Ease of recovery: high before data/users, lower after integration.
- Blast radius: grows with credentials and vendor lock-in.
- Hidden cost: invoices, debugging, complexity, training Codex on more context.

### Minimum guardrails

- Write the milestone first.
- Require one cheaper alternative.
- Define a removal condition.
- Store exact pricing in a snapshot.
- Add no secrets until the tool is approved.

### Recovery plan

If a tool is not earning its keep, freeze new usage, export data/config if needed, remove credentials, simplify the stack, and update docs/AGENTS so Codex stops assuming the tool exists.

## Budget and Constraint Notes

### Cheapest reliable path

Use manual processes, simple files, platform defaults, and fewer services until repeated pain justifies a tool.

### Fastest high-usage path

Spend usage on comparisons, migration plans, and setup docs, but do not let Codex execute purchases or credential wiring unattended.

### Low-attention path

Low-attention tool decisions should be report-only. Human approval is required for billing, auth, payments, secrets, and deployments.

### Production-quality path

Require official docs, owner, backup/export path, monitoring, security review, and a cost watch.

## Stable Core

Total-cost reasoning is stable. Tool markets change, but setup cost, maintenance cost, lock-in, hidden costs, and opportunity cost remain the right evaluation axes.

## Volatile Surface

Tool pricing, market categories, product capabilities, free-tier limits, seat models, and AI integrations are volatile.

## Obsolescence Watch

Review when tool-category pricing shifts, major vendors change packaging, or the project’s phase changes from prototype to production/maintenance.

## Evidence and Sources

- `openai.codex.pricing` — official OpenAI anchor for Codex cost volatility
- `github.docs.actions_billing` — official GitHub source for CI billing volatility
- `vercel.pricing` — official Vercel pricing anchor
- `supabase.pricing` — official Supabase pricing anchor
- `stripe.pricing` — official Stripe pricing anchor
- `posthog.pricing` — official PostHog pricing anchor

## Related Topics

- `vcb.chapter.tool_stack_catalog`
- `vcb.chapter.budget_aware_codex_workflows`
- `vcb.chapter.build_phase_vs_maintenance_phase`
- `vcb.chapter.dependency_package_framework_decisions`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.cost_benefit_analysis -->
