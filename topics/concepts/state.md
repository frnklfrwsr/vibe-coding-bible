<!-- VCB:BEGIN_TOPIC id=vcb.concepts.state version=0.1.0 -->
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
id: vcb.concepts.state
title: State
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
- vcb.shortcut.accepting_looks_done
durable_principles:
- state must have a clear owner
- duplicate or stale state causes bugs
- Codex needs to distinguish UI state from server truth
likely_to_change:
- framework state APIs
- client cache libraries
- server component patterns
obsolete_when:
- apps stop needing changing memory
related_topics:
- vcb.concepts.frontend_backend
- vcb.concepts.async
- vcb.concepts.api_basics
- vcb.chapter.frontend_work
---

> Summary:
> State is what an app remembers right now: form values, logged-in user, selected tab, server data, loading status, and cached results.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.state.human -->
## 1. For the Human: Plain-Language Concept

### What this means

State is the app’s memory. It is why a form remembers what you typed, why a spinner appears while loading, why a cart count changes, and why a logged-in user stays logged in while moving pages.

### Why it matters

State bugs feel spooky: old data appears, buttons stay disabled, a success message lies, or two parts of the page disagree. Codex often patches the visible symptom unless you name the state owner.

### The mental model

State is a whiteboard in the app’s head. If two whiteboards disagree, users see weird behavior.

### What good looks like

- one source of truth is clear
- loading/error/empty/success states are represented
- server data is refreshed when needed
- form state is reset intentionally

### What bad looks like

- duplicate copies drift apart
- UI says saved before server confirms
- stale cached data is shown as fresh
- Codex adds random state instead of fixing ownership

### Minimal example

A todo item can exist in server state from the database and UI state in the current form. Typing into the form should not pretend the database has already changed.

### Checklist

- Name the state owner.
- List loading/error/empty/success states.
- Avoid duplicate derived state.
- Refresh or invalidate server data after mutation.
<!-- VCB:END_SECTION id=vcb.concepts.state.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.state.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Prevent “add more state” patches by teaching ownership and lifecycle.

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
Map the state for this screen: owner, initial value, updates, reset condition, server sync, and error handling. Do not edit yet.
```

```text
Fix this state bug by identifying the source of truth first. Avoid adding duplicate state unless justified.
```

### Red flags to call out directly

- extra state variable added without deleting old source
- no error/loading state
- success shown before server confirms
- state reset missing after navigation

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.state.ai_coach -->

## Shortcut Reality

### The ideal practice

Use one clear source of truth and handle lifecycle states explicitly.

### What users often do instead

Users click around once and accept the UI if it looks correct.

### When the shortcut may be fine

Small local visual tweak with no server data.

### When the shortcut is a bad idea

Checkout, auth, permissions, data edits, collaborative screens, or production flows.

### Risk profile

- Probability of failure: medium
- Impact if it fails: medium/high depending on data
- Ease of recovery: medium
- Blast radius: screen, cache, user decisions
- Skill needed to recover: frontend/data-flow debugging
- Hidden cost: intermittent bugs

### Minimum guardrails

- Create a state matrix.
- Test loading, error, empty, success.
- Avoid duplicate state.
- Use existing cache/update conventions.

### Recovery plan

Revert symptom patches, trace state ownership, remove duplicate state, and add a regression check for the broken state transition.

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

- state must have a clear owner
- duplicate or stale state causes bugs
- Codex needs to distinguish UI state from server truth

## Volatile Surface

- framework state APIs
- client cache libraries
- server component patterns

## Obsolescence Watch

Obsolete or review this topic when:

- apps stop needing changing memory

## Evidence and Sources

- `react.docs.state_memory` — source anchor for this concept.
- `react.docs.managing_state` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.frontend_backend
- vcb.concepts.async
- vcb.concepts.api_basics
- vcb.chapter.frontend_work

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.state -->
