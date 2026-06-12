<!-- VCB:BEGIN_TOPIC id=vcb.workflow.unknown_codebase version=0.1.0 -->
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
id: vcb.workflow.unknown_codebase
title: Working in an Unknown Codebase
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- Large repositories
- Legacy codebases
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.editing_before_understanding
- vcb.shortcut.context_dumping
- vcb.shortcut.broad_refactor
durable_principles:
- understanding must precede mutation in unfamiliar systems
- entry points, tests, and dependencies define safe first moves
- read-only exploration is cheaper than wrong edits
likely_to_change:
- Codex repo search behavior
- surface-specific navigation features
- remote repository indexing
- IDE context features
obsolete_when:
- agents can safely change unfamiliar repos without explicit mapping, entry-point discovery,
  or reviewable assumptions
related_topics:
- vcb.chapter.understanding_unknown_codebase
- vcb.prompting.context_management
- vcb.prompting.plan_first
- vcb.workflow.feature_slicing
- vcb.concepts.frontend_backend
- vcb.concepts.dependency
- vcb.codex.cli
- vcb.codex.ide_extension
---

> Summary:
> The unknown-codebase workflow uses Codex to map the repo before editing it: find entry points, flows, tests, risky seams, and first safe change.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.unknown_codebase.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This workflow asks Codex to explore an unfamiliar repo before changing it. The output should be a map: entry points, important files, data flow, tests, risks, and suggested first safe slice.

### Why it matters

Unknown codebases punish confident guessing. Codex can help you understand them quickly, but only if you explicitly ask it to read, trace, and explain before editing.

### The mental model

Treat Codex like a guide walking you through a building with the power off. First find the exits, wiring, and load-bearing walls. Then renovate.

### What good looks like

Good: “Do not edit. Map how signup works from route to database. Include files, call flow, tests, config, risky areas, and a safe first change.”

### What bad looks like

Bad: “Add OAuth to this repo.” That asks Codex to mutate a system before either of you knows its shape.

### Minimal example

Read-only map request: entry points, modules, request/data flow, tests to run, configuration/secrets, risky assumptions, and recommended first slice.

### Checklist

- start read-only
- ask for a file-and-flow map
- identify tests and run commands
- name risky seams such as auth, billing, database, and deployment
- approve one small first edit only after the map
<!-- VCB:END_SECTION id=vcb.workflow.unknown_codebase.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.unknown_codebase.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to convert repo unfamiliarity into a structured exploration task before implementation.

### Diagnose the human’s current model

- Has Codex inspected the entry points?
- Does the map cite actual files?
- Are tests and run commands known?
- What business-critical flows are nearby?
- Can the first change be reversed easily?

### Explanation strategy

Keep the first pass read-only. Ask Codex to trace flows from user action to storage or external call. Reject generic architecture summaries. The map must point to files and risk areas.

### Useful metaphor

Unknown-codebase work is spelunking. Do not swing a pickaxe until you know where the tunnel supports are.

### Coaching tactics

- ask for entry points first
- trace one user flow end to end
- separate facts from guesses
- ask for tests and gaps
- turn the map into a plan-first prompt for the first slice

### Prompt patterns

```text
Do not edit. Map [feature/flow]. Include entry points, call path, files, tests, configs, risky assumptions, and the smallest safe first change.
Based on this map, propose one reversible implementation slice. Do not code yet.
Before editing, list what you still do not know and how you would verify it.
```

### Red flags to call out directly

- Codex proposes implementation before mapping
- summary has no file paths
- risky areas are not named
- tests are unknown
- first slice requires broad refactor

### Exercises

- Ask the human to request a flow map for one feature.
- Have them mark each Codex claim as fact, inference, or unknown.
- Ask them to choose one first slice and one thing not to touch.
<!-- VCB:END_SECTION id=vcb.workflow.unknown_codebase.ai_coach -->

## Shortcut Reality

### The ideal practice

Use a read-only exploration pass before editing an unfamiliar repo.

### What users often do instead

Users often start implementing immediately because Codex appears to understand the codebase.

### When the shortcut may be fine

Direct editing may be fine for isolated typo fixes, docs changes, or one-file experiments with easy rollback.

### When the shortcut is a bad idea

It is a bad trade for auth, payments, data, deploy scripts, dependency upgrades, migrations, or legacy areas with weak tests.

### Risk profile

- Probability of failure: High failure probability when the first edit relies on unverified architecture assumptions.
- Impact if it fails: Can be large because wrong assumptions spread into multiple files and workflows.
- Ease of recovery: Good if the first pass was read-only; poor if Codex already made broad edits.
- Blast radius: The blast radius includes every subsystem the agent misunderstood.
- Skill needed to recover: Medium to high; recovery may require architectural reading and Git cleanup.
- Hidden cost: Long cleanup, broken hidden flows, duplicated patterns, and lost trust in the repo.

### Minimum guardrails

- start read-only
- require file-path citations in the map
- identify tests before edits
- make first edit reversible
- avoid broad refactors until the flow is understood

### Recovery plan

- Stop implementation.
- Reset to a clean branch if needed.
- Run a read-only mapping prompt.
- Compare current diff to the map.
- Keep only changes supported by the mapped facts.

## Budget and Constraint Notes

### Cheapest reliable path

A read-only map is cheaper than fixing a wrong multi-file implementation.

### Fastest high-usage path

Use Codex to parallelize exploration across independent areas, but do not merge parallel edits until maps agree.

### Low-attention path

Unknown-codebase implementation is not a good low-attention task. Low-attention read-only mapping is acceptable.

### Production-quality path

Production unknown-codebase work needs mapping, tests, rollback, and reviewer ownership before mutation.

### Prototype versus production

Prototype work can accept rough maps. Maintenance work in existing repos needs precise file-backed maps. 

## Stable Core

- read before edit in unfamiliar systems
- file-backed maps beat generic summaries
- safe first slices require tests and reversibility

## Volatile Surface

- Codex search/index behavior
- IDE navigation integrations
- cloud repo setup
- subagent mapping features
- model codebase-reasoning quality

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex gains reliable repo-wide semantic maps by default
- official docs change onboarding workflow recommendations
- repository tooling generates current architecture maps automatically

## Evidence and Sources

- `openai.codex.use_cases.codebase_onboarding` — Official OpenAI Codex use case for tracing large codebases and mapping repo flows before editing.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples for explicit context, done definitions, bug fixes, and tests.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, review, and verification.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.understanding_unknown_codebase`
- `vcb.prompting.context_management`
- `vcb.prompting.plan_first`
- `vcb.workflow.feature_slicing`
- `vcb.concepts.frontend_backend`
- `vcb.concepts.dependency`
- `vcb.codex.cli`
- `vcb.codex.ide_extension`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.unknown_codebase -->
