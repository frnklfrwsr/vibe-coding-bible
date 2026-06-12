<!-- VCB:BEGIN_TOPIC id=vcb.failure.dependency_bloat version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex anchors, relevant vendor or named expert anchors
  where cited, and VCB maintainer synthesis for failure-mode control loops
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
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.failure.dependency_bloat
title: Dependency Bloat
type: failure_mode
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Package managers
- Frontend apps
- Backend services
- Dependency update workflows
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.adding_dependencies_fast
- vcb.shortcut.framework_churn
- vcb.shortcut.tool_sprawl
- vcb.shortcut.generated_prototype_as_production_foundation
durable_principles:
- dependencies carry ongoing maintenance cost
- lockfiles are reviewable source artifacts
- new packages need a decision boundary
likely_to_change:
- package manager behavior
- advisory databases
- dependency-review tooling
- package maintenance status
- bundle-size tooling
obsolete_when:
- package ecosystems can prove safety, compatibility, maintenance health, and net
  value automatically
related_topics:
- vcb.workflow.dependency_decisions
- vcb.workflow.dependency_update_review
- vcb.concepts.dependency
- vcb.safety.security_review
- vcb.failure.broad_refactor_drift
---

> Summary:
> Dependency bloat happens when Codex adds packages, frameworks, plugins, or SDKs faster than the project can justify, maintain, audit, and update them.

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

<!-- VCB:BEGIN_SECTION id=vcb.failure.dependency_bloat.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A dependency is code you did not write but now rely on. It can save time. It also adds version drift, security exposure, bundle size, learning cost, update work, and supply-chain review.

### Why it matters

Agents often reach for a package because public examples do. That can be sensible, but not every small problem deserves a new external owner.

### The mental model

A dependency is not free code. It is a tiny vendor relationship inside your repo.

### What good looks like

Good: “Before adding a package, compare built-in code, existing dependency, and new dependency. Show install size/risk, maintenance status, lockfile impact, and rollback.”

### What bad looks like

Bad: adding a package for formatting a date, parsing one small string, or replacing an existing project utility.

### Minimal example

Ask Codex to name the evidence it used, the assumption it is making, the files it changed, and the verification that would catch this failure mode if it were wrong.

### Checklist

- existing solution checked
- package owner and maintenance reviewed
- lockfile diff inspected
- security/advisory signal checked
- rollback path known
<!-- VCB:END_SECTION id=vcb.failure.dependency_bloat.human -->

<!-- VCB:BEGIN_SECTION id=vcb.failure.dependency_bloat.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that dependencies are operational commitments, not just implementation shortcuts.

### Diagnose the human’s current model

- Is there already a project dependency or helper?
- Is the new package runtime or dev-only?
- What changed in the lockfile?
- Who maintains it?
- Can removal be done cleanly later?

### Explanation strategy

Make Codex produce a dependency decision memo before editing package files. Require “no new dependency” as the default unless the package clearly reduces net maintenance cost.

### Useful metaphor

A dependency is not free code. It is a tiny vendor relationship inside your repo.

### Coaching tactics

- slow the human down at the first unsupported assumption
- ask for artifact-backed evidence instead of a verbal assurance
- separate read-only diagnosis from mutation
- require a smaller diff when review quality drops
- turn repeated misses into durable guidance only after the pattern is verified

### Prompt patterns

```text
Do not add dependencies by default. For this task, compare no-new-dependency, existing-project-dependency, and new-package options. If you recommend a package, cite why it is necessary, what files change, lockfile impact, security/update risk, and rollback steps.
```

### Red flags to call out directly

- package files changed without discussion
- dependency solves a one-line problem
- new framework appears inside a refactor
- lockfile diff is huge and unread
- package duplicates existing utilities

### Exercises

- Ask the human to estimate the maintenance cost of a new package before looking at the implementation convenience.
- Ask the human to write one “stop condition” that would make Codex pause instead of pushing through.
- Review a previous agent diff and classify which evidence was missing.
<!-- VCB:END_SECTION id=vcb.failure.dependency_bloat.ai_coach -->

## Shortcut Reality

### The ideal practice

Prefer built-ins or existing dependencies unless a new package clearly lowers total cost and risk.

### What users often do instead

Users let Codex install packages because it makes the current prompt finish faster.

### When the shortcut may be fine

A new package can be fine for disposable prototypes, isolated dev tooling, or mature libraries that solve a hard domain problem.

### When the shortcut is a bad idea

It is a bad trade for core app paths, bundle-sensitive frontend code, security-sensitive systems, or weakly maintained packages.

### Risk profile

- Probability of failure: Medium; public examples bias agents toward package-shaped solutions.
- Impact if it fails: Medium to high depending on runtime exposure, supply-chain risk, and update burden.
- Ease of recovery: Good if isolated; poor if the package spreads through architecture.
- Blast radius: Install path, build pipeline, runtime bundle, transitive dependencies, security posture, and future updates.
- Skill needed to recover: Medium for removal; high when a framework or SDK changes architecture.
- Hidden cost: Dependency updates, advisories, bundle growth, cold-start cost, and lockfile review.

### Minimum guardrails

- no-new-dependency default
- decision memo
- lockfile review
- security/update check
- rollback plan

### Recovery plan

- Freeze further use.
- Inspect package and lockfile diff.
- Replace simple use cases with local code or existing utilities.
- Remove package and rerun install/build/tests.
- Document dependency policy.

## Budget and Constraint Notes

### Cheapest reliable path

Ask Codex for a no-new-dependency solution first. The cheapest dependency is the one you do not have to maintain.

### Fastest high-usage path

High-throughput users can use dependency summaries, but package changes still need owner review.

### Low-attention path

Low-attention dependency tasks should be report-only unless policy pre-approves the package family.

### Production-quality path

Production dependency changes need security review, lockfile inspection, affected tests, and rollback.

### Prototype versus production

Prototype dependency bloat is acceptable only if the prototype is not becoming the production foundation.

### Maintenance phase

In maintenance, every dependency adds recurring review. Budget for updates, advisories, compatibility checks, and removal paths.

## Stable Core

- dependencies carry ongoing maintenance cost
- lockfiles are reviewable source artifacts
- new packages need a decision boundary

## Volatile Surface

- package manager behavior
- advisory databases
- dependency-review tooling
- package maintenance status
- bundle-size tooling

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- package ecosystems can prove safety, compatibility, maintenance health, and net value automatically

## Evidence and Sources

- `openai.codex.use_cases.dependency_incident_audits` — Official OpenAI Codex use case for dependency incident audits and evidence-first dependency review.
- `npm.docs.package_json` — Official npm documentation for package.json dependency fields.
- `npm.docs.package_lock` — Official npm documentation for package-lock and exact dependency tree visibility.
- `github.docs.dependency_maintenance_best_practices` — Official GitHub documentation for dependency maintenance, review, and supply-chain hygiene.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable failure-mode, risk, review, budget, and recovery discipline.

## Related Topics

- `vcb.workflow.dependency_decisions`
- `vcb.workflow.dependency_update_review`
- `vcb.concepts.dependency`
- `vcb.safety.security_review`
- `vcb.failure.broad_refactor_drift`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.failure.dependency_bloat -->
