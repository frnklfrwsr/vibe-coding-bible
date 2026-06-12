<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.ignoring_model_biases version=0.25.0-draft.chunk24 -->
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
id: vcb.shortcut.ignoring_model_biases
title: Ignoring Model Biases
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- model choice
- AI review
- failure-mode diagnosis
- estimates
- answer acceptance
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- model_bias
- failure_modes
- verification
- review
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
- bias-to-guardrail checklist
- uncertainty request
- local evidence requirement
- disconfirming check
- failure-mode routing
shortcut_profiles:
- vcb.shortcut.ignoring_model_biases
durable_principles:
- models have predictable failure tendencies
- guardrails should match failure mode
- better models reduce but do not eliminate verification needs
likely_to_change:
- current model behavior
- available model families
- product-level confidence or citation features
obsolete_when:
- models provide reliable calibrated uncertainty, source-grounded claims, and automatic task-specific risk classification
related_topics:
- vcb.failure.hallucinated_apis
- vcb.failure.done_claim_without_evidence
- vcb.failure.context_pollution
- vcb.prompting.acceptance_criteria
- vcb.constraints.review_budget
---

# Ignoring Model Biases

> Summary:
> This shortcut is forgetting that models can be biased toward plausible answers, overconfident summaries, common patterns, pleasing the user, and underestimating hidden project constraints.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.ignoring_model_biases.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Model bias here means predictable failure tendencies, not political bias. Examples: sounding confident, choosing common patterns, underweighting local constraints, or agreeing with the user too easily.

### Why it matters

If you do not name the likely bias, you cannot add the right guardrail. The model will feel more reliable than it is, especially in familiar-looking but locally weird codebases.

### What good looks like

Good: “Before accepting output, ask which failure bias is most likely: hallucinated API, context pollution, weak tests, broad refactor drift, dependency bloat, UI taste gap, CI false confidence, or unsupported done claim.”

### What bad looks like

Bad: “Assume a confident answer is neutral because it came from a better model or a second AI.”

### Minimal example

For a UI task, the likely bias may be generic taste and happy-path screenshots. Add visual reference, states, breakpoints, and accessibility checks.

### Checklist

- name the likely bias
- map bias to guardrail
- ask for uncertainty and missing evidence
- verify local constraints
- run a disconfirming check

<!-- VCB:END_SECTION id=vcb.shortcut.ignoring_model_biases.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.ignoring_model_biases.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to convert “models can be wrong” into specific guardrails by task type.

### Diagnostic questions

- What failure pattern is likely for this task?
- What would the model tend to over-assume?
- What local evidence would challenge the answer?
- Which guardrail matches the bias?

### Coaching tactics

- use a bias-to-guardrail checklist
- ask for missing evidence before accepting
- make the model cite local artifacts
- route to failure-mode cards by symptom

### Red flags

- the human says “this model is usually right”
- confident tone replaces verification
- local constraints are ignored
- the model agrees with a risky shortcut

### Prompt pattern

```text
Before I accept this AI answer, identify the likely model failure biases for this task. For each bias, state the risk, the missing evidence, the guardrail, and the smallest check that would catch it.
```

<!-- VCB:END_SECTION id=vcb.shortcut.ignoring_model_biases.ai_coach -->

## Shortcut Reality

### Ideal practice

Use model strengths aggressively while adding guardrails for predictable failure tendencies.

### What people often do instead

People upgrade models or ask another AI but keep the same blind spot.

### When the shortcut may be acceptable

Acceptable for brainstorming when no action is taken until evidence is checked.

### When it becomes a bad trade

Bad when a model’s confident style, common-pattern bias, or agreement with the user controls production code, tests, dependencies, data, or security work.

### Risk profile

- Probability: high because fluent output feels like understanding.
- Impact: high when the bias matches a high-blast-radius task.
- Recoverability: medium if guarded before merge; low after broad changes or commitments.

### Blast radius

The blast radius is whichever project boundary the unguarded bias touches: code, tests, dependencies, UX, CI, data, or production process.

### Minimum guardrails

- bias-to-guardrail checklist
- uncertainty request
- local evidence requirement
- disconfirming check
- failure-mode routing

### Recovery plan

- Name the suspected bias.
- Route to the matching failure-mode card.
- Collect missing local evidence.
- Re-review the diff or answer.
- Add the guardrail to future prompts or AGENTS.md if repeated.

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

- models have predictable failure tendencies
- guardrails should match failure mode
- better models reduce but do not eliminate verification needs

## Volatile Surface

- current model behavior
- available model families
- product-level confidence or citation features

## Obsolescence Watch

This card should be revised if:

- models provide reliable calibrated uncertainty, source-grounded claims, and automatic task-specific risk classification

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for task context, constraints, done-when criteria, plan-first work, review, and verification.
- `openai.codex.subagents` — Official OpenAI Codex guidance for subagent workflows, parallel agents, orchestration, sandbox inheritance, and token-use caveats.
- `openai.codex.subagent_concepts` — Official OpenAI Codex concept guidance for context pollution, context rot, parallel analysis, and write-heavy workflow cautions.
- `openai.codex.models` — Official OpenAI Codex model source for volatile model-availability and model-configuration watchlist routing.
- `openai.help.truthfulness` — Official OpenAI Help Center truthfulness caveat for treating fluent answers as fallible and requiring verification.
- `openai.hallucinations` — Official OpenAI hallucination explainer for confident wrong-answer and guessing-incentive framing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, evidence, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.failure.hallucinated_apis`
- `vcb.failure.done_claim_without_evidence`
- `vcb.failure.context_pollution`
- `vcb.prompting.acceptance_criteria`
- `vcb.constraints.review_budget`

<!-- VCB:STOP_RETRIEVAL reason="ignoring-model-biases_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.ignoring_model_biases -->
