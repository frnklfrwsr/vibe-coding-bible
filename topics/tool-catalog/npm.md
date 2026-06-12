<!-- VCB:BEGIN_TOPIC id=tool.npm version=0.1.0 -->
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
id: tool.npm
title: npm
name: npm
type: tool_card
category: package_manager
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: high
pricing_snapshot_required: false
setup_effort: 'low-medium: manifests and scripts are simple initially but need conventions
  for CI, audit, lockfiles, and dependency review'
maintenance_effort: 'medium-high: packages, lockfiles, script conventions, advisories,
  and ecosystem tooling change frequently'
debugging_effort: 'medium-high: failures can be version ranges, lockfile drift, lifecycle
  scripts, platform assumptions, package registry issues, or transitive dependency
  conflicts'
lock_in_risk: 'medium: script conventions and package-manager behavior can become
  project-specific and hard to migrate'
hidden_cost_risk: 'high: dependency bloat, supply-chain exposure, install flakiness,
  and audit noise can exceed initial implementation savings'
codex_integration_value: high for JavaScript projects because Codex often needs package
  scripts, install behavior, and audit/dependency evidence
best_for:
- JavaScript dependency manifests
- package scripts
- lockfile-based install reproducibility
- dependency audit reports
- Node project setup and CI commands
not_for:
- blind package installation
- security approval from audit output alone
- large framework decisions without alternatives
- opaque script chains no one can explain
integrates_with_codex:
- Codex CLI
- codex exec
- GitHub Actions
- Dependabot
- Playwright
- dependency review workflows
hidden_costs:
- transitive dependency growth
- lockfile conflicts
- install time
- audit triage
- script maintenance
- supply-chain review
applies_to:
- npm
- repository/CI/dependency/quality-assurance workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.adding_dependencies_fast
- vcb.shortcut.skipping_setup
- vcb.shortcut.skipping_tests
durable_principles:
- Every dependency is future maintenance and supply-chain surface.
- Package scripts should be understandable, reviewable, and CI-compatible.
- Audit output is useful evidence, not a complete security decision.
likely_to_change:
- CLI commands, script lifecycle details, lockfile formats, audit output, registry
  behavior, package metadata, and package-manager defaults
obsolete_when:
- the project leaves the JavaScript/npm ecosystem or replaces npm as the package-manager
  source of truth.
related_topics:
- vcb.concepts.dependency
- vcb.workflow.dependency_decisions
- vcb.workflow.dependency_update_review
- vcb.failure.dependency_bloat
- tool.github_dependabot
- tool.github_actions
- tool.playwright
---

# npm

> Summary:
> npm is the JavaScript package-manager and registry workflow layer for package manifests, scripts, lockfiles, installs, audits, and dependency-maintenance evidence.

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

<!-- VCB:BEGIN_SECTION id=tool.npm.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

npm is the package-manager surface most JavaScript and Node projects use to define dependencies, scripts, lockfiles, and install/audit workflows. For vibe coders, it is where dependency decisions become executable and reviewable.

### Why it matters

AI agents often suggest packages or commands quickly. npm makes that decision concrete in package manifests and lockfiles, which means it also creates maintenance, security, install, and CI obligations.

### What good looks like

A good npm workflow keeps dependencies justified, scripts simple, lockfiles reviewed, audit output treated as evidence, and install/test behavior reproducible enough for CI and teammates.

### What bad looks like

A bad workflow installs packages because they sound useful, ignores lockfile changes, treats audit output as complete security review, or hides important checks behind unexplained scripts.

### Minimal example

Before adding a package, ask whether the standard library or existing dependency can solve it; if not, document why the package is worth its maintenance and supply-chain cost.

### Best-fit cases

- JavaScript dependency manifests
- package scripts
- lockfile-based install reproducibility
- dependency audit reports
- Node project setup and CI commands

### Not-fit cases

- blind package installation
- security approval from audit output alone
- large framework decisions without alternatives
- opaque script chains no one can explain

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | low-medium: manifests and scripts are simple initially but need conventions for CI, audit, lockfiles, and dependency review |
| Maintenance effort | medium-high: packages, lockfiles, script conventions, advisories, and ecosystem tooling change frequently |
| Debugging effort | medium-high: failures can be version ranges, lockfile drift, lifecycle scripts, platform assumptions, package registry issues, or transitive dependency conflicts |
| Lock-in risk | medium: script conventions and package-manager behavior can become project-specific and hard to migrate |
| Hidden cost risk | high: dependency bloat, supply-chain exposure, install flakiness, and audit noise can exceed initial implementation savings |

### Checklist

- define what evidence this tool is supposed to produce
- keep tool output tied to a branch, PR, log, artifact, or report
- separate automated signal from human approval
- keep pricing, quotas, defaults, and UI mechanics out of stable decisions
- re-check official vendor/project docs before encoding setup mechanics

<!-- VCB:END_SECTION id=tool.npm.human -->

<!-- VCB:BEGIN_SECTION id=tool.npm.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.npm` as JavaScript package manifests, scripts, lockfiles, dependency install, and audit workflows. The core lesson is not “use the tool”; it is “use the tool to create reviewable evidence with bounded blast radius.”

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
Use npm for this task only if it produces reviewable evidence. Goal: [goal]. Current repo state: [branch/PR/logs/files]. Risk: [secrets/production/users/money]. Required evidence: [artifact/check/report]. Recommend the smallest safe use of the tool, the review step, and the rollback plan.
```

### Red flags

- tool output is treated as approval
- setup mechanics are copied from memory instead of official docs
- mutation happens before a report or review owner exists
- broad permissions are granted because the run is “just CI” or “just maintenance”
- exact prices, limits, quotas, or defaults are frozen in stable prose

### Intervention rule

When the human asks for current product behavior, exact pricing, limits, quotas, UI labels, command flags, permission defaults, or setup mechanics, route to official vendor/project sources or a dated volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.npm.ai_coach -->

## Shortcut Reality

### The ideal practice

Use npm as one bounded part of the control loop: define intent, run the tool, collect evidence, review artifacts, then decide.

### What users often do instead

Users often treat the tool as a shortcut around review: a passed check, opened PR, audit output, generated browser test, or supply-chain score becomes “good enough” without inspecting the underlying evidence.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only reports, low-risk maintenance, or local experiments where rollback is trivial and no secrets, production state, or real users are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate dependencies, workflows, repository permissions, browser state, release gates, or production-sensitive code without a clear review owner and rollback path.

### Relevant shortcut cards

- `vcb.shortcut.adding_dependencies_fast`
- `vcb.shortcut.skipping_setup`
- `vcb.shortcut.skipping_tests`

### Minimum guardrails

- one bounded tool purpose per run/change
- least privilege for repository, CI, package, and browser surfaces
- artifact or diff review before acceptance
- explicit rollback or revert path
- source check for current mechanics before updating durable docs
- Require a no-new-dependency attempt, a maintenance-cost note, lockfile review, and the smallest relevant test before accepting a package change.

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

- transitive dependency growth
- lockfile conflicts
- install time
- audit triage
- script maintenance
- supply-chain review

## Stable Core

- Every dependency is future maintenance and supply-chain surface.
- Package scripts should be understandable, reviewable, and CI-compatible.
- Audit output is useful evidence, not a complete security decision.

## Volatile Surface

- CLI commands, script lifecycle details, lockfile formats, audit output, registry behavior, package metadata, and package-manager defaults

Exact prices, plan packaging, quota limits, policy defaults, permission defaults, current UI labels, command flags, vulnerability/scoring details, and setup mechanics must be checked against official vendor/project sources or dated snapshots before use.

## Obsolescence Watch

This card becomes obsolete when: the project leaves the JavaScript/npm ecosystem or replaces npm as the package-manager source of truth.

Review official vendor/project docs before relying on current mechanics.

## Evidence and Sources

- `npm.docs.package_json` — official/synthesis source anchor for this tool card.
- `npm.docs.package_dependencies` — official/synthesis source anchor for this tool card.
- `npm.docs.scripts` — official/synthesis source anchor for this tool card.
- `npm.docs.package_lock` — official/synthesis source anchor for this tool card.
- `npm.docs.audit` — official/synthesis source anchor for this tool card.
- `npm.docs.security_audit` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.concepts.dependency`
- `vcb.workflow.dependency_decisions`
- `vcb.workflow.dependency_update_review`
- `vcb.failure.dependency_bloat`
- `tool.github_dependabot`
- `tool.github_actions`
- `tool.playwright`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.npm -->
