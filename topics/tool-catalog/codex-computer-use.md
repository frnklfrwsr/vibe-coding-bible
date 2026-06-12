<!-- VCB:BEGIN_TOPIC id=tool.codex_computer_use version=0.1.0 -->
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
id: tool.codex_computer_use
title: Codex Computer Use
name: Codex Computer Use
category: codex_gui_automation
setup_effort: 'medium to high: requires plugin/setup, OS-level permissions, app approvals,
  and a safe desktop state'
maintenance_effort: 'medium: permissions, platform behavior, app compatibility, and safety
  defaults are volatile'
debugging_effort: 'high: failures may come from window focus, permissions, screen state, app
  timing, stale UI assumptions, or wrong-window interaction'
lock_in_risk: 'moderate: desktop control behavior, approvals, and locked/foreground behavior
  are Codex-specific and platform-specific'
hidden_cost_risk: 'high: human supervision, permission review, interruption, and recovery
  from wrong-window actions can dominate the task'
codex_integration_value: strong for GUI workflows that cannot be solved through code, tests,
  APIs, plugins, or the in-app browser
best_for:
- GUI-only bug reproduction
- desktop app verification
- visual state inspection
- narrow cross-app information gathering with supervision
not_for:
- unattended sensitive account changes
- production consoles
- payment or credential flows
- parallel runs against the same app window
integrates_with_codex:
- Codex App
- desktop apps
- browser workflows
- visual QA workflows
hidden_costs:
- supervision time
- permission review
- interrupted local work
- cleanup after wrong-window interaction
applies_to:
- Codex App
- macOS desktop apps
- Windows desktop foreground sessions
- browser tasks via desktop control
shortcut_profiles:
- vcb.shortcut.production_console_computer_use
- vcb.shortcut.always_allow_sensitive_apps
- vcb.shortcut.logged_in_browser_secrets
- vcb.shortcut.browser_clicking_without_repro
durable_principles:
- GUI automation is account and state automation; scope it like a production-risk action.
- A narrow visual flow beats a broad desktop objective.
- Human presence is required when secrets, money, privacy, or account authority are involved.
likely_to_change:
- OS permission requirements, foreground/locked behavior, app approvals, sensitive-action
  prompts, plugin setup, platform support, and UI labels
obsolete_when:
- OpenAI retires Computer Use or replaces desktop-app operation with a different permission
  and control model.
related_topics:
- tool.codex_app
- tool.codex_browser
- tool.codex_chrome_extension
- vcb.codex.computer_use
- vcb.shortcut.production_console_computer_use
- vcb.safety.production_red_lines
---

# Codex Computer Use

> Summary:
> Codex Computer Use lets Codex operate allowed desktop apps visually; use it for narrow GUI flows, not broad account or production control.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_computer_use.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex Computer Use is the desktop-app control surface. Codex can inspect screen content, take screenshots, and interact with windows, menus, keyboard input, and clipboard state in allowed apps.

### Why it matters

Computer Use matters when the task lives in a GUI rather than a repo or API. It also carries higher risk because visible app state, signed-in accounts, and system permissions become part of the task surface.

### What good looks like

Use it for one narrow app flow: reproduce a GUI-only bug, verify a desktop app path, collect information from an app, or test behavior that cannot be reached through code alone.

### What bad looks like

Do not allow broad desktop control for vague goals, production consoles, payments, credentials, account settings, or sensitive workflows without human presence and explicit approvals.

### Minimal example

Tell Codex the exact app, screen, and flow to operate. Keep unrelated apps closed, stay present for sensitive prompts, and require screenshots plus exact steps before accepting the result.

### Best-fit cases

- GUI-only bug reproduction
- desktop app verification
- visual state inspection
- narrow cross-app information gathering with supervision

### Not-fit cases

- unattended sensitive account changes
- production consoles
- payment or credential flows
- parallel runs against the same app window

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium to high: requires plugin/setup, OS-level permissions, app approvals, and a safe desktop state |
| Maintenance effort | medium: permissions, platform behavior, app compatibility, and safety defaults are volatile |
| Debugging effort | high: failures may come from window focus, permissions, screen state, app timing, stale UI assumptions, or wrong-window interaction |
| Lock-in risk | moderate: desktop control behavior, approvals, and locked/foreground behavior are Codex-specific and platform-specific |
| Hidden cost risk | high: human supervision, permission review, interruption, and recovery from wrong-window actions can dominate the task |

### Checklist

- choose this adjunct surface only when the task shape requires it
- write the task boundary, allowed actions, and forbidden zones before use
- prefer read-only or report-only output until the workflow is proven
- require evidence before accepting a summary
- check official OpenAI docs for current mechanics before relying on product behavior

<!-- VCB:END_SECTION id=tool.codex_computer_use.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_computer_use.ai_coach -->
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
Use Computer Use for one named app and one exact flow. Keep unrelated apps out of scope. Stop before account, payment, credential, production, or security-sensitive actions unless I explicitly approve each step.
```

### Red flags

- the task names a sensitive app but no stop point
- the user wants Always Allow for convenience
- Codex may interact with a production or billing console
- two GUI tasks could fight over the same foreground app

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_computer_use.ai_coach -->

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

- `vcb.shortcut.production_console_computer_use`
- `vcb.shortcut.always_allow_sensitive_apps`
- `vcb.shortcut.logged_in_browser_secrets`
- `vcb.shortcut.browser_clicking_without_repro`

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

- visible secrets in screenshots
- wrong-window clicks
- clipboard leakage
- signed-in account actions being treated as user actions

## Stable Core

- GUI automation is account and state automation; scope it like a production-risk action.
- A narrow visual flow beats a broad desktop objective.
- Human presence is required when secrets, money, privacy, or account authority are involved.

## Volatile Surface

- OS permission requirements, foreground/locked behavior, app approvals, sensitive-action prompts, plugin setup, platform support, and UI labels

Exact prices, plan packaging, usage-credit quantities, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires Computer Use or replaces desktop-app operation with a different permission and control model.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.app_computer_use` — official/synthesis source anchor for this tool card.
- `openai.codex.use_cases.qa_computer_use` — official/synthesis source anchor for this tool card.
- `openai.codex.app_settings` — official/synthesis source anchor for this tool card.
- `openai.codex.sandboxing` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex_app`
- `tool.codex_browser`
- `tool.codex_chrome_extension`
- `vcb.codex.computer_use`
- `vcb.shortcut.production_console_computer_use`
- `vcb.safety.production_red_lines`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_computer_use -->
