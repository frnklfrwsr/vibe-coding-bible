<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.skipping_tests version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
last_reviewed: '2026-06-09'
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
evidence_scope: official OpenAI/Codex guidance plus VCB maintainer synthesis for risk-managed
  shortcut harm reduction
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
- major_refactor
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.shortcut.skipping_tests
title: Skipping Tests
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- tests
- CI
- Codex App
- Codex CLI
- Codex IDE
- pull requests
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- verification
- testing
- evidence
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- manual exact-flow check
- smallest relevant automated check
- do not weaken assertions
- explicit not-verified note
shortcut_profiles:
- vcb.shortcut.skipping_tests
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls
  than prototypes
likely_to_change:
- current Codex test/review UI affordances
- project-specific test commands
- CI coverage and runtime
- model summary habits
obsolete_when:
- agents can produce trusted task-scoped verification proof without human or CI review
related_topics:
- vcb.workflow.testing
- vcb.prompting.acceptance_criteria
- vcb.failure.weakened_tests
- vcb.failure.ci_false_confidence
- vcb.failure.done_claim_without_evidence
- vcb.constraints.review_budget
---

# Skipping Tests

> Summary:
> Skipping tests is the shortcut of accepting code without running the smallest meaningful check that could catch the likely failure.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skipping_tests.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Skipping tests means Codex changed code and you accept the result without running the relevant automated or manual check. It is tempting because the output looks simple or because tests are slow, flaky, or unfamiliar.

### Why it matters

Tests are not ceremony; they are executable expectations. When you skip them, you replace evidence with hope, and the bug often moves from a cheap local fix into a PR, release, or user session.

### What good looks like

Good: “Run the smallest relevant test, typecheck/build if cheap, and state exactly what was not checked.”

### What bad looks like

Bad: “Looks fine. Ship it.”

### Minimal example

After a date-formatting change, run the affected unit test or the exact UI flow instead of the whole suite or no check at all.

### Checklist

- name the behavior that could break
- run the nearest relevant test or manual flow
- keep the test assertion at least as strong as before
- record failures separately from old unrelated failures
- do not claim production-ready when checks did not run

<!-- VCB:END_SECTION id=vcb.shortcut.skipping_tests.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skipping_tests.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that the minimum useful test is a budget tool: it prevents expensive rollback and reduces review uncertainty.

### Diagnostic questions

- What behavior changed?
- Which existing test or command is closest to that behavior?
- Is the user avoiding tests because they are slow, failing, or unknown?
- Did Codex change tests as well as code?
- What would make the “done” claim false?

### Coaching tactics

- ask for one targeted check before broad suites
- separate old failures from failures introduced by this change
- forbid weakening assertions unless the requirement changed
- convert “tests are too slow” into “which smallest check is meaningful?”
- require explicit not-run notes

### Red flags

- all tests pass with no command/output
- test deletion or broadened assertions
- UI/backend changes accepted from diff only
- production, auth, billing, or data changes with no check
- flaky-test handwaving without evidence

### Prompt pattern

```text
Run or identify the smallest meaningful verification for this change. Do not weaken tests to make them pass. Report command, result, old unrelated failures, new failures, and what was not verified.
```

<!-- VCB:END_SECTION id=vcb.shortcut.skipping_tests.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They take the shortcut because it reduces immediate friction: fewer prompts, fewer checks, fewer approvals, less review, or a faster-looking result.

### When the shortcut may be acceptable

Acceptable for disposable prototypes, throwaway local experiments, or tightly isolated work where rollback is trivial, no real users or secrets are involved, and the output is not treated as production evidence.

### When it becomes a bad trade

Bad when the task touches production, auth, payments, data deletion, secrets, CI permissions, public documentation, dependency supply chain, or a diff too broad for available review.

### Risk profile

- Probability: medium for disciplined small tasks; high when prompts are vague, permissions are broad, or review is deferred.
- Impact: low for local throwaways; high for production, team repos, security-sensitive systems, and public releases.
- Recoverability: good before merge with a clean branch; worse after release, data migration, dependency rollout, credential exposure, or undocumented behavior change.

### Blast radius

The shortcut can spread from one fast turn into merged code, stale tests, false release notes, hidden security exposure, future debugging assumptions, and more expensive recovery work.

### Minimum guardrails

- manual exact-flow check
- smallest relevant automated check
- do not weaken assertions
- explicit not-verified note

### Recovery plan

1. Stop the current run or merge path.
2. Create or restore a Git checkpoint.
3. Ask Codex for a risk and evidence table for the shortcut taken.
4. Run the smallest relevant verification or review pass.
5. Revert, isolate, or split the work if evidence is missing.
6. Update the prompt, AGENTS.md guidance, or workflow checklist so the same shortcut has a guardrail next time.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest guardrail that can catch the likely failure before spending on retries, broad context, or recovery.

### Fastest high-usage path

High-throughput users can spend more turns, but should spend them on bounded checks, comparison, or review rather than broad unverified mutation.

### Low-attention path

Low-attention delegation is only safe when scope, permissions, and stop conditions are narrower than they would be in supervised work.

### Production-quality path

Production work requires explicit evidence, diff review, rollback planning, and refusal to treat summaries as approval.

### Prototype versus production

Prototype shortcuts can be rational when they are isolated and disposable. Production shortcuts need documented guardrails or rejection.

### Maintenance phase

Maintenance work should reduce repeated shortcut risk by encoding durable commands, review criteria, and do-not rules after the shortcut recurs.

## Stable Core

- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls than prototypes

## Volatile Surface

- current Codex test/review UI affordances
- project-specific test commands
- CI coverage and runtime
- model summary habits

## Obsolescence Watch

This card should be revised if:

- agents can produce trusted task-scoped verification proof without human or CI review

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, done-when criteria, testing, review, and permission posture.
- `openai.codex.workflows` — Official OpenAI Codex workflow guidance for context, definition of done, reproduction, and verification loops.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.testing`
- `vcb.prompting.acceptance_criteria`
- `vcb.failure.weakened_tests`
- `vcb.failure.ci_false_confidence`
- `vcb.failure.done_claim_without_evidence`
- `vcb.constraints.review_budget`

<!-- VCB:STOP_RETRIEVAL reason="skipping_tests_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.skipping_tests -->
