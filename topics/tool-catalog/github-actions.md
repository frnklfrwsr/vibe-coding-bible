<!-- VCB:BEGIN_TOPIC id=tool.github_actions version=0.1.0 -->
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
id: tool.github_actions
title: GitHub Actions
name: GitHub Actions
type: tool_card
category: repo_ci
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: high
pricing_snapshot_required: false
setup_effort: 'medium: workflow files, triggers, permissions, secrets, runners, and
  required checks must be designed deliberately'
maintenance_effort: 'medium-high: action versions, runners, secrets, permissions,
  build environments, and triggers drift'
debugging_effort: 'high: failures can be environment, cache, dependency, secret, token,
  runner, network, or test flake issues'
lock_in_risk: 'moderate-high: workflow syntax, marketplace actions, environment rules,
  and repository settings are GitHub-specific'
hidden_cost_risk: 'high: reruns, flakes, broad matrices, artifact retention, and failed
  automation can create hidden time and billing costs'
codex_integration_value: high as the evidence layer for Codex patches, non-interactive
  reports, and review gates
best_for:
- continuous integration
- pull-request checks
- repeatable build/test/lint evidence
- report-only automation
- release or deployment gates with human review
not_for:
- silent production mutation with broad credentials
- security approval without threat review
- untested deployment scripts
- using green CI as a complete product-quality claim
integrates_with_codex:
- codex exec
- Codex GitHub Review
- Codex Cloud PRs
- Codex Security
- GitHub repositories
hidden_costs:
- runner minutes and storage
- workflow maintenance
- flaky check triage
- secret and token management
- third-party action review
applies_to:
- GitHub Actions
- repository/CI/dependency/quality-assurance workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.overbroad_ci_permissions
- vcb.shortcut.long_lived_ci_secrets
- vcb.shortcut.automation_mutation_without_review
- vcb.shortcut.skipping_tests
durable_principles:
- CI is configured evidence, not universal correctness.
- Workflow permissions and secrets should be as narrow and short-lived as the task
  allows.
- Automation should report first and mutate only under explicit review gates.
likely_to_change:
- workflow syntax, runner images, marketplace action versions, billing, token defaults,
  permission defaults, UI labels, and hosted-runner behavior
obsolete_when:
- the project stops using GitHub-hosted workflow automation or GitHub Actions stops
  being the official CI/workflow layer for GitHub repositories.
related_topics:
- vcb.concepts.ci
- vcb.workflow.ci_triage
- vcb.workflow.ci_noninteractive
- vcb.failure.ci_false_confidence
- tool.codex_exec
- tool.github
- tool.openssf_scorecard
---

# GitHub Actions

> Summary:
> GitHub Actions is the workflow automation and CI layer for running checks, builds, tests, reports, deployment gates, and repository automation from versioned workflow definitions.

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

<!-- VCB:BEGIN_SECTION id=tool.github_actions.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

GitHub Actions runs repository workflows. In practice, vibe coders use it to turn tests, builds, linting, reports, preview checks, release tasks, and recurring validation into visible evidence attached to commits and pull requests.

### Why it matters

Codex can propose a patch, but CI says whether the configured checks passed in a clean environment. That evidence is narrow, but it is far better than trusting a local summary or a model claim.

### What good looks like

A good Actions workflow is least-privilege, repeatable, scoped to clear triggers, and produces logs or artifacts that a human can inspect before merge or deployment.

### What bad looks like

A bad workflow runs broad permissions, long-lived secrets, unpinned third-party actions, or automatic mutation without a review owner, then treats green status as proof that the product is safe.

### Minimal example

For a dependency PR, run install, unit tests, relevant browser tests, dependency review, and package audit; require a human to inspect the diff and logs before merge.

### Best-fit cases

- continuous integration
- pull-request checks
- repeatable build/test/lint evidence
- report-only automation
- release or deployment gates with human review

### Not-fit cases

- silent production mutation with broad credentials
- security approval without threat review
- untested deployment scripts
- using green CI as a complete product-quality claim

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: workflow files, triggers, permissions, secrets, runners, and required checks must be designed deliberately |
| Maintenance effort | medium-high: action versions, runners, secrets, permissions, build environments, and triggers drift |
| Debugging effort | high: failures can be environment, cache, dependency, secret, token, runner, network, or test flake issues |
| Lock-in risk | moderate-high: workflow syntax, marketplace actions, environment rules, and repository settings are GitHub-specific |
| Hidden cost risk | high: reruns, flakes, broad matrices, artifact retention, and failed automation can create hidden time and billing costs |

### Checklist

- define what evidence this tool is supposed to produce
- keep tool output tied to a branch, PR, log, artifact, or report
- separate automated signal from human approval
- keep pricing, quotas, defaults, and UI mechanics out of stable decisions
- re-check official vendor/project docs before encoding setup mechanics

<!-- VCB:END_SECTION id=tool.github_actions.human -->

<!-- VCB:BEGIN_SECTION id=tool.github_actions.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.github_actions` as CI workflows, tests, builds, secrets, permissions, and repeatable repository automation. The core lesson is not “use the tool”; it is “use the tool to create reviewable evidence with bounded blast radius.”

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
Use GitHub Actions for this task only if it produces reviewable evidence. Goal: [goal]. Current repo state: [branch/PR/logs/files]. Risk: [secrets/production/users/money]. Required evidence: [artifact/check/report]. Recommend the smallest safe use of the tool, the review step, and the rollback plan.
```

### Red flags

- tool output is treated as approval
- setup mechanics are copied from memory instead of official docs
- mutation happens before a report or review owner exists
- broad permissions are granted because the run is “just CI” or “just maintenance”
- exact prices, limits, quotas, or defaults are frozen in stable prose

### Intervention rule

When the human asks for current product behavior, exact pricing, limits, quotas, UI labels, command flags, permission defaults, or setup mechanics, route to official vendor/project sources or a dated volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.github_actions.ai_coach -->

## Shortcut Reality

### The ideal practice

Use GitHub Actions as one bounded part of the control loop: define intent, run the tool, collect evidence, review artifacts, then decide.

### What users often do instead

Users often treat the tool as a shortcut around review: a passed check, opened PR, audit output, generated browser test, or supply-chain score becomes “good enough” without inspecting the underlying evidence.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only reports, low-risk maintenance, or local experiments where rollback is trivial and no secrets, production state, or real users are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate dependencies, workflows, repository permissions, browser state, release gates, or production-sensitive code without a clear review owner and rollback path.

### Relevant shortcut cards

- `vcb.shortcut.overbroad_ci_permissions`
- `vcb.shortcut.long_lived_ci_secrets`
- `vcb.shortcut.automation_mutation_without_review`
- `vcb.shortcut.skipping_tests`

### Minimum guardrails

- one bounded tool purpose per run/change
- least privilege for repository, CI, package, and browser surfaces
- artifact or diff review before acceptance
- explicit rollback or revert path
- source check for current mechanics before updating durable docs
- Start new workflows as report-only where possible; add mutation, deployment, or token privileges only after logs and review ownership are proven.

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

- runner minutes and storage
- workflow maintenance
- flaky check triage
- secret and token management
- third-party action review

## Stable Core

- CI is configured evidence, not universal correctness.
- Workflow permissions and secrets should be as narrow and short-lived as the task allows.
- Automation should report first and mutate only under explicit review gates.

## Volatile Surface

- workflow syntax, runner images, marketplace action versions, billing, token defaults, permission defaults, UI labels, and hosted-runner behavior

Exact prices, plan packaging, quota limits, policy defaults, permission defaults, current UI labels, command flags, vulnerability/scoring details, and setup mechanics must be checked against official vendor/project sources or dated snapshots before use.

## Obsolescence Watch

This card becomes obsolete when: the project stops using GitHub-hosted workflow automation or GitHub Actions stops being the official CI/workflow layer for GitHub repositories.

Review official vendor/project docs before relying on current mechanics.

## Evidence and Sources

- `github.docs.actions_overview` — official/synthesis source anchor for this tool card.
- `github.docs.actions_workflow_syntax` — official/synthesis source anchor for this tool card.
- `github.docs.actions_ci` — official/synthesis source anchor for this tool card.
- `github.docs.actions_secure_use` — official/synthesis source anchor for this tool card.
- `github.docs.github_token` — official/synthesis source anchor for this tool card.
- `github.docs.actions_secrets` — official/synthesis source anchor for this tool card.
- `github.docs.actions_billing` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.concepts.ci`
- `vcb.workflow.ci_triage`
- `vcb.workflow.ci_noninteractive`
- `vcb.failure.ci_false_confidence`
- `tool.codex_exec`
- `tool.github`
- `tool.openssf_scorecard`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.github_actions -->
