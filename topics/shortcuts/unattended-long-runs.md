<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.unattended_long_runs version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
last_reviewed: '2026-06-09'
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
  shortcut harm reduction
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
id: vcb.shortcut.unattended_long_runs
title: Unattended Long Runs
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex Cloud
- Codex worktrees
- codex exec
- scheduled jobs
- background tasks
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- delegation
- automation
- low_attention
- usage_burn
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- branch or worktree isolation
- explicit stop condition
- no secrets
- scope cap
- final evidence report
shortcut_profiles:
- vcb.shortcut.unattended_long_runs
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls
  than prototypes
likely_to_change:
- non-interactive flags
- worktree behavior
- cloud task controls
- usage accounting
- automation UI
obsolete_when:
- long-running agents can guarantee bounded scope, safe permissions, and complete
  evidence without human review
related_topics:
- vcb.codex.cloud
- vcb.workflow.ci_noninteractive
- vcb.constraints.attention_budget
- vcb.constraints.scope_budget
- vcb.constraints.usage_burn
- vcb.failure.context_pollution
---

# Unattended Long Runs

> Summary:
> Unattended long runs are large Codex tasks left running without bounded milestones, permission limits, or a reviewable final contract.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.unattended_long_runs.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut asks Codex to keep working while you leave. That can be useful for read-only audits or isolated background work. It fails when the task mutates too much, spends too much, or drifts away from the original objective.

### Why it matters

Time is not the only cost. Long runs accumulate context drift, usage burn, broad diffs, and hidden assumptions. The longer the run, the more important the stop condition.

### What good looks like

Good: “Run a bounded read-only audit or one isolated implementation slice, then stop with findings, files changed, commands run, and unresolved risks.”

### What bad looks like

Bad: “Work on this until it is done; I will check later.”

### Minimal example

Ask for a two-hour dependency audit report in read-only mode, not an unattended broad remediation that edits build files, CI, and application code.

### Checklist

- define a stop condition
- isolate the worktree or branch
- cap mutation scope
- keep secrets unavailable
- require a structured final report
- review before continuing the run

<!-- VCB:END_SECTION id=vcb.shortcut.unattended_long_runs.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.unattended_long_runs.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that unattended is a supervision mode, not a quality guarantee. The lower the attention, the narrower the task must be.

### Diagnostic questions

- Is this read-only or mutating?
- What should make the run stop?
- Which files may change?
- What budget or runtime cap exists?
- Can the human review the diff if it gets large?

### Coaching tactics

- convert long work into milestones
- default to read-only reports for broad tasks
- use isolated branches/worktrees
- require evidence and residual-risk sections
- block unattended production or secret-bearing work

### Red flags

- no stop condition
- task says “fix everything”
- same run can edit and deploy
- secret-bearing environment
- multiple areas changed before review

### Prompt pattern

```text
You may work only on this bounded slice. Stop after the first reviewable milestone and report: files changed, commands run, evidence, unresolved risks, and whether another pass is needed. Do not broaden scope without asking.
```

<!-- VCB:END_SECTION id=vcb.shortcut.unattended_long_runs.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They take the shortcut because it reduces immediate friction: fewer prompts, fewer checks, fewer approvals, less review, or a faster-looking result.

### When the shortcut may be acceptable

Acceptable for disposable prototypes, throwaway local experiments, or tightly isolated work where rollback is trivial, no real users or secrets are involved, and the output is not treated as production evidence.

### When it becomes a bad trade

Bad when the task touches production, auth, payments, data deletion, secrets, CI permissions, public documentation, dependency supply chain, or a diff too broad for available review.

### Risk profile

- Probability: medium for disciplined small tasks; high when prompts are vague, permissions are broad, or review is deferred.
- Impact: low for local throwaways; high for production, team repos, security-sensitive systems, and public releases.
- Recoverability: good before merge with a clean branch; worse after release, data migration, dependency rollout, credential exposure, or undocumented behavior change.

### Blast radius

The shortcut can spread from one fast turn into merged code, stale tests, false release notes, hidden security exposure, future debugging assumptions, and more expensive recovery work.

### Minimum guardrails

- branch or worktree isolation
- explicit stop condition
- no secrets
- scope cap
- final evidence report

### Recovery plan

1. Stop the current run or merge path.
2. Create or restore a Git checkpoint.
3. Ask Codex for a risk and evidence table for the shortcut taken.
4. Run the smallest relevant verification or review pass.
5. Revert, isolate, or split the work if evidence is missing.
6. Update the prompt, AGENTS.md guidance, or workflow checklist so the same shortcut has a guardrail next time.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest guardrail that can catch the likely failure before spending on retries, broad context, or recovery.

### Fastest high-usage path

High-throughput users can spend more turns, but should spend them on bounded checks, comparison, or review rather than broad unverified mutation.

### Low-attention path

Low-attention delegation is only safe when scope, permissions, and stop conditions are narrower than they would be in supervised work.

### Production-quality path

Production work requires explicit evidence, diff review, rollback planning, and refusal to treat summaries as approval.

### Prototype versus production

Prototype shortcuts can be rational when they are isolated and disposable. Production shortcuts need documented guardrails or rejection.

### Maintenance phase

Maintenance work should reduce repeated shortcut risk by encoding durable commands, review criteria, and do-not rules after the shortcut recurs.

## Stable Core

- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls than prototypes

## Volatile Surface

- non-interactive flags
- worktree behavior
- cloud task controls
- usage accounting
- automation UI

## Obsolescence Watch

This card should be revised if:

- long-running agents can guarantee bounded scope, safe permissions, and complete evidence without human review

## Evidence and Sources

- `openai.codex.noninteractive` — Official OpenAI Codex non-interactive guidance for codex exec, sandbox defaults, automation, and structured outputs.
- `openai.codex.app_worktrees` — Official OpenAI Codex worktrees guidance for isolated background work and handoff to local review.
- `openai.codex.use_cases.follow_goals` — Official OpenAI Codex use case for long-running goal work, validation, and stopping conditions.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, done-when criteria, testing, review, and permission posture.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.cloud`
- `vcb.workflow.ci_noninteractive`
- `vcb.constraints.attention_budget`
- `vcb.constraints.scope_budget`
- `vcb.constraints.usage_burn`
- `vcb.failure.context_pollution`

<!-- VCB:STOP_RETRIEVAL reason="unattended_long_runs_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.unattended_long_runs -->
