<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.conflicting_parallel_agents version=0.1.0 -->
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
id: vcb.shortcut.conflicting_parallel_agents
title: Conflicting Parallel Agents
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
- one mutating owner per boundary
- read-only parallel analysis
- isolated branches for alternatives
- single integrator
- post-integration checks
shortcut_profiles:
- vcb.shortcut.conflicting_parallel_agents
durable_principles:
- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
likely_to_change:
- worktree and branch controls
- subagent write permissions
- cloud task conflict warnings
- integrated review UI
obsolete_when:
- agent platforms enforce file ownership, semantic conflict detection, and safe integration
  workflows automatically
related_topics:
- vcb.codex.subagents
- vcb.codex.cloud
- vcb.shortcut.parallel_agents_edit_same_files
- vcb.shortcut.subagent_swarm
- vcb.shortcut.parallel_cloud_sprawl
- vcb.workflow.reviewing_diffs
---

# Conflicting Parallel Agents

> Summary:
> Conflicting Parallel Agents means letting multiple agents, automations, or cloud tasks mutate overlapping files or behaviors without file ownership and integration rules.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.conflicting_parallel_agents.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “They can all work at the same time; I will sort it out.” That only works when each agent owns a separate boundary. If agents edit the same files or behavior, conflict resolution becomes a coding task and a reasoning task.

### Why it matters

Git can show text conflicts, but it cannot tell you which agent’s assumption is correct. Parallel write conflicts often hide semantic conflicts even when the merge is clean.

### What good looks like

Good: “Agent A writes tests, Agent B analyzes logs, Agent C edits docs. Only one agent mutates the implementation.”

### What bad looks like

Bad: “One agent refactors the auth module while another fixes checkout in the same files.”

### Minimal example

Two agents can independently inspect a failure. Only one should edit the failing module unless their branches are deliberately isolated and an integrator reviews both diffs.

### Checklist

- one owner per file or behavior
- analysis can be parallel; mutation is serialized
- separate branches/worktrees for competing fixes
- one integrator for merged output
- rerun checks after integration

<!-- VCB:END_SECTION id=vcb.shortcut.conflicting_parallel_agents.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.conflicting_parallel_agents.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach that parallel thinking is cheap; parallel mutation requires ownership boundaries.

### Diagnostic questions

- Which agents can write files?
- Do their file scopes overlap?
- Who integrates competing diffs?
- Are branches isolated?
- What checks run after integration?

### Coaching tactics

- make extra agents read-only reviewers
- assign file ownership before launch
- serialize implementation after parallel analysis
- require conflict report format
- reject summary-only integration

### Red flags

- several agents “fix” the same issue
- same files appear in multiple task packets
- no integrator named
- clean merge is treated as correctness
- tests run before integration but not after

### Prompt pattern

```text
Parallelize analysis, not overlapping writes. Assign each agent either read-only diagnosis or a disjoint file scope. If two proposed fixes touch the same file or behavior, stop and produce a comparison report for one integrator instead of merging both.
```

<!-- VCB:END_SECTION id=vcb.shortcut.conflicting_parallel_agents.ai_coach -->

## Shortcut Reality

### Ideal practice

Use one mutating owner per file/behavior and one explicit integrator for competing outputs.

### What people often do instead

They let agents race on the same area and rely on Git, summaries, or intuition to reconcile conflicts.

### When the shortcut may be acceptable

Acceptable when all but one agent are read-only, or when competing implementations stay isolated until reviewed by an integrator.

### When it becomes a bad trade

Bad for auth, payments, migrations, state management, CI, shared abstractions, and broad refactors.

### Risk profile

- Probability: medium in parallel workflows; high when scopes overlap or tasks are phrased broadly.
- Impact: high for shared behavior and severe for production-sensitive code.
- Recoverability: medium with isolated branches; low after manual conflict resolution without evidence.

### Blast radius

The shortcut can turn concurrency into semantic drift, duplicated changes, broken invariants, and tests that no longer match the final integrated diff.

### Minimum guardrails

- one mutating owner per boundary
- read-only parallel analysis
- isolated branches for alternatives
- single integrator
- post-integration checks

### Recovery plan

1. Stop all overlapping write agents.
2. Generate a changed-file overlap table.
3. Pick one branch as the integration base.
4. Review competing hunks by evidence and acceptance criteria.
5. Rerun tests/checks after the final integrated diff.

## Budget and Constraint Notes

### Cheapest reliable path

Write the smallest task packet, isolation rule, and review packet requirement before launching the agent. This costs less than reconciling a broad or unsafe background result.

### Fastest high-usage path

Parallelism saves time only when integration cost is lower than wall-clock savings. Overlap usually reverses that equation.

### Low-attention path

Low-attention workflows should avoid overlapping mutating agents entirely; use report-only parallel analysis.

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

- worktree and branch controls
- subagent write permissions
- cloud task conflict warnings
- integrated review UI

## Obsolescence Watch

This card should be revised if:

- agent platforms enforce file ownership, semantic conflict detection, and safe integration workflows automatically

## Evidence and Sources

- `openai.codex.subagents` — Official OpenAI Codex subagent guidance for bounded agent roles and parallelism cautions.
- `openai.codex.app_worktrees` — Official OpenAI Codex app worktree guidance for isolated parallel local task execution.
- `openai.codex.cloud` — Official OpenAI Codex cloud guidance for delegated background and parallel cloud task shape.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for context, constraints, done-when criteria, planning, validation, and review.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.subagents`
- `vcb.codex.cloud`
- `vcb.shortcut.parallel_agents_edit_same_files`
- `vcb.shortcut.subagent_swarm`
- `vcb.shortcut.parallel_cloud_sprawl`
- `vcb.workflow.reviewing_diffs`

<!-- VCB:STOP_RETRIEVAL reason="conflicting_parallel_agents_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.conflicting_parallel_agents -->
