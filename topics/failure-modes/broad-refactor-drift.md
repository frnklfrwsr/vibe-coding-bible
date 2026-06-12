<!-- VCB:BEGIN_TOPIC id=vcb.failure.broad_refactor_drift version=0.1.0 -->
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
id: vcb.failure.broad_refactor_drift
title: Broad-Refactor Drift
type: failure_mode
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Legacy codebases
- Maintenance work
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.broad_refactor
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.skipping_tests
- vcb.shortcut.ignoring_lint_typecheck
durable_principles:
- refactoring preserves observable behavior
- broad diffs increase review risk
- migrations and features should be separate from cleanup
likely_to_change:
- Codex refactor use-case details
- framework migration tools
- language refactor tooling
- test commands
obsolete_when:
- agents can safely perform broad refactors while proving behavior preservation across
  all affected paths
related_topics:
- vcb.workflow.refactoring
- vcb.workflow.reviewing_diffs
- vcb.workflow.testing
- vcb.concepts.diff
- vcb.concepts.recoverability
---

> Summary:
> Broad-refactor drift happens when a cleanup request turns into behavior changes, hidden migrations, new abstractions, deleted edge cases, or a rewrite nobody explicitly approved.

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

<!-- VCB:BEGIN_SECTION id=vcb.failure.broad_refactor_drift.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A refactor should change the shape of code without changing what users see. Drift is what happens when “clean this up” slowly becomes “change how this works.”

### Why it matters

Codex is good at finding patterns and making broad edits. That speed turns dangerous when the task has no boundary, no behavior-preservation checks, and no rule against mixing cleanup with features.

### The mental model

Refactoring is moving furniture in the same house. Drift is knocking down walls while calling it tidying.

### What good looks like

Good: “Refactor only the parser module. Preserve public behavior. Do not change dependency versions, API shapes, or storage. Run these parity checks.”

### What bad looks like

Bad: “Modernize this codebase” followed by changed APIs, new packages, test rewrites, and altered edge cases.

### Minimal example

Ask Codex to name the evidence it used, the assumption it is making, the files it changed, and the verification that would catch this failure mode if it were wrong.

### Checklist

- one refactor theme
- behavior-preservation statement
- no hidden dependency/framework migration
- small diff boundary
- parity checks named and run
<!-- VCB:END_SECTION id=vcb.failure.broad_refactor_drift.human -->

<!-- VCB:BEGIN_SECTION id=vcb.failure.broad_refactor_drift.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to split refactoring from features, migrations, and rewrites.

### Diagnose the human’s current model

- What behavior must stay fixed?
- What is the one structural improvement?
- Did public API change?
- Did dependencies change?
- Can the diff be reviewed as one idea?

### Explanation strategy

Require Codex to name current behavior, intended structural change, validation check, and intentional non-changes before editing.

### Useful metaphor

Refactoring is moving furniture in the same house. Drift is knocking down walls while calling it tidying.

### Coaching tactics

- slow the human down at the first unsupported assumption
- ask for artifact-backed evidence instead of a verbal assurance
- separate read-only diagnosis from mutation
- require a smaller diff when review quality drops
- turn repeated misses into durable guidance only after the pattern is verified

### Prompt patterns

```text
Plan first. Identify one refactor pass for [boundary]. Preserve behavior. Do not change APIs, data shapes, dependencies, framework versions, or tests except to add characterization coverage. Name parity checks and implement only pass 1.
```

### Red flags to call out directly

- diff spans unrelated folders
- new abstractions appear without a caller
- edge-case handling disappears
- package files change
- tests are rewritten to match new behavior

### Exercises

- Ask the human to separate a mixed diff into refactor, behavior change, dependency update, and migration piles.
- Ask the human to write one “stop condition” that would make Codex pause instead of pushing through.
- Review a previous agent diff and classify which evidence was missing.
<!-- VCB:END_SECTION id=vcb.failure.broad_refactor_drift.ai_coach -->

## Shortcut Reality

### The ideal practice

Refactor one boundary, run parity checks, review the diff, commit, and repeat.

### What users often do instead

Users ask for repo-wide cleanup because messy code feels expensive and embarrassing.

### When the shortcut may be fine

Broad cleanup is acceptable only for disposable prototypes or read-only analysis that produces a plan.

### When the shortcut is a bad idea

It is a bad trade for production services, public APIs, data handling, auth, weak tests, or release branches.

### Risk profile

- Probability of failure: High when the prompt says “clean up,” “modernize,” or “make this better” without boundaries.
- Impact if it fails: High when drift changes contracts or deletes edge cases.
- Ease of recovery: Good with small commits; poor when drift is mixed across many files.
- Blast radius: Every behavior path touched by moved, generalized, or deleted code.
- Skill needed to recover: Medium to high; recovery requires behavior understanding and git discipline.
- Hidden cost: Review fatigue, lost domain knowledge, accidental migrations, and future avoidance of cleanup.

### Minimum guardrails

- plan-only first
- one theme per pass
- no behavior changes
- parity checks
- commit boundary

### Recovery plan

- Stop the run.
- Split the diff by concern.
- Revert mixed behavior changes.
- Add characterization tests.
- Reapply the smallest safe refactor.

## Budget and Constraint Notes

### Cheapest reliable path

Buy one safe pass, not one broad cleanup. It costs less to review a small refactor than unwind a rewrite.

### Fastest high-usage path

High-throughput users can parallelize read-only analysis, but write passes should serialize by boundary.

### Low-attention path

Low-attention refactor work should return a plan and proposed slices, not a giant patch.

### Production-quality path

Production refactors need behavior parity, code-owner review, rollback, and no hidden migrations.

### Prototype versus production

Prototype refactors can be aggressive if discardable. Production refactors must preserve user-visible behavior.

### Maintenance phase

In maintenance, refactoring is worthwhile only when it lowers future change cost without creating regression debt.

## Stable Core

- refactoring preserves observable behavior
- broad diffs increase review risk
- migrations and features should be separate from cleanup

## Volatile Surface

- Codex refactor use-case details
- framework migration tools
- language refactor tooling
- test commands

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- agents can safely perform broad refactors while proving behavior preservation across all affected paths

## Evidence and Sources

- `openai.codex.use_cases.refactor_your_codebase` — Official OpenAI Codex use case for small reviewable behavior-preserving refactor passes.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, reusable guidance, validation, and review.
- `martin_fowler.refactoring` — Named expert source for refactoring as behavior-preserving restructuring.
- `martin_fowler.preparatory_refactoring` — Named expert source for behavior preservation and green tests during refactoring.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable failure-mode, risk, review, budget, and recovery discipline.

## Related Topics

- `vcb.workflow.refactoring`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.testing`
- `vcb.concepts.diff`
- `vcb.concepts.recoverability`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.failure.broad_refactor_drift -->
