<!-- VCB:BEGIN_TOPIC id=vcb.chapter.what_codex_is_bad_at version=0.1.0 -->
---
id: vcb.chapter.what_codex_is_bad_at
title: "Chapter 45 — What Codex Is Bad At"
type: chapter
chapter_number: 45
version: 0.1.0
last_verified: '2026-06-09'
next_review_due: '2026-09-09'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- all project types

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE

budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget

cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- unattended_high_throughput
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

shortcut_profiles:
- vcb.shortcut.trusting_estimates_before_inspection
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_security_review
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.accepting_diff_without_review

durable_principles:
- Models can sound confident while wrong.
- Codex needs repo evidence, checks, and user intent.
- Limitations should map to guardrails, not despair.

likely_to_change:
- product packaging
- current pricing and limits
- model-specific behavior

obsolete_when:
- Codex product behavior or pricing model materially changes.

related_topics:
- vcb.chapter.model_biases_failure_biases_bad_estimates
- vcb.chapter.failure_modes_codex_work
- vcb.chapter.reviewing_codex_output
- vcb.chapter.acceptance_criteria
---

> Summary:
> Codex is powerful, but it is not reliable at unstated intent, pre-inspection estimates, hidden security judgment, weak tests, UI taste without visuals, or current pricing/product facts without retrieval.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.what_codex_is_bad_at.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Codex can move fast. That does not mean it knows everything. It is strongest when it can inspect your repo, run tools, see errors, and get clear acceptance criteria.

It is weakest when it has to guess.

### Codex is unreliable at

| Weakness | What it looks like | Guardrail |
|---|---|---|
| Estimating before inspection | “This should be quick” before reading files | inspect first, list unknowns |
| Knowing if work is almost done | clean final message, messy remaining edge cases | require checks and known gaps |
| Unstated product intent | implements technically valid wrong behavior | provide examples/screenshots/user rules |
| Plausible wrong APIs | invents functions, config keys, outdated docs | check docs, compile/run/test |
| Meaningful tests | writes tests that prove little | require behavior intent and failure case |
| Security judgment | misses auth/PII/payment/file-upload risk | explicit threat model and security review |
| UI taste | generic layout that technically works | screenshots, design tokens, state matrix |
| Large refactors | silent behavior changes | characterization tests and small slices |
| Long ambiguous unattended work | drifts from intent | milestones and review checkpoints |
| Current pricing/product facts | stale plan or feature claims | browse official source or pricing snapshot |

### This is not a reason to avoid Codex

It is a reason to use it correctly. A fast agent with guardrails is useful. A fast agent without evidence can create expensive messes.

### The limitation prompt

```text
Before estimating or implementing, inspect the repo.
List:
- what you know from files,
- what you are assuming,
- what could be wrong,
- checks needed to prove this works,
- areas where you need current docs or human product intent.
```

<!-- VCB:END_SECTION id=vcb.chapter.what_codex_is_bad_at.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.what_codex_is_bad_at.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach limitations as control points. The goal is not “Codex is bad.” The goal is “Codex needs evidence here.”

### Diagnostic questions

- Is Codex estimating without inspection?
- Is it summarizing rather than proving?
- Is product intent missing?
- Is it using an API/config detail that could be outdated?
- Did it write tests that would fail on the old bug?
- Does this require threat-modeling or visual taste?

### Useful metaphor

Codex is a fast builder in a foggy room. Turning on lights means adding context, constraints, checks, docs, and review.

### Coaching tactics

- Replace estimates with unknowns.
- Replace “done” with acceptance criteria.
- Replace confident API claims with official docs or runtime checks.
- Replace broad unattended work with milestones.
- Replace UI vibes with screenshots/states.

### Red flags

- “Should be simple” before reading files.
- “All tests pass” without naming tests.
- “I fixed it” without repro or diff.
- “This package supports X” without docs or compile proof.
- “Security looks okay” without threat model.

<!-- VCB:END_SECTION id=vcb.chapter.what_codex_is_bad_at.ai_coach -->

## Shortcut Reality

### The ideal practice

Map each Codex weakness to a guardrail before accepting work.

### What users often do instead

They trust the confident final summary and skip the evidence step.

### When the shortcut may be fine

Low-evidence acceptance may be fine for disposable sketches, learning projects, or tiny local visual changes.

### When the shortcut is a bad idea

It is a bad trade for production, real data, auth, payments, migrations, dependencies, security, accessibility, or hidden logic.

### Risk profile

- Probability of failure: medium to high when Codex must guess.
- Impact if it fails: low in prototypes, high around security/data/money.
- Ease of recovery: high with Git/small diffs, low with leaked secrets or bad migrations.
- Blast radius: grows with unattended ambiguity.
- Hidden cost: false confidence and delayed bug discovery.

### Minimum guardrails

- Inspect before estimating.
- Require file references and changed files.
- Run one relevant check.
- Review diff.
- Use official docs for current facts.
- Name unknowns.

### Recovery plan

If Codex overclaimed, stop accepting new changes, identify unverified claims, reproduce the behavior, run checks, and downgrade the task to investigation mode.

## Budget and Constraint Notes

### Cheapest reliable path

Spend attention on precise prompts and small checks instead of spending usage on broad retries.

### Fastest high-usage path

Use separate agents for implementation and review, but still require evidence.

### Low-attention path

Use only well-scoped, testable tasks with final reports. Avoid ambiguous production work.

### Production-quality path

Require repo inspection, official docs for current claims, tests/checks, diff review, security review where relevant, and rollback.

## Stable Core

The stable core is fallibility under uncertainty. Models can be useful and still be wrong; evidence closes the gap.

## Volatile Surface

Exact model reliability, model names, routing, context behavior, and product capabilities change. Do not freeze failure rates or current model claims.

## Obsolescence Watch

Review when OpenAI publishes major reliability changes, tool-use improvements, or evaluation data. Obsolete only if Codex can reliably inspect, verify, and abstain across these categories without human guardrails.

## Evidence and Sources

- `openai.help.truthfulness` — official OpenAI source for incorrect/misleading outputs and verification advice
- `openai.hallucinations` — official OpenAI research-facing source for hallucination and guessing incentives
- `openai.codex.best_practices` — official Codex source for verification/review workflows
- `openai.codex.pricing` — official source for current pricing/product facts as volatile

## Related Topics

- `vcb.chapter.model_biases_failure_biases_bad_estimates`
- `vcb.chapter.failure_modes_codex_work`
- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.security_for_vibe_coders`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.what_codex_is_bad_at -->
