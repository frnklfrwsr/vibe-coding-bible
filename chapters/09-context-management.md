<!-- VCB:BEGIN_TOPIC id=vcb.chapter.context_management version=0.1.0 -->
---
id: vcb.chapter.context_management
title: 'Chapter 9 — Context Management: Enough Context, Not Everything'
type: chapter
chapter_number: 9
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-12-08'
review_cadence: semiannual

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- screenshots
- logs
- local repo evidence

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
- vcb.shortcut.context_dumping
- vcb.shortcut.unattended_long_runs

durable_principles:
- Relevant context beats maximum context.
- Missing context makes Codex guess.
- Stale or excessive context can anchor Codex on the wrong task.
- Long-running work needs context hygiene, progress summaries, and reset points.

likely_to_change:
- context-window sizes
- automatic compaction behavior
- surface-specific context capture
- MCP and connector capabilities
- model-specific retrieval behavior

obsolete_when:
- Codex can reliably infer all relevant context for high-risk tasks without explicit file, log, test, or behavior references.
- Future Codex retrieval makes manual context selection obsolete across all project types and surfaces.

related_topics:
- vcb.chapter.four_part_prompt
- vcb.chapter.plan_first_code_second
- vcb.chapter.acceptance_criteria
- vcb.chapter.installing_and_configuring_codex
- vcb.concepts.diff
- vcb.prompting.context_management
- vcb.failure.context_pollution
---

> Summary:
> Context management is choosing the evidence Codex needs for this task and excluding stale or irrelevant noise. More context is not automatically better.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.context_management.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Context is the information Codex uses to understand the task.

Useful context can be:

- files,
- selected code,
- open editor tabs,
- logs,
- stack traces,
- screenshots,
- design references,
- issue descriptions,
- API docs,
- tests,
- examples from neighboring code,
- previous command output.

Bad context is not “too much text” by itself. Bad context is information that makes Codex solve the wrong problem.

### The core rule

```text
Give Codex enough context to stop guessing, but not so much that irrelevant details steer the task.
```

A good context bundle is like packing for a trip. Bring what the trip needs. Do not bring the whole garage.

### Missing context versus context overload

| Problem | What it looks like | Result |
|---|---|---|
| Missing context | “Fix the API bug” with no route, log, repro, or expected behavior | Codex guesses. |
| Wrong context | Old files, stale docs, unrelated errors | Codex solves yesterday’s problem. |
| Context overload | Whole repo pasted, many unrelated issues, huge logs | Codex may anchor on irrelevant details and waste usage. |
| Good context | relevant files + error + expected behavior + constraints | Codex can inspect, patch, and verify. |

### What to include by task type

| Task | Best starting context |
|---|---|
| Bug | repro steps, expected/actual behavior, logs, stack trace, suspected files, failing test if any |
| Feature | user behavior, route/page/API, existing similar feature, constraints, acceptance criteria |
| UI | screenshot, current component, desired states, design token or existing component examples |
| Refactor | current responsibility, files to preserve, public API boundaries, tests, no-behavior-change rule |
| Test work | behavior to prove, current test style, failure output, exact command |
| Security/auth | threat model, current auth flow, sensitive files, must-not-change rules, reviewer expectations |

### Ask Codex what context it used

For serious tasks, ask:

```text
Before editing, list the files and evidence you used.
Name any missing context or assumptions.
```

This catches wrong context early. If Codex says it did not inspect the file that controls the behavior, stop and redirect it.

### Stale context pollution

Old context can poison a new task. If the previous task was about billing and the new task is about profile settings, do not let the old thread assumptions leak into the new work.

Use a reset summary:

```text
New task. Ignore prior implementation assumptions unless they are in the repo.
Current goal: [goal]
Relevant context: [files/logs/screenshots]
Constraints: [constraints]
Done when: [checks]
```

If the session has become messy, start fresh with a concise handoff:

```text
Here is the current repo state and task summary.
Do not rely on earlier thread history.
```

### Context is also a budget issue

Every irrelevant file, pasted log, and old discussion can cost attention and usage. Constrained users should be aggressive about curation. High-throughput users can let Codex explore more, but only after the task boundary is clear.

### What good context management looks like

- You point Codex at the likely entrypoints.
- You include exact errors, not vague descriptions.
- You provide screenshots for visual work.
- You name examples of existing patterns.
- You remove stale assumptions between unrelated tasks.
- You ask Codex to state assumptions before editing.
- You let Codex ask for missing context when blocked.
<!-- VCB:END_SECTION id=vcb.chapter.context_management.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.context_management.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to supply enough relevant evidence for Codex to solve the actual problem while avoiding context dumping and stale-thread contamination.

### Diagnose the human’s current model

Common bad models:

- “Codex can figure it out from the repo.” Sometimes true, but expensive and risky.
- “More context is always better.” False. Irrelevant context changes the problem.
- “The previous thread already knows.” Dangerous when the task changed.
- “A screenshot is optional for UI.” Often false; visual acceptance needs visual evidence.

### Explanation strategy

Use the context triage frame:

```text
What evidence proves the current state?
What evidence defines the desired state?
What evidence constrains the path?
What evidence proves completion?
```

If one is missing, ask for it or make a clearly labeled assumption.

### Useful metaphors

- **Packing for a trip:** bring what this trip needs, not everything you own.
- **Case file:** the detective needs the relevant evidence, not every document in the building.
- **Spotlight:** context should illuminate the task, not flood the room.

### Coaching tactics

When context is missing:

```text
Codex will have to guess. Add the route/file, the exact error, expected behavior, and the command or user flow that proves the fix.
```

When context is overloaded:

```text
This is too much mixed context. Compress it into: current goal, relevant files, key error, constraints, and done-when.
```

When context is stale:

```text
Start a fresh thread or reset the task summary. Old assumptions from the prior task are now noise.
```

For UI tasks, ask for a state matrix:

```text
Include loading, empty, error, success, mobile, disabled, and keyboard states if this is production UI.
```

### Prompt patterns

Context-curated prompt:

```text
Relevant context only:
- Files to inspect first:
- Error/log/output:
- Existing pattern to follow:
- Current behavior:
- Desired behavior:
- Constraints:
Do not inspect unrelated areas unless these files are insufficient. If they are insufficient, explain what is missing before editing.
```

Context reset prompt:

```text
New task. Ignore prior thread assumptions unless confirmed in the repo.
Use only the following context plus files you inspect directly:
[summary]
```

Context audit prompt:

```text
Before implementing, tell me:
1. what context you used,
2. what assumptions you made,
3. what context appears missing,
4. whether the task is safe to proceed with.
```

### Red flags to call out directly

- The user pastes a giant log without the failing behavior.
- The user provides a screenshot but not the file/component.
- The user gives old architecture notes as if they are current repo truth.
- The user asks Codex to work from memory instead of inspecting files.
- The task spans multiple unrelated goals in one context bundle.
- The user wants low-attention work but provides no starting files or stopping rule.

### Exercises

Take a vague bug report and ask the human to identify:

- current evidence,
- missing evidence,
- desired behavior,
- constraints,
- completion proof.

Then turn it into a context block.
<!-- VCB:END_SECTION id=vcb.chapter.context_management.ai_coach -->

## Shortcut Reality

### The ideal practice

Give Codex relevant, current, task-shaped context.

### What users often do instead

They dump too much context, too little context, or stale context from an old task.

### When the shortcut may be fine

Loose context can be fine for:

- brainstorming,
- disposable prototypes,
- learning questions,
- low-risk visual exploration,
- small tasks where Codex can inspect the obvious file.

### When the shortcut is a bad idea

Poor context is a bad trade for:

- production debugging,
- security-sensitive work,
- migrations,
- unfamiliar codebases,
- UI work without screenshots or states,
- long unattended sessions,
- issues involving logs, data, timing, or environment differences.

### Risk profile

- Probability of failure: medium to high when relevant evidence is missing.
- Impact if it fails: high when Codex changes the wrong behavior or follows stale assumptions.
- Ease of recovery: medium if diff is small; low if context pollution drives a broad refactor.
- Blast radius: expands when Codex explores without boundaries.
- Skill needed to recover: medium; high for architecture/security/data mistakes.
- Hidden cost: wasted usage, false confidence, and repeated correction loops.

### Minimum guardrails

- Name the current task explicitly.
- Provide relevant files or ask Codex to identify them before editing.
- Include exact error text or screenshots when available.
- State what context is authoritative.
- Reset or summarize between unrelated tasks.
- Ask Codex to list assumptions before risky edits.

### Recovery plan

If context pollution caused bad work:

1. Stop the thread.
2. Inspect the diff and changed files.
3. Identify which assumption caused the wrong direction.
4. Revert unrelated changes.
5. Start a fresh prompt with curated context.
6. Add a durable repo rule if the same context mistake repeats.

### AI coach guidance

Say this directly:

```text
The problem is not that Codex needs more text. It needs the right evidence. Let’s shrink this to the files, error, desired behavior, constraints, and done-when.
```

## Budget and Constraint Notes

### Cheapest reliable path

Curate context tightly. Use file references, exact errors, and one or two examples. Avoid broad repo exploration unless the first pass proves the starting context is wrong.

### Fastest high-usage path

Let Codex explore after you set task boundaries. Ask it to produce a context map first, then implement from the relevant slice.

### Low-attention path

Low-attention work needs better context than supervised work. Provide starting files, stop rules, forbidden areas, and progress-report expectations before leaving Codex alone.

### Production-quality path

Production context should include source of truth, tests/checks, risky areas, rollback expectations, and any real-data or security constraints. Screenshots and logs should be attached when they define the behavior.

## Stable Core

- Relevant evidence beats volume.
- Missing context creates guesses.
- Stale context creates wrong assumptions.
- Context should be refreshed between unrelated tasks.
- Codex claims should be checked against repo evidence, command output, and diffs.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-12-08 source_required=true -->

Volatile items:

- context-window size and compaction behavior,
- IDE/app/browser context capture,
- file-mention behavior,
- MCP and connector capabilities,
- model-specific retrieval behavior.

Use official OpenAI docs before writing exact current behavior.

<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes context handling, compaction, or context-window behavior,
- IDE/app/CLI context capture behavior changes,
- official guidance changes on file mentions, images, connectors, MCP, or external tool context,
- future Codex surfaces provide structured context bundles.

## Evidence and Sources

- `openai.codex.prompting` — official current anchor for including context such as files/images, IDE open-file/selection context, context windows, and compaction behavior.
- `openai.codex.best_practices` — official current anchor for providing the right task context and prompt structure in larger or higher-stakes work.
- `openai.codex.follow_goals` — official current anchor for pointing Codex at files, docs, issues, logs, plans, and progress proof in longer tasks.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for context triage, reset prompts, and context-pollution harm reduction.

## Related Topics

- `vcb.chapter.four_part_prompt`
- `vcb.chapter.plan_first_code_second`
- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.installing_and_configuring_codex`
- `vcb.concepts.diff`
- `vcb.prompting.context_management`
- `vcb.failure.context_pollution`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.context_management -->
