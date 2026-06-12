<!-- VCB:BEGIN_TOPIC id=vcb.workflow.github_pr_review version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex and vendor documentation anchors plus VCB maintainer synthesis for risk, budget, and coaching guidance
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
id: vcb.workflow.github_pr_review
title: GitHub PR Review with Codex Workflow
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- GitHub
- Pull requests
- Codex GitHub review
- Codex Cloud
- CI
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_codex_review_as_approval
- vcb.shortcut.skipping_pr_review
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.skipping_tests
durable_principles:
- AI PR review is a signal, not approval
- review guidance should be repository-specific
- human ownership remains at merge time
likely_to_change:
- GitHub integration mechanics
- automatic review settings
- severity labels
- review-comment UI
- repository rule configuration
obsolete_when:
- Codex PR review becomes a verified policy gate that can safely replace human merge review
related_topics:
- vcb.chapter.github_pr_review_with_codex
- vcb.codex.github_review
- vcb.workflow.reviewing_diffs
- vcb.workflow.codex_output_review
- vcb.concepts.pull_request
- vcb.concepts.ci
---

> Summary:
> GitHub PR review with Codex uses Codex as an additional reviewer for pull requests, not as merge authority.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.github_pr_review.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A pull request is a proposed change to a shared repository. Codex can review a PR and leave findings, but it is still an assistant. It helps you find risks; it does not become the person responsible for merging.

### Why it matters

PRs are where local experiments become shared code. A second review pass can catch regressions, missing tests, security-sensitive changes, and documentation gaps before merge.

### The mental model

Codex PR review is a second reviewer who is fast and tireless but not accountable. You still need an owner.

### What good looks like

Good: “Codex, review this PR for blocking issues only: regressions, missing tests, auth/security/data risks, dependency changes, and CI/deployment impact.”

### What bad looks like

Bad: Merging because Codex left no comments or because the automatic review looked quiet.

### Minimal example

On a PR that changes user roles, ask Codex to focus on authorization regressions, privilege escalation, missing negative tests, and migrations. Then read the diff and CI yourself.

### Checklist

- state the review focus
- confirm CI status independently
- triage Codex findings by severity
- read the diff yourself for high-risk areas
- do not treat silence as approval
- update AGENTS.md if repeated review guidance is needed
<!-- VCB:END_SECTION id=vcb.workflow.github_pr_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.github_pr_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use Codex PR review as risk amplification, not responsibility transfer.

### Diagnose the human’s current model

- What risk should the PR reviewer inspect?
- Are automatic reviews too noisy or too broad?
- Does AGENTS.md tell Codex how to review this repo?
- Are branch protection and required checks independent of Codex?
- Is the human still reading high-risk diff areas?

### Explanation strategy

Separate three roles: author, AI reviewer, merge owner. Codex can be an author or reviewer; it should not be the unchecked merge owner. For sensitive PRs, combine Codex review with required checks and human review.

### Useful metaphor

Codex PR review is a smoke alarm in the PR, not the key to the production door.

### Coaching tactics

- make review prompts severity-focused
- ask for blocking issues first and nits last or never
- add repository-specific review instructions to AGENTS.md
- require human triage for every high-severity finding
- rerun review after substantial fixes

### Prompt patterns

```text
@codex review
Focus on blocking issues only. Check behavior regressions, missing tests, authorization/security/data risks, new dependencies, CI/deployment impact, and backwards compatibility. Ignore style nits unless they hide real risk.
```

### Red flags to call out directly

- “Codex approved it” language
- automatic review comments treated as policy
- no human review on auth, payments, data, or deployment code
- Codex asked to fix its own high-risk finding without review
- PR merges with failed or skipped checks

### Exercises

- Ask the human to write a PR review focus for an auth change.
- Have them triage three Codex findings into block, fix-later, and noise.
- Ask them to define which branch rule should block merge independent of AI review.
<!-- VCB:END_SECTION id=vcb.workflow.github_pr_review.ai_coach -->

## Shortcut Reality

### The ideal practice

Use Codex PR review as an additional review signal inside a normal PR discipline: tests, CI, human review, and merge ownership.

### What users often do instead

Users treat a quiet Codex review as permission to merge.

### When the shortcut may be fine

This shortcut may be acceptable for low-risk docs or prototype PRs with easy rollback and passing checks.

### When the shortcut is a bad idea

It is bad for production changes, public API contracts, auth, data, secrets, dependencies, deployments, migrations, or security-sensitive code.

### Risk profile

- Probability of failure: Medium; review silence can hide gaps and noisy comments can distract from real risk.
- Impact if it fails: High when PRs affect shared systems or user data.
- Ease of recovery: Good when branch protection, revert strategy, and small PRs exist; poor when risky work is bundled.
- Blast radius: The merged PR and every downstream environment that consumes it.
- Skill needed to recover: Medium for normal code review; high for security, data, infrastructure, or incident follow-up.
- Hidden cost: False approval language, noisy automation, skipped ownership, and weaker review culture.

### Minimum guardrails

- keep required checks independent
- keep a human merge owner
- write focused review prompts
- treat Codex findings as findings, not orders
- rerun review or checks after changes

### Recovery plan

- Pause the merge.
- Resolve or explicitly dismiss each blocking finding.
- Ask for focused re-review after fixes.
- Add missing tests or branch rules.
- Revert quickly if a merged PR escapes review.

## Budget and Constraint Notes

### Cheapest reliable path

Use manual `@codex review` only on PRs above a risk threshold, with a narrow focus.

### Fastest high-usage path

Enable high-signal review patterns and repository guidance so Codex spends review attention on real blockers.

### Low-attention path

Low-attention PR review is only acceptable when CI, branch rules, and human final review remain in place.

### Production-quality path

Production PRs require passing checks, human review, risk-focused Codex review where useful, and a rollback plan.

### Prototype versus production

Prototype PRs can tolerate lighter review. Production PRs need clear ownership and independent gates.

### Maintenance phase

In maintenance, PR review must preserve ownership and gate quality; repeated AI-only approvals create hidden operational debt.

## Stable Core

- PR review is a merge gate
- AI findings are review inputs
- branch rules and CI should not depend on vibes

## Volatile Surface

- GitHub integration commands
- automatic review settings
- severity taxonomy
- GitHub review UI
- Codex account/plan behavior

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex GitHub review invocation changes
- automatic review behavior changes
- GitHub branch-protection rules or status-check semantics change

## Evidence and Sources

- `openai.codex.github_review` — Official OpenAI Codex GitHub review documentation.
- `openai.codex.use_cases.github_code_reviews` — Official OpenAI Codex use case for reviewing GitHub pull requests.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples for PR review.
- `github.docs.pull_requests` — Official GitHub pull-request documentation.
- `github.docs.branch_protection` — Official GitHub branch-protection documentation for required checks and merge controls.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.github_pr_review_with_codex`
- `vcb.codex.github_review`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.codex_output_review`
- `vcb.concepts.pull_request`
- `vcb.concepts.ci`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.github_pr_review -->
