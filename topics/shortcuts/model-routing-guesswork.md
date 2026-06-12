<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.model_routing_guesswork version=0.25.0-draft.chunk24 -->
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
id: vcb.shortcut.model_routing_guesswork
title: Model-Routing Guesswork
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- model choice
- operating mode
- budget
- configuration
- team defaults
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- model_routing
- cost
- model_bias
- configuration
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: MODERATE_RISK_SHORTCUT
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- current official source check
- task/risk classification
- no exact values in stable prose
- usage-burn review
- same verification regardless of model
shortcut_profiles:
- vcb.shortcut.model_routing_guesswork
durable_principles:
- choose models by task and risk
- exact model availability is volatile
- verification remains necessary after model choice
likely_to_change:
- current Codex model catalog
- reasoning-level controls
- service tiers and plan packaging
- model-specific behavior
obsolete_when:
- Codex surfaces provide reliable automatic task-to-model routing with transparent cost/risk/evidence reporting
related_topics:
- vcb.codex.feature_maturity
- vcb.codex.changelog_monitoring
- vcb.constraints.operating_mode
- vcb.constraints.usage_burn
- vcb.constraints.review_budget
---

# Model-Routing Guesswork

> Summary:
> This shortcut is choosing a model, reasoning level, surface, or AI tool by brand feeling, stale advice, or price anxiety instead of current docs, task shape, risk, and evidence needs.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.model_routing_guesswork.human -->
## 1. For the Human: Plain-Language Concept

### What this means

The shortcut is treating model choice as folklore. Current model names, tiers, routing, context behavior, and feature availability can change, so hardcoded advice ages fast.

### Why it matters

The wrong model/surface choice can waste usage, miss needed reasoning, overkill simple work, or encourage unsafe delegation. Exact model availability belongs in current sources or dated snapshots, not stable prose.

### What good looks like

Good: “Choose by task shape: speed for small scoped edits, deeper reasoning for ambiguous/risky work, current official docs for feature availability, and verification for output quality.”

### What bad looks like

Bad: “Always use the biggest model for everything, or always use the cheapest model for production-risk work because a blog post said so months ago.”

### Minimal example

For a small rename, fast/local is fine. For auth refactor, choose a deeper reasoning mode, plan first, and verify with tests and review.

### Checklist

- check current official model/source docs
- choose by task difficulty and risk
- avoid frozen model recipes
- track usage burn
- validate output regardless of model

<!-- VCB:END_SECTION id=vcb.shortcut.model_routing_guesswork.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.model_routing_guesswork.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat model routing as a volatile configuration decision governed by task/risk, not identity or habit.

### Diagnostic questions

- What task shape is this?
- What risk level is involved?
- What current source confirms model availability?
- Is speed, reasoning depth, cost, or safety the binding constraint?

### Coaching tactics

- route simple tasks to cheaper/faster modes
- route ambiguous/high-risk tasks to plan-first deeper reasoning
- separate exact current values into snapshots
- make output verification model-independent

### Red flags

- hardcoded model names in stable guidance
- using price as the only selector
- using the largest model to avoid defining scope
- assuming a model change removes need for review

### Prompt pattern

```text
Help me choose a Codex operating mode/model posture for this task. Use current official docs only for product facts. Classify the task by scope, ambiguity, risk, verification needed, attention available, and usage burn. Do not hardcode exact pricing or model-routing claims into durable guidance.
```

<!-- VCB:END_SECTION id=vcb.shortcut.model_routing_guesswork.ai_coach -->

## Shortcut Reality

### Ideal practice

Model routing is current-source-checked, task-shaped, risk-aware, and followed by the same review discipline.

### What people often do instead

People use stale model rankings or pay for more model than the task needs because choosing feels hard.

### When the shortcut may be acceptable

Acceptable for disposable experiments if cost and review risk are small and no durable guidance is created.

### When it becomes a bad trade

Bad when model routing controls production-risk work, budget commitments, team defaults, or stable documentation without current source checks.

### Risk profile

- Probability: medium because model catalogs and plan packaging change.
- Impact: medium for waste; high if the wrong mode hides risk or enables unsafe automation.
- Recoverability: high for one-off choices; medium/low for team defaults or stale docs.

### Blast radius

Stale model-routing advice can spread through AGENTS.md, team docs, scripts, or habits and quietly degrade every future task.

### Minimum guardrails

- current official source check
- task/risk classification
- no exact values in stable prose
- usage-burn review
- same verification regardless of model

### Recovery plan

- Remove stale model claims from durable docs.
- Check current official sources.
- Reclassify recent failures by task/risk mismatch.
- Update config or prompt guidance.
- Move exact values to a dated snapshot if needed.

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

- choose models by task and risk
- exact model availability is volatile
- verification remains necessary after model choice

## Volatile Surface

- current Codex model catalog
- reasoning-level controls
- service tiers and plan packaging
- model-specific behavior

## Obsolescence Watch

This card should be revised if:

- Codex surfaces provide reliable automatic task-to-model routing with transparent cost/risk/evidence reporting

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for task context, constraints, done-when criteria, plan-first work, review, and verification.
- `openai.codex.subagents` — Official OpenAI Codex guidance for subagent workflows, parallel agents, orchestration, sandbox inheritance, and token-use caveats.
- `openai.codex.subagent_concepts` — Official OpenAI Codex concept guidance for context pollution, context rot, parallel analysis, and write-heavy workflow cautions.
- `openai.codex.models` — Official OpenAI Codex model source for volatile model-availability and model-configuration watchlist routing.
- `openai.help.truthfulness` — Official OpenAI Help Center truthfulness caveat for treating fluent answers as fallible and requiring verification.
- `openai.hallucinations` — Official OpenAI hallucination explainer for confident wrong-answer and guessing-incentive framing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, evidence, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.feature_maturity`
- `vcb.codex.changelog_monitoring`
- `vcb.constraints.operating_mode`
- `vcb.constraints.usage_burn`
- `vcb.constraints.review_budget`

<!-- VCB:STOP_RETRIEVAL reason="model-routing-guesswork_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.model_routing_guesswork -->
