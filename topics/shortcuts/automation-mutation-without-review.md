<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.automation_mutation_without_review version=0.1.0 -->
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
id: vcb.shortcut.automation_mutation_without_review
title: Automation Mutation Without Review
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
- report-only default
- branch-only mutation
- human owner
- protected-branch/deploy ban
- audit log and review packet
shortcut_profiles:
- vcb.shortcut.automation_mutation_without_review
durable_principles:
- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
likely_to_change:
- Codex automation worktree behavior
- non-interactive sandbox flags
- approval/security controls
- CI and app integration mechanics
obsolete_when:
- scheduled agents can safely mutate with enforced least privilege, complete audit trails,
  atomic rollback, and mandatory human gates by default
related_topics:
- vcb.codex.automations
- vcb.workflow.ci_noninteractive
- vcb.shortcut.unattended_mutation
- vcb.shortcut.full_access_automation
- vcb.shortcut.automation_spam
- vcb.constraints.recovery_budget
---

# Automation Mutation Without Review

> Summary:
> Automation Mutation Without Review means allowing scheduled or non-interactive AI work to change files, settings, PRs, or accounts without an explicit human review gate.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.automation_mutation_without_review.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut turns “automate a report” into “automate changes.” Mutation is not automatically wrong, but a recurring or script-driven agent needs tighter controls than a supervised session because mistakes repeat without you noticing.

### Why it matters

Automations can run when attention is low. If they can write, push, change config, or operate tools without review, a bad prompt or stale context becomes a recurring side-effect machine.

### What good looks like

Good: “Automation reports proposed changes with patch suggestions; a human chooses whether to apply them.”

### What bad looks like

Bad: “Every night, have Codex update dependencies, fix failures, and push changes to the repo.”

### Minimal example

A scheduled docs freshness check should open a report or draft branch, not directly rewrite public docs and merge them.

### Checklist

- start report-only
- use branch-only mutation if mutation is required
- set owner and review gate
- forbid protected branches, deploys, secrets, and migrations
- keep logs and changed-file evidence

<!-- VCB:END_SECTION id=vcb.shortcut.automation_mutation_without_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.automation_mutation_without_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach that recurring mutation needs a gate. Report/propose is the default; write-capable automation is an exception with isolation.

### Diagnostic questions

- Can this automation write files or settings?
- Where do changes land?
- Who reviews them?
- Can it affect protected branches or production?
- What audit trail exists?

### Coaching tactics

- downgrade to report-only
- branch-only for first runs
- require human-owned merge
- use least privilege
- capture structured output and logs

### Red flags

- automation has broad write access
- no owner named
- runs on protected branch or production config
- dependency or CI changes happen unattended
- same prompt controls repeated mutation

### Prompt pattern

```text
Make this automation report/propose first. If mutation is unavoidable, it may only create a branch or patch artifact, must not touch protected branches, deploys, secrets, migrations, or production config, and must return changed files, commands, evidence, and review checklist for a human owner.
```

<!-- VCB:END_SECTION id=vcb.shortcut.automation_mutation_without_review.ai_coach -->

## Shortcut Reality

### Ideal practice

Keep recurring AI automation report-only unless a specific, isolated, branch-only mutation flow has review gates and audit evidence.

### What people often do instead

They skip review because the automation is “just routine” and forget that routine mistakes repeat.

### When the shortcut may be acceptable

Acceptable for disposable branch-only changes in low-risk repos with human merge and easy rollback.

### When it becomes a bad trade

Bad for dependencies, CI, secrets, migrations, production config, public docs, auth, billing, or data-changing workflows.

### Risk profile

- Probability: medium for scheduled coding tasks; high when the same automation prompt runs against changing context.
- Impact: high to severe when write permissions reach shared repos, CI, secrets, or production.
- Recoverability: medium before merge; low after repeated unattended writes or credential exposure.

### Blast radius

The shortcut can create repeated bad commits, hidden config drift, broken CI, stale public documentation, or a chain of automated fixes that mask the original issue.

### Minimum guardrails

- report-only default
- branch-only mutation
- human owner
- protected-branch/deploy ban
- audit log and review packet

### Recovery plan

1. Disable the automation.
2. List all runs, branches, commits, settings, and external actions it touched.
3. Revert or isolate mutations before restarting.
4. Rotate credentials if broad tokens or secrets were exposed.
5. Restart as report-only and add explicit owner/review gates.

## Budget and Constraint Notes

### Cheapest reliable path

Write the smallest task packet, isolation rule, and review packet requirement before launching the agent. This costs less than reconciling a broad or unsafe background result.

### Fastest high-usage path

Paying for automation is rational only when review cost is lower than manual execution. Ungated mutation creates downstream cleanup cost.

### Low-attention path

Low-attention automation should be report-only. If it must mutate, it must stop at a branch or patch and wait.

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

- Codex automation worktree behavior
- non-interactive sandbox flags
- approval/security controls
- CI and app integration mechanics

## Obsolescence Watch

This card should be revised if:

- scheduled agents can safely mutate with enforced least privilege, complete audit trails, atomic rollback, and mandatory human gates by default

## Evidence and Sources

- `openai.codex.app_automations` — Official OpenAI Codex automations guidance for scheduled background tasks, inbox behavior, and worktree/local-project choices.
- `openai.codex.noninteractive` — Official OpenAI Codex non-interactive guidance for `codex exec`, scripts/CI use, sandbox defaults, and automation cautions.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `openai.codex.app_worktrees` — Official OpenAI Codex app worktree guidance for isolated parallel local task execution.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.automations`
- `vcb.workflow.ci_noninteractive`
- `vcb.shortcut.unattended_mutation`
- `vcb.shortcut.full_access_automation`
- `vcb.shortcut.automation_spam`
- `vcb.constraints.recovery_budget`

<!-- VCB:STOP_RETRIEVAL reason="automation_mutation_without_review_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.automation_mutation_without_review -->
