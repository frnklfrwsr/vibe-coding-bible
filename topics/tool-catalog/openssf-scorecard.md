<!-- VCB:BEGIN_TOPIC id=tool.openssf_scorecard version=0.1.0 -->
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
id: tool.openssf_scorecard
title: OpenSSF Scorecard
name: OpenSSF Scorecard
type: tool_card
category: supply_chain_quality
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: high
pricing_snapshot_required: false
setup_effort: 'medium: running checks is simple, but interpreting results and turning
  them into policy needs team context'
maintenance_effort: 'medium: check definitions, scoring, project support, and supply-chain
  standards evolve'
debugging_effort: 'medium: unexpected findings may involve repository configuration,
  project metadata, CI, dependency, review, or maintenance practices'
lock_in_risk: 'low-medium: Scorecard is open source, but policies built around its
  output can become organization-specific'
hidden_cost_risk: 'medium: hardening findings can create review and policy work that
  is easy to underestimate'
codex_integration_value: medium-high as a structured dependency/repository health
  signal that Codex can summarize but must not overrule
best_for:
- open-source dependency health review
- repository supply-chain posture
- hardening backlog generation
- dependency adoption review
- CI supply-chain quality signal
not_for:
- security certification
- exploitability proof
- complete vendor due diligence
- automatic dependency allow/deny decisions
- replacing manual threat review
integrates_with_codex:
- Codex Security
- GitHub Actions
- Dependabot
- dependency-review workflows
- GitHub repositories
hidden_costs:
- finding interpretation
- false-positive triage
- policy exceptions
- CI integration maintenance
- maintainer follow-up for upstream dependencies
applies_to:
- OpenSSF Scorecard
- repository/CI/dependency/quality-assurance workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.trusting_external_tool_output
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.adding_dependencies_fast
durable_principles:
- Supply-chain scores are triage signals, not safety certificates.
- Finding details and project context matter more than the headline score.
- Automated checks should feed a human hardening backlog.
likely_to_change:
- check definitions, scoring mechanics, action setup, supported platforms, output
  formats, and policy guidance
obsolete_when:
- OpenSSF Scorecard is retired or replaced by a different official supply-chain health
  framework used by the project.
related_topics:
- vcb.workflow.dependency_decisions
- vcb.workflow.dependency_update_review
- vcb.failure.dependency_bloat
- tool.github
- tool.github_actions
- tool.github_dependabot
- tool.codex_security
---

# OpenSSF Scorecard

> Summary:
> OpenSSF Scorecard is a supply-chain quality signal for repository security posture, best used to prioritize hardening work rather than to certify that a project or dependency is safe.

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

<!-- VCB:BEGIN_SECTION id=tool.openssf_scorecard.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

OpenSSF Scorecard runs automated checks against open source repositories and reports security-health signals. For vibe coders, it is a way to ask “what hardening gaps does this project expose?” before adopting or maintaining code.

### Why it matters

AI can make dependency and project choices sound simple. Scorecard adds structured supply-chain signals, but those signals still need human interpretation, context, and false-positive/false-negative review.

### What good looks like

A good Scorecard workflow treats results as a prioritized checklist: inspect risky checks, decide which findings matter for this project, and pair changes with CI, branch, dependency, and release controls.

### What bad looks like

A bad workflow treats a score as a binary pass/fail certification, ignores the check details, or blocks useful dependencies without considering context, alternatives, and compensating controls.

### Minimal example

Before adopting an unfamiliar dependency, review its repository health signals, recent maintenance, branch protection, dependency-update posture, and test/release practices alongside package popularity and API fit.

### Best-fit cases

- open-source dependency health review
- repository supply-chain posture
- hardening backlog generation
- dependency adoption review
- CI supply-chain quality signal

### Not-fit cases

- security certification
- exploitability proof
- complete vendor due diligence
- automatic dependency allow/deny decisions
- replacing manual threat review

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: running checks is simple, but interpreting results and turning them into policy needs team context |
| Maintenance effort | medium: check definitions, scoring, project support, and supply-chain standards evolve |
| Debugging effort | medium: unexpected findings may involve repository configuration, project metadata, CI, dependency, review, or maintenance practices |
| Lock-in risk | low-medium: Scorecard is open source, but policies built around its output can become organization-specific |
| Hidden cost risk | medium: hardening findings can create review and policy work that is easy to underestimate |

### Checklist

- define what evidence this tool is supposed to produce
- keep tool output tied to a branch, PR, log, artifact, or report
- separate automated signal from human approval
- keep pricing, quotas, defaults, and UI mechanics out of stable decisions
- re-check official vendor/project docs before encoding setup mechanics

<!-- VCB:END_SECTION id=tool.openssf_scorecard.human -->

<!-- VCB:BEGIN_SECTION id=tool.openssf_scorecard.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.openssf_scorecard` as supply-chain health signals, repository hardening checks, and dependency-adoption risk review. The core lesson is not “use the tool”; it is “use the tool to create reviewable evidence with bounded blast radius.”

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
Use OpenSSF Scorecard for this task only if it produces reviewable evidence. Goal: [goal]. Current repo state: [branch/PR/logs/files]. Risk: [secrets/production/users/money]. Required evidence: [artifact/check/report]. Recommend the smallest safe use of the tool, the review step, and the rollback plan.
```

### Red flags

- tool output is treated as approval
- setup mechanics are copied from memory instead of official docs
- mutation happens before a report or review owner exists
- broad permissions are granted because the run is “just CI” or “just maintenance”
- exact prices, limits, quotas, or defaults are frozen in stable prose

### Intervention rule

When the human asks for current product behavior, exact pricing, limits, quotas, UI labels, command flags, permission defaults, or setup mechanics, route to official vendor/project sources or a dated volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.openssf_scorecard.ai_coach -->

## Shortcut Reality

### The ideal practice

Use OpenSSF Scorecard as one bounded part of the control loop: define intent, run the tool, collect evidence, review artifacts, then decide.

### What users often do instead

Users often treat the tool as a shortcut around review: a passed check, opened PR, audit output, generated browser test, or supply-chain score becomes “good enough” without inspecting the underlying evidence.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only reports, low-risk maintenance, or local experiments where rollback is trivial and no secrets, production state, or real users are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate dependencies, workflows, repository permissions, browser state, release gates, or production-sensitive code without a clear review owner and rollback path.

### Relevant shortcut cards

- `vcb.shortcut.trusting_external_tool_output`
- `vcb.shortcut.accepting_looks_done`
- `vcb.shortcut.adding_dependencies_fast`

### Minimum guardrails

- one bounded tool purpose per run/change
- least privilege for repository, CI, package, and browser surfaces
- artifact or diff review before acceptance
- explicit rollback or revert path
- source check for current mechanics before updating durable docs
- Use Scorecard results as a checklist for review and hardening, then document accepted risks rather than treating scores as approval.

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

- finding interpretation
- false-positive triage
- policy exceptions
- CI integration maintenance
- maintainer follow-up for upstream dependencies

## Stable Core

- Supply-chain scores are triage signals, not safety certificates.
- Finding details and project context matter more than the headline score.
- Automated checks should feed a human hardening backlog.

## Volatile Surface

- check definitions, scoring mechanics, action setup, supported platforms, output formats, and policy guidance

Exact prices, plan packaging, quota limits, policy defaults, permission defaults, current UI labels, command flags, vulnerability/scoring details, and setup mechanics must be checked against official vendor/project sources or dated snapshots before use.

## Obsolescence Watch

This card becomes obsolete when: OpenSSF Scorecard is retired or replaced by a different official supply-chain health framework used by the project.

Review official vendor/project docs before relying on current mechanics.

## Evidence and Sources

- `openssf.scorecard` — official/synthesis source anchor for this tool card.
- `openssf.scorecard_checks` — official/synthesis source anchor for this tool card.
- `openssf.scorecard_action` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.workflow.dependency_decisions`
- `vcb.workflow.dependency_update_review`
- `vcb.failure.dependency_bloat`
- `tool.github`
- `tool.github_actions`
- `tool.github_dependabot`
- `tool.codex_security`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.openssf_scorecard -->
