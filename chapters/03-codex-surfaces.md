<!-- VCB:BEGIN_TOPIC id=vcb.chapter.codex_surfaces version=0.1.0 -->
---
id: vcb.chapter.codex_surfaces
title: "Chapter 3 — The Codex Surfaces: App, IDE, CLI, Cloud, GitHub, SDK"
type: chapter
chapter_number: 3
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- SDK
- GitHub Actions

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS

stability:
  principle: AGENTIC_PRINCIPLE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE

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

shortcut_profiles:
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.unofficial_tools

durable_principles:
- Choose the Codex surface by task shape, context needs, risk, and attention budget.
- Local surfaces are better when local-only context matters.
- Cloud/background surfaces are better when work can be isolated and reviewed later.
- Review surfaces provide signals; they do not replace human ownership.

likely_to_change:
- exact supported platforms
- UI labels and commands
- feature availability by plan
- model routing
- cloud environment behavior
- SDK package details
- GitHub integration behavior

obsolete_when:
- Codex surfaces merge into a single interface with no meaningful task-routing differences.
- OpenAI materially changes surface capabilities or access models.

related_topics:
- vcb.chapter.codex_mental_model
- vcb.chapter.vibe_coder_advantage_and_risk
- vcb.codex.app
- vcb.codex.ide_extension
- vcb.codex.cli
- vcb.codex.cloud
- vcb.codex.github_review
- vcb.codex.sdk
- vcb.workflow.cloud_delegation
- vcb.workflow.reviewing_diffs
- vcb.safety.permissions
---

> Summary:
> The right Codex surface depends on the shape of the job. Use the app for orchestration, the IDE for local context, the CLI for terminal-native control, cloud/web for isolated background work, GitHub review for PR risk signals, and the SDK for programmatic workflows.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.codex_surfaces.human -->
## 1. For the Human: Plain-Language Concept

### The simple rule

Do not choose a Codex surface by habit. Choose it by the task.

Ask four questions:

1. **Where is the context?** Open files, local repo, GitHub PR, cloud repo, browser, logs, or external tool?
2. **How long will the work run?** One small edit, one feature slice, a background task, or recurring automation?
3. **How risky is the change?** Prototype, production, auth, payments, data, secrets, deployment?
4. **How much attention will you give it?** Continuous supervision, periodic check-in, or review later?

### Current surface map

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
This table is a dated surface snapshot. Re-check official OpenAI Codex docs before relying on exact product names, platform support, commands, plan access, or feature availability.

| Surface | Best for | Avoid or delay when |
|---|---|---|
| Codex app | Orchestrating multiple threads, projects, worktrees, reviews, automations, and Git-oriented work from a desktop command center. | You only need one tiny local edit, or the project is not ready for parallel/background work. |
| Codex IDE extension | Working beside open files, selected code, local editor context, and quick implementation/review loops. | The task is long-running, independent, or better isolated in a cloud/worktree flow. |
| Codex CLI | Terminal-native work, scripts, local repo inspection, exact command-line control, and developer workflows in a selected directory. | The task is mostly visual/browser-based or needs rich UI inspection. |
| Codex web/cloud | Delegating background tasks in a cloud environment, including parallel work and repository-backed tasks that may create PRs. | Important context is only on your uncommitted local machine, or the task is ambiguous and risky. |
| GitHub code review | Getting another review signal on pull request diffs, especially serious issues, missing tests, regressions, or risky changes. | You need exploratory implementation, product design, or final human merge approval. |
| SDK / GitHub Action | Programmatic or CI/CD workflows, internal tools, repeatable automation, and controlled agent execution from code. | The job is one-off and interactive; manual Codex use is simpler. |
<!-- VCB:END_VOLATILE_INFO -->

### How to choose quickly

Use this decision table:

| You need | Start with |
|---|---|
| Explain or patch code near open files | IDE extension |
| Run terminal commands and inspect local output | CLI |
| Let Codex work while you do something else | Codex app or Codex web/cloud, with isolation |
| Compare or review a pull request | GitHub code review or app review flow |
| Run the same agent task repeatedly in CI | SDK or GitHub Action |
| Build a visual/web UI and inspect it | App/browser-capable workflow or local IDE + browser |

### The surface does not remove responsibility

A better surface reduces friction. It does not make the patch safe by itself.

The same risk questions still apply:

- Is the diff small enough to review?
- Did it touch sensitive files?
- Were checks run?
- Can you roll it back?
- Is the task isolated from unfinished work?
- Are real secrets, money, users, or persistent data involved?

### Common mistake

The common mistake is using the most powerful or most convenient surface for every job.

Examples:

- Using cloud delegation for a tiny one-line fix that needs local context.
- Using the IDE extension for a long independent background task.
- Using GitHub review as if it were merge approval.
- Using the SDK for a one-off task that does not need automation.
- Letting an unattended surface operate on ambiguous production work.

The surface should reduce friction for the task, not hide the risk.

<!-- VCB:END_SECTION id=vcb.chapter.codex_surfaces.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.codex_surfaces.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach task/surface matching without overfitting to current UI details. The durable concept is: context location, task duration, risk, and attention decide the surface.

### Diagnose the current surface choice

Ask:

- Which surface is the human using now?
- Is the necessary context local, in GitHub, in a browser, or external?
- Does the work need synchronous steering or can it run in the background?
- Is the working tree clean?
- Is the task safe to delegate unattended?
- Is this a one-off task or a repeatable workflow?

### Explanation strategy

Use the surface as a routing decision, not a brand preference.

```text
The IDE is best when the context is what you are looking at now. The CLI is best when commands and local files matter. Cloud is best when the task can be isolated and reviewed later. GitHub review is best when there is already a PR diff. The SDK is for repeatable automation, not casual prompting.
```

### Useful metaphors

- **Workbench:** IDE and CLI surfaces are the workbench where local tools and open files are already laid out.
- **Separate workshop:** cloud/background work is a separate workshop where Codex can make a mess without covering your main desk.
- **Inspection station:** GitHub review is an inspection station, not the factory that builds the part.
- **Conveyor belt:** SDK and GitHub Action workflows are conveyor belts for repeatable tasks; do not put one-off creative work on them too early.

### Coaching tactics

For a local, context-heavy bug:

```text
Use the IDE extension or CLI. The relevant context is local and interactive. Cloud may miss uncommitted state unless you provide it.
```

For a long feature slice:

```text
Use Codex app or cloud only after making the task small and isolating the branch/worktree. Require a final report and review the diff.
```

For a PR review:

```text
Use GitHub review as an additional signal. Do not treat it as final approval. Ask it to focus on P0/P1 risks or the specific risk area.
```

For automation:

```text
Use SDK or GitHub Action only when the workflow is repeatable and narrow. Start read-only/report-only before allowing mutations.
```

### Prompt patterns

```text
Choose the best Codex surface for this task.
Context location:
Task length:
Risk level:
Human attention:
Need for local commands:
Need for PR review:
Need for repeatable automation:
Recommend one surface, one fallback, and the guardrails.
```

```text
I want Codex to work in the background.
Before starting, classify whether this is safe for low-attention work.
If it is not safe, explain the smallest isolation and review steps needed.
```

### Red flags to call out directly

- The user wants background/cloud work while the actual context is uncommitted local state.
- The user wants unattended work touching auth, payments, data, secrets, or deployment.
- The user treats GitHub review as a merge gate instead of a signal.
- The user wants to build custom SDK automation for an unstable manual workflow.
- The user chooses a surface because it is new or powerful, not because it fits the task.

### Exercises

1. Give the human five tasks and ask them to pick the best surface for each.
2. Ask them to explain why a cloud task needs isolation before low-attention work.
3. Ask them to identify what context would be missing if the same task moved from IDE to cloud.

<!-- VCB:END_SECTION id=vcb.chapter.codex_surfaces.ai_coach -->

## Shortcut Reality

### The ideal practice

The ideal practice is to choose the smallest surface that has the needed context, authority, and workflow fit. More power is not automatically better.

### What users often do instead

Users often use one favorite surface for everything. High-usage users may over-delegate to cloud/background work. Technical users may overbuild SDK automation. Beginners may stay in chat or the IDE even when a PR review or isolated background task would fit better.

### When the shortcut may be fine

Using one surface for most work may be fine when:

- the repo is small,
- the project is local or prototype-only,
- the human is supervising closely,
- the task is low risk,
- the workflow is not repeated often enough to automate.

### When the shortcut is a bad idea

It is a bad idea when:

- the surface lacks the real context,
- the surface has more permissions than the task needs,
- background work touches production-sensitive areas,
- automation can mutate code without review,
- the user is avoiding diff review because the surface made delegation easy.

### Risk profile

- Probability of failure: low when surface and context match; medium to high when they do not.
- Impact if it fails: depends on permissions, deployment coupling, and data sensitivity.
- Ease of recovery: high with branches/worktrees and reports; low with direct edits and no checkpoint.
- Blast radius: grows with background autonomy, network access, and sensitive credentials.
- Skill needed to recover: higher for SDK/CI automation and cloud changes than for supervised IDE edits.
- Hidden cost: context gaps, duplicate work, automation maintenance, and review debt.

### Minimum guardrails

- Use local surfaces when local-only context matters.
- Use cloud/background surfaces only with isolated branches/worktrees for non-trivial changes.
- Start SDK/GitHub Action workflows as report-only where possible.
- Treat GitHub review as an additional signal, not merge approval.
- Require final reports for background work.
- Re-check official docs for surface-specific behavior before writing exact instructions.

### Recovery plan

If the wrong surface caused trouble:

1. Stop the current task.
2. Identify which context was missing or which permission was excessive.
3. Save or discard the diff from an isolated branch/worktree.
4. Move the task to the correct surface.
5. Rewrite the prompt with explicit context and constraints.
6. Add a note to future guidance if the same surface mismatch is likely to recur.

### AI coach guidance

Do not tell the user “always use X.” That will rot quickly and is usually wrong.

```text
The surface choice is off. This task needs local context and close steering, so use the IDE or CLI. Cloud/background work is better after we isolate a branch and make the task precise enough to review later.
```

## Budget and Constraint Notes

### Cheapest reliable path

Pick one primary surface and use it well. For many constrained users, the IDE or CLI plus small scoped tasks is cheaper than broad cloud exploration. Avoid SDK automation until a workflow is repeated and stable.

### Fastest high-usage path

Use the Codex app or cloud for isolated parallel tasks, GitHub review for second-pass checks, and local IDE/CLI for fast steering. Spend usage to save attention only when branches/worktrees and final reports preserve reviewability.

### Low-attention path

Low-attention work belongs in isolated background tasks with explicit boundaries. It should not touch real secrets, payments, auth rules, production deployment, migrations, or data deletion unless the review and rollback process is already strong.

### Production-quality path

Use surface specialization: local surfaces for precise edits, cloud/worktrees for isolated feature branches, GitHub review for PR-level risk signals, and SDK/GitHub Action only for narrow repeatable workflows with controlled permissions and logs.

## Stable Core

- Choose surfaces by context, task length, risk, and attention.
- Local surfaces are better for local-only context.
- Background surfaces need isolation and review.
- Review surfaces add signal but do not replace ownership.
- Automation is valuable only after a workflow is narrow and repeatable.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
The current Codex surface map is volatile. Official docs currently describe Codex app, IDE extension, CLI, web/cloud, GitHub code review, SDK, GitHub Action, automations, skills, and other features. Exact feature names, platform support, maturity labels, commands, app flows, and access rules must be rechecked against official OpenAI docs before use.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes Codex surface names or feature boundaries.
- app, IDE, CLI, cloud/web, GitHub review, or SDK capabilities materially change.
- a feature maturity label changes for a surface-critical capability.
- pricing/plan access changes in a way that affects budget routing.
- new official Codex surfaces become first-class.

## Evidence and Sources

- `openai.codex.overview` — Official Codex positioning as a coding agent.
- `openai.codex.app` — Official app surface anchor.
- `openai.codex.app_features` — Official app feature anchor, including threads/worktrees/review/automation-oriented capabilities.
- `openai.codex.ide` — Official IDE extension surface anchor.
- `openai.codex.cli` — Official CLI surface anchor.
- `openai.codex.cloud` — Official Codex web/cloud surface anchor.
- `openai.codex.github_review` — Official GitHub code review integration anchor.
- `openai.codex.sdk` — Official SDK/programmatic control anchor.
- `openai.codex.github_action` — Official GitHub Action anchor for CI/CD workflows.
- `openai.codex.feature_maturity` — Official maturity-label source for feature stability.
- `openai.codex.changelog` — Official source for surface and feature-change monitoring.

## Related Topics

- `vcb.chapter.codex_mental_model`
- `vcb.chapter.vibe_coder_advantage_and_risk`
- `vcb.codex.app`
- `vcb.codex.ide_extension`
- `vcb.codex.cli`
- `vcb.codex.cloud`
- `vcb.codex.github_review`
- `vcb.codex.sdk`
- `vcb.workflow.cloud_delegation`
- `vcb.workflow.reviewing_diffs`
- `vcb.safety.permissions`
- `vcb.shortcut.unattended_long_runs`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.codex_surfaces -->
