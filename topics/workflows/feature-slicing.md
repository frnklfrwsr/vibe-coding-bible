<!-- VCB:BEGIN_TOPIC id=vcb.workflow.feature_slicing version=0.1.0 -->
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
id: vcb.workflow.feature_slicing
title: Feature Slicing
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- Product features
- Pull requests
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.one_big_prompt
- vcb.shortcut.broad_refactor
- vcb.shortcut.generated_prototype_as_production_foundation
durable_principles:
- small slices reduce review cost and recovery cost
- a slice should deliver observable behavior
- the first slice should avoid irreversible architecture commitments
likely_to_change:
- Codex planning behavior
- PR generation flows
- branch/worktree features
- surface support for parallel tasks
obsolete_when:
- large agent-generated feature dumps become cheaper to verify and safer to merge than small
  incremental slices
related_topics:
- vcb.chapter.feature_slicing
- vcb.prompting.plan_first
- vcb.prompting.acceptance_criteria
- vcb.workflow.testing
- vcb.concepts.feature_flag
- vcb.concepts.pull_request
- vcb.codex.cloud
- vcb.codex.github_review
---

> Summary:
> Feature slicing turns a broad feature request into small, reviewable, reversible increments that Codex can implement and you can inspect.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.feature_slicing.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Feature slicing means asking Codex for the smallest useful piece of a feature, not the whole product vision in one prompt. Each slice should be easy to review, test, and roll back.

### Why it matters

Big prompts create big diffs. Big diffs hide bugs. Small slices make Codex faster to supervise because you can see what changed and why.

### The mental model

A feature slice is a stepping stone. You cross the river one stable stone at a time instead of asking Codex to build a bridge overnight.

### What good looks like

Good: “Implement only the backend endpoint with tests. No UI yet. Keep response shape compatible. Done when endpoint tests pass and the diff is under the named files.”

### What bad looks like

Bad: “Build the whole dashboard, auth, billing, notifications, and tests.” That is not one Codex task; it is a project.

### Minimal example

Slice sequence: data model stub, API endpoint, one UI state, validation, error handling, tests, cleanup. Each slice has its own done-when.

### Checklist

- slice produces one observable behavior
- slice has a verification path
- slice avoids unrelated refactor
- slice can be reviewed in one sitting
- slice can be rolled back without losing the whole project
<!-- VCB:END_SECTION id=vcb.workflow.feature_slicing.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.feature_slicing.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to constrain Codex work to increments that are useful, reviewable, and reversible.

### Diagnose the human’s current model

- Is the request one behavior or several?
- Can this slice ship behind a flag or remain internal?
- What files should not be touched yet?
- What proof belongs to this slice only?
- What is the next slice if this one succeeds?

### Explanation strategy

Split broad asks by user-visible behavior, not by technical layer alone. Keep the first slice as the least risky change that creates evidence. Use acceptance criteria for each slice.

### Useful metaphor

Slicing is portion control for code. Too much at once is not productivity; it is review indigestion.

### Coaching tactics

- ask Codex to propose three slices before coding
- choose the slice with the best evidence-to-risk ratio
- ban unrelated cleanup from feature slices
- prefer flags or internal-only paths for early production slices
- merge learning back into the next prompt

### Prompt patterns

```text
Break this feature into 3-5 slices. For each, list behavior, files, checks, risk, and rollback. Do not code yet.
Implement slice 1 only: [slice]. Constraints: [constraints]. Done when: [criteria].
Stop after this slice and report what the next slice should be based on what you found.
```

### Red flags to call out directly

- one prompt contains UI, backend, auth, data migration, and deployment
- slice cannot be tested alone
- diff touches files outside stated scope
- Codex adds a new framework to finish a small slice
- prototype code becomes production foundation without hardening

### Exercises

- Give the human a feature and ask for five possible slices.
- Have them pick the slice with smallest blast radius.
- Ask them to write done-when criteria for the first slice only.
<!-- VCB:END_SECTION id=vcb.workflow.feature_slicing.ai_coach -->

## Shortcut Reality

### The ideal practice

Split features into small, behavior-based, reviewable slices.

### What users often do instead

Users often ask Codex for the whole feature in one run because it feels faster.

### When the shortcut may be fine

A larger dump can be acceptable for disposable prototypes or design exploration when you intend to throw away or rewrite the code.

### When the shortcut is a bad idea

It is a bad trade for production features, shared APIs, migrations, billing/auth, or anything requiring reliable maintenance.

### Risk profile

- Probability of failure: Medium failure probability for large feature prompts; high when new architecture is invented under time pressure.
- Impact if it fails: Large diffs increase hidden bugs, review fatigue, and merge conflicts.
- Ease of recovery: Good with small slices; poor with tangled all-in-one implementations.
- Blast radius: The blast radius is the union of all subsystems pulled into the feature dump.
- Skill needed to recover: Medium for review; high for untangling broad generated code.
- Hidden cost: Future maintenance cost, architecture lock-in, duplicate abstractions, and tests that only fit generated code.

### Minimum guardrails

- ask for slices before code
- implement one slice per prompt
- ban unrelated refactor
- require proof for each slice
- use Git branches or commits per slice

### Recovery plan

- Stop the broad run.
- List actual behaviors in the diff.
- Keep or extract the smallest coherent slice.
- Revert the rest.
- Continue with planned slices and criteria.

## Budget and Constraint Notes

### Cheapest reliable path

Small slices reduce token burn from corrections and human time spent reviewing broad diffs.

### Fastest high-usage path

High-throughput teams can run independent slices in parallel only when file overlap is low and merge order is clear.

### Low-attention path

Low-attention feature work should be limited to one isolated slice with strict done-when criteria.

### Production-quality path

Production slices need tests, rollback, migration discipline, and reviewer checkpoints.

### Prototype versus production

Prototype slicing can be rough. Production slicing should optimize for reviewability and future maintenance, not only first demo speed. 

## Stable Core

- small reviewable increments are safer than broad diffs
- slices need their own acceptance criteria
- build speed must include review and recovery cost

## Volatile Surface

- Codex parallel task support
- PR automation features
- branch/worktree UI
- model ability to keep slices isolated
- usage economics for parallel runs

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex reliably creates enforceable slice plans automatically
- official workflow docs change guidance around parallel broad feature work
- team CI/review tooling makes large generated diffs cheaper to verify

## Evidence and Sources

- `openai.codex.use_cases.follow_goals` — Official OpenAI Codex use case for goal-following, constraints, validation, stopping, checkpoints, and proof.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples for explicit context, done definitions, bug fixes, and tests.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, review, and verification.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.feature_slicing`
- `vcb.prompting.plan_first`
- `vcb.prompting.acceptance_criteria`
- `vcb.workflow.testing`
- `vcb.concepts.feature_flag`
- `vcb.concepts.pull_request`
- `vcb.codex.cloud`
- `vcb.codex.github_review`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.feature_slicing -->
