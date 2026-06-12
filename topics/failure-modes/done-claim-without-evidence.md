<!-- VCB:BEGIN_TOPIC id=vcb.failure.done_claim_without_evidence version=0.1.0 -->
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
evidence_scope: official Codex guidance on done-when criteria, workflows, review evidence, and VCB synthesis for completion-proof failure modes
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
id: vcb.failure.done_claim_without_evidence
title: Done Claim Without Evidence
type: failure_mode
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- prompting
- review
- testing
- CI
- Codex App
- Codex CLI
- maintenance
stability:
  principle: AGENTIC_PRINCIPLE
  surface: STABLE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.reviewing_cloud_summary_only
- vcb.shortcut.skipping_tests
durable_principles:
- completion is a claim until it is tied to changed files, checks, and acceptance criteria
- evidence should be task-specific, not generic confidence language
- review cost is lower before an unsupported done claim spreads into merge, release, or documentation decisions
likely_to_change:
- current Codex product UI wording for completion summaries
- supported review panes, browser checks, and automation surfaces
- model-specific confidence patterns
obsolete_when:
- agentic tooling can produce complete, verifiable, task-scoped proof of completion without human review
related_topics:
- vcb.prompting.acceptance_criteria
- vcb.workflow.codex_output_review
- vcb.workflow.reviewing_diffs
- vcb.workflow.testing
- vcb.workflow.ci_triage
- vcb.failure.ci_false_confidence
---

# Done Claim Without Evidence

<!-- VCB:BEGIN_SECTION id=vcb.failure.done_claim_without_evidence.structure_notice -->
> This is an atomic failure-mode card. Prefer it over broad chapters when the user needs to diagnose a confident completion summary, merge-ready claim, or polished agent response that is not backed by concrete proof.
<!-- VCB:END_SECTION id=vcb.failure.done_claim_without_evidence.structure_notice -->

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

<!-- VCB:BEGIN_SECTION id=vcb.failure.done_claim_without_evidence.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A done claim without evidence happens when Codex says the task is complete, fixed, implemented, or verified, but the answer does not show the proof needed to trust that claim.

### Why it matters

The dangerous part is not that the model is confident. The dangerous part is that confident language can replace the control loop: changed files, diff review, acceptance criteria, tests, repro steps, browser checks, or CI output.

### What good looks like

Good: “I changed these files, this is the acceptance criterion each change satisfies, these checks ran, this check did not run, and this risk remains.”

### What bad looks like

Bad: “Implemented and tested” with no file list, no test command, no output, no screenshot, no repro, and no explanation of what was not checked.

### Minimal example

Ask Codex: “Do not say done yet. Give me a completion-evidence table with changed files, acceptance criteria, verification performed, verification not performed, and remaining risk.”

### Checklist

- Identify the exact claim Codex is making.
- Ask what file, diff, test, log, repro, screenshot, or CI result supports it.
- Separate “implemented,” “compiled,” “tested,” “reviewed,” and “ready to merge.”
- Require an explicit “not verified” line for anything not checked.
- Treat unsupported claims as review prompts, not merge approval.

<!-- VCB:END_SECTION id=vcb.failure.done_claim_without_evidence.human -->

<!-- VCB:BEGIN_SECTION id=vcb.failure.done_claim_without_evidence.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Coaching stance

Teach the human to downgrade completion summaries into hypotheses until there is task-shaped evidence. The goal is not to distrust every agent output; it is to prevent confidence language from bypassing the engineering loop.

### Diagnostic questions

- What exactly is Codex claiming is done?
- Which acceptance criterion does each changed file satisfy?
- Which verification was run, and what was the output?
- Which verification was skipped, impossible, or out of scope?
- What would make this claim false in production?

### Coaching tactics

- Convert the final answer into an evidence table.
- Ask for “proof before polish”: changed files, checks, failures, non-checks, and residual risk.
- For UI work, require browser or screenshot evidence, not just a code diff.
- For bug fixes, require the same-path reproduction to fail before and pass after, when feasible.
- For CI, require scope: which checks ran and what they actually cover.

### Red flags

- “All tests pass” with no command or output.
- “Implemented” with no changed-file list.
- “Fixed” without a reproduction path.
- “Ready to merge” without diff review or risk notes.
- “Minor change” on auth, payments, data deletion, production config, or dependency updates.

### Prompt pattern

```text
Before you claim this is done, produce a completion-evidence table:
- changed file
- intended behavior
- acceptance criterion satisfied
- verification command or manual check
- result
- what was not verified
- residual risk
Do not mark the task done if any required acceptance criterion lacks evidence.
```

<!-- VCB:END_SECTION id=vcb.failure.done_claim_without_evidence.ai_coach -->

## Shortcut Reality

### Ideal practice

Completion claims should be backed by task-specific evidence before the human treats the work as ready.

### What people often do instead

They accept a polished final response, skim the diff, and move on because the answer sounds organized and confident.

### When the shortcut may be acceptable

This can be acceptable for disposable prototypes, throwaway experiments, or low-risk local cleanup where rollback is trivial and no user data, auth, billing, production config, or dependency surface is touched.

### When it becomes a bad trade

It is a bad trade when the task affects production behavior, security, data integrity, public docs, dependencies, releases, or anything that another human will rely on as true.

### Risk profile

- Probability: medium to high when prompts lack explicit done-when criteria.
- Impact: low for throwaway demos; high for production, security, CI, or release workflows.
- Recoverability: good before merge; worse after release, documentation publication, or dependency rollout.

### Blast radius

Unsupported done claims can propagate into merged code, false release notes, skipped QA, stale documentation, and future debugging sessions that assume the work was actually verified.

### Minimum guardrails

- Require changed-file and verification summaries.
- Require explicit “not verified” lines.
- For production work, require human diff review.
- For UI, require browser/screenshot evidence where practical.
- For bugs, require same-path repro verification where practical.

### Recovery plan

1. Reopen the task as “claimed done, evidence missing.”
2. Ask Codex to reconstruct the evidence table from the diff and logs.
3. Run the smallest relevant checks manually or in CI.
4. Revert or isolate unsupported changes before expanding the task.
5. Update the prompt template so future completion claims require proof.

## Budget and Constraint Notes

### Cheapest reliable path

Add one sentence to every serious prompt: “Do not say done unless you can list changed files, checks run, checks skipped, and remaining risk.” This costs little and prevents expensive review drift.

### Fastest high-usage path

Use a standard completion-evidence table for every Codex task. It keeps high-throughput work reviewable without custom review prompts each time.

### Low-attention path

Low-attention delegation is only acceptable if the agent’s final response is evidence-structured and the task runs in a low-blast-radius branch or sandbox.

### Production-quality path

Production work needs evidence from diff review, tests or reproducible checks, and risk notes. A completion summary is not a deployment gate.

### Prototype versus production

Prototype: a clear caveat may be enough. Production: unsupported done claims should block merge or release until verified.

### Maintenance phase

In maintenance, unsupported done claims create long-lived false assumptions. Require evidence now because future maintainers will not know which parts were actually checked.

## Stable Core

- Done means acceptance criteria are satisfied with evidence.
- Agent confidence is not verification.
- Review should distinguish implemented, tested, reviewed, and releasable.
- Missing evidence should be explicit, not hidden behind positive language.
- Smaller tasks produce cheaper, clearer completion evidence.

## Volatile Surface

- Codex completion-summary format and UI labels can change.
- Review panes, browser tooling, and CI integrations can change.
- Model behavior around confidence and caveats can change.
- Exact command names and platform-specific verification workflows can change.

## Obsolescence Watch

Re-check this card if official Codex guidance introduces structured completion proofs, if automated verification becomes strongly tied to task acceptance criteria, or if repository tools can reliably block unsupported done claims.

## Evidence and Sources

- `openai.codex.best_practices` — official guidance for prompts with goal, context, constraints, and done-when criteria.
- `openai.codex.workflows` — official workflow guidance for reproduction, checks, and post-change verification.
- `openai.codex.app_review` — official review-surface guidance for diff-centered review and staged/reverted changes.
- `openai.codex.use_cases.qa_computer_use` — official QA-output guidance with flows, repro steps, expected results, actual results, and severity.
- VCB maintainer synthesis — stable engineering control-loop guidance for completion proof and failure-mode recovery.

## Related Topics

- `vcb.prompting.acceptance_criteria`
- `vcb.workflow.codex_output_review`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.testing`
- `vcb.workflow.ci_triage`
- `vcb.failure.ci_false_confidence`

<!-- VCB:STOP_RETRIEVAL reason="failure_mode_card_complete" -->
<!-- VCB:END_TOPIC id=vcb.failure.done_claim_without_evidence -->
