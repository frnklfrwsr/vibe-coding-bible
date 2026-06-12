<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.ignoring_lint_typecheck version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-12'
last_reviewed: '2026-06-12'
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
evidence_scope: official OpenAI/Codex guidance, TypeScript/ESLint/npm documentation anchors, and VCB maintainer synthesis for risk-managed shortcut harm reduction
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
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.shortcut.ignoring_lint_typecheck
title: Ignoring Lint and Typecheck
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-12'
applies_to:
- lint
- typecheck
- CI
- TypeScript
- JavaScript
- changed-file verification
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- verification
- lint
- typecheck
- CI
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
- run nearest check
- separate old failures
- fix changed-file failures
- do not suppress rules silently
shortcut_profiles:
- vcb.shortcut.ignoring_lint_typecheck
durable_principles:
- fast static checks catch cheap mistakes
- old failures are not permission to add new failures
- suppressing checks is a code change that needs review
likely_to_change:
- project-specific check commands
- lint and typecheck tool versions
- CI check names and coverage
- model ability to infer command intent
obsolete_when:
- generated code can be trusted without static or equivalent project-specific verification
related_topics:
- vcb.workflow.testing
- vcb.workflow.ci_triage
- vcb.concepts.typecheck
- vcb.concepts.lint
- vcb.concepts.ci
- vcb.failure.ci_false_confidence
---

# Ignoring Lint and Typecheck

> Summary:
> Ignoring lint and typecheck is accepting code while static checks are failing or unrun, without separating old noise from new failures.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.ignoring_lint_typecheck.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut happens when Codex changes code and you skip or ignore lint, typecheck, build, or similar fast static checks. It also happens when there are old failures and nobody checks whether the new work added more.

### Why it matters

Static checks are cheap tripwires. They catch broken imports, wrong types, dead variables, formatting rules, unsafe patterns, and build assumptions before a human has to debug runtime behavior.

### What good looks like

Good: "Run the nearest lint/typecheck/build command. Separate pre-existing failures from failures introduced by this diff."

### What bad looks like

Bad: "Lint was already red, so ignore it."

### Minimal example

If `npm run typecheck` has 30 old errors, rerun it after the change and verify the count, files, or failure class did not worsen in changed files.

### Checklist

- run the nearest relevant static check
- record command and result
- classify old versus new failures
- fix failures caused by changed files
- do not weaken or suppress rules without review

<!-- VCB:END_SECTION id=vcb.shortcut.ignoring_lint_typecheck.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.ignoring_lint_typecheck.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that noisy checks still contain useful signal when the review asks what changed.

### Diagnostic questions

- Which check is nearest to the edited files?
- Did the command fail before this change?
- Are any failures in changed files?
- Did Codex add a suppression, config change, or weaker rule?
- Is CI green because the right check ran, or because the check is missing?

### Coaching tactics

- ask for changed-file static checks before broad cleanup
- separate baseline noise from new failures
- prohibit blanket ignores during feature work
- treat config/rule changes as high-review edits
- suggest a follow-up cleanup issue for old failures instead of hiding new ones

### Red flags

- lint or typecheck not run for typed code changes
- "existing failure" with no baseline comparison
- new `any`, ignore comments, disabled rules, or skipped checks
- CI configured green but local nearest check fails
- generated tests pass while typecheck fails

### Prompt pattern

```text
Run the nearest lint/typecheck/build check for the changed files. If it fails, classify failures as pre-existing or introduced by this change. Do not add suppressions or weaken config unless explicitly approved.
```

<!-- VCB:END_SECTION id=vcb.shortcut.ignoring_lint_typecheck.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They skip static checks because they are noisy, slow, unfamiliar, or already failing.

### When the shortcut may be acceptable

Acceptable for throwaway prototypes or docs-only edits where static checks cannot apply and the output is not treated as merge-ready.

### When it becomes a bad trade

Bad for typed code, build changes, public apps, shared repos, CI workflows, dependencies, generated code, and production-facing behavior.

### Risk profile

- Probability: medium for small edits; high when generated code changes types, imports, config, or build paths.
- Impact: low for disposable local experiments; high for shared branches and production builds.
- Recoverability: good before merge; worse after static failures become mixed with unrelated cleanup.

### Blast radius

Ignoring static checks can normalize broken builds, hide generated mistakes, and turn cheap local errors into CI churn or production defects.

### Minimum guardrails

- run nearest check
- separate old failures
- fix changed-file failures
- do not suppress rules silently

### Recovery plan

1. Re-run the nearest static check.
2. Capture current failures.
3. Compare against baseline if available.
4. Fix failures introduced by changed files.
5. Revert suppressions or config changes that were not approved.
6. File old unrelated failures separately.

## Budget and Constraint Notes

### Cheapest reliable path

Run the narrow static check before broad tests or manual review.

### Fastest high-usage path

High-throughput users should automate recurring static checks, but still inspect whether the right check ran.

### Low-attention path

Low-attention runs should return command, result, and old/new failure classification.

### Production-quality path

Production work should not merge with new lint/typecheck/build failures unless there is a documented exception and owner.

### Prototype versus production

Prototype code can carry temporary rough edges. Production code needs static-check accountability.

### Maintenance phase

Maintenance work should reduce noisy checks over time, not use noise as a reason to ignore new failures.

## Stable Core

- fast static checks catch cheap mistakes
- old failures are not permission to add new failures
- suppressing checks is a code change that needs review

## Volatile Surface

- project-specific check commands
- lint and typecheck tool versions
- CI check names and coverage
- model ability to infer command intent

## Obsolescence Watch

This card should be revised if:

- generated code can be trusted without static or equivalent project-specific verification

## Evidence and Sources

- `openai.codex.best_practices` - Official OpenAI Codex guidance for validation and review.
- `npm.docs.scripts` - Official npm documentation for script commands and lifecycle-script behavior.
- `typescript.docs.home` - Official TypeScript documentation anchor for type checking.
- `eslint.docs.home` - Official ESLint documentation anchor for linting JavaScript code problems.
- `vcb.synthesis.stable_engineering_practice` - VCB maintainer synthesis for durable risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.workflow.testing`
- `vcb.workflow.ci_triage`
- `vcb.concepts.typecheck`
- `vcb.concepts.lint`
- `vcb.concepts.ci`
- `vcb.failure.ci_false_confidence`

<!-- VCB:STOP_RETRIEVAL reason="ignoring_lint_typecheck_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.ignoring_lint_typecheck -->
