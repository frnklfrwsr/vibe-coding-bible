<!-- VCB:BEGIN_TOPIC id=vcb.concepts.git_branch version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-08'
review_cadence: annual
audiences:
- human
- ai_coach
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- Human software work
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
- disposable_prototype
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
id: vcb.concepts.git_branch
title: Git Branch
type: concept
next_review_due: '2027-06-08'
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
stability:
  principle: CORE_ENGINEERING
  surface: STABLE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.coding_on_main
- vcb.shortcut.unattended_long_runs
durable_principles:
- branches isolate code timelines
- branches improve review and rollback
- branches do not remove the need to review diffs and checks
likely_to_change:
- exact GitHub, Codex, and IDE branch UI
- worktree and cloud delegation product behavior
obsolete_when:
- version-control systems stop using branch-like isolated lines of development
related_topics:
- vcb.concepts.diff
- vcb.concepts.recoverability
- vcb.concepts.rollback
- vcb.concepts.pull_request
- vcb.workflow.feature_slicing
---

> Summary:
> A Git branch is a parallel line of development. Use branches to let Codex work without immediately risking the main code path.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.git_branch.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A **Git branch** is a parallel timeline for your code.

Your main timeline usually holds the stable version. A branch lets you try a change somewhere else. If the branch works, you can merge it back. If it fails, you can abandon it.

### Why it matters

Branches turn Codex work into a proposal instead of an immediate change to the main path.

This matters because Codex can edit many files quickly. A branch gives you a safer place to inspect, test, and reject work.

### The mental model

Imagine writing a new chapter in a copy of a document. The original stays safe while you experiment. Later you decide whether to copy the changes back.

### What good looks like

Good branch discipline:

```text
main stays stable.
feature branch contains one task.
diff is reviewed.
checks run.
pull request proposes merge.
```

### What bad looks like

Bad branch discipline:

```text
Everything happens on main.
Several unrelated Codex tasks are mixed together.
The app auto-deploys before review.
Rollback is unclear.
```

### Minimal example

```text
main
  └── feature/add-login-error-message
```

The branch name tells you the job. The branch should contain only that job.

### Checklist

Use a branch when:

- Codex will edit more than one file.
- The change may take multiple attempts.
- The work might be reviewed later.
- The repository is shared.
- The branch may become a pull request.
- Auto-deploy from main exists.
<!-- VCB:END_SECTION id=vcb.concepts.git_branch.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.git_branch.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach branches as isolation and recoverability, not as Git trivia.

### Diagnose the human’s current model

Ask:

- Are you on main or a task branch?
- Is the working tree clean?
- Does this branch contain one task or several?
- Is auto-deploy tied to this branch?
- Are multiple agents editing the same files?

### Explanation strategy

Start with “parallel timeline.” Then explain that a branch only helps if the task is scoped and reviewed.

### Useful metaphors

- Alternate timeline.
- Scratch copy.
- Workshop bench away from the sales floor.

### Coaching tactics

If the user is on main and the task is non-trivial, push for a branch before edits. If they refuse, reduce blast radius: commit first, keep the diff small, disable auto-deploy if relevant.

### Prompt patterns

```text
Before editing, confirm the current branch and whether the working tree is clean.
If this is main, recommend a branch unless the task is tiny and local-only.
```

```text
Keep this branch focused on one task.
Do not mix formatting, refactors, dependencies, and behavior changes unless explicitly requested.
```

### Red flags to call out directly

- Working directly on main with auto-deploy.
- Multiple Codex sessions editing the same files.
- A branch name that no longer matches the work.
- Unrelated changes mixed into the branch.
- Branch contains migrations, auth changes, and UI refactor in one bundle.

### Exercises

Ask the human to name a branch for each task:

1. Fix login error message.
2. Add payment webhook retry.
3. Refactor dashboard components.

Then ask what should not be included in each branch.
<!-- VCB:END_SECTION id=vcb.concepts.git_branch.ai_coach -->

## Shortcut Reality

### The ideal practice

Use a branch for non-trivial work, especially with Codex, teams, or production deployment.

### What users often do instead

Solo builders often work directly on main because it feels faster.

### When the shortcut may be fine

Working on main can be fine for solo local projects with no auto-deploy, frequent commits, and small reversible changes.

### When the shortcut is a bad idea

It is a bad idea with shared repos, production auto-deploy, multiple agents, migrations, auth, payments, or large diffs.

### Risk profile

- Probability of failure: medium when main accumulates unrelated Codex edits.
- Impact if it fails: low locally; high with auto-deploy or shared team workflows.
- Ease of recovery: better with branches and commits.
- Blast radius: branch reduces code-path blast radius but not secret/data blast radius by itself.
- Skill needed to recover: rises when changes are mixed and uncommitted.
- Hidden cost: branchless work makes review and rollback messier.

### Minimum guardrails

- Commit before Codex starts.
- Use a branch for multi-file work.
- Keep one task per branch.
- Do not let multiple agents edit overlapping files.
- Review the diff before merging.

### Recovery plan

If work on main got messy, stop. Inspect changed files, commit or stash intentional work if needed, then separate unrelated changes into branches or roll back accidental changes.

### AI coach guidance

Do not turn branch advice into a lecture. Explain the practical benefit: “This lets us reject Codex’s work without damaging main.”

## Budget and Constraint Notes

### Cheapest reliable path

A branch is cheap protection. It reduces rework and makes review easier.

### Fastest high-usage path

High-throughput users should use branches or worktrees for parallel Codex attempts.

### Low-attention path

Unattended Codex work should not run directly on main. Use branch/worktree isolation and final reports.

### Production-quality path

Production repositories should treat branches and pull requests as default review boundaries.

## Stable Core

- Branches isolate work.
- Branches improve review and rollback.
- Branches do not replace diff review, tests, or deployment controls.

## Volatile Surface

- GitHub branch UI.
- Codex branch/worktree features.
- IDE branch controls.
- Hosting branch-deploy rules.

## Obsolescence Watch

Review if the dominant version-control workflow changes away from branch-like isolated lines of development.

## Evidence and Sources

- `git.docs.glossary`: official Git glossary definition of branch as a line of development.
- `git.docs.branch_book`: official Git source for branch/timeline framing and branch-based work isolation.
- `openai.codex.best_practices`: official validation/review anchor for Codex workflows.

## Related Topics

- `vcb.concepts.diff`
- `vcb.concepts.pull_request`
- `vcb.concepts.rollback`
- `vcb.concepts.recoverability`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.git_branch -->
