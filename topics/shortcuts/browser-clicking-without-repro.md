<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.browser_clicking_without_repro version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex guidance plus VCB maintainer synthesis for risk-managed
  parallel, cloud, automation, and GUI/browser shortcut harm reduction
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
- disposable_prototype
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
id: vcb.shortcut.browser_clicking_without_repro
title: Browser Clicking Without Repro
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex Cloud
- Codex App
- Codex Automations
- Codex CLI non-interactive mode
- Computer Use
- browser/GUI tasks
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- parallel_cloud_automation
- delegation
- automation
- browser_gui
- blast_radius
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: false
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- exact repro steps
- expected/actual statement
- fake or staging data
- scoped browser/app approvals
- before/after evidence
shortcut_profiles:
- vcb.shortcut.browser_clicking_without_repro
durable_principles:
- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
likely_to_change:
- Browser plugin behavior
- Computer Use permissions
- Chrome extension approvals
- screenshot and annotation mechanics
obsolete_when:
- GUI agents can infer stable repro flows and isolate app state without explicit user steps
  or fake accounts
related_topics:
- vcb.codex.computer_use
- vcb.workflow.visual_qa
- vcb.workflow.frontend_work
- vcb.shortcut.production_console_computer_use
- vcb.shortcut.logged_in_browser_secrets
- vcb.failure.ui_taste_gap
---

# Browser Clicking Without Repro

> Summary:
> Browser Clicking Without Repro means asking an agent to operate a browser or GUI and fix what it sees before the failing flow, expected result, actual result, and evidence target are defined.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.browser_clicking_without_repro.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut treats browser/GUI control as discovery and verification at the same time. The agent can click around, but without a repro it may fix the symptom it happens to see, miss the real bug, or make visual changes that are hard to review.

### Why it matters

GUI work is stateful. The same page can behave differently by login, viewport, data, browser state, feature flags, and time. A reproducible flow is the anchor.

### What good looks like

Good: “Open this local route, use these steps, expected result is X, actual result is Y, fix only the overflow, and provide before/after evidence.”

### What bad looks like

Bad: “Use the browser and make the checkout page work.”

### Minimal example

For a mobile layout bug, give viewport size, route, login state, steps, expected/actual behavior, and the component/file area to change.

### Checklist

- write exact flow steps
- state expected and actual result
- use fake/staging data
- scope allowed actions
- capture screenshot or browser evidence after fix

<!-- VCB:END_SECTION id=vcb.shortcut.browser_clicking_without_repro.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.browser_clicking_without_repro.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach that browser/GUI operation needs a testable flow. Clicking is not a substitute for a repro.

### Diagnostic questions

- What exact route/app/window should be opened?
- What steps reproduce the issue?
- What state or account is required?
- What result proves the fix?
- What should Codex not click or change?

### Coaching tactics

- ask for repro steps first
- prefer local unauthenticated routes
- scope to one visible issue
- require before/after evidence
- separate exploration from mutation

### Red flags

- “click around until you find it”
- production or customer account needed
- no expected/actual behavior
- agent changes code after observing one transient state
- no screenshot or final flow evidence

### Prompt pattern

```text
Use browser/GUI control only for this exact repro: [steps]. Expected: [expected]. Actual: [actual]. Use fake/staging data only. Fix the smallest code path, do not change unrelated UI, then rerun the same flow and provide before/after evidence, changed files, and remaining risks.
```

<!-- VCB:END_SECTION id=vcb.shortcut.browser_clicking_without_repro.ai_coach -->

## Shortcut Reality

### Ideal practice

Define the repro and verification flow before allowing browser or GUI mutation.

### What people often do instead

They use visual operation to avoid specifying the bug, then accept a screenshot as proof.

### When the shortcut may be acceptable

Acceptable for read-only exploration or simple local UI checks where no real accounts, production data, or persistent settings are exposed.

### When it becomes a bad trade

Bad for signed-in production flows, payments, admin consoles, destructive actions, or UI bugs with unclear expected behavior.

### Risk profile

- Probability: medium for GUI work; high when no reproducible steps exist.
- Impact: medium for prototypes; high for production, auth, payment, or customer data flows.
- Recoverability: medium if local and branch-isolated; low after account state, settings, or real data changes.

### Blast radius

The shortcut can create superficial visual fixes, broken hidden states, wrong account changes, and false confidence from a single screenshot.

### Minimum guardrails

- exact repro steps
- expected/actual statement
- fake or staging data
- scoped browser/app approvals
- before/after evidence

### Recovery plan

1. Stop the browser/GUI task.
2. Record the actual path clicked and any state changed.
3. Reproduce the issue manually or with explicit steps.
4. Revert changes not tied to the repro.
5. Rerun with fake data and exact verification evidence.

## Budget and Constraint Notes

### Cheapest reliable path

Write the smallest task packet, isolation rule, and review packet requirement before launching the agent. This costs less than reconciling a broad or unsafe background result.

### Fastest high-usage path

Fast users should maintain lightweight UI repro templates; they cost less than repeated visual guesswork.

### Low-attention path

Low-attention GUI work needs strict route, account, and action boundaries because the agent can affect visible app state.

### Production-quality path

Production work requires human ownership of sensitive actions, branch/worktree isolation, least privilege, explicit evidence, and rollback or revocation planning.

### Prototype versus production

Prototype shortcuts are acceptable only when the environment, accounts, credentials, and data are fake or disposable. Production shortcuts need hard gates or refusal.

### Maintenance phase

Maintenance should remove stale automations, prune approvals, archive obsolete branches, update task templates, and encode safer defaults when the same shortcut repeats.

## Stable Core

- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
- the minimum guardrail should move the user at least one level up the guardrail ladder

## Volatile Surface

- Browser plugin behavior
- Computer Use permissions
- Chrome extension approvals
- screenshot and annotation mechanics

## Obsolescence Watch

This card should be revised if:

- GUI agents can infer stable repro flows and isolate app state without explicit user steps or fake accounts

## Evidence and Sources

- `openai.codex.app_browser` — Official OpenAI Codex in-app browser guidance for browser operation, website approval, local preview, and page evidence.
- `openai.codex.app_computer_use` — Official OpenAI Codex Computer Use guidance for GUI operation, system/app permissions, scoped tasks, and sensitive-action caution.
- `openai.codex.chrome_extension` — Official OpenAI Codex Chrome extension guidance for signed-in browser tasks and site approvals.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for context, constraints, done-when criteria, planning, validation, and review.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.computer_use`
- `vcb.workflow.visual_qa`
- `vcb.workflow.frontend_work`
- `vcb.shortcut.production_console_computer_use`
- `vcb.shortcut.logged_in_browser_secrets`
- `vcb.failure.ui_taste_gap`

<!-- VCB:STOP_RETRIEVAL reason="browser_clicking_without_repro_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.browser_clicking_without_repro -->
