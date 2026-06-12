<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.broad_refactor version=0.1.0 -->
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
id: vcb.shortcut.broad_refactor
title: Broad Refactor
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- refactoring
- cleanup
- modernization
- dead-code removal
- architecture work
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- refactoring
- scope
- reviewability
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
- one bounded seam
- branch checkpoint
- behavior invariants
- parity checks
- no dependency/framework changes
shortcut_profiles:
- vcb.shortcut.broad_refactor
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls
  than prototypes
likely_to_change:
- Codex refactor use-case examples
- current diff/review tools
- project test coverage
- framework migration patterns
obsolete_when:
- agents can prove behavior preservation across broad refactors with complete semantic
  diff evidence
related_topics:
- vcb.workflow.refactoring
- vcb.failure.broad_refactor_drift
- vcb.workflow.reviewing_diffs
- vcb.workflow.testing
- vcb.constraints.scope_budget
- vcb.constraints.recovery_budget
---

# Broad Refactor

> Summary:
> Broad refactor is asking Codex to clean up many files, abstractions, or layers at once while still expecting behavior preservation.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.broad_refactor.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A refactor should change structure without changing behavior. This shortcut turns refactoring into a wide rewrite, often mixing cleanup, bug fixes, dependency changes, style changes, and architecture changes in one diff.

### Why it matters

The danger is review invisibility. When too much moves at once, behavior changes become hard to spot, tests can be weakened, and rollback becomes expensive.

### What good looks like

Good: “Plan first. Refactor one module or seam. Preserve public behavior. Run parity checks. Stop before adding dependencies or changing features.”

### What bad looks like

Bad: “Clean up the whole app and modernize anything you see.”

### Minimal example

Extract one duplicated formatter function and run its tests; do not simultaneously rename APIs, move folders, alter state, and change framework versions.

### Checklist

- separate refactor from feature work
- pick one seam or module
- protect behavior with tests or parity checks
- avoid dependency/framework changes in the same diff
- review moved code and deleted branches

<!-- VCB:END_SECTION id=vcb.shortcut.broad_refactor.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.broad_refactor.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to keep refactors boring. If the behavior changes, call it a feature or migration and use a different workflow.

### Diagnostic questions

- What behavior must remain identical?
- Which files are allowed to move?
- Is the task hiding a rewrite?
- Are dependencies or frameworks changing?
- Which parity check will prove behavior stayed stable?

### Coaching tactics

- force a plan-only pass
- limit file count or module boundary
- ask for before/after behavior summary
- reject mixed cleanup plus migration diffs
- use branch checkpoints and small commits

### Red flags

- large rename/move plus logic changes
- tests edited heavily during refactor
- new abstractions across the app
- dependency changes bundled with cleanup
- no parity evidence

### Prompt pattern

```text
Refactor only this bounded area. Preserve external behavior. Do not add dependencies, change public APIs, or change features. List invariants, changed files, parity checks, and anything that should be split into a separate task.
```

<!-- VCB:END_SECTION id=vcb.shortcut.broad_refactor.ai_coach -->

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

- one bounded seam
- branch checkpoint
- behavior invariants
- parity checks
- no dependency/framework changes

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

- Codex refactor use-case examples
- current diff/review tools
- project test coverage
- framework migration patterns

## Obsolescence Watch

This card should be revised if:

- agents can prove behavior preservation across broad refactors with complete semantic diff evidence

## Evidence and Sources

- `openai.codex.use_cases.refactor_your_codebase` — Official OpenAI Codex use case for small reviewable refactor and modernization passes.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, done-when criteria, testing, review, and permission posture.
- `martin_fowler.refactoring` — Named expert source for refactoring as behavior-preserving restructuring.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.refactoring`
- `vcb.failure.broad_refactor_drift`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.testing`
- `vcb.constraints.scope_budget`
- `vcb.constraints.recovery_budget`

<!-- VCB:STOP_RETRIEVAL reason="broad_refactor_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.broad_refactor -->
