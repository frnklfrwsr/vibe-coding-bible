<!-- VCB:BEGIN_TOPIC id=vcb.concepts.test version=0.1.0 -->
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
id: vcb.concepts.test
title: Test
type: concept
next_review_due: '2027-06-09'
source_status:
  official_openai: true
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
- vcb.shortcut.skipping_tests
- vcb.shortcut.manual_testing_only
durable_principles:
- tests are evidence, not decoration
- weak tests can produce false confidence
- Codex must not weaken tests to make code pass
likely_to_change:
- framework test syntax
- runner commands
- coverage tooling
obsolete_when:
- software behavior can be proven without executable checks
related_topics:
- vcb.concepts.ci
- vcb.concepts.typecheck
- vcb.concepts.lint
- vcb.chapter.writing_updating_tests
---

> Summary:
> A test is an executable expectation: it proves a specific behavior still works, or fails when that behavior breaks.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.test.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A test is code that checks whether your code behaves as expected. Good tests are tripwires: if Codex breaks important behavior later, the tripwire snaps.

### Why it matters

Codex can write code quickly, which makes tests more important, not less. Without tests, speed just creates more places for hidden breakage.

### The mental model

A test is a smoke alarm. It does not prevent fire, but it tells you when something important is burning.

### What good looks like

- test name says the behavior
- test fails before the fix and passes after
- test checks user-visible behavior or critical logic
- test is not just asserting implementation details

### What bad looks like

- test only checks that a component renders
- Codex deletes or weakens assertions
- mocks remove the behavior being tested
- tests pass but prove nothing important

### Minimal example

A bug test should reproduce the bug. If deleting the fix does not make the test fail, the test is weak.

### Checklist

- Ask what behavior must be protected.
- Prefer regression tests for real bugs.
- Review test diffs carefully.
- Do not accept deleted/loosened assertions without reason.
<!-- VCB:END_SECTION id=vcb.concepts.test.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.test.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach tests as executable acceptance criteria and watch for Codex weakening the guardrails.

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
Add a regression test that fails for the current bug and passes after the fix. Do not weaken existing assertions.
```

```text
Review these tests: what behavior do they prove, what do they miss, and are any assertions too weak?
```

### Red flags to call out directly

- tests changed more than production code
- assertions removed
- snapshot updated blindly
- test mocks out the failing behavior

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.test.ai_coach -->

## Shortcut Reality

### The ideal practice

Run or add the smallest meaningful test for risky behavior.

### What users often do instead

Users click once manually and accept the change.

### When the shortcut may be fine

Low-risk prototype, copy tweak, local-only visual experiment.

### When the shortcut is a bad idea

Auth, billing, migrations, data deletion, API contracts, production fixes, or recurring bugs.

### Risk profile

- Probability of failure: medium
- Impact if it fails: project-dependent
- Ease of recovery: high if caught before merge, lower after release
- Blast radius: behavior covered by tests
- Skill needed to recover: test reading and debugging
- Hidden cost: false confidence from weak tests

### Minimum guardrails

- Commit first.
- Run relevant tests.
- Add regression test for real bug.
- Review test diff for weakening.
- Manual-check exact path if no tests exist.

### Recovery plan

Restore weakened tests, reproduce the bug, add meaningful assertion, and rerun checks before accepting the fix.

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

- tests are evidence, not decoration
- weak tests can produce false confidence
- Codex must not weaken tests to make code pass

## Volatile Surface

- framework test syntax
- runner commands
- coverage tooling

## Obsolescence Watch

Obsolete or review this topic when:

- software behavior can be proven without executable checks

## Evidence and Sources

- `openai.codex.workflows` — source anchor for this concept.
- `jest.docs_getting_started` — official Jest source anchor for JavaScript test-runner setup and test concept terminology.
- `openai.codex.guide_ai_native_engineering_team` — source anchor for this concept.
- `github.docs.actions_ci` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.ci
- vcb.concepts.typecheck
- vcb.concepts.lint
- vcb.chapter.writing_updating_tests

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.test -->
