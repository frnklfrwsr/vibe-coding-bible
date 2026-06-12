<!-- VCB:BEGIN_TOPIC id=vcb.chapter.debugging_with_reproduction version=0.1.0 -->
---
id: vcb.chapter.debugging_with_reproduction
title: "Chapter 13 — Debugging with Reproduction, Not Guessing"
type: chapter
chapter_number: 13
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-12-08'
review_cadence: semiannual

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- logs
- tests
- browser checks
- CI failures

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE

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

shortcut_profiles:
- vcb.shortcut.debugging_without_repro
- vcb.shortcut.skipping_tests
- vcb.shortcut.accepting_looks_done

durable_principles:
- A bug report should include expected behavior, actual behavior, reproduction steps, environment, and evidence.
- Reproduce first when feasible, then patch, then rerun the same reproduction.
- Root cause should be explained before broad changes are accepted.
- Regression tests are the durable form of bug knowledge when feasible.

likely_to_change:
- browser/computer-use debugging mechanics
- Codex debugger plugins and tool integrations
- CI autofix workflows
- product-specific log and observability integrations

obsolete_when:
- Codex can reliably infer, reproduce, patch, and validate bugs without explicit repro steps or evidence.
- Official Codex debugging workflows no longer recommend reproducing and verifying bugs.

related_topics:
- vcb.chapter.understanding_unknown_codebase
- vcb.chapter.acceptance_criteria
- vcb.chapter.writing_updating_tests
- vcb.chapter.context_management
- vcb.chapter.git_discipline
- vcb.concepts.diff
- vcb.concepts.recoverability
- vcb.workflow.bug_repro
- vcb.workflow.testing
---

> Summary:
> Debugging with Codex works best when the bug is made concrete: reproduce it, explain root cause, patch narrowly, and rerun the same check.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.debugging_with_reproduction.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Debugging means finding why behavior is wrong and changing the smallest code path that causes it.

A repro is a way to make the bug happen on purpose.

Use this line:

```text
A bug without a repro is a rumor.
```

That does not mean the bug is fake. It means you do not yet have enough evidence to fix it reliably.

### Why it matters

Codex is good at making plausible fixes. Plausible fixes are dangerous when the actual failure is not understood.

Without a repro, Codex may:

- patch the wrong file,
- fix a symptom instead of the cause,
- add defensive code that hides the failure,
- change architecture unnecessarily,
- make tests pass without proving the bug is gone,
- declare victory because the code looks reasonable.

A reproduction loop prevents guessing.

### The debugging loop

Use this loop:

1. Describe the bug.
2. Provide reproduction steps.
3. State expected behavior.
4. State actual behavior.
5. Attach logs, stack traces, screenshots, failing tests, or CI output.
6. Ask Codex to reproduce or simulate the failure.
7. Ask for root cause before patching.
8. Patch narrowly.
9. Rerun the same repro.
10. Add or update a regression test when feasible.

### Good bug prompt

```text
Bug:
Clicking Save shows "Saved" but the new name is not persisted after refresh.

Repro:
1. Log in as test user.
2. Go to /settings/profile.
3. Change display name to "Alex Test".
4. Click Save.
5. Refresh the page.

Expected:
The page still shows "Alex Test".

Actual:
The old name returns after refresh.

Constraints:
- keep the fix minimal,
- do not change the public API shape,
- add or update a regression test if feasible.

Start by reproducing or tracing the bug. Explain root cause before patching. After the fix, rerun the repro or nearest check.
```

### Evidence that helps Codex

| Evidence | Why it helps |
|---|---|
| Repro steps | turns vague bug into repeatable behavior |
| Expected vs actual | prevents Codex from guessing intent |
| Stack trace | points to failing call path |
| Logs | shows runtime facts |
| Screenshot/video | shows UI state and timing |
| Failing test | gives Codex a machine-checkable target |
| CI output | captures environment and command failure |
| Recent diff | shows what likely introduced the bug |

### When reproduction is hard

Some bugs are intermittent, timing-dependent, environment-specific, or production-only. Do not pretend they are easy.

For hard repros, ask Codex to gather evidence first:

```text
Do not patch yet. Create an investigation plan.
List possible causes, evidence needed, logs to inspect, instrumentation to add, and the safest next diagnostic step.
```

The next step may be logging, a narrower test, or a manual checklist. Guessing should still be the last resort.

### Good root cause explanation

A good root cause explanation says:

```text
The UI shows Saved because saveProfile() resolves, but the API handler ignores displayName when building the update payload. The database never receives the new value. Evidence: src/api/profile.ts and src/services/profile.ts.
```

A weak explanation says:

```text
There was a state issue. I fixed it.
```

That is not enough.
<!-- VCB:END_SECTION id=vcb.chapter.debugging_with_reproduction.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.debugging_with_reproduction.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to convert bugs into reproducible, verifiable loops before accepting patches.

The target behavior is not “Codex changed code.” The target behavior is “the same failing path now passes for the right reason.”

### Diagnose the human’s current model

Watch for:

- “Fix this” with only a screenshot or complaint.
- No expected behavior.
- No actual behavior.
- No environment.
- No repro steps.
- Codex proposing a broad rewrite.
- Patches before root cause.
- Tests added after the fact that only assert the new implementation detail.

### Explanation strategy

Use this sequence:

1. **Make it repeatable.** Repro or nearest diagnostic evidence.
2. **Make intent explicit.** Expected versus actual.
3. **Trace cause.** Relevant files and call path.
4. **Patch narrowly.** Fix the smallest cause.
5. **Lock it in.** Regression test or exact manual check.

When the user wants to skip repro, do not argue abstractly. Say:

```text
We can move faster by making the bug concrete. Give Codex the exact failing path; otherwise it will guess.
```

### Useful metaphors

- **Crime scene:** do not clean up before collecting evidence.
- **Smoke alarm:** silence is not proof the fire is out.
- **Doctor diagnosis:** symptoms guide the exam; they are not the diagnosis.

### Coaching tactics

If the user has no repro, ask for the smallest possible one:

```text
What is the minimum sequence that makes the bug appear once?
```

If they only have logs, ask Codex to trace from the log to the likely code path, then propose a diagnostic check before patching.

If the bug is production-only, push for staging, fake data, read-only log analysis, or instrumentation before destructive changes.

### Prompt patterns

#### Repro-first bug fix

```text
Start by reproducing the bug or proving why it cannot be reproduced locally.
Then explain the root cause with file references.
Then make the smallest patch.
Then rerun the same repro/check.
Add a regression test if feasible.
```

#### Investigation-only prompt

```text
Investigate only. Do not patch yet.
Given this bug report, identify likely code paths, missing evidence, diagnostic commands, and the safest next step.
```

#### Patch from stack trace, with guardrails

```text
This stack trace points to a likely bug.
Patch only if the root cause is obvious from inspected files.
If not obvious, stop and ask for reproduction evidence.
Keep the fix minimal and report confidence.
```

### Red flags to call out directly

- “No repro yet.”
- “Codex patched before explaining root cause.”
- “The fix changes architecture instead of the failing line/path.”
- “The test proves the implementation, not the user-visible behavior.”
- “The final report says it works but does not show the repro rerun.”

### Exercises

1. Turn a vague bug into expected/actual/repro.
2. Ask Codex to trace the call path without patching.
3. Ask for root cause with file evidence.
4. Patch narrowly.
5. Add a regression test or exact manual check.
<!-- VCB:END_SECTION id=vcb.chapter.debugging_with_reproduction.ai_coach -->

## Shortcut Reality

### The ideal practice

Reproduce the bug, explain root cause, patch narrowly, rerun repro, and add a regression test when feasible.

### What users often do instead

They paste an error message or screenshot and ask Codex to “fix it,” then accept the first plausible patch.

### When the shortcut may be fine

Patching without a full repro may be acceptable when:

- the failure is obvious from the stack trace,
- the code path is tiny,
- the project is a throwaway prototype,
- no persistent data or security boundary is involved,
- rollback is easy,
- the patch is one small obvious correction.

Example: a misspelled import in a local script.

### When the shortcut is a bad idea

It is a bad trade when:

- the bug is intermittent,
- production data is involved,
- the bug touches auth, payments, permissions, concurrency, or migrations,
- the patch changes public behavior,
- the root cause is unknown,
- the test suite is weak,
- logs are the only evidence and they are ambiguous.

### Risk profile

- Probability of failure: medium for obvious stack traces, high for intermittent or stateful bugs.
- Impact if it fails: low in prototypes, high in production.
- Ease of recovery: high if the patch is small and committed; poor if it hides a deeper issue.
- Blast radius: grows with state, concurrency, and data writes.
- Skill needed to recover: medium to high.
- Hidden cost: repeated patches that mask the real bug.

### Minimum guardrails

- Preserve the error message or screenshot.
- Ask Codex to identify likely root cause before patching.
- Keep the patch small.
- Rerun the failing path or closest check.
- Add a regression test when feasible.
- Do not broaden architecture to fix an unclear bug.

### Recovery plan

If a guess patch made things worse:

1. Stop changing code.
2. Inspect the diff.
3. Revert speculative changes.
4. Rebuild the repro.
5. Trace root cause with file evidence.
6. Patch only the failing path.
7. Add a test or diagnostic to prevent recurrence.

### AI coach guidance

Say:

```text
This is still a rumor until we can reproduce or trace it. The fastest safe path is to make the failure concrete, then patch the smallest cause.
```

## Budget and Constraint Notes

### Cheapest reliable path

Give Codex exact repro steps, logs, and constraints upfront. That saves usage by avoiding broad exploration and speculative fixes.

### Fastest high-usage path

Use one agent to reproduce/trace and another to propose a minimal patch only after evidence exists. Keep both on branches or read-only until the patch is chosen.

### Low-attention path

Low-attention debugging requires a repro/check and final report. Do not leave Codex to patch ambiguous production bugs unattended.

### Production-quality path

Require root cause, regression test or documented repro rerun, diff review, monitoring/rollback notes, and security review if the bug touches sensitive boundaries.

## Stable Core

- Reproduction turns a complaint into engineering evidence.
- Root cause comes before patch acceptance.
- The same failing path should be rerun after the fix.
- Regression tests preserve bug knowledge.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
- Computer-use debugging capabilities.
- Browser/app annotation features.
- CI autofix workflows.
- Simulator/debugger/MCP/plugin integrations.
- Product-specific log and issue-triage integrations.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex debugging features materially change how repro, logs, browser checks, or CI failures are gathered and validated.

## Evidence and Sources

- `openai.codex.workflows` — official current anchor for bug-fix workflows that start by reproducing the bug, then patching and running checks.
- `openai.codex.use_cases.automation_bug_triage` — official current anchor for checking alerts, issues, failed checks, logs, and reports during bug triage.
- `openai.codex.use_cases.qa_computer_use` — official current anchor for exercising app flows and reporting bugs with repro, expected result, actual result, and severity.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for reproduction-first debugging, root-cause discipline, and regression protection.

## Related Topics

- `vcb.chapter.understanding_unknown_codebase`
- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.writing_updating_tests`
- `vcb.chapter.context_management`
- `vcb.chapter.git_discipline`
- `vcb.concepts.diff`
- `vcb.concepts.recoverability`
- `vcb.workflow.bug_repro`
- `vcb.workflow.testing`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.chapter.debugging_with_reproduction -->
