<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.trusting_estimates_before_inspection version=0.25.0-draft.chunk24 -->
---
version: 0.25.0-draft.chunk24
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
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
evidence_scope: official OpenAI/Codex guidance on prompting, best practices, subagents, model/current-source volatility, and truthfulness/hallucination caveats; VCB maintainer synthesis for multi-AI, answer-selection, model-bias, estimate, and integration harm reduction
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
id: vcb.shortcut.trusting_estimates_before_inspection
title: Trusting Estimates Before Inspection
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- estimation
- unknown codebases
- planning
- dependency upgrades
- refactors
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- estimates
- model_bias
- planning
- inspection
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: HIGH_RISK_SHORTCUT
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- label uninspected guesses
- inspect before committed estimates
- list unknowns
- slice the task
- use confidence bands
shortcut_profiles:
- vcb.shortcut.trusting_estimates_before_inspection
durable_principles:
- uninspected estimates are guesses
- unknowns dominate unfamiliar work
- confidence should follow evidence
likely_to_change:
- Codex model estimation behavior
- model-selection controls
- repository analysis tooling
obsolete_when:
- agents can automatically inspect all relevant artifacts, calculate historical project velocity, and report calibrated confidence with evidence
related_topics:
- vcb.workflow.unknown_codebase
- vcb.prompting.plan_first
- vcb.constraints.scope_budget
- vcb.constraints.review_budget
- vcb.failure.done_claim_without_evidence
---

# Trusting Estimates Before Inspection

> Summary:
> This shortcut is believing an AI estimate before the model has inspected the actual code, dependencies, tests, constraints, and unknowns.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.trusting_estimates_before_inspection.human -->
## 1. For the Human: Plain-Language Concept

### What this means

The shortcut is asking “how hard is this?” and treating the answer as project truth before the AI has looked at the relevant evidence.

### Why it matters

Models are good at producing plausible ranges. They are not magic x-rays. In unfamiliar code, the unknowns usually dominate the estimate.

### What good looks like

Good: “Ask for an inspection plan first: likely files, unknowns, risk factors, and the smallest reconnaissance task before estimating.”

### What bad looks like

Bad: “Accept “two hours” for a migration without checking call sites, build scripts, tests, data shape, or deployment path.”

### Minimal example

Before estimating a dependency upgrade, inspect package manifests, lockfile, import sites, changelog, tests, and CI history.

### Checklist

- separate rough guess from inspected estimate
- ask for unknowns first
- inspect relevant files before commitment
- state confidence and assumptions
- convert estimates into slices

<!-- VCB:END_SECTION id=vcb.shortcut.trusting_estimates_before_inspection.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.trusting_estimates_before_inspection.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that estimates without inspection are planning placeholders, not commitments.

### Diagnostic questions

- What did the AI inspect?
- What could make the estimate wrong by 3x?
- Which files or tests are unknown?
- Can the task be sliced before committing?

### Coaching tactics

- label pre-inspection estimates as guesses
- ask for risk factors and unknowns
- do a read-only reconnaissance pass
- estimate after a small spike

### Red flags

- precise estimates with no repo inspection
- AI says “straightforward” in an unfamiliar codebase
- deadline set from a chat answer
- unknowns omitted

### Prompt pattern

```text
Do not estimate yet. First inspect the relevant files and return: known facts, unknowns, files checked, hidden risk factors, likely slices, and what evidence is needed before a credible estimate. Then provide a confidence-rated estimate only if evidence is enough.
```

<!-- VCB:END_SECTION id=vcb.shortcut.trusting_estimates_before_inspection.ai_coach -->

## Shortcut Reality

### Ideal practice

Use estimates as evidence-aware planning tools that improve after inspection.

### What people often do instead

People use AI estimates to feel certain before doing the reading that creates certainty.

### When the shortcut may be acceptable

Acceptable for early ballpark planning if explicitly labeled as uninspected and not used for commitments.

### When it becomes a bad trade

Bad for customer promises, sprint commitments, migrations, security work, data changes, dependency upgrades, and production incidents.

### Risk profile

- Probability: high because users want confidence quickly.
- Impact: medium for planning misses; high for commitments and risky work.
- Recoverability: medium if caught early; low after promises or partially completed broad changes.

### Blast radius

The blast radius is the commitment made from the estimate: deadline, scope, risk, and skipped discovery.

### Minimum guardrails

- label uninspected guesses
- inspect before committed estimates
- list unknowns
- slice the task
- use confidence bands

### Recovery plan

- Reclassify the estimate as uninspected.
- Run a reconnaissance prompt over relevant files.
- List unknowns and risk multipliers.
- Break work into slices.
- Reset commitments with evidence-backed ranges.

## Budget and Constraint Notes

### Cheapest reliable path

Use one AI/tool/agent first, require one evidence packet, and spend the smallest amount of model usage needed to inspect the actual project before accepting or comparing answers.

### Fastest high-usage path

High-throughput users can run parallel analysis, but only with role separation, read-only reviewers where possible, explicit output schemas, and one final integration gate.

### Low-attention path

Low-attention delegation should default to report-only or read-only work. Do not let many agents, model guesses, or consensus summaries mutate code before a human reviews evidence.

### Production-quality path

Production-quality use requires current-source checks for volatile product/model facts, file-level evidence, changed-file review, tests or checks, rollback, and a record of why one AI answer was accepted over alternatives.

### Prototype versus production

A disposable prototype may use rough model choice, loose estimates, or multiple brainstormed answers. Persistent or production-bound work needs evidence, one owner, and guardrails before mutation.

### Maintenance phase

In maintenance, multi-AI shortcuts compound because stale assumptions survive across docs, config, prompts, and team habits. Revisit role boundaries, model-routing advice, and answer-selection rubrics after repeated failures or phase changes.

## Stable Core

- uninspected estimates are guesses
- unknowns dominate unfamiliar work
- confidence should follow evidence

## Volatile Surface

- Codex model estimation behavior
- model-selection controls
- repository analysis tooling

## Obsolescence Watch

This card should be revised if:

- agents can automatically inspect all relevant artifacts, calculate historical project velocity, and report calibrated confidence with evidence

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for task context, constraints, done-when criteria, plan-first work, review, and verification.
- `openai.codex.subagents` — Official OpenAI Codex guidance for subagent workflows, parallel agents, orchestration, sandbox inheritance, and token-use caveats.
- `openai.codex.subagent_concepts` — Official OpenAI Codex concept guidance for context pollution, context rot, parallel analysis, and write-heavy workflow cautions.
- `openai.codex.models` — Official OpenAI Codex model source for volatile model-availability and model-configuration watchlist routing.
- `openai.help.truthfulness` — Official OpenAI Help Center truthfulness caveat for treating fluent answers as fallible and requiring verification.
- `openai.hallucinations` — Official OpenAI hallucination explainer for confident wrong-answer and guessing-incentive framing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, evidence, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.unknown_codebase`
- `vcb.prompting.plan_first`
- `vcb.constraints.scope_budget`
- `vcb.constraints.review_budget`
- `vcb.failure.done_claim_without_evidence`

<!-- VCB:STOP_RETRIEVAL reason="trusting-estimates-before-inspection_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.trusting_estimates_before_inspection -->
