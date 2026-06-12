<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.best_of_n_without_review version=0.25.0-draft.chunk24 -->
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
id: vcb.shortcut.best_of_n_without_review
title: Best-of-N Without Review
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- best-of-N prompting
- model comparison
- AI answer selection
- diff review
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- answer_selection
- multi_ai
- review
- evidence
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
- selection rubric before answers
- same evidence requirements for all candidates
- diff/check review for winner
- document rejected alternatives briefly
shortcut_profiles:
- vcb.shortcut.best_of_n_without_review
durable_principles:
- search diversity does not equal correctness
- selection needs a rubric
- confidence is not evidence
likely_to_change:
- model behavior and presentation style
- available model choices
- tool support for comparing runs
obsolete_when:
- multi-run tools provide verified candidate scoring with reproducible checks, diff comparison, and uncertainty calibration
related_topics:
- vcb.workflow.reviewing_diffs
- vcb.failure.done_claim_without_evidence
- vcb.constraints.review_budget
- vcb.shortcut.cherry_picking_ai_answers
- vcb.shortcut.consensus_as_correctness
---

# Best-of-N Without Review

> Summary:
> This shortcut is asking several AIs for answers, then accepting the one that looks best without checking diffs, tests, source evidence, or risks.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.best_of_n_without_review.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Best-of-N can be useful when you compare attempts by evidence. The shortcut is treating “the best sounding answer” as the best answer.

### Why it matters

LLM outputs are optimized to be helpful and coherent. The most persuasive option may be the one that hides uncertainty best.

### What good looks like

Good: “Compare candidates using a rubric: changed files, tests run, assumptions, risk, rollback, and acceptance criteria.”

### What bad looks like

Bad: “Pick the answer with the cleanest prose or most confident estimate without checking whether it actually works.”

### Minimal example

For three bug-fix candidates, require each to show repro, root cause, changed files, test command, and remaining risks. Pick the one with evidence, not the prettiest explanation.

### Checklist

- define the comparison rubric first
- require artifact evidence from each answer
- reject answers with unsupported claims
- review diffs before choosing
- run the same verification command on the winner

<!-- VCB:END_SECTION id=vcb.shortcut.best_of_n_without_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.best_of_n_without_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to convert multi-answer choice into a review process, not a taste contest.

### Diagnostic questions

- What is the selection rubric?
- Which answer has file-level evidence?
- Which answer ran or proposed the closest check?
- Which answer states uncertainty?
- Which answer is easiest to rollback?

### Coaching tactics

- score answers against acceptance criteria
- ask each AI for disconfirming evidence
- hide author/model names during review when possible
- run the same smoke check on finalists

### Red flags

- choosing by tone
- choosing by model brand
- choosing the shortest answer because it feels clean
- no negative evidence requested

### Prompt pattern

```text
Compare these AI-generated solutions. Score each on correctness evidence, changed files, tests/checks, unstated assumptions, security risk, rollback, and maintenance cost. Do not choose a winner until you state the evidence gap for each option.
```

<!-- VCB:END_SECTION id=vcb.shortcut.best_of_n_without_review.ai_coach -->

## Shortcut Reality

### Ideal practice

Use multiple attempts to widen search, then use one evidence rubric to narrow selection.

### What people often do instead

People ask several AIs and pick the answer that matches what they hoped was true.

### When the shortcut may be acceptable

Acceptable for copy, throwaway snippets, or ideation where no persistent system behavior changes.

### When it becomes a bad trade

Bad for production changes, dependencies, security, data, tests, estimates, or unfamiliar code where plausibility is cheap and evidence matters.

### Risk profile

- Probability: high when the user is uncertain or deadline-pressured.
- Impact: high if the selected answer changes code, tests, or architecture.
- Recoverability: medium when diff review exists; low when pasted directly.

### Blast radius

Best-of-N without review can import the hidden failure mode of the most persuasive answer into the project.

### Minimum guardrails

- selection rubric before answers
- same evidence requirements for all candidates
- diff/check review for winner
- document rejected alternatives briefly

### Recovery plan

- Recover the original state from git.
- List candidate answers and evidence gaps.
- Run the same verification on each viable candidate.
- Select by artifact evidence.
- Preserve the review rubric for future comparisons.

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

- search diversity does not equal correctness
- selection needs a rubric
- confidence is not evidence

## Volatile Surface

- model behavior and presentation style
- available model choices
- tool support for comparing runs

## Obsolescence Watch

This card should be revised if:

- multi-run tools provide verified candidate scoring with reproducible checks, diff comparison, and uncertainty calibration

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for task context, constraints, done-when criteria, plan-first work, review, and verification.
- `openai.codex.subagents` — Official OpenAI Codex guidance for subagent workflows, parallel agents, orchestration, sandbox inheritance, and token-use caveats.
- `openai.codex.subagent_concepts` — Official OpenAI Codex concept guidance for context pollution, context rot, parallel analysis, and write-heavy workflow cautions.
- `openai.codex.models` — Official OpenAI Codex model source for volatile model-availability and model-configuration watchlist routing.
- `openai.help.truthfulness` — Official OpenAI Help Center truthfulness caveat for treating fluent answers as fallible and requiring verification.
- `openai.hallucinations` — Official OpenAI hallucination explainer for confident wrong-answer and guessing-incentive framing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, evidence, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.reviewing_diffs`
- `vcb.failure.done_claim_without_evidence`
- `vcb.constraints.review_budget`
- `vcb.shortcut.cherry_picking_ai_answers`
- `vcb.shortcut.consensus_as_correctness`

<!-- VCB:STOP_RETRIEVAL reason="best-of-n-without-review_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.best_of_n_without_review -->
