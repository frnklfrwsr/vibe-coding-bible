<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.subagent_swarm version=0.25.0-draft.chunk24 -->
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
id: vcb.shortcut.subagent_swarm
title: Subagent Swarm
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- subagents
- custom agents
- parallel analysis
- review swarms
- codebase exploration
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- multi_ai
- subagents
- context
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
- one question per subagent
- read-only first
- structured evidence output
- small agent count
- parent synthesis before mutation
shortcut_profiles:
- vcb.shortcut.subagent_swarm
durable_principles:
- parallel analysis needs scoped questions
- summary is not evidence
- write-capable agents need stronger boundaries
likely_to_change:
- subagent availability by surface
- custom-agent configuration
- token accounting and thread visibility
obsolete_when:
- subagent orchestration automatically limits redundant agents, enforces evidence schemas, and blocks write conflicts by default
related_topics:
- vcb.codex.subagents
- vcb.failure.context_pollution
- vcb.constraints.usage_burn
- vcb.constraints.review_budget
- vcb.shortcut.many_ais_same_files
---

# Subagent Swarm

> Summary:
> This shortcut is spawning many subagents or custom agents before each has a bounded question, role, context, output format, and integration plan.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.subagent_swarm.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Subagents can isolate context and parallelize analysis. The shortcut is turning uncertainty into a swarm instead of a small set of named questions.

### Why it matters

More agents consume more tokens, create more outputs to review, and can amplify confusion if their findings are not triaged. Parallel thinking is not free review.

### What good looks like

Good: “Use one subagent per explicit concern, such as security, tests, race conditions, or maintainability, and require evidence-backed findings.”

### What bad looks like

Bad: “Spawn ten agents for a vague refactor, then accept the consolidated summary without checking the underlying evidence.”

### Minimal example

For a PR review, spawn agents for security, test gaps, and maintainability. Each must output severity, files, evidence, and confidence; the main agent synthesizes without editing.

### Checklist

- use subagents only for separable concerns
- make most subagents read-only
- define output schema
- limit count
- triage findings before mutation

<!-- VCB:END_SECTION id=vcb.shortcut.subagent_swarm.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.subagent_swarm.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use subagents as scoped analysts, not as a swarm of unsupervised implementers.

### Diagnostic questions

- What question does each subagent answer?
- Is the concern independent?
- Can the subagent mutate files?
- What output schema makes findings reviewable?
- Who synthesizes conflicts?

### Coaching tactics

- start with two or three analysts
- use severity/evidence/confidence fields
- forbid mutation unless explicitly required
- merge findings through one parent agent or human

### Red flags

- subagents are spawned because the task is vague
- agents have overlapping missions
- findings lack file evidence
- the consolidated summary replaces evidence review

### Prompt pattern

```text
Spawn at most three read-only subagents. Assign one question per agent. Each output must include files inspected, claim, severity, evidence, confidence, and recommended next check. Parent agent must synthesize conflicts and not edit code until I approve.
```

<!-- VCB:END_SECTION id=vcb.shortcut.subagent_swarm.ai_coach -->

## Shortcut Reality

### Ideal practice

Subagents divide analysis into clear questions and return evidence packets that the parent/human can verify.

### What people often do instead

People spawn more agents when they should first narrow the task, gather context, or define done.

### When the shortcut may be acceptable

Acceptable for read-heavy codebase exploration or PR review when outputs are structured and mutation is disabled.

### When it becomes a bad trade

Bad when subagents mutate code, share unclear scope, touch secrets, operate with broad permissions, or produce summaries without inspectable evidence.

### Risk profile

- Probability: medium when subagent features are easy to trigger.
- Impact: medium for token burn and confusion; high for write-capable swarms.
- Recoverability: high for read-only findings; medium/low for overlapping write agents.

### Blast radius

A swarm can spread context pollution and unsupported claims across many outputs, making the final summary feel more authoritative than it is.

### Minimum guardrails

- one question per subagent
- read-only first
- structured evidence output
- small agent count
- parent synthesis before mutation

### Recovery plan

- Stop spawning new agents.
- Collect all subagent outputs.
- Discard unsupported findings.
- Group conflicts by file/claim.
- Run a smaller targeted follow-up with explicit questions.

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

- parallel analysis needs scoped questions
- summary is not evidence
- write-capable agents need stronger boundaries

## Volatile Surface

- subagent availability by surface
- custom-agent configuration
- token accounting and thread visibility

## Obsolescence Watch

This card should be revised if:

- subagent orchestration automatically limits redundant agents, enforces evidence schemas, and blocks write conflicts by default

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for task context, constraints, done-when criteria, plan-first work, review, and verification.
- `openai.codex.subagents` — Official OpenAI Codex guidance for subagent workflows, parallel agents, orchestration, sandbox inheritance, and token-use caveats.
- `openai.codex.subagent_concepts` — Official OpenAI Codex concept guidance for context pollution, context rot, parallel analysis, and write-heavy workflow cautions.
- `openai.codex.models` — Official OpenAI Codex model source for volatile model-availability and model-configuration watchlist routing.
- `openai.help.truthfulness` — Official OpenAI Help Center truthfulness caveat for treating fluent answers as fallible and requiring verification.
- `openai.hallucinations` — Official OpenAI hallucination explainer for confident wrong-answer and guessing-incentive framing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, evidence, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.subagents`
- `vcb.failure.context_pollution`
- `vcb.constraints.usage_burn`
- `vcb.constraints.review_budget`
- `vcb.shortcut.many_ais_same_files`

<!-- VCB:STOP_RETRIEVAL reason="subagent-swarm_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.subagent_swarm -->
