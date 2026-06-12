<!-- VCB:BEGIN_TOPIC id=vcb.codex.feature_maturity version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
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
id: vcb.codex.feature_maturity
title: Codex Feature Maturity
type: codex_feature
review_cadence: monthly
next_review_due: '2026-07-09'
applies_to:
- Codex docs
- Codex features
- Update review
- Production decisions
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.ignoring_model_biases
- vcb.shortcut.default_config_forever
durable_principles:
- feature maturity labels are risk signals
- experimental or beta features need stronger review and fallback plans
- production guidance should not treat all Codex features as equally stable
likely_to_change:
- maturity labels and definitions
- which features carry which labels
- deprecation policy and feature support levels
obsolete_when:
- OpenAI removes or replaces Codex feature-maturity labels
related_topics:
- vcb.chapter.maintaining_updating_bible
- vcb.codex.changelog_monitoring
- vcb.codex.hooks
- vcb.codex.subagents
- vcb.chapter.what_codex_is_bad_at
---

> Summary:
> Feature maturity labels tell you how stable or experimental a Codex feature is and how much production confidence to place in it.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.feature_maturity.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Feature maturity is the label that tells you whether a Codex feature is stable, beta, experimental, or otherwise not ready. You should treat those labels like weather reports for your workflow risk.

### Why it matters

If you build a core production workflow around an unstable feature, your process can break when the product changes. If you treat all features as equally safe, you will overtrust volatile surfaces.

### The mental model

Feature maturity is a road sign. Stable means paved road. Beta means road work. Experimental means bring a spare tire and do not route ambulances through it.

### What good looks like

Good use: check maturity before relying on a feature for production automation, CI, security review, or unattended work.

### What bad looks like

Bad use: build a critical release process around an experimental feature without fallback.

### Minimal example

Example: before making an automation part of your team’s release gate, check its maturity, changelog history, and fallback path.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.feature_maturity.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.feature_maturity.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach maturity labels as decision inputs for risk, review cadence, and fallback requirements.

### Diagnose the human’s current model

- Is this feature part of a critical path?
- What maturity label does the official page give it?
- What happens if the behavior changes next month?
- Is there a manual fallback?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

A maturity label is a food expiration date plus handling instruction. It does not mean “never eat”; it means know how risky it is.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Before we rely on this Codex feature, check its official maturity/status page and changelog. Summarize whether it is stable enough for [workflow], what could change, and the fallback if it breaks.
```

### Red flags to call out directly

- production gate using experimental feature
- no fallback for volatile surface
- old tutorial treated as current product truth
- model/feature advice copied without review date

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.feature_maturity.ai_coach -->

## Shortcut Reality

### The ideal practice

Use maturity labels to choose guardrails, review cadence, and production readiness.

### What users often do instead

Users often ignore maturity labels because the feature works once.

### When the shortcut may be fine

This may be fine for prototypes, demos, or isolated experiments.

### When the shortcut is a bad idea

It is bad when the feature controls CI, security, deployment, billing, or unattended production workflows.

### Risk profile

- Probability of failure: Failure probability depends on maturity
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- check official maturity label
- record review date
- keep manual fallback
- avoid critical dependency on experimental features
- monitor changelog

### Recovery plan

Switch to fallback workflow, update affected cards/config/skills/hooks, log deprecation risk, and review all topics that referenced the changed feature.

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

- feature maturity labels are risk signals
- experimental or beta features need stronger review and fallback plans
- production guidance should not treat all Codex features as equally stable

## Volatile Surface

- maturity labels and definitions
- which features carry which labels
- deprecation policy and feature support levels

## Obsolescence Watch

- OpenAI removes or replaces Codex feature-maturity labels

## Evidence and Sources

- `openai.codex.feature_maturity` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.changelog` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.maintaining_updating_bible`
- `vcb.codex.changelog_monitoring`
- `vcb.codex.hooks`
- `vcb.codex.subagents`
- `vcb.chapter.what_codex_is_bad_at`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.feature_maturity -->
