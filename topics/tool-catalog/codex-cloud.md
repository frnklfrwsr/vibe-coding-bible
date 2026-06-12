<!-- VCB:BEGIN_TOPIC id=tool.codex_cloud version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex tool documentation plus VCB maintainer synthesis
  for setup, risk, budget, and coaching guidance
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
id: tool.codex_cloud
title: Codex Cloud
name: Codex Cloud
type: tool_card
category: codex_cloud_delegation
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
setup_effort: 'medium to high: repo connection, cloud environment, dependencies, setup
  scripts, secrets policy, and review path'
maintenance_effort: 'high: cloud environment behavior, access controls, internet settings,
  PR flow, and usage economics are volatile'
debugging_effort: 'high: failures can be repo connection, branch, setup script, missing
  dependency, internet, secret, or task-context issues'
lock_in_risk: 'moderate to high: cloud workflows depend on Codex/GitHub integration
  and OpenAI environment mechanics'
hidden_cost_risk: 'high: parallel cloud work can multiply usage, review time, and
  merge conflict recovery'
codex_integration_value: high for isolated background work that returns reviewable
  code artifacts
best_for:
- bounded background tasks
- parallel independent branches
- repo exploration that can report evidence
- reviewable PR/diff proposals
not_for:
- local-only uncommitted state
- production credential-heavy work
- unbounded refactors
- tasks no one will review
integrates_with_codex:
- GitHub repositories
- cloud environments
- pull requests
- Codex App/IDE/CLI handoff
- environment variables and secrets
hidden_costs:
- environment setup drift
- parallel integration conflicts
- review backlog
- secrets/network exposure
- cloud task usage burn
applies_to:
- Codex Web
- Codex Cloud
- cloud environments
- background tasks
- parallel tasks
- GitHub PR flows
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.unattended_cloud_delegation
- vcb.shortcut.cloud_task_without_context
- vcb.shortcut.parallel_cloud_sprawl
- vcb.shortcut.reviewing_cloud_summary_only
durable_principles:
- Cloud work needs explicit task packets and review packets.
- Parallelism requires disjoint scopes and an integration owner.
- Secrets, internet access, and production paths should be minimized and reviewed
  before launch.
likely_to_change:
- cloud environment setup, internet-access controls, task lifecycle, PR mechanics,
  source-control integration, plan packaging, and usage economics
obsolete_when:
- OpenAI retires Codex Cloud/Web or changes it so it is no longer a background cloud
  execution surface for repository tasks.
related_topics:
- vcb.codex.cloud
- vcb.chapter.cloud_delegation_parallel_work
- vcb.shortcut.unattended_cloud_delegation
- vcb.shortcut.cloud_task_without_context
- vcb.shortcut.parallel_cloud_sprawl
- vcb.constraints.review_budget
---

# Codex Cloud

> Summary:
> Codex Cloud/Web is the first-party background delegation surface for running Codex tasks in a cloud environment, including parallel cloud work and PR-style review paths.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_cloud.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex Cloud lets Codex work away from your local foreground session in a cloud environment. It is useful for tasks that can be isolated, reviewed later, and merged deliberately.

### Why it matters

Cloud is powerful because it saves attention and enables parallelism. It is dangerous when the task depends on local-only context, real secrets, broad internet access, or unreviewed mutation.

### What good looks like

Use cloud for one bounded branch task with setup, environment, secret policy, internet policy, and final review packet.

### What bad looks like

Send a vague production refactor to cloud, give broad secrets/network access, and merge from the summary.

### Minimal example

Delegate a docs update, bug investigation, or small feature branch with a do-not-touch list, expected checks, and PR/diff review before merge.

### Best-fit cases

- bounded background tasks
- parallel independent branches
- repo exploration that can report evidence
- reviewable PR/diff proposals

### Not-fit cases

- local-only uncommitted state
- production credential-heavy work
- unbounded refactors
- tasks no one will review

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium to high: repo connection, cloud environment, dependencies, setup scripts, secrets policy, and review path |
| Maintenance effort | high: cloud environment behavior, access controls, internet settings, PR flow, and usage economics are volatile |
| Debugging effort | high: failures can be repo connection, branch, setup script, missing dependency, internet, secret, or task-context issues |
| Lock-in risk | moderate to high: cloud workflows depend on Codex/GitHub integration and OpenAI environment mechanics |
| Hidden cost risk | high: parallel cloud work can multiply usage, review time, and merge conflict recovery |

### Checklist

- choose the smallest Codex surface that fits the task
- confirm permissions before mutation
- require a diff, report, structured output, or check evidence
- keep exact pricing, limits, model availability, and UI mechanics out of stable decisions
- review official OpenAI docs before freezing current product behavior

<!-- VCB:END_SECTION id=tool.codex_cloud.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_cloud.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach cloud as isolated review-later execution. Background work shifts when attention is spent; it does not remove the need for context and review.

### Diagnostic questions

- Can this task succeed without local uncommitted state?
- Is the cloud environment configured for dependencies and tools?
- Does it need secrets or internet, and can those be avoided or scoped?
- How will the returned diff or PR be reviewed?

### Coaching tactics

- require a delegation packet before launch
- use branch/worktree isolation
- prefer fake/staging secrets and minimal internet access
- require changed files, commands, evidence, gaps, and risks

### Prompt pattern

```text
Run this as one Codex Cloud task. Goal: [goal]. Context: [files/issues/logs]. Constraints: no production secrets, no deploys, no broad refactor, no new dependencies unless justified. Done when: return diff/PR, checks run, evidence, gaps, risks, and rollback notes.
```

### Red flags

- cloud task launched from vague request
- uncommitted local context not provided
- parallel cloud tasks share files
- summary accepted without diff/PR review
- real secrets placed in cloud environment unnecessarily

### Intervention rule

When the human asks for a current product detail, exact price, exact limit, model-routing claim, UI label, command flag, or plan-packaging fact, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_cloud.ai_coach -->

## Shortcut Reality

### The ideal practice

Use this tool only after the task, context, permissions, evidence, and review path are clear.

### What users often do instead

Users often pick the most convenient surface, then retrofit the safety controls after the tool has already produced output.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only inspection, docs work, small branches, or reports where rollback is trivial and no secrets or production state are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate broad code, touch secrets, make production changes, create noisy automation, hide environment assumptions, or return a polished summary without verifiable evidence.

### Relevant shortcut cards

- `vcb.shortcut.unattended_cloud_delegation`
- `vcb.shortcut.cloud_task_without_context`
- `vcb.shortcut.parallel_cloud_sprawl`
- `vcb.shortcut.reviewing_cloud_summary_only`

### Minimum guardrails

- one bounded task per run/thread/job
- explicit permissions and forbidden zones
- Git checkpoint or isolated branch/worktree for mutation
- evidence packet before acceptance
- human review before merge, deploy, credential use, or production action

### Recovery plan

Stop the tool, preserve logs/transcripts/output, inspect the diff or generated artifact, revert or isolate unsafe changes, rotate exposed secrets if needed, and restart with a smaller task packet.

## Budget and Constraint Notes

### Cheapest reliable path

Use the narrowest surface, smallest context packet, and cheapest reviewable workflow that can produce the needed evidence. Avoid retry loops caused by vague prompts.

### Fastest high-usage path

Use parallel or automated surfaces only when work is independent, review capacity exists, and integration cost is budgeted.

### Low-attention path

Low-attention use requires isolation, stop conditions, and a final review packet. It does not justify broad mutation or production access.

### Production-quality path

Production use requires explicit scope, least privilege, checks, security review where relevant, and human acceptance based on artifacts rather than summaries.

### Hidden costs to watch

- environment setup drift
- parallel integration conflicts
- review backlog
- secrets/network exposure
- cloud task usage burn

## Stable Core

- Cloud work needs explicit task packets and review packets.
- Parallelism requires disjoint scopes and an integration owner.
- Secrets, internet access, and production paths should be minimized and reviewed before launch.

## Volatile Surface

- cloud environment setup, internet-access controls, task lifecycle, PR mechanics, source-control integration, plan packaging, and usage economics

Exact prices, plan packaging, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires Codex Cloud/Web or changes it so it is no longer a background cloud execution surface for repository tasks.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.cloud` — official/synthesis source anchor for this tool card.
- `openai.codex.cloud_environments` — official/synthesis source anchor for this tool card.
- `openai.codex.cloud_internet_access` — official/synthesis source anchor for this tool card.
- `openai.codex.best_practices` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.codex.cloud`
- `vcb.chapter.cloud_delegation_parallel_work`
- `vcb.shortcut.unattended_cloud_delegation`
- `vcb.shortcut.cloud_task_without_context`
- `vcb.shortcut.parallel_cloud_sprawl`
- `vcb.constraints.review_budget`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_cloud -->
