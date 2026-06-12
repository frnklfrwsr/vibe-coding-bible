<!-- VCB:BEGIN_TOPIC id=vcb.concepts.recoverability version=0.1.0 -->
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
id: vcb.concepts.recoverability
title: Recoverability
type: concept
next_review_due: '2027-06-08'
source_status:
  official_openai: false
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
- vcb.shortcut.accepting_diff_without_review
durable_principles:
- make fast work reversible before increasing speed
- risk is lower when rollback is known and cheap
- Git checkpoints and branches improve recoverability for code changes
likely_to_change:
- exact Git client UI for restore, reset, revert, and branch actions
- Codex UI support for checkpoints and worktrees
obsolete_when:
- AI-assisted development no longer produces reversible code changes or versioned
  artifacts
related_topics:
- vcb.concepts.rollback
- vcb.concepts.git_branch
- vcb.concepts.diff
- vcb.concepts.blast_radius
- vcb.concepts.pull_request
---

> Summary:
> Recoverability means how hard it is to undo a mistake. Before moving fast, make the work easier to recover.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.recoverability.human -->
## 1. For the Human: Plain-Language Concept

### What this means

**Recoverability** means: if this goes wrong, how hard is it to undo?

A risky shortcut becomes less dangerous when recovery is easy.

### Why it matters

Vibe coding is fast. Fast is useful only if mistakes are reversible.

If Codex breaks a prototype branch, you can usually recover. If Codex deletes production data, leaks an API key, or charges customers incorrectly, recovery may be slow, expensive, or impossible.

### The mental model

Ask one question before moving fast:

```text
Can we make this reversible first?
```

### What good looks like

Easy to recover:

- Bad CSS change on a branch.
- Broken local prototype.
- Generated throwaway code.
- A feature guarded by a feature flag.
- A committed change that can be reverted.

Hard to recover:

- Deleted production data.
- Leaked API key.
- Broken production migration.
- Incorrect customer charges.
- Public API behavior changed without warning.

### What bad looks like

Bad recoverability sounds like:

```text
I do not have a commit, I do not know what changed, and I already deployed it.
```

At that point the problem is no longer just code. It is forensic recovery.

### Minimal example

Before a Codex task:

```text
Good: create branch → ask Codex to change one thing → review diff → run check → merge later.
Bad: edit main → accept large diff → auto-deploy → notice users are broken.
```

### Checklist

Before letting Codex make a risky change:

- Is the working tree clean?
- Is there a commit or branch checkpoint?
- Can you identify all changed files?
- Can you revert the code change?
- Is any data migration reversible?
- Are real secrets involved?
- Is auto-deploy enabled?
<!-- VCB:END_SECTION id=vcb.concepts.recoverability.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.recoverability.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach recoverability before lecturing about best practices. The fastest useful intervention is often “commit first” or “use a branch.”

### Diagnose the human’s current model

Ask:

- What is the rollback path if this fails?
- Is the work committed or isolated?
- Does the change touch mutable data or external systems?
- Would reverting code undo all side effects?
- Who needs to be notified if recovery fails?

### Explanation strategy

Make recoverability concrete. Do not say “be careful.” Say which condition makes recovery easy or hard.

### Useful metaphors

- Save point in a game.
- Undo stack.
- Trail of breadcrumbs out of the forest.

### Coaching tactics

For small tasks, suggest a Git checkpoint. For larger tasks, suggest branch/worktree plus tests. For data/security tasks, add backups, fake credentials, staging, or manual approval.

### Prompt patterns

```text
Before editing, tell me how we will recover if this change fails.
Include Git rollback, data rollback, and deployment rollback separately.
```

```text
Make this task more recoverable before implementing it.
Use a branch/checkpoint, keep the diff small, and avoid irreversible changes.
```

### Red flags to call out directly

- No clean checkpoint.
- Production data mutation.
- Secret exposure.
- Auto-deploy from current branch.
- Codex proposes a migration without rollback discussion.
- User wants to keep adding patches after a bad shortcut without first recovering.

### Exercises

Ask the human to classify recovery difficulty for each:

1. Revert a button text change.
2. Revert a production database migration.
3. Rotate a leaked API key.
4. Undo a bad commit on a feature branch.

Then identify the guardrail that would have made each easier.
<!-- VCB:END_SECTION id=vcb.concepts.recoverability.ai_coach -->

## Shortcut Reality

### The ideal practice

Make work recoverable before moving fast: branch, commit, scope, verify, and document rollback.

### What users often do instead

Users often move fast first, then discover they do not know what changed or how to undo it.

### When the shortcut may be fine

Low recoverability may be acceptable in disposable projects where nothing important can be lost.

### When the shortcut is a bad idea

It is a bad idea when the task touches real data, secrets, production deployment, billing, auth, or customer-visible behavior.

### Risk profile

- Probability of failure: depends on task ambiguity and verification.
- Impact if it fails: depends on blast radius.
- Ease of recovery: the core variable.
- Blast radius: larger blast radius demands higher recoverability.
- Skill needed to recover: rises sharply with data/security/production incidents.
- Hidden cost: poor recoverability turns small bugs into long investigations.

### Minimum guardrails

- Commit before change.
- Use a branch for risky work.
- Keep the diff small.
- Avoid real secrets and production data during experiments.
- Ask for a rollback plan before migrations, auth, payments, and deployment changes.

### Recovery plan

If recoverability is poor, pause implementation. Identify changed files, current environment, affected data, and available backups/checkpoints. Use `vcb.concepts.rollback` before asking for new feature work.

### AI coach guidance

Use this phrase: “Can we make this reversible before moving fast?” It is direct and avoids moralizing.

## Budget and Constraint Notes

### Cheapest reliable path

A Git checkpoint is the cheapest high-leverage guardrail. It costs little and saves a lot of recovery time.

### Fastest high-usage path

High-throughput users can delegate more aggressively when every task is isolated in branches/worktrees and reviewable later.

### Low-attention path

Low-attention work requires strong recoverability: branch/worktree, no real secrets, clear final report, and review before merge.

### Production-quality path

Production recovery must include code rollback, deployment rollback, database/data rollback, feature flag strategy, and monitoring.

## Stable Core

- Fast work is safer when reversible.
- Git improves code recoverability but does not automatically undo data or external side effects.
- Recovery difficulty should shape shortcut tolerance.

## Volatile Surface

- Git client UI.
- Codex checkpoint/worktree features.
- Hosting rollback controls.
- Database backup and migration tooling.

## Obsolescence Watch

Review if Codex or hosting platforms introduce reliable automatic rollback for code, data, and deployment side effects. Until then, assume recovery must be designed.

## Evidence and Sources

- `git.docs.revert`: official Git documentation on revert as a new commit that reverses previous changes.
- `git.docs.restore`: official Git documentation on restoring files.
- `git.docs.reset`: official Git documentation on moving local state/history.
- `vcb.blueprint.v1`: governing risk-managed shortcut policy.

## Related Topics

- `vcb.concepts.rollback`
- `vcb.concepts.git_branch`
- `vcb.concepts.blast_radius`
- `vcb.concepts.diff`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.recoverability -->
