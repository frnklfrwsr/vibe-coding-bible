<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.overbroad_ci_permissions version=0.1.0 -->
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
id: vcb.shortcut.overbroad_ci_permissions
title: Overbroad CI Permissions
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- GitHub Actions
- non-interactive Codex
- CI/CD
- repository tokens
- deployment automation
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- ci
- permissions
- automation
- secrets
- supply_chain
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: DO_NOT_DO_IN_PRODUCTION
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: false
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- job-level minimal permissions
- separate deploy/release jobs
- no secrets for untrusted PR code
- review third-party actions
- document each write scope
shortcut_profiles:
- vcb.shortcut.overbroad_ci_permissions
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, permission scope,
  and evidence quality
- production, secrets, credentials, CI permissions, and GUI/account actions require
  stronger controls than prototypes
- the minimum guardrail should move the user at least one level up the guardrail ladder
likely_to_change:
- GitHub token permission defaults
- workflow syntax
- Codex CI guidance
- cloud deployment permission models
obsolete_when:
- CI providers can prove per-command least privilege automatically and block broad
  permissions from untrusted code paths by default
related_topics:
- vcb.workflow.ci_noninteractive
- vcb.workflow.ci_triage
- vcb.concepts.ci
- vcb.shortcut.long_lived_ci_secrets
- vcb.constraints.production_quality
- vcb.failure.ci_false_confidence
---

# Overbroad CI Permissions

> Summary:
> Overbroad CI Permissions means giving CI workflows broad repository, package, deployment, or cloud permissions because narrowing them takes setup time.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.overbroad_ci_permissions.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “The workflow is easier if the token can do everything.” That trades a small setup cost for a large blast radius.

### Why it matters

CI runs commands from code, dependencies, and workflow definitions. If that path has broad write or deployment authority, a compromised action, script, dependency, or prompt-driven change can reach repositories, releases, secrets, packages, or production environments.

### What good looks like

Good: “Set the workflow token permissions to only the scopes this job needs, then add permissions one by one when evidence demands it.”

### What bad looks like

Bad: “Give the CI job write-all and deployment access so Codex can stop failing.”

### Minimal example

A test job usually needs read access and artifact upload, not package publishing, pull-request approval, deployment, or repository administration.

### Checklist

- start from read-only or minimal token permissions
- separate test, release, and deploy jobs
- pin or review third-party actions
- avoid secrets on untrusted PR paths
- document why each write permission exists

<!-- VCB:END_SECTION id=vcb.shortcut.overbroad_ci_permissions.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.overbroad_ci_permissions.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach least privilege as a debugging accelerator: narrower permissions make failures clearer and compromises smaller.

### Diagnostic questions

- What is the exact workflow job trying to do?
- Which permission is failing, and is the failure legitimate?
- Can the job be split into read-only test and separate release/deploy phases?
- Can a fork or dependency script influence this workflow?
- What token or cloud role would be exposed if the job is compromised?

### Coaching tactics

- ask for a permissions diff instead of a blanket fix
- require job-level permissions, not repository-wide defaults
- treat write-all as a temporary incident exception
- add a comment explaining each permission
- route deploy permissions through protected environments

### Red flags

- permissions: write-all
- broad cloud credentials in generic CI jobs
- publishing or deployment in the same job as untrusted tests
- pull_request_target with secrets and untrusted code
- Codex asked to “just fix permissions” without a threat model

### Prompt pattern

```text
Review this workflow for least-privilege permissions. For each permission, state the command that needs it, the safer narrower value, and whether it belongs in this job or a separate protected release/deploy job.
```

<!-- VCB:END_SECTION id=vcb.shortcut.overbroad_ci_permissions.ai_coach -->

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

- job-level minimal permissions
- separate deploy/release jobs
- no secrets for untrusted PR code
- review third-party actions
- document each write scope

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

- GitHub token permission defaults
- workflow syntax
- Codex CI guidance
- cloud deployment permission models

## Obsolescence Watch

This card should be revised if:

- CI providers can prove per-command least privilege automatically and block broad permissions from untrusted code paths by default

## Evidence and Sources

- `github.docs.actions_secure_use` — Official GitHub Actions secure-use guidance for workflow hardening, third-party action risk, and least-privilege posture.
- `github.docs.github_token` — Official GitHub Actions guidance for GITHUB_TOKEN authentication and permissions.
- `openai.codex.noninteractive` — Official OpenAI Codex non-interactive guidance for codex exec, CI/script use, sandbox defaults, and automation cautions.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.ci_noninteractive`
- `vcb.workflow.ci_triage`
- `vcb.concepts.ci`
- `vcb.shortcut.long_lived_ci_secrets`
- `vcb.constraints.production_quality`
- `vcb.failure.ci_false_confidence`

<!-- VCB:STOP_RETRIEVAL reason="overbroad_ci_permissions_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.overbroad_ci_permissions -->
