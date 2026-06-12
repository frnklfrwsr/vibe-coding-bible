<!-- VCB:BEGIN_TOPIC id=vcb.concepts.feature_flag version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
review_cadence: annual
audiences:
- human
- ai_coach
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- Human software work
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
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.concepts.feature_flag
title: Feature Flag
type: concept
next_review_due: '2027-06-09'
source_status:
  official_openai: false
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: concept definition anchored to official/vendor/expert sources; Codex-specific
  risk guidance is maintainer synthesis
stability:
  principle: CORE_ENGINEERING
  surface: STABLE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.manual_testing_only
- vcb.shortcut.generated_prototype_as_production_foundation
durable_principles:
- feature flags can reduce deployment blast radius
- flags add complexity and need cleanup
- flags are not a substitute for correct authorization or security
likely_to_change:
- flag platforms
- SDK APIs
- targeting/rules UI
obsolete_when:
- software deployments become perfectly risk-free without conditional behavior
related_topics:
- vcb.concepts.rollback
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.chapter.first_serious_app
---

> Summary:
> A feature flag is a switch that lets code exist before everyone sees or uses it, reducing release risk when managed carefully.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.feature_flag.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A feature flag is a switch in code or configuration that controls whether a feature is active. It can let you deploy code while keeping the feature hidden, roll out gradually, or disable a risky path quickly.

### Why it matters

Flags are useful for reducing blast radius. They are also debt. A forgotten flag can split the app into confusing versions forever.

### The mental model

A feature flag is a light switch installed before the room opens to the public. Useful during construction, but bad if no one remembers which switch controls what.

### What good looks like

- flag has owner and removal plan
- default state is safe
- flag protects user-visible behavior, not data integrity alone
- tests cover enabled and disabled paths when risk requires it

### What bad looks like

- flag used as permanent architecture
- flag hides insecure backend path
- no one knows when to remove it
- many flags interact in untested ways

### Minimal example

A new billing screen can be deployed behind `newBillingUI=false`, then enabled for internal testers before all users.

### Checklist

- Name the flag purpose.
- Set safe default.
- Know who can enable it.
- Test both states for risky paths.
- Schedule cleanup.
<!-- VCB:END_SECTION id=vcb.concepts.feature_flag.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.feature_flag.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach flags as temporary risk controls, not permanent product logic sprawl.

### Diagnose the human’s current model

- What part of the concept is the human treating as magic?
- What evidence would show this is working?
- What is the risky production version of this concept?
- Can the human name the boundary, data, or check involved?

### Explanation strategy

Start with a concrete everyday analogy, then tie it to the exact files, commands, checks, or data flow Codex is likely to touch. Keep the explanation practical and risk-scaled.

### Useful metaphors

- Use one simple metaphor, then return to the actual repo.
- Treat the concept as an operational control, not trivia.

### Coaching tactics

- Ask Codex to inspect current project conventions before editing.
- Convert the concept into a small checklist.
- Escalate when the concept touches production, secrets, data, auth, payments, or CI.

### Prompt patterns

```text
Add this feature behind a small, named flag with safe default off. Include where it is checked, how it is enabled, and when it should be removed.
```

```text
Review existing feature flags and classify which are release flags, operational flags, experiment flags, or stale flags.
```

### Red flags to call out directly

- flag controls only frontend while backend action remains open
- no cleanup plan
- flag name unclear
- authorization confused with feature visibility

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.feature_flag.ai_coach -->

## Shortcut Reality

### The ideal practice

Use flags to reduce rollout risk while keeping tests and cleanup.

### What users often do instead

Users add flags everywhere to avoid making release decisions.

### When the shortcut may be fine

Short-lived prototype/demo switch or internal preview.

### When the shortcut is a bad idea

Auth/security/payment enforcement, data migrations, or permanent business rules hidden behind vague flags.

### Risk profile

- Probability of failure: medium
- Impact if it fails: medium/high
- Ease of recovery: high if flag works, low if backend unsafe
- Blast radius: rollout population
- Skill needed to recover: release/config discipline
- Hidden cost: stale conditional complexity

### Minimum guardrails

- Safe default.
- Owner and removal date.
- Server-side enforcement for security.
- Test enabled/disabled.
- Document rollout/rollback.

### Recovery plan

Turn off flag if safe, revert code if flag is broken, remove stale paths after rollout, and add cleanup tracking.

### AI coach guidance

Do not lecture first. Classify the project risk, then move the human one guardrail level up. If this touches real users, secrets, money, auth, production data, migrations, or CI credentials, be direct and require evidence before acceptance.

## Budget and Constraint Notes

### Cheapest reliable path

Use this card to clarify the concept before asking Codex to edit. Spend one short inspection or explanation pass, then make the smallest verified change.

### Fastest high-usage path

Run a plan/implementation/review loop, but keep diffs isolated and require Codex to report the concept-specific risk areas before acceptance.

### Low-attention path

Low-attention work needs stronger written constraints, not broader trust. Require a final report with files changed, checks run, known gaps, and any concept-specific risk.

### Production-quality path

Use the concept as a release gate: define the boundary, verify the important cases, review the diff, and preserve rollback/recovery options.

## Stable Core

- feature flags can reduce deployment blast radius
- flags add complexity and need cleanup
- flags are not a substitute for correct authorization or security

## Volatile Surface

- flag platforms
- SDK APIs
- targeting/rules UI

## Obsolescence Watch

Obsolete or review this topic when:

- software deployments become perfectly risk-free without conditional behavior

## Evidence and Sources

- `openfeature.docs_intro` — official OpenFeature source anchor for feature flags as runtime-controlled behavior and vendor-agnostic flag evaluation.
- `martin_fowler.feature_toggles` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.rollback
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.chapter.first_serious_app

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.feature_flag -->
