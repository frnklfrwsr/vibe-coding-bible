<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.consensus_as_correctness version=0.25.0-draft.chunk24 -->
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
id: vcb.shortcut.consensus_as_correctness
title: Consensus as Correctness
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- AI consensus
- multi-model review
- technical claims
- estimates
- API claims
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- multi_ai
- model_bias
- evidence
- verification
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
- claim-by-claim verification
- independent evidence check
- one disconfirming pass
- same final checks as single-answer output
shortcut_profiles:
- vcb.shortcut.consensus_as_correctness
durable_principles:
- agreement is not proof
- shared premises can produce shared wrong answers
- artifact-backed verification wins over vote count
likely_to_change:
- model families and overlap
- tool support for independent context isolation
- run-comparison interfaces
obsolete_when:
- AI comparison tools can prove independence, cite evidence, and validate claims against the live codebase automatically
related_topics:
- vcb.failure.hallucinated_apis
- vcb.failure.done_claim_without_evidence
- vcb.workflow.testing
- vcb.workflow.codex_output_review
- vcb.shortcut.best_of_n_without_review
---

# Consensus as Correctness

> Summary:
> This shortcut is treating agreement between multiple AIs as proof that a claim, estimate, fix, or design is correct.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.consensus_as_correctness.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Consensus is a signal, not proof. Two models can agree because they share training patterns, copied context, the same false premise, or the same missing evidence.

### Why it matters

Agreement can reduce uncertainty only when the agents worked from independent evidence and their claims can be checked. Otherwise it just repeats the same guess in different words.

### What good looks like

Good: “Use AI consensus to identify what to inspect next. Require sources, file references, checks, or command output before accepting the claim.”

### What bad looks like

Bad: “Three AIs say a function exists, so you code against it without checking the library docs or local interface.”

### Minimal example

If multiple AIs agree a migration is safe, still inspect the schema, call sites, tests, and rollback path.

### Checklist

- ask what evidence each answer used
- check whether context was independent
- verify claims in code/docs/tests
- treat agreement as a prioritization hint
- require one executable or source-backed proof

<!-- VCB:END_SECTION id=vcb.shortcut.consensus_as_correctness.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.consensus_as_correctness.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that agreement is useful for triage but insufficient for acceptance.

### Diagnostic questions

- Did the AIs see the same context?
- Did any answer cite artifacts?
- Could they share the same false assumption?
- What check can falsify the consensus?

### Coaching tactics

- separate consensus from verification
- ask one model to attack the shared assumption
- inspect the cited files/docs
- turn agreement into a checklist of claims to verify

### Red flags

- “all the AIs agree” as the only evidence
- no one checked the actual repo
- consensus used to skip tests
- answers cite no files or command output

### Prompt pattern

```text
Multiple AI answers agree. Convert that consensus into a verification plan. List each shared claim, the evidence needed, the local file/doc/command to check, and whether the claim is verified, unverified, or contradicted.
```

<!-- VCB:END_SECTION id=vcb.shortcut.consensus_as_correctness.ai_coach -->

## Shortcut Reality

### Ideal practice

Consensus narrows the search space; verification decides correctness.

### What people often do instead

People treat agreement as a vote and let the vote replace proof.

### When the shortcut may be acceptable

Acceptable for low-stakes brainstorming or choosing which hypothesis to inspect first.

### When it becomes a bad trade

Bad when consensus justifies code changes, estimates, security claims, dependency choices, test weakening, or production decisions.

### Risk profile

- Probability: medium/high when users are overwhelmed by conflicting technical uncertainty.
- Impact: high when the shared wrong assumption reaches production code.
- Recoverability: medium if evidence review happens before merge; low if consensus bypasses review.

### Blast radius

Consensus can give one unsupported claim the social weight of several independent proofs even when no proof exists.

### Minimum guardrails

- claim-by-claim verification
- independent evidence check
- one disconfirming pass
- same final checks as single-answer output

### Recovery plan

- Identify the consensus claim.
- Trace which evidence each AI used.
- Verify claim in repo/docs/tests.
- Revert decisions based only on agreement.
- Document proof requirements for future consensus checks.

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

- agreement is not proof
- shared premises can produce shared wrong answers
- artifact-backed verification wins over vote count

## Volatile Surface

- model families and overlap
- tool support for independent context isolation
- run-comparison interfaces

## Obsolescence Watch

This card should be revised if:

- AI comparison tools can prove independence, cite evidence, and validate claims against the live codebase automatically

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
- `vcb.workflow.testing`
- `vcb.workflow.codex_output_review`
- `vcb.shortcut.best_of_n_without_review`

<!-- VCB:STOP_RETRIEVAL reason="consensus-as-correctness_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.consensus_as_correctness -->
