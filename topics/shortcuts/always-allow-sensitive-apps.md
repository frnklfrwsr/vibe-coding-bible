<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.always_allow_sensitive_apps version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex security, permission, and automation guidance
  plus official vendor security documentation where cited; VCB maintainer synthesis
  for risk-managed shortcut harm reduction
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
id: vcb.shortcut.always_allow_sensitive_apps
title: Always Allow Sensitive Apps
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex App
- Computer Use
- Chrome extension
- browser tasks
- desktop apps
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- computer_use
- browser
- permissions
- secrets
- accounts
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: DO_NOT_DO_IN_PRODUCTION
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: false
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: false
minimum_guardrails:
- current-task approval by default
- no persistent allow for sensitive apps
- test/staging account first
- review and prune allowlists
- human present for account/security/payment/credential flows
shortcut_profiles:
- vcb.shortcut.always_allow_sensitive_apps
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, permission scope,
  and evidence quality
- production, secrets, credentials, CI permissions, and GUI/account actions require
  stronger controls than prototypes
- the minimum guardrail should move the user at least one level up the guardrail ladder
likely_to_change:
- Computer Use app approval UI
- Chrome allowlist/blocklist behavior
- browser-history controls
- Codex app settings labels
obsolete_when:
- persistent app and website approvals become risk-aware, task-scoped, automatically
  expiring, and unable to expose sensitive state without human reapproval
related_topics:
- vcb.codex.computer_use
- vcb.shortcut.production_console_computer_use
- vcb.shortcut.logged_in_browser_secrets
- vcb.safety.secrets
- vcb.constraints.attention_budget
- vcb.failure.done_claim_without_evidence
---

# Always Allow Sensitive Apps

> Summary:
> Always Allow Sensitive Apps means permanently allowing Codex to use sensitive desktop apps, websites, or browser hosts so future prompts do not pause for approval.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.always_allow_sensitive_apps.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “Stop asking me; this app is allowed.” That may be acceptable for a calculator or local preview. It is dangerous for apps that contain accounts, private data, credentials, admin settings, payments, or customer records.

### Why it matters

An allowlist turns a one-time decision into a future default. Future prompts, misleading page content, browser state, or task drift may reach the same app without the fresh risk check you would have made manually.

### What good looks like

Good: “Allow only the current chat/task, use a staging or test account, and remove persistent allow rules after the task.”

### What bad looks like

Bad: “Always allow Gmail, Stripe, AWS, GitHub admin, CRM, production console, or password manager because Codex needs it sometimes.”

### Minimal example

Always allowing a local design preview may be fine. Always allowing a signed-in billing dashboard is not.

### Checklist

- prefer current-task approval over persistent allow
- use fake/staging accounts for sensitive apps
- keep password managers and production consoles blocked
- review allowed apps/domains after risky tasks
- remove allow rules when the task ends

<!-- VCB:END_SECTION id=vcb.shortcut.always_allow_sensitive_apps.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.always_allow_sensitive_apps.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach allowlists as persistent authority. A saved app or website approval should be narrower than a one-time approval, not broader.

### Diagnostic questions

- What data or actions does this app expose?
- Would you let an intern use it unattended?
- Can the approval be per-task instead of persistent?
- Is the app signed into production, billing, or admin state?
- How will the human remember to revoke the allow rule?

### Coaching tactics

- downgrade Always Allow to current-task allow
- use a separate browser/profile/test account
- block password managers and production admin sites
- schedule an allowlist cleanup at task end
- stop if the wrong window or host appears

### Red flags

- Always Allow on production admin apps
- signed-in browser with customer data
- password manager visible
- payments, billing, auth, support, CRM, or cloud console host
- human plans to step away after approving

### Prompt pattern

```text
Before approving any app or website, classify it as safe-local, test/staging, internal-sensitive, or production-sensitive. Use current-task approval unless it is safe-local. Never persistently allow password managers, production consoles, billing, auth, CRM, or customer-data surfaces.
```

<!-- VCB:END_SECTION id=vcb.shortcut.always_allow_sensitive_apps.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, recoverability, and permission scope.

### What people often do instead

They remove friction by making an approval, credential, CI setting, browser/app permission, or production action broader and more persistent than the task actually requires.

### When the shortcut may be acceptable

Acceptable only for disposable, isolated, non-production work where no real secrets, accounts, user data, money, deployment path, or persistent state is exposed, and where rollback is trivial.

### When it becomes a bad trade

Bad when the task touches production, auth, payments, billing, customer data, secrets, CI permissions, deployment credentials, browser sessions, account settings, or any surface that treats agent actions as your actions.

### Risk profile

- Probability: medium when the task is scoped and supervised; high when the permission or credential survives beyond the task.
- Impact: low for fake local environments; high or severe for production, CI, secrets, admin consoles, and signed-in accounts.
- Recoverability: good only before side effects occur; poor after credential exposure, account mutation, deployment, data change, or audit-trail ambiguity.

### Blast radius

The shortcut can spread from one fast approval into leaked credentials, overbroad automation, irreversible account changes, hidden production state drift, CI token abuse, and expensive incident response.

### Minimum guardrails

- current-task approval by default
- no persistent allow for sensitive apps
- test/staging account first
- review and prune allowlists
- human present for account/security/payment/credential flows

### Recovery plan

1. Stop the agent, workflow, browser task, or automation immediately.
2. Create or preserve an audit record: branch, diff, logs, screenshots, workflow run, and changed settings.
3. Revoke or narrow any exposed approval, token, app permission, website allowlist, or CI credential.
4. Rotate secrets if exposure is possible; do not wait for proof of misuse.
5. Revert or isolate changes before continuing.
6. Re-run the task with narrower permissions, fake/staging credentials, and explicit stop conditions.

## Budget and Constraint Notes

### Cheapest reliable path

Spend the first minute narrowing permissions, credentials, and scope. That is cheaper than later incident response, credential rotation, rollback, and forensic review.

### Fastest high-usage path

High-throughput users should spend extra turns on permission inventories, secret audits, diff reports, and rollback plans rather than broad unattended mutation.

### Low-attention path

Low-attention delegation requires stricter limits than supervised work: read-only first, branch-only mutation, fake credentials, explicit stop conditions, and review packets.

### Production-quality path

Production work requires human ownership of sensitive actions, least privilege, no real secrets in broad agent contexts, auditable evidence, and a rollback or revocation plan.

### Prototype versus production

Prototype shortcuts are acceptable only when data, credentials, and environments are fake or disposable. Production shortcuts need hard gates or refusal.

### Maintenance phase

Maintenance should remove persistent approvals, prune stale secrets, review CI permissions, and encode safer defaults so the same shortcut does not recur silently.

## Stable Core

- shortcut acceptability depends on blast radius, recoverability, permission scope, and evidence quality
- production, secrets, credentials, CI permissions, and GUI/account actions require stronger controls than prototypes
- the minimum guardrail should move the user at least one level up the guardrail ladder

## Volatile Surface

- Computer Use app approval UI
- Chrome allowlist/blocklist behavior
- browser-history controls
- Codex app settings labels

## Obsolescence Watch

This card should be revised if:

- persistent app and website approvals become risk-aware, task-scoped, automatically expiring, and unable to expose sensitive state without human reapproval

## Evidence and Sources

- `openai.codex.app_computer_use` — Official OpenAI Codex Computer Use guidance for app approvals, Always Allow, signed-in browser/account risk, sensitive-flow presence, screenshots, and GUI safety.
- `openai.codex.chrome_extension` — Official OpenAI Codex Chrome extension guidance for signed-in browser state, website approvals, always-allow behavior, browser-history risk, and extension permissions.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.computer_use`
- `vcb.shortcut.production_console_computer_use`
- `vcb.shortcut.logged_in_browser_secrets`
- `vcb.safety.secrets`
- `vcb.constraints.attention_budget`
- `vcb.failure.done_claim_without_evidence`

<!-- VCB:STOP_RETRIEVAL reason="always_allow_sensitive_apps_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.always_allow_sensitive_apps -->
