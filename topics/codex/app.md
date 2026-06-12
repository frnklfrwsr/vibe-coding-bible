<!-- VCB:BEGIN_TOPIC id=vcb.codex.app version=0.1.0 -->
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
id: vcb.codex.app
title: Codex App
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Git
- Local repositories
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.parallel_agents_edit_same_files
durable_principles:
- use the app when the work benefits from parallel threads, worktrees, review panes,
  and durable project context
- treat app-generated changes as patch proposals until reviewed
- prefer app workflows when visual review, Git review, or repeated local project context
  matter
likely_to_change:
- platform support and installation flow
- review pane details
- worktree and automation UI
- available app features and settings
obsolete_when:
- Codex app is deprecated or replaced by another official primary surface
- official docs no longer describe app work as thread/worktree-oriented
related_topics:
- vcb.chapter.codex_surfaces
- vcb.codex.cli
- vcb.codex.ide_extension
- vcb.codex.cloud
- vcb.codex.automations
- vcb.concepts.diff
- vcb.concepts.git_branch
---

> Summary:
> The Codex app is the workspace-style surface for managing Codex threads, local projects, worktrees, reviews, and repeated work in one place.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.app.human -->
## 1. For the Human: Plain-Language Concept

### What this means

The Codex app is the place to manage Codex work when the job is bigger than one quick terminal request. Think of it like a project room: you can keep multiple work threads, inspect changes, use Git-aware review surfaces, and coordinate local project work without turning every task into a new one-off chat.

### Why it matters

The app matters because serious Codex work usually needs more than a prompt box. You need a place to watch what changed, compare threads, keep work isolated, and decide what to accept. The app is useful when you want Codex to work like a teammate with a desk, not like a single autocomplete response.

### The mental model

Use the app as the command center. The human owns direction and acceptance. Codex proposes changes. Git, diffs, checks, and final reports are the evidence.

### What good looks like

Good use: create a branch or worktree, give Codex a scoped task, review the diff in the app, run the relevant checks, and accept only the change you understand.

### What bad looks like

Bad use: start multiple broad threads against the same files, trust the final summary, and merge changes because the app makes the work look tidy.

### Minimal example

Example: ask the app to update one settings screen, keep the change in an isolated worktree, then compare the resulting diff against the acceptance criteria before committing.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.app.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.app.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the app as a coordination surface, not as proof that the work is safe.

### Diagnose the human’s current model

- Is the user juggling multiple Codex tasks that could touch the same files?
- Does the user know where to review the diff and what checks prove done?
- Is the task safer as a worktree, branch, or read-only investigation first?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

The app is a workshop bench. It helps organize tools and parts, but it does not inspect the finished machine for you.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Use the Codex app for this as an isolated task. Work only on [scope]. Before editing, summarize the likely files. After editing, leave a report with changed files, checks run, risks, and whether another thread might conflict with this work.
```

### Red flags to call out directly

- multiple app threads editing the same files
- user reviewing only the app summary
- automation or worktree work touching secrets, deployment config, or production data without explicit guardrails

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.app.ai_coach -->

## Shortcut Reality

### The ideal practice

Use the app for multi-step, reviewable Codex work where threads, worktrees, Git review, and durable project context help.

### What users often do instead

Users often treat the app’s tidy interface as a safety guarantee and accept work because the final report sounds coherent.

### When the shortcut may be fine

The shortcut may be fine for a throwaway prototype branch or a UI sketch with no real users and an easy rollback.

### When the shortcut is a bad idea

It is a bad idea for auth, payments, production data, deployment config, or parallel edits where conflicts can be hidden.

### Risk profile

- Probability of failure: Medium failure probability, medium to high impact when multiple threads touch shared files, good recovery if every task is isolated and committed.
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- one task per thread
- one branch or worktree per broad task
- review the diff, not only the summary
- run one relevant check
- do not let parallel threads edit the same files without an integration plan

### Recovery plan

Stop new app threads, inspect Git status in every worktree, identify overlapping files, keep the smallest correct diff, discard or reset the rest, then record the lesson in AGENTS.md if this is recurring.

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

- use the app when the work benefits from parallel threads, worktrees, review panes, and durable project context
- treat app-generated changes as patch proposals until reviewed
- prefer app workflows when visual review, Git review, or repeated local project context matter

## Volatile Surface

- platform support and installation flow
- review pane details
- worktree and automation UI
- available app features and settings

## Obsolescence Watch

- Codex app is deprecated or replaced by another official primary surface
- official docs no longer describe app work as thread/worktree-oriented

## Evidence and Sources

- `openai.codex.app` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.app_features` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.app_review` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.app_worktrees` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.codex_surfaces`
- `vcb.codex.cli`
- `vcb.codex.ide_extension`
- `vcb.codex.cloud`
- `vcb.codex.automations`
- `vcb.concepts.diff`
- `vcb.concepts.git_branch`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.app -->
