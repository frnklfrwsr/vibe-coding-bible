<!-- VCB:BEGIN_TOPIC id=vcb.constraints.production_quality version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex constraint, planning, review, and pricing anchors plus VCB
  maintainer synthesis for budget, attention, recovery, and phase-control guidance
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
id: vcb.constraints.production_quality
title: Production-Quality Constraints
type: concept
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- production builds
- security review
- release gates
- CI
- observability
- maintenance
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_security_review
- vcb.shortcut.manual_testing_only
- vcb.shortcut.skipping_pr_review
durable_principles:
- production quality is a constraint set, not an aesthetic label
- real-user risk requires verification, review, rollback, and monitoring
- prototype evidence is not enough for production acceptance
likely_to_change:
- Codex review and security surfaces
- deployment platform UI
- current CI/check tooling
- plan-specific product availability
obsolete_when:
- production systems can be changed safely without human-defined constraints, verification, or
  rollback
related_topics:
- vcb.safety.production_red_lines
- vcb.safety.security_review
- vcb.safety.secrets
- vcb.workflow.testing
- vcb.workflow.ci_triage
- vcb.concepts.observability
- vcb.constraints.recovery_budget
- vcb.constraints.review_budget
---

# Production-Quality Constraints

> Summary:
> Production quality means the work is safe enough for real users, maintainers, data, and operations. It requires evidence, rollback, security posture, observability, and ownership, not just working demo behavior.

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

<!-- VCB:BEGIN_SECTION id=vcb.constraints.production_quality.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Production-quality constraints are the rules that must be true before code affects real users or live systems: tests, review, security checks, rollback, monitoring, docs, and clear ownership.

### Why it matters

Codex can produce working code quickly. Production quality asks a different question: can this change fail safely, be understood later, and be trusted by people who did not watch it being generated?

### The mental model

A demo asks “does it work once?” Production asks “what happens when it fails at 2 a.m.?”

### What good looks like

Good: “Before merge, show diff risk, tests run, security-sensitive paths, rollback plan, observability impact, and anything not verified.”

### What bad looks like

Bad: “It works locally; ship it.”

### Minimal example

For production, require evidence across five gates: behavior, security, data, rollback, and observability.

### Checklist

- acceptance criteria are explicit
- tests/checks match risk
- secrets and permissions are reviewed
- rollback path exists
- observability or support impact is known

<!-- VCB:END_SECTION id=vcb.constraints.production_quality.human -->

<!-- VCB:BEGIN_SECTION id=vcb.constraints.production_quality.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Coach the human to define production quality as concrete gates. Reject “production-ready” unless the claim is backed by task-shaped evidence.

### Diagnostic questions

- Does this affect real users or persistent data?
- What tests and manual checks cover the change?
- What security or trust boundary changed?
- How will the team know if it fails?
- How can it be rolled back?

### Coaching tactics

- turn production readiness into an evidence table
- force security and data-risk questions early
- require “not verified” lines
- keep release notes and docs tied to the diff
- escalate if the agent proposes production action without approval

### Red flags

- production-ready claim with no checks
- auth/payment/data path changed without security review
- manual-only testing on critical behavior
- no rollback or monitoring note
- feature maturity ignored for production dependency

### Prompt pattern

```text
Assess this change against production-quality constraints. Return a table for behavior, tests, security, data, rollback, observability, docs, and unresolved risk. Do not call it production-ready unless each required gate has evidence or an explicit owner decision.
```

<!-- VCB:END_SECTION id=vcb.constraints.production_quality.ai_coach -->

## Shortcut Reality

### Ideal practice

Treat production quality as a set of gates that must be satisfied before merge or deploy.

### What people often do instead

Users equate “it runs” or “CI is green” with production readiness.

### When the shortcut may be acceptable

Acceptable only for non-user-facing prototypes, internal experiments, or changes behind isolation/feature flags with no real data risk.

### When it becomes a bad trade

Bad for auth, billing, data deletion, migrations, secrets, permissions, public docs, releases, or customer-visible behavior.

### Risk profile

- Probability: medium if production gates are informal; high when agent summaries replace review.
- Impact: high because production failures affect users and trust.
- Recoverability: depends on rollback, monitoring, and data side effects.

### Blast radius

Weak production constraints can ship security issues, data bugs, misleading docs, support burden, and operational failures.

### Minimum guardrails

- require human approval for production-risk work
- use branch/PR gates
- review secrets and permissions
- run smallest relevant checks plus risk-specific checks
- record rollback and monitoring notes

### Recovery plan

1. Stop deploy or revert if already shipped.
2. Identify which production gate lacked evidence.
3. Run targeted checks and inspect logs.
4. Patch or rollback with owner approval.
5. Update the production-quality checklist.

## Budget and Constraint Notes

### Cheapest reliable path

add production gates only where real user risk exists; do not overprocess toy work.

### Fastest high-usage path

use Codex to draft checklists and evidence tables, but keep human approval on risky gates.

### Low-attention path

production-quality work is not low-attention unless fully isolated and reviewable.

### Production-quality path

budget for security, data, rollback, monitoring, docs, and support impact.

### Prototype versus production

prototypes prove possibility; production constraints prove survivability.

### Maintenance phase

preserve operator knowledge by keeping checks, docs, and rollback notes current.

## Stable Core

- production quality is a constraint set, not an aesthetic label
- real-user risk requires verification, review, rollback, and monitoring
- prototype evidence is not enough for production acceptance

## Volatile Surface

- Codex review and security surfaces
- deployment platform UI
- current CI/check tooling
- plan-specific product availability

Review volatile details against official sources or dated pricing snapshots before freezing commands, UI labels, model choices, plan packaging, context limits, feature availability, exact prices, or exact limits.

## Obsolescence Watch

- production systems can be changed safely without human-defined constraints, verification, or rollback

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for constraints, done-when criteria, planning, reusable guidance, testing, review, permissions, and validation.
- `openai.codex.security_threat_model` — Official OpenAI Codex security threat-model guidance for trust boundaries, auth assumptions, and sensitive data paths.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples for explicit context, validation, and done definitions.
- `openai.codex.feature_maturity` — Official OpenAI Codex feature-maturity guidance for volatile product-surface judgment.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable engineering control loops, risk, review, recovery, and constraint management.

## Related Topics

- `vcb.safety.production_red_lines`
- `vcb.safety.security_review`
- `vcb.safety.secrets`
- `vcb.workflow.testing`
- `vcb.workflow.ci_triage`
- `vcb.concepts.observability`
- `vcb.constraints.recovery_budget`
- `vcb.constraints.review_budget`

<!-- VCB:STOP_RETRIEVAL reason="constraint_topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.constraints.production_quality -->
