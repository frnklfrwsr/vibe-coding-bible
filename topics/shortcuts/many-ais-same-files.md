<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.many_ais_same_files version=0.25.0-draft.chunk24 -->
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
id: vcb.shortcut.many_ais_same_files
title: Many AIs on the Same Files
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- multi-AI workflows
- parallel agents
- subagents
- worktrees
- same-file edits
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- multi_ai
- parallel_agents
- integration
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
- one mutating implementer
- read-only reviewers
- branch/worktree isolation for parallel edits
- evidence-based integration table
shortcut_profiles:
- vcb.shortcut.many_ais_same_files
durable_principles:
- parallel analysis is safer than parallel mutation
- overlapping edits need ownership and integration
- selection must be evidence-based, not vibe-based
likely_to_change:
- Codex subagent visibility
- worktree and branch UI behavior
- model/tool availability across AI products
obsolete_when:
- agent tooling provides reliable file-ownership locking, conflict-aware integration, and provenance for every generated change
related_topics:
- vcb.codex.subagents
- vcb.codex.cloud
- vcb.workflow.reviewing_diffs
- vcb.constraints.review_budget
- vcb.failure.broad_refactor_drift
---

# Many AIs on the Same Files

> Summary:
> This shortcut is using multiple AI systems on the same files without one owner, one branch strategy, and one integration path.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.many_ais_same_files.human -->
## 1. For the Human: Plain-Language Concept

### What this means

You ask Codex, another AI, and maybe a browser agent to all work on the same code area. Each answer may be plausible, but the project now has no single source of truth for which change owns the file.

### Why it matters

Parallel help is useful for analysis. Parallel mutation of the same files creates merge conflicts, contradictory abstractions, duplicated fixes, and review fog.

### What good looks like

Good: “Use one AI as the mutating implementer. Use other AIs read-only for critique, test ideas, risk review, or alternative designs.”

### What bad looks like

Bad: “Let three agents edit the same component, then manually copy pieces together because each answer looked good in isolation.”

### Minimal example

Ask one agent to implement on a branch. Ask a second agent to review the diff only. Ask a third agent for test gaps. Do not let all three rewrite the same files.

### Checklist

- choose one mutating implementer
- keep other agents read-only
- separate branches/worktrees if multiple agents must edit
- compare by diff and tests, not prose
- make one human or agent the integrator

<!-- VCB:END_SECTION id=vcb.shortcut.many_ais_same_files.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.many_ais_same_files.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat multi-AI work like parallel branches: useful only when ownership and integration are explicit.

### Diagnostic questions

- Which agent is allowed to edit files?
- Which agents are review-only?
- Are any two agents touching the same file?
- Who integrates the final diff?
- What evidence decides between outputs?

### Coaching tactics

- assign roles before prompting
- use read-only critique agents for second opinions
- require each answer to cite files, assumptions, and checks
- serialize edits when files overlap

### Red flags

- copying code between AI outputs by taste
- multiple agents changing the same file without branch isolation
- accepting the answer with the nicest explanation
- no final integration review

### Prompt pattern

```text
Use one AI as implementer for this task. Use any other AI only as read-only reviewer. Return an integration table: file, owning agent, proposed change, evidence, conflicts, and final accept/reject decision.
```

<!-- VCB:END_SECTION id=vcb.shortcut.many_ais_same_files.ai_coach -->

## Shortcut Reality

### Ideal practice

One mutating path, multiple review signals, explicit integration, and artifact-backed selection.

### What people often do instead

People run the same task through several AIs and paste together the most convincing pieces.

### When the shortcut may be acceptable

Acceptable for tiny disposable prototypes when no persistent data, secrets, or production code are involved and a git checkpoint exists.

### When it becomes a bad trade

Bad for shared branches, migrations, auth, payments, stateful UI, dependency changes, or any file where partial integration can silently break behavior.

### Risk profile

- Probability: high when several AI subscriptions or tabs are available and the user is stuck.
- Impact: medium for conflicts; high for mixed abstractions and broken behavior.
- Recoverability: medium with branch checkpoints; low if pasted changes bypass diff review.

### Blast radius

The blast radius is the union of every file and assumption each AI touched, not just the final pasted snippet.

### Minimum guardrails

- one mutating implementer
- read-only reviewers
- branch/worktree isolation for parallel edits
- evidence-based integration table

### Recovery plan

- Stop all agents and commit or stash the current state.
- List files touched by each AI.
- Choose one base diff and revert the rest.
- Reapply only changes that survive tests and diff review.
- Write down the owner/integrator rule for the next run.

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

- parallel analysis is safer than parallel mutation
- overlapping edits need ownership and integration
- selection must be evidence-based, not vibe-based

## Volatile Surface

- Codex subagent visibility
- worktree and branch UI behavior
- model/tool availability across AI products

## Obsolescence Watch

This card should be revised if:

- agent tooling provides reliable file-ownership locking, conflict-aware integration, and provenance for every generated change

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
- `vcb.codex.cloud`
- `vcb.workflow.reviewing_diffs`
- `vcb.constraints.review_budget`
- `vcb.failure.broad_refactor_drift`

<!-- VCB:STOP_RETRIEVAL reason="many-ais-same-files_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.many_ais_same_files -->
