<!-- VCB:BEGIN_TOPIC id=vcb.codex.automations version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
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
evidence_scope: official OpenAI product behavior anchors plus VCB maintainer synthesis
  for risk, workflow, and coaching guidance
budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget
cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- unattended_high_throughput
- production_quality
project_phases:
- prototype
- mvp
- production_build
- maintenance
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.codex.automations
title: Codex Automations
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Recurring work
- Local projects
- Worktrees
- Skills
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.automating_unstable_workflow
- vcb.shortcut.automation_spam
- vcb.shortcut.automation_mutation_without_review
durable_principles:
- automate stable recurring work, not ambiguous judgment-heavy work
- report-only automation is safer than mutation
- automations need schedules, owners, inputs, and stopping conditions
likely_to_change:
- automation UI and scheduling options
- inbox/archive behavior
- local project/worktree execution details
- interaction with skills and models
obsolete_when:
- Codex automations are removed or replaced by another scheduled-task mechanism
related_topics:
- vcb.chapter.automations_recurring_work
- vcb.codex.skills
- vcb.codex.app
- vcb.codex.cloud
- vcb.chapter.prompt_library_to_team_workflow
---

> Summary:
> Codex automations are scheduled recurring tasks, useful when the same scoped work needs to run repeatedly and report findings.

## Quick Navigation
- For the Human
- For the AI Coach
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=vcb.codex.automations.human -->
## 1. For the Human: Plain-Language Concept

### What this means

An automation is Codex doing a repeated task on a schedule. Good examples are weekly dependency summaries, release-note drafts, stale issue triage, or report-only checks. Bad examples are vague product work or unattended destructive changes.

### Why it matters

Automations matter because repeated prompts are wasteful. But automating a messy workflow just makes the mess repeat faster.

### The mental model

An automation is a recurring alarm plus a work order. It should know what to inspect, when to run, what to report, and when to stay quiet.

### What good looks like

Good use: schedule a read-only weekly report that summarizes recent CI failures and links evidence.

### What bad looks like

Bad use: schedule Codex to rewrite production code every night with broad permissions and no owner.

### Minimal example

Example: every Monday, ask Codex to scan merged PRs and draft release notes, then place findings in an inbox for human review.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.automations.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.automations.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach automations as recurring, stable, scoped workflows. Push report-first before mutation.

### Diagnose the human’s current model

- Is this task repeated and stable?
- Who owns the findings?
- Can it run read-only first?
- What should happen if there is nothing to report?
- What is the stop condition?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

Automation is a dishwasher, not a chef. It is great for repeatable cycles and bad at deciding what dinner should be.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Turn this repeated task into a report-only automation. Define cadence, project, prompt, inputs, forbidden actions, output location, when to archive/no-op, and what requires human approval before mutation.
```

### Red flags to call out directly

- automation mutates without review
- task is still changing every week
- no owner for findings
- automation touches secrets or production config
- spammy reports are ignored

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.automations.ai_coach -->

## Shortcut Reality

### The ideal practice

Automate recurring, low-ambiguity work with clear output and human review for any mutation.

### What users often do instead

Users often schedule unstable workflows because automation feels like progress.

### When the shortcut may be fine

A short-lived experimental automation is fine if it is read-only and easy to delete.

### When the shortcut is a bad idea

It is bad when it mutates production, spams reports, uses broad permissions, or runs on unclear acceptance criteria.

### Risk profile

- Probability of failure: Medium failure probability from stale prompts
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- start read-only
- set a clear cadence and owner
- use skills for stable method, automation for schedule
- prefer worktrees for changes
- review output before action

### Recovery plan

Disable the automation, inspect recent runs, revert any unwanted changes, narrow the prompt, and restart only after a report-only trial.

### AI coach guidance

Do not moralize the shortcut. Name the tradeoff, reduce blast radius, improve recoverability, and require the smallest guardrail that changes the risk profile.

## Budget and Constraint Notes

### Cheapest reliable path

Use this feature for one narrow task with curated context, conservative permissions, and one relevant check. Do not spend usage exploring broad unknowns unless the task is important enough to justify it.

### Fastest high-usage path

Use this feature aggressively only with branch/worktree isolation, clear acceptance criteria, structured final reports, and independent review for risky diffs.

### Low-attention path

Low-attention work requires stronger isolation, report-only or read-only posture when possible, fake credentials, and a final report that names files changed, checks run, unresolved risks, and review needs.

### Production-quality path

Use least privilege, clear done-when criteria, Git checkpoints, tests/build/lint where relevant, diff review, source-register discipline, and a rollback plan before accepting work.

## Stable Core

- automate stable recurring work, not ambiguous judgment-heavy work
- report-only automation is safer than mutation
- automations need schedules, owners, inputs, and stopping conditions

## Volatile Surface

- automation UI and scheduling options
- inbox/archive behavior
- local project/worktree execution details
- interaction with skills and models

## Obsolescence Watch

- Codex automations are removed or replaced by another scheduled-task mechanism

## Evidence and Sources

- `openai.codex.app_automations` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.skills` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.best_practices` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.automations_recurring_work`
- `vcb.codex.skills`
- `vcb.codex.app`
- `vcb.codex.cloud`
- `vcb.chapter.prompt_library_to_team_workflow`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.automations -->
