<!-- VCB:BEGIN_TOPIC id=vcb.concepts.rollback version=0.1.0 -->
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
id: vcb.concepts.rollback
title: Rollback
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
- rollback is a planned path back to a known-good state
- code rollback and data rollback are different
- do not use destructive recovery commands casually
likely_to_change:
- exact Git commands shown by product UIs
- hosting rollback mechanics
- database migration rollback tooling
obsolete_when:
- software delivery systems guarantee safe automatic recovery across code, data, secrets,
  and deployment side effects
related_topics:
- vcb.concepts.recoverability
- vcb.concepts.git_branch
- vcb.concepts.diff
- vcb.concepts.blast_radius
- vcb.concepts.pull_request
---

> Summary:
> A rollback is a controlled return to a known-good state after a bad change. It is not just “undo”; it is a recovery plan.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.rollback.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A **rollback** means going back to a known-good state after a change goes wrong.

It can mean:

- undoing local file edits,
- creating a new commit that reverses a bad commit,
- deploying the previous version,
- restoring data from backup,
- disabling a feature flag,
- rotating a leaked secret.

Those are different recovery paths. Do not collapse them into one vague “undo.”

### Why it matters

Codex can move faster than your ability to inspect every consequence. A rollback plan gives you a way out.

Rollback is most valuable before you need it. If you wait until production is broken, you may discover that code rollback does not undo a database change or leaked credential.

### The mental model

Rollback is the emergency exit. You do not install the exit after the building is on fire.

### What good looks like

Good rollback planning:

```text
If this branch breaks, we revert the commit.
If the deploy breaks, we redeploy the previous release.
If the migration breaks, we restore from backup or run the tested down migration.
If the feature misbehaves, we turn off the feature flag.
```

### What bad looks like

Bad rollback planning:

```text
We will figure it out if something goes wrong.
```

That is not a plan. That is a wish.

### Minimal example

A safe local recovery path:

```text
1. Commit before Codex starts.
2. Let Codex edit on a branch.
3. Review the diff.
4. If bad, discard the branch or revert the commit.
```

A dangerous path:

```text
1. Let Codex edit main.
2. Auto-deploy.
3. Apply a database migration.
4. Notice the app is broken.
5. Discover no backup or down migration exists.
```

### Checklist

Before accepting risky work, answer:

- What is the known-good state?
- How do we return to it?
- Does code rollback also undo data changes?
- Are secrets or external systems involved?
- Is this rollback tested, or only imagined?
- Who decides when to roll back?
<!-- VCB:END_SECTION id=vcb.concepts.rollback.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.rollback.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach rollback as a concrete recovery path, not a generic comfort word. Separate code rollback, data rollback, deployment rollback, and secret recovery.

### Diagnose the human’s current model

Ask:

- What exactly would be rolled back?
- Is the rollback a Git operation, deploy operation, database operation, or credential operation?
- Is the working tree clean?
- Are there uncommitted changes mixed with Codex output?
- Would rollback preserve or destroy work the human wants to keep?

### Explanation strategy

For beginners, start with “rollback means going back to a known-good state.” Then explain that different kinds of changes require different rollback paths.

### Useful metaphors

- Emergency exit.
- Save point.
- Time machine that only works for the things it recorded.

### Coaching tactics

If the user is panicking, stop new edits. Ask Codex to inspect `git status`, changed files, recent commits, and deployment/data state before proposing commands.

Do not casually recommend destructive commands. Explain consequences before reset, restore, or deleting files.

### Prompt patterns

```text
A shortcut went wrong. Help me recover.
Before editing, inspect git status and recent changes.
Separate intended changes from accidental changes.
Propose the safest rollback path and explain what each step preserves or discards.
```

```text
Before implementing this migration, give me a rollback plan.
Separate code rollback, database rollback, deployment rollback, and user-impact monitoring.
```

### Red flags to call out directly

- User wants to run reset/restore/delete commands without understanding what will be lost.
- Migration has no tested rollback or backup.
- Secrets may have leaked.
- Production deploy happened automatically from an unreviewed branch.
- Multiple agents changed overlapping files.

### Exercises

Ask the human to write rollback paths for:

1. A bad CSS change.
2. A bad API response shape.
3. A bad database migration.
4. A leaked API key.

Then explain why only the first two are mostly code rollback.
<!-- VCB:END_SECTION id=vcb.concepts.rollback.ai_coach -->

## Shortcut Reality

### The ideal practice

Define rollback before risky implementation. Test it when the stakes justify it.

### What users often do instead

Users often rely on Git as a magic undo button, then discover that Git does not undo production data changes, customer emails, payment charges, or leaked credentials.

### When the shortcut may be fine

For local-only code changes on a branch, a simple Git rollback path may be enough.

### When the shortcut is a bad idea

For migrations, production deploys, secrets, payments, auth, or data deletion, vague rollback is not enough.

### Risk profile

- Probability of failure: higher when work is broad, unattended, or poorly specified.
- Impact if it fails: high when production, data, or secrets are involved.
- Ease of recovery: high with known-good commits and isolated branches; low with irreversible side effects.
- Blast radius: determines how detailed rollback must be.
- Skill needed to recover: can become senior-level incident response.
- Hidden cost: recovery under pressure is slower and riskier than rollback planning.

### Minimum guardrails

- Commit before risky work.
- Use a branch or worktree.
- Know the previous good commit/release.
- Do not run destructive recovery commands without understanding consequences.
- For data changes, confirm backup or down-migration strategy.

### Recovery plan

If something broke, stop implementing. Inspect state, identify the bad change, choose the least destructive rollback, preserve evidence, and verify after rollback.

### AI coach guidance

When the user says “just undo it,” slow down. Ask what must be preserved and what can be discarded. Wrong rollback can lose good work.

## Budget and Constraint Notes

### Cheapest reliable path

For local work: commit first, branch, and keep changes small enough to revert.

### Fastest high-usage path

High-throughput work is acceptable only when each attempt is isolated and discardable.

### Low-attention path

Unattended work needs explicit rollback notes in the final report.

### Production-quality path

Production rollback must include release rollback, database strategy, monitoring, communication, and feature flags where appropriate.

## Stable Core

- Rollback should be planned before high-risk work.
- Code rollback, data rollback, deployment rollback, and secret recovery are separate.
- Git can help recover code; it does not automatically recover external side effects.

## Volatile Surface

- Exact Git client UI.
- Hosting rollback controls.
- Database migration tooling.
- Codex or platform checkpoint features.

## Obsolescence Watch

Review if platforms provide reliable end-to-end rollback across code, data, deploys, secrets, and external effects. Until then, keep rollback explicit.

## Evidence and Sources

- `git.docs.revert`: official Git documentation on reverting commits by recording new reversing commits.
- `git.docs.restore`: official Git documentation on file restoration.
- `git.docs.reset`: official Git documentation on state/history movement.
- `vcb.blueprint.v1`: governing recoverability and shortcut-risk requirements.

## Related Topics

- `vcb.concepts.recoverability`
- `vcb.concepts.git_branch`
- `vcb.concepts.diff`
- `vcb.concepts.blast_radius`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.rollback -->
