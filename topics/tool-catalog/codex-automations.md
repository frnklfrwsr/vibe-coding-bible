<!-- VCB:BEGIN_TOPIC id=tool.codex_automations version=0.1.0 -->
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
id: tool.codex_automations
title: Codex Automations
name: Codex Automations
category: codex_recurring_automation
setup_effort: 'medium: requires a proven manual run, scoped project context, cadence, output
  format, and review owner'
maintenance_effort: 'high: automations drift as repos, docs, dependencies, priorities, and
  permissions change'
debugging_effort: 'medium to high: failures may be schedule, setup, stale context, worktree/local
  mode, permissions, or noisy criteria'
lock_in_risk: 'moderate: cadence, inbox, background thread, and project automation behavior
  are first-party Codex conventions'
hidden_cost_risk: 'high: recurring runs compound usage, review backlog, and false-positive
  cleanup'
codex_integration_value: strong for recurring Codex checks when they produce reviewable artifacts
  and have narrow stop conditions
best_for:
- recurring triage reports
- documentation or dependency watchlists
- scheduled QA checks
- small review-later maintenance loops
not_for:
- unreviewed production mutation
- credential rotation without human presence
- broad account actions
- noise-generating reminders with no owner
integrates_with_codex:
- Codex App
- Codex Worktrees
- Codex Cloud
- Triage/review workflows
hidden_costs:
- reviewing recurring output
- noise suppression
- stale automation cleanup
- recovering from repeated bad edits
applies_to:
- Codex App
- Codex Worktrees
- local project automation
shortcut_profiles:
- vcb.shortcut.automation_spam
- vcb.shortcut.automation_mutation_without_review
- vcb.shortcut.full_access_automation
- vcb.shortcut.unattended_mutation
durable_principles:
- Automate only a workflow that has worked manually.
- Recurring mutation needs stronger guardrails than recurring reporting.
- Every automation needs an owner, stop condition, and review path.
likely_to_change:
- automation scheduling controls, triage behavior, worktree/local execution choices, project
  scoping, permissions, and UI labels
obsolete_when:
- OpenAI retires Codex Automations or changes recurring Codex work so it no longer behaves
  as a scheduled/background workflow surface.
related_topics:
- tool.codex_app
- tool.codex_worktrees
- vcb.codex.automations
- vcb.shortcut.automation_spam
- vcb.shortcut.automation_mutation_without_review
- vcb.constraints.attention_budget
---

# Codex Automations

> Summary:
> Codex Automations run recurring or scheduled Codex work, ideally producing reviewable reports before any recurring mutation is trusted.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_automations.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex Automations are the recurring-work surface. They let Codex wake up around a repeated objective, run in a chosen project context, and produce output that should be reviewed before it changes important state.

### Why it matters

Automations matter because repeated work is where vague prompts become operational debt. A useful automation has a cadence, scope, allowed actions, stop conditions, and a signal threshold.

### What good looks like

Start with report-only automations for recurring triage, documentation drift, dependency watchlists, QA sweeps, or issue summaries. Promote to mutation only after manual runs prove signal quality.

### What bad looks like

Do not schedule a vague automation with broad file, account, or production access and assume the inbox result is safe because Codex ran it in the background.

### Minimal example

Create a weekly report-only automation that checks a specific folder for stale docs, lists candidate changes, and asks for review before editing any file.

### Best-fit cases

- recurring triage reports
- documentation or dependency watchlists
- scheduled QA checks
- small review-later maintenance loops

### Not-fit cases

- unreviewed production mutation
- credential rotation without human presence
- broad account actions
- noise-generating reminders with no owner

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: requires a proven manual run, scoped project context, cadence, output format, and review owner |
| Maintenance effort | high: automations drift as repos, docs, dependencies, priorities, and permissions change |
| Debugging effort | medium to high: failures may be schedule, setup, stale context, worktree/local mode, permissions, or noisy criteria |
| Lock-in risk | moderate: cadence, inbox, background thread, and project automation behavior are first-party Codex conventions |
| Hidden cost risk | high: recurring runs compound usage, review backlog, and false-positive cleanup |

### Checklist

- choose this adjunct surface only when the task shape requires it
- write the task boundary, allowed actions, and forbidden zones before use
- prefer read-only or report-only output until the workflow is proven
- require evidence before accepting a summary
- check official OpenAI docs for current mechanics before relying on product behavior

<!-- VCB:END_SECTION id=tool.codex_automations.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_automations.ai_coach -->
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
Design this as report-only first. Define cadence, scope, allowed reads, forbidden writes, output format, review owner, signal threshold, and stop condition. Do not schedule mutation until a manual run proves value.
```

### Red flags

- no owner for reviewing the output
- automation is scheduled before a manual proof run
- the task can touch secrets or production state
- the output will create more work than it removes

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_automations.ai_coach -->

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

- `vcb.shortcut.automation_spam`
- `vcb.shortcut.automation_mutation_without_review`
- `vcb.shortcut.full_access_automation`
- `vcb.shortcut.unattended_mutation`

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

- alert fatigue
- recurring noisy summaries
- background changes colliding with active work

## Stable Core

- Automate only a workflow that has worked manually.
- Recurring mutation needs stronger guardrails than recurring reporting.
- Every automation needs an owner, stop condition, and review path.

## Volatile Surface

- automation scheduling controls, triage behavior, worktree/local execution choices, project scoping, permissions, and UI labels

Exact prices, plan packaging, usage-credit quantities, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires Codex Automations or changes recurring Codex work so it no longer behaves as a scheduled/background workflow surface.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.app_automations` — official/synthesis source anchor for this tool card.
- `openai.codex.app_worktrees` — official/synthesis source anchor for this tool card.
- `openai.codex.app_settings` — official/synthesis source anchor for this tool card.
- `openai.codex.use_cases.proactive_teammate` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex_app`
- `tool.codex_worktrees`
- `vcb.codex.automations`
- `vcb.shortcut.automation_spam`
- `vcb.shortcut.automation_mutation_without_review`
- `vcb.constraints.attention_budget`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_automations -->
