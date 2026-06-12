<!-- VCB:BEGIN_TOPIC id=tool.codex_browser version=0.1.0 -->
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
id: tool.codex_browser
title: Codex In-App Browser
name: Codex In-App Browser
category: codex_browser_testing
setup_effort: 'low to medium: requires app browser/plugin availability, a reachable preview
  target, and a scoped visual task'
maintenance_effort: 'medium: browser behavior, plugin controls, allowed sites, preview support,
  and UI labels are volatile'
debugging_effort: 'medium: failures may come from local server state, routing, responsive
  viewport, browser permissions, or hidden auth assumptions'
lock_in_risk: 'moderate: app browser comments and thread-integrated browser use are first-party
  Codex conventions'
hidden_cost_risk: 'medium: visual iteration can become subjective and expensive without acceptance
  criteria'
codex_integration_value: strong for frontend work where Codex needs rendered-state feedback
  and the human needs a reviewable visual trail
best_for:
- local web-app previews
- visual comments
- frontend bug reproduction
- read-only browser inspection of public pages
not_for:
- signed-in websites
- browser-extension-dependent flows
- production account actions
- evidence-free screenshot approval
integrates_with_codex:
- Codex App
- frontend workflows
- visual QA
- browser verification
hidden_costs:
- visual-review loops
- ambiguous design feedback
- local server setup
- manual reproduction time
applies_to:
- Codex App
- local development servers
- file-backed previews
- public pages without sign-in
shortcut_profiles:
- vcb.shortcut.browser_clicking_without_repro
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.logged_in_browser_secrets
durable_principles:
- Browser verification needs reproducible steps, not only a screenshot.
- Use the least account-exposed browser surface that can prove the behavior.
- Visual claims must map back to code, checks, and acceptance criteria.
likely_to_change:
- browser plugin setup, supported sites, comment UI, website approval behavior, screenshot
  controls, preview limitations, and UI labels
obsolete_when:
- OpenAI retires the in-app browser or replaces rendered-page preview and browser use with
  a different Codex surface.
related_topics:
- tool.codex_app
- tool.codex_computer_use
- tool.codex_chrome_extension
- vcb.workflow.visual_qa
- vcb.codex.computer_use
- vcb.shortcut.browser_clicking_without_repro
---

# Codex In-App Browser

> Summary:
> The Codex in-app browser gives Codex and the human a shared rendered-page view for local previews, comments, screenshots, and browser-based verification.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_browser.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

The Codex in-app browser is the app-contained browser surface for previewing rendered pages, leaving visual comments, inspecting local or public pages, and verifying web-app behavior without using the regular browser profile.

### Why it matters

It matters because frontend work needs evidence from the rendered UI. Screenshots alone are weak; the useful packet is repro steps, expected and actual behavior, screenshot or observation evidence, and the code diff that explains the fix.

### What good looks like

Use it for local development servers, file-backed previews, public pages that do not require sign-in, visual comments, and scoped browser verification of a web-app bug.

### What bad looks like

Do not use the in-app browser as a shortcut around authentication, extension-dependent behavior, production account actions, or reproducible browser tests.

### Minimal example

Have Codex open the local page, reproduce one named layout issue, fix the smallest code path, and return the URL/path, exact steps, screenshot observations, diff, and checks.

### Best-fit cases

- local web-app previews
- visual comments
- frontend bug reproduction
- read-only browser inspection of public pages

### Not-fit cases

- signed-in websites
- browser-extension-dependent flows
- production account actions
- evidence-free screenshot approval

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | low to medium: requires app browser/plugin availability, a reachable preview target, and a scoped visual task |
| Maintenance effort | medium: browser behavior, plugin controls, allowed sites, preview support, and UI labels are volatile |
| Debugging effort | medium: failures may come from local server state, routing, responsive viewport, browser permissions, or hidden auth assumptions |
| Lock-in risk | moderate: app browser comments and thread-integrated browser use are first-party Codex conventions |
| Hidden cost risk | medium: visual iteration can become subjective and expensive without acceptance criteria |

### Checklist

- choose this adjunct surface only when the task shape requires it
- write the task boundary, allowed actions, and forbidden zones before use
- prefer read-only or report-only output until the workflow is proven
- require evidence before accepting a summary
- check official OpenAI docs for current mechanics before relying on product behavior

<!-- VCB:END_SECTION id=tool.codex_browser.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_browser.ai_coach -->
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
Use the in-app browser for this exact page and flow. Return the URL/path, reproduction steps, expected result, actual result, screenshot or rendered-state observations, code changes, and verification evidence.
```

### Red flags

- the page requires sign-in
- the human asks whether it looks done without repro steps
- the task depends on an extension or regular browser profile
- visual feedback has no acceptance criteria

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_browser.ai_coach -->

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

- `vcb.shortcut.browser_clicking_without_repro`
- `vcb.shortcut.accepting_looks_done`
- `vcb.shortcut.logged_in_browser_secrets`

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

- auth assumptions
- responsive layout gaps
- screenshot-only verification
- public page content as untrusted context

## Stable Core

- Browser verification needs reproducible steps, not only a screenshot.
- Use the least account-exposed browser surface that can prove the behavior.
- Visual claims must map back to code, checks, and acceptance criteria.

## Volatile Surface

- browser plugin setup, supported sites, comment UI, website approval behavior, screenshot controls, preview limitations, and UI labels

Exact prices, plan packaging, usage-credit quantities, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires the in-app browser or replaces rendered-page preview and browser use with a different Codex surface.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.app_browser` — official/synthesis source anchor for this tool card.
- `openai.codex.app_settings` — official/synthesis source anchor for this tool card.
- `openai.codex.app_features` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex_app`
- `tool.codex_computer_use`
- `tool.codex_chrome_extension`
- `vcb.workflow.visual_qa`
- `vcb.codex.computer_use`
- `vcb.shortcut.browser_clicking_without_repro`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_browser -->
