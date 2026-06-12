<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.debugging_without_repro version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-12'
last_reviewed: '2026-06-12'
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
evidence_scope: official OpenAI/Codex workflow guidance plus VCB maintainer synthesis for risk-managed shortcut harm reduction
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
id: vcb.shortcut.debugging_without_repro
title: Debugging Without Reproduction
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-12'
applies_to:
- bug fixes
- incident triage
- regression testing
- logs
- support reports
- Codex Cloud
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- debugging
- reproduction
- root cause
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
- expected versus actual
- steps or failing command
- preserve evidence
- rerun same repro after fix
shortcut_profiles:
- vcb.shortcut.debugging_without_repro
durable_principles:
- a bug fix needs an observable failure target
- root cause and symptom are not the same thing
- the same repro should fail before and pass after when feasible
likely_to_change:
- bug-triage automation behavior
- observability/logging tools
- test framework commands
- Codex browser/computer-use evidence surfaces
obsolete_when:
- agents can reliably infer, prove, and fix bugs without explicit reproduction evidence
related_topics:
- vcb.workflow.bug_repro
- vcb.workflow.testing
- vcb.prompting.acceptance_criteria
- vcb.failure.done_claim_without_evidence
- vcb.failure.weakened_tests
- vcb.concepts.test
---

# Debugging Without Reproduction

> Summary:
> Debugging without reproduction is asking Codex to patch a bug before the failure is observable as steps, logs, screenshots, a command, or a failing test.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.debugging_without_repro.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut means Codex starts fixing before the bug has a stable target. The target can be a failing test, exact manual steps, logs, a screenshot sequence, or a command that shows the problem.

### Why it matters

Without a repro, Codex may fix the symptom, hide the error, weaken a test, or change unrelated code. You cannot know the bug is fixed if you never proved how it failed.

### What good looks like

Good: "First reproduce or specify the failure. Then patch narrowly. Done when the same repro passes."

### What bad looks like

Bad: "It sometimes breaks. Make it not break."

### Minimal example

For a crash report, capture the route, inputs, expected result, actual error, log line, and recent change before editing code.

### Checklist

- state expected and actual behavior
- capture steps, command, log, screenshot, or failing test
- keep the failing evidence visible during the fix
- separate symptom from suspected root cause
- rerun the same repro after the patch

<!-- VCB:END_SECTION id=vcb.shortcut.debugging_without_repro.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.debugging_without_repro.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that a repro is the boundary between debugging and guessing.

### Diagnostic questions

- Can the bug be triggered on demand?
- What is expected versus actual?
- What evidence proves the bug exists?
- What changed recently?
- Would the proposed fix make the repro pass?

### Coaching tactics

- ask for a bug packet before mutation
- allow a hypothesis only after evidence is captured
- turn manual repro into a test when feasible
- reject fixes that only swallow errors
- require same-repro verification after the change

### Red flags

- patch proposed before failure is described
- no expected/actual behavior
- intermittent bug treated as obvious
- test weakened or deleted
- final answer claims fixed without rerunning the same path

### Prompt pattern

```text
Do not patch yet. First produce a bug packet: exact steps or command, expected behavior, actual behavior, logs/screenshots, suspected area, and what evidence will prove the fix. Then propose the smallest patch.
```

<!-- VCB:END_SECTION id=vcb.shortcut.debugging_without_repro.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They ask Codex to infer the bug from a vague symptom because reproducing it is annoying or intermittent.

### When the shortcut may be acceptable

Acceptable when the cause is a clear syntax error, missing import, obvious stack trace, or disposable prototype issue, and the fix can still be checked immediately.

### When it becomes a bad trade

Bad for production bugs, intermittent failures, data corruption, auth/payment issues, user-reported defects, regressions, and anything that could be masked by a shallow patch.

### Risk profile

- Probability: low for obvious compiler/runtime errors; high for intermittent or stateful bugs.
- Impact: low for isolated local issues; high for production incidents or recurring regressions.
- Recoverability: medium with preserved evidence; poor when the original failure disappears or becomes mixed with new changes.

### Blast radius

Skipping reproduction can spread false fixes, hidden weakened tests, swallowed errors, and wrong root-cause assumptions into future debugging sessions.

### Minimum guardrails

- expected versus actual
- steps or failing command
- preserve evidence
- rerun same repro after fix

### Recovery plan

1. Stop patching.
2. Capture current symptom evidence.
3. Reconstruct the smallest repro from logs, steps, or tests.
4. Revert speculative edits if they obscure the failure.
5. Patch the smallest likely root cause.
6. Rerun the same repro and one nearest regression check.

## Budget and Constraint Notes

### Cheapest reliable path

Spend time finding the smallest repro before paying for repeated speculative patches.

### Fastest high-usage path

High-throughput users can ask Codex to generate repro hypotheses, but should not let it mutate until evidence exists.

### Low-attention path

Low-attention bug work should return a bug packet and stop if reproduction cannot be established.

### Production-quality path

Production bug fixes require evidence, root-cause explanation, verification, and rollback consideration.

### Prototype versus production

Prototype bugs may accept lighter reproduction. Production bugs need repeatable evidence.

### Maintenance phase

Maintenance should convert recurring bug repros into tests or observability checks.

## Stable Core

- a bug fix needs an observable failure target
- root cause and symptom are not the same thing
- the same repro should fail before and pass after when feasible

## Volatile Surface

- bug-triage automation behavior
- observability/logging tools
- test framework commands
- Codex browser/computer-use evidence surfaces

## Obsolescence Watch

This card should be revised if:

- agents can reliably infer, prove, and fix bugs without explicit reproduction evidence

## Evidence and Sources

- `openai.codex.workflows` - Official OpenAI Codex workflow guidance for explicit context, definition of done, and verification loops.
- `openai.codex.use_cases.automation_bug_triage` - Official OpenAI Codex use case for bug triage automation.
- `openai.codex.best_practices` - Official OpenAI Codex guidance for validation and review.
- `vcb.synthesis.stable_engineering_practice` - VCB maintainer synthesis for durable risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.bug_repro`
- `vcb.workflow.testing`
- `vcb.prompting.acceptance_criteria`
- `vcb.failure.done_claim_without_evidence`
- `vcb.failure.weakened_tests`
- `vcb.concepts.test`

<!-- VCB:STOP_RETRIEVAL reason="debugging_without_repro_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.debugging_without_repro -->
