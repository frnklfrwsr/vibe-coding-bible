<!-- VCB:BEGIN_TOPIC id=tool.codex_worktrees version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
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
evidence_scope: official OpenAI/Codex tool documentation plus VCB maintainer synthesis for
  setup, risk, budget, and coaching guidance
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
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
type: tool_card
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
id: tool.codex_worktrees
title: Codex Worktrees
name: Codex Worktrees
category: codex_isolation_worktrees
setup_effort: 'medium: requires a Git repository, clean enough baseline, local environment
  setup, and a merge/review habit'
maintenance_effort: 'medium: worktrees need cleanup, dependency setup, branch hygiene, and
  conflict management'
debugging_effort: 'medium: failures may be caused by missing untracked files, setup drift,
  branch divergence, or environment assumptions'
lock_in_risk: 'low to moderate: Git worktrees are general, but Codex app worktree handoff
  and review behavior are first-party conventions'
hidden_cost_risk: 'medium: isolation reduces trampling but adds setup, cleanup, and integration
  review cost'
codex_integration_value: strong for parallel Codex App work, safe automation staging, and
  reviewable branch isolation
best_for:
- isolating parallel local tasks
- reviewable experiments
- background app work that should not touch the active checkout
- automation runs that need separate change space
not_for:
- shared uncommitted state that only exists in the main checkout
- two agents editing the same files at the same time
- production hotfixes without a merge and rollback plan
- non-Git projects that need strict file isolation
integrates_with_codex:
- Codex App
- Codex Automations
- Codex Cloud handoff patterns
- Git review workflows
hidden_costs:
- worktree setup scripts
- dependency caches and local services
- merge conflict resolution
- cleanup of abandoned branches and directories
applies_to:
- Codex App
- Codex Automations
- local Git repositories
shortcut_profiles:
- vcb.shortcut.conflicting_parallel_agents
- vcb.shortcut.parallel_agents_edit_same_files
- vcb.shortcut.many_ais_same_files
- vcb.shortcut.skipping_setup
durable_principles:
- Isolation is useful only when the task boundary is clear.
- Reviewable branches beat mixed local edits for parallel work.
- Worktree results still need tests, diff review, and integration judgment.
likely_to_change:
- Codex app worktree controls, handoff behavior, automation defaults, setup scripts, local
  environment handling, and UI labels
obsolete_when:
- OpenAI removes Codex worktree support or makes another isolation mechanism the documented
  primary path for parallel local/app work.
related_topics:
- tool.codex_app
- tool.codex_automations
- tool.codex_cloud
- vcb.codex.app
- vcb.codex.automations
- vcb.shortcut.conflicting_parallel_agents
- vcb.concepts.git_branch
---

# Codex Worktrees

> Summary:
> Codex Worktrees isolate parallel local/app work so separate Codex threads can explore or change code without trampling the main checkout.

## Quick Navigation

- 1. For the Human: Plain-Language Concept
- 2. For the AI Coach: How to Teach This to Your Human
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=tool.codex_worktrees.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex Worktrees are the isolation layer for running Codex work away from the local checkout. In practical terms, a worktree is a separate Git-backed working directory that lets a thread or automation make changes without mixing them into your currently edited files.

### Why it matters

Worktrees matter because parallel work is only useful when the branches are reviewable. Without isolation, two helpful agents can create one unreadable pile of changes.

### What good looks like

Use a worktree when a task may edit files while you continue working locally, when an automation needs a separate change area, or when two independent experiments should remain reviewable.

### What bad looks like

Do not treat worktrees as conflict prevention magic. They separate working directories; they do not remove the need to define ownership, run setup, reconcile branches, and review the resulting diff.

### Minimal example

For a risky refactor, put the Codex thread in a worktree, assign it one bounded target, forbid unrelated files, require tests, and merge only after reviewing the diff against the main checkout.

### Best-fit cases

- isolating parallel local tasks
- reviewable experiments
- background app work that should not touch the active checkout
- automation runs that need separate change space

### Not-fit cases

- shared uncommitted state that only exists in the main checkout
- two agents editing the same files at the same time
- production hotfixes without a merge and rollback plan
- non-Git projects that need strict file isolation

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: requires a Git repository, clean enough baseline, local environment setup, and a merge/review habit |
| Maintenance effort | medium: worktrees need cleanup, dependency setup, branch hygiene, and conflict management |
| Debugging effort | medium: failures may be caused by missing untracked files, setup drift, branch divergence, or environment assumptions |
| Lock-in risk | low to moderate: Git worktrees are general, but Codex app worktree handoff and review behavior are first-party conventions |
| Hidden cost risk | medium: isolation reduces trampling but adds setup, cleanup, and integration review cost |

### Checklist

- choose this adjunct surface only when the task shape requires it
- write the task boundary, allowed actions, and forbidden zones before use
- prefer read-only or report-only output until the workflow is proven
- require evidence before accepting a summary
- check official OpenAI docs for current mechanics before relying on product behavior

<!-- VCB:END_SECTION id=tool.codex_worktrees.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_worktrees.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach this as an adjunct control surface, not a generic productivity boost. The primary lesson is: pick the smallest surface that fits, isolate risk, and demand evidence.

### Diagnostic questions

- What primary Codex surface is this adjunct attached to?
- Is the task read-only, mutating, recurring, parallel, browser-based, or GUI-based?
- What permission boundary prevents the wrong files, windows, sites, or accounts from being touched?
- What artifact proves success: diff, report, screenshot with repro, test output, or review note?
- What must stop the run immediately?

### Coaching tactics

- route surface-choice questions through `tool.codex` first, then this adjunct card if relevant
- translate vague delegation into a task packet with scope, allowed actions, and done-when evidence
- keep product mechanics, UI labels, current feature availability, and pricing in volatile-source review
- pair every shortcut warning with the smallest reliable guardrail
- require human review when secrets, account authority, production state, or persistent data are involved

### Prompt pattern

```text
Use an isolated worktree for this task. Scope: [target files/behavior]. Do not touch [forbidden areas]. Return changed files, checks run, merge risks, and anything that must be reconciled with the main checkout.
```

### Red flags

- the human wants several worktrees but no file ownership map
- untracked setup files exist only in the main checkout
- the task spans the same files as active local edits
- the user treats a clean worktree summary as merge approval

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_worktrees.ai_coach -->

## Shortcut Reality

### The ideal practice

Use this tool only after the task, context, permission boundary, evidence requirement, and review owner are clear.

### What users often do instead

Users often reach for the powerful adjunct surface because it feels faster, then discover that parallelism, browser state, GUI control, or recurrence has multiplied the review problem.

### When the shortcut may be acceptable

The shortcut can be acceptable for read-only inspection, disposable prototypes, isolated worktrees, report-only automation, local visual checks, or account-safe flows where rollback is trivial and no sensitive state is exposed.

### When it becomes a bad trade

It becomes a bad trade when the surface can mutate broad code, touch signed-in accounts, hide environment assumptions, operate sensitive apps, run repeatedly, or produce polished summaries without artifacts.

### Relevant shortcut cards

- `vcb.shortcut.conflicting_parallel_agents`
- `vcb.shortcut.parallel_agents_edit_same_files`
- `vcb.shortcut.many_ais_same_files`
- `vcb.shortcut.skipping_setup`

### Minimum guardrails

- one bounded task per run/thread/automation
- explicit allowed actions and forbidden zones
- isolation through branch, worktree, sandbox, account boundary, or read-only mode where possible
- evidence packet before acceptance
- human review before merge, deploy, account action, credential use, or production action

### Recovery plan

Stop the run, preserve the transcript and generated artifacts, inspect diffs or account actions, revert unsafe changes, rotate exposed secrets if needed, remove broad approvals, and restart with a narrower task packet.

## Budget and Constraint Notes

### Cheapest reliable path

Use the narrowest Codex surface and the smallest context packet that can produce reviewable evidence. Avoid parallel, recurring, browser, or GUI control until a simpler surface fails.

### Fastest high-usage path

Use this adjunct surface only when independence, isolation, and review capacity are already planned. Otherwise it creates speed theater: more activity with less confidence.

### Low-attention path

Low-attention use requires isolation, stop conditions, and report-only or review-later output. Low attention does not justify broad mutation, signed-in account action, or production access.

### Production-quality path

Production use requires least privilege, explicit scope, checks, security review where relevant, and human acceptance based on artifacts rather than summaries.

### Hidden costs to watch

- orphaned worktrees
- different dependency state than the main checkout
- parallel branches that solve incompatible versions of the same problem

## Stable Core

- Isolation is useful only when the task boundary is clear.
- Reviewable branches beat mixed local edits for parallel work.
- Worktree results still need tests, diff review, and integration judgment.

## Volatile Surface

- Codex app worktree controls, handoff behavior, automation defaults, setup scripts, local environment handling, and UI labels

Exact prices, plan packaging, usage-credit quantities, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI removes Codex worktree support or makes another isolation mechanism the documented primary path for parallel local/app work.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.app_worktrees` — official/synthesis source anchor for this tool card.
- `openai.codex.app_features` — official/synthesis source anchor for this tool card.
- `openai.codex.app_automations` — official/synthesis source anchor for this tool card.
- `openai.codex.best_practices` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex_app`
- `tool.codex_automations`
- `tool.codex_cloud`
- `vcb.codex.app`
- `vcb.codex.automations`
- `vcb.shortcut.conflicting_parallel_agents`
- `vcb.concepts.git_branch`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_worktrees -->
