<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.accepting_looks_done version=0.1.0 -->
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
id: vcb.shortcut.accepting_looks_done
title: Accepting Looks Done
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex final summaries
- diff review
- frontend checks
- bug fixes
- pull requests
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- review
- completion evidence
- acceptance criteria
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
- completion-evidence table
- changed-file review
- one relevant check
- explicit not-verified list
shortcut_profiles:
- vcb.shortcut.accepting_looks_done
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls
  than prototypes
likely_to_change:
- current Codex completion-summary style
- review pane labels
- available browser/screenshot evidence surfaces
- model confidence patterns
obsolete_when:
- Codex completion summaries become automatically complete, auditable, and acceptance-criteria
  scoped
related_topics:
- vcb.prompting.acceptance_criteria
- vcb.workflow.codex_output_review
- vcb.workflow.reviewing_diffs
- vcb.failure.done_claim_without_evidence
- vcb.workflow.visual_qa
- vcb.constraints.production_quality
---

# Accepting Looks Done

> Summary:
> Accepting “looks done” is treating a polished agent response or superficially plausible UI/code result as completion evidence.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.accepting_looks_done.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut happens when Codex sounds confident, the app appears to load, or the diff looks tidy, so you stop before checking the actual acceptance criteria.

### Why it matters

The failure is not cosmetic. “Looks done” can hide missing edge states, skipped tests, broken auth paths, wrong data, or a summary that never tied changes to evidence.

### What good looks like

Good: “Show changed files, acceptance criteria satisfied, verification run, verification not run, and remaining risks.”

### What bad looks like

Bad: “It says implemented and the screenshot looks okay.”

### Minimal example

For a checkout button, a screenshot of the button is not enough; verify empty cart, disabled state, success path, failure path, and relevant logs or tests.

### Checklist

- define done before accepting output
- ask for changed files and evidence
- verify at least the main path
- list unverified paths
- treat polished summaries as hypotheses until proven

<!-- VCB:END_SECTION id=vcb.shortcut.accepting_looks_done.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.accepting_looks_done.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to separate presentation quality from engineering evidence. A clean answer is not a passing check.

### Diagnostic questions

- What exact claim is being accepted?
- Which acceptance criterion backs that claim?
- What evidence exists besides prose?
- Was the risky path checked or only the happy path?
- Could this be wrong while still looking good?

### Coaching tactics

- convert final answer into an evidence table
- ask for not-verified items before merge
- require screenshot/browser evidence for UI work
- require repro/check output for bugs
- tie every “done” claim to a file, command, log, or screenshot

### Red flags

- implemented and tested with no output
- single screenshot for multi-state UI
- no changed-file summary
- ready-to-merge claim without diff review
- acceptance criteria added after the fact

### Prompt pattern

```text
Before I accept this, produce a completion-evidence table: changed file, intended behavior, acceptance criterion, check performed, result, not verified, and residual risk. Do not call it done if required evidence is missing.
```

<!-- VCB:END_SECTION id=vcb.shortcut.accepting_looks_done.ai_coach -->

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

- completion-evidence table
- changed-file review
- one relevant check
- explicit not-verified list

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

- current Codex completion-summary style
- review pane labels
- available browser/screenshot evidence surfaces
- model confidence patterns

## Obsolescence Watch

This card should be revised if:

- Codex completion summaries become automatically complete, auditable, and acceptance-criteria scoped

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, done-when criteria, testing, review, and permission posture.
- `openai.codex.app_review` — Official OpenAI Codex app review guidance for changed files, diff inspection, staging, and review-pane workflow.
- `openai.codex.workflows` — Official OpenAI Codex workflow guidance for context, definition of done, reproduction, and verification loops.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.prompting.acceptance_criteria`
- `vcb.workflow.codex_output_review`
- `vcb.workflow.reviewing_diffs`
- `vcb.failure.done_claim_without_evidence`
- `vcb.workflow.visual_qa`
- `vcb.constraints.production_quality`

<!-- VCB:STOP_RETRIEVAL reason="accepting_looks_done_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.accepting_looks_done -->
