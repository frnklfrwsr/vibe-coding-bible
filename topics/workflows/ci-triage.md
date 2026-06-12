<!-- VCB:BEGIN_TOPIC id=vcb.workflow.ci_triage version=0.1.0 -->
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
id: vcb.workflow.ci_triage
title: CI Failure Triage with Codex Workflow
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- CI
- GitHub Actions
- Pull requests
- Codex App
- Codex Cloud
- Codex CLI
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.treating_symptom_as_root_cause
- vcb.shortcut.automation_spam
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.skipping_tests
durable_principles:
- triage separates observed facts from guesses
- fixes should target root cause, not just the failing line
- CI failures are evidence, not annoyance
likely_to_change:
- CI provider log format
- GitHub Actions UI
- Codex access to failed checks
- automation/inbox behavior
- test-runner output
obsolete_when:
- CI systems always provide perfect root-cause diagnosis and verified fixes
related_topics:
- vcb.chapter.ci_noninteractive_github_actions
- vcb.workflow.testing
- vcb.workflow.bug_repro
- vcb.prompting.acceptance_criteria
- vcb.concepts.ci
- vcb.codex.automations
---

> Summary:
> CI triage uses Codex to summarize failed checks, logs, likely causes, and next actions without confusing symptoms for root causes.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.ci_triage.human -->
## 1. For the Human: Plain-Language Concept

### What this means

CI is the automated check system that runs tests, lint, type checks, builds, or deployment gates. CI triage means reading the failure, identifying what is known, what is guessed, and what the smallest next action should be.

### Why it matters

CI failures often look noisy. Codex can summarize logs quickly, but it can also jump to a plausible wrong fix. Good triage prevents churn: changing code blindly until checks turn green.

### The mental model

CI is the smoke. Triage finds the fire; it does not just wave the smoke away.

### What good looks like

Good: “Summarize failed checks. Separate observed facts from hypotheses. Identify likely root cause, smallest fix, and exact command to rerun. Do not edit yet.”

### What bad looks like

Bad: “Fix CI” with no logs, no failing check name, no root-cause explanation, and no rerun evidence.

### Minimal example

If a PR build fails on typecheck, Codex should identify the exact error, affected file, change that introduced it, likely root cause, and targeted command before editing.

### Checklist

- capture failing job/check names
- quote or summarize the specific failing evidence
- separate observed facts from guesses
- map failure to recent diff when possible
- propose the smallest next action
- rerun targeted check after fix
- do not hide flaky or skipped tests
<!-- VCB:END_SECTION id=vcb.workflow.ci_triage.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.ci_triage.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to make CI triage evidence-first and root-cause-oriented.

### Diagnose the human’s current model

- What check failed?
- What exact log line or assertion is evidence?
- Was the failure introduced by this diff or preexisting?
- Is the proposed fix addressing root cause or only satisfying CI?
- What targeted command proves the fix?

### Explanation strategy

Use a no-edit triage pass first. Have Codex return input sources, inaccessible sources, observed failures, hypotheses, severity, and recommended next action. Only then allow a small patch and rerun.

### Useful metaphor

CI triage is incident intake for code. The first job is facts, not heroics.

### Coaching tactics

- ask for triage before mutation
- require inaccessible sources to be named
- group duplicates instead of listing every failure separately
- keep flaky-test diagnosis separate from product bug diagnosis
- record rerun evidence after fixes

### Prompt patterns

```text
Triage these CI failures. Do not edit files yet.
Return: input sources reviewed, inaccessible sources, failed checks, observed evidence, suspected root cause, confidence, smallest next action, and targeted rerun command.
Keep observed facts separate from guesses.
```

### Red flags to call out directly

- Codex changes code before reading logs
- fix deletes or skips the failing test
- root cause is stated without evidence
- automation posts noisy duplicate triage reports
- CI turns green by weakening checks

### Exercises

- Give the human one failing log and ask for facts versus guesses.
- Ask them to choose the smallest rerun command.
- Have them reject a “fix” that only skips the failure.
<!-- VCB:END_SECTION id=vcb.workflow.ci_triage.ai_coach -->

## Shortcut Reality

### The ideal practice

Triage first, patch narrowly, rerun the failing check, then broaden verification if risk warrants it.

### What users often do instead

Users ask Codex to “fix CI” and accept whatever patch makes the visible failure disappear.

### When the shortcut may be fine

A fast direct fix may be fine for obvious syntax or formatting failures on a local branch.

### When the shortcut is a bad idea

Blind CI fixes are bad for flaky tests, failing security checks, production deploy gates, migrations, dependency failures, or repeated failures with unclear ownership.

### Risk profile

- Probability of failure: Medium; CI symptoms are easy to misread, especially in long logs.
- Impact if it fails: High when the “fix” weakens tests, disables checks, hides a production bug, or breaks deployment confidence.
- Ease of recovery: Good when the patch is small and rerun evidence exists; poor when checks are skipped or disabled.
- Blast radius: The failed pipeline, changed tests/checks, and any merge/deployment gate depending on CI.
- Skill needed to recover: Medium; high when failures involve infra, credentials, flaky distributed tests, or deployment systems.
- Hidden cost: Check erosion, flaky-test normalization, rerun spam, and loss of trust in CI.

### Minimum guardrails

- triage before editing
- do not delete or skip failing checks without explicit approval
- rerun targeted check
- record evidence and unresolved gaps
- escalate repeated or security/deployment failures

### Recovery plan

- Revert any check-weakening patch.
- Restore skipped tests or disabled jobs.
- Collect failing logs.
- Patch root cause narrowly.
- Rerun and update CI guidance if the failure pattern repeats.

## Budget and Constraint Notes

### Cheapest reliable path

Ask Codex for a no-edit triage summary and one targeted rerun command.

### Fastest high-usage path

High-throughput users can automate CI triage summaries, but should avoid auto-mutation until the workflow is reliable.

### Low-attention path

Low-attention CI triage may summarize failures, but mutation requires strong isolation and explicit permission.

### Production-quality path

Production CI failures must preserve gates, explain root cause, rerun checks, and avoid weakening verification.

### Prototype versus production

Prototype CI may be minimal. Production CI is part of the safety contract and should not be bypassed casually.

### Maintenance phase

In maintenance, preserve CI signal quality; noisy or bypassed checks train the team and the agent to ignore real failures.

## Stable Core

- logs are evidence
- triage precedes mutation
- green CI created by weaker checks is not success

## Volatile Surface

- CI provider log layout
- GitHub Actions failure UI
- Codex access to issues/checks/logs
- automation scheduling behavior
- test command names

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex automation or GitHub integration changes failure-access behavior
- CI provider changes log retention or permissions
- project test strategy changes

## Evidence and Sources

- `openai.codex.use_cases.automation_bug_triage` — Official OpenAI Codex use case for triaging alerts, issues, failed checks, and logs.
- `openai.codex.workflows` — Official OpenAI Codex workflow examples involving debugging, tests, and review.
- `github.docs.actions_ci` — Official GitHub Actions CI guidance.
- `github.docs.pull_requests` — Official GitHub pull-request guidance for review context.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.ci_noninteractive_github_actions`
- `vcb.workflow.testing`
- `vcb.workflow.bug_repro`
- `vcb.prompting.acceptance_criteria`
- `vcb.concepts.ci`
- `vcb.codex.automations`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.ci_triage -->
