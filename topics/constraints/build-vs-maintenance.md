<!-- VCB:BEGIN_TOPIC id=vcb.constraints.build_vs_maintenance version=0.1.0 -->
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
id: vcb.constraints.build_vs_maintenance
title: Build Phase vs Maintenance Phase
type: concept
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- prototype work
- MVPs
- production builds
- maintenance
- refactoring
- documentation
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: HIGHLY_VOLATILE
shortcut_profiles:
- vcb.shortcut.generated_prototype_as_production_foundation
- vcb.shortcut.skipping_maintenance_cleanup
- vcb.shortcut.permanent_high_usage_plan
- vcb.shortcut.overbuilding_first_app
durable_principles:
- build-phase shortcuts become maintenance debt if not retired
- maintenance work values small reversible changes over raw speed
- phase should be stated in prompts because it changes acceptable risk
likely_to_change:
- Codex use-case templates
- product features that support maintenance workflows
- team-specific release cadence
- current review and automation surfaces
obsolete_when:
- AI systems can infer project phase and debt boundaries reliably from repository state without
  human input
related_topics:
- vcb.chapter.build_phase_vs_maintenance_phase
- vcb.workflow.refactoring
- vcb.workflow.documentation_updates
- vcb.workflow.testing
- vcb.failure.broad_refactor_drift
- vcb.failure.dependency_bloat
- vcb.constraints.scope_budget
- vcb.constraints.review_budget
---

# Build Phase vs Maintenance Phase

> Summary:
> Build phase optimizes for learning and forward motion. Maintenance phase optimizes for preserving behavior, reducing surprise, and lowering future cost. Codex prompts must change when the phase changes.

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

<!-- VCB:BEGIN_SECTION id=vcb.constraints.build_vs_maintenance.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Build phase is when you are still discovering shape: features, flows, architecture, and product fit. Maintenance phase is when users, teammates, tests, docs, and production behavior already depend on the system.

### Why it matters

The same Codex behavior can be useful in build phase and harmful in maintenance. A broad generated prototype can teach you fast. A broad maintenance diff can break contracts, confuse future debugging, and create hidden debt.

### The mental model

Building is sketching the map. Maintenance is repairing a bridge while people are driving over it.

### What good looks like

Good: “This is maintenance. Preserve public behavior, change one concern, update tests/docs only where necessary, and flag anything that looks like a larger redesign.”

### What bad looks like

Bad: “Refactor this old area and modernize anything you see.”

### Minimal example

Start prompts with the phase: prototype, MVP, production build, maintenance, major refactor, or emergency hotfix.

### Checklist

- phase is declared
- acceptable shortcut level matches phase
- public behavior boundaries are explicit
- tests/docs expectations match phase
- debt created or retired is named

<!-- VCB:END_SECTION id=vcb.constraints.build_vs_maintenance.human -->

<!-- VCB:BEGIN_SECTION id=vcb.constraints.build_vs_maintenance.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that project phase changes what “good” means. Build-phase velocity is not the same as maintenance-phase quality.

### Diagnostic questions

- Is this exploratory or preserving existing behavior?
- Who relies on the current behavior?
- Are tests/docs/contracts already public?
- Is the user asking for cleanup that should be a separate refactor?
- What debt is acceptable temporarily?

### Coaching tactics

- prefix prompts with phase
- allow disposable shortcuts only in prototypes
- require behavior-preservation language in maintenance
- separate redesign from repair
- ask Codex to list debt introduced or retired

### Red flags

- prototype code treated as production foundation
- maintenance diff includes unrelated rewrites
- tests updated to match new behavior without approval
- docs drift after code changes
- high-usage plan becomes permanent process crutch

### Prompt pattern

```text
This task is in [prototype / MVP / production build / maintenance / hotfix] phase. Adapt your behavior to that phase. State what shortcuts are acceptable, what behavior must be preserved, what evidence is required, and what debt will remain.
```

<!-- VCB:END_SECTION id=vcb.constraints.build_vs_maintenance.ai_coach -->

## Shortcut Reality

### Ideal practice

Use phase-appropriate speed: explore in build phase, preserve in maintenance.

### What people often do instead

Users keep prompting like they are prototyping after the app has users and history.

### When the shortcut may be acceptable

Acceptable to move fast in prototypes when code is disposable and risk is low.

### When it becomes a bad trade

Bad when prototype shortcuts become permanent architecture, auth, data, or payment foundations.

### Risk profile

- Probability: medium when phase is unstated; high when old code is treated as blank slate.
- Impact: low for throwaway prototypes; high for maintenance behavior drift.
- Recoverability: good before users depend on behavior; weaker after docs/tests/integrations rely on it.

### Blast radius

Phase confusion creates debt: generated prototypes become production foundations, maintenance changes expand into rewrites, and future work inherits unclear intent.

### Minimum guardrails

- state phase in prompt
- separate prototype from production branch
- require maintenance behavior preservation
- track debt explicitly
- retire temporary shortcuts before release

### Recovery plan

1. Classify current work by phase.
2. Audit prototype shortcuts that reached production.
3. Split cleanup from feature work.
4. Add tests/docs around behavior that must be preserved.
5. Create a maintenance prompt template.

## Budget and Constraint Notes

### Cheapest reliable path

spend build-phase budget on learning, then stop and harden before production.

### Fastest high-usage path

use high throughput to explore alternatives, not to merge broad unreviewed maintenance diffs.

### Low-attention path

low-attention build exploration is safer than low-attention maintenance mutation.

### Production-quality path

production work budgets for tests, docs, review, rollback, and observability.

### Prototype versus production

prototype shortcuts require an explicit retirement date or replacement gate.

### Maintenance phase

optimize for small diffs, stable APIs, accurate docs, and future debugging cost.

## Stable Core

- build-phase shortcuts become maintenance debt if not retired
- maintenance work values small reversible changes over raw speed
- phase should be stated in prompts because it changes acceptable risk

## Volatile Surface

- Codex use-case templates
- product features that support maintenance workflows
- team-specific release cadence
- current review and automation surfaces

Review volatile details against official sources or dated pricing snapshots before freezing commands, UI labels, model choices, plan packaging, context limits, feature availability, exact prices, or exact limits.

## Obsolescence Watch

- AI systems can infer project phase and debt boundaries reliably from repository state without human input

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex guidance for constraints, done-when criteria, planning, reusable guidance, testing, review, permissions, and validation.
- `openai.codex.use_cases.refactor_your_codebase` — Official OpenAI Codex refactoring use case for small behavior-preserving refactor passes.
- `openai.codex.use_cases.update_documentation` — Official OpenAI Codex documentation-update use case for comparing code, docs, release notes, and verification steps.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable engineering control loops, risk, review, recovery, and constraint management.

## Related Topics

- `vcb.chapter.build_phase_vs_maintenance_phase`
- `vcb.workflow.refactoring`
- `vcb.workflow.documentation_updates`
- `vcb.workflow.testing`
- `vcb.failure.broad_refactor_drift`
- `vcb.failure.dependency_bloat`
- `vcb.constraints.scope_budget`
- `vcb.constraints.review_budget`

<!-- VCB:STOP_RETRIEVAL reason="constraint_topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.constraints.build_vs_maintenance -->
