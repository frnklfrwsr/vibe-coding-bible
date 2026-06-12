<!-- VCB:BEGIN_TOPIC id=vcb.workflow.testing version=0.1.0 -->
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
evidence_scope: official OpenAI Codex prompting/workflow anchors plus VCB maintainer synthesis
  for risk, budget, and coaching guidance
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
id: vcb.workflow.testing
title: Testing Workflow with Codex
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- CI
- Pull requests
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.skipping_tests
- vcb.shortcut.manual_testing_only
- vcb.shortcut.ignoring_lint_typecheck
- vcb.shortcut.accepting_looks_done
durable_principles:
- tests are evidence, not decoration
- generated tests need human review
- a good bug test fails before the fix and passes after
likely_to_change:
- test runner commands
- framework syntax
- Codex test-running support
- CI integration behavior
- coverage tools
obsolete_when:
- software changes can be safely merged without executable or equivalent verification evidence
related_topics:
- vcb.chapter.writing_updating_tests
- vcb.prompting.acceptance_criteria
- vcb.workflow.bug_repro
- vcb.workflow.feature_slicing
- vcb.concepts.test
- vcb.concepts.typecheck
- vcb.concepts.lint
- vcb.concepts.ci
---

> Summary:
> The testing workflow uses Codex to create, update, and run meaningful checks without treating generated tests as unquestionable truth.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.testing.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Testing with Codex means asking it to help write, update, and run checks that prove behavior. The test is not good because Codex wrote it. It is good if it would catch a real breakage.

### Why it matters

Codex can make code move fast. Tests keep that speed from turning into silent regressions.

### The mental model

Tests are guardrails on the road. Codex can help install them, but you still inspect whether they are placed at the cliff edge or in a decorative circle in a parking lot.

### What good looks like

Good: “Add a test for invalid promo codes. Show that it fails before the fix, implement the smallest fix, then run the targeted test and relevant suite.”

### What bad looks like

Bad: “Add tests” with no behavior target. Codex may add shallow tests that only prove the component renders.

### Minimal example

Testing request: behavior under test, existing test file/pattern, negative case, command to run, failure-first requirement, and final result summary.

### Checklist

- test targets behavior, not only implementation details
- bug test fails before the fix when possible
- test command is named
- Codex does not weaken or delete assertions
- human reviews generated tests for false confidence
<!-- VCB:END_SECTION id=vcb.workflow.testing.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.testing.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat tests as verification artifacts and generated tests as reviewable code.

### Diagnose the human’s current model

- What behavior should this test catch?
- Would this test fail if the bug returned?
- Is the test too coupled to implementation?
- Did Codex weaken existing assertions?
- Which checks are enough for this slice?

### Explanation strategy

Ask for targeted tests linked to acceptance criteria. For bugs, prefer failure-first. For features, cover the primary behavior and one important negative path. Review generated tests with the same skepticism as generated production code.

### Useful metaphor

Generated tests are witnesses, not judges. They can provide evidence, but you still cross-examine them.

### Coaching tactics

- ask for test intent before code
- require Codex to explain why the test would fail on the old behavior
- run targeted checks before broad suites when budget is tight
- keep manual testing separate from automated evidence
- watch for assertion weakening and over-mocking

### Prompt patterns

```text
Add or update tests for [behavior]. Follow existing patterns in [file]. The test should fail on the old behavior if feasible. Do not weaken existing tests.
Run [targeted command] and summarize failures. Do not change code until you explain the failing behavior.
After implementation, list tests added, tests changed, commands run, and any checks not run.
```

### Red flags to call out directly

- test passes before the fix for a claimed bug test
- test asserts implementation details only
- Codex deletes a failing test
- mocks remove the behavior under test
- manual click-through replaces all automated evidence for production code

### Exercises

- Ask the human to identify what a test would catch if the bug returned.
- Have them review a generated test and mark weak assertions.
- Practice choosing targeted checks versus full suite based on risk and budget.
<!-- VCB:END_SECTION id=vcb.workflow.testing.ai_coach -->

## Shortcut Reality

### The ideal practice

Use tests or equivalent verification evidence for mergeable changes.

### What users often do instead

Users often skip tests because Codex output looks plausible or because running tests costs time.

### When the shortcut may be fine

Skipping automated tests may be acceptable for throwaway prototypes, docs-only edits, or visual explorations with no merge intent.

### When the shortcut is a bad idea

It is a bad trade for production, shared logic, auth, payments, migrations, concurrency, or bug fixes.

### Risk profile

- Probability of failure: Medium to high risk of hidden regressions when tests are skipped or shallow.
- Impact if it fails: Impact is high when untested changes reach users or corrupt data.
- Ease of recovery: Good when Git history and repro evidence exist; poor when false confidence allowed multiple untested changes to stack.
- Blast radius: The blast radius is the behavior changed without executable tripwires.
- Skill needed to recover: Low for running checks; medium for evaluating test quality; high for recovering from untested regressions.
- Hidden cost: Flaky future releases, brittle tests, weaker CI, and maintenance debt.

### Minimum guardrails

- name targeted checks
- review generated tests
- require failure-first for bugs when feasible
- do not allow assertion weakening without justification
- record checks not run

### Recovery plan

- List recent untested changes.
- Write or request targeted tests for highest-risk behavior.
- Run checks and capture failures.
- Fix regressions before adding more features.
- Add CI or a checklist to prevent repeat skipping.

## Budget and Constraint Notes

### Cheapest reliable path

Run the smallest targeted check that proves the slice, then escalate if it fails or risk is high.

### Fastest high-usage path

High-throughput users should let Codex draft tests and commands, but keep human review on test quality.

### Low-attention path

Low-attention implementation must return tests/checks run and unresolved verification gaps. Otherwise it is not ready.

### Production-quality path

Production changes need automated checks where practical plus human review of generated tests.

### Prototype versus production

Prototype testing can be manual and shallow. Production and maintenance work need executable evidence and regression awareness. 

## Stable Core

- tests are part of the proof of change
- generated tests require review
- bugs need tests that would catch recurrence when feasible

## Volatile Surface

- test framework commands
- CI provider behavior
- Codex ability to run tests per surface
- coverage tooling
- language-specific test patterns

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- official Codex testing guidance changes
- Codex gets stronger automatic test-quality evaluation
- project CI changes enough that recommended commands must be updated

## Evidence and Sources

- `openai.codex.workflows` — Official OpenAI Codex workflow examples for explicit context, done definitions, bug fixes, and tests.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, review, and verification.
- `openai.codex.guide_ai_native_engineering_team` — Official OpenAI Codex guide for AI-native engineering teams, including testing and human review posture.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.writing_updating_tests`
- `vcb.prompting.acceptance_criteria`
- `vcb.workflow.bug_repro`
- `vcb.workflow.feature_slicing`
- `vcb.concepts.test`
- `vcb.concepts.typecheck`
- `vcb.concepts.lint`
- `vcb.concepts.ci`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.testing -->
