<!-- VCB:BEGIN_TOPIC id=vcb.codex.github_review version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
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
id: vcb.codex.github_review
title: Codex GitHub PR Review
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- GitHub
- Pull requests
- Codex Cloud
- Code review
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_codex_review_as_approval
- vcb.shortcut.skipping_pr_review
- vcb.shortcut.accepting_diff_without_review
durable_principles:
- Codex review is a review signal, not merge approval
- PR review must be risk-focused and repository-specific
- human review remains necessary for product intent, tradeoffs, and final responsibility
likely_to_change:
- GitHub invocation mechanics
- automatic review settings
- review severity categories
- AGENTS.md review customization behavior
obsolete_when:
- official docs no longer support Codex GitHub review or PR review behavior changes
  materially
related_topics:
- vcb.chapter.github_pr_review_with_codex
- vcb.chapter.reviewing_codex_output
- vcb.codex.cloud
- vcb.concepts.pull_request
- vcb.concepts.diff
- vcb.safety.security_review
---

> Summary:
> Codex GitHub PR review is an additional review pass on pull requests, useful for high-priority regressions, missing tests, and risky behavior changes.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.github_review.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Codex can review a GitHub pull request and leave findings in the PR workflow. It is like adding another reviewer that can scan the diff and repository guidance. It is not a human approval and it is not a guarantee that the PR is safe.

### Why it matters

PR review matters because many AI-generated mistakes hide in diffs that look reasonable. Codex can catch a different class of issue than the implementer, especially when given clear review guidance.

### The mental model

Codex review is a smoke alarm, not the fire department and not a building inspector. If it rings, investigate. If it is silent, still inspect risky work.

### What good looks like

Good use: ask for Codex review on a PR that touches shared logic, tests, security-sensitive code, or dependencies, then triage findings by severity before merging.

### What bad looks like

Bad use: treat “Codex had no comments” as approval to merge production code without human diff review or checks.

### Minimal example

Example: before merging a billing-related PR, ask Codex to review for missing tests, changed auth/payment behavior, dependency changes, and backward-compatibility risks.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.github_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.github_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach Codex PR review as independent risk detection with scoped instructions and human triage.

### Diagnose the human’s current model

- What risk area should the reviewer focus on?
- Does AGENTS.md include review guidance?
- Are checks passing independently of Codex comments?
- Is the human using Codex review as an excuse not to read the diff?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

Codex PR review is a second pair of eyes. It helps most when told what kind of damage to look for.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Review this PR for blocking issues only. Focus on behavior regressions, missing tests, auth/security/data risks, new dependencies, and deployment/migration impact. Ignore style nits unless they hide real risk.
```

### Red flags to call out directly

- Codex review treated as merge approval
- automatic reviews producing noise
- review comments without severity triage
- security-sensitive PRs with no human review

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.github_review.ai_coach -->

## Shortcut Reality

### The ideal practice

Use Codex review as an additional signal before human merge decisions, especially for non-trivial or risky PRs.

### What users often do instead

Users often accept a clean Codex review as proof that the PR is safe.

### When the shortcut may be fine

This may be acceptable for tiny docs or prototype-only changes with passing checks and easy rollback.

### When the shortcut is a bad idea

It is bad for auth, payments, migrations, production data, deployments, or public API changes.

### Risk profile

- Probability of failure: Low to medium failure probability for simple PRs, high impact if review silence hides security or data behavior
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- keep human diff review
- require CI checks
- tell Codex review what risks to inspect
- triage review comments
- do not merge solely because Codex is quiet

### Recovery plan

Reopen or revert the PR, ask Codex and a human for focused review of the escaped issue, add a regression test or review guideline, and update AGENTS.md if the failure was predictable.

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

- Codex review is a review signal, not merge approval
- PR review must be risk-focused and repository-specific
- human review remains necessary for product intent, tradeoffs, and final responsibility

## Volatile Surface

- GitHub invocation mechanics
- automatic review settings
- review severity categories
- AGENTS.md review customization behavior

## Obsolescence Watch

- official docs no longer support Codex GitHub review or PR review behavior changes materially

## Evidence and Sources

- `openai.codex.github_review` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.use_cases.github_code_reviews` — official source anchor for this card's current Codex feature behavior.
- `github.docs.pull_requests` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.github_pr_review_with_codex`
- `vcb.chapter.reviewing_codex_output`
- `vcb.codex.cloud`
- `vcb.concepts.pull_request`
- `vcb.concepts.diff`
- `vcb.safety.security_review`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.github_review -->
