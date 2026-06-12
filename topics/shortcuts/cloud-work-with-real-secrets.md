<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.cloud_work_with_real_secrets version=0.1.0 -->
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
id: vcb.shortcut.cloud_work_with_real_secrets
title: Cloud Work with Real Secrets
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex Cloud
- background tasks
- cloud environments
- internet-enabled agents
- setup scripts
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- cloud
- secrets
- credentials
- internet_access
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
- fake/staging credentials by default
- least-scope revocable tokens
- internet access off unless justified
- read-only inspection first
- rotate after unsafe exposure
shortcut_profiles:
- vcb.shortcut.cloud_work_with_real_secrets
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, permission scope,
  and evidence quality
- production, secrets, credentials, CI permissions, and GUI/account actions require
  stronger controls than prototypes
- the minimum guardrail should move the user at least one level up the guardrail ladder
likely_to_change:
- Codex cloud environment behavior
- internet allowlist settings
- setup-script behavior
- provider credential mechanisms
obsolete_when:
- cloud delegated agents can use verifiable just-in-time credentials that cannot be
  logged, read by dependencies, exfiltrated, or used outside the task boundary
related_topics:
- vcb.codex.cloud
- vcb.safety.secrets
- vcb.shortcut.real_secrets_in_prototype
- vcb.shortcut.unattended_mutation
- vcb.constraints.operating_mode
- vcb.failure.context_pollution
---

# Cloud Work with Real Secrets

> Summary:
> Cloud Work with Real Secrets means delegating cloud/background Codex work while real credentials, tokens, or sensitive environment values are available to the task.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.cloud_work_with_real_secrets.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “Cloud Codex needs the same secrets my local app needs.” Sometimes a task needs environment setup, but real secrets inside delegated cloud work create a larger trust and exfiltration surface.

### Why it matters

Cloud tasks can run commands, inspect files, use internet access if enabled, and produce logs or summaries. If real secrets are present, a mistaken command, malicious dependency, prompt injection, or overbroad environment can expose them.

### What good looks like

Good: “Use fake, sandbox, or least-scope revocable credentials in delegated cloud work; keep production secrets outside the task unless a human-approved security case requires them.”

### What bad looks like

Bad: “Put production database and cloud provider keys into the cloud task so the agent can debug freely.”

### Minimal example

Let Codex reproduce a bug against a seeded staging database with a revocable test token, not the production database with customer data.

### Checklist

- use sandbox or staging credentials
- avoid production data and production keys
- limit internet access and dependency installation
- review environment setup scripts
- rotate credentials if they were exposed to an unsafe task

<!-- VCB:END_SECTION id=vcb.shortcut.cloud_work_with_real_secrets.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.cloud_work_with_real_secrets.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach delegated cloud work as a separate environment with its own secret policy, not a copy of the developer laptop.

### Diagnostic questions

- Which secrets does the cloud task actually need?
- Can the task use mocks, fixtures, or staging data?
- Is internet access enabled?
- Can dependency scripts or untrusted content read the secret?
- What logs, summaries, or artifacts might contain secret-derived values?

### Coaching tactics

- ask for a secret necessity table
- replace production secrets with scoped staging values
- disable internet access unless required
- run read-only inspection before execution
- treat real-secret cloud exposure as a rotation event

### Red flags

- production database URL in delegated cloud work
- cloud agent with internet access and real tokens
- setup scripts that print environment values
- customer data mounted for a debugging task
- secret exposure accepted because the branch is private

### Prompt pattern

```text
Before using any cloud task environment, list every required secret and classify it as fake, sandbox, staging, or production. Replace production secrets with test equivalents where possible. If a real secret remains, state why it is required, how it is scoped, and the rotation plan.
```

<!-- VCB:END_SECTION id=vcb.shortcut.cloud_work_with_real_secrets.ai_coach -->

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

- fake/staging credentials by default
- least-scope revocable tokens
- internet access off unless justified
- read-only inspection first
- rotate after unsafe exposure

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

- Codex cloud environment behavior
- internet allowlist settings
- setup-script behavior
- provider credential mechanisms

## Obsolescence Watch

This card should be revised if:

- cloud delegated agents can use verifiable just-in-time credentials that cannot be logged, read by dependencies, exfiltrated, or used outside the task boundary

## Evidence and Sources

- `openai.codex.cloud_internet_access` — Official OpenAI Codex web internet-access guidance for allowlists, prompt-injection, exfiltration, dependency, and license risk.
- `openai.codex.cloud_environments` — Official OpenAI Codex cloud environment guidance for setup scripts, environment configuration, and cloud execution loop.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `owasp.secrets_management` — OWASP Secrets Management Cheat Sheet for secret lifecycle, storage, auditing, rotation, and CI/CD secret discipline.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.cloud`
- `vcb.safety.secrets`
- `vcb.shortcut.real_secrets_in_prototype`
- `vcb.shortcut.unattended_mutation`
- `vcb.constraints.operating_mode`
- `vcb.failure.context_pollution`

<!-- VCB:STOP_RETRIEVAL reason="cloud_work_with_real_secrets_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.cloud_work_with_real_secrets -->
