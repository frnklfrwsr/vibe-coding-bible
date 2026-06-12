<!-- VCB:BEGIN_TOPIC id=vcb.workflow.dependency_update_review version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
audiences:
- human
- ai_coach
source_status:
  official_openai: false
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official GitHub/npm dependency update and review documentation plus
  VCB maintainer synthesis
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
id: vcb.workflow.dependency_update_review
title: Dependency Update Review Workflow with Codex
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- GitHub PRs
- Dependabot
- Package managers
- CI
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.adding_dependencies_fast
- vcb.shortcut.automation_spam
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_tests
durable_principles:
- dependency updates are code changes
- lockfile changes need review
- security updates need urgency without blind trust
likely_to_change:
- Dependabot behavior
- package audit command output
- advisory data
- package manager lockfile formats
- semver/release-note conventions
obsolete_when:
- dependency update systems can prove compatibility and safety without project-specific
  checks
related_topics:
- vcb.workflow.dependency_decisions
- vcb.concepts.dependency
- vcb.workflow.ci_triage
- vcb.workflow.testing
- vcb.workflow.reviewing_diffs
- vcb.safety.security_review
---

> Summary:
> Dependency update review uses Codex to inspect version bumps, lockfile changes, release notes, security motivation, and targeted checks before merging package updates.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.dependency_update_review.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Dependency update review means treating a package version bump as a real code change. You inspect what changed, why it changed, what lockfile moved, and which checks prove your app still works.

### Why it matters

Automated dependency PRs can fix vulnerabilities and also break builds, change behavior, or pull a larger transitive tree than expected.

### The mental model

A dependency update is swapping a part in a machine. The part may be safer, but the machine still needs a test run.

### What good looks like

Good: “Review this dependency update. Identify direct and transitive changes, security reason, release-note highlights, breaking-change risk, affected app areas, and targeted checks. Do not merge.”

### What bad looks like

Bad: Merging automated update PRs because CI is green without reading what changed.

### Minimal example

Provide the PR, package manager, manifest/lockfile diff, security advisory if any, and relevant checks.

### Checklist

- direct package/version change identified
- transitive lockfile impact summarized
- security advisory or version motivation named
- breaking-change/release-note risk checked
- affected app area named
- CI and targeted local checks considered
- rollback/downgrade path named
<!-- VCB:END_SECTION id=vcb.workflow.dependency_update_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.dependency_update_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to review dependency PRs by change impact, not by automation label.

### Diagnose the human’s current model

- Is this security, patch, minor, major, or framework migration?
- Which lockfile entries changed?
- What release notes matter?
- Which app paths use the package?
- What check would catch a break?

### Explanation strategy

Ask Codex for a dependency-impact report first. Separate security urgency from compatibility proof. For major updates or runtime dependencies, require affected-path checks and rollback plan.

### Useful metaphor

Automation can bring the replacement part to the workbench. It cannot certify the whole car drives safely.

### Coaching tactics

- summarize manifest plus lockfile diff
- group updates only when test coverage is strong
- treat major updates as migrations
- avoid blind auto-merge for runtime packages
- record ignored advisories and rationale

### Prompt patterns

```text
Review this dependency update PR. Report direct updates, transitive changes, security/advisory reason, release-note or breaking-change risk, files using the package, checks already run, additional targeted checks, rollback/downgrade path, and merge recommendation. Do not edit unless asked.
```

### Red flags to call out directly

- major version hidden in grouped PR
- runtime dependency merged with no app-path check
- lockfile diff not read
- security update delayed without owner
- package update fixes CI by weakening tests

### Exercises

- Have the human classify update risk from patch/minor/major plus runtime/dev scope.
- Ask them to find affected code paths for one package.
- Review a Dependabot PR and write a merge memo.
<!-- VCB:END_SECTION id=vcb.workflow.dependency_update_review.ai_coach -->

## Shortcut Reality

### The ideal practice

Review dependency updates with manifest, lockfile, release/advisory context, targeted checks, and rollback.

### What users often do instead

Users merge automated update PRs as maintenance noise.

### When the shortcut may be fine

Auto-merge may be acceptable for low-risk dev-only patch updates with strong CI and easy rollback.

### When the shortcut is a bad idea

It is a bad trade for major versions, runtime packages, security-sensitive libraries, build tools, frameworks, or weak CI.

### Risk profile

- Probability of failure: Medium risk for routine updates; high for major/runtime/build-tool updates.
- Impact if it fails: Impact includes broken builds, changed runtime behavior, vulnerabilities, bundle changes, and deployment failure.
- Ease of recovery: Good if the update is isolated; poor if grouped updates obscure the cause.
- Blast radius: The blast radius is the code paths and build/runtime environments that use the updated package tree.
- Skill needed to recover: Medium for package review; high for major migrations and security advisory interpretation.
- Hidden cost: Alert fatigue, stale dependencies, brittle CI, and unowned package risk.

### Minimum guardrails

- classify update risk
- inspect lockfile
- read relevant release/advisory notes
- run targeted checks
- avoid broad auto-merge for runtime/major updates

### Recovery plan

- Revert or downgrade the package update.
- Bisect grouped updates if needed.
- Run affected-path checks.
- Patch compatibility code separately.
- Tune grouping/auto-merge policy.

## Budget and Constraint Notes

### Cheapest reliable path

Review only changed manifests/lockfiles plus affected tests for low-risk patch updates.

### Fastest high-usage path

Use Codex to summarize update risk across many PRs, but require human attention for major/runtime/security-sensitive updates.

### Low-attention path

Low-attention update handling can triage and label PRs, but mutation/merge should wait for checks and policy.

### Production-quality path

Production dependency updates need CI, affected-path checks, rollback, and security owner attention for vulnerabilities.

### Prototype versus production

Prototype updates can be loose if the app is disposable. Production and maintenance updates need a repeatable dependency-review habit.

### Maintenance phase

In maintenance, dependency review is recurring cost. Reduce it with grouping rules, ownership, and targeted checks, not blind auto-merge.

## Stable Core

- dependency updates are code changes
- lockfile changes need review
- security updates need urgency without blind trust

## Volatile Surface

- Dependabot behavior
- package audit command output
- advisory data
- package manager lockfile formats
- semver/release-note conventions

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- dependency update systems can prove compatibility and safety without project-specific checks

## Evidence and Sources

- `github.docs.dependabot_security_updates` — Official GitHub documentation for Dependabot security update PRs.
- `github.docs.dependabot_version_updates` — Official GitHub documentation for Dependabot version update PRs.
- `github.docs.dependency_review` — Official GitHub dependency-review documentation for dependency diffs, vulnerabilities, and enforcement.
- `npm.docs.security_audit` — Official npm documentation for auditing package dependencies for vulnerabilities.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, and review discipline.

## Related Topics

- `vcb.workflow.dependency_decisions`
- `vcb.concepts.dependency`
- `vcb.workflow.ci_triage`
- `vcb.workflow.testing`
- `vcb.workflow.reviewing_diffs`
- `vcb.safety.security_review`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.dependency_update_review -->
