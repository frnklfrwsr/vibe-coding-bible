<!-- VCB:BEGIN_TOPIC id=tool.github_dependabot version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-11'
last_reviewed: '2026-06-11'
audiences:
- human
- ai_coach
source_status:
  official_openai: false
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official vendor/project documentation plus VCB maintainer synthesis
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
id: tool.github_dependabot
title: GitHub Dependabot
name: GitHub Dependabot
type: tool_card
category: supply_chain
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: high
pricing_snapshot_required: false
setup_effort: 'medium: dependency graph, alerts, update configuration, review cadence,
  tests, and PR policies need setup'
maintenance_effort: 'medium-high: ecosystems, advisory signals, update grouping, ignored
  versions, and CI reliability require ongoing care'
debugging_effort: 'medium-high: failures can be package-manager behavior, lockfile
  churn, transitive dependency conflicts, or breaking changes'
lock_in_risk: 'medium: alerts, PR metadata, update configuration, and automation behavior
  are GitHub-specific'
hidden_cost_risk: 'high: many small PRs can create CI spend, reviewer fatigue, and
  accidental auto-merge risk'
codex_integration_value: high as a source of dependency-maintenance tasks that Codex
  can summarize, test, and review under human control
best_for:
- dependency security update PRs
- dependency version update queue
- supply-chain maintenance visibility
- lockfile review prompts
- recurring dependency hygiene
not_for:
- automatic trust in new dependency versions
- unreviewed lockfile churn
- large framework migrations without manual planning
- supply-chain security guarantees
integrates_with_codex:
- Codex GitHub Review
- Codex Security
- GitHub Actions
- npm workflows
- dependency-review workflows
hidden_costs:
- review queue volume
- CI cost from many update PRs
- breakage from transitive changes
- release-note research
- rollback after incompatible updates
applies_to:
- GitHub Dependabot
- repository/CI/dependency/quality-assurance workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.adding_dependencies_fast
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_tests
durable_principles:
- Dependency-update PRs are prompts for review, not automatic approvals.
- Security alerts require exploitability and affected-path review, not panic merges.
- Lockfile and transitive changes are part of the diff.
likely_to_change:
- Dependabot configuration options, UI labels, ecosystem support, advisory metadata,
  grouping mechanics, PR behavior, and update defaults
obsolete_when:
- GitHub replaces Dependabot with a different official dependency-maintenance system
  or the project moves dependency automation to another source of truth.
related_topics:
- vcb.workflow.dependency_update_review
- vcb.workflow.dependency_decisions
- vcb.failure.dependency_bloat
- tool.github
- tool.github_actions
- tool.npm
- tool.openssf_scorecard
---

# GitHub Dependabot

> Summary:
> GitHub Dependabot is the dependency-maintenance signal and PR generator for vulnerable or outdated dependencies, best used as a review queue rather than an auto-merge authority.

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

<!-- VCB:BEGIN_SECTION id=tool.github_dependabot.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Dependabot watches dependency manifests and security signals, then opens alerts or pull requests for dependency updates. It is a maintenance assistant, not a guarantee that the update is safe.

### Why it matters

Vibe-coded projects accumulate packages quickly. Dependabot keeps dependency work visible, but every update still needs lockfile review, release-note review, compatibility checks, and targeted tests.

### What good looks like

A good Dependabot workflow groups or schedules updates deliberately, runs relevant tests, reviews direct and transitive changes, and treats security updates as urgent evidence to investigate.

### What bad looks like

A bad workflow auto-merges update PRs, ignores lockfile churn, skips changelog/release-note review, or treats dependency freshness as proof of supply-chain safety.

### Minimal example

For a vulnerable package update, inspect the advisory, changed version, lockfile diff, release notes, affected code paths, and CI results before merge.

### Best-fit cases

- dependency security update PRs
- dependency version update queue
- supply-chain maintenance visibility
- lockfile review prompts
- recurring dependency hygiene

### Not-fit cases

- automatic trust in new dependency versions
- unreviewed lockfile churn
- large framework migrations without manual planning
- supply-chain security guarantees

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: dependency graph, alerts, update configuration, review cadence, tests, and PR policies need setup |
| Maintenance effort | medium-high: ecosystems, advisory signals, update grouping, ignored versions, and CI reliability require ongoing care |
| Debugging effort | medium-high: failures can be package-manager behavior, lockfile churn, transitive dependency conflicts, or breaking changes |
| Lock-in risk | medium: alerts, PR metadata, update configuration, and automation behavior are GitHub-specific |
| Hidden cost risk | high: many small PRs can create CI spend, reviewer fatigue, and accidental auto-merge risk |

### Checklist

- define what evidence this tool is supposed to produce
- keep tool output tied to a branch, PR, log, artifact, or report
- separate automated signal from human approval
- keep pricing, quotas, defaults, and UI mechanics out of stable decisions
- re-check official vendor/project docs before encoding setup mechanics

<!-- VCB:END_SECTION id=tool.github_dependabot.human -->

<!-- VCB:BEGIN_SECTION id=tool.github_dependabot.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.github_dependabot` as dependency alerts, dependency update PRs, advisory triage, and lockfile review workflows. The core lesson is not “use the tool”; it is “use the tool to create reviewable evidence with bounded blast radius.”

### Diagnostic questions

- What decision is the human trying to make with this tool?
- What artifact will prove the result: diff, check, log, report, screenshot, advisory, lockfile, or pull request?
- Does the tool have permission to mutate code, dependencies, repository settings, secrets, or production state?
- What is the rollback path if the tool output is wrong?

### Coaching tactics

- route tool-choice questions to the smallest active tool card before chapter fallbacks
- ask for exact evidence and acceptance criteria before mutation
- separate signal, recommendation, and approval
- force source checks for current setup mechanics, permissions, pricing, and defaults
- preserve logs or artifacts before asking Codex to repair failures

### Prompt pattern

```text
Use GitHub Dependabot for this task only if it produces reviewable evidence. Goal: [goal]. Current repo state: [branch/PR/logs/files]. Risk: [secrets/production/users/money]. Required evidence: [artifact/check/report]. Recommend the smallest safe use of the tool, the review step, and the rollback plan.
```

### Red flags

- tool output is treated as approval
- setup mechanics are copied from memory instead of official docs
- mutation happens before a report or review owner exists
- broad permissions are granted because the run is “just CI” or “just maintenance”
- exact prices, limits, quotas, or defaults are frozen in stable prose

### Intervention rule

When the human asks for current product behavior, exact pricing, limits, quotas, UI labels, command flags, permission defaults, or setup mechanics, route to official vendor/project sources or a dated volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.github_dependabot.ai_coach -->

## Shortcut Reality

### The ideal practice

Use GitHub Dependabot as one bounded part of the control loop: define intent, run the tool, collect evidence, review artifacts, then decide.

### What users often do instead

Users often treat the tool as a shortcut around review: a passed check, opened PR, audit output, generated browser test, or supply-chain score becomes “good enough” without inspecting the underlying evidence.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only reports, low-risk maintenance, or local experiments where rollback is trivial and no secrets, production state, or real users are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate dependencies, workflows, repository permissions, browser state, release gates, or production-sensitive code without a clear review owner and rollback path.

### Relevant shortcut cards

- `vcb.shortcut.adding_dependencies_fast`
- `vcb.shortcut.accepting_looks_done`
- `vcb.shortcut.skipping_tests`

### Minimum guardrails

- one bounded tool purpose per run/change
- least privilege for repository, CI, package, and browser surfaces
- artifact or diff review before acceptance
- explicit rollback or revert path
- source check for current mechanics before updating durable docs
- Require update PRs to carry a compatibility hypothesis, affected-path review, lockfile inspection, and targeted checks before merge.

### Recovery plan

Stop automation or merging, preserve the log/report/diff, inspect changed files and permissions, revert unsafe changes, rotate exposed secrets if any, rerun the smallest meaningful check, and reopen the work with a narrower task packet.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest tool capability that creates the needed evidence. Avoid broad matrices, broad dependency updates, or wide scans until the value is clear.

### Fastest high-usage path

Use parallel or automated runs only when the work is independent, review capacity exists, and the project can afford triage and reruns.

### Low-attention path

Low-attention use should be report-first. Mutation, merge, deploy, package publication, repository-setting changes, or credential use require explicit human review.

### Production-quality path

Production use requires branch/PR discipline, least privilege, repeatable checks, failure artifacts, human review, and a documented rollback path.

### Hidden costs to watch

- review queue volume
- CI cost from many update PRs
- breakage from transitive changes
- release-note research
- rollback after incompatible updates

## Stable Core

- Dependency-update PRs are prompts for review, not automatic approvals.
- Security alerts require exploitability and affected-path review, not panic merges.
- Lockfile and transitive changes are part of the diff.

## Volatile Surface

- Dependabot configuration options, UI labels, ecosystem support, advisory metadata, grouping mechanics, PR behavior, and update defaults

Exact prices, plan packaging, quota limits, policy defaults, permission defaults, current UI labels, command flags, vulnerability/scoring details, and setup mechanics must be checked against official vendor/project sources or dated snapshots before use.

## Obsolescence Watch

This card becomes obsolete when: GitHub replaces Dependabot with a different official dependency-maintenance system or the project moves dependency automation to another source of truth.

Review official vendor/project docs before relying on current mechanics.

## Evidence and Sources

- `github.docs.dependabot_quickstart` — official/synthesis source anchor for this tool card.
- `github.docs.dependabot_security_updates` — official/synthesis source anchor for this tool card.
- `github.docs.dependabot_version_updates` — official/synthesis source anchor for this tool card.
- `github.docs.dependabot_alerts` — official/synthesis source anchor for this tool card.
- `github.docs.dependency_review` — official/synthesis source anchor for this tool card.
- `github.docs.dependency_graph` — official/synthesis source anchor for this tool card.
- `github.docs.dependency_maintenance_best_practices` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.workflow.dependency_update_review`
- `vcb.workflow.dependency_decisions`
- `vcb.failure.dependency_bloat`
- `tool.github`
- `tool.github_actions`
- `tool.npm`
- `tool.openssf_scorecard`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.github_dependabot -->
