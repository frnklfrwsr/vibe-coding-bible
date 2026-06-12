<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.unattended_mutation version=0.1.0 -->
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
id: vcb.shortcut.unattended_mutation
title: Unattended Mutation
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex Cloud
- Codex App
- non-interactive Codex
- automations
- subagents
- CI/CD
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- unattended
- automation
- permissions
- cloud
- blast_radius
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
- isolated branch/worktree
- diff-size or milestone cap
- no production/secrets/deploy actions
- review packet required
- human merge gate
shortcut_profiles:
- vcb.shortcut.unattended_mutation
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, permission scope,
  and evidence quality
- production, secrets, credentials, CI permissions, and GUI/account actions require
  stronger controls than prototypes
- the minimum guardrail should move the user at least one level up the guardrail ladder
likely_to_change:
- cloud/background task controls
- automation settings
- approval behavior
- worktree mechanics
obsolete_when:
- agent platforms provide reliable side-effect budgets, atomic rollback, and enforced
  stop conditions for every unattended mutating task
related_topics:
- vcb.codex.cloud
- vcb.codex.automations
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.reviewing_cloud_summary_only
- vcb.constraints.attention_budget
- vcb.constraints.recovery_budget
---

# Unattended Mutation

> Summary:
> Unattended Mutation means letting an agent change files, settings, data, CI, dependencies, or accounts while the human is not checking milestones or evidence.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.unattended_mutation.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “Let it run and I will review later.” Review-later can work for isolated branches. It breaks down when the agent can mutate production, shared state, CI, secrets, dependencies, or many files without checkpoints.

### Why it matters

The longer a mutating run continues without supervision, the more hidden assumptions can compound. Recovery moves from “revert a small diff” to “untangle unknown edits, logs, migrations, permissions, and side effects.”

### What good looks like

Good: “Run unattended analysis or branch-only changes with checkpoint summaries, then review the diff, commands, and evidence before merging.”

### What bad looks like

Bad: “Let the agent update dependencies, fix tests, push CI changes, and deploy while I am offline.”

### Minimal example

A background task can draft a branch that updates docs. It should not modify production config, secrets, database migrations, and deployment workflows unattended.

### Checklist

- branch/worktree isolation
- small milestone checkpoints
- no production data or secrets
- no direct deploy or protected-branch writes
- final report with changed files, commands, evidence, and risks

<!-- VCB:END_SECTION id=vcb.shortcut.unattended_mutation.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.unattended_mutation.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the difference between unattended thinking and unattended mutation. The first is often useful; the second needs isolation.

### Diagnostic questions

- What can the agent change while unattended?
- Can it deploy, push, migrate, delete, or alter permissions?
- What evidence will prove the result?
- How big can the diff get before stopping?
- What is the rollback path?

### Coaching tactics

- convert task to read-only planning if risk is high
- cap unattended runs to one slice or milestone
- use separate worktrees/branches
- forbid production and secret-touching actions
- require a final review packet

### Red flags

- unattended run can deploy
- agent can edit CI/secrets/auth/payment code
- no diff-size limit
- broad refactor plus no checkpoints
- summary accepted without changed-file review

### Prompt pattern

```text
You may work unattended only inside this branch/worktree and only on the stated files. Stop after the first milestone, report changed files, commands run, evidence, unresolved risks, and anything outside scope. Do not deploy, migrate, delete, change secrets, or alter CI permissions.
```

<!-- VCB:END_SECTION id=vcb.shortcut.unattended_mutation.ai_coach -->

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

- isolated branch/worktree
- diff-size or milestone cap
- no production/secrets/deploy actions
- review packet required
- human merge gate

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

- cloud/background task controls
- automation settings
- approval behavior
- worktree mechanics

## Obsolescence Watch

This card should be revised if:

- agent platforms provide reliable side-effect budgets, atomic rollback, and enforced stop conditions for every unattended mutating task

## Evidence and Sources

- `openai.codex.cloud` — Official OpenAI Codex cloud guidance for delegated background task shape and review boundary.
- `openai.codex.noninteractive` — Official OpenAI Codex non-interactive guidance for codex exec, CI/script use, sandbox defaults, and automation cautions.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.cloud`
- `vcb.codex.automations`
- `vcb.shortcut.unattended_long_runs`
- `vcb.shortcut.reviewing_cloud_summary_only`
- `vcb.constraints.attention_budget`
- `vcb.constraints.recovery_budget`

<!-- VCB:STOP_RETRIEVAL reason="unattended_mutation_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.unattended_mutation -->
