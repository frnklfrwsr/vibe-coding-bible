<!-- VCB:BEGIN_TOPIC id=vcb.chapter.feature_slicing version=0.1.0 -->
---
id: vcb.chapter.feature_slicing
title: "Chapter 12 — Building a Feature in Small Slices"
type: chapter
chapter_number: 12
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
- branches
- worktrees
- pull requests

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
- vcb.shortcut.one_big_prompt
- vcb.shortcut.skipping_plan
- vcb.shortcut.unattended_long_runs

durable_principles:
- A feature should be sliced into reviewable, verifiable milestones.
- Each slice should create one observable behavior or one enabling step with a clear check.
- Large feature prompts are acceptable for disposable prototypes but dangerous for durable products.
- Feature work should preserve rollback boundaries.

likely_to_change:
- Codex cloud/worktree mechanics
- Goal mode and long-running task behavior
- native milestone/planning UI
- product-specific branch and PR creation flows

obsolete_when:
- Codex can reliably decompose, implement, verify, and review large features without explicit milestone boundaries.
- Official Codex workflows no longer emphasize focused steps, validation, or reviewable outputs.

related_topics:
- vcb.chapter.four_part_prompt
- vcb.chapter.plan_first_code_second
- vcb.chapter.context_management
- vcb.chapter.acceptance_criteria
- vcb.chapter.understanding_unknown_codebase
- vcb.chapter.git_discipline
- vcb.concepts.diff
- vcb.concepts.recoverability
- vcb.workflow.feature_slicing
---

> Summary:
> Feature slicing means turning a big product idea into small, reviewable changes that Codex can implement, verify, and hand back safely.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.feature_slicing.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A feature slice is the smallest useful piece of a feature that can be built and checked.

Bad feature request:

```text
Build the whole dashboard.
```

Better sliced request:

```text
Milestone 1: show the dashboard shell with real routing and placeholder cards.
No database changes yet. Done when the route loads, existing layout conventions are used, and build/typecheck pass.
```

A slice is not always tiny. It is bounded. It has a finish line.

### Why it matters

Codex can write a lot of code quickly. That is useful until the diff becomes too large to review.

Large feature prompts create problems:

- too many files change at once,
- UI, backend, database, auth, and tests get mixed together,
- Codex may invent missing requirements,
- bugs hide inside the large diff,
- rollback becomes all-or-nothing,
- the human cannot tell which part actually works.

Small slices make each step easier to inspect, test, and undo.

### The mental model

Think of feature building like crossing a river on stepping stones.

One giant prompt tries to jump the river. Sometimes it works in a demo. In real projects, you want stones:

1. route exists,
2. UI shell renders,
3. data loads from existing API,
4. mutation works,
5. validation and error states work,
6. tests prove critical behavior,
7. polish and accessibility pass.

Each stone should hold your weight before you step to the next one.

### Ways to slice a feature

| Slice type | Example |
|---|---|
| Visible behavior | “The settings page opens and shows current values.” |
| Route/API boundary | “Add `GET /api/settings` only; no edit flow yet.” |
| UI state | “Add loading, empty, and error states for the existing data.” |
| Backend capability | “Persist the new preference field; no UI yet.” |
| Testable rule | “Reject invalid invite emails and preserve current valid flow.” |
| Risk boundary | “No payment changes in this slice.” |
| Migration boundary | “Add nullable column only; no backfill yet.” |

### Feature slicing prompt

```text
Plan the feature in small slices before coding.

Goal:
[feature]

Constraints:
- keep slices independently reviewable,
- each slice must have a done-when check,
- do not combine database migration, auth policy, and UI polish in one slice,
- identify rollback points.

Return:
1. slice list,
2. files likely affected per slice,
3. risk per slice,
4. checks per slice,
5. recommended first slice only.
```

Then tell Codex:

```text
Implement slice 1 only. Do not start slice 2.
```

### What good looks like

Good feature work has:

- a branch or worktree,
- one milestone at a time,
- a small diff,
- clear changed behavior,
- explicit constraints,
- tests or manual checks,
- a final report,
- a commit or checkpoint before the next slice.

Bad feature work has:

- one huge prompt,
- no boundaries,
- no tests,
- no rollback point,
- new dependencies without discussion,
- architecture changes mixed with product changes,
- “done” based only on Codex’s summary.

### Example: invite users feature

Too broad:

```text
Add team invites.
```

Sliced:

1. Create invite data model with no sending.
2. Add API endpoint to create pending invite.
3. Add admin UI form.
4. Add email sending with fake/local provider first.
5. Add accept-invite flow.
6. Add expiration and resend.
7. Add tests for permission and token cases.

Auth and email are risky. They should not be hidden inside one giant Codex patch.
<!-- VCB:END_SECTION id=vcb.chapter.feature_slicing.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.feature_slicing.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to convert product intent into Codex-sized implementation packets.

A good packet has enough context to act, enough constraints to avoid damage, and enough acceptance criteria to know when to stop.

### Diagnose the human’s current model

Watch for:

- “Build the full app” requests.
- Feature asks that mix UI, API, database, auth, billing, emails, and tests.
- “Just keep going” without milestone boundaries.
- Multiple agents editing the same files.
- No definition of the first reviewable checkpoint.
- Pro/high-throughput users confusing more parallel work with less review.

### Explanation strategy

Use the sequence:

1. **Name the full feature.** Do not lose product intent.
2. **Identify risk boundaries.** Data, auth, payments, migrations, deploy config.
3. **Choose the first observable behavior.** Avoid invisible architecture work unless necessary.
4. **Define done for that slice.** Evidence before next slice.
5. **Commit or checkpoint.** Make rollback cheap.

Say directly:

```text
This feature is too large for one safe Codex task. We need a slice plan, then implement slice 1 only.
```

### Useful metaphors

- **Stepping stones:** each slice must support weight before moving on.
- **Surgical incision:** make the smallest cut that reaches the problem.
- **Lego build:** assemble stable pieces, not a melted block.

### Coaching tactics

Ask for a slice table:

```text
Slice | User-visible outcome | Files likely touched | Risks | Checks | Rollback point
```

Then pick the first slice with the smallest useful behavior and lowest dependency on future work.

For constrained users, prefer fewer Codex turns but still keep slices small. For high-throughput users, parallelize only independent slices in separate branches/worktrees.

### Prompt patterns

#### Slice plan prompt

```text
Plan only. Split this feature into reviewable slices.
Do not edit files.
Each slice must have:
- outcome,
- likely files,
- risks,
- done-when checks,
- rollback notes.
Recommend slice 1.
```

#### Implement one slice prompt

```text
Implement slice 1 only.
Do not start later slices.
Preserve current public API unless explicitly needed.
Run the smallest relevant checks.
End with files changed, checks run, known gaps, and suggested next slice.
```

#### Stop scope creep prompt

```text
You are drifting into later slices. Stop.
Re-state the current slice boundary, revert unrelated edits if any, and finish only the current milestone.
```

### Red flags to call out directly

- “This diff is too large to review.”
- “The task combines migration, API, UI, and email; split it.”
- “Codex is changing architecture while implementing a feature.”
- “The first slice has no observable behavior.”
- “The prompt says ‘keep going’ but has no stopping rule.”

### Exercises

1. Take a feature idea and split it into five slices.
2. Mark which slices touch data, auth, payments, or deployment.
3. Write done-when criteria for slice 1.
4. Implement slice 1 only.
5. Review diff and decide whether slice 2 is still correct.
<!-- VCB:END_SECTION id=vcb.chapter.feature_slicing.ai_coach -->

## Shortcut Reality

### The ideal practice

Plan the feature, split it into slices, implement one slice, verify it, commit, then continue.

### What users often do instead

They give Codex one giant prompt and accept the generated app or feature as if the whole thing is production-ready.

### When the shortcut may be fine

A one-big-prompt feature may be acceptable when:

- the work is a disposable prototype,
- the goal is to discover product shape,
- no real users or data are involved,
- the output will be reviewed or rebuilt,
- the repo is isolated and easy to delete,
- the user understands it is a concept car, not production infrastructure.

### When the shortcut is a bad idea

It is a bad trade when:

- the diff is too large to review,
- the feature touches auth, payments, database migrations, user data, or deployment,
- rollback is unclear,
- multiple agents edit the same files,
- tests are missing or weak,
- the branch auto-deploys,
- Codex adds dependencies to make the giant request easier.

### Risk profile

- Probability of failure: medium for prototypes, high for durable products.
- Impact if it fails: low for demos, high for production or data-sensitive systems.
- Ease of recovery: good if isolated; poor if mixed into main branch.
- Blast radius: grows with every boundary included in the prompt.
- Skill needed to recover: medium to high when architecture and product changes are mixed.
- Hidden cost: reviewing and untangling a large generated diff.

### Minimum guardrails

- Use a branch or worktree.
- Ask for a slice plan first.
- Implement one slice only.
- Do not combine risky boundaries.
- Run checks for the slice.
- Commit between slices.
- Review the diff before continuing.

### Recovery plan

If a one-big-prompt diff is already large:

1. Stop further changes.
2. Ask Codex to summarize changed files by intended slice.
3. Revert unrelated or speculative work.
4. Keep only the smallest verified slice.
5. Commit or discard.
6. Restart with a slice plan.

### AI coach guidance

Use harm reduction:

```text
A giant prompt is fine for a throwaway sketch. For a real feature, it creates an unreviewable diff. Keep the product goal, but build it in slices.
```

## Budget and Constraint Notes

### Cheapest reliable path

Spend one short planning pass, then one small implementation pass. Avoid multiple speculative attempts unless the first slice is unclear.

### Fastest high-usage path

Use parallel branches for alternative implementations of the same slice, or for independent slices that do not touch the same files. Review and merge deliberately.

### Low-attention path

Low-attention feature work requires stronger boundaries: one branch/worktree, explicit stopping rule, no production secrets, no risky boundaries, and a final report with checks.

### Production-quality path

Use milestone branches or PRs, tests/checks per slice, diff review, rollback plan, and feature flags for risky launch paths.

## Stable Core

- Slices make diffs reviewable.
- Reviewable diffs make rollback cheaper.
- Each slice needs observable done criteria.
- Feature work should progress through checkpoints, not vibes.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
- Codex cloud and worktree mechanics.
- Goal mode and long-running task behavior.
- Native milestone/planning features.
- Exact UI for branches, PRs, and task delegation.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex adds stronger built-in milestone planning, automatic branch isolation, or reliable slice validation that changes how users structure feature work.

## Evidence and Sources

- `openai.codex.workflows` — official current anchor for explicit context, surface-specific workflows, and verification examples.
- `openai.codex.prompting` — official current anchor for breaking complex work into focused steps, task loops, and validation.
- `openai.codex.follow_goals` — official current anchor for long-running objectives with validation loops, checkpoints, and stopping conditions.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for incremental delivery, reviewable diffs, and rollback boundaries.

## Related Topics

- `vcb.chapter.four_part_prompt`
- `vcb.chapter.plan_first_code_second`
- `vcb.chapter.context_management`
- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.understanding_unknown_codebase`
- `vcb.chapter.git_discipline`
- `vcb.concepts.diff`
- `vcb.concepts.recoverability`
- `vcb.workflow.feature_slicing`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.chapter.feature_slicing -->
