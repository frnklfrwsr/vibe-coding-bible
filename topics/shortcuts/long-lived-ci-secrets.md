<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.long_lived_ci_secrets version=0.1.0 -->
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
id: vcb.shortcut.long_lived_ci_secrets
title: Long-Lived CI Secrets
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- GitHub Actions
- CI/CD
- deployment automation
- cloud credentials
- non-interactive Codex
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- ci
- secrets
- credentials
- automation
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
- short-lived or OIDC credentials when available
- environment-scoped secrets
- protected deploy environments
- secret rotation plan
- no secret output in logs
shortcut_profiles:
- vcb.shortcut.long_lived_ci_secrets
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, permission scope,
  and evidence quality
- production, secrets, credentials, CI permissions, and GUI/account actions require
  stronger controls than prototypes
- the minimum guardrail should move the user at least one level up the guardrail ladder
likely_to_change:
- OIDC setup steps
- GitHub secret UI labels
- cloud-provider role configuration
- masking/log behavior
obsolete_when:
- CI providers make long-lived deploy credentials unnecessary and enforce short-lived
  scoped identities by default
related_topics:
- vcb.safety.secrets
- vcb.workflow.ci_noninteractive
- vcb.shortcut.overbroad_ci_permissions
- vcb.shortcut.real_secrets_in_prototype
- vcb.concepts.environment_variable
- vcb.constraints.recovery_budget
---

# Long-Lived CI Secrets

> Summary:
> Long-Lived CI Secrets means using persistent cloud/API tokens in CI because short-lived credentials, OIDC, or scoped environments take more setup.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.long_lived_ci_secrets.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “Put the token in CI and move on.” The hidden problem is duration: a long-lived secret remains useful after the workflow, branch, contributor, or task has changed.

### Why it matters

CI logs, artifacts, forks, dependency scripts, third-party actions, and misconfigured jobs can expose or misuse credentials. A long-lived token turns a temporary mistake into an ongoing access problem.

### What good looks like

Good: “Use OIDC or short-lived scoped credentials where available; otherwise use the narrowest secret, environment protection, and rotation plan.”

### What bad looks like

Bad: “Store a broad personal access token or cloud root key in CI for all jobs.”

### Minimal example

A deploy workflow should receive a short-lived role for one environment, not a permanent account token available to build, test, and lint jobs.

### Checklist

- prefer OIDC or short-lived credentials
- scope secrets by environment/job
- keep secrets away from untrusted PR paths
- mask and avoid printing secret-derived values
- set rotation and revocation instructions before use

<!-- VCB:END_SECTION id=vcb.shortcut.long_lived_ci_secrets.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.long_lived_ci_secrets.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to judge secrets by scope, lifetime, exposure path, and revocation plan.

### Diagnostic questions

- Can this job use OIDC instead of a stored secret?
- What can the secret do if copied?
- Which jobs and branches can access it?
- How quickly can it be revoked and rotated?
- Could any logs or artifacts reveal secret-derived values?

### Coaching tactics

- ask Codex to inventory secret usage before changing workflows
- replace broad account tokens with environment-scoped credentials
- move deployment secrets behind protected environments
- add rotation notes to the PR
- never debug by echoing secret values

### Red flags

- cloud root keys in CI
- personal access tokens used as service credentials
- secrets available to all workflow jobs
- manual secret copies across repos
- no owner or rotation schedule

### Prompt pattern

```text
Inspect the CI workflow for long-lived secrets. Propose an OIDC or short-lived credential path if available. If not, list the narrowest scopes, protected environments, rotation plan, and jobs allowed to access each secret.
```

<!-- VCB:END_SECTION id=vcb.shortcut.long_lived_ci_secrets.ai_coach -->

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

- short-lived or OIDC credentials when available
- environment-scoped secrets
- protected deploy environments
- secret rotation plan
- no secret output in logs

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

- OIDC setup steps
- GitHub secret UI labels
- cloud-provider role configuration
- masking/log behavior

## Obsolescence Watch

This card should be revised if:

- CI providers make long-lived deploy credentials unnecessary and enforce short-lived scoped identities by default

## Evidence and Sources

- `github.docs.actions_oidc` — Official GitHub Actions OIDC guidance for cloud authentication without long-lived stored cloud secrets.
- `github.docs.actions_secrets` — Official GitHub Actions guidance for repository, environment, and organization secrets and log caution.
- `owasp.secrets_management` — OWASP Secrets Management Cheat Sheet for secret lifecycle, storage, auditing, rotation, and CI/CD secret discipline.
- `openai.codex.noninteractive` — Official OpenAI Codex non-interactive guidance for codex exec, CI/script use, sandbox defaults, and automation cautions.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.safety.secrets`
- `vcb.workflow.ci_noninteractive`
- `vcb.shortcut.overbroad_ci_permissions`
- `vcb.shortcut.real_secrets_in_prototype`
- `vcb.concepts.environment_variable`
- `vcb.constraints.recovery_budget`

<!-- VCB:STOP_RETRIEVAL reason="long_lived_ci_secrets_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.long_lived_ci_secrets -->
