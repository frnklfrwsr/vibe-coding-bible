<!-- VCB:BEGIN_TOPIC id=vcb.workflow.codex_output_review version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex and vendor documentation anchors plus VCB maintainer synthesis for risk, budget, and coaching guidance
budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget
cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- unattended_high_throughput
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
id: vcb.workflow.codex_output_review
title: Codex Output Review Workflow
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- Git
- Pull requests
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.reviewing_cloud_summary_only
- vcb.shortcut.skipping_tests
durable_principles:
- the diff is the source of truth for code changes
- a summary is not evidence
- review intensity should scale with blast radius
likely_to_change:
- Codex review-pane UI
- summary format
- available review scopes
- surface-specific commands
obsolete_when:
- Codex can produce formally verified changes and trustworthy risk proofs without human review
related_topics:
- vcb.chapter.reviewing_codex_output
- vcb.workflow.reviewing_diffs
- vcb.codex.app
- vcb.codex.cloud
- vcb.concepts.diff
- vcb.workflow.testing
---

> Summary:
> Reviewing Codex output means inspecting the actual diff, commands, tests, and risks instead of accepting a confident summary.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.codex_output_review.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Codex output review is the step where you stop reading the assistant’s confident explanation and inspect what actually changed. The output is not just the final message. It includes the diff, commands run, tests passed or skipped, files touched, and unresolved risks.

### Why it matters

AI-generated code can be internally consistent and still wrong. Review catches mistakes that do not look like syntax errors: changed behavior, missing edge cases, deleted checks, overbroad edits, and security-sensitive assumptions.

### The mental model

Treat Codex like a fast junior engineer who wrote a patch and a status note. The note helps you navigate, but the patch is what gets reviewed.

### What good looks like

Good: “Show me the diff grouped by behavior. Explain each file changed, tests run, tests not run, and risky assumptions. Do not mark this done until I review the diff.”

### What bad looks like

Bad: “Looks good, ship it” after reading only Codex’s completion summary.

### Minimal example

A login fix should return: changed files, the exact auth behavior changed, targeted test or manual repro evidence, what was not checked, and a small diff you can read in one sitting.

### Checklist

- read the actual diff, not only the summary
- compare changes to the original task and acceptance criteria
- check for unrelated files or broad refactors
- confirm tests/checks were run or explicitly skipped
- look for deleted assertions, weakened validation, and new dependencies
- record unresolved risks before merge or handoff
<!-- VCB:END_SECTION id=vcb.workflow.codex_output_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.codex_output_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to separate “Codex says it is done” from “the work has evidence.”

### Diagnose the human’s current model

- Did the human inspect the diff?
- What acceptance criteria did the output satisfy?
- Which files changed outside the intended scope?
- What checks were run, and what was skipped?
- Does the summary hide uncertainty or risk?

### Explanation strategy

Start with an evidence ladder: diff, commands, test output, final report, and unresolved gaps. Make the human review the smallest artifact that could falsify Codex’s claim. Escalate for auth, data, payments, secrets, migrations, deployments, or public API behavior.

### Useful metaphor

The Codex summary is a map. The diff is the terrain.

### Coaching tactics

- ask for a diff walkthrough before accepting a patch
- force Codex to label confidence versus evidence
- use file-by-file review for small diffs and risk-area review for larger diffs
- reject “done” when checks are absent without a reason
- turn recurring misses into AGENTS.md or prompt-library guidance

### Prompt patterns

```text
Review your own output before I do.
List: changed files, intended behavior change, unintended or broad changes, tests/checks run, checks not run, risk areas, and rollback path.
Then show the diff grouped by behavior. Do not summarize risk away.
```

### Red flags to call out directly

- final answer says “done” but names no checks
- large diff with no plan or no file grouping
- new dependency, permission, migration, auth path, or data write hidden in the patch
- deleted tests or weaker assertions
- cloud/task summary reviewed without opening the actual diff

### Exercises

- Give the human a generated patch and ask them to find one unrelated edit.
- Ask them to classify each changed file as intended, support, or suspicious.
- Practice requiring a final report with checks run and checks not run.
<!-- VCB:END_SECTION id=vcb.workflow.codex_output_review.ai_coach -->

## Shortcut Reality

### The ideal practice

Review the actual patch and verification evidence before accepting Codex output.

### What users often do instead

Users read the completion summary and assume the implementation matches the request.

### When the shortcut may be fine

Summary-only review may be acceptable for throwaway notes, docs drafts, or disposable prototype code that will not be merged.

### When the shortcut is a bad idea

It is a bad trade for shared code, production behavior, auth, data, money movement, security-sensitive logic, migrations, CI, or dependency changes.

### Risk profile

- Probability of failure: Medium; higher when the prompt was vague, context was stale, or the diff is broad.
- Impact if it fails: High when mistakes reach production, leak secrets, weaken security checks, or corrupt data.
- Ease of recovery: Good when work is branch-isolated and small; poor when several unreviewed patches are stacked.
- Blast radius: Every file Codex changed plus every behavior those files control.
- Skill needed to recover: Low for reading small diffs; medium for judging tests; high for security, data, and deployment review.
- Hidden cost: False confidence, regression debt, noisy future debugging, and expensive post-merge cleanup.

### Minimum guardrails

- require a diff
- require checks run or gaps listed
- reject unrelated edits
- keep work on a branch or worktree
- escalate high-risk files to human review

### Recovery plan

- Stop adding new changes.
- Compare the diff against the original request.
- Revert unrelated or risky edits.
- Run targeted checks.
- Add a regression test or review rule for the miss.

## Budget and Constraint Notes

### Cheapest reliable path

Ask for a concise diff walkthrough and run the smallest targeted check that proves the changed behavior.

### Fastest high-usage path

High-usage users can ask Codex to produce a structured self-review first, then spend human attention only on high-risk files and failing checks.

### Low-attention path

Low-attention delegation must return a reviewable diff, final report, checks run, and known gaps. A summary alone is not a handoff.

### Production-quality path

Production work needs human diff review, passing relevant checks, risk-area inspection, and rollback awareness.

### Prototype versus production

Prototype review can focus on whether the idea works. Production review must focus on what can break, who is affected, and how to recover.

### Maintenance phase

In maintenance, budget for review time on every AI-assisted patch; skipped review compounds into unknown behavior debt.

## Stable Core

- review artifacts beat confident summaries
- small diffs are cheaper to review
- unchecked generated code is not done

## Volatile Surface

- Codex review-pane layout
- available review scopes
- surface-specific slash commands
- Cloud handoff and task-summary behavior

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex adds new review modes or evidence artifacts
- review summaries begin including stronger machine-checkable provenance
- repository review tooling changes how diffs are displayed

## Evidence and Sources

- `openai.codex.app_review` — Official OpenAI Codex app review-pane guidance for inspecting changes and giving line-specific feedback.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples for local review and PR review flows.
- `openai.codex.best_practices` — Official OpenAI Codex best practices for validation, review, and done-when criteria.
- `git.docs.diff` — Official Git diff documentation for inspecting changes.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.reviewing_codex_output`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.testing`
- `vcb.prompting.acceptance_criteria`
- `vcb.codex.app`
- `vcb.codex.cloud`
- `vcb.concepts.diff`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.codex_output_review -->
