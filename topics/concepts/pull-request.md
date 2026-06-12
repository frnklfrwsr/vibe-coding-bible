<!-- VCB:BEGIN_TOPIC id=vcb.concepts.pull_request version=0.1.0 -->
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
id: vcb.concepts.pull_request
title: Pull Request
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
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.manual_testing_only
durable_principles:
- pull requests package proposed changes for review
- checks and diffs are evidence inside a PR
- a PR is not proof that a change is safe
likely_to_change:
- GitHub pull request UI
- Codex GitHub review integration details
- automation and check surfaces
obsolete_when:
- code review systems stop using PR-like proposed-change containers
related_topics:
- vcb.concepts.diff
- vcb.concepts.git_branch
- vcb.concepts.recoverability
- vcb.concepts.rollback
- vcb.workflow.reviewing_diffs
- vcb.workflow.github_pr_review
---

> Summary:
> A pull request is a proposed change with review. It gives humans, checks, and AI reviewers a shared place to inspect the diff before merging.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.pull_request.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A **pull request** is a proposed change to a codebase.

It usually says:

- here is what I changed,
- here are the commits,
- here is the diff,
- here are the checks,
- please review before merging.

A pull request is not the same as shipping. It is the review container before merge.

### Why it matters

Codex can produce code quickly. A pull request gives you a place to slow down just enough to inspect it.

It helps separate “Codex made a change” from “we accepted this change into the main codebase.”

### The mental model

A pull request is a proposal on the table. The diff is the evidence. Tests and checks are supporting evidence. Review comments are the debate. Merge is the decision.

### What good looks like

A good pull request:

- has a focused scope,
- explains the user-facing change,
- links to issue/task context if available,
- includes tests or manual verification notes,
- has a readable diff,
- makes risky areas obvious,
- can be rolled back if needed.

### What bad looks like

A bad pull request:

- mixes unrelated features,
- includes broad formatting churn,
- adds dependencies without explanation,
- removes tests,
- says “fixed stuff,”
- hides auth, data, payment, or deployment changes in a large diff.

### Minimal example

```text
Title: Fix empty-state message on dashboard
Scope: UI copy only
Checks: npm test -- dashboard empty state
Risk: low; no auth/data/deployment changes
```

That is easier to review than:

```text
Title: Update app
Scope: many things
Checks: not run
Risk: unknown
```

### Checklist

Before merging a PR:

- Read the changed file list.
- Review the diff.
- Check whether tests, lint, typecheck, or build ran.
- Look at failing checks before trusting passing ones.
- Verify risky domains: auth, payments, data, secrets, migrations, deployment.
- Confirm rollback path.
<!-- VCB:END_SECTION id=vcb.concepts.pull_request.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.pull_request.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the pull request as the review boundary for AI-generated changes. The PR bundles context, diff, checks, discussion, and merge decision.

### Diagnose the human’s current model

Ask:

- Is this change ready for review or still draft work?
- What behavior changed?
- What checks ran?
- What files are riskiest?
- Does the PR mix unrelated tasks?
- Is merge blocked by failed checks or unresolved risk?

### Explanation strategy

For beginners, define PR as “a proposed change with a review page.” Then explain that the PR is useful because it forces the change to be visible before it lands.

### Useful metaphors

- Proposal on the table.
- Review packet.
- Gate before the main road.

### Coaching tactics

Help the human write a PR summary that is evidence-based, not marketing. Include changed behavior, files/risk areas, checks run, known gaps, and rollback notes.

### Prompt patterns

```text
Draft a pull request summary for this diff.
Include: user-facing behavior, files changed, tests/checks run, risks, rollback plan, and anything reviewers should inspect closely.
```

```text
Review this pull request as a second signal.
Prioritize P0/P1 correctness, security, data, auth, dependency, and regression risks.
Avoid style nitpicks unless they hide real risk.
```

### Red flags to call out directly

- PR says “all set” but checks did not run.
- Draft-quality work is marked ready.
- PR includes unrelated formatting and behavior changes.
- Review ignores the Files changed tab.
- PR touches production-sensitive code without tests or rollback.

### Exercises

Ask the human to turn a vague PR summary into a useful one:

```text
Bad: Updated dashboard.
Better: Adds empty/loading/error states to dashboard; changes DashboardPage and DashboardEmptyState; tests empty state; no data/auth changes; rollback by reverting PR.
```
<!-- VCB:END_SECTION id=vcb.concepts.pull_request.ai_coach -->

## Shortcut Reality

### The ideal practice

Use pull requests for non-trivial changes, especially in shared or production repositories.

### What users often do instead

Solo builders often merge directly or accept Codex changes locally without a PR.

### When the shortcut may be fine

Skipping a PR can be fine for local prototypes, private scripts, small one-person repos, and disposable experiments.

### When the shortcut is a bad idea

Skipping a PR is a bad idea for shared repos, production systems, auth, payments, migrations, data deletion, security-sensitive work, or large AI-generated diffs.

### Risk profile

- Probability of failure: lower when PR review and checks are meaningful.
- Impact if it fails: depends on blast radius.
- Ease of recovery: better when PRs are focused and revertable.
- Blast radius: PRs reveal blast radius but do not reduce it by themselves.
- Skill needed to recover: rises when PRs mix unrelated changes.
- Hidden cost: poor PR hygiene makes future debugging harder.

### Minimum guardrails

- Use draft PRs for work in progress.
- Include changed behavior and checks run.
- Review Files changed.
- Do not merge failed checks without a clear reason.
- Ask for a fresh review on risky AI-generated changes.

### Recovery plan

If a merged PR breaks something, identify the PR, inspect changed files and commits, revert or hotfix according to risk, and update the PR template or `AGENTS.md` if Codex repeated a mistake.

### AI coach guidance

Treat Codex PR review as a second signal, not approval. Human merge responsibility remains with the project owner.

## Budget and Constraint Notes

### Cheapest reliable path

For solo work, create a lightweight PR or at least use the PR-style checklist: summary, diff, checks, risks, rollback.

### Fastest high-usage path

Use Codex implementation plus independent PR review for medium/high-risk changes.

### Low-attention path

A PR is useful for review-later workflows, but only if the final report, checks, and risk notes are explicit.

### Production-quality path

Production PRs need checks, meaningful review, rollback plan, and clear ownership of risky areas.

## Stable Core

- A PR is a proposed change, not proof.
- The diff and checks inside the PR are evidence.
- Focused PRs are easier to review and revert.

## Volatile Surface

- GitHub PR UI and tabs.
- Codex GitHub review command names and product integration details.
- CI/check provider interfaces.

## Obsolescence Watch

Review if GitHub or Codex changes PR review surfaces, automatic review behavior, or merge/check semantics.

## Evidence and Sources

- `github.docs.pull_requests`: official GitHub documentation for PRs as proposed changes, review, checks, files changed, and merge status.
- `openai.codex.best_practices`: official OpenAI validation/review anchor for Codex workflows.
- `vcb.blueprint.v1`: governing review and human/AI coach structure.

## Related Topics

- `vcb.concepts.diff`
- `vcb.concepts.git_branch`
- `vcb.concepts.rollback`
- `vcb.concepts.recoverability`
- `vcb.workflow.github_pr_review`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.pull_request -->
