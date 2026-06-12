<!-- VCB:BEGIN_TOPIC id=tool.codex_github_review version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI/Codex tool documentation plus VCB maintainer synthesis
  for setup, risk, budget, and coaching guidance
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
id: tool.codex_github_review
title: Codex GitHub Review
name: Codex GitHub Review
type: tool_card
category: codex_github_pr_review
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
setup_effort: 'medium: repository integration, Codex Cloud setup, review settings,
  and optional AGENTS.md guidance'
maintenance_effort: 'medium: trigger mechanics, automatic review settings, GitHub
  integration, and review behavior can change'
debugging_effort: 'medium: failures may be repository setup, permissions, trigger
  syntax, PR event settings, or missing guidance'
lock_in_risk: 'moderate: review comments and automation depend on Codex/GitHub integration
  behavior'
hidden_cost_risk: 'medium: automatic reviews can create review noise, usage, and process
  confusion if unmanaged'
codex_integration_value: high as a second-pass risk scanner when human review remains
  authoritative
best_for:
- additional PR risk scan
- serious issue detection
- review guideline enforcement
- large PR triage before human review
not_for:
- final approval
- style-only bikeshedding
- unreviewed auto-merge
- PRs without enough context or tests
integrates_with_codex:
- GitHub PRs
- Codex Cloud
- AGENTS.md
- repository review guidance
- human code review
hidden_costs:
- review noise if guidelines are poor
- false confidence from no findings
- team process drift
- missed issues outside diff context
applies_to:
- GitHub pull requests
- Codex code review
- automatic PR review
- review guidelines
- AGENTS.md review guidance
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_tests
- vcb.shortcut.reviewing_cloud_summary_only
- vcb.shortcut.consensus_as_correctness
durable_principles:
- AI PR review is evidence, not ownership.
- Review guidance improves signal only when it is durable and specific.
- No findings does not prove absence of defects.
likely_to_change:
- GitHub trigger mechanics, automatic review settings, comment behavior, integration
  permissions, and Codex review focus
obsolete_when:
- OpenAI retires the GitHub PR review integration or changes it so it no longer posts
  review output on pull requests.
related_topics:
- vcb.codex.github_review
- vcb.workflow.github_pr_review
- vcb.workflow.reviewing_diffs
- vcb.safety.security_review
- vcb.failure.ci_false_confidence
---

# Codex GitHub Review

> Summary:
> Codex GitHub Review is the first-party PR review surface for getting an additional Codex review pass on GitHub pull requests.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_github_review.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex GitHub Review is a reviewer signal on a pull request. It can inspect a PR diff and post review comments, but it is not an approval authority.

### Why it matters

It matters because a second review pass can catch serious issues. It fails when teams treat no comments as proof that the PR is safe.

### What good looks like

Use it as one reviewer in a human-owned review process with tests, diff reading, and repository guidance.

### What bad looks like

Enable automatic reviews and merge whenever Codex does not complain.

### Minimal example

Request a Codex review on a risky PR, compare comments to tests and human review, resolve serious findings, and still inspect the final diff.

### Best-fit cases

- additional PR risk scan
- serious issue detection
- review guideline enforcement
- large PR triage before human review

### Not-fit cases

- final approval
- style-only bikeshedding
- unreviewed auto-merge
- PRs without enough context or tests

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: repository integration, Codex Cloud setup, review settings, and optional AGENTS.md guidance |
| Maintenance effort | medium: trigger mechanics, automatic review settings, GitHub integration, and review behavior can change |
| Debugging effort | medium: failures may be repository setup, permissions, trigger syntax, PR event settings, or missing guidance |
| Lock-in risk | moderate: review comments and automation depend on Codex/GitHub integration behavior |
| Hidden cost risk | medium: automatic reviews can create review noise, usage, and process confusion if unmanaged |

### Checklist

- choose the smallest Codex surface that fits the task
- confirm permissions before mutation
- require a diff, report, structured output, or check evidence
- keep exact pricing, limits, model availability, and UI mechanics out of stable decisions
- review official OpenAI docs before freezing current product behavior

<!-- VCB:END_SECTION id=tool.codex_github_review.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_github_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach PR review as a signal amplifier. Codex can flag risks, but humans still own merge decisions and production accountability.

### Diagnostic questions

- Is Codex Cloud set up for the repository?
- Is AGENTS.md or review guidance present?
- Does the PR have enough tests and context for review?
- Who decides merge after Codex comments?

### Coaching tactics

- ask for high-priority risk focus
- route recurring review guidance into AGENTS.md
- combine Codex review with human diff review
- treat automatic review as triage, not approval

### Prompt pattern

```text
Review this PR for serious issues only. Focus on correctness, security, data loss, auth, migrations, tests, and hidden behavior changes. Cite file/line evidence and state what would need to be true before merge.
```

### Red flags

- merge rule treats Codex as approval
- automatic review configured but no human owner
- PR lacks tests for risky paths
- Codex comments resolved without verifying the underlying diff

### Intervention rule

When the human asks for a current product detail, exact price, exact limit, model-routing claim, UI label, command flag, or plan-packaging fact, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_github_review.ai_coach -->

## Shortcut Reality

### The ideal practice

Use this tool only after the task, context, permissions, evidence, and review path are clear.

### What users often do instead

Users often pick the most convenient surface, then retrofit the safety controls after the tool has already produced output.

### When the shortcut may be acceptable

The shortcut can be acceptable for disposable prototypes, read-only inspection, docs work, small branches, or reports where rollback is trivial and no secrets or production state are exposed.

### When it becomes a bad trade

It becomes a bad trade when the tool can mutate broad code, touch secrets, make production changes, create noisy automation, hide environment assumptions, or return a polished summary without verifiable evidence.

### Relevant shortcut cards

- `vcb.shortcut.accepting_looks_done`
- `vcb.shortcut.skipping_tests`
- `vcb.shortcut.reviewing_cloud_summary_only`
- `vcb.shortcut.consensus_as_correctness`

### Minimum guardrails

- one bounded task per run/thread/job
- explicit permissions and forbidden zones
- Git checkpoint or isolated branch/worktree for mutation
- evidence packet before acceptance
- human review before merge, deploy, credential use, or production action

### Recovery plan

Stop the tool, preserve logs/transcripts/output, inspect the diff or generated artifact, revert or isolate unsafe changes, rotate exposed secrets if needed, and restart with a smaller task packet.

## Budget and Constraint Notes

### Cheapest reliable path

Use the narrowest surface, smallest context packet, and cheapest reviewable workflow that can produce the needed evidence. Avoid retry loops caused by vague prompts.

### Fastest high-usage path

Use parallel or automated surfaces only when work is independent, review capacity exists, and integration cost is budgeted.

### Low-attention path

Low-attention use requires isolation, stop conditions, and a final review packet. It does not justify broad mutation or production access.

### Production-quality path

Production use requires explicit scope, least privilege, checks, security review where relevant, and human acceptance based on artifacts rather than summaries.

### Hidden costs to watch

- review noise if guidelines are poor
- false confidence from no findings
- team process drift
- missed issues outside diff context

## Stable Core

- AI PR review is evidence, not ownership.
- Review guidance improves signal only when it is durable and specific.
- No findings does not prove absence of defects.

## Volatile Surface

- GitHub trigger mechanics, automatic review settings, comment behavior, integration permissions, and Codex review focus

Exact prices, plan packaging, feature availability, commands, flags, model menus, context limits, UI labels, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires the GitHub PR review integration or changes it so it no longer posts review output on pull requests.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.github_review` — official/synthesis source anchor for this tool card.
- `openai.codex.cloud` — official/synthesis source anchor for this tool card.
- `openai.codex.agents_md` — official/synthesis source anchor for this tool card.
- `openai.codex.best_practices` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `vcb.codex.github_review`
- `vcb.workflow.github_pr_review`
- `vcb.workflow.reviewing_diffs`
- `vcb.safety.security_review`
- `vcb.failure.ci_false_confidence`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_github_review -->
