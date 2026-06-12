<!-- VCB:BEGIN_TOPIC id=tool.github version=0.1.0 -->
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
id: tool.github
title: GitHub
name: GitHub
type: tool_card
category: repo_ci
status: active
review_cadence: quarterly
next_review_due: '2026-09-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: high
pricing_snapshot_required: false
setup_effort: 'medium: repository conventions, branches, reviews, checks, permissions,
  and labels need explicit setup'
maintenance_effort: 'medium: branch rules, teams, CODEOWNERS-style ownership, CI integrations,
  and repository settings drift over time'
debugging_effort: 'medium: failures may be Git history, branch protection, mergeability,
  required checks, permissions, or review process'
lock_in_risk: 'moderate: collaboration workflow, PR automation, checks, and issue
  history may become GitHub-specific'
hidden_cost_risk: 'medium: review queue, merge conflicts, stale branches, and permission
  cleanup can dominate apparent tool cost'
codex_integration_value: high as the durable review and source-control layer for Codex-generated
  work
best_for:
- repository source of truth
- pull requests and code review
- branch protection and review gates
- issues and release coordination
- handoff between Codex, CI, and humans
not_for:
- private secrets or credentials in repo history
- unreviewed direct-to-main mutation
- using PR summaries as proof
- large unrelated changes that no reviewer can audit
integrates_with_codex:
- Codex GitHub Review
- Codex Cloud PRs
- Codex App Git workflows
- GitHub Actions
- Codex Security
hidden_costs:
- review backlog from oversized PRs
- branch-rule maintenance
- merge conflict recovery
- permission and repository-role cleanup
applies_to:
- GitHub
- repository/CI/dependency/quality-assurance workflows
- Codex-assisted development
stability:
  principle: CORE_ENGINEERING
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_tests
- vcb.shortcut.broad_agent_permissions
durable_principles:
- Generated code needs a durable review surface, not just a chat transcript.
- Small branches and pull requests reduce blast radius and review cost.
- Branch protections and required checks are guardrails, not substitutes for human
  review.
likely_to_change:
- repository settings, pull-request UI, branch-rule mechanics, review features, integrations,
  billing, and permission defaults
obsolete_when:
- GitHub is no longer the repository collaboration system used by the project or its
  official docs stop treating repositories, branches, and pull requests as core collaboration
  surfaces.
related_topics:
- vcb.concepts.git_branch
- vcb.concepts.pull_request
- vcb.concepts.diff
- vcb.workflow.reviewing_diffs
- vcb.workflow.github_pr_review
- tool.github_actions
- tool.codex_github_review
---

# GitHub

> Summary:
> GitHub is the repository collaboration layer for code history, pull requests, review, branch protection, issues, and the source-of-truth handoff between humans, Codex, CI, and deployment tools.

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

<!-- VCB:BEGIN_SECTION id=tool.github.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

GitHub is where the code, review discussion, pull requests, branch rules, issues, and repository history live. It is not just storage. It is the place where work becomes reviewable and recoverable.

### Why it matters

Vibe coding fails fast when generated patches live only in chat, local folders, or screenshots. GitHub gives the team a durable review surface: branches, diffs, pull requests, checks, owners, and rollback history.

### What good looks like

A good GitHub workflow keeps AI-generated work on a branch or pull request, requires meaningful checks, records review decisions, and keeps secrets or production state out of casual repo changes.

### What bad looks like

A bad workflow pushes broad generated changes directly to the default branch, treats a green check as full approval, and uses issues or PR descriptions as vague summaries instead of evidence packets.

### Minimal example

For a Codex-generated feature, create a branch, open a small PR, attach the done-when evidence, wait for checks, review the diff, and merge only after the human reviewer understands the blast radius.

### Best-fit cases

- repository source of truth
- pull requests and code review
- branch protection and review gates
- issues and release coordination
- handoff between Codex, CI, and humans

### Not-fit cases

- private secrets or credentials in repo history
- unreviewed direct-to-main mutation
- using PR summaries as proof
- large unrelated changes that no reviewer can audit

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: repository conventions, branches, reviews, checks, permissions, and labels need explicit setup |
| Maintenance effort | medium: branch rules, teams, CODEOWNERS-style ownership, CI integrations, and repository settings drift over time |
| Debugging effort | medium: failures may be Git history, branch protection, mergeability, required checks, permissions, or review process |
| Lock-in risk | moderate: collaboration workflow, PR automation, checks, and issue history may become GitHub-specific |
| Hidden cost risk | medium: review queue, merge conflicts, stale branches, and permission cleanup can dominate apparent tool cost |

### Checklist

- define what evidence this tool is supposed to produce
- keep tool output tied to a branch, PR, log, artifact, or report
- separate automated signal from human approval
- keep pricing, quotas, defaults, and UI mechanics out of stable decisions
- re-check official vendor/project docs before encoding setup mechanics

<!-- VCB:END_SECTION id=tool.github.human -->

<!-- VCB:BEGIN_SECTION id=tool.github.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach `tool.github` as version control, pull requests, issues, review, branch protection, and repository collaboration. The core lesson is not “use the tool”; it is “use the tool to create reviewable evidence with bounded blast radius.”

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
Use GitHub for this task only if it produces reviewable evidence. Goal: [goal]. Current repo state: [branch/PR/logs/files]. Risk: [secrets/production/users/money]. Required evidence: [artifact/check/report]. Recommend the smallest safe use of the tool, the review step, and the rollback plan.
```

### Red flags

- tool output is treated as approval
- setup mechanics are copied from memory instead of official docs
- mutation happens before a report or review owner exists
- broad permissions are granted because the run is “just CI” or “just maintenance”
- exact prices, limits, quotas, or defaults are frozen in stable prose

### Intervention rule

When the human asks for current product behavior, exact pricing, limits, quotas, UI labels, command flags, permission defaults, or setup mechanics, route to official vendor/project sources or a dated volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.github.ai_coach -->

## Shortcut Reality

### The ideal practice

Use GitHub as one bounded part of the control loop: define intent, run the tool, collect evidence, review artifacts, then decide.

### What users often do instead

Users often treat the tool as a shortcut around review: a passed check, opened PR, audit output, generated browser test, or supply-chain score becomes “good enough” without inspecting the underlying evidence.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only reports, low-risk maintenance, or local experiments where rollback is trivial and no secrets, production state, or real users are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate dependencies, workflows, repository permissions, browser state, release gates, or production-sensitive code without a clear review owner and rollback path.

### Relevant shortcut cards

- `vcb.shortcut.accepting_looks_done`
- `vcb.shortcut.skipping_tests`
- `vcb.shortcut.broad_agent_permissions`

### Minimum guardrails

- one bounded tool purpose per run/change
- least privilege for repository, CI, package, and browser surfaces
- artifact or diff review before acceptance
- explicit rollback or revert path
- source check for current mechanics before updating durable docs
- Use branch protection, small PRs, explicit check expectations, and review owners before treating GitHub history as safe enough for production work.

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

- review backlog from oversized PRs
- branch-rule maintenance
- merge conflict recovery
- permission and repository-role cleanup

## Stable Core

- Generated code needs a durable review surface, not just a chat transcript.
- Small branches and pull requests reduce blast radius and review cost.
- Branch protections and required checks are guardrails, not substitutes for human review.

## Volatile Surface

- repository settings, pull-request UI, branch-rule mechanics, review features, integrations, billing, and permission defaults

Exact prices, plan packaging, quota limits, policy defaults, permission defaults, current UI labels, command flags, vulnerability/scoring details, and setup mechanics must be checked against official vendor/project sources or dated snapshots before use.

## Obsolescence Watch

This card becomes obsolete when: GitHub is no longer the repository collaboration system used by the project or its official docs stop treating repositories, branches, and pull requests as core collaboration surfaces.

Review official vendor/project docs before relying on current mechanics.

## Evidence and Sources

- `github.docs.repositories` — official/synthesis source anchor for this tool card.
- `github.docs.pull_requests` — official/synthesis source anchor for this tool card.
- `github.docs.branch_protection` — official/synthesis source anchor for this tool card.
- `github.docs.actions_overview` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.concepts.git_branch`
- `vcb.concepts.pull_request`
- `vcb.concepts.diff`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.github_pr_review`
- `tool.github_actions`
- `tool.codex_github_review`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.github -->
