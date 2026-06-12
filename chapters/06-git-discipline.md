<!-- VCB:BEGIN_TOPIC id=vcb.chapter.git_discipline version=0.1.0 -->
---
id: vcb.chapter.git_discipline
title: Chapter 6 — Git Discipline for Vibe Coders
type: chapter
chapter_number: 6
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2027-06-08'
review_cadence: annual

audiences:
- human
- ai_coach

applies_to:
- Git
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- local development workflows

source_status:
  official_openai: false
  official_vendor: true
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: CORE_ENGINEERING
  surface: STABLE
  pricing: STABLE

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
- vcb.shortcut.coding_on_main
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.unattended_long_runs

durable_principles:
- Git is the undo and review system for Codex work.
- Commit or otherwise checkpoint before large agent changes.
- Review the diff before accepting Codex output.
- Branches and worktrees isolate experiments and parallel agent work.
- Do not let multiple agents edit the same files without coordination.

likely_to_change:
- Codex app Git UI features
- worktree orchestration in Codex surfaces
- GitHub review integration details
- exact preferred commands in product UI

obsolete_when:
- Git is no longer the dominant repository/version-control substrate for Codex workflows.
- Codex offers an equivalent auditable checkpoint/review/rollback system that replaces Git for local software work.

related_topics:
- vcb.concepts.diff
- vcb.concepts.git_branch
- vcb.concepts.pull_request
- vcb.concepts.rollback
- vcb.concepts.recoverability
- vcb.chapter.sandboxing_and_approvals
- vcb.chapter.installing_and_configuring_codex
- vcb.workflow.reviewing_diffs
- vcb.workflow.git_discipline
- vcb.shortcut.coding_on_main
---

> Summary:
> Git is the practical undo system for Codex. Before broad agent work, checkpoint. During work, watch the diff. After work, commit only what you understand.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.git_discipline.human -->
## 1. For the Human: Plain-Language Concept

### Git is your undo system

Codex can change many files quickly. Git is how you keep those changes reviewable and reversible.

You do not need to become a Git wizard before using Codex. You do need a few instincts:

- know whether the working tree is clean,
- save a checkpoint before large changes,
- review the diff after Codex works,
- isolate risky work on a branch or worktree,
- do not accept changes you cannot explain.

The core rule:

```text
Before Codex makes a big mess, make sure Git can show you and undo the mess.
```

### The five Git ideas that matter first

| Git idea | Plain-language meaning | Why it matters with Codex |
|---|---|---|
| `git status` | What changed? What is staged? What is untracked? | Tells you whether the workspace is already dirty. |
| `git diff` | Exact line-by-line changes | Lets you review evidence instead of trusting the final summary. |
| Commit | Saved checkpoint | Lets you return to a known state. |
| Branch | Separate timeline | Lets Codex experiment without touching the main line. |
| Worktree | Separate folder tied to the same repo | Lets multiple branches/tasks exist side by side. |

You can learn more commands later. These ideas are enough to stop most agent-created chaos.

### Before Codex edits

Run or ask Codex to inspect:

```text
git status
```

Conceptually, you are asking:

- Are there already changes?
- Are those changes mine, Codex’s, or from another task?
- Are there untracked files that matter?
- Should I commit, stash, branch, or stop?

If the tree is dirty, do not blindly start another Codex task. Make Codex summarize the existing changes first.

### During Codex work

Keep changes small enough to review. A diff is like an X-ray: useful only if the image is readable. A 20-line diff can be inspected. A 2,000-line diff mixed across auth, UI, dependencies, and tests is a review problem.

Good Codex instructions:

```text
Keep this patch small.
Touch only the files needed.
Do not refactor unrelated code.
Do not add dependencies.
Stop and ask before editing auth, payments, migrations, deployment config, or secrets.
```

### After Codex works

Review in this order:

1. `git status` — what files changed?
2. `git diff` — what changed inside them?
3. tests/checks — what evidence supports the patch?
4. final message — what does Codex claim?

The final message comes last. It is a claim, not the evidence.

### Branches and worktrees

A branch is a separate code timeline. It lets Codex try something without directly changing the main line.

A worktree is a separate folder attached to the same repository. Worktrees are useful when you want multiple isolated tasks at once: one folder for a hotfix, one for a feature, one for a Codex experiment.

Use branches or worktrees when:

- the task is broad,
- multiple agents may work in parallel,
- the change is risky,
- the main branch auto-deploys,
- you want to review later.

### Commands to understand conceptually

Do not memorize these as magic spells. Understand what each kind of command does.

| Command family | What it is for | Warning |
|---|---|---|
| `git status` | see current state | safe read-only inspection |
| `git diff` | inspect changes | safe read-only inspection |
| `git restore` | restore files from index or a commit | can discard local file changes |
| `git reset` | move HEAD/index/working tree depending on mode | can rewrite local state; dangerous with `--hard` |
| `git revert` | create a new commit that reverses prior commits | usually safer for shared history |
| `git reflog` | find where refs used to point locally | useful for recovery, not a backup system |
| `git worktree` | manage multiple working directories | useful for parallel isolated work |

### What good Git discipline looks like

- Start from a clean or understood working tree.
- Create a branch for non-trivial work.
- Commit before broad Codex tasks.
- Keep diffs reviewable.
- Ask Codex to summarize changed files and checks.
- Review diff before commit or merge.
- Commit logical chunks, not the entire weekend.
- Use PRs for shared or production work.

### What bad Git discipline looks like

- Starting Codex with mystery local changes.
- Letting multiple agents edit the same files.
- Accepting a giant diff because “it says it finished.”
- Running destructive Git commands without understanding consequences.
- Working on `main` when `main` auto-deploys.
- Mixing feature work, formatting, dependency changes, and refactors in one patch.

<!-- VCB:END_SECTION id=vcb.chapter.git_discipline.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.git_discipline.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Make Git feel like a safety harness, not a gatekeeping ritual. Teach just enough Git to make Codex work inspectable, reversible, and shareable.

### Diagnose the Git state

Ask or infer:

- Is this a Git repository?
- Is the working tree clean?
- Are changes already present from the human or another agent?
- Is the user on `main` or a feature branch?
- Does `main` auto-deploy?
- Is there a remote/shared repo?
- Is this change small enough to review?
- Is rollback available if the patch fails?

### Explanation strategy

Use this intervention when the user is moving fast with no checkpoint:

```text
We are about to let Codex move faster than your ability to remember what changed. First make Git remember for you.
```

### Useful metaphors

- **Save point:** a commit is a video-game save before a boss fight.
- **Tracked changes:** a diff is Google Docs tracked changes for code.
- **Parallel timeline:** a branch is a safe timeline where the experiment can fail.
- **Clean table:** a clean working tree means you can tell which mess Codex made.

### Coaching tactics

For a dirty working tree:

```text
Stop. Ask Codex to summarize current changes before editing. Do not mix old human changes with new agent changes unless the user explicitly accepts that risk.
```

For broad tasks:

```text
Use a branch or worktree. Ask for a plan first. Keep checkpoints by milestone.
```

For large diffs:

```text
Do not review this as one blob. Ask Codex to split the diff by purpose: feature logic, tests, formatting, dependencies, config. Revert unrelated pieces.
```

For multiple agents:

```text
Do not let two agents edit the same files. Divide by branch/worktree or by analysis-only roles.
```

### Prompt patterns

#### Dirty tree inspection

```text
Before editing, inspect the Git state.

Run or report:
- current branch,
- whether the working tree is clean,
- changed files,
- untracked files,
- what each change appears to be for.

Do not modify files until I confirm how to handle the existing changes.
```

#### Small patch discipline

```text
Implement the smallest safe patch.

Constraints:
- keep the diff reviewable,
- avoid unrelated refactors,
- avoid dependency changes,
- stop before touching auth/payments/migrations/deployment/secrets,
- report changed files and checks run.
```

#### Recovery-first prompt

```text
A Codex change went wrong. Recovery first.

Do not edit yet.
Inspect Git state and propose the safest path to:
- preserve any useful work,
- discard accidental changes,
- avoid losing uncommitted human work,
- restore a known-good state.
Explain any destructive command before using it.
```

### Red flags to call out directly

- Dirty tree plus broad task.
- Working on `main` with auto-deploy.
- Codex wants to run `reset --hard` without explaining loss.
- Multiple agents editing the same files.
- Large diff with unrelated formatting or dependency changes.
- User wants to commit without reading the diff.
- Codex deleted tests or changed checks to make them pass.

### Exercises

1. Have the human predict what `git status` will show, then check.
2. Review a small diff and ask what changed in behavior.
3. Create a branch for one Codex task, then delete it after review.
4. Compare `restore`, `reset`, `revert`, and `reflog` conceptually without running destructive commands.

<!-- VCB:END_SECTION id=vcb.chapter.git_discipline.ai_coach -->

## Shortcut Reality

### The ideal practice

Use a branch or worktree for non-trivial Codex tasks, commit before large changes, review diffs, run checks, and merge only intentional work.

### What users often do instead

They work directly on `main`, skip commits, accept Codex output from the final summary, and only discover the problem when the app breaks.

### When the shortcut may be fine

Working directly on `main` may be fine when:

- it is a solo local project,
- there is no auto-deploy,
- the change is tiny,
- the human is supervising,
- there is a recent commit,
- no real users/data/money/secrets are affected.

### When the shortcut is a bad idea

Working directly on `main` or without checkpoints is a bad trade when:

- the repo is shared,
- `main` auto-deploys,
- the task is broad or risky,
- multiple agents are running,
- the change touches auth, payments, migrations, deployment, or secrets,
- there is no clear rollback path.

### Risk profile

- Probability of failure: medium for broad Codex tasks; lower for tiny supervised edits.
- Impact if it fails: low in local prototypes; high in shared/prod repos.
- Ease of recovery: high with commits/branches; low with uncommitted mixed changes.
- Blast radius: controlled by branch, worktree, auto-deploy coupling, and touched files.
- Skill needed to recover: low for clean branch restore; high for mixed uncommitted changes and destructive reset mistakes.
- Hidden cost: lost work, confusing history, review fatigue, accidental deploys, and merge conflicts.

### Minimum guardrails

- Run or ask for `git status` first.
- Commit or stash unrelated existing work.
- Use a branch for broad tasks.
- Keep diffs small.
- Do not let agents overlap on the same files.
- Review changed files before accepting.
- Avoid destructive Git commands unless the user understands the consequence.

### Recovery plan

If Git discipline breaks down:

1. Stop Codex edits.
2. Inspect status and diff.
3. Save useful work if possible.
4. Separate unrelated changes.
5. Restore accidental files or revert bad commits.
6. Use reflog only as a recovery aid, not as a normal workflow.
7. Restart on a clean branch or worktree.

### AI coach guidance

```text
Working on main is not automatically wrong. In this context it is wrong because main is shared/auto-deployed and this task is broad. Make a branch or worktree first, then let Codex work there.
```

## Budget and Constraint Notes

### Cheapest reliable path

Git discipline is cheap. A checkpoint and diff review cost less than a long recovery session. Constrained users should use Git to avoid wasting Codex usage on cleanup.

### Fastest high-usage path

Use branches/worktrees aggressively. High-throughput users can run multiple attempts only when each attempt is isolated and reviewable.

### Low-attention path

Low-attention Codex work requires Git isolation. Use a branch/worktree, forbid sensitive areas, require a final report, and review before merge.

### Production-quality path

Use branches, PRs, tests/checks, diff review, independent review where useful, deployment controls, and explicit rollback procedures.

## Stable Core

- Git makes Codex changes visible and recoverable.
- Review the diff, not the final summary.
- Checkpoint before broad work.
- Branches and worktrees reduce blast radius.
- Shared/production work needs stricter Git discipline than solo prototypes.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Git concepts are stable, but Codex app Git features, worktree orchestration, GitHub integration details, branch UI, and automated PR behavior are volatile. Re-check official Codex and GitHub docs before writing surface-specific Git instructions.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- Codex introduces a new default checkpoint/rollback system.
- Codex app worktree behavior changes materially.
- GitHub PR review integration changes merge/review assumptions.
- Git itself changes semantics around status, diff, restore, reset, revert, reflog, branch, or worktree in ways that affect guidance.

## Evidence and Sources

- `git.docs.status` — Official source for working tree/index status display.
- `git.docs.diff` — Official source for diff as changes between working tree, index, commits, trees, blobs, or files.
- `git.docs.branch_book` — Official Pro Git source for branching as diverging from the main line of development.
- `git.docs.commit` — Official source for commits as stored project state/checkpoints.
- `git.docs.restore` — Official source for restoring working tree or index contents from a tree.
- `git.docs.reset` — Official source for reset behavior and local history/state movement.
- `git.docs.revert` — Official source for revert as new commits that reverse previous commits.
- `git.docs.reflog` — Official source for reference logs recording prior branch/reference positions.
- `git.docs.worktree` — Official source for linked working tree management.
- `github.docs.pull_requests` — Official GitHub source for PR review containers.
- `vcb.synthesis.stable_engineering_practice` — VCB synthesis for Git-as-control-loop framing; not a product-behavior source.

## Related Topics

- `vcb.concepts.diff`
- `vcb.concepts.git_branch`
- `vcb.concepts.pull_request`
- `vcb.concepts.rollback`
- `vcb.concepts.recoverability`
- `vcb.chapter.sandboxing_and_approvals`
- `vcb.chapter.installing_and_configuring_codex`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.git_discipline`
- `vcb.shortcut.coding_on_main`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.git_discipline -->
