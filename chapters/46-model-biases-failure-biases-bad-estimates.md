<!-- VCB:BEGIN_TOPIC id=vcb.chapter.model_biases_failure_biases_bad_estimates version=0.1.0 -->
---
id: vcb.chapter.model_biases_failure_biases_bad_estimates
title: "Chapter 46 — Model Biases, Failure Biases, and Bad Estimates"
type: chapter
chapter_number: 46
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
  pricing: STABLE

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
- vcb.shortcut.ignoring_model_biases
- vcb.shortcut.trusting_estimates_before_inspection
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.cherry_picking_ai_answers

durable_principles:
- Name the bias, then add a guardrail.
- Use bias labels diagnostically, not as insults.
- Bad estimates before inspection are guesses, not evidence.

likely_to_change:
- product packaging
- current pricing and limits
- model-specific behavior

obsolete_when:
- Codex product behavior or pricing model materially changes.

related_topics:
- vcb.chapter.what_codex_is_bad_at
- vcb.chapter.failure_modes_codex_work
- vcb.chapter.reviewing_codex_output
- vcb.chapter.risk_managed_shortcuts
---

> Summary:
> Codex failure modes are predictable enough to name. Bias labels help the AI coach diagnose behavior and immediately attach the right guardrail.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.model_biases_failure_biases_bad_estimates.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A bias is a predictable tilt. It does not mean Codex is malicious. It means the model often leans toward a certain kind of mistake unless you add a guardrail.

Bias labels help you catch the mistake early.

### Bias table

| Bias | What it looks like | Guardrail |
|---|---|---|
| Optimism bias | underestimates complexity | inspect repo and list unknowns |
| Completion bias | presents task as done too early | require checks, diff, known gaps |
| Plausibility bias | code looks right but fails | compile, run, test |
| Common-pattern bias | assumes popular framework conventions | point to actual files |
| Greenfield bias | rewrites instead of preserving behavior | state compatibility constraints |
| Compatibility bias | over-preserves old patterns in greenfield | state “greenfield; no legacy migration” |
| Package bias | adds dependencies quickly | require no-new-dependency first |
| Happy-path bias | misses loading/error/empty/mobile states | require state matrix |
| Test-satisfaction bias | tests pass but prove little | require behavior intent |
| Summary confidence bias | final message sounds cleaner than diff | review diff |
| Context anchoring | old task pollutes new task | reset and summarize context |
| Authority mimicry | sounds senior while guessing | demand evidence, sources, command output |

### Bad estimate prompt

```text
Do not estimate time yet.
First inspect the repo and identify unknowns.
Then give:
- known work,
- unknown work,
- likely hidden work,
- confidence level,
- what could multiply effort.
```

### Bias correction prompt

```text
Check your answer for optimism bias, completion bias, plausible API claims, weak tests, and unstated assumptions.
For each risk, name the evidence needed to verify it.
```

<!-- VCB:END_SECTION id=vcb.chapter.model_biases_failure_biases_bad_estimates.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.model_biases_failure_biases_bad_estimates.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Use bias labels as fast diagnostic tools. The right move is: name the bias, explain it plainly, and offer the immediate guardrail.

### Diagnostic questions

- Is the model guessing because it lacks evidence?
- Is the final answer cleaner than the diff?
- Did it choose a common convention without checking repo reality?
- Did it add a package before trying a local solution?
- Are tests proving behavior or only implementation details?

### Useful metaphors

- Optimism bias: planning a road trip without checking traffic.
- Summary confidence bias: reading the receipt instead of checking the groceries.
- Context anchoring: wearing yesterday’s glasses for today’s map.

### Coaching tactics

- Be direct: “That is optimism bias; Codex has not inspected enough.”
- Do not shame the user; add a guardrail.
- Make evidence concrete: files, command output, tests, screenshots, official docs.
- Prefer small corrective prompts over long lectures.

### Red flags

- Estimate before inspection.
- Done claim without changed-file list.
- “Probably” API/config details.
- Passing tests with deleted assertions.
- UI accepted without states/screenshots.
- Current pricing/model claims without source retrieval.

<!-- VCB:END_SECTION id=vcb.chapter.model_biases_failure_biases_bad_estimates.ai_coach -->

## Shortcut Reality

### The ideal practice

Check for predictable biases before accepting Codex output.

### What users often do instead

They accept the answer because it sounds senior, complete, and confident.

### When the shortcut may be fine

Skipping bias review may be fine for disposable work where failure is visible and cheap.

### When the shortcut is a bad idea

It is dangerous for hidden logic, production, auth, data, security, dependencies, or anything costly to undo.

### Risk profile

- Probability of failure: medium whenever evidence is weak.
- Impact if it fails: high when confidence masks hidden issues.
- Ease of recovery: high with small diffs/checkpoints, low with broad changes.
- Blast radius: grows with acceptance of unverified assumptions.
- Hidden cost: bugs discovered late because the answer sounded done.

### Minimum guardrails

- Ask for unknowns before estimates.
- Ask for evidence before acceptance.
- Review the diff.
- Run checks.
- Verify current facts against sources.
- Use a fresh review for high-risk changes.

### Recovery plan

If bias caused a bad change, identify which assumption failed, add a guardrail to `AGENTS.md` or a prompt template, revert or patch the diff, and add a check that catches the failure next time.

## Budget and Constraint Notes

### Cheapest reliable path

Use a short bias checklist before expensive retries.

### Fastest high-usage path

Use independent review agents to target specific bias classes: security, tests, dependencies, UI states, and compatibility.

### Low-attention path

Low-attention work must have explicit checks and final evidence. It cannot rely on confidence.

### Production-quality path

Require bias review as part of senior checklist, especially for estimates, current facts, security, tests, and large diffs.

## Stable Core

The specific model may improve, but the guardrail logic is stable: uncertainty, ambiguity, and missing evidence require verification.

## Volatile Surface

Exact failure rates, model-specific bias patterns, and current model names are volatile. Store only durable bias categories in stable prose.

## Obsolescence Watch

Review semiannually or when OpenAI publishes major reliability/hallucination changes. Obsolete only if models reliably abstain, cite current evidence, and self-calibrate without prompting.

## Evidence and Sources

- `openai.help.truthfulness` — official OpenAI source for confident but wrong outputs and verification advice
- `openai.hallucinations` — official OpenAI source on hallucinations and incentives to guess
- `openai.codex.best_practices` — official Codex source for verification and review controls
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for bias-to-guardrail mapping

## Related Topics

- `vcb.chapter.what_codex_is_bad_at`
- `vcb.chapter.failure_modes_codex_work`
- `vcb.chapter.reviewing_codex_output`
- `vcb.chapter.risk_managed_shortcuts`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.model_biases_failure_biases_bad_estimates -->
