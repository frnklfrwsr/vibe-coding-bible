<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.coding_on_main version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-12'
last_reviewed: '2026-06-12'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI/Codex guidance, Git/GitHub branch documentation, and VCB maintainer synthesis for risk-managed shortcut harm reduction
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
id: vcb.shortcut.coding_on_main
title: Coding on Main
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-12'
applies_to:
- Git
- branches
- pull requests
- shared repos
- production deploys
- Codex App
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- git
- recoverability
- branch discipline
risk_level:
  prototype: LOW_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- commit before edits
- create branch or worktree
- disable auto-deploy
- review before merge
shortcut_profiles:
- vcb.shortcut.coding_on_main
durable_principles:
- branch isolation preserves recovery options
- shared main branches need review and checks
- automation should not mutate the canonical line without a gate
likely_to_change:
- GitHub branch protection UI
- Codex worktree affordances
- repository deployment wiring
- team branching conventions
obsolete_when:
- main-branch mutation becomes automatically isolated, reversible, reviewed, and non-deploying by default
related_topics:
- vcb.concepts.git_branch
- vcb.concepts.rollback
- vcb.concepts.pull_request
- vcb.chapter.git_discipline
- vcb.workflow.github_pr_review
- vcb.constraints.recovery_budget
---

# Coding on Main

> Summary:
> Coding on main is letting Codex mutate the canonical branch directly instead of using a branch, worktree, or checkpointed review path.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.coding_on_main.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Coding on main means changes land directly on the branch everyone treats as the source of truth. In a solo toy project this may feel harmless. In a shared or deploying repo, it removes a major safety layer.

### Why it matters

Branches and worktrees make AI changes reviewable, revertable, and separable from production. Main-branch mutation can blend work in progress with release-ready code and make rollback harder.

### What good looks like

Good: "Create a branch or worktree, make the change, run checks, review diff, then merge intentionally."

### What bad looks like

Bad: "Let Codex edit main and push if it looks done."

### Minimal example

Before a generated fix in a shared repo, create `fix/login-timeout`, commit the starting point if needed, and keep deployment disabled until review passes.

### Checklist

- know whether the current branch is main
- commit or stash unrelated local work
- create a branch/worktree for mutation
- avoid auto-deploy from unreviewed edits
- merge only after review and checks

<!-- VCB:END_SECTION id=vcb.shortcut.coding_on_main.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.coding_on_main.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that branch isolation is the cheapest recoverability control for AI-generated changes.

### Diagnostic questions

- Is this repo shared, public, or deployed?
- Does main trigger CI, release, or deployment?
- Are there unrelated local changes?
- Is there a branch protection or PR expectation?
- What is the rollback path if Codex edits the wrong thing?

### Coaching tactics

- ask for branch/worktree before mutation
- require status check before edits
- keep production deploy paths out of unreviewed runs
- use PRs for shared or production work
- let solo disposable work use lighter branch discipline only when recovery is trivial

### Red flags

- direct edits on main in a shared repo
- auto-deploy from main with no review
- no Git checkpoint before a broad prompt
- uncommitted unrelated changes mixed with Codex work
- force-push or reset suggestions used to clean up confusion

### Prompt pattern

```text
Before editing, inspect branch and working tree status. If this is main or has unrelated changes, stop and propose a branch/worktree plan. Do not push, merge, or deploy.
```

<!-- VCB:END_SECTION id=vcb.shortcut.coding_on_main.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They work on main because it avoids branch setup and the change feels small.

### When the shortcut may be acceptable

Acceptable for a disposable local repo, a throwaway prototype, or a solo scratch project with no deployment, no collaborators, and a recent checkpoint.

### When it becomes a bad trade

Bad for shared repos, public apps, production deploys, CI-gated projects, dependency updates, migrations, or any work that requires review.

### Risk profile

- Probability: low for tiny solo edits; high when Codex generates broad changes.
- Impact: low for disposable local work; high when main deploys or is shared.
- Recoverability: medium with clean commits; poor with mixed uncommitted changes or auto-deploy.

### Blast radius

Coding on main can turn a local mistake into a shared branch problem, broken deploy, hidden release, or messy recovery path.

### Minimum guardrails

- commit before edits
- create branch or worktree
- disable auto-deploy
- review before merge

### Recovery plan

1. Stop editing and pushing.
2. Inspect branch and status.
3. Commit, stash, or copy out unrelated work safely.
4. Move the intended change to a branch if possible.
5. Revert or reset only with explicit ownership and backup.
6. Re-run checks before merging intentionally.

## Budget and Constraint Notes

### Cheapest reliable path

Creating a branch is cheaper than untangling shared main history.

### Fastest high-usage path

High-throughput workflows should automate branch/worktree setup rather than skipping it.

### Low-attention path

Low-attention mutation should never target main directly.

### Production-quality path

Production work requires branch isolation, PR review, checks, and deploy gates.

### Prototype versus production

Prototype main may be fine when disposable. Production main is a release boundary.

### Maintenance phase

Maintenance work benefits from branch names that capture the fix and make rollback obvious.

## Stable Core

- branch isolation preserves recovery options
- shared main branches need review and checks
- automation should not mutate the canonical line without a gate

## Volatile Surface

- GitHub branch protection UI
- Codex worktree affordances
- repository deployment wiring
- team branching conventions

## Obsolescence Watch

This card should be revised if:

- main-branch mutation becomes automatically isolated, reversible, reviewed, and non-deploying by default

## Evidence and Sources

- `openai.codex.best_practices` - Official OpenAI Codex guidance for validation, review, and safe task framing.
- `git.docs.branch_book` - Official Git documentation/book anchor for branch concepts.
- `git.docs.worktree` - Official Git documentation for multiple working trees and branch isolation.
- `github.docs.branch_protection` - Official GitHub documentation for protected branches and review/check requirements.
- `vcb.synthesis.stable_engineering_practice` - VCB maintainer synthesis for durable risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.concepts.git_branch`
- `vcb.concepts.rollback`
- `vcb.concepts.pull_request`
- `vcb.chapter.git_discipline`
- `vcb.workflow.github_pr_review`
- `vcb.constraints.recovery_budget`

<!-- VCB:STOP_RETRIEVAL reason="coding_on_main_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.coding_on_main -->
