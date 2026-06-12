<!-- VCB:BEGIN_TOPIC id=vcb.chapter.subagents_parallel_thinking version=0.1.0 -->
---
id: vcb.chapter.subagents_parallel_thinking
title: "Chapter 28 — Subagents: Parallel Thinking Without Parallel Chaos"
type: chapter
chapter_number: 28
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- subagents
- custom agents
- codebase exploration
- review workflows
- planning workflows
- high-throughput work

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE

budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget

cost_postures:
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
- vcb.shortcut.subagent_swarm
- vcb.shortcut.parallel_editing_same_files
- vcb.shortcut.best_of_n_without_review
- vcb.shortcut.unattended_long_runs

durable_principles:
- Use subagents for independent analysis more often than independent mutation.
- Each subagent needs one bounded job and one return format.
- The main agent or human must integrate results.
- Parallel agent work increases cost and coordination burden.

likely_to_change:
- subagent invocation mechanics
- custom-agent configuration fields
- subagent visibility across Codex surfaces
- model-selection options
- token/usage economics

obsolete_when:
- Codex changes subagent spawning, visibility, or custom-agent configuration materially.
- Subagent workflows become automatic/default rather than explicitly requested.
- Official guidance changes on where subagents are surfaced.

related_topics:
- vcb.chapter.cloud_delegation_parallel_work
- vcb.chapter.context_management
- vcb.chapter.reviewing_codex_output
- vcb.chapter.security_for_vibe_coders
- vcb.chapter.codex_config_defaults
- vcb.codex.subagents
- vcb.workflow.reviewing_diffs
---

> Summary:
> Subagents are specialized agents that work in parallel and return distilled results to the main thread. They are useful for independent investigation and review, but they create chaos when multiple agents edit the same thing without an integration plan.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.subagents_parallel_thinking.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Subagents are helper agents. Instead of one Codex thread trying to think about everything, you can ask Codex to send smaller jobs to specialized agents and collect their answers.

A subagent might review security, inspect tests, map a code path, compare two approaches, or investigate a failure. The main thread stays cleaner because it receives the conclusion instead of every intermediate note.

### Why it matters

Subagents can make big tasks faster and cleaner. They can also burn usage and produce conflicting advice.

Use them when the work can be split by concern:

- security review;
- test review;
- dependency review;
- architecture map;
- frontend state matrix;
- performance suspicion;
- docs impact;
- unknown-codebase exploration.

Do not use them as a swarm of unsupervised coders all changing the same files.

### The mental model

Subagents are a panel of specialists. The security specialist should not rewrite your UI. The test specialist should not redesign auth. The architect should not commit a patch behind everyone else.

The main agent is the editor-in-chief. It receives the specialist reports, resolves conflicts, and decides what work should actually happen.

### Good subagent jobs

Good:

```text
Ask one subagent to inspect auth/security risks.
Ask one subagent to inspect test coverage and weak assertions.
Ask one subagent to map the data flow.
Then consolidate the findings by severity.
```

Bad:

```text
Ask five subagents to each implement the same feature and merge whatever looks best.
```

Best-of-N can be useful for prototypes, but production code still needs review, tests, and a choice based on evidence.

### Return formats matter

Subagents should return short, structured output:

- finding;
- evidence/file reference;
- severity;
- recommended action;
- uncertainty;
- whether it blocks merge.

Without a return format, you get parallel noise.

### What good looks like

A good subagent workflow has:

- one clear job per agent;
- no overlapping edit ownership;
- read-only analysis unless mutation is explicitly safe;
- short return format;
- findings ranked by severity;
- a single integration decision;
- a human or main agent reviewing conflicts.

### Checklist

Before using subagents:

- Can this task be split cleanly?
- What is each agent’s job?
- Should the job be read-only?
- What output format do I need?
- Who integrates the results?
- What files are off-limits?
- Is the usage cost justified?

<!-- VCB:END_SECTION id=vcb.chapter.subagents_parallel_thinking.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.subagents_parallel_thinking.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach subagents as bounded specialists, not as a magic swarm. Bias toward read-only analysis and independent review before parallel editing.

### Diagnose the human’s current model

Ask:

- “What problem needs parallel perspectives?”
- “Are these jobs independent?”
- “Should the subagents edit files or only report?”
- “What return format should each use?”
- “Who resolves disagreements?”
- “Can the user afford the extra usage?”
- “Would a single focused pass be enough?”

### Explanation strategy

Route by task type:

- Exploration: subagents are useful.
- Review: subagents are useful.
- Implementation: subagents are useful only if boundaries are separate.
- Same-file editing: usually bad.
- Security/production: prefer read-only specialists first.

### Useful metaphors

- Subagents are consultants, not a mob.
- The main thread is the meeting room; subagents go do fieldwork and bring back notes.
- Parallel editing without ownership is five people holding one steering wheel.

### Coaching tactics

- Suggest subagents when the task has separable concerns.
- Keep each job small and named.
- Make every subagent cite files, commands, or observations.
- Consolidate findings by severity and confidence.
- Prevent agents from editing the same files unless one is clearly the integrator.
- For constrained users, recommend one high-value reviewer instead of many agents.

### Prompt patterns

```text
Use subagents for read-only analysis only.

Main task:
[task]

Spawn these bounded subagent jobs:
1. Security reviewer: inspect auth/secrets/user-data risk. Return blockers first.
2. Test reviewer: inspect changed tests and missing regression coverage.
3. Architecture mapper: identify affected files and data flow.

Each subagent must return:
- findings,
- evidence/file references,
- severity,
- uncertainty,
- recommended next step.

Do not let subagents edit files.
Consolidate into one prioritized report.
```

```text
Before using subagents, decide whether this work can be split by file ownership. If not, use one agent to implement and a separate fresh agent to review.
```

### Red flags to call out directly

- “Subagents are not free; they consume extra usage.”
- “Do not send multiple agents to edit the same files.”
- “A pile of findings is not a decision.”
- “Use read-only subagents first for security-sensitive work.”
- “Best-of-N code still needs evidence and review.”

### Exercises

1. Take one feature and split it into analysis-only subagent jobs.
2. Write a return format for each job.
3. Classify findings as blocker/non-blocker.
4. Pick one integrator.
5. Decide whether any subagent should edit files.

<!-- VCB:END_SECTION id=vcb.chapter.subagents_parallel_thinking.ai_coach -->

## Shortcut Reality

### The ideal practice

Use a small number of bounded subagents for independent analysis or review, then integrate their findings through one main thread and one human decision.

### What users often do instead

They create a swarm because it feels powerful, ask everyone to explore or implement broadly, then end up with conflicting patches, repeated work, and a noisy main thread.

### When the shortcut may be fine

A subagent swarm can be useful in a disposable research/prototype context where the goal is divergent ideas, not a clean merge.

### When the shortcut is a bad idea

It is a bad idea when multiple agents can mutate the same files, when findings cannot be reviewed, when the task involves production secrets/data, or when the user is budget-constrained and one focused pass would work.

### Risk profile

- Probability of failure: medium; high with overlapping edit ownership.
- Impact if it fails: low for reports, high for conflicting patches or security-sensitive edits.
- Ease of recovery: high for read-only findings; medium/low for conflicting mutations.
- Blast radius: context quality, usage budget, changed files, merge conflicts.
- Skill needed to recover: medium for integration, high for conflicting production changes.
- Hidden cost: token burn, review fatigue, false consensus, duplicated work.

### Minimum guardrails

- One job per subagent.
- Prefer read-only analysis.
- Require evidence/file references.
- Use a fixed return format.
- Keep one integrator.
- Do not allow overlapping file edits.
- Review findings before acting.

### Recovery plan

1. Stop all broad agent work.
2. Collect reports only.
3. Discard conflicting patches.
4. Pick one implementation path.
5. Re-run one focused agent task.
6. Add boundaries to future prompts or config.

### AI coach guidance

Use subagents when they reduce context pollution or add genuinely independent perspectives. Do not recommend subagents for every task. Extra agents are justified by independent value, not by novelty.

## Budget and Constraint Notes

### Cheapest reliable path

Use one focused agent plus one fresh review pass. Avoid subagents unless the task is complex enough to justify the usage.

### Fastest high-usage path

Use subagents for parallel exploration, security/test/docs review, and best-of-N spikes. Keep implementation ownership isolated.

### Low-attention path

Low-attention subagent work should be read-only and return a consolidated report. Do not let several agents mutate production-sensitive files while the human is absent.

### Production-quality path

Use subagents as reviewers and investigators. Merge only through one implementation branch with tests, diff review, and clear owner decisions.

## Stable Core

- Independent perspectives can catch more issues.
- Parallelism needs boundaries.
- Context pollution hurts agent reliability.
- Findings need evidence and severity.
- Integration is a separate job.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Subagent availability, invocation mechanics, custom-agent configuration, visibility across Codex surfaces, model options, and usage economics are volatile. Verify official Codex docs before giving exact operational instructions.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex changes subagent triggering, custom-agent configuration, subagent visibility in the IDE/app/CLI, or default behavior around automatic spawning.

## Evidence and Sources

- `openai.codex.subagents` — official OpenAI source for subagent workflows, parallel specialized agents, custom agents, availability, and token-use caveats.
- `openai.codex.subagent_concepts` — official OpenAI source for context-pollution tradeoffs, parallel analysis, bounded work, and main-thread consolidation.
- `openai.codex.customization` — official OpenAI source for how subagents fit with other Codex customization layers.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: independent review is useful only when findings are integrated through a single decision path.

## Related Topics

- vcb.chapter.cloud_delegation_parallel_work
- vcb.chapter.context_management
- vcb.chapter.reviewing_codex_output
- vcb.chapter.security_for_vibe_coders
- vcb.chapter.codex_config_defaults
- vcb.codex.subagents
- vcb.workflow.reviewing_diffs

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.subagents_parallel_thinking -->
