<!-- VCB:BEGIN_TOPIC id=vcb.concepts.observability version=0.1.0 -->
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
id: vcb.concepts.observability
title: Observability
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
- vcb.shortcut.skipping_maintenance_cleanup
- vcb.shortcut.accepting_looks_done
durable_principles:
- production needs evidence after deployment
- logs/metrics/traces/errors answer different questions
- observability should be designed before incidents when possible
likely_to_change:
- vendor dashboards
- instrumentation libraries
- retention/pricing
obsolete_when:
- production systems stop failing in unknown ways
related_topics:
- vcb.concepts.ci
- vcb.concepts.rollback
- vcb.concepts.feature_flag
- vcb.chapter.tool_stack_catalog
---

> Summary:
> Observability is how you understand what happened inside a running system by looking at outputs such as logs, metrics, traces, errors, and events.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.observability.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Observability is your ability to answer “what happened?” after your app is running. It includes logs, error reports, metrics, traces, audit events, and dashboards.

### Why it matters

Without observability, Codex may “fix” production issues blindly. You need evidence: which users were affected, which endpoint failed, when it started, what changed, and whether the fix worked.

### The mental model

Observability is the airplane’s instrument panel and flight recorder. You do not want to build it after the emergency starts.

### What good looks like

- errors include useful context without secrets
- important flows emit logs/events
- metrics show rate/latency/error changes
- deploys can be correlated with incidents
- alerts are actionable

### What bad looks like

- only `console.log` in dev
- logs contain secrets
- no way to know if production fix worked
- alerts are noisy or absent

### Minimal example

If checkout failures spike after deploy, observability should show error rate, affected route, recent release, stack trace, and sample request context without exposing card data.

### Checklist

- Log enough to debug, not secrets.
- Track errors and important business events.
- Correlate deploys with failures.
- Add instrumentation around risky features.
<!-- VCB:END_SECTION id=vcb.concepts.observability.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.observability.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach observability as production evidence and connect it to rollback/recovery.

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
Identify what evidence we would need if this failed in production: logs, metrics, traces, errors, audit events, and user-visible symptoms.
```

```text
Add minimal observability for this risky path without logging secrets or personal data.
```

### Red flags to call out directly

- no production evidence for “fixed” claim
- logs reveal secrets/PII
- alert fatigue
- Codex adds logging but no error boundary or metric

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.observability.ai_coach -->

## Shortcut Reality

### The ideal practice

Add minimal useful evidence before relying on production behavior.

### What users often do instead

Users ship and wait for complaints.

### When the shortcut may be fine

Tiny local/personal tools where failure is obvious and harmless.

### When the shortcut is a bad idea

Production, payments, auth, background jobs, integrations, performance-sensitive paths, or intermittent bugs.

### Risk profile

- Probability of failure: medium
- Impact if it fails: high during incidents
- Ease of recovery: medium if evidence exists, low if blind
- Blast radius: production users and incident response
- Skill needed to recover: debugging/ops literacy
- Hidden cost: slow incident diagnosis

### Minimum guardrails

- Do not log secrets.
- Capture errors and key events.
- Correlate deploys.
- Keep alerts actionable.
- Add dashboards only when they answer decisions.

### Recovery plan

Add missing evidence, roll back if impact is high, inspect logs/errors/traces, fix the cause, and document the incident signals needed next time.

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

- production needs evidence after deployment
- logs/metrics/traces/errors answer different questions
- observability should be designed before incidents when possible

## Volatile Surface

- vendor dashboards
- instrumentation libraries
- retention/pricing

## Obsolescence Watch

Obsolete or review this topic when:

- production systems stop failing in unknown ways

## Evidence and Sources

- `opentelemetry.docs.what_is_opentelemetry` — source anchor for this concept.
- `opentelemetry.docs.observability_primer` — source anchor for this concept.
- `sentry.docs.platform` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.ci
- vcb.concepts.rollback
- vcb.concepts.feature_flag
- vcb.chapter.tool_stack_catalog

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.observability -->
