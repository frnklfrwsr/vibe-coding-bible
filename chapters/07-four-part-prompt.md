<!-- VCB:BEGIN_TOPIC id=vcb.chapter.four_part_prompt version=0.1.0 -->
---
id: vcb.chapter.four_part_prompt
title: 'Chapter 7 — The Four-Part Prompt: Goal, Context, Constraints, Done When'
type: chapter
chapter_number: 7
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
- AI coach workflows

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
- vcb.shortcut.vague_prompt
- vcb.shortcut.one_big_prompt

durable_principles:
- A useful Codex prompt names the outcome, relevant context, constraints, and observable completion criteria.
- Prompt structure reduces guessing and rework.
- Prompt detail should scale with ambiguity and risk.
- Prompt wording is not proof; the diff and verification evidence still matter.

likely_to_change:
- Codex Goal mode mechanics
- Codex Plan mode mechanics
- surface-specific context capture
- slash-command names and UI controls
- model-specific prompt sensitivity

obsolete_when:
- Codex reliably infers goal, context, constraints, and done-when for production tasks without explicit user guidance.
- Official OpenAI guidance replaces the goal/context/constraints/done-when pattern with a materially different default task contract.

related_topics:
- vcb.chapter.plan_first_code_second
- vcb.chapter.context_management
- vcb.chapter.acceptance_criteria
- vcb.chapter.codex_mental_model
- vcb.chapter.git_discipline
- vcb.prompting.four_part_prompt
- vcb.shortcut.one_big_prompt
---

> Summary:
> The four-part prompt is the default work order for Codex: goal, context, constraints, and done when. It turns a vibe into an executable, reviewable task.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.four_part_prompt.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A Codex prompt is not a wish. It is a work order.

A strong work order has four parts:

| Part | Plain meaning | Example |
|---|---|---|
| Goal | What should exist after the task? | “Add a password reset flow.” |
| Context | What should Codex inspect or know first? | “Use the existing auth routes in `app/auth/*` and this error log.” |
| Constraints | What must Codex preserve or avoid? | “No new dependencies. Keep the API response shape.” |
| Done when | What proves the task is complete? | “Invalid tokens fail safely and auth tests pass.” |

Think of it like ordering food. “Make me something good” can work at a food truck. It is not enough when you need allergy-safe catering for a hundred people. Codex can improvise, but higher-risk code should not depend on improvisation.

### Why it matters

Vague prompts create invisible assumptions. Codex fills gaps using repo patterns, common framework habits, and guesses. Sometimes the guesses are useful. Sometimes they quietly change behavior you cared about but never stated.

A four-part prompt narrows the target:

```text
Goal:
Add a CSV export button to the invoices page.

Context:
Relevant files: app/invoices/page.tsx, lib/invoices.ts, existing export utility in lib/export.ts.
Current problem: users copy rows manually.

Constraints:
No new package. Preserve current table filters. Export only the filtered rows the user can already see.
Do not touch billing calculation logic.

Done when:
The button downloads a CSV with visible invoice rows, empty state is handled, and existing invoice tests still pass.
Report files changed and checks run.
```

This does not guarantee correct code. It does make the result easier to inspect and recover from.

### The mental model

Use this sentence:

```text
Goal tells Codex where to go.
Context tells it what map to read.
Constraints tell it where not to step.
Done when tells it when to stop.
```

If one part is missing, Codex can still proceed. The missing part becomes a guess.

### Bad prompt versus better prompt

Bad:

```text
Make the dashboard better.
```

Better:

```text
Goal:
Improve the dashboard loading state so users know data is still loading.

Context:
Start with `app/dashboard/page.tsx` and existing components in `components/ui`.

Constraints:
Use existing design tokens. Do not change data fetching behavior. No new dependency.

Done when:
The dashboard shows loading, error, empty, and loaded states. Existing dashboard checks pass or you explain why none exist.
```

The better prompt is not better because it is longer. It is better because it removes dangerous ambiguity.

### What good looks like

A good Codex prompt:

- names one main outcome,
- points to starting files or evidence,
- states what not to change,
- includes checks or behavior that prove completion,
- says when Codex should stop or ask,
- matches the risk level of the task.

For a typo, one sentence is enough. For auth, migrations, payments, deployments, security, or a broad refactor, the four-part structure is the minimum.

### Checklist

Before sending a serious prompt, ask:

- Did I name the outcome?
- Did I provide the relevant files, logs, screenshots, issue, or example?
- Did I state important constraints?
- Did I define observable completion?
- Did I say what should make Codex stop?
- Is this task small enough to review as a diff?
<!-- VCB:END_SECTION id=vcb.chapter.four_part_prompt.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.four_part_prompt.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to convert vague intent into a bounded, verifiable Codex task without burying them in prompt-engineering theater.

### Diagnose the human’s current model

Look for these patterns:

- They describe vibes instead of behavior: “make it better,” “clean this up,” “fix auth.”
- They provide a goal but no context.
- They provide context but no constraints.
- They ask for broad work but do not define “done.”
- They say “use best practices” instead of naming the actual rule.
- They rely on Codex to decide scope.

When you see this, rewrite the request into the four boxes and show the difference.

### Explanation strategy

Use progressive repair:

1. Start with the user’s raw ask.
2. Extract the implied goal.
3. Add missing context from known repo facts, or ask only for context that is truly blocking.
4. Name constraints based on risk.
5. Turn “done” into observable checks.
6. Keep the final prompt short enough to use.

Do not overfit. A tiny low-risk task does not need a huge specification. The standard is enough structure for the risk.

### Useful metaphors

- **Work order:** a prompt is the ticket handed to a contractor.
- **GPS route:** goal is the destination, context is the map, constraints are closed roads, done-when is arrival proof.
- **Kitchen allergy note:** constraints matter most when guessing can hurt someone.

### Coaching tactics

When the prompt is too vague, say:

```text
That prompt gives Codex too much room to guess. Here is the safer four-part version.
```

Then provide the prompt. Avoid a long interrogation unless the task is truly blocked.

For production-sensitive tasks, add:

```text
Stop and ask before changing auth, billing, migrations, deployment config, or secrets.
```

For a constrained user, compress the prompt:

```text
Use the cheapest reliable path: inspect only the named files, make the smallest patch, run the smallest relevant check, and stop.
```

### Prompt patterns

```text
Goal:
[one outcome]

Context:
[files, logs, screenshots, issue, examples, current behavior]

Constraints:
[architecture, no-new-deps, compatibility, security, files not to touch]

Done when:
[tests/checks/behavior/final report]
```

Risk-aware variant:

```text
Project risk: [prototype | production | security-sensitive]
Human attention: [supervised | review later]
Blast radius must stay within: [files/feature/branch]
Stop before: [irreversible or sensitive operations]
```

### Red flags to call out directly

- “Just build the whole thing.”
- “Make it production-ready” without defining production behavior.
- “Use best practices” with no project constraints.
- “Fix this” with no repro, log, or expected behavior.
- “Refactor everything” with no rollback strategy.
- “Improve UI” with no screenshot, component examples, states, or design constraints.

### Exercises

Ask the human to turn these into four-part prompts:

1. “Fix login.”
2. “Make the dashboard nicer.”
3. “Add exports.”
4. “Clean up this code.”
5. “Make this app work on mobile.”

Score the result by missing boxes, not by style.
<!-- VCB:END_SECTION id=vcb.chapter.four_part_prompt.ai_coach -->

## Shortcut Reality

### The ideal practice

Use a clear four-part prompt for any non-trivial task.

### What users often do instead

They send a one-line vibe prompt and let Codex infer everything.

### When the shortcut may be fine

A vague prompt can be fine for:

- disposable prototypes,
- visual exploration,
- quick local scripts,
- learning exercises,
- brainstorming before implementation.

### When the shortcut is a bad idea

A vague prompt is a bad trade for:

- production changes,
- auth, payments, security, or secrets,
- data migrations or deletion,
- public APIs,
- large refactors,
- tasks that will run unattended.

### Risk profile

- Probability of failure: medium; higher as ambiguity grows.
- Impact if it fails: low in throwaway work, high in production paths.
- Ease of recovery: high if on a branch with a clean checkpoint; low if Codex changes broad files without review.
- Blast radius: controlled only if constraints are explicit.
- Skill needed to recover: low for visible UI changes, high for data/security regressions.
- Hidden cost: rework, diff review burden, and misleading “done” summaries.

### Minimum guardrails

- Add at least a goal and done-when.
- Name files Codex should inspect first.
- State “no new dependencies” unless you truly allow them.
- Commit or branch before broad edits.
- Ask for changed files, checks run, and remaining risks.

### Recovery plan

If a vague prompt produced a mess:

1. Stop new edits.
2. Inspect `git status` and `git diff`.
3. Separate useful changes from scope creep.
4. Revert or restore unrelated changes.
5. Rewrite the task as a four-part prompt.
6. Retry in a smaller branch or milestone.

### AI coach guidance

Do not moralize. Say the actual risk:

```text
This shortcut may work for sketching, but it gives Codex authority to guess scope. The safer version is to keep your speed and add two guardrails: what should change and how we prove it changed.
```

## Budget and Constraint Notes

### Cheapest reliable path

Use one tight four-part prompt. Keep context curated. Ask Codex to inspect only relevant files, make the smallest change, run the smallest relevant check, and stop.

### Fastest high-usage path

Use the four boxes plus branch/worktree isolation. For broad build work, combine the prompt with milestones and let Codex produce progress reports after each checkpoint.

### Low-attention path

A low-attention prompt needs stronger boundaries, not fewer boundaries. Include stop conditions, reviewable checkpoints, forbidden areas, and final-report requirements.

### Production-quality path

Production prompts should include acceptance criteria, security constraints, compatibility constraints, verification commands, rollback expectations, and review expectations. “Make it work” is not enough.

## Stable Core

- The durable structure is outcome, relevant evidence, boundaries, and completion criteria.
- Prompt clarity reduces assumptions; it does not remove the need for review.
- Prompt structure should scale with risk and ambiguity.
- A prompt is not proof. The diff and checks remain the evidence.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-12-08 source_required=true -->

Volatile items:

- `/goal`, `/plan`, and related Codex command mechanics,
- surface-specific context capture,
- speech/dictation and UI controls,
- context-window and compaction behavior,
- model-specific prompt sensitivity.

Use official OpenAI docs before writing exact product instructions.

<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes official Codex prompting guidance,
- Goal mode or Plan mode changes materially,
- context capture behavior changes across surfaces,
- future Codex surfaces replace freeform prompts with structured task forms.

## Evidence and Sources

- `openai.codex.best_practices` — official current anchor for the four-part prompt default: Goal, Context, Constraints, and Done when.
- `openai.codex.prompting` — official current anchor for context handling and goal/completion framing.
- `openai.codex.follow_goals` — official current anchor for goals, stopping conditions, checkpoints, and validation contract.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for work-order framing, risk scaling, and harm-reduction prompt repair.

## Related Topics

- `vcb.chapter.plan_first_code_second`
- `vcb.chapter.context_management`
- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.codex_mental_model`
- `vcb.chapter.git_discipline`
- `vcb.prompting.four_part_prompt`
- `vcb.shortcut.one_big_prompt`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.four_part_prompt -->
