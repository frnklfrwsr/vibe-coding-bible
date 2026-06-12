<!-- VCB:BEGIN_TOPIC id=vcb.workflow.dependency_decisions version=0.1.0 -->
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
evidence_scope: official GitHub/npm dependency documentation plus VCB maintainer synthesis
  for dependency risk and budget framing
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
id: vcb.workflow.dependency_decisions
title: Dependency Decision Workflow with Codex
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Package managers
- Pull requests
- Frontend/backend apps
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.adding_dependencies_fast
- vcb.shortcut.framework_churn
- vcb.shortcut.tool_sprawl
- vcb.shortcut.broad_agent_permissions
durable_principles:
- a dependency is a maintenance relationship
- no-new-dependency should be considered first
- lockfile and transitive impact matter
likely_to_change:
- package manager commands
- dependency review UI
- security advisory data
- license policy
- ecosystem package health
obsolete_when:
- package ecosystems make new dependency risk negligible and automatically reversible
related_topics:
- vcb.chapter.dependency_package_framework_decisions
- vcb.concepts.dependency
- vcb.workflow.dependency_update_review
- vcb.workflow.reviewing_diffs
- vcb.safety.security_review
- vcb.concepts.build_step
---

> Summary:
> Dependency decisions use Codex to justify new packages, compare no-new-dependency alternatives, inspect lockfile impact, and separate prototype convenience from production liability.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.dependency_decisions.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A dependency decision is the choice to rely on someone else’s package, framework, SDK, service, or build tool. Codex should not install first and justify later.

### Why it matters

Packages can save time, but they also add security, license, bundle, install, versioning, and maintenance risk.

### The mental model

A dependency is a tiny vendor relationship. Free code is not free ownership.

### What good looks like

Good: “Solve without a new dependency first. If you still recommend one, explain alternatives, production/dev scope, lockfile impact, security/license/bundle risk, and rollback. Do not install until approved.”

### What bad looks like

Bad: “Install a library for this” when the existing framework or a small helper would solve it.

### Minimal example

Ask for no-new-dependency, existing-dependency, dev-only, and production-dependency options before allowing installation.

### Checklist

- no-new-dependency option considered
- existing packages checked
- dev vs production scope classified
- lockfile diff reviewed
- security/license risk considered
- bundle/runtime/install cost considered
- rollback path named
<!-- VCB:END_SECTION id=vcb.workflow.dependency_decisions.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.dependency_decisions.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to make dependencies earn their place.

### Diagnose the human’s current model

- Can current code or platform APIs solve it?
- Is an existing dependency already available?
- Is this dev-only or runtime?
- What does the lockfile add?
- How hard is removal later?

### Explanation strategy

Force a dependency decision memo before install. Compare local helper, existing dependency, new dev dependency, new production dependency, and framework change. For production dependencies, require review of manifest and lockfile.

### Useful metaphor

A dependency is a loan. It gives leverage now and payments later.

### Coaching tactics

- stop install commands until approved
- separate package choice from implementation
- ask Codex to inspect package manager and lockfile conventions
- flag framework changes as architecture decisions
- tie dependency risk to project phase

### Prompt patterns

```text
Before adding a dependency, propose a no-new-dependency solution. If a package is justified, provide package name, purpose, alternatives rejected, dev/runtime scope, files and lockfiles changed, security/license/bundle/install risks, maintenance risk, rollback plan, and checks. Do not install until approved.
```

### Red flags to call out directly

- new package in a simple helper task
- production dependency for test-only work
- large lockfile diff unexplained
- framework choice hidden in feature work
- package selected because Codex knows its API

### Exercises

- Ask the human to classify packages as dev or production.
- Have them read a lockfile diff summary.
- Compare local helper versus package for a small utility.
<!-- VCB:END_SECTION id=vcb.workflow.dependency_decisions.ai_coach -->

## Shortcut Reality

### The ideal practice

Decide before installing, then review manifest, lockfile, risk, and rollback.

### What users often do instead

Users let Codex install the first package that makes implementation easy.

### When the shortcut may be fine

Fast dependency additions can be acceptable in disposable prototypes or dev-only tooling with easy removal.

### When the shortcut is a bad idea

It is a bad trade for production dependencies, auth/security/payment SDKs, build tools, frameworks, native modules, or abandoned packages.

### Risk profile

- Probability of failure: Medium risk per package; high cumulative risk when dependency additions become habitual.
- Impact if it fails: Impact can include vulnerabilities, legal issues, broken deploys, larger bundles, and migration debt.
- Ease of recovery: Good before code depends on it; poor after the package shapes architecture.
- Blast radius: The blast radius is the runtime, build, security, and future maintenance surface introduced by the package tree.
- Skill needed to recover: Low for reading package.json; medium for lockfile/transitive risk; high for framework choices.
- Hidden cost: Upgrade burden, attack surface, install flakiness, and future migrations.

### Minimum guardrails

- no install before decision memo
- dev/runtime classification
- manifest plus lockfile review
- security/license check
- rollback path

### Recovery plan

- Pause implementation.
- Remove unused package and lockfile changes.
- Replace with existing/local option if feasible.
- Run install/build/test checks.
- Add a no-new-dependency prompt rule.

## Budget and Constraint Notes

### Cheapest reliable path

Use existing code, platform APIs, or a small helper first. This avoids install, review, and future upgrade cost.

### Fastest high-usage path

High-usage users can ask Codex for a comparison memo quickly, but should not delegate the final package choice for production code.

### Low-attention path

Low-attention dependency work should be report-only until a human approves install and lockfile changes.

### Production-quality path

Production dependency decisions need security/license review, lockfile review, compatibility checks, and rollback plan.

### Prototype versus production

Prototype dependencies can accelerate learning. Production and maintenance work must price in future upgrades and removal cost.

### Maintenance phase

In maintenance, a new dependency must reduce long-term cost more than it adds upgrade/security/review overhead.

## Stable Core

- a dependency is a maintenance relationship
- no-new-dependency should be considered first
- lockfile and transitive impact matter

## Volatile Surface

- package manager commands
- dependency review UI
- security advisory data
- license policy
- ecosystem package health

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- package ecosystems make new dependency risk negligible and automatically reversible

## Evidence and Sources

- `github.docs.dependency_review` — Official GitHub dependency-review documentation for dependency diffs, vulnerabilities, and enforcement.
- `github.docs.dependency_graph` — Official GitHub dependency-graph documentation for dependency inventory and transitive visibility.
- `github.docs.dependency_maintenance_best_practices` — Official GitHub dependency-maintenance guidance for review and update practices.
- `npm.docs.package_json` — Official npm documentation for package.json dependency declarations and version ranges.
- `npm.docs.package_lock` — Official npm documentation for lockfile behavior and exact dependency trees.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, and review discipline.

## Related Topics

- `vcb.chapter.dependency_package_framework_decisions`
- `vcb.concepts.dependency`
- `vcb.workflow.dependency_update_review`
- `vcb.workflow.reviewing_diffs`
- `vcb.safety.security_review`
- `vcb.concepts.build_step`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.dependency_decisions -->
