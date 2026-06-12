<!-- VCB:BEGIN_TOPIC id=vcb.concepts.dependency version=0.1.0 -->
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
id: vcb.concepts.dependency
title: Dependency
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
- vcb.shortcut.adding_dependencies_fast
- vcb.shortcut.tool_sprawl
durable_principles:
- dependencies are liabilities as well as capabilities
- use existing code or platform features first when reasonable
- dependency changes need review and lockfile inspection
likely_to_change:
- package ecosystem health
- package-manager behavior
- security advisories
obsolete_when:
- software stops composing third-party code
related_topics:
- vcb.concepts.build_step
- vcb.concepts.ci
- vcb.chapter.dependency_package_framework_decisions
- vcb.chapter.tool_stack_catalog
---

> Summary:
> A dependency is outside code your project relies on; every package adds capability, but also maintenance, security, versioning, and lock-in cost.

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

<!-- VCB:BEGIN_SECTION id=vcb.concepts.dependency.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A dependency is a package or library your app depends on. It may save weeks of work. It also becomes part of your supply chain and future maintenance burden.

### Why it matters

Codex likes to solve problems by adding packages because packages are common in examples. That can be fine, but in production every dependency adds updates, vulnerabilities, compatibility risks, bundle size, licenses, and debugging surface.

### The mental model

A dependency is hiring a tiny outside contractor into your codebase. Useful, but now you depend on their work showing up safely every day.

### What good looks like

- no-new-dependency solution considered first
- package purpose is justified
- lockfile diff reviewed
- security/license/maintenance risk considered
- dependency is scoped correctly as runtime or dev

### What bad looks like

- small task adds a large framework
- package added without lockfile review
- dependency used for one trivial function
- Codex installs unmaintained packages

### Minimal example

A date picker package may be worth it. A left-pad package for one line probably is not.

### Checklist

- Ask for no-new-dependency option first.
- Review package.json and lockfile.
- Check whether it is runtime or dev-only.
- Consider security, license, size, maintenance, and lock-in.
<!-- VCB:END_SECTION id=vcb.concepts.dependency.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.dependency.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Make dependency review concrete and prevent package-as-progress behavior.

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
Solve this without adding dependencies first. If a dependency is still justified, explain why and list maintenance/security/bundle risks.
```

```text
Review this dependency change: direct/transitive packages, lockfile size, vulnerability/license risk, and simpler alternatives.
```

### Red flags to call out directly

- new dependency for trivial helper
- lockfile explosion ignored
- package with unclear maintenance
- dependency added inside security/auth/build tooling

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.dependency.ai_coach -->

## Shortcut Reality

### The ideal practice

Justify dependencies and review their downstream cost.

### What users often do instead

Users let Codex install a package because the first solution compiles.

### When the shortcut may be fine

Disposable prototype with no sensitive data and a rebuild plan.

### When the shortcut is a bad idea

Production, auth, build tooling, payments, native modules, or security-sensitive packages.

### Risk profile

- Probability of failure: medium
- Impact if it fails: medium/high
- Ease of recovery: medium before adoption, lower after integration
- Blast radius: build, runtime, security, bundle, CI
- Skill needed to recover: package ecosystem debugging
- Hidden cost: transitive maintenance

### Minimum guardrails

- No-new-deps first.
- Inspect manifest and lockfile.
- Prefer established packages.
- Avoid secrets with install scripts.
- Commit before install.

### Recovery plan

Remove the package, revert lockfile/manifest changes, replace with simpler code or better-vetted dependency, and add an AGENTS.md rule if Codex keeps adding packages.

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

- dependencies are liabilities as well as capabilities
- use existing code or platform features first when reasonable
- dependency changes need review and lockfile inspection

## Volatile Surface

- package ecosystem health
- package-manager behavior
- security advisories

## Obsolescence Watch

Obsolete or review this topic when:

- software stops composing third-party code

## Evidence and Sources

- `npm.docs.package_json` — source anchor for this concept.
- `npm.docs.package_dependencies` — source anchor for this concept.
- `github.docs.dependency_review` — source anchor for this concept.
- `owasp.dependency_graph_sbom` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.build_step
- vcb.concepts.ci
- vcb.chapter.dependency_package_framework_decisions
- vcb.chapter.tool_stack_catalog

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.dependency -->
