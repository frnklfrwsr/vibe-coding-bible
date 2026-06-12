<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.logged_in_browser_secrets version=0.1.0 -->
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
id: vcb.shortcut.logged_in_browser_secrets
title: Logged-In Browser Secrets
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
- fake or staging account
- no real secrets/customer data
- scoped site/app approvals
- human-present sensitive actions
- credential rotation plan
shortcut_profiles:
- vcb.shortcut.logged_in_browser_secrets
durable_principles:
- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
likely_to_change:
- Browser plugin and Chrome extension approval behavior
- Computer Use permission prompts
- website allow/block controls
- workspace/admin browser policies
obsolete_when:
- agents can safely operate signed-in sensitive accounts with provable data minimization,
  action gating, complete audit trails, and automatic secret redaction
related_topics:
- vcb.codex.computer_use
- vcb.safety.secrets
- vcb.shortcut.cloud_work_with_real_secrets
- vcb.shortcut.always_allow_sensitive_apps
- vcb.shortcut.production_console_computer_use
- vcb.shortcut.browser_clicking_without_repro
---

# Logged-In Browser Secrets

> Summary:
> Logged-In Browser Secrets means letting an agent operate a signed-in browser, app, or GUI where real credentials, sessions, customer data, admin panels, or sensitive pages are visible.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.logged_in_browser_secrets.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “It is already logged in, so let the agent use it.” A signed-in browser is not just a browser. It is an authority surface: the agent may see private data, trigger account actions, or expose session-bearing context.

### Why it matters

Browser and GUI tasks can cross boundaries outside the repo. When a session is logged in, the agent’s clicks and reads can become your account actions and your data exposure.

### What good looks like

Good: “Use a local unauthenticated route or a fake staging account with no real customer data and scoped website/app approval.”

### What bad looks like

Bad: “Use my logged-in production admin console and fix whatever setting is wrong.”

### Minimal example

Use a seeded demo account to verify checkout layout. Do not let an agent operate a live Stripe, cloud, database, email, or customer-support console unattended.

### Checklist

- prefer local or staging app
- use fake/demo account
- remove visible secrets and customer data
- scope app/site approvals
- rotate credentials if exposure is possible

<!-- VCB:END_SECTION id=vcb.shortcut.logged_in_browser_secrets.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.logged_in_browser_secrets.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach that signed-in GUI/browser use is a permission decision, not a convenience detail.

### Diagnostic questions

- What account is logged in?
- Can the agent see secrets, customer data, or admin controls?
- Can clicks spend money, delete data, deploy, invite users, or change permissions?
- Is there a fake/staging account?
- What should be revoked or rotated if exposed?

### Coaching tactics

- downgrade to screenshots or report-only
- use staging/demo credentials
- remove secrets from visible pages
- keep human present for sensitive flows
- rotate tokens after suspected exposure

### Red flags

- production admin console
- billing/payment dashboard
- customer data table visible
- Always Allow on sensitive app/site
- agent asked to click through destructive settings

### Prompt pattern

```text
Do not use a signed-in production browser or admin console. Use local, staging, or fake/demo accounts only. If sensitive data, secrets, tokens, billing, customer records, or destructive controls are visible, stop and report what safer context is needed. Do not click irreversible or account-changing controls.
```

<!-- VCB:END_SECTION id=vcb.shortcut.logged_in_browser_secrets.ai_coach -->

## Shortcut Reality

### Ideal practice

Keep browser/GUI tasks on local, staging, fake, or read-only contexts and avoid exposing real secrets or customer data.

### What people often do instead

They reuse their logged-in browser because setting up fake data feels slower.

### When the shortcut may be acceptable

Acceptable only for low-risk read-only flows with fake/staging accounts, scoped approvals, and no real secrets or sensitive user data.

### When it becomes a bad trade

Bad for production admin, billing, cloud consoles, database dashboards, customer-support tools, email, secrets managers, or any action that is logged as the human.

### Risk profile

- Probability: medium whenever browser/GUI tasks use signed-in pages; high with persistent approvals.
- Impact: severe for credentials, customer data, money movement, production settings, or compliance-sensitive systems.
- Recoverability: low after data exposure or irreversible account action; medium if caught before sensitive pages/actions are reached.

### Blast radius

The shortcut can expose credentials, sessions, customer data, admin capabilities, audit-trail ambiguity, and irreversible external state changes.

### Minimum guardrails

- fake or staging account
- no real secrets/customer data
- scoped site/app approvals
- human-present sensitive actions
- credential rotation plan

### Recovery plan

1. Stop the task and preserve an audit record.
2. Identify visible secrets, pages, data, actions, and approvals.
3. Revoke site/app approvals and narrow permissions.
4. Rotate credentials or sessions if exposure is plausible.
5. Review audit logs for account actions and restore changed settings.
6. Rerun with fake/staging data or a read-only report.

## Budget and Constraint Notes

### Cheapest reliable path

Write the smallest task packet, isolation rule, and review packet requirement before launching the agent. This costs less than reconciling a broad or unsafe background result.

### Fastest high-usage path

High-speed GUI workflows should invest in seeded fake accounts. Real-account recovery is slower than setup.

### Low-attention path

Low-attention browser tasks must not use real logged-in accounts. Human-present supervision is required for sensitive surfaces.

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

- Browser plugin and Chrome extension approval behavior
- Computer Use permission prompts
- website allow/block controls
- workspace/admin browser policies

## Obsolescence Watch

This card should be revised if:

- agents can safely operate signed-in sensitive accounts with provable data minimization, action gating, complete audit trails, and automatic secret redaction

## Evidence and Sources

- `openai.codex.app_browser` — Official OpenAI Codex in-app browser guidance for browser operation, website approval, local preview, and page evidence.
- `openai.codex.chrome_extension` — Official OpenAI Codex Chrome extension guidance for signed-in browser tasks and site approvals.
- `openai.codex.app_computer_use` — Official OpenAI Codex Computer Use guidance for GUI operation, system/app permissions, scoped tasks, and sensitive-action caution.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.computer_use`
- `vcb.safety.secrets`
- `vcb.shortcut.cloud_work_with_real_secrets`
- `vcb.shortcut.always_allow_sensitive_apps`
- `vcb.shortcut.production_console_computer_use`
- `vcb.shortcut.browser_clicking_without_repro`

<!-- VCB:STOP_RETRIEVAL reason="logged_in_browser_secrets_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.logged_in_browser_secrets -->
