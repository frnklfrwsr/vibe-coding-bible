<!-- VCB:BEGIN_TOPIC id=vcb.failure.ci_false_confidence version=0.1.0 -->
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
id: vcb.failure.ci_false_confidence
title: CI False-Confidence Loop
type: failure_mode
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex CLI
- Codex GitHub Action
- GitHub Actions
- CI
- Release pipelines
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.overbroad_ci_permissions
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.unattended_mutation
- vcb.shortcut.long_lived_ci_secrets
durable_principles:
- CI proves only the checks that ran
- automation needs least privilege
- summaries need artifact-backed evidence
likely_to_change:
- Codex non-interactive flags
- GitHub Actions syntax and permissions
- CI provider UI labels
- artifact retention behavior
obsolete_when:
- CI systems can guarantee complete relevant coverage and safe agent permissions automatically
related_topics:
- vcb.workflow.ci_triage
- vcb.workflow.ci_noninteractive
- vcb.workflow.testing
- vcb.safety.secrets
- vcb.safety.production_red_lines
---

> Summary:
> A CI false-confidence loop happens when green or agent-generated checks create confidence that the change is safe even though the wrong checks ran, checks were bypassed, permissions were too broad, or output was not reviewed.

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

<!-- VCB:BEGIN_SECTION id=vcb.failure.ci_false_confidence.human -->
## 1. For the Human: Plain-Language Concept

### What this means

CI is a robot that runs checks. It is useful, but it only proves the checks it actually ran. If the wrong job runs, if tests are weak, if Codex edits the workflow to pass itself, or if a summary hides details, green is not safe.

### Why it matters

Non-interactive agents and CI can be powerful. They can also produce neat outputs that hide missing coverage, skipped jobs, overbroad permissions, and unreviewed mutations.

### The mental model

CI is a smoke detector, not a building inspector. It must be installed in the right rooms and not allowed to silence itself.

### What good looks like

Good: “Run Codex in read-only CI to summarize risk, then require existing tests, least permissions, artifacts, and human review before mutation or merge.”

### What bad looks like

Bad: a workflow lets Codex patch code, edit tests, broaden permissions, and post “all good” with no artifact review.

### Minimal example

Ask Codex to name the evidence it used, the assumption it is making, the files it changed, and the verification that would catch this failure mode if it were wrong.

### Checklist

- right checks ran
- skips not introduced
- permissions least-privilege
- artifacts/logs reviewed
- agent cannot self-approve risky mutation
<!-- VCB:END_SECTION id=vcb.failure.ci_false_confidence.human -->

<!-- VCB:BEGIN_SECTION id=vcb.failure.ci_false_confidence.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that CI confidence is conditional evidence, not a blanket approval.

### Diagnose the human’s current model

- Which checks ran and which did not?
- Did Codex change the workflow or tests?
- What permissions did the job have?
- Is the output a summary or artifact-backed evidence?
- Can a human reproduce the failure or success locally?

### Explanation strategy

Separate CI triage, CI mutation, and CI approval. Require least privilege, structured outputs, artifact links, and human gate for risky writes.

### Useful metaphor

CI is a smoke detector, not a building inspector. It must be installed in the right rooms and not allowed to silence itself.

### Coaching tactics

- slow the human down at the first unsupported assumption
- ask for artifact-backed evidence instead of a verbal assurance
- separate read-only diagnosis from mutation
- require a smaller diff when review quality drops
- turn repeated misses into durable guidance only after the pattern is verified

### Prompt patterns

```text
In CI, inspect only. Summarize failed/passed checks, skipped jobs, changed workflow files, permissions, and artifacts. Do not edit code or tests. Flag any false-confidence risks before proposing a patch.
```

### Red flags to call out directly

- Codex edits CI config to make itself pass
- test jobs are skipped or narrowed silently
- workflow permissions broaden
- final summary has no logs/artifacts
- green CI follows test weakening

### Exercises

- Ask the human to read a passing CI run and identify what it did not test.
- Ask the human to write one “stop condition” that would make Codex pause instead of pushing through.
- Review a previous agent diff and classify which evidence was missing.
<!-- VCB:END_SECTION id=vcb.failure.ci_false_confidence.ai_coach -->

## Shortcut Reality

### The ideal practice

Use CI as evidence with explicit scope, least privilege, immutable logs, and human review.

### What users often do instead

Users treat green checks or a polished agent summary as enough.

### When the shortcut may be fine

A CI summary can be enough for low-risk documentation or formatting changes when the diff confirms scope.

### When the shortcut is a bad idea

It is a bad trade for deployments, permissions, generated patches, workflow edits, secrets, or production-risk code.

### Risk profile

- Probability of failure: Medium; automation hides omitted checks and permission drift.
- Impact if it fails: High when unsafe code merges or credentials/workflows are exposed.
- Ease of recovery: Good if logs/artifacts are retained; poor if mutation and approval are blended.
- Blast radius: Merge gate, test trust, workflow permissions, secrets, release pipeline, and production deploy path.
- Skill needed to recover: Medium to high; recovery requires CI, security, and git history inspection.
- Hidden cost: Flaky gates, normalized bypassing, overprivileged workflows, and bad release muscle memory.

### Minimum guardrails

- least privilege
- read-only triage mode
- artifact-backed summary
- workflow diff review
- human merge gate

### Recovery plan

- Freeze merge or deploy.
- Inspect workflow/test diffs.
- Re-run full checks from a trusted branch.
- Restore least permissions.
- Add a gate preventing agent self-approval.

## Budget and Constraint Notes

### Cheapest reliable path

Run targeted CI triage before paying for agent patches. Logs are cheaper than wrong mutations.

### Fastest high-usage path

High-throughput users can automate summaries, but mutation should remain constrained and auditable.

### Low-attention path

Low-attention CI runs should be report-only unless the workflow has mature guardrails.

### Production-quality path

Production CI needs least privilege, required checks, artifact retention, review, and rollback gates.

### Prototype versus production

Prototype CI can be light. Production CI must not let the same automation weaken the gate it depends on.

### Maintenance phase

In maintenance, CI false confidence is cumulative. Periodically review skipped tests, permissions, and agent-authored workflow changes.

## Stable Core

- CI proves only the checks that ran
- automation needs least privilege
- summaries need artifact-backed evidence

## Volatile Surface

- Codex non-interactive flags
- GitHub Actions syntax and permissions
- CI provider UI labels
- artifact retention behavior

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- CI systems can guarantee complete relevant coverage and safe agent permissions automatically

## Evidence and Sources

- `openai.codex.noninteractive` — Official OpenAI Codex documentation for non-interactive script/CI use, sandbox settings, and structured output.
- `openai.codex.github_action` — Official OpenAI Codex GitHub Action documentation for CI/CD use and workflow permissions.
- `github.docs.actions_ci` — Official GitHub Actions documentation for CI running build/test workflows and exposing results.
- `github.docs.github_token` — Official GitHub documentation for GITHUB_TOKEN authentication and workflow permissions.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable failure-mode, risk, review, budget, and recovery discipline.

## Related Topics

- `vcb.workflow.ci_triage`
- `vcb.workflow.ci_noninteractive`
- `vcb.workflow.testing`
- `vcb.safety.secrets`
- `vcb.safety.production_red_lines`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.failure.ci_false_confidence -->
