<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.unattended_cloud_delegation version=0.1.0 -->
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
id: vcb.shortcut.unattended_cloud_delegation
title: Unattended Cloud Delegation
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
- branch/worktree isolation
- explicit task packet
- do-not-touch list
- milestone stop condition
- human review before merge
shortcut_profiles:
- vcb.shortcut.unattended_cloud_delegation
durable_principles:
- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
likely_to_change:
- Codex Cloud task controls
- cloud environment and worktree behavior
- PR and follow-up mechanics
- review UI labels and summaries
obsolete_when:
- cloud agents enforce reliable side-effect budgets, automatic safe rollback, mandatory review
  packets, and hard stop conditions for unattended mutating work
related_topics:
- vcb.codex.cloud
- vcb.codex.automations
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.reviewing_cloud_summary_only
- vcb.constraints.attention_budget
- vcb.constraints.recovery_budget
---

# Unattended Cloud Delegation

> Summary:
> Unattended Cloud Delegation means sending Codex or another agent to work in the cloud/background and treating “I will check later” as the main safety control.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.unattended_cloud_delegation.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “Start the cloud task, leave it alone, and review when it says done.” That can work for isolated research or a small branch. It fails when the task can edit broad code, touch secrets, change CI, open a PR, or drift from the original goal while nobody is watching.

### Why it matters

Cloud work can run outside your foreground attention and can run in parallel. The risk is not that cloud delegation is bad; the risk is giving a background worker too much scope, too little context, and no stop condition.

### What good looks like

Good: “Work only on this branch/worktree, touch only the listed files, stop after the first milestone, and return changed files, commands run, evidence, gaps, and risks.”

### What bad looks like

Bad: “Fix the whole auth flow in the cloud while I am offline and open a PR when it is done.”

### Minimal example

A background task can draft a docs cleanup branch. It should not rewrite auth, update dependencies, alter deployment settings, and summarize the result as safe to merge.

### Checklist

- use a branch or worktree
- give a do-not-touch list
- cap the task by milestone or file set
- forbid deploys, secrets, migrations, and production actions
- require a final review packet before merge

<!-- VCB:END_SECTION id=vcb.shortcut.unattended_cloud_delegation.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.unattended_cloud_delegation.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach that background execution is an attention shortcut, not an ownership transfer. The human still owns scope, review, merge, and rollback.

### Diagnostic questions

- What can the cloud task change while nobody is watching?
- Is the task isolated to a branch/worktree?
- What exact files, folders, or behaviors are in scope?
- What should make the agent stop instead of continue?
- What evidence will the human review before merging?

### Coaching tactics

- convert broad unattended work into a plan-only pass
- set a file/folder scope and forbidden areas
- require one milestone, then stop
- use branch/worktree isolation
- ask for a review packet instead of a confident summary

### Red flags

- task says “fix everything” or “clean up the repo”
- no branch/worktree isolation
- cloud task can alter CI, secrets, migrations, or deploy files
- no stop condition
- human plans to merge from summary only

### Prompt pattern

```text
You may work in the cloud only on this branch/worktree and only on the stated scope. Stop after the first milestone. Do not touch secrets, CI permissions, deployment, migrations, production config, or files outside scope. Return changed files, commands run, evidence, gaps, risks, and a rollback note.
```

<!-- VCB:END_SECTION id=vcb.shortcut.unattended_cloud_delegation.ai_coach -->

## Shortcut Reality

### Ideal practice

Delegate only a bounded cloud task with explicit context, branch/worktree isolation, stop conditions, and a review packet.

### What people often do instead

They use cloud/background work as a way to avoid writing a task packet or reviewing intermediate decisions.

### When the shortcut may be acceptable

Acceptable for isolated prototype or documentation work where rollback is trivial, no secrets or production state are present, and the result is inspected before merge.

### When it becomes a bad trade

Bad for production, auth, billing, migrations, CI, secrets, broad refactors, or any task where a wrong branch can create hidden side effects.

### Risk profile

- Probability: medium for scoped cloud tasks; high when scope is vague and review is deferred.
- Impact: low for disposable isolated branches; high or severe for production paths, credentials, or shared repos.
- Recoverability: medium before merge with a clean branch; low after deploy, migration, credential exposure, or large unreviewed diff.

### Blast radius

The shortcut can spread from one unattended branch into broad diff drift, hidden dependency/config changes, stale PR assumptions, and expensive recovery work.

### Minimum guardrails

- branch/worktree isolation
- explicit task packet
- do-not-touch list
- milestone stop condition
- human review before merge

### Recovery plan

1. Stop or pause the cloud task if still running.
2. Preserve branch, logs, task prompt, changed-file list, and command output.
3. Diff against the intended base and mark out-of-scope edits.
4. Revert or split unsafe changes before continuing.
5. Rotate credentials if secrets or sensitive environment data may have been exposed.
6. Rerun as a smaller cloud task or plan-only pass with explicit stop conditions.

## Budget and Constraint Notes

### Cheapest reliable path

Write the smallest task packet, isolation rule, and review packet requirement before launching the agent. This costs less than reconciling a broad or unsafe background result.

### Fastest high-usage path

High-throughput users should batch cloud tasks only after writing per-task scopes and a comparison/review rubric. Parallelizing vague work burns review budget.

### Low-attention path

Low-attention delegation requires stronger guardrails than supervised work: branch-only, no secrets, no deploy, stop-after-first-milestone, and final evidence packet.

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

- Codex Cloud task controls
- cloud environment and worktree behavior
- PR and follow-up mechanics
- review UI labels and summaries

## Obsolescence Watch

This card should be revised if:

- cloud agents enforce reliable side-effect budgets, automatic safe rollback, mandatory review packets, and hard stop conditions for unattended mutating work

## Evidence and Sources

- `openai.codex.cloud` — Official OpenAI Codex cloud guidance for delegated background and parallel cloud task shape.
- `openai.codex.cloud_environments` — Official OpenAI Codex cloud-environment guidance for containers, branch checkout, setup, environment variables, secrets, and task loop behavior.
- `openai.codex.app_worktrees` — Official OpenAI Codex app worktree guidance for isolated parallel local task execution.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for context, constraints, done-when criteria, planning, validation, and review.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.cloud`
- `vcb.codex.automations`
- `vcb.shortcut.unattended_long_runs`
- `vcb.shortcut.reviewing_cloud_summary_only`
- `vcb.constraints.attention_budget`
- `vcb.constraints.recovery_budget`

<!-- VCB:STOP_RETRIEVAL reason="unattended_cloud_delegation_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.unattended_cloud_delegation -->
