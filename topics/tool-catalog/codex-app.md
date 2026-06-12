<!-- VCB:BEGIN_TOPIC id=tool.codex_app version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex tool documentation plus VCB maintainer synthesis
  for setup, risk, budget, and coaching guidance
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
id: tool.codex_app
title: Codex App
name: Codex App
type: tool_card
category: codex_desktop_app
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
setup_effort: 'medium: desktop install, sign-in, project trust, Git/worktree posture,
  and optional feature settings'
maintenance_effort: 'medium: app capabilities, settings, review flows, worktree behavior,
  and platform support are volatile'
debugging_effort: 'medium: failures may live in local environment, app settings, Git
  state, worktrees, or approvals'
lock_in_risk: 'moderate: app threads, review flows, and desktop behaviors are first-party
  Codex conventions'
hidden_cost_risk: 'medium to high: local context makes starting easy, but parallel
  threads and review debt can accumulate quickly'
codex_integration_value: strong for visible local control loops that combine code
  changes, review, Git, and optional desktop/browser workflows
best_for:
- supervised local repository work
- parallel local threads with worktree isolation
- reviewing/staging/committing Codex changes
- designing recurring automations after manual proof
not_for:
- headless CI jobs
- unattended production operations
- broad signed-in browser/account actions
- tasks that require only a quick terminal script
integrates_with_codex:
- local Git projects
- Codex Cloud handoff
- Automations
- worktrees
- Computer Use
- in-app browser
hidden_costs:
- parallel thread merge conflicts
- review backlog
- desktop permissions and signed-in app exposure
- worktree cleanup
applies_to:
- Codex App
- local projects
- worktrees
- review pane
- automations
- browser/computer-use app features
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.parallel_cloud_sprawl
- vcb.shortcut.conflicting_parallel_agents
- vcb.shortcut.browser_clicking_without_repro
- vcb.shortcut.logged_in_browser_secrets
durable_principles:
- Supervised app work still needs a scoped task, isolated change path, and reviewable
  evidence.
- Parallel local work increases integration cost unless scopes are disjoint.
- Desktop/browser access requires stronger account and secret controls.
likely_to_change:
- platform availability, app settings, worktree UI, automations UI, review-pane labels,
  browser/computer-use permissions
obsolete_when:
- OpenAI retires the desktop app surface or changes it so it no longer manages local
  project threads and reviewable Codex work.
related_topics:
- vcb.codex.app
- vcb.codex.cloud
- vcb.codex.automations
- vcb.codex.computer_use
- vcb.workflow.reviewing_diffs
- vcb.shortcut.unattended_cloud_delegation
---

# Codex App

> Summary:
> Codex App is the desktop command-center surface for local project threads, review, Git actions, worktrees, automations, and app/browser-style workflows.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_app.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex App is the desktop workspace for running Codex against local projects. It is useful when you want a visible thread, local file access, review panes, worktree isolation, and desktop-oriented coordination.

### Why it matters

The app matters because it makes Codex work inspectable. It is better for supervised local work than a blind background run, but it can still create damage if permissions, worktrees, or browser/computer-use surfaces are too broad.

### What good looks like

Use the app for a local branch/worktree task where you can watch progress, inspect the diff, run checks, and commit deliberately.

### What bad looks like

Use the app as an always-on production operator with broad access, hidden browser state, and no review gate.

### Minimal example

Open a project, start one thread for one task, keep changes isolated, and require a final changed-files/checks summary before staging or pushing.

### Best-fit cases

- supervised local repository work
- parallel local threads with worktree isolation
- reviewing/staging/committing Codex changes
- designing recurring automations after manual proof

### Not-fit cases

- headless CI jobs
- unattended production operations
- broad signed-in browser/account actions
- tasks that require only a quick terminal script

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: desktop install, sign-in, project trust, Git/worktree posture, and optional feature settings |
| Maintenance effort | medium: app capabilities, settings, review flows, worktree behavior, and platform support are volatile |
| Debugging effort | medium: failures may live in local environment, app settings, Git state, worktrees, or approvals |
| Lock-in risk | moderate: app threads, review flows, and desktop behaviors are first-party Codex conventions |
| Hidden cost risk | medium to high: local context makes starting easy, but parallel threads and review debt can accumulate quickly |

### Checklist

- choose the smallest Codex surface that fits the task
- confirm permissions before mutation
- require a diff, report, structured output, or check evidence
- keep exact pricing, limits, model availability, and UI mechanics out of stable decisions
- review official OpenAI docs before freezing current product behavior

<!-- VCB:END_SECTION id=tool.codex_app.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_app.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the app as supervised local orchestration. It is a reviewable workspace, not a substitute for branch hygiene or tests.

### Diagnostic questions

- Is this a local project task or a cloud/background task?
- Will worktree isolation reduce merge risk?
- Does the user need browser/computer-use features, and are secrets visible?
- What review pane or diff evidence will be inspected?

### Coaching tactics

- prefer one thread per bounded task
- use worktrees for parallel local work
- make the app return changed files, commands, and remaining risks
- escalate when browser/computer-use or signed-in state enters the task

### Prompt pattern

```text
Use the Codex App for one local task. Scope: [files/behavior]. Use a branch/worktree if parallel work is needed. Do not touch [forbidden areas]. Return changed files, commands run, checks, risks, and what still needs human review.
```

### Red flags

- multiple app threads touching the same files
- review skipped because the app summary sounds complete
- computer/browser access enabled for vague tasks
- automations created before a manual run proves value

### Intervention rule

When the human asks for a current product detail, exact price, exact limit, model-routing claim, UI label, command flag, or plan-packaging fact, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_app.ai_coach -->

## Shortcut Reality

### The ideal practice

Use this tool only after the task, context, permissions, evidence, and review path are clear.

### What users often do instead

Users often pick the most convenient surface, then retrofit the safety controls after the tool has already produced output.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only inspection, docs work, small branches, or reports where rollback is trivial and no secrets or production state are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate broad code, touch secrets, make production changes, create noisy automation, hide environment assumptions, or return a polished summary without verifiable evidence.

### Relevant shortcut cards

- `vcb.shortcut.parallel_cloud_sprawl`
- `vcb.shortcut.conflicting_parallel_agents`
- `vcb.shortcut.browser_clicking_without_repro`
- `vcb.shortcut.logged_in_browser_secrets`

### Minimum guardrails

- one bounded task per run/thread/job
- explicit permissions and forbidden zones
- Git checkpoint or isolated branch/worktree for mutation
- evidence packet before acceptance
- human review before merge, deploy, credential use, or production action

### Recovery plan

Stop the tool, preserve logs/transcripts/output, inspect the diff or generated artifact, revert or isolate unsafe changes, rotate exposed secrets if needed, and restart with a smaller task packet.

## Budget and Constraint Notes

### Cheapest reliable path

Use the narrowest surface, smallest context packet, and cheapest reviewable workflow that can produce the needed evidence. Avoid retry loops caused by vague prompts.

### Fastest high-usage path

Use parallel or automated surfaces only when work is independent, review capacity exists, and integration cost is budgeted.

### Low-attention path

Low-attention use requires isolation, stop conditions, and a final review packet. It does not justify broad mutation or production access.

### Production-quality path

Production use requires explicit scope, least privilege, checks, security review where relevant, and human acceptance based on artifacts rather than summaries.

### Hidden costs to watch

- parallel thread merge conflicts
- review backlog
- desktop permissions and signed-in app exposure
- worktree cleanup

## Stable Core

- Supervised app work still needs a scoped task, isolated change path, and reviewable evidence.
- Parallel local work increases integration cost unless scopes are disjoint.
- Desktop/browser access requires stronger account and secret controls.

## Volatile Surface

- platform availability, app settings, worktree UI, automations UI, review-pane labels, browser/computer-use permissions

Exact prices, plan packaging, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires the desktop app surface or changes it so it no longer manages local project threads and reviewable Codex work.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.app` — official/synthesis source anchor for this tool card.
- `openai.codex.app_features` — official/synthesis source anchor for this tool card.
- `openai.codex.app_settings` — official/synthesis source anchor for this tool card.
- `openai.codex.app_worktrees` — official/synthesis source anchor for this tool card.
- `openai.codex.best_practices` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.codex.app`
- `vcb.codex.cloud`
- `vcb.codex.automations`
- `vcb.codex.computer_use`
- `vcb.workflow.reviewing_diffs`
- `vcb.shortcut.unattended_cloud_delegation`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_app -->
