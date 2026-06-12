<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.manual_testing_only version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-12'
last_reviewed: '2026-06-12'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI/Codex guidance, testing-tool documentation anchors, and VCB maintainer synthesis for risk-managed shortcut harm reduction
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
id: vcb.shortcut.manual_testing_only
title: Manual Testing Only
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-12'
applies_to:
- manual QA
- automated tests
- UI checks
- regression testing
- CI
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- verification
- testing
- regression risk
risk_level:
  prototype: LOW_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- record exact manual flow
- add one targeted check when feasible
- cover negative path
- document not-automated risk
shortcut_profiles:
- vcb.shortcut.manual_testing_only
durable_principles:
- manual checks are useful but fragile memory
- repeated behavior deserves executable evidence
- production regressions need checks that can run again
likely_to_change:
- test runner commands
- browser automation tooling
- CI test environment behavior
- project-specific test coverage
obsolete_when:
- manual observations can be converted into trusted repeatable verification automatically
related_topics:
- vcb.workflow.testing
- vcb.workflow.frontend_work
- vcb.workflow.visual_qa
- vcb.concepts.test
- vcb.concepts.ci
- vcb.failure.ci_false_confidence
---

# Manual Testing Only

> Summary:
> Manual testing only is relying on a one-time click-through or eyeball check when the changed behavior needs repeatable verification.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.manual_testing_only.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Manual testing only means you click through the app or inspect behavior once, then treat that as enough proof. Sometimes that is all a prototype deserves. For repeated or production behavior, it leaves no reusable tripwire.

### Why it matters

A manual check can prove that one person saw one path work once. It does not automatically prove regression safety, edge states, negative paths, browser differences, or future changes.

### What good looks like

Good: "Record the manual path, then add or run one targeted automated check for the behavior most likely to regress."

### What bad looks like

Bad: "I clicked the happy path once. Ship it."

### Minimal example

For a form fix, manually test the happy path and one error path, then add or run a focused test for validation behavior if the form will stay in the product.

### Checklist

- record exact manual steps
- capture expected and actual result
- test at least one negative or edge path
- add automated evidence when behavior will recur
- document what remains manual-only

<!-- VCB:END_SECTION id=vcb.shortcut.manual_testing_only.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.manual_testing_only.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use manual testing as evidence, not as a permanent substitute for repeatable checks.

### Diagnostic questions

- Is this behavior likely to change again?
- Could the bug return unnoticed?
- Which manual steps were actually performed?
- Is there an existing test harness nearby?
- What path would be expensive to miss?

### Coaching tactics

- ask for exact manual steps and result
- convert repeated manual checks into targeted tests
- keep manual UI and automated logic checks complementary
- ask for one negative path
- let disposable prototype work stay manual with explicit caveat

### Red flags

- no steps recorded
- only the happy path checked
- production behavior with no repeatable check
- manual UI check used to prove backend logic
- automated check skipped because it is unfamiliar

### Prompt pattern

```text
Record the manual verification path as steps, expected, actual, and evidence. If this behavior is durable, add or run the smallest repeatable check that would catch the likely regression.
```

<!-- VCB:END_SECTION id=vcb.shortcut.manual_testing_only.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They trust a one-time manual click because it is immediate and familiar.

### When the shortcut may be acceptable

Acceptable for disposable prototypes, one-off demos, visual exploration, or low-risk changes where repeatable automation costs more than the value of the behavior.

### When it becomes a bad trade

Bad for production, shared code, auth, payments, data, bug fixes, regressions, critical user flows, and behavior likely to be changed again.

### Risk profile

- Probability: low for tiny demos; medium/high for recurring product behavior.
- Impact: low for throwaway prototypes; high when manual checks miss future regressions.
- Recoverability: medium before merge; poor when no one can reproduce the exact manual evidence later.

### Blast radius

Manual-only verification can let regressions return, hide edge-state gaps, and make future reviewers depend on memory instead of executable proof.

### Minimum guardrails

- record exact manual flow
- add one targeted check when feasible
- cover negative path
- document not-automated risk

### Recovery plan

1. Write down the manual steps that were actually tested.
2. Identify the most likely regression.
3. Add or run the nearest automated check if feasible.
4. Mark remaining manual-only coverage explicitly.
5. Add a follow-up test task for durable behavior if time is constrained.

## Budget and Constraint Notes

### Cheapest reliable path

Keep the manual check, but add one narrow automated check when the behavior will survive the prototype.

### Fastest high-usage path

High-throughput users should ask Codex to convert repeated manual flows into tests over time.

### Low-attention path

Low-attention work needs repeatable checks because the human is not present to remember what was clicked.

### Production-quality path

Production work needs repeatable verification for critical behavior, plus manual exploratory checks when UI state matters.

### Prototype versus production

Prototype manual-only checks are acceptable when explicitly disposable. Production manual-only checks are a gap.

### Maintenance phase

Maintenance should turn recurring manual checks into regression tests.

## Stable Core

- manual checks are useful but fragile memory
- repeated behavior deserves executable evidence
- production regressions need checks that can run again

## Volatile Surface

- test runner commands
- browser automation tooling
- CI test environment behavior
- project-specific test coverage

## Obsolescence Watch

This card should be revised if:

- manual observations can be converted into trusted repeatable verification automatically

## Evidence and Sources

- `openai.codex.best_practices` - Official OpenAI Codex guidance for validation and review.
- `openai.codex.workflows` - Official OpenAI Codex workflow guidance for explicit context, definition of done, and verification.
- `playwright.docs.writing_tests` - Official Playwright documentation for browser action/assertion test writing.
- `vitest.docs.guide` - Official Vitest guide anchor for JavaScript test-runner mechanics.
- `vcb.synthesis.stable_engineering_practice` - VCB maintainer synthesis for durable risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.testing`
- `vcb.workflow.frontend_work`
- `vcb.workflow.visual_qa`
- `vcb.concepts.test`
- `vcb.concepts.ci`
- `vcb.failure.ci_false_confidence`

<!-- VCB:STOP_RETRIEVAL reason="manual_testing_only_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.manual_testing_only -->
