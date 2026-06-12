<!-- VCB:BEGIN_TOPIC id=vcb.codex.subagents version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
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
evidence_scope: official OpenAI product behavior anchors plus VCB maintainer synthesis
  for risk, workflow, and coaching guidance
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
project_phases:
- prototype
- mvp
- production_build
- maintenance
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.codex.subagents
title: Codex Subagents
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Parallel analysis
- Review workflows
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.subagent_swarm
- vcb.shortcut.unreviewed_subagent_findings
- vcb.shortcut.conflicting_parallel_agents
durable_principles:
- subagents are best for independent analysis and review, not uncontrolled parallel
  editing
- the main thread must integrate results
- parallel work burns more usage and needs clearer boundaries
likely_to_change:
- subagent triggering and configuration
- available models for subagents
- subagent output format
- token/usage behavior
obsolete_when:
- Codex subagent workflows are deprecated or become automatic in ways that change
  human control assumptions
related_topics:
- vcb.chapter.subagents_parallel_thinking
- vcb.codex.cloud
- vcb.codex.automations
- vcb.concepts.diff
- vcb.chapter.model_biases_failure_biases_bad_estimates
---

> Summary:
> Subagents let Codex split work into specialized parallel agents, useful for independent investigation, tests, review, and summarization.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.subagents.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A subagent is another Codex worker focused on a subtask. One might inspect tests, another might review security risk, and the main agent can use their summaries to make a decision.

### Why it matters

Subagents matter because one long conversation can get noisy. Parallel analysis can reveal more without polluting the main thread. But multiple agents editing code at once can create conflicts and expensive chaos.

### The mental model

Subagents are scouts. They should bring back maps and warnings. They should not all start rebuilding the bridge at the same time.

### What good looks like

Good use: ask one subagent to inspect failing tests, another to review security implications, and the main agent to integrate findings before any patch.

### What bad looks like

Bad use: spawn five agents to edit the same feature files and then choose the nicest-sounding summary.

### Minimal example

Example: for a risky refactor, use subagents for read-only architecture mapping, test impact, and security review before the implementation agent edits anything.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.subagents.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.subagents.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach subagents as bounded parallel analysis with one integration owner.

### Diagnose the human’s current model

- Can the subtask be done independently?
- Should subagents be read-only?
- Who integrates findings?
- Are agents touching the same files?
- Is the usage cost justified?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

Subagents are a review panel, not a stampede.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Use subagents for read-only analysis only. Agent A: inspect tests. Agent B: inspect security/auth implications. Agent C: inspect dependency/build impact. Main agent: summarize conflicts and recommend the smallest safe path. Do not edit until I approve.
```

### Red flags to call out directly

- subagents editing same files
- best-of-N chosen without diff review
- no integration owner
- high usage spent on low-value parallelism

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.subagents.ai_coach -->

## Shortcut Reality

### The ideal practice

Use subagents for independent read-heavy analysis, triage, review, or summarization, then integrate findings deliberately.

### What users often do instead

Users often spawn many agents because it feels like intelligence scales linearly.

### When the shortcut may be fine

A small read-only swarm can be useful for exploration in a high-throughput budget.

### When the shortcut is a bad idea

Parallel write-heavy work is risky when files overlap, task boundaries are unclear, or human review is low-attention.

### Risk profile

- Probability of failure: Medium failure probability from conflicting findings, high cost in usage, high impact if multiple patches collide
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- prefer read-heavy subagents
- one concern per agent
- one integrator
- avoid parallel edits to same files
- review summaries against raw evidence when risk is high

### Recovery plan

Stop parallel editing, preserve raw findings, discard conflicting patches, choose one integration path, and rerun narrowly with branch isolation.

### AI coach guidance

Do not moralize the shortcut. Name the tradeoff, reduce blast radius, improve recoverability, and require the smallest guardrail that changes the risk profile.

## Budget and Constraint Notes

### Cheapest reliable path

Use this feature for one narrow task with curated context, conservative permissions, and one relevant check. Do not spend usage exploring broad unknowns unless the task is important enough to justify it.

### Fastest high-usage path

Use this feature aggressively only with branch/worktree isolation, clear acceptance criteria, structured final reports, and independent review for risky diffs.

### Low-attention path

Low-attention work requires stronger isolation, report-only or read-only posture when possible, fake credentials, and a final report that names files changed, checks run, unresolved risks, and review needs.

### Production-quality path

Use least privilege, clear done-when criteria, Git checkpoints, tests/build/lint where relevant, diff review, source-register discipline, and a rollback plan before accepting work.

## Stable Core

- subagents are best for independent analysis and review, not uncontrolled parallel editing
- the main thread must integrate results
- parallel work burns more usage and needs clearer boundaries

## Volatile Surface

- subagent triggering and configuration
- available models for subagents
- subagent output format
- token/usage behavior

## Obsolescence Watch

- Codex subagent workflows are deprecated or become automatic in ways that change human control assumptions

## Evidence and Sources

- `openai.codex.subagents` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.subagent_concepts` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.best_practices` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.subagents_parallel_thinking`
- `vcb.codex.cloud`
- `vcb.codex.automations`
- `vcb.concepts.diff`
- `vcb.chapter.model_biases_failure_biases_bad_estimates`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.subagents -->
