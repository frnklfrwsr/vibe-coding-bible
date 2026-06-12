<!-- VCB:BEGIN_TOPIC id=vcb.prompting.context_management version=0.1.0 -->
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
evidence_scope: official OpenAI Codex prompting/workflow anchors plus VCB maintainer synthesis
  for risk, budget, and coaching guidance
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
id: vcb.prompting.context_management
title: Context Management
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- Large repositories
- Long sessions
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.context_dumping
- vcb.shortcut.vague_prompt
- vcb.shortcut.cloud_task_without_context
durable_principles:
- relevance beats volume
- fresh context beats stale assumptions
- context must include constraints and evidence, not just files
likely_to_change:
- context window behavior
- compaction behavior
- IDE selected-context mechanics
- cloud environment context visibility
- supported attachments
obsolete_when:
- agentic coding systems can always infer the exact relevant context without user selection,
  summaries, or constraints
related_topics:
- vcb.chapter.context_management
- vcb.prompting.four_part_prompt
- vcb.prompting.plan_first
- vcb.workflow.unknown_codebase
- vcb.codex.ide_extension
- vcb.codex.cloud
- vcb.codex.agents_md
---

> Summary:
> Context management is the discipline of giving Codex enough relevant information to act without drowning it in unrelated text.

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

<!-- VCB:BEGIN_SECTION id=vcb.prompting.context_management.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Context management means choosing the right files, logs, commands, errors, constraints, and history for Codex. More context is not automatically better. Relevant context is better.

### Why it matters

Codex fails when it sees too little, sees stale information, or sees so much noise that the important signal gets buried. Context is the map you hand the agent.

### The mental model

Context is a spotlight, not a landfill. Aim it at the problem; do not dump the whole garage into the prompt.

### What good looks like

Good: include the failing stack trace, the two files involved, the route that triggers the issue, the test command, and “do not change public API.”

### What bad looks like

Bad: paste ten unrelated files, old logs, and a vague request, then expect Codex to infer the bug.

### Minimal example

Context pack: current behavior, expected behavior, exact error, relevant files, recent changes, commands already run, constraints, and unknowns.

### Checklist

- include the smallest set of relevant files
- include fresh errors or logs
- state what Codex cannot see, such as local-only state
- remove unrelated historical chat
- refresh context after major discovery or compaction
<!-- VCB:END_SECTION id=vcb.prompting.context_management.human -->

<!-- VCB:BEGIN_SECTION id=vcb.prompting.context_management.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to curate context as an operating surface, not as a dumping ground.

### Diagnose the human’s current model

- What does Codex need to know to avoid guessing?
- Which files are necessary and which are distracting?
- Is there stale context in the conversation?
- Does the cloud or remote surface have the same context as the local environment?
- What should Codex ask before editing?

### Explanation strategy

Build a context pack before complex tasks. Ask Codex to identify missing context during planning. Prefer focused selections, linked files, current logs, and explicit constraints over large unstructured dumps.

### Useful metaphor

Good context is a crime-scene packet. It includes the scene, evidence, and constraints; it does not include every newspaper from the last year.

### Coaching tactics

- summarize long background into current facts
- include exact errors, not paraphrases
- separate facts from assumptions
- remove outdated instructions after pivots
- ask Codex what context it lacks before implementation

### Prompt patterns

```text
Use only these files unless you explain why more are needed: [files]. Current error: [error]. Expected behavior: [expected]. Constraints: [constraints].
Before editing, list any missing context that would change the plan.
The previous assumption was wrong. Ignore earlier direction about [x]. Updated context: [new facts].
```

### Red flags to call out directly

- massive paste with no labels
- old error messages after code changed
- cloud task depends on uncommitted local files
- ambiguous “same as before” references
- Codex confidently edits files it never inspected

### Exercises

- Have the human trim a bloated prompt to a context pack.
- Ask Codex to list missing context and compare it to the user’s pack.
- Practice updating context after a failed attempt without carrying stale assumptions.
<!-- VCB:END_SECTION id=vcb.prompting.context_management.ai_coach -->

## Shortcut Reality

### The ideal practice

Provide compact, fresh, relevant context and update it when reality changes.

### What users often do instead

Users often dump everything or provide almost nothing.

### When the shortcut may be fine

Thin context is fine for simple syntax questions, isolated files, or disposable experiments. Broad context is fine for read-only exploration if it is labeled.

### When the shortcut is a bad idea

Bad context is dangerous for bug fixes, unfamiliar codebases, cloud tasks, migrations, and production changes.

### Risk profile

- Probability of failure: Medium failure probability with stale or noisy context; high when the task depends on unseen local state.
- Impact if it fails: Impact ranges from wasted usage to wrong production behavior.
- Ease of recovery: Good if context is corrected before merge; worse when the agent has already spread a false assumption across files.
- Blast radius: The blast radius is every file Codex edits based on missing or stale information.
- Skill needed to recover: Low for creating context packs; medium for recovering from false-assumption diffs.
- Hidden cost: Token waste, compaction drift, repeated failed attempts, and hidden dependency on local-only state.

### Minimum guardrails

- label context by type
- include exact errors
- state freshness of logs
- avoid unrelated file dumps
- ask for missing context before editing

### Recovery plan

- Stop the run.
- Write a fresh context pack.
- Mark old assumptions as obsolete.
- Ask Codex to compare new context to current diff.
- Revert or narrow changes based on the corrected context.

## Budget and Constraint Notes

### Cheapest reliable path

Spend tokens on relevant files and exact errors, not long chat history.

### Fastest high-usage path

Use reusable context-pack templates for bug, feature, refactor, and test tasks.

### Low-attention path

Low-attention work needs complete context up front because the agent cannot ask you at the right moment if you are gone.

### Production-quality path

Production context must include constraints, rollback concerns, data impact, and verification commands.

### Prototype versus production

Prototype context can be thin if you accept throwaway output. Maintenance work needs richer context because hidden dependencies are the risk. 

## Stable Core

- context relevance matters more than context volume
- freshness must be explicit after code changes
- remote surfaces need context parity with local assumptions

## Volatile Surface

- context window and compaction behavior
- IDE selected-range behavior
- attachment support
- cloud environment visibility
- model-specific tolerance for long context

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- official Codex docs change context recommendations
- surfaces add automatic context selection that materially lowers user curation cost
- compaction behavior changes enough to alter long-session guidance

## Evidence and Sources

- `openai.codex.prompting` — Official OpenAI Codex prompting guidance for goals, context, success criteria, and interaction patterns.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples for explicit context, done definitions, bug fixes, and tests.
- `openai.codex.use_cases.codebase_onboarding` — Official OpenAI Codex use case for tracing large codebases and mapping repo flows before editing.
- `vcb.synthesis.prompting_operator_practice` — VCB maintainer synthesis for prompt operating patterns, guardrails, and coaching tactics.

## Related Topics

- `vcb.chapter.context_management`
- `vcb.prompting.four_part_prompt`
- `vcb.prompting.plan_first`
- `vcb.workflow.unknown_codebase`
- `vcb.codex.ide_extension`
- `vcb.codex.cloud`
- `vcb.codex.agents_md`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.prompting.context_management -->
