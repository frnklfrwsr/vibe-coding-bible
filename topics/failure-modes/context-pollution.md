<!-- VCB:BEGIN_TOPIC id=vcb.failure.context_pollution version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex anchors, relevant vendor or named expert anchors
  where cited, and VCB maintainer synthesis for failure-mode control loops
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
- major_refactor
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.failure.context_pollution
title: Context Pollution
type: failure_mode
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- AGENTS.md
- Long-running sessions
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.context_dumping
- vcb.shortcut.vague_prompt
- vcb.shortcut.overstuffing_agents_md
- vcb.shortcut.editing_before_understanding
durable_principles:
- context quality matters more than context quantity
- stale context must be labeled or excluded
- contradictions need resolution before mutation
likely_to_change:
- Codex context-window behavior
- IDE auto-context behavior
- AGENTS.md loading mechanics
- memory and thread behavior
obsolete_when:
- agents can reliably prioritize contradictory, stale, and oversized context without
  explicit source ranking
related_topics:
- vcb.prompting.context_management
- vcb.workflow.unknown_codebase
- vcb.codex.agents_md
- vcb.failure.done_claim_without_evidence
- vcb.chapter.context_management
---

> Summary:
> Context pollution happens when stale, irrelevant, contradictory, or oversized context steers Codex away from the task that actually matters.

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

<!-- VCB:BEGIN_SECTION id=vcb.failure.context_pollution.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Context is what Codex can see and use. More context is not automatically better. Bad context is like giving a mechanic three repair manuals for three different cars and hoping they pick the right one.

### Why it matters

Codex works better with explicit context, but a context dump can bury the real signal. Old snippets, half-true requirements, outdated docs, old test output, and conflicting instructions make the agent optimize for the wrong target.

### The mental model

Context is a workbench, not a landfill. Put the right tools on it and remove the junk.

### What good looks like

Good: “Use these three files, this failing test, and this current constraint. Ignore the old prototype folder unless you need historical behavior.”

### What bad looks like

Bad: dumping a whole issue thread, stale docs, screenshots, logs, and prior AI guesses with no priority order.

### Minimal example

Ask Codex to name the evidence it used, the assumption it is making, the files it changed, and the verification that would catch this failure mode if it were wrong.

### Checklist

- current files named
- stale sources labeled or excluded
- constraints ranked
- done-when evidence specified
- old agent guesses treated as untrusted
<!-- VCB:END_SECTION id=vcb.failure.context_pollution.human -->

<!-- VCB:BEGIN_SECTION id=vcb.failure.context_pollution.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to curate context rather than maximizing context volume.

### Diagnose the human’s current model

- What information is current?
- Which context is only background?
- What should Codex ignore?
- Are there conflicting instructions?
- Can the task be solved with fewer files?

### Explanation strategy

Ask for a context inventory before edits. Make Codex restate which sources it will trust, which it will ignore, and what contradiction needs human decision.

### Useful metaphor

Context is a workbench, not a landfill. Put the right tools on it and remove the junk.

### Coaching tactics

- slow the human down at the first unsupported assumption
- ask for artifact-backed evidence instead of a verbal assurance
- separate read-only diagnosis from mutation
- require a smaller diff when review quality drops
- turn repeated misses into durable guidance only after the pattern is verified

### Prompt patterns

```text
Before coding, audit the provided context. Separate current task facts, useful background, stale/contradictory material, and unknowns. Ask only blocking questions. Then propose the smallest context packet needed for the implementation.
```

### Red flags to call out directly

- agent follows old docs over current code
- prompt contains multiple goals with no priority
- large pasted logs hide the actual failure
- AGENTS.md contains vague or obsolete rules
- Codex cites another AI guess as proof

### Exercises

- Have the human rewrite an overstuffed prompt into current facts, constraints, and done-when evidence.
- Ask the human to write one “stop condition” that would make Codex pause instead of pushing through.
- Review a previous agent diff and classify which evidence was missing.
<!-- VCB:END_SECTION id=vcb.failure.context_pollution.ai_coach -->

## Shortcut Reality

### The ideal practice

Provide a small, current, ranked context packet and update durable guidance only when the pattern repeats.

### What users often do instead

Users paste everything because they fear leaving out the one important clue.

### When the shortcut may be fine

A broad read-only exploration prompt can be fine when the output is a map, not a patch.

### When the shortcut is a bad idea

It is a bad trade when Codex is allowed to edit with contradictory instructions or stale specs.

### Risk profile

- Probability of failure: High in long projects, inherited repos, and repeated AI sessions.
- Impact if it fails: Medium to high: the change may be coherent but pointed at the wrong goal.
- Ease of recovery: Good if caught before implementation; expensive after many files are changed.
- Blast radius: Every file touched under the wrong assumption, plus durable guidance if bad rules are saved.
- Skill needed to recover: Low to medium; recovery requires prioritizing evidence and pruning context.
- Hidden cost: Repeated rework, agent confusion, stale AGENTS.md rules, and distrust of prompts.

### Minimum guardrails

- context inventory
- stale-material labels
- priority order
- plan-first gate
- small context packet

### Recovery plan

- Stop implementation.
- List trusted and untrusted context.
- Discard stale assumptions.
- Re-run plan-only with the clean packet.
- Revert or split any diff produced under polluted context.

## Budget and Constraint Notes

### Cheapest reliable path

Spend one cheap prompt cleaning the context before paying for a long implementation run.

### Fastest high-usage path

High-throughput users can use subagents for read-only mapping, but the final writer needs one curated packet.

### Low-attention path

Low-attention work should require the agent to summarize its context assumptions before mutating files.

### Production-quality path

Production work needs explicit source priority: code, tests, specs, incident data, then historical notes.

### Prototype versus production

Prototype context can be rough. Production context must distinguish current truth from brainstorming.

### Maintenance phase

In maintenance, update durable guidance when context mistakes repeat, but delete obsolete rules instead of accumulating them.

## Stable Core

- context quality matters more than context quantity
- stale context must be labeled or excluded
- contradictions need resolution before mutation

## Volatile Surface

- Codex context-window behavior
- IDE auto-context behavior
- AGENTS.md loading mechanics
- memory and thread behavior

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- agents can reliably prioritize contradictory, stale, and oversized context without explicit source ranking

## Evidence and Sources

- `openai.codex.prompting` — Official OpenAI Codex prompting documentation for context and task framing.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, reusable guidance, validation, and review.
- `openai.codex.agents_md` — Official OpenAI Codex AGENTS.md guidance for durable repository instructions and layering.
- `openai.codex.use_cases.codebase_onboarding` — Official OpenAI Codex use case for mapping unfamiliar codebases before editing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable failure-mode, risk, review, budget, and recovery discipline.

## Related Topics

- `vcb.prompting.context_management`
- `vcb.workflow.unknown_codebase`
- `vcb.codex.agents_md`
- `vcb.failure.done_claim_without_evidence`
- `vcb.chapter.context_management`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.failure.context_pollution -->
