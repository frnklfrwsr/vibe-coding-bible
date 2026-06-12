<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.real_secrets_in_prototype version=0.1.0 -->
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
id: vcb.shortcut.real_secrets_in_prototype
title: Real Secrets in Prototype
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- prototype apps
- Codex CLI
- Codex App
- cloud delegation
- browser or GUI work
- CI
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- secrets
- prototype
- credentials
- environment
- blast_radius
risk_level:
  prototype: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
  personal_tool: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
  internal_tool: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
  public_app: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: false
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: false
minimum_guardrails:
- fake or sandbox credentials
- ignored local config files
- no secrets in prompts/logs/screenshots
- low-scope revocable keys only if unavoidable
- rotate on exposure
shortcut_profiles:
- vcb.shortcut.real_secrets_in_prototype
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, permission scope,
  and evidence quality
- production, secrets, credentials, CI permissions, and GUI/account actions require
  stronger controls than prototypes
- the minimum guardrail should move the user at least one level up the guardrail ladder
likely_to_change:
- provider sandbox features
- secret-manager UI labels
- environment-variable handling
- Codex data/control behavior
obsolete_when:
- secret-bearing prototypes can be proven unable to leak, persist, commit, display,
  or transmit credentials outside an isolated test boundary
related_topics:
- vcb.safety.secrets
- vcb.concepts.environment_variable
- vcb.shortcut.cloud_work_with_real_secrets
- vcb.shortcut.long_lived_ci_secrets
- vcb.constraints.production_quality
- vcb.failure.done_claim_without_evidence
---

# Real Secrets in Prototype

> Summary:
> Real Secrets in Prototype means using live API keys, production databases, real customer accounts, or payment credentials in a prototype because fake data slows the first demo.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.real_secrets_in_prototype.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “It is just a prototype, so using the real key is fine.” That is backwards. Prototypes are messy by design, so real secrets are less safe there than in hardened systems.

### Why it matters

Prototype code is often pasted, logged, screen-shared, committed, forked, deployed casually, or delegated to broad agents. A real key can survive the throwaway code and create real account, data, or billing exposure.

### What good looks like

Good: “Use fake credentials, sandbox accounts, local test data, or revocable low-scope keys until the system is ready for security review.”

### What bad looks like

Bad: “Put the production Stripe/OpenAI/database key in .env so Codex can build faster.”

### Minimal example

Use a payment sandbox key and fake customer record for the checkout prototype. Do not connect a disposable demo to a real billing account.

### Checklist

- use sandbox/fake credentials
- keep .env out of prompts and commits
- separate prototype data from production data
- use low-scope revocable keys if a real service is unavoidable
- rotate immediately after any exposure

<!-- VCB:END_SECTION id=vcb.shortcut.real_secrets_in_prototype.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.real_secrets_in_prototype.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that prototype speed should come from fake data, not weaker secret discipline.

### Diagnostic questions

- Is this key tied to real money, users, emails, data, or infrastructure?
- Could Codex see the secret through prompts, files, logs, browser state, or screenshots?
- Is the prototype repo private, disposable, and isolated?
- Can a sandbox key or mock service prove the same workflow?
- Is there a rotation plan if this was already exposed?

### Coaching tactics

- replace real keys with fake or sandbox values
- ask for a secret exposure inventory before continuing
- move config into ignored local files or secret managers
- add a no-real-secrets rule to AGENTS.md
- treat exposed prototype secrets as compromised

### Red flags

- production API key in .env during a demo
- real database URL in prototype code
- screenshots/logs showing tokens
- agent granted broad access to files with secrets
- “we will rotate later” without doing it now

### Prompt pattern

```text
Assume this prototype may be pasted, logged, committed, and delegated. Replace real secrets with fake or sandbox values. If any real credential is present, stop and list where it appears, what it can access, and the rotation steps.
```

<!-- VCB:END_SECTION id=vcb.shortcut.real_secrets_in_prototype.ai_coach -->

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

- fake or sandbox credentials
- ignored local config files
- no secrets in prompts/logs/screenshots
- low-scope revocable keys only if unavoidable
- rotate on exposure

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

- provider sandbox features
- secret-manager UI labels
- environment-variable handling
- Codex data/control behavior

## Obsolescence Watch

This card should be revised if:

- secret-bearing prototypes can be proven unable to leak, persist, commit, display, or transmit credentials outside an isolated test boundary

## Evidence and Sources

- `owasp.secrets_management` — OWASP Secrets Management Cheat Sheet for secret lifecycle, storage, auditing, rotation, and CI/CD secret discipline.
- `github.docs.actions_secrets` — Official GitHub Actions guidance for repository, environment, and organization secrets and log caution.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.safety.secrets`
- `vcb.concepts.environment_variable`
- `vcb.shortcut.cloud_work_with_real_secrets`
- `vcb.shortcut.long_lived_ci_secrets`
- `vcb.constraints.production_quality`
- `vcb.failure.done_claim_without_evidence`

<!-- VCB:STOP_RETRIEVAL reason="real_secrets_in_prototype_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.real_secrets_in_prototype -->
