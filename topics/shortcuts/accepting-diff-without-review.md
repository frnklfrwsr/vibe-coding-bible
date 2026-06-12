<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.accepting_diff_without_review version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex and GitHub review guidance plus VCB maintainer synthesis for risk-managed shortcut harm reduction
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
id: vcb.shortcut.accepting_diff_without_review
title: Accepting Diff Without Review
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-12'
applies_to:
- diff review
- pull requests
- Codex review panes
- local branches
- code review
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- review
- diffs
- pull requests
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- changed-files pass
- risky-area pass
- evidence pass
- explicit not-reviewed list
shortcut_profiles:
- vcb.shortcut.accepting_diff_without_review
durable_principles:
- generated code is still code review work
- review the diff by intent, risk, and evidence
- a summary is not a substitute for changed-file inspection
likely_to_change:
- Codex review UI affordances
- GitHub pull request review UI
- model diff summary behavior
- repository-specific review checklists
obsolete_when:
- generated diffs become automatically complete, formally verified, and reviewable without human or CI inspection
related_topics:
- vcb.workflow.reviewing_diffs
- vcb.workflow.codex_output_review
- vcb.workflow.github_pr_review
- vcb.concepts.diff
- vcb.concepts.pull_request
- vcb.failure.done_claim_without_evidence
---

# Accepting Diff Without Review

> Summary:
> Accepting diff without review is keeping Codex changes because the summary sounds good, without inspecting what changed and what evidence backs it.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.accepting_diff_without_review.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut happens when you accept a patch because Codex says it is done, or because the app seems to work, without reading the changed files.

### Why it matters

The diff is where unrelated edits, deleted checks, hidden dependencies, broad rewrites, and unsafe assumptions usually show up first. Review is cheaper before merge than after users find the mistake.

### What good looks like

Good: "Show changed files. For each file, explain why it changed, risk, and check evidence."

### What bad looks like

Bad: "The final answer says tests passed, so merge it."

### Minimal example

For a checkout fix, review not only the changed button but also any session, payment, environment, dependency, or test changes that appeared in the diff.

### Checklist

- inspect changed-file list
- classify each file as intended, support, or suspicious
- look for tests weakened or deleted
- inspect dependencies, config, auth, data, and CI changes
- tie acceptance to checks or explicit not-verified gaps

<!-- VCB:END_SECTION id=vcb.shortcut.accepting_diff_without_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.accepting_diff_without_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat the diff as the source of truth and the agent summary as a lead to verify.

### Diagnostic questions

- Which files changed?
- Which changes directly serve the request?
- Did any test, config, dependency, auth, or data path change?
- What evidence proves the risky behavior?
- What was not reviewed?

### Coaching tactics

- ask for a three-pass review: scope, risk, evidence
- request file-by-file intent before line-level reading
- require explicit notes for high-risk file categories
- separate Codex review comments from merge approval
- mark not-reviewed areas instead of pretending the review was complete

### Red flags

- final summary accepted as review
- broad diff with no changed-file table
- tests or checks altered without explanation
- dependency/config changes hidden in normal code edits
- PR review skipped because Codex already reviewed it

### Prompt pattern

```text
Review the diff before acceptance. Return changed files, intended/support/suspicious classification, risky areas, tests or checks run, not-reviewed areas, and blocking issues first.
```

<!-- VCB:END_SECTION id=vcb.shortcut.accepting_diff_without_review.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They accept the patch from the final summary, screenshot, or green-looking check without reading the changed files.

### When the shortcut may be acceptable

Acceptable for throwaway prototypes or local experiments where the diff is disposable and not merged into shared history.

### When it becomes a bad trade

Bad when the patch touches production, auth, payments, data, dependencies, CI, security boundaries, public docs, or a shared branch.

### Risk profile

- Probability: medium for small local patches; high for broad or generated diffs.
- Impact: low for disposable changes; high for shared, production, and security-sensitive work.
- Recoverability: good before merge; worse after release, data migration, or dependency adoption.

### Blast radius

An unreviewed diff can carry unrelated behavior, weakened tests, hidden dependency risk, and false confidence into every future change built on top of it.

### Minimum guardrails

- changed-files pass
- risky-area pass
- evidence pass
- explicit not-reviewed list

### Recovery plan

1. Stop merge or release.
2. Save the current diff.
3. Produce a changed-file review table.
4. Revert or split unrelated changes.
5. Run targeted checks for the risky areas.
6. Capture not-reviewed gaps before acceptance.

## Budget and Constraint Notes

### Cheapest reliable path

Review the changed-file list first; it is faster than debugging a wrong merge later.

### Fastest high-usage path

High-throughput users can ask Codex to prepare the review table, but the human still owns acceptance.

### Low-attention path

Low-attention review-later work must return a review packet, not just a summary.

### Production-quality path

Production work requires diff review, evidence, rollback, and independent review when blast radius is high.

### Prototype versus production

Prototype diffs can be disposable. Production diffs become obligations.

### Maintenance phase

Maintenance diffs need extra care because small-looking patches can disturb existing contracts.

## Stable Core

- generated code is still code review work
- review the diff by intent, risk, and evidence
- a summary is not a substitute for changed-file inspection

## Volatile Surface

- Codex review UI affordances
- GitHub pull request review UI
- model diff summary behavior
- repository-specific review checklists

## Obsolescence Watch

This card should be revised if:

- generated diffs become automatically complete, formally verified, and reviewable without human or CI inspection

## Evidence and Sources

- `openai.codex.app_review` - Official OpenAI Codex app review guidance for changed files, diff inspection, staging, and review workflows.
- `openai.codex.use_cases.github_code_reviews` - Official OpenAI Codex use case for PR review, regressions, missing tests, and risky behavior changes.
- `github.docs.pull_requests` - Official GitHub documentation for pull requests, changed files, checks, and merge review context.
- `vcb.synthesis.stable_engineering_practice` - VCB maintainer synthesis for durable risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.codex_output_review`
- `vcb.workflow.github_pr_review`
- `vcb.concepts.diff`
- `vcb.concepts.pull_request`
- `vcb.failure.done_claim_without_evidence`

<!-- VCB:STOP_RETRIEVAL reason="accepting_diff_without_review_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.accepting_diff_without_review -->
