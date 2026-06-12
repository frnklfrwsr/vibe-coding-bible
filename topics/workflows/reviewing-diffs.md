<!-- VCB:BEGIN_TOPIC id=vcb.workflow.reviewing_diffs version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI/Codex and vendor documentation anchors plus VCB maintainer synthesis for risk, budget, and coaching guidance
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
id: vcb.workflow.reviewing_diffs
title: Reviewing Diffs Workflow
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Git
- Codex App
- Codex CLI
- Codex IDE Extension
- Pull requests
- Local branches
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.broad_refactor
- vcb.shortcut.ignoring_lint_typecheck
- vcb.shortcut.skipping_tests
durable_principles:
- review diffs by intent, not line count alone
- separate behavior changes from cleanup
- small reversible diffs reduce review cost
likely_to_change:
- Git UI surfaces
- Codex diff rendering
- IDE diff controls
- review-summary formats
obsolete_when:
- code review no longer relies on inspecting changes because every patch has trustworthy formal proof
related_topics:
- vcb.chapter.reviewing_codex_output
- vcb.workflow.codex_output_review
- vcb.concepts.diff
- vcb.concepts.git_branch
- vcb.concepts.pull_request
- vcb.workflow.testing
---

> Summary:
> Diff review is the habit of reading only what changed, then deciding whether the change is intended, verified, and safe to keep.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.reviewing_diffs.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A diff is the set of changes between two versions of your code. Reviewing diffs means asking: what changed, why did it change, what behavior does it affect, and what proof says it works?

### Why it matters

Most AI coding failures are visible in the diff before they become production incidents. Diff review is the cheapest place to catch unrelated edits, weakened checks, overbroad rewrites, dependency creep, and unsafe assumptions.

### The mental model

A diff is an invoice. It shows exactly what Codex is charging your codebase for the requested outcome. Pay only for lines that buy the intended behavior.

### What good looks like

Good: “Review this diff by changed behavior. Flag unrelated edits, weakened tests, security-sensitive changes, and missing checks.”

### What bad looks like

Bad: Reviewing by vibe: scrolling until the code looks professional, then accepting everything.

### Minimal example

For a small password-reset fix, the diff should mostly touch the reset flow and tests. A surprise change to session handling, environment variables, or dependencies deserves a stop-and-explain gate.

### Checklist

- start with the files changed list
- classify each file: intended change, support change, or suspicious change
- look for deleted validation, weakened tests, and new dependencies
- trace user-visible behavior from diff to acceptance criteria
- require targeted checks before accepting
- keep cleanup/refactor separate from behavior change when risk is high
<!-- VCB:END_SECTION id=vcb.workflow.reviewing_diffs.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.reviewing_diffs.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to read diffs as risk maps rather than syntax decorations.

### Diagnose the human’s current model

- Can the human explain why each file changed?
- Are behavior change and cleanup mixed together?
- Is there a test or check for the changed behavior?
- Did Codex modify config, dependencies, auth, or data paths?
- Is the diff small enough to review honestly?

### Explanation strategy

Use a three-pass diff review: scope pass, risk pass, evidence pass. First ask whether the diff belongs to the task. Then inspect high-risk areas. Then verify tests, commands, and rollback.

### Useful metaphor

Diff review is airport security for code. Most bags pass quickly, but suspicious objects get opened.

### Coaching tactics

- ask Codex to group changes by intent before the human reads details
- reject mixed refactor-plus-feature diffs unless the split is justified
- force explicit notes for config, dependency, schema, auth, and permission changes
- use targeted checks first, broad checks second
- turn review misses into a checklist item or AGENTS.md instruction

### Prompt patterns

```text
Review this diff in three passes.
1. Scope: which changes are directly required, supporting, or unrelated?
2. Risk: auth, data, security, dependencies, migrations, public API, CI, or deployment impact.
3. Evidence: tests/checks run, gaps, and rollback path.
Return blocking issues first.
```

### Red flags to call out directly

- large generated diff with no changed-file summary
- style cleanup mixed into behavior change
- new dependency added without need
- tests deleted, skipped, or weakened
- config or environment changes hidden among normal code edits

### Exercises

- Ask the human to identify the riskiest file in a diff.
- Ask them to split a broad diff into reviewable commits conceptually.
- Give them a diff with an unrelated edit and require a rejection note.
<!-- VCB:END_SECTION id=vcb.workflow.reviewing_diffs.ai_coach -->

## Shortcut Reality

### The ideal practice

Read the diff before merge, classify changes, and require verification evidence proportional to risk.

### What users often do instead

Users trust that a passing-looking patch is correct because Codex wrote it fluently.

### When the shortcut may be fine

Shallow review may be acceptable for tiny local experiments or throwaway prototype branches with no merge intent.

### When the shortcut is a bad idea

It is bad for broad refactors, production fixes, dependency changes, migrations, security-sensitive code, and anything touching persistent data.

### Risk profile

- Probability of failure: Medium for small tasks, high for broad or mixed-purpose diffs.
- Impact if it fails: Impact rises with shared code, user data, auth, payment, and deployment paths.
- Ease of recovery: Good for small committed branches; poor for broad uncommitted patches or mixed refactors.
- Blast radius: All changed files and the runtime behavior they influence.
- Skill needed to recover: Medium; the reviewer needs enough codebase understanding to spot unrelated or risky edits.
- Hidden cost: Review fatigue, accidental architecture drift, brittle tests, and difficult revert decisions.

### Minimum guardrails

- require changed-file summary
- reject unrelated edits
- separate refactor from behavior change when possible
- run targeted checks
- commit or stash before risky follow-up work

### Recovery plan

- Stop work and snapshot current state.
- Use Git to inspect or revert suspicious hunks.
- Ask Codex to explain why each risky hunk exists.
- Run the nearest checks.
- Split the patch into smaller reviewable changes.

## Budget and Constraint Notes

### Cheapest reliable path

Review only changed files and run the closest relevant check.

### Fastest high-usage path

Use Codex to pre-label the diff by intent, then human-review only suspicious or high-risk groups first.

### Low-attention path

Do not accept low-attention work without a diff summary, changed-file list, checks, and explicit gaps.

### Production-quality path

Production diffs need human review, passing checks, clear rollback, and no hidden config/credential/dependency surprises.

### Prototype versus production

Prototype diffs can be coarse. Production diffs should be narrow, explained, and easy to revert.

### Maintenance phase

In maintenance, diff review cost is the carrying cost of the codebase; keep diffs small so future fixes stay cheap.

## Stable Core

- diffs expose actual change
- smaller diffs are safer and cheaper
- review is evidence triage, not aesthetic judgment

## Volatile Surface

- diff UI controls
- Codex review pane behavior
- PR review bot output format
- IDE review shortcuts

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex diff review begins producing structured risk annotations
- Git or hosting provider changes diff semantics or default views
- repository moves to generated code where raw diffs are less meaningful

## Evidence and Sources

- `openai.codex.app_review` — Official OpenAI Codex app review guidance for understanding and commenting on changes.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for review and validation.
- `git.docs.diff` — Official Git documentation for comparing changes.
- `git.docs.status` — Official Git status documentation for working-tree state before review.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.reviewing_codex_output`
- `vcb.workflow.codex_output_review`
- `vcb.concepts.diff`
- `vcb.concepts.git_branch`
- `vcb.concepts.pull_request`
- `vcb.workflow.testing`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.reviewing_diffs -->
