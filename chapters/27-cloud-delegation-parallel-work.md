<!-- VCB:BEGIN_TOPIC id=vcb.chapter.cloud_delegation_parallel_work version=0.1.0 -->
---
id: vcb.chapter.cloud_delegation_parallel_work
title: "Chapter 27 — Cloud Delegation and Parallel Work"
type: chapter
chapter_number: 27
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex Web
- Codex Cloud
- Codex App
- GitHub
- cloud environments
- worktrees
- pull requests
- parallel task delegation

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: VOLATILE
  pricing: VOLATILE

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
- vcb.shortcut.cloud_task_without_context
- vcb.shortcut.parallel_agents_edit_same_files
- vcb.shortcut.cloud_work_with_real_secrets

durable_principles:
- Delegate only when the task boundary is clear enough to review later.
- Keep parallel work isolated by branch, worktree, repository, or read-only report.
- Cloud work is a patch proposal, not completed shipping work.
- High-throughput workflows spend usage to save attention but still need review and rollback.

likely_to_change:
- Codex web/cloud UI and task lifecycle
- cloud environment setup behavior
- GitHub connection and PR-creation details
- internet access controls
- plan/package access and usage economics

obsolete_when:
- Codex cloud task architecture or environment model changes materially.
- Cloud task review/PR workflow changes enough that routing advice is stale.
- Internet-access or secret-handling guidance changes.

related_topics:
- vcb.chapter.codex_surfaces
- vcb.chapter.git_discipline
- vcb.chapter.acceptance_criteria
- vcb.chapter.ci_noninteractive_github_actions
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.workflow.cloud_delegation
- vcb.codex.cloud
---


> Summary:
> Cloud delegation means giving Codex a scoped job to run away from your local hands-on session. It is useful when work can happen in a separate environment, branch, or worktree and return as a reviewable diff or report.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.cloud_delegation_parallel_work.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Cloud delegation is when you hand Codex a task and let it work in the background instead of sitting in the same local thread while it edits. The right mental model is: **you send a contractor to a separate workshop, then inspect what comes back before you install it in the house.**

This is powerful because Codex can run longer tasks, work in parallel, and come back with a patch, PR, or explanation. It is risky because distance makes it easier to miss missing context, wrong assumptions, hidden setup failures, and broad changes.

### When cloud delegation is a good fit

Use cloud delegation when the task has a clear boundary:

- "Investigate why this test is failing and propose a fix."
- "Implement this small feature slice on a branch and open a PR."
- "Audit these files and report where the API behavior changed."
- "Try a refactor in an isolated worktree, but do not merge it."

Bad fit:

- "Make my app better."
- "Redesign the whole architecture."
- "Fix production."
- "Figure out everything and ship it while I am away."

The cloud is not magic judgment. It is more distance plus more autonomy. That can be productive only when the task has a clear map.

### Parallel work is not parallel chaos

Parallel work means multiple independent attempts or tasks can run at the same time. It does **not** mean multiple agents should edit the same files, same branch, same migration, or same deployment settings.

Good parallelization:

- one branch explores approach A, another explores approach B;
- one task writes tests while another performs read-only security review;
- one task investigates a bug while another maps relevant code paths;
- one cloud task implements a backend slice while a local session works on copy or docs.

Bad parallelization:

- three agents edit the same component;
- two agents change the same database migration;
- one agent refactors while another adds a feature on top of the old structure;
- cloud task modifies deployment config while CI automation is also changing it.

### What good looks like

A good cloud task has:

- one goal;
- exact repo/branch context;
- files or modules likely involved;
- constraints and forbidden areas;
- checks to run;
- a final report format;
- a branch/worktree/PR boundary;
- a human review gate before merge or deploy.

### What bad looks like

Bad cloud delegation usually has one of these shapes:

- The prompt is broad enough that Codex invents scope.
- The task needs local-only context that was never committed or attached.
- The agent has internet or secret access it does not need.
- Multiple agents touch the same files.
- The human merges because the task "completed" instead of reviewing the diff.

### Minimal prompt

```text
Run this as a cloud task on a separate branch/worktree.

Goal:
Implement only [small behavior].

Context:
Relevant files: [files].
Relevant issue/spec: [link or text].

Constraints:
- Do not touch auth, billing, deployment config, secrets, or migrations.
- Do not add dependencies.
- Keep public API shape unchanged.

Done when:
- Relevant tests/checks pass or failures are reported with output.
- Final report lists files changed, checks run, risks, and anything not done.
- Open/propose a PR only for human review; do not merge.
```

### Checklist

Before delegating:

- Is the task small enough to review later?
- Is the repo state committed/pushed or otherwise available?
- Can the agent run checks in its environment?
- Is the work isolated from your local edits?
- Does the task avoid secrets, production data, and destructive operations?
- Do you know what would count as done?
<!-- VCB:END_SECTION id=vcb.chapter.cloud_delegation_parallel_work.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.cloud_delegation_parallel_work.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use cloud delegation as **scoped asynchronous work**, not as unattended shipping. The core intervention is: "What exactly should come back for review?"

### Diagnose the human’s current model

Ask:

- Is this task independent enough to run away from the current local context?
- Are uncommitted local changes required for Codex to understand it?
- Could two tasks collide on the same files?
- Does the work need secrets, production access, or internet access?
- Will the human review a diff or just trust the completion message?

### Explanation strategy

Frame cloud work as a branch factory. The factory can produce several candidate patches quickly, but the human still chooses what enters the product. If the human wants speed, give speed through isolation, not through blind trust.

### Useful metaphors

- **Workshop metaphor:** Codex builds in another workshop; inspect the part before installing it.
- **Branch factory:** cloud tasks produce candidate branches, not truth.
- **Air traffic control:** parallel tasks need lanes; same-file edits are runway collisions.

### Coaching tactics

- Force a task boundary before cloud delegation.
- Ask for branch/worktree/PR isolation.
- Convert broad goals into one slice or one report.
- Prefer read-only reports for unknown, security-sensitive, or production-adjacent work.
- When the user wants several attempts, make each attempt independent and require a comparison report.

### Prompt patterns

```text
Before delegating to cloud, split this into independent tasks.
For each task, list:
- files likely affected,
- branch/worktree name,
- exact output expected,
- checks to run,
- merge risk,
- whether it may edit code or must stay read-only.
```

```text
Run a best-of-3 cloud exploration.
Each attempt should stay on its own branch and solve only [narrow goal].
At the end, compare the branches by correctness, diff size, test coverage, dependency changes, and rollback risk.
Do not merge anything.
```

### Red flags to call out directly

- "Leave it running for hours and ship whatever it returns."
- "Let several tasks edit the same files."
- "Use production credentials because setup is easier."
- "The code is only on my laptop, but I sent a cloud task anyway."
- "It opened a PR, therefore it is done."

### Exercises

1. Take a broad product request and split it into three isolated cloud tasks.
2. Rewrite an unsafe cloud prompt into a report-only prompt.
3. Given two cloud PRs, identify whether their diffs conflict before reviewing quality.
<!-- VCB:END_SECTION id=vcb.chapter.cloud_delegation_parallel_work.ai_coach -->


## Shortcut Reality

### The ideal practice

Delegate only scoped, reviewable tasks. Keep cloud work isolated. Review the diff, logs, and final report before merging.

### What users often do instead

They send a giant vague task, leave it running, and treat the returned PR as if Codex already did the senior-engineer review.

### When the shortcut may be fine

A long unattended run can be rational when the task is on a disposable branch, has no real secrets, touches no production data, and returns a reviewable report or diff.

### When the shortcut is a bad idea

It is a bad idea when the task is ambiguous, destructive, production-connected, secret-bearing, migration-heavy, or colliding with local work.

### Risk profile

- Probability of failure: medium for broad tasks, low/medium for narrow tasks.
- Impact if it fails: low in isolated prototypes; high with production config, data, secrets, or deploy paths.
- Ease of recovery: high with branch/worktree isolation and clean commits; low with merged unattended changes.
- Blast radius: controlled by branch, environment, internet access, and secrets.
- Skill needed to recover: medium; higher if multiple branches conflict.
- Hidden cost: review burden, duplicated work, usage burn, context mismatch.

### Minimum guardrails

- Use a branch/worktree or PR boundary.
- Keep the task small enough to review in one pass.
- Do not provide real secrets unless the task strictly requires them and the environment is designed for that risk.
- Prefer internet access off or allowlisted.
- Ask for files changed, checks run, assumptions, and risks.

### Recovery plan

If cloud work goes wrong, do not merge more. Compare the branch to the target branch, identify touched files, revert or discard the branch if needed, then re-run as a smaller task with tighter constraints.

### AI coach guidance

Do not block high-throughput workflows reflexively. Move the user toward isolation and review. The safer version of "let Codex work while I do something else" is "let Codex work in a bounded branch and return evidence."

## Budget and Constraint Notes

### Cheapest reliable path

Use cloud rarely. Plan locally, delegate one narrow task, and ask for the smallest relevant checks.

### Fastest high-usage path

Run several isolated branches or worktrees, then compare the diffs. Spend usage on parallel exploration, not on unbounded mutation.

### Low-attention path

Use report-only or branch-only tasks. Require final artifacts: summary, changed files, checks, risks, and next actions. Do not allow auto-merge.

### Production-quality path

Use cloud work as an implementation or review lane. Require PR review, tests, CI, security review where relevant, and an explicit rollback plan.

## Stable Core

Delegation only works when the task boundary, review boundary, and recovery boundary are clear. Parallelism helps only when tasks are independent.

## Volatile Surface

Codex web/cloud UI, environment setup behavior, PR creation, internet-access controls, plan access, worktree behavior, and exact task lifecycle are product-specific and must be rechecked before writing command-level guidance.

## Obsolescence Watch

Review this chapter if cloud tasks gain new isolation models, new merge/PR automation, changed environment rules, changed secret handling, changed internet access behavior, or materially different pricing/usage economics.

## Evidence and Sources

- `openai.codex.cloud` — official OpenAI source for Codex cloud/background task delegation and PR creation positioning.
- `openai.codex.cloud_environments` — official OpenAI source for cloud task environment setup, setup scripts, cached containers, checks, diffs, and environment variables/secrets behavior.
- `openai.codex.cloud_internet_access` — official OpenAI source for default internet posture, allowlists, prompt-injection risk, exfiltration risk, and network controls.
- `openai.codex.workflows` — official OpenAI source for delegating longer implementation work to cloud tasks after local planning.
- `openai.codex.app` — official OpenAI source for app worktrees, parallel threads, and review/shipping surface categories.
- `openai.codex.remote_connections` — official OpenAI source for remote hosts, remote approvals, connected devices, screenshots, diffs, and remote session security boundaries.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: asynchronous work needs scope, isolation, review, and recovery.

## Related Topics

- vcb.chapter.codex_surfaces
- vcb.chapter.git_discipline
- vcb.chapter.reviewing_codex_output
- vcb.chapter.ci_noninteractive_github_actions
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.workflow.cloud_delegation
- vcb.codex.cloud

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.cloud_delegation_parallel_work -->
