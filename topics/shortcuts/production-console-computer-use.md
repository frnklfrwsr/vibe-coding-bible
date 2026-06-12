<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.production_console_computer_use version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
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
id: vcb.shortcut.production_console_computer_use
title: Production Console Computer Use
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex App
- Computer Use
- browser or GUI work
- production consoles
- admin dashboards
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- computer_use
- production
- permissions
- secrets
- blast_radius
risk_level:
  prototype: HIGH_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: DO_NOT_DO_IN_PRODUCTION
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: false
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- report-only mode for production
- human present for every mutation
- staging/fake account first
- explicit no-click list
- before/after evidence capture
shortcut_profiles:
- vcb.shortcut.production_console_computer_use
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, permission scope,
  and evidence quality
- production, secrets, credentials, CI permissions, and GUI/account actions require
  stronger controls than prototypes
- the minimum guardrail should move the user at least one level up the guardrail ladder
likely_to_change:
- Computer Use permission labels
- app approval settings
- browser-control behavior
- production-provider UI flows
obsolete_when:
- production GUI operations become formally sandboxed, reversible, auditable, and
  unable to mutate real user, billing, auth, or data state without explicit human
  action
related_topics:
- vcb.codex.computer_use
- vcb.safety.production_red_lines
- vcb.safety.secrets
- vcb.shortcut.always_allow_sensitive_apps
- vcb.constraints.recovery_budget
- vcb.failure.done_claim_without_evidence
---

# Production Console Computer Use

> Summary:
> Production Console Computer Use means using Codex Computer Use or browser control inside production/admin consoles where clicks can affect real users, money, data, or credentials.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.production_console_computer_use.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “Let Codex operate the production console because the UI is faster than writing code or scripts.” It is not a normal coding shortcut. It turns an AI task into an account action performed through your authority.

### Why it matters

Production consoles usually bypass code review, tests, CI, and rollback discipline. A wrong click, form submission, data export, permission change, or billing action may be treated by the service as your deliberate action.

### What good looks like

Good: “Use Codex to observe the screen and draft a step-by-step checklist; the human performs any production mutation.”

### What bad looks like

Bad: “@Computer, log into Stripe/Supabase/AWS/GitHub admin and fix the production setting while I step away.”

### Minimal example

Use Codex to compare a staging setting against production and produce a report. Do not let it click Save in production unless you are present and have approved that exact action.

### Checklist

- prefer staging or local reproduction
- use report-only mode for production consoles
- stay present for every sensitive click
- forbid deletions, billing, auth, and permission changes by default
- capture evidence before and after any approved action

<!-- VCB:END_SECTION id=vcb.shortcut.production_console_computer_use.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.production_console_computer_use.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that production GUI control is account-level authority, not just another test surface.

### Diagnostic questions

- Is this a real production console or a staging/sandbox account?
- Could the task be done by a script, PR, or read-only report instead?
- What exact clicks are allowed and what clicks are forbidden?
- Is any customer, billing, auth, credential, or deletion path visible?
- Who is accountable if the UI action is wrong?

### Coaching tactics

- downgrade to observe/report mode
- move the task to staging or a fake account
- require a click-by-click plan before control
- stop at the confirmation screen for human action
- capture screenshots, audit trail, and rollback notes

### Red flags

- production admin console with Codex driving unattended
- ambiguous prompt like “fix the account”
- visible customer data or credentials
- permission, billing, auth, deletion, or deployment buttons
- no audit trail or rollback path

### Prompt pattern

```text
Use production GUI surfaces in report-only mode. Identify the exact screen, risk, and proposed action. Stop before any mutation, save, delete, permission, billing, auth, or credential-related action and wait for human approval.
```

<!-- VCB:END_SECTION id=vcb.shortcut.production_console_computer_use.ai_coach -->

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

- report-only mode for production
- human present for every mutation
- staging/fake account first
- explicit no-click list
- before/after evidence capture

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

- Computer Use permission labels
- app approval settings
- browser-control behavior
- production-provider UI flows

## Obsolescence Watch

This card should be revised if:

- production GUI operations become formally sandboxed, reversible, auditable, and unable to mutate real user, billing, auth, or data state without explicit human action

## Evidence and Sources

- `openai.codex.app_computer_use` — Official OpenAI Codex Computer Use guidance for app approvals, Always Allow, signed-in browser/account risk, sensitive-flow presence, screenshots, and GUI safety.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `owasp.secrets_management` — OWASP Secrets Management Cheat Sheet for secret lifecycle, storage, auditing, rotation, and CI/CD secret discipline.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.computer_use`
- `vcb.safety.production_red_lines`
- `vcb.safety.secrets`
- `vcb.shortcut.always_allow_sensitive_apps`
- `vcb.constraints.recovery_budget`
- `vcb.failure.done_claim_without_evidence`

<!-- VCB:STOP_RETRIEVAL reason="production_console_computer_use_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.production_console_computer_use -->
