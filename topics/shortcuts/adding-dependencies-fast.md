<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.adding_dependencies_fast version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
last_reviewed: '2026-06-09'
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
evidence_scope: official OpenAI/Codex guidance plus VCB maintainer synthesis for risk-managed
  shortcut harm reduction
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
- major_refactor
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.shortcut.adding_dependencies_fast
title: Adding Dependencies Fast
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- package selection
- framework choice
- SDK adoption
- plugins
- supply-chain review
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- dependency
- supply_chain
- maintenance
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
- no-new-dependency first
- dependency decision memo
- manifest and lockfile review
- no install with secrets exposed
- rollback plan
shortcut_profiles:
- vcb.shortcut.adding_dependencies_fast
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls
  than prototypes
likely_to_change:
- package ecosystem health
- vulnerability databases
- lockfile formats
- Codex package suggestions
- vendor docs and release cadence
obsolete_when:
- dependency ecosystems become fully verified, low-maintenance, and automatically
  risk-scored at install time
related_topics:
- vcb.concepts.dependency
- vcb.workflow.dependency_decisions
- vcb.workflow.dependency_update_review
- vcb.failure.dependency_bloat
- vcb.constraints.build_vs_maintenance
- vcb.constraints.review_budget
---

# Adding Dependencies Fast

> Summary:
> Adding dependencies fast is accepting a new package, framework, SDK, plugin, or service before proving the project actually needs it and can maintain it.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.adding_dependencies_fast.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut feels efficient because a package can make code appear quickly. The hidden cost is maintenance, security review, bundle size, lockfile churn, license questions, and future upgrade work.

### Why it matters

A dependency is not just code you did not write. It is an ongoing relationship with someone else’s API, release cadence, vulnerabilities, transitive dependencies, and migration path.

### What good looks like

Good: “Try no-new-dependency first. If a dependency is still justified, inspect package health, size/scope, license, maintenance, alternatives, lockfile impact, and rollback.”

### What bad looks like

Bad: “Install whatever package solves this quickest.”

### Minimal example

Before adding a date library for one format, check whether the platform or existing stack already handles it. If not, document why the package is worth the maintenance cost.

### Checklist

- attempt no-new-dependency first
- name the exact problem the package solves
- inspect package health and maintenance
- review lockfile and transitive impact
- define rollback or replacement path

<!-- VCB:END_SECTION id=vcb.shortcut.adding_dependencies_fast.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.adding_dependencies_fast.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat every new package as a budget and security decision, not just an implementation shortcut.

### Diagnostic questions

- Is this dependency solving a real repeated problem?
- Can the existing stack do it?
- What transitive dependencies arrive?
- Who maintains it and how active is it?
- What breaks if it is abandoned or compromised?

### Coaching tactics

- force a no-new-dependency alternative
- ask for dependency decision memo
- separate dependency decision from implementation
- review manifest and lockfile diff
- prefer narrow, boring, widely maintained dependencies

### Red flags

- package added for one trivial helper
- framework migration smuggled into a small task
- install scripts run with secrets available
- lockfile diff is ignored
- Codex chooses package by memory rather than current docs

### Prompt pattern

```text
Do not add a dependency unless you first show the no-new-dependency option and why it fails. If you still recommend a package, give purpose, alternatives, maintenance risk, lockfile impact, license/security notes, and rollback plan.
```

<!-- VCB:END_SECTION id=vcb.shortcut.adding_dependencies_fast.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They take the shortcut because it reduces immediate friction: fewer prompts, fewer checks, fewer approvals, less review, or a faster-looking result.

### When the shortcut may be acceptable

Acceptable for disposable prototypes, throwaway local experiments, or tightly isolated work where rollback is trivial, no real users or secrets are involved, and the output is not treated as production evidence.

### When it becomes a bad trade

Bad when the task touches production, auth, payments, data deletion, secrets, CI permissions, public documentation, dependency supply chain, or a diff too broad for available review.

### Risk profile

- Probability: medium for disciplined small tasks; high when prompts are vague, permissions are broad, or review is deferred.
- Impact: low for local throwaways; high for production, team repos, security-sensitive systems, and public releases.
- Recoverability: good before merge with a clean branch; worse after release, data migration, dependency rollout, credential exposure, or undocumented behavior change.

### Blast radius

The shortcut can spread from one fast turn into merged code, stale tests, false release notes, hidden security exposure, future debugging assumptions, and more expensive recovery work.

### Minimum guardrails

- no-new-dependency first
- dependency decision memo
- manifest and lockfile review
- no install with secrets exposed
- rollback plan

### Recovery plan

1. Stop the current run or merge path.
2. Create or restore a Git checkpoint.
3. Ask Codex for a risk and evidence table for the shortcut taken.
4. Run the smallest relevant verification or review pass.
5. Revert, isolate, or split the work if evidence is missing.
6. Update the prompt, AGENTS.md guidance, or workflow checklist so the same shortcut has a guardrail next time.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest guardrail that can catch the likely failure before spending on retries, broad context, or recovery.

### Fastest high-usage path

High-throughput users can spend more turns, but should spend them on bounded checks, comparison, or review rather than broad unverified mutation.

### Low-attention path

Low-attention delegation is only safe when scope, permissions, and stop conditions are narrower than they would be in supervised work.

### Production-quality path

Production work requires explicit evidence, diff review, rollback planning, and refusal to treat summaries as approval.

### Prototype versus production

Prototype shortcuts can be rational when they are isolated and disposable. Production shortcuts need documented guardrails or rejection.

### Maintenance phase

Maintenance work should reduce repeated shortcut risk by encoding durable commands, review criteria, and do-not rules after the shortcut recurs.

## Stable Core

- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls than prototypes

## Volatile Surface

- package ecosystem health
- vulnerability databases
- lockfile formats
- Codex package suggestions
- vendor docs and release cadence

## Obsolescence Watch

This card should be revised if:

- dependency ecosystems become fully verified, low-maintenance, and automatically risk-scored at install time

## Evidence and Sources

- `openai.codex.use_cases.dependency_incident_audits` — Official OpenAI Codex dependency-incident audit use case for read-only manifest, lockfile, CI, and evidence review.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, done-when criteria, testing, review, and permission posture.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.concepts.dependency`
- `vcb.workflow.dependency_decisions`
- `vcb.workflow.dependency_update_review`
- `vcb.failure.dependency_bloat`
- `vcb.constraints.build_vs_maintenance`
- `vcb.constraints.review_budget`

<!-- VCB:STOP_RETRIEVAL reason="adding_dependencies_fast_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.adding_dependencies_fast -->
