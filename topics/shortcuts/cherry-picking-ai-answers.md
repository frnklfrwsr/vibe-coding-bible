<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.cherry_picking_ai_answers version=0.25.0-draft.chunk24 -->
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
id: vcb.shortcut.cherry_picking_ai_answers
title: Cherry-Picking AI Answers
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- AI answer selection
- decision review
- estimates
- security shortcuts
- dependency shortcuts
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- answer_selection
- model_bias
- confirmation_bias
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
- explicit decision rubric
- red-team answer required
- artifact evidence before acceptance
- record rejected risks
shortcut_profiles:
- vcb.shortcut.cherry_picking_ai_answers
durable_principles:
- humans cherry-pick convenient evidence
- AI confidence can amplify confirmation bias
- risk review must include disconfirming evidence
likely_to_change:
- model tone and refusal style
- available comparison tools
- product UI for run comparison
obsolete_when:
- AI tools reliably surface contradictory evidence, show confidence calibration, and block unsupported acceptance decisions
related_topics:
- vcb.failure.done_claim_without_evidence
- vcb.failure.hallucinated_apis
- vcb.constraints.review_budget
- vcb.prompting.acceptance_criteria
- vcb.shortcut.best_of_n_without_review
---

# Cherry-Picking AI Answers

> Summary:
> This shortcut is choosing the answer that confirms your preferred plan instead of the answer with the best evidence.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.cherry_picking_ai_answers.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Cherry-picking happens when you ask several AIs, ignore the inconvenient warnings, and keep the output that says your shortcut is fine.

### Why it matters

This turns AI from a reasoning tool into a permission machine. It is especially dangerous when the user wants to skip tests, add dependencies, ignore security, or estimate work they have not inspected.

### What good looks like

Good: “Ask for disconfirming evidence and make the chosen answer cite artifacts, not vibes.”

### What bad looks like

Bad: “Keep re-prompting until one AI says the migration is easy, then proceed without reading the codebase.”

### Minimal example

If one answer says “safe” and another says “auth edge cases likely,” inspect the auth paths. Do not choose “safe” because it is more convenient.

### Checklist

- state the decision before asking
- ask what would change the decision
- require evidence against the preferred answer
- compare risks, not reassurance
- log why the rejected answer was rejected

<!-- VCB:END_SECTION id=vcb.shortcut.cherry_picking_ai_answers.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.cherry_picking_ai_answers.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to notice when they are using AI to launder a decision they already wanted.

### Diagnostic questions

- Which answer do you want to be true?
- What evidence would prove it wrong?
- Did any model mention a risk you are ignoring?
- Are you asking for permission or analysis?

### Coaching tactics

- force a red-team pass
- ask for strongest objection first
- separate ideation from decision
- require evidence for yes/no advice

### Red flags

- the human says “another AI said it was fine”
- warnings are treated as overcautious
- the easiest answer wins
- the user reruns until the answer changes

### Prompt pattern

```text
I may be cherry-picking. Challenge my preferred answer. List evidence that supports it, evidence against it, unknowns that matter, checks to run, and the smallest safe next step. Do not optimize for reassurance.
```

<!-- VCB:END_SECTION id=vcb.shortcut.cherry_picking_ai_answers.ai_coach -->

## Shortcut Reality

### Ideal practice

Use multiple AI answers to expose disagreement and risk, then resolve with inspection and checks.

### What people often do instead

People keep the answer that lowers effort and discard answers that increase work.

### When the shortcut may be acceptable

Acceptable only for low-stakes ideation, naming, copy, or disposable experiments where wrongness is cheap.

### When it becomes a bad trade

Bad when the shortcut affects real users, tests, estimates, dependencies, security, production, data, or architecture.

### Risk profile

- Probability: high because users naturally prefer convenient answers.
- Impact: medium to severe depending on the decision being rationalized.
- Recoverability: medium if caught before mutation; low if the decision commits architecture or data changes.

### Blast radius

The blast radius is the decision hidden behind the AI answer, not the answer itself.

### Minimum guardrails

- explicit decision rubric
- red-team answer required
- artifact evidence before acceptance
- record rejected risks

### Recovery plan

- Pause the decision.
- Write the preferred answer and ignored warnings.
- Inspect the evidence source.
- Run the smallest disconfirming check.
- Choose the next step based on risk and proof, not reassurance.

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

- humans cherry-pick convenient evidence
- AI confidence can amplify confirmation bias
- risk review must include disconfirming evidence

## Volatile Surface

- model tone and refusal style
- available comparison tools
- product UI for run comparison

## Obsolescence Watch

This card should be revised if:

- AI tools reliably surface contradictory evidence, show confidence calibration, and block unsupported acceptance decisions

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for task context, constraints, done-when criteria, plan-first work, review, and verification.
- `openai.codex.subagents` — Official OpenAI Codex guidance for subagent workflows, parallel agents, orchestration, sandbox inheritance, and token-use caveats.
- `openai.codex.subagent_concepts` — Official OpenAI Codex concept guidance for context pollution, context rot, parallel analysis, and write-heavy workflow cautions.
- `openai.codex.models` — Official OpenAI Codex model source for volatile model-availability and model-configuration watchlist routing.
- `openai.help.truthfulness` — Official OpenAI Help Center truthfulness caveat for treating fluent answers as fallible and requiring verification.
- `openai.hallucinations` — Official OpenAI hallucination explainer for confident wrong-answer and guessing-incentive framing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, evidence, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.failure.done_claim_without_evidence`
- `vcb.failure.hallucinated_apis`
- `vcb.constraints.review_budget`
- `vcb.prompting.acceptance_criteria`
- `vcb.shortcut.best_of_n_without_review`

<!-- VCB:STOP_RETRIEVAL reason="cherry-picking-ai-answers_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.cherry_picking_ai_answers -->
