<!-- VCB:BEGIN_TOPIC id=vcb.workflow.bug_repro version=0.1.0 -->
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
id: vcb.workflow.bug_repro
title: Bug Reproduction First
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- Computer Use QA
- Bug triage
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.debugging_without_repro
- vcb.shortcut.treating_symptom_as_root_cause
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.browser_clicking_without_repro
durable_principles:
- a bug fix needs a failing observation before the fix
- repro steps define the boundary of the problem
- root cause and symptom must be separated
likely_to_change:
- Computer Use QA behavior
- browser automation support
- test framework commands
- Codex bug-triage automation
obsolete_when:
- coding agents can safely fix bugs without reproducing, testing, or specifying failure behavior
related_topics:
- vcb.chapter.debugging_with_reproduction
- vcb.prompting.acceptance_criteria
- vcb.workflow.testing
- vcb.concepts.test
- vcb.concepts.observability
- vcb.codex.computer_use
- vcb.codex.automations
---

> Summary:
> The repro-first debugging workflow makes Codex reproduce or specify the bug before changing code, preventing symptom fixes and false completion.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.bug_repro.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Repro-first debugging means Codex must show or define how the bug happens before it fixes code. A repro can be a failing test, exact steps, a log, a screenshot sequence, or a minimal command.

### Why it matters

Without a repro, Codex may fix the symptom, remove the error, weaken a test, or change unrelated behavior. The repro is the evidence that the bug exists and later that it is fixed.

### The mental model

A repro is the crime scene. If you skip it, you are not debugging; you are guessing with a patch file.

### What good looks like

Good: “First reproduce the failing checkout flow. Record steps, expected, actual, and likely root cause. Then propose the smallest fix. Done when the repro fails before and passes after.”

### What bad looks like

Bad: “This crashes sometimes. Fix it.” That gives Codex no stable target.

### Minimal example

Bug packet: environment, version, exact steps, expected result, actual result, logs/errors, recent changes, suspected area, and severity.

### Checklist

- state expected and actual behavior
- include exact steps or failing command
- capture logs or screenshots when relevant
- ask Codex to separate symptom from suspected cause
- verify the same repro passes after the fix
<!-- VCB:END_SECTION id=vcb.workflow.bug_repro.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.bug_repro.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to make bugs observable before asking Codex to change code.

### Diagnose the human’s current model

- Can the user trigger the bug on demand?
- What is expected versus actual?
- What changed recently?
- Is there a failing test or can one be added?
- What would prove the fix did not only hide the symptom?

### Explanation strategy

Insist on a bug packet. If the bug is intermittent, ask Codex to narrow conditions and add observability. Do not accept a patch until the evidence path is clear.

### Useful metaphor

Debugging without a repro is shooting at fog. A repro turns the fog into a target.

### Coaching tactics

- ask for repro before root cause
- turn manual steps into an automated test when feasible
- keep the failing observation visible throughout the session
- reject fixes that delete assertions or swallow errors
- ask Codex for alternative root causes before editing

### Prompt patterns

```text
Do not fix yet. Reproduce or specify the bug. Output steps, expected, actual, logs, suspected files, and a verification plan.
Create a failing test for this bug first. Show why it fails. Then implement the smallest fix.
After the fix, rerun the original repro and list exactly what changed.
```

### Red flags to call out directly

- Codex changes code before reproducing
- fix only catches and ignores an exception
- test is weakened to pass
- root cause is asserted without evidence
- manual UI claim has no steps or screenshot sequence

### Exercises

- Have the human write a bug packet from a vague complaint.
- Ask Codex to propose three possible repro paths before code.
- Compare pre-fix and post-fix evidence and reject unsupported claims.
<!-- VCB:END_SECTION id=vcb.workflow.bug_repro.ai_coach -->

## Shortcut Reality

### The ideal practice

Reproduce or specify the bug before changing code.

### What users often do instead

Users often ask Codex to patch the likely cause immediately.

### When the shortcut may be fine

Direct patching can be fine for obvious syntax errors, deterministic failing tests, or disposable prototypes where failure is cheap.

### When the shortcut is a bad idea

It is a bad trade for intermittent bugs, production incidents, data corruption, auth, payments, security, or UI flows where state matters.

### Risk profile

- Probability of failure: High failure probability when expected and actual behavior are not pinned down.
- Impact if it fails: Impact can be high because symptom fixes mask root causes and delay real resolution.
- Ease of recovery: Good if the original failure evidence exists; poor when the team cannot tell whether the bug was ever fixed.
- Blast radius: The blast radius includes every behavior touched by a guess-based fix.
- Skill needed to recover: Medium for normal bugs; high for intermittent production or stateful UI issues.
- Hidden cost: Recurring incidents, hidden swallowed errors, weakened tests, and false confidence.

### Minimum guardrails

- write expected and actual behavior
- capture exact repro steps
- add or run a failing check
- forbid weakening tests to pass
- verify the original repro after the fix

### Recovery plan

- Stop new fixes.
- Reconstruct the repro from logs, users, or tests.
- Audit current diff for symptom hiding.
- Create a failing check if possible.
- Apply the smallest root-cause fix and rerun evidence.

## Budget and Constraint Notes

### Cheapest reliable path

A small repro saves repeated failed prompts and review cycles.

### Fastest high-usage path

For high-throughput bug triage, standardize bug packets and let Codex classify severity before fixing.

### Low-attention path

Low-attention bug fixing is unsafe without a deterministic repro and clear done-when evidence.

### Production-quality path

Production bugs need logs, rollback thinking, severity, blast radius, and post-fix verification.

### Prototype versus production

Prototype bugs can sometimes be patched directly. Maintenance and production bugs need evidence because they recur. 

## Stable Core

- debugging starts with observable failure
- the same repro should pass after the fix
- root cause claims need evidence

## Volatile Surface

- Codex Computer Use QA behavior
- browser-control affordances
- automation bug-triage features
- test framework commands
- observability tooling

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- official Codex QA guidance changes
- Codex automatically captures reliable repro artifacts
- test-generation workflows change enough to alter failure-first guidance

## Evidence and Sources

- `openai.codex.workflows` — Official OpenAI Codex workflow examples for explicit context, done definitions, bug fixes, and tests.
- `openai.codex.use_cases.qa_computer_use` — Official OpenAI Codex use case for QA with Computer Use, bug reports, setup, expected/actual behavior, and severity.
- `openai.codex.use_cases.automation_bug_triage` — Official OpenAI Codex use case for automation-oriented bug triage.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.debugging_with_reproduction`
- `vcb.prompting.acceptance_criteria`
- `vcb.workflow.testing`
- `vcb.concepts.test`
- `vcb.concepts.observability`
- `vcb.codex.computer_use`
- `vcb.codex.automations`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.bug_repro -->
