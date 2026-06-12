<!-- VCB:BEGIN_TOPIC id=vcb.chapter.writing_updating_tests version=0.1.0 -->
---
id: vcb.chapter.writing_updating_tests
title: "Chapter 14 — Writing and Updating Tests with Codex"
type: chapter
chapter_number: 14
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-12-08'
review_cadence: semiannual

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- CI
- unit tests
- integration tests
- end-to-end tests

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE

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
- vcb.shortcut.skipping_tests
- vcb.shortcut.manual_testing_only
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.ignoring_lint_typecheck

durable_principles:
- Tests are executable expectations, not decoration.
- Tests should prove user-visible behavior or important technical contracts.
- Codex must not weaken tests to make implementation pass.
- Bug fixes should add or update regression tests when feasible.

likely_to_change:
- Codex test-generation quality
- native test-running integrations
- CI and non-interactive Codex workflows
- framework-specific test conventions

obsolete_when:
- Codex can reliably infer meaningful test intent, detect weak tests, and validate behavior without explicit human acceptance criteria.
- Official Codex guidance no longer treats tests, lint, typecheck, build, and review as verification signals.

related_topics:
- vcb.chapter.acceptance_criteria
- vcb.chapter.debugging_with_reproduction
- vcb.chapter.feature_slicing
- vcb.chapter.git_discipline
- vcb.concepts.diff
- vcb.concepts.recoverability
- vcb.workflow.testing
- vcb.failure.weakened_tests
---

> Summary:
> Tests turn behavior into executable evidence. Codex can write tests quickly, but the human and AI coach must ensure those tests prove the right thing.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.writing_updating_tests.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A test is code that checks whether other code behaves as expected.

Think of tests as tripwires. If future changes break important behavior, the test should trip before users do.

Codex can write tests fast. That is useful. It is also risky if the tests are weak.

A weak test only proves that code runs. A useful test proves a behavior you care about.

### Why it matters

Codex can make code look correct. Tests help prove whether it is correct.

Good tests help with:

- bug fixes,
- feature slices,
- refactors,
- dependency changes,
- production releases,
- future Codex sessions.

Bad tests create false confidence. A passing test suite that proves nothing is worse than no test in some cases, because it makes people less cautious.

### Common test types

| Test type | Plain-language meaning | Good for |
|---|---|---|
| Unit test | checks one function or small unit | rules, calculations, pure logic |
| Integration test | checks multiple pieces together | API + database, service boundaries |
| End-to-end test | acts like a user through the app | critical user flows |
| Regression test | proves a bug stays fixed | bug fixes and edge cases |
| Snapshot test | compares output to stored output | stable rendered output or generated structures |
| Manual check | human runs exact path | prototypes, UI taste, low-risk changes |

You do not need every test type for every task. You need the smallest test that proves the important behavior.

### Good test prompt

```text
Write or update tests for this behavior.

Behavior to prove:
A user cannot accept an expired invite token.

Context:
Use existing test conventions near tests/invites.

Constraints:
- do not weaken or delete existing assertions,
- prefer behavior-level assertions over implementation details,
- keep the public API shape unchanged,
- if a test is not feasible, explain why and give a manual check.

Done when:
The relevant test fails before the fix if possible, passes after the fix, and existing related tests still pass.
```

### Weak test patterns

Call out tests that:

- only check that a component renders,
- assert mocked functions were called without checking user behavior,
- delete assertions to pass,
- change expected output to match broken behavior,
- test implementation details instead of behavior,
- only cover the happy path,
- skip error, empty, loading, unauthorized, or invalid states,
- add brittle snapshots with no explanation.

### Regression tests

A regression test is a test for a bug that already happened.

Use it when:

- a real bug affected users,
- the failure could return,
- the behavior can be checked automatically,
- future Codex sessions may touch the same area.

Good bug-fix instruction:

```text
Add a regression test that fails on the current bug before applying the fix, if feasible. If not feasible, explain why and provide the closest useful check.
```

### Updating tests safely

Tests sometimes need updates when behavior intentionally changes. That is fine.

Danger signs:

- Codex deletes a failing test without explaining the intended behavior change.
- Codex changes the expected result without linking it to acceptance criteria.
- Codex weakens the assertion from specific behavior to “does not throw.”
- Codex skips or marks flaky tests without root cause.

When tests change, ask:

```text
Which tests changed, and why? Does each changed expectation reflect intended behavior or just make the suite pass?
```

### Minimum test discipline

For low-risk local work, a manual check may be enough.

For production, auth, billing, permissions, migrations, data deletion, or security-sensitive work, weak or absent tests are not a good trade. At minimum, require targeted automated checks plus diff review.
<!-- VCB:END_SECTION id=vcb.chapter.writing_updating_tests.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.writing_updating_tests.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that tests are executable acceptance criteria. Codex can generate them, but it must be guided toward meaningful behavior proof.

### Diagnose the human’s current model

Watch for:

- “Add tests” with no behavior specified.
- Tests written after implementation with no failure proof.
- Accepting tests that only assert mocks.
- Deleted or weakened assertions.
- No regression test for a real bug.
- Confusing coverage percentage with confidence.
- Treating manual UI clicking as enough for high-risk logic.

### Explanation strategy

Start with behavior, not framework mechanics.

Ask:

```text
What user-visible behavior or technical contract should this test prove?
What would count as a failure?
What edge case matters?
What existing test style should Codex follow?
```

Then turn answers into a test prompt.

### Useful metaphors

- **Tripwire:** a future break should trigger the test before users are hurt.
- **Smoke detector:** it does not prevent fire, but it makes failure visible.
- **Contract:** the test states what behavior the code owes you.

### Coaching tactics

When Codex writes tests, inspect the test intent:

- What behavior is proven?
- Would the test fail if the bug returned?
- Does it avoid implementation-only assertions?
- Did any old assertion get weaker?
- Did Codex add mocks that bypass the real risk?

For bug fixes, ask Codex for a “red/green” explanation:

```text
Would this test fail before the fix? If not, what does it prove?
```

For refactors, require characterization tests or unchanged behavior tests.

### Prompt patterns

#### Behavior-first test prompt

```text
Write tests for this behavior, not just this implementation.
Behavior:
[behavior]
Edge cases:
[edge cases]
Follow existing test conventions.
Do not delete or weaken existing assertions.
Run the smallest relevant test command and report the result.
```

#### Regression test prompt

```text
Before fixing, add or identify a regression test for this bug.
It should fail with the current bug if feasible.
After the fix, rerun the same test and report the command/output summary.
```

#### Test review prompt

```text
Review the test changes only.
Flag weak assertions, over-mocking, deleted coverage, behavior not proven, and expectations changed merely to pass.
```

### Red flags to call out directly

- “This test proves rendering, not behavior.”
- “Codex changed the expected value without explaining the product rule.”
- “The regression test would pass even if the bug came back.”
- “The test mocks away the failing dependency.”
- “A deleted assertion is not a fix.”

### Exercises

1. Ask Codex to write a test for one function using nearby conventions.
2. Ask what behavior the test proves.
3. Ask whether it would fail before the fix.
4. Ask Codex to review its own test for weakness.
5. Run the test or note why it could not run.
<!-- VCB:END_SECTION id=vcb.chapter.writing_updating_tests.ai_coach -->

## Shortcut Reality

### The ideal practice

Write or update tests that prove the intended behavior. For bugs, add a regression test when feasible. Run the relevant checks before accepting the diff.

### What users often do instead

They skip tests, rely on manual clicking, or accept Codex-generated tests that only prove the code can render or the mock was called.

### When the shortcut may be fine

Skipping automated tests or using manual checks may be acceptable when:

- the project is a throwaway prototype,
- the change is visual and low risk,
- the behavior is easy to manually verify,
- there are no real users/data/money involved,
- the diff is small and committed,
- the user understands the risk.

### When the shortcut is a bad idea

It is a bad trade when:

- auth, billing, permissions, migrations, data deletion, or security-sensitive behavior is involved,
- the bug has happened before,
- the behavior is hard to manually inspect,
- the change has hidden edge cases,
- multiple future Codex sessions will touch the area,
- the product has real users.

### Risk profile

- Probability of failure: medium when tests are skipped; high when tests are weak and confidence is high.
- Impact if it fails: low in demos, high in production.
- Ease of recovery: medium if caught before deploy; poor if bad data or money movement occurs.
- Blast radius: grows with persistent data, permissions, and payment flows.
- Skill needed to recover: medium to high.
- Hidden cost: false confidence and repeated regressions.

### Minimum guardrails

- Commit before changes.
- For low-risk work, manually test the exact changed flow.
- For bugs, add a regression test when feasible.
- Run the smallest relevant test/check.
- Review test diffs for weakened assertions.
- Do not skip tests for auth, payments, migrations, data deletion, or security-sensitive changes.

### Recovery plan

If weak tests let a bug through:

1. Reproduce the failure.
2. Add a regression test that catches it.
3. Fix the root cause.
4. Run the relevant test/check.
5. Review whether other tests were weakened.
6. Update durable guidance so Codex does not repeat the pattern.

### AI coach guidance

Say:

```text
The point is not to have more tests. The point is to have a tripwire for the behavior that matters. Ask Codex what this test would catch if the bug returned.
```

## Budget and Constraint Notes

### Cheapest reliable path

Ask for the smallest meaningful test or manual check. Do not spend usage generating broad test suites for low-risk changes.

### Fastest high-usage path

Use Codex to generate tests, run them, and then ask a fresh reviewer to inspect the test quality. This is worth it for risky code.

### Low-attention path

Low-attention work needs stronger automated checks. Manual-only verification is weak when the human plans to review later.

### Production-quality path

Require behavior-focused tests, targeted regression coverage for bugs, CI or local checks, diff review, and explicit final report of what was not tested.

## Stable Core

- Tests are behavior evidence.
- Weak tests create false confidence.
- Regression tests preserve lessons from bugs.
- Codex-generated tests still need human/coach review for meaning.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
- Native test-running features in Codex surfaces.
- Test-generation quality by model and framework.
- CI/non-interactive test automation mechanics.
- Framework-specific conventions and generated-test quality.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex gains stronger automatic test-quality evaluation, framework-aware regression generation, or reliable detection of weakened tests.

## Evidence and Sources

- `openai.codex.best_practices` — official current anchor for writing/updating tests, running relevant checks, lint/typecheck/build, behavior confirmation, and diff review.
- `openai.codex.workflows` — official current anchor for write-a-test workflows and bug-fix prompts that include regression tests when feasible.
- `openai.codex.guide_ai_native_engineering_team` — official current anchor for tests as an important source of truth when agents can generate code quickly.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for behavior-first tests, regression protection, and weak-test review.

## Related Topics

- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.debugging_with_reproduction`
- `vcb.chapter.feature_slicing`
- `vcb.chapter.git_discipline`
- `vcb.concepts.diff`
- `vcb.concepts.recoverability`
- `vcb.workflow.testing`
- `vcb.failure.weakened_tests`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.chapter.writing_updating_tests -->
