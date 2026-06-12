<!-- VCB:BEGIN_TOPIC id=vcb.concepts.lint version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
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
id: vcb.concepts.lint
title: Lint
type: concept
next_review_due: '2027-06-09'
source_status:
  official_openai: false
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: concept definition anchored to official/vendor/expert sources; Codex-specific
  risk guidance is maintainer synthesis
stability:
  principle: CORE_ENGINEERING
  surface: STABLE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.ignoring_lint_typecheck
durable_principles:
- lint is cheap feedback
- lint rules encode team/project conventions
- lint passing is not behavior proof
likely_to_change:
- specific lint rules
- formatter integration
- framework defaults
obsolete_when:
- software no longer benefits from automated style/safety scans
related_topics:
- vcb.concepts.typecheck
- vcb.concepts.test
- vcb.concepts.ci
- vcb.chapter.git_discipline
---

> Summary:
> Lint checks code for patterns that are risky, inconsistent, unused, unreachable, or outside the project’s style/safety rules.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.lint.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Lint is an automated code reviewer for common patterns. It can catch unused variables, unreachable code, accidental globals, inconsistent imports, unsafe patterns, and project style violations.

### Why it matters

Codex may leave dead variables, broad disable comments, or inconsistent patterns. Lint catches some of that cheaply before humans review.

### The mental model

Lint is a hallway monitor. It does not know whether the whole product is good, but it catches obvious rule-breaking before it spreads.

### What good looks like

- lint command passes for changed files or project
- Codex does not add broad disable comments
- warnings are understood, not blindly suppressed
- style-only changes are separated from behavior changes

### What bad looks like

- `eslint-disable` added at file top
- lint skipped before CI
- formatter churn mixed with logic changes
- unused code left behind

### Minimal example

A lint rule can catch `no-unused-vars` after Codex deletes usage but leaves an import behind.

### Checklist

- Run lint if available.
- Treat new warnings as changed-code debt.
- Avoid broad disable comments.
- Separate formatting-only diffs from behavior diffs.
<!-- VCB:END_SECTION id=vcb.concepts.lint.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.lint.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Frame lint as cheap hygiene and reject suppressions that hide real issues.

### Diagnose the human’s current model

- What part of the concept is the human treating as magic?
- What evidence would show this is working?
- What is the risky production version of this concept?
- Can the human name the boundary, data, or check involved?

### Explanation strategy

Start with a concrete everyday analogy, then tie it to the exact files, commands, checks, or data flow Codex is likely to touch. Keep the explanation practical and risk-scaled.

### Useful metaphors

- Use one simple metaphor, then return to the actual repo.
- Treat the concept as an operational control, not trivia.

### Coaching tactics

- Ask Codex to inspect current project conventions before editing.
- Convert the concept into a small checklist.
- Escalate when the concept touches production, secrets, data, auth, payments, or CI.

### Prompt patterns

```text
Run the lint command and fix changed-code warnings. Do not add broad disable comments unless there is a narrow documented reason.
```

```text
Explain each lint error in plain language and whether it is style, safety, or dead-code related.
```

### Red flags to call out directly

- broad disable comments
- lint failures called “not important” without classification
- formatting churn hides behavior change
- unused variables from abandoned approach

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.lint.ai_coach -->

## Shortcut Reality

### The ideal practice

Run lint and fix changed-code issues.

### What users often do instead

Users ignore lint to move faster.

### When the shortcut may be fine

Throwaway demo when lint config is noisy and no CI depends on it.

### When the shortcut is a bad idea

Shared repo, CI-gated project, production change, generated code that humans maintain.

### Risk profile

- Probability of failure: low/medium
- Impact if it fails: low individually, medium as decay
- Ease of recovery: high early
- Blast radius: code quality and CI
- Skill needed to recover: low/medium
- Hidden cost: style churn and CI friction

### Minimum guardrails

- Run lint on changed files/project.
- Avoid broad disables.
- Document pre-existing failures.
- Commit formatting separately when large.

### Recovery plan

Remove broad disables, restore lint config, fix changed-code errors, and separate style cleanup from behavior patches.

### AI coach guidance

Do not lecture first. Classify the project risk, then move the human one guardrail level up. If this touches real users, secrets, money, auth, production data, migrations, or CI credentials, be direct and require evidence before acceptance.

## Budget and Constraint Notes

### Cheapest reliable path

Use this card to clarify the concept before asking Codex to edit. Spend one short inspection or explanation pass, then make the smallest verified change.

### Fastest high-usage path

Run a plan/implementation/review loop, but keep diffs isolated and require Codex to report the concept-specific risk areas before acceptance.

### Low-attention path

Low-attention work needs stronger written constraints, not broader trust. Require a final report with files changed, checks run, known gaps, and any concept-specific risk.

### Production-quality path

Use the concept as a release gate: define the boundary, verify the important cases, review the diff, and preserve rollback/recovery options.

## Stable Core

- lint is cheap feedback
- lint rules encode team/project conventions
- lint passing is not behavior proof

## Volatile Surface

- specific lint rules
- formatter integration
- framework defaults

## Obsolescence Watch

Obsolete or review this topic when:

- software no longer benefits from automated style/safety scans

## Evidence and Sources

- `eslint.docs.home` — source anchor for this concept.
- `eslint.docs.latest` — source anchor for this concept.
- `npm.docs.scripts` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.typecheck
- vcb.concepts.test
- vcb.concepts.ci
- vcb.chapter.git_discipline

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.lint -->
