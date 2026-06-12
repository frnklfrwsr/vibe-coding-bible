<!-- VCB:BEGIN_TOPIC id=vcb.concepts.typecheck version=0.1.0 -->
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
id: vcb.concepts.typecheck
title: Typecheck
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
- vcb.shortcut.ignoring_lint_typecheck
durable_principles:
- typechecks catch classes of mistakes before runtime
- types are contracts about data shape
- passing typecheck is not proof of behavior
likely_to_change:
- type-system syntax
- compiler options
- framework-generated types
obsolete_when:
- dynamic behavior replaces static consistency checks entirely
related_topics:
- vcb.concepts.test
- vcb.concepts.lint
- vcb.concepts.api_basics
- vcb.chapter.writing_updating_tests
---

> Summary:
> A typecheck verifies that values are used consistently: strings as strings, numbers as numbers, promises as promises, and API shapes as expected.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.typecheck.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A typecheck is a robot grammar check for data. It asks whether the code is using values in ways that make sense: not calling string methods on numbers, not ignoring missing fields, not treating a promise like its result.

### Why it matters

Codex often makes plausible code with wrong data shapes. Typecheck catches many of those mistakes before the app runs.

### The mental model

Types are labels on boxes. If a box says “eggs,” code should not treat it like “hammer.”

### What good looks like

- changed code passes project typecheck
- types reflect real API/data shapes
- Codex does not use `any` to silence errors
- old unrelated type errors are separated from new ones

### What bad looks like

- Codex adds `any` everywhere
- type errors ignored as “existing” without proof
- typecheck skipped before CI
- types pass but behavior is still untested

### Minimal example

If an API may return `null`, the type should force the UI to handle the missing value instead of crashing later.

### Checklist

- Run the typecheck command if available.
- Separate old errors from new errors.
- Reject broad `any` or cast-based silencing.
- Remember typecheck is not a behavior test.
<!-- VCB:END_SECTION id=vcb.concepts.typecheck.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.typecheck.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Make typecheck a cheap guardrail without overselling it as full correctness.

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
Run the project typecheck and separate pre-existing errors from errors caused by this change. Do not silence errors with `any` or casts without explaining why.
```

```text
Explain this type error in plain language and fix the data-shape mismatch rather than bypassing it.
```

### Red flags to call out directly

- new `any`/casts to make errors disappear
- typecheck not run after API/schema changes
- generated types ignored
- type errors dismissed without baseline

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.typecheck.ai_coach -->

## Shortcut Reality

### The ideal practice

Run typecheck and fix changed-code errors.

### What users often do instead

Users skip typecheck because the app appears to work.

### When the shortcut may be fine

Tiny prototype with no CI and no critical data, if manual path works.

### When the shortcut is a bad idea

API, database, auth, payments, shared libraries, or CI-gated repos.

### Risk profile

- Probability of failure: medium
- Impact if it fails: medium
- Ease of recovery: high before merge
- Blast radius: changed data paths
- Skill needed to recover: type-system basics
- Hidden cost: runtime bugs from ignored compile warnings

### Minimum guardrails

- Run typecheck.
- Do not silence with `any`.
- Document pre-existing errors.
- Pair with tests for behavior.

### Recovery plan

Revert unsafe casts, run typecheck, fix underlying data shape, and add an acceptance check for the runtime path.

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

- typechecks catch classes of mistakes before runtime
- types are contracts about data shape
- passing typecheck is not proof of behavior

## Volatile Surface

- type-system syntax
- compiler options
- framework-generated types

## Obsolescence Watch

Obsolete or review this topic when:

- dynamic behavior replaces static consistency checks entirely

## Evidence and Sources

- `typescript.docs.basic_types` — source anchor for this concept.
- `typescript.docs.home` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.test
- vcb.concepts.lint
- vcb.concepts.api_basics
- vcb.chapter.writing_updating_tests

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.typecheck -->
