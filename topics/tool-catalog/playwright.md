<!-- VCB:BEGIN_TOPIC id=tool.playwright version=0.1.0 -->
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
id: tool.playwright
title: Playwright
name: Playwright
type: tool_card
category: browser_testing
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: high
pricing_snapshot_required: false
setup_effort: 'medium: test runner, browsers, fixtures, data setup, CI, and artifact
  handling need deliberate setup'
maintenance_effort: 'medium-high: UI changes, test data, browser updates, selectors,
  and CI environments require maintenance'
debugging_effort: 'medium-high: failures can be app bugs, test flake, timing, browser
  dependencies, network, data, or selector drift'
lock_in_risk: 'medium: test patterns, fixtures, selectors, and trace/report workflows
  may become Playwright-specific'
hidden_cost_risk: 'medium-high: browser tests can consume CI time and reviewer attention
  if scoped too broadly'
codex_integration_value: high for web projects because Codex can use browser-test
  output as concrete UI verification evidence
best_for:
- end-to-end browser tests
- critical user journey verification
- frontend regression checks
- screenshots and trace evidence
- CI browser testing
not_for:
- unit-test replacement
- security review
- accessibility approval by itself
- manual taste review replacement
- testing flows with unstable test data and no isolation
integrates_with_codex:
- Codex App browser workflows
- GitHub Actions
- npm scripts
- Codex frontend work
- visual QA workflows
hidden_costs:
- test flakiness
- browser dependency setup
- CI runtime
- test data isolation
- trace artifact storage
- locator maintenance
applies_to:
- Playwright
- repository/CI/dependency/quality-assurance workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.browser_clicking_without_repro
- vcb.shortcut.skipping_tests
- vcb.shortcut.accepting_looks_done
durable_principles:
- Browser tests should protect critical behavior, not every pixel.
- Use artifacts to diagnose failure rather than accepting screenshots as proof.
- Stable user-facing locators beat brittle DOM-shape guesses.
likely_to_change:
- browser versions, CI setup, config options, report formats, locator guidance, trace
  tooling, and installation mechanics
obsolete_when:
- the project stops being web/browser-facing or replaces Playwright with a different
  browser-test authority.
related_topics:
- vcb.workflow.frontend_work
- vcb.workflow.visual_qa
- vcb.workflow.testing
- vcb.failure.ui_taste_gap
- vcb.failure.ci_false_confidence
- tool.github_actions
- tool.npm
---

# Playwright

> Summary:
> Playwright is a browser-testing and UI-verification tool for end-to-end tests, browser automation, screenshots, traces, and CI evidence for web apps.

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

<!-- VCB:BEGIN_SECTION id=tool.playwright.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Playwright lets a project express browser behavior as tests and inspect rendered results. It is useful when a model says “the UI works” but the truth depends on user flows, states, responsive behavior, and browser evidence.

### Why it matters

Screenshots and model summaries are weak evidence. Playwright can turn critical web flows into repeatable checks that run locally or in CI and produce artifacts a reviewer can inspect.

### What good looks like

A good Playwright workflow covers a few high-value user journeys, uses stable user-facing locators, produces failure artifacts, and runs in CI when the flow matters for release confidence.

### What bad looks like

A bad workflow records brittle click paths, overfits screenshots, hides flakes with sleeps, or treats passing browser tests as proof that accessibility, security, and backend behavior are complete.

### Minimal example

For a signup flow, test the happy path, one validation failure, and the post-submit state. Attach trace or screenshot artifacts when the test fails.

### Best-fit cases

- end-to-end browser tests
- critical user journey verification
- frontend regression checks
- screenshots and trace evidence
- CI browser testing

### Not-fit cases

- unit-test replacement
- security review
- accessibility approval by itself
- manual taste review replacement
- testing flows with unstable test data and no isolation

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: test runner, browsers, fixtures, data setup, CI, and artifact handling need deliberate setup |
| Maintenance effort | medium-high: UI changes, test data, browser updates, selectors, and CI environments require maintenance |
| Debugging effort | medium-high: failures can be app bugs, test flake, timing, browser dependencies, network, data, or selector drift |
| Lock-in risk | medium: test patterns, fixtures, selectors, and trace/report workflows may become Playwright-specific |
| Hidden cost risk | medium-high: browser tests can consume CI time and reviewer attention if scoped too broadly |

### Checklist

- define what evidence this tool is supposed to produce
- keep tool output tied to a branch, PR, log, artifact, or report
- separate automated signal from human approval
- keep pricing, quotas, defaults, and UI mechanics out of stable decisions
- re-check official vendor/project docs before encoding setup mechanics

<!-- VCB:END_SECTION id=tool.playwright.human -->

<!-- VCB:BEGIN_SECTION id=tool.playwright.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.playwright` as browser testing, end-to-end user journeys, screenshots, traces, and CI UI evidence. The core lesson is not “use the tool”; it is “use the tool to create reviewable evidence with bounded blast radius.”

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
Use Playwright for this task only if it produces reviewable evidence. Goal: [goal]. Current repo state: [branch/PR/logs/files]. Risk: [secrets/production/users/money]. Required evidence: [artifact/check/report]. Recommend the smallest safe use of the tool, the review step, and the rollback plan.
```

### Red flags

- tool output is treated as approval
- setup mechanics are copied from memory instead of official docs
- mutation happens before a report or review owner exists
- broad permissions are granted because the run is “just CI” or “just maintenance”
- exact prices, limits, quotas, or defaults are frozen in stable prose

### Intervention rule

When the human asks for current product behavior, exact pricing, limits, quotas, UI labels, command flags, permission defaults, or setup mechanics, route to official vendor/project sources or a dated volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.playwright.ai_coach -->

## Shortcut Reality

### The ideal practice

Use Playwright as one bounded part of the control loop: define intent, run the tool, collect evidence, review artifacts, then decide.

### What users often do instead

Users often treat the tool as a shortcut around review: a passed check, opened PR, audit output, generated browser test, or supply-chain score becomes “good enough” without inspecting the underlying evidence.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only reports, low-risk maintenance, or local experiments where rollback is trivial and no secrets, production state, or real users are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate dependencies, workflows, repository permissions, browser state, release gates, or production-sensitive code without a clear review owner and rollback path.

### Relevant shortcut cards

- `vcb.shortcut.browser_clicking_without_repro`
- `vcb.shortcut.skipping_tests`
- `vcb.shortcut.accepting_looks_done`

### Minimum guardrails

- one bounded tool purpose per run/change
- least privilege for repository, CI, package, and browser surfaces
- artifact or diff review before acceptance
- explicit rollback or revert path
- source check for current mechanics before updating durable docs
- Start with the smallest critical flows, isolate test data, publish failure evidence, and treat flaky tests as product or test debt rather than noise to ignore.

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

- test flakiness
- browser dependency setup
- CI runtime
- test data isolation
- trace artifact storage
- locator maintenance

## Stable Core

- Browser tests should protect critical behavior, not every pixel.
- Use artifacts to diagnose failure rather than accepting screenshots as proof.
- Stable user-facing locators beat brittle DOM-shape guesses.

## Volatile Surface

- browser versions, CI setup, config options, report formats, locator guidance, trace tooling, and installation mechanics

Exact prices, plan packaging, quota limits, policy defaults, permission defaults, current UI labels, command flags, vulnerability/scoring details, and setup mechanics must be checked against official vendor/project sources or dated snapshots before use.

## Obsolescence Watch

This card becomes obsolete when: the project stops being web/browser-facing or replaces Playwright with a different browser-test authority.

Review official vendor/project docs before relying on current mechanics.

## Evidence and Sources

- `playwright.docs.intro` — official/synthesis source anchor for this tool card.
- `playwright.docs.writing_tests` — official/synthesis source anchor for this tool card.
- `playwright.docs.ci` — official/synthesis source anchor for this tool card.
- `playwright.docs.visual_comparisons` — official/synthesis source anchor for this tool card.
- `playwright.docs.screenshots` — official/synthesis source anchor for this tool card.
- `playwright.docs.accessibility_testing` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.workflow.frontend_work`
- `vcb.workflow.visual_qa`
- `vcb.workflow.testing`
- `vcb.failure.ui_taste_gap`
- `vcb.failure.ci_false_confidence`
- `tool.github_actions`
- `tool.npm`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.playwright -->
