<!-- VCB:BEGIN_TOPIC id=vcb.concepts.async version=0.1.0 -->
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
id: vcb.concepts.async
title: Async and Timing
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
- vcb.shortcut.debugging_without_repro
- vcb.shortcut.manual_testing_only
durable_principles:
- async code requires explicit loading/error/order handling
- race conditions happen when timing assumptions are false
- Codex should reproduce timing bugs before patching broad logic
likely_to_change:
- language async APIs
- framework data-fetching patterns
- job queue tooling
obsolete_when:
- programs stop waiting on external work
related_topics:
- vcb.concepts.state
- vcb.concepts.api_basics
- vcb.concepts.test
- vcb.chapter.debugging_with_reproduction
---

> Summary:
> Async work happens later: network requests, file reads, jobs, timers, promises, and background tasks can finish after other code has moved on.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.async.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Async means “not right now.” Your app asks for something, then continues while waiting. Later, the result succeeds, fails, or arrives too late to matter.

### Why it matters

Many bugs happen because Codex writes happy-path code that assumes data is already available or requests return in the order users expect. Real networks and jobs do not behave that politely.

### The mental model

Async is ordering takeout. You place the order now, but food arrives later. You need a plan for waiting, cancellation, wrong order, and delivery after you already left.

### What good looks like

- loading states exist
- errors are handled
- stale responses are ignored or reconciled
- operations are retried or cancelled intentionally

### What bad looks like

- `undefined` crashes before data loads
- two requests race and old data wins
- errors disappear silently
- Codex patches with arbitrary delays

### Minimal example

If a user searches “cat” then quickly “car,” the slower “cat” response should not overwrite the newer “car” result.

### Checklist

- Identify what completes later.
- Handle pending, success, failure, and cancellation/stale result.
- Avoid arbitrary sleeps.
- Reproduce timing bug when possible.
<!-- VCB:END_SECTION id=vcb.concepts.async.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.async.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach async as timing uncertainty and stop guess patches like sleeps/timeouts.

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
Explain the async flow for this bug: what starts, what waits, what can fail, and what happens if results arrive out of order.
```

```text
Reproduce the timing issue before patching. Avoid arbitrary sleeps; use the project’s existing async/cancellation pattern.
```

### Red flags to call out directly

- `setTimeout` used as a fix
- missing loading/error paths
- old response overwrites new state
- Codex cannot explain event order

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.async.ai_coach -->

## Shortcut Reality

### The ideal practice

Represent pending/failure/stale states and verify the timing-sensitive path.

### What users often do instead

Users patch from the visible symptom without reproducing the order/timing problem.

### When the shortcut may be fine

Tiny prototype where a refresh is acceptable.

### When the shortcut is a bad idea

Payments, data writes, background jobs, retries, uploads, or collaborative state.

### Risk profile

- Probability of failure: medium/high
- Impact if it fails: medium/high
- Ease of recovery: medium
- Blast radius: user-visible stale data or duplicate actions
- Skill needed to recover: async/debugging skill
- Hidden cost: flaky bugs

### Minimum guardrails

- Capture repro steps.
- Log event order.
- Avoid sleeps.
- Handle stale/cancelled results.
- Add regression test if feasible.

### Recovery plan

Roll back speculative timing fixes, reproduce with logs, then patch ordering/cancellation/error handling directly.

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

- async code requires explicit loading/error/order handling
- race conditions happen when timing assumptions are false
- Codex should reproduce timing bugs before patching broad logic

## Volatile Surface

- language async APIs
- framework data-fetching patterns
- job queue tooling

## Obsolescence Watch

Obsolete or review this topic when:

- programs stop waiting on external work

## Evidence and Sources

- `mdn.js.promises` — source anchor for this concept.
- `mdn.async_javascript` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.state
- vcb.concepts.api_basics
- vcb.concepts.test
- vcb.chapter.debugging_with_reproduction

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.async -->
