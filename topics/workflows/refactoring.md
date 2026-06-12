<!-- VCB:BEGIN_TOPIC id=vcb.workflow.refactoring version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex refactoring anchors, named expert refactoring
  guidance, and VCB maintainer synthesis
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
id: vcb.workflow.refactoring
title: Safe Refactoring Workflow with Codex
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- Legacy codebases
- Maintenance work
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.broad_refactor
- vcb.shortcut.skipping_tests
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.ignoring_lint_typecheck
durable_principles:
- refactoring preserves observable behavior
- small behavior-preserving passes reduce risk
- tests or characterization checks are part of safe refactoring
likely_to_change:
- Codex refactor use-case guidance
- framework migration paths
- test commands
- language tooling
- IDE refactor support
obsolete_when:
- agents can reliably restructure large systems while proving behavior preservation
  without human review
related_topics:
- vcb.chapter.refactoring_without_breaking_everything
- vcb.workflow.reviewing_diffs
- vcb.workflow.testing
- vcb.workflow.unknown_codebase
- vcb.workflow.dependency_update_review
- vcb.concepts.diff
---

> Summary:
> Safe refactoring uses Codex to improve code structure in small behavior-preserving passes with parity checks, reviewable diffs, and a clear boundary against rewrites or migrations.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.refactoring.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Refactoring changes how code is organized without changing what the app does. If users get new behavior, that is a feature or bug fix, not just a refactor.

### Why it matters

Codex can move code fast. That is useful for cleanup and dangerous for large rewrites disguised as cleanup.

### The mental model

Refactoring is replacing the plumbing without changing the water pressure at the faucet.

### What good looks like

Good: “Plan only. Refactor the session-loading module in one small pass. Preserve public behavior, avoid new dependencies, list parity checks, then implement only the first pass.”

### What bad looks like

Bad: “Clean up this codebase” followed by a huge diff, deleted tests, changed APIs, and no behavior evidence.

### Minimal example

Give Codex the boundary, behavior that must stay fixed, forbidden changes, target cleanup theme, checks, and rollback point.

### Checklist

- behavior-preserving boundary is named
- migration/dependency/API changes are split out
- one cleanup theme per diff
- tests or characterization checks exist
- diff is small enough to review
- Codex reports intentional non-changes
<!-- VCB:END_SECTION id=vcb.workflow.refactoring.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.refactoring.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to refuse broad refactors and demand parity evidence.

### Diagnose the human’s current model

- What behavior must not change?
- What is the one refactor theme?
- Did public API or data shape change?
- What check proves parity?
- Is this actually a migration?

### Explanation strategy

Use plan-first mode. Make Codex name current behavior, intended structural change, validation check, and rollback before editing. Split migrations, dependency upgrades, and behavior changes into separate tasks.

### Useful metaphor

Use two hats: one for changing structure, one for changing behavior. Do not wear both at once.

### Coaching tactics

- ban “cleanup the whole repo” prompts
- ask for characterization checks when tests are weak
- review deleted logic line-by-line
- commit after each safe pass
- call out hidden migrations immediately

### Prompt patterns

```text
Plan first. Refactor [boundary] without behavior change. Identify current behavior, public contracts, risky files, smallest pass, parity checks, and rollback. Then implement only pass 1. Do not add dependencies, change APIs, weaken tests, or bundle unrelated formatting.
```

### Red flags to call out directly

- large diff with many unrelated files
- tests deleted or weakened
- new dependency appears
- public API changes without approval
- Codex cannot state what behavior stayed the same

### Exercises

- Ask the human to classify changes as refactor, feature, migration, or rewrite.
- Have them write a characterization check before cleanup.
- Review a refactor diff and mark behavior risks.
<!-- VCB:END_SECTION id=vcb.workflow.refactoring.ai_coach -->

## Shortcut Reality

### The ideal practice

Plan, slice, preserve behavior, run parity checks, review the diff, commit, then repeat.

### What users often do instead

Users ask Codex to clean everything in one pass because messy code feels painful.

### When the shortcut may be fine

Small local cleanup without tests may be acceptable for dead comments, obvious unused imports, or throwaway prototypes.

### When the shortcut is a bad idea

It is a bad trade for production code, auth, payments, data writes, migrations, public APIs, or weakly tested legacy systems.

### Risk profile

- Probability of failure: High risk of accidental behavior changes when refactors are broad.
- Impact if it fails: High when cleanup changes contracts, data handling, auth, or release behavior.
- Ease of recovery: Good with small commits; poor with a huge mixed diff.
- Blast radius: The blast radius is every behavior path touched by moved, deleted, or generalized code.
- Skill needed to recover: Medium for local refactors; high for legacy behavior preservation.
- Hidden cost: Review fatigue, lost edge cases, test gaps, and future distrust of cleanup work.

### Minimum guardrails

- plan first
- one refactor theme
- no behavior changes unless approved
- parity checks
- small commit boundary

### Recovery plan

- Stop new edits.
- Split the diff by concern.
- Revert uncertain moves.
- Reproduce behavior on old and new code.
- Reapply the safest pass with tests.

## Budget and Constraint Notes

### Cheapest reliable path

Refactor one local boundary and run the smallest parity check. Do not buy broad cleanup with broad review cost.

### Fastest high-usage path

High-throughput users can run parallel analysis, but only one write pass should touch a boundary at a time.

### Low-attention path

Low-attention refactoring should be report-only or branch-isolated until parity evidence is returned.

### Production-quality path

Production refactors need small diffs, behavior-preservation evidence, human review, and rollback checkpoints.

### Prototype versus production

Prototype refactors can be aggressive if the code is disposable. Production and maintenance refactors must protect existing behavior.

### Maintenance phase

In maintenance, safe refactors pay down cost only if they reduce future change friction without creating review debt or regression debt.

## Stable Core

- refactoring preserves observable behavior
- small behavior-preserving passes reduce risk
- tests or characterization checks are part of safe refactoring

## Volatile Surface

- Codex refactor use-case guidance
- framework migration paths
- test commands
- language tooling
- IDE refactor support

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- agents can reliably restructure large systems while proving behavior preservation without human review

## Evidence and Sources

- `openai.codex.use_cases.refactor_your_codebase` — Official OpenAI Codex use case for small reviewable refactor and modernization passes.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, review, reusable skills, and verification.
- `martin_fowler.refactoring` — Named expert source for refactoring as behavior-preserving restructuring.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, and review discipline.

## Related Topics

- `vcb.chapter.refactoring_without_breaking_everything`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.testing`
- `vcb.workflow.unknown_codebase`
- `vcb.workflow.dependency_update_review`
- `vcb.concepts.diff`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.refactoring -->
