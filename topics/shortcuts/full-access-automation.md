<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.full_access_automation version=0.1.0 -->
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
id: vcb.shortcut.full_access_automation
title: Full-Access Automation
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- non-interactive Codex
- CI/CD
- automation
- Codex CLI
- background tasks
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- automation
- permissions
- sandbox
- ci
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
- read-only automation first
- branch-only mutation
- no broad secrets
- command/network allowlist
- human review gate
shortcut_profiles:
- vcb.shortcut.full_access_automation
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, permission scope,
  and evidence quality
- production, secrets, credentials, CI permissions, and GUI/account actions require
  stronger controls than prototypes
- the minimum guardrail should move the user at least one level up the guardrail ladder
likely_to_change:
- Codex exec flags
- sandbox defaults
- approval-policy names
- CI runner permissions
obsolete_when:
- automated agents can be constrained to formally declared side effects with enforced
  review, rollback, and secret isolation by default
related_topics:
- vcb.workflow.ci_noninteractive
- vcb.shortcut.overbroad_ci_permissions
- vcb.shortcut.unattended_mutation
- vcb.shortcut.broad_agent_permissions
- vcb.constraints.review_budget
- vcb.safety.production_red_lines
---

# Full-Access Automation

> Summary:
> Full-Access Automation means running automated Codex or agent jobs with full filesystem, command, network, or credential access because approval prompts make automation inconvenient.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.full_access_automation.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “Automation only works if it never stops to ask.” That may be true for narrow read-only reporting, but it is false for broad mutation with secrets and network access.

### Why it matters

Full-access automation combines the worst risk multipliers: unattended execution, broad permissions, hidden context, dependency scripts, network paths, and weak human review.

### What good looks like

Good: “Use read-only or workspace-limited automation by default, then require explicit human approval for any write, network, deployment, or credential-bearing action.”

### What bad looks like

Bad: “Run codex exec with full access, no approval, and production secrets in CI to fix whatever it finds.”

### Minimal example

A nightly job can produce a read-only maintenance report. It should not push branches, rotate config, update dependencies, and deploy without a human gate.

### Checklist

- read-only by default
- workspace-only before full access
- no production secrets in broad automation
- allowlist commands and network hosts
- require PR/diff review before merge or deploy

<!-- VCB:END_SECTION id=vcb.shortcut.full_access_automation.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.full_access_automation.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach automation as a permission amplifier: unattended plus broad access is a security decision, not a convenience setting.

### Diagnostic questions

- What can the automation mutate?
- Can it reach the network?
- Can it read secrets?
- Who reviews the diff and logs?
- What stops it from repeating a wrong action across many files or repos?

### Coaching tactics

- downgrade to read-only report generation
- split analysis from mutation
- make writes branch-only
- require explicit allowlists
- add a stop condition after the first unexpected command

### Red flags

- approval never with full access
- network enabled with credentials
- automation can push directly to protected branches
- job can alter CI, secrets, deployments, or permissions
- no human owner for the output

### Prompt pattern

```text
Design this automation with the least authority possible. Separate read-only analysis from mutation. If mutation is required, restrict it to a branch, list allowed commands/network hosts, and require human diff review before merge or deployment.
```

<!-- VCB:END_SECTION id=vcb.shortcut.full_access_automation.ai_coach -->

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

- read-only automation first
- branch-only mutation
- no broad secrets
- command/network allowlist
- human review gate

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

- Codex exec flags
- sandbox defaults
- approval-policy names
- CI runner permissions

## Obsolescence Watch

This card should be revised if:

- automated agents can be constrained to formally declared side effects with enforced review, rollback, and secret isolation by default

## Evidence and Sources

- `openai.codex.noninteractive` — Official OpenAI Codex non-interactive guidance for codex exec, CI/script use, sandbox defaults, and automation cautions.
- `openai.codex.sandboxing` — Official OpenAI Codex sandboxing concept guidance for read-only, workspace-write, approval, and full-access modes.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `github.docs.actions_secure_use` — Official GitHub Actions secure-use guidance for workflow hardening, third-party action risk, and least-privilege posture.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.ci_noninteractive`
- `vcb.shortcut.overbroad_ci_permissions`
- `vcb.shortcut.unattended_mutation`
- `vcb.shortcut.broad_agent_permissions`
- `vcb.constraints.review_budget`
- `vcb.safety.production_red_lines`

<!-- VCB:STOP_RETRIEVAL reason="full_access_automation_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.full_access_automation -->
