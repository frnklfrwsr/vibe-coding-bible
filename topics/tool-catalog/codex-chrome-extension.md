<!-- VCB:BEGIN_TOPIC id=tool.codex_chrome_extension version=0.1.0 -->
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
id: tool.codex_chrome_extension
title: Codex Chrome Extension
name: Codex Chrome Extension
category: codex_signed_in_browser_workflows
setup_effort: 'medium: requires extension/plugin setup, Chrome permissions, website approvals,
  and a safe browser profile posture'
maintenance_effort: 'high: website approvals, extension permissions, browser-history sensitivity,
  account policies, and product behavior are volatile'
debugging_effort: 'high: failures may be auth state, website permission, tab state, app/plugin
  state, prompt scope, or hostile page content'
lock_in_risk: 'moderate: extension permissions, website allow/block controls, and Chrome-specific
  task grouping are first-party Codex conventions'
hidden_cost_risk: 'high: supervision, approvals, cleanup, account risk, and review time often
  exceed the apparent task cost'
codex_integration_value: strong only when signed-in browser state is necessary and less-exposed
  Codex surfaces cannot do the job
best_for:
- signed-in website QA with supervision
- account-specific browser workflows
- internal web tools where no safer integration exists
- browser tasks that require normal Chrome state
not_for:
- public local previews that fit the in-app browser
- unattended production console actions
- credential or billing changes
- broad always-allowed hosts for unclear work
integrates_with_codex:
- Codex App
- Chrome
- signed-in web apps
- website approvals
hidden_costs:
- permission review
- account-action audit
- browser-history exposure
- cleanup after wrong site or form action
applies_to:
- Codex App
- Chrome
- signed-in websites
- internal tools
shortcut_profiles:
- vcb.shortcut.logged_in_browser_secrets
- vcb.shortcut.always_allow_sensitive_apps
- vcb.shortcut.production_console_computer_use
- vcb.shortcut.browser_clicking_without_repro
durable_principles:
- Signed-in browser automation acts with account authority.
- Prefer the in-app browser unless signed-in state is required.
- Approve the narrowest website and action scope that can complete the task.
likely_to_change:
- extension setup, website approval options, allow/block behavior, Chrome permission text,
  tab grouping, browser data access, and UI labels
obsolete_when:
- OpenAI retires the Chrome extension or changes signed-in browser work to a materially different
  permission model.
related_topics:
- tool.codex_app
- tool.codex_browser
- tool.codex_computer_use
- vcb.shortcut.logged_in_browser_secrets
- vcb.shortcut.always_allow_sensitive_apps
- vcb.safety.secrets
---

# Codex Chrome Extension

> Summary:
> The Codex Chrome extension lets Codex work in signed-in Chrome browser contexts with website approvals, making account-scope and permission discipline central.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_chrome_extension.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

The Codex Chrome extension is the signed-in browser surface. It lets Codex use Chrome when the task needs your normal browser profile, authenticated websites, or account-specific web workflows.

### Why it matters

It matters because signed-in browser work is not just browsing. Approved clicks, form submissions, and page reads can be account actions, and website content can become untrusted task context.

### What good looks like

Use it only when the in-app browser is insufficient because the task genuinely needs signed-in state. Scope the site, task, allowed actions, and stop points before approving access.

### What bad looks like

Do not give broad website approvals for vague tasks, production consoles, billing systems, admin dashboards, credential pages, or private data flows without close supervision.

### Minimal example

For a signed-in QA task, approve only the needed host for the current task, specify the exact page and flow, forbid account/billing/security changes, and require a review packet before any submission.

### Best-fit cases

- signed-in website QA with supervision
- account-specific browser workflows
- internal web tools where no safer integration exists
- browser tasks that require normal Chrome state

### Not-fit cases

- public local previews that fit the in-app browser
- unattended production console actions
- credential or billing changes
- broad always-allowed hosts for unclear work

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: requires extension/plugin setup, Chrome permissions, website approvals, and a safe browser profile posture |
| Maintenance effort | high: website approvals, extension permissions, browser-history sensitivity, account policies, and product behavior are volatile |
| Debugging effort | high: failures may be auth state, website permission, tab state, app/plugin state, prompt scope, or hostile page content |
| Lock-in risk | moderate: extension permissions, website allow/block controls, and Chrome-specific task grouping are first-party Codex conventions |
| Hidden cost risk | high: supervision, approvals, cleanup, account risk, and review time often exceed the apparent task cost |

### Checklist

- choose this adjunct surface only when the task shape requires it
- write the task boundary, allowed actions, and forbidden zones before use
- prefer read-only or report-only output until the workflow is proven
- require evidence before accepting a summary
- check official OpenAI docs for current mechanics before relying on product behavior

<!-- VCB:END_SECTION id=tool.codex_chrome_extension.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_chrome_extension.ai_coach -->
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
Use Chrome only because this task requires signed-in state. Limit access to [host/page]. Do not change billing, account, security, admin, production, or credential settings. Stop before submitting forms or irreversible actions.
```

### Red flags

- the in-app browser would be sufficient
- the user wants Always Allow to avoid prompts
- the task includes billing, admin, or credential pages
- the site content could steer Codex into unsafe actions

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_chrome_extension.ai_coach -->

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

- `vcb.shortcut.logged_in_browser_secrets`
- `vcb.shortcut.always_allow_sensitive_apps`
- `vcb.shortcut.production_console_computer_use`
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

- website prompt injection
- browser-history exposure
- signed-in account side effects
- overbroad host approvals

## Stable Core

- Signed-in browser automation acts with account authority.
- Prefer the in-app browser unless signed-in state is required.
- Approve the narrowest website and action scope that can complete the task.

## Volatile Surface

- extension setup, website approval options, allow/block behavior, Chrome permission text, tab grouping, browser data access, and UI labels

Exact prices, plan packaging, usage-credit quantities, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires the Chrome extension or changes signed-in browser work to a materially different permission model.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.chrome_extension` — official/synthesis source anchor for this tool card.
- `openai.codex.app_browser` — official/synthesis source anchor for this tool card.
- `openai.codex.app_settings` — official/synthesis source anchor for this tool card.
- `openai.codex.app_computer_use` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex_app`
- `tool.codex_browser`
- `tool.codex_computer_use`
- `vcb.shortcut.logged_in_browser_secrets`
- `vcb.shortcut.always_allow_sensitive_apps`
- `vcb.safety.secrets`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_chrome_extension -->
