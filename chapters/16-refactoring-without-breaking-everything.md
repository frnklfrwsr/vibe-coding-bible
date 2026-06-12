<!-- VCB:BEGIN_TOPIC id=vcb.chapter.refactoring_without_breaking_everything version=0.1.0 -->
---
id: vcb.chapter.refactoring_without_breaking_everything
title: "Chapter 16 — Refactoring Without Breaking Everything"
type: chapter
chapter_number: 16
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
- Git
- tests
- refactoring
- legacy code

source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: CORE_ENGINEERING
  surface: STABLE
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

project_phases:
- maintenance
- major_refactor
- production_build
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.broad_refactor
- vcb.shortcut.one_big_prompt
- vcb.shortcut.skipping_tests
- vcb.shortcut.accepting_diff_without_review

durable_principles:
- A refactor changes structure while preserving behavior.
- Broad refactors must be split into reviewable passes with validation after each pass.
- Public APIs, data contracts, and user-visible behavior are protected unless the task explicitly changes them.
- Refactors are safer with tests, characterization checks, clean Git state, and rollback points.

likely_to_change:
- Codex refactoring capability by model and framework
- official refactor workflow surface mechanics
- skill/plugin names for planning or refactor workflows

obsolete_when:
- Codex can automatically prove behavior preservation across large refactors and explain every semantic equivalence without explicit tests or review.
- Official Codex guidance no longer recommends small reviewable refactor passes or plan-first workflows for broad changes.

related_topics:
- vcb.chapter.plan_first_code_second
- vcb.chapter.feature_slicing
- vcb.chapter.writing_updating_tests
- vcb.chapter.git_discipline
- vcb.concepts.diff
- vcb.concepts.recoverability
- vcb.concepts.rollback
- vcb.workflow.refactoring
- vcb.failure.unreviewed_large_diffs
---

> Summary:
> Refactoring is changing the shape of code without changing what users get. Codex can do it fast, so the guardrails must be stronger: plan, slice, preserve behavior, test, review, commit.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.refactoring_without_breaking_everything.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A refactor changes how code is organized without changing what the app does.

If users see different behavior, that is not just a refactor. That is a behavior change.

Good refactor:

- split one huge file into smaller helpers,
- remove dead code,
- rename confusing variables,
- move repeated logic into one place,
- make tests easier to write,
- keep the same user-visible behavior.

Bad refactor:

- turns into a rewrite,
- changes API shape accidentally,
- removes edge-case behavior,
- deletes tests,
- adds dependencies because the new structure is easier that way,
- produces a diff too large to review.

### Why it matters with Codex

Codex is good at moving and rewriting code quickly. That is useful when code is messy. It is also dangerous because a large refactor can silently change behavior while looking cleaner.

Clean code that breaks the product is not progress.

### Refactor versus rewrite

| Term | Meaning | Risk |
|---|---|---|
| Refactor | same behavior, better structure | moderate if sliced and tested |
| Cleanup | small local simplification | low if scoped |
| Migration | change framework, package, API, or data model | high |
| Rewrite | rebuild a subsystem from scratch | high/very high |

Do not let Codex call a rewrite a refactor.

### The safe refactor loop

```text
1. Commit or stash current work.
2. Ask for a plan only.
3. Name behavior that must stay the same.
4. Pick one small pass.
5. Implement only that pass.
6. Run targeted checks.
7. Review the diff.
8. Commit.
9. Repeat.
```

### Good refactor prompt

```text
Plan first. Do not edit yet.

Goal:
Refactor the auth session loading code to separate token parsing, session lookup, and permission checks.

Context:
Relevant files: [list files if known].
Existing behavior must remain the same.

Constraints:
- no user-visible behavior changes,
- keep public API shape stable,
- no new dependencies,
- no database schema changes,
- split into small reviewable passes,
- call out anything that is actually a migration.

Done when:
The plan lists each milestone, likely files, behavior-preservation checks, tests to run/update, and rollback strategy.
```

### Behavior preservation

Before accepting a refactor, ask:

- What behavior is supposed to remain unchanged?
- Which tests or manual checks prove that?
- Did public API shape change?
- Did database shape change?
- Did auth/permissions behavior change?
- Did error handling change?
- Did Codex delete or weaken tests?
- Is the diff small enough to review?

### Characterization checks

A characterization check records what the existing system currently does before you change its structure.

Use this when old code is messy and not well tested.

Example:

```text
Before refactoring, identify the current behavior of this function for normal, empty, invalid, and unauthorized inputs. Add or describe characterization checks that preserve the current behavior unless I explicitly approve a behavior change.
```

### Good refactor slices

Useful slices include:

- delete dead code,
- extract one helper,
- move one group of functions,
- rename one concept consistently,
- collapse duplicate logic,
- add tests around current behavior,
- split one component into presentational and data-loading parts,
- isolate side effects behind a small boundary.

Bad slices are vague:

- "clean up the whole app,"
- "modernize the backend,"
- "refactor auth, payments, and the dashboard,"
- "make it elegant."

### What good looks like

A good Codex refactor has:

- a plan,
- one pass at a time,
- protected behavior,
- no accidental API or data migration,
- targeted checks,
- reviewable diff,
- rollback path.

### What bad looks like

A bad Codex refactor has:

- no tests,
- huge diff,
- behavior changes hidden in cleanup,
- new dependencies,
- modified public contracts,
- deleted edge cases,
- no explanation of what stayed the same.
<!-- VCB:END_SECTION id=vcb.chapter.refactoring_without_breaking_everything.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.refactoring_without_breaking_everything.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat refactoring as behavior-preserving structural work. The core intervention is to prevent "cleanup" from becoming an unreviewable rewrite.

### Diagnose the human’s current model

Watch for:

- "refactor everything" prompts,
- no definition of behavior preservation,
- no tests or characterization checks,
- changing public APIs without intent,
- mixing dependency upgrades with structural cleanup,
- broad changes on a dirty working tree,
- multiple agents editing the same files,
- accepting a prettier architecture with no evidence.

### Explanation strategy

Use this distinction:

```text
A refactor is like reorganizing a kitchen without changing the menu. If the customer gets a different meal, it was not just a refactor.
```

Then ask for the protected behavior and smallest pass.

### Useful metaphors

- **Kitchen reorganization:** same meals, better layout.
- **Untangling knots:** pull one strand at a time or the knot tightens.
- **Bridge repair:** keep traffic rules explicit before moving supports.
- **Receipt versus groceries:** Codex's summary is not proof; the diff and checks are proof.

### Coaching tactics

Use this gate before broad refactors:

```text
Before edits, list:
- current responsibilities,
- behavior that must remain unchanged,
- public APIs/contracts to preserve,
- tests/checks that prove parity,
- the first reviewable pass,
- rollback strategy.
```

If the plan is vague, reject it:

```text
This plan is not actionable. It names goals but not milestones, files, checks, or rollback. Ask for a file-level plan before edits.
```

If the human is low-attention, push harder:

```text
A broad refactor is not a good unattended task unless it is isolated, milestone-based, and has checks after each pass.
```

### Prompt patterns

#### Refactor plan-only prompt

```text
Plan only. Do not edit.
Identify dead code, duplicated logic, oversized modules, stale abstractions, and behavior-preservation checks.
Split into small passes.
For each pass: files, exact structural change, behavior that should not change, check to run, rollback note.
```

#### One-pass implementation prompt

```text
Implement Pass 1 only.
Do not start Pass 2.
Preserve public behavior and API shape.
Do not add dependencies.
Run the targeted checks from the plan.
Report files changed, checks run, and any behavior-risk areas.
```

#### Refactor review prompt

```text
Review this refactor diff.
Flag behavior changes, public API changes, deleted edge cases, weakened tests, new dependencies, broad file churn, and anything that should be split into a migration.
```

### Red flags to call out directly

- "This is a rewrite, not a refactor."
- "The diff is too large to review safely."
- "Codex changed behavior while claiming cleanup."
- "Dependency upgrades do not belong inside this refactor pass."
- "There is no parity check. We do not know if behavior stayed stable."

### Exercises

1. Ask Codex to map one messy file's responsibilities.
2. Ask for a no-edit refactor plan.
3. Pick one extraction pass.
4. Ask for the parity check before implementation.
5. Review the diff for behavior changes.
<!-- VCB:END_SECTION id=vcb.chapter.refactoring_without_breaking_everything.ai_coach -->

## Shortcut Reality

### The ideal practice

Plan first, protect behavior, split into small passes, run checks after each pass, review the diff, and commit logical milestones.

### What users often do instead

They ask Codex to "clean up" a large area, accept a broad diff, and only later discover that behavior, tests, API shape, or edge cases changed.

### When the shortcut may be fine

A broad refactor shortcut may be acceptable when:

- the code is a throwaway branch,
- the app has no real users,
- no data/auth/payment behavior is involved,
- the task is exploratory,
- the user wants to compare approaches,
- the output is treated as a prototype, not accepted directly.

### When the shortcut is a bad idea

It is a bad trade when:

- production behavior must remain stable,
- tests are weak or absent,
- auth, billing, permissions, migrations, or data deletion are involved,
- the change touches public APIs,
- the diff is too large to review,
- multiple agents may conflict,
- the human will review later with low attention.

### Risk profile

- Probability of failure: medium for small refactors, high for broad unsliced ones.
- Impact if it fails: low in prototypes, high in production.
- Ease of recovery: high with commits and small passes; poor with large uncommitted churn.
- Blast radius: grows with shared modules, public APIs, data models, and auth logic.
- Skill needed to recover: medium to high.
- Hidden cost: subtle behavior drift and review fatigue.

### Minimum guardrails

- Commit before starting.
- Ask for a plan-only pass.
- Preserve public behavior/API unless explicitly changed.
- Implement one pass at a time.
- Run targeted tests/checks.
- Review changed files and deleted logic.
- Separate migrations, dependency upgrades, and framework changes into their own tasks.

### Recovery plan

If a refactor goes wrong:

1. Stop new edits.
2. Inspect `git status` and `git diff`.
3. Identify intended structural changes versus accidental behavior changes.
4. Revert the whole pass if the diff is not separable.
5. Reapply only the smallest safe piece.
6. Add a characterization or regression test for the broken behavior.
7. Update future guidance to require smaller passes.

### AI coach guidance

Say:

```text
This is exactly where Codex can create a clean-looking mess. Ask for one behavior-preserving pass with a check. Do not accept a broad cleanup diff without parity evidence.
```

## Budget and Constraint Notes

### Cheapest reliable path

Use a short plan-only pass, then one small refactor pass. Avoid exploratory multi-agent refactors unless the payoff is high.

### Fastest high-usage path

Run alternative refactor plans in isolated worktrees, compare them, and implement the safest plan milestone by milestone. Use a fresh reviewer before accepting.

### Low-attention path

Do not leave broad refactors unattended unless they are isolated, milestone-based, and required to stop after each pass with checks and a diff summary.

### Production-quality path

Require clean Git state, plan, behavior contract, tests or characterization checks, small commits, diff review, and rollback strategy.

## Stable Core

- Refactors preserve behavior.
- Large structural changes need small reviewable passes.
- Tests and characterization checks protect against hidden behavior drift.
- Migrations and dependency upgrades are separate risk categories.
- Reviewability is a safety property.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-12-08 source_required=true -->
- Codex refactor use-case workflows, Plan skill naming, cloud delegation mechanics, and review commands.
- Model ability to preserve semantics across large code movement.
- Framework-specific modernization patterns.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex can reliably prove semantic equivalence for broad refactors, detect all public API behavior changes, and generate trusted parity checks automatically.

## Evidence and Sources

- `openai.codex.use_cases.refactor_your_codebase` — official current anchor for small reviewable refactor passes, preserving behavior, and separating migrations or dependency upgrades.
- `openai.codex.workflows` — official current anchor for plan-first refactor workflows, clean Git state, file-level milestones, rollback strategy, cloud delegation, and review.
- `git.docs.status` — official Git anchor for checking working tree state before broad edits.
- `git.docs.diff` — official Git anchor for reviewing exact changed lines.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for behavior preservation, characterization checks, and refactor risk control.

## Related Topics

- `vcb.chapter.plan_first_code_second`
- `vcb.chapter.feature_slicing`
- `vcb.chapter.writing_updating_tests`
- `vcb.chapter.git_discipline`
- `vcb.concepts.diff`
- `vcb.concepts.recoverability`
- `vcb.concepts.rollback`
- `vcb.workflow.refactoring`
- `vcb.failure.unreviewed_large_diffs`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.chapter.refactoring_without_breaking_everything -->
