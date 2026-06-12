<!-- VCB:BEGIN_TOPIC id=vcb.chapter.senior_engineer_checklist version=0.1.0 -->
---
id: vcb.chapter.senior_engineer_checklist
title: "Chapter 35 — The Senior Engineer Checklist for Vibe Coders"
type: chapter
chapter_number: 35
version: 0.1.0
last_verified: '2026-06-09'
next_review_due: '2026-09-09'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- Git
- tests
- CI
- all project types

source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: CORE_ENGINEERING
  surface: STABLE
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
- major_refactor
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.skipping_senior_checklist
- vcb.shortcut.checklist_theater
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.accepting_looks_done

durable_principles:
- The checklist is a thinking tool, not a ritual.
- Risk determines strictness.
- Diffs, checks, and rollback paths are evidence.

likely_to_change:
- exact UI locations for review
- Codex final-report conventions
- GitHub review interface
- current check commands per stack

obsolete_when:
- Codex or repository tooling provides a first-class, source-aware checklist that reliably covers these gates.

related_topics:
- vcb.chapter.reviewing_codex_output
- vcb.chapter.git_discipline
- vcb.chapter.acceptance_criteria
- vcb.chapter.failure_modes_codex_work
- vcb.chapter.security_for_vibe_coders
- vcb.concepts.diff
- vcb.concepts.rollback
---


> Summary:
> The senior engineer checklist is a compact before/during/before-accepting/after-accepting loop for vibe coders. It turns Codex work from “looks good” into reviewable engineering evidence.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.senior_engineer_checklist.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A senior engineer checklist is a short set of questions you run before, during, and after Codex work.

It is not there to slow you down. It is there to prevent expensive mistakes while keeping speed. The checklist is the seatbelt, not the traffic jam.

### Before starting

Ask:

- Is the working tree clean or intentionally dirty?
- Is the task small enough to review?
- Did I define done?
- Did I provide the relevant files, logs, screenshots, docs, or examples?
- Did I say what must not change?
- Are permissions appropriate for the risk?
- Is this prototype mode or production mode?
- Is there a rollback path?

If the answer is "no" on more than one of these, do not ask for broad implementation yet. Ask for a plan or context map first.

### During work

Watch for:

- Codex editing unrelated files;
- Codex adding dependencies;
- Codex weakening tests;
- Codex changing auth, data, deployment, or config behavior;
- Codex skipping reproduction or checks;
- Codex making a large diff without a checkpoint;
- Codex sounding confident without evidence.

During work, the best intervention is usually small:

```text
Pause. Summarize changed files, assumptions, and current verification status before continuing.
```

### Before accepting

Do not accept based on the final message alone. Check:

- What files changed?
- Is the diff in scope?
- Did tests/lint/typecheck/build run?
- Did Codex report command output, not just claims?
- Did it weaken or delete tests?
- Did dependencies change?
- Did auth/security/data behavior change?
- Did it touch migrations, deployment config, or secrets?
- Is manual UI/browser verification needed?
- Is rollback clear?

Codex’s summary is a claim. The diff, tests, command output, screenshots, and logs are evidence.

### After accepting

After you accept useful work:

- commit a logical checkpoint;
- update `AGENTS.md` if Codex learned a repeated rule;
- create a skill only if the workflow repeated;
- create automation only for stable recurring work;
- note known gaps;
- keep follow-up tasks separate.

### Risk-adjusted strictness

For a throwaway prototype:

- small diff;
- manual check;
- Git checkpoint;
- known gaps.

For a personal local tool:

- same as prototype plus data-loss check.

For a public app:

- branch;
- relevant automated checks;
- diff review;
- PR review;
- rollback notes.

For auth/payment/user-data systems:

- everything above plus explicit security review, fake/staging data first, and no unattended broad mutation.

### The compact checklist

```text
Before:
[ ] clean or understood working tree
[ ] task small enough
[ ] done criteria defined
[ ] relevant context provided
[ ] forbidden areas named
[ ] permissions match risk
[ ] rollback path exists

During:
[ ] changes stay in scope
[ ] no surprise dependencies
[ ] no weakened tests
[ ] no sensitive files touched unexpectedly
[ ] checks/repro attempted when relevant

Before accepting:
[ ] reviewed diff
[ ] reviewed tests changed
[ ] reviewed command output
[ ] checked auth/data/security/deploy impact
[ ] checked UI states if relevant
[ ] known gaps listed

After:
[ ] commit
[ ] update durable guidance if repeated
[ ] split follow-ups
```

### What bad looks like

Bad checklist use is theater:

- boxes checked without inspecting evidence;
- "tests pass" accepted without seeing command output;
- security box checked because the diff looked small;
- rollback box checked without knowing how to revert;
- production flow shipped because prototype flow worked once.

A checklist that does not change decisions is decoration.
<!-- VCB:END_SECTION id=vcb.chapter.senior_engineer_checklist.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.senior_engineer_checklist.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Use the checklist as a lightweight enforcement tool. It should calibrate strictness by risk, not make every task heavy.

### Diagnose the human’s current model

Ask:

- Are they trying to accept work based on vibes?
- Is the diff small enough for them to review?
- Did Codex prove anything with command output or artifacts?
- Did the task touch high-risk areas?
- Is the human in prototype or production mode?

### Explanation strategy

Teach the checklist as four gates:

```text
before → during → before accepting → after
```

Each gate catches a different class of failure. Before catches vague tasks. During catches scope drift. Before accepting catches false confidence. After captures learning and rollback.

### Useful metaphors

- **Checklist:** preflight checklist.
- **Diff:** evidence bag.
- **Tests:** smoke alarms.
- **Rollback:** emergency exit.
- **AGENTS.md update:** writing the lesson into the operating manual.

### Coaching tactics

- For low-risk work, apply the short checklist and keep momentum.
- For production/security work, slow down and require evidence.
- If the user says "it looks done," ask for changed files and checks run.
- If Codex says "all set," ask which command output proves it.
- If no rollback exists, create one before risky work.

### Prompt patterns

```text
Run the senior engineer checklist on this Codex result.
Use only evidence from the diff, command output, screenshots/logs, and changed files.
Do not rely on the final summary.
Return blocking issues first.
```

```text
Before I accept this change, make a review packet:
- files changed,
- behavior changed,
- checks run and output,
- tests changed and whether they were weakened,
- dependency changes,
- auth/data/security/deploy risks,
- rollback path,
- known gaps.
```

### Red flags to call out directly

- The user cannot name what changed.
- The diff is large and unreviewed.
- Tests were edited but not inspected.
- The change touches secrets, auth, payments, data deletion, migrations, or deploy config.
- There is no rollback path.
- The user wants to skip checks because Codex sounded confident.

### Exercises

Take one accepted Codex patch and run the checklist after the fact. Identify which question would have caught the most risk earliest.
<!-- VCB:END_SECTION id=vcb.chapter.senior_engineer_checklist.ai_coach -->

## Shortcut Reality

### The ideal practice

Use the checklist every time, scaled to the risk of the change.

### What users often do instead

Users accept Codex’s final message, glance at the app once, and move on without reviewing the diff, checks, or rollback path.

### When the shortcut may be fine

For throwaway prototypes, a minimal checklist is enough: inspect changed files, manually test the exact path, and commit or discard.

### When the shortcut is a bad idea

Skipping the checklist is a bad idea for production apps, shared repos, auth, payments, persistent data, migrations, CI secrets, deployment config, security-sensitive flows, and unattended agent work.

### Risk profile

- Probability of failure: medium when unchecked; high for broad diffs.
- Impact if it fails: low in prototypes; high/severe for production/security.
- Ease of recovery: high with Git checkpoints; low with data loss/secrets.
- Blast radius: grows with permissions, deploy coupling, and affected systems.
- Skill needed to recover: higher after deploy or data mutation.
- Hidden cost: accepting small-looking changes that create future instability.

### Minimum guardrails

- Review changed files.
- Run or verify at least one relevant check.
- Inspect tests if changed.
- Check sensitive areas.
- Know rollback.
- Commit after acceptance.

### Recovery plan

If you skipped the checklist and something broke, stop further edits, inspect Git status/diff, identify changed files, revert or isolate the risky changes, rerun the relevant check, and add one durable rule if the mistake is repeatable.

### AI coach guidance

Use the checklist to protect speed. Do not turn every CSS tweak into a security audit, but do not let high-risk work pass with prototype-level review.

## Budget and Constraint Notes

### Cheapest reliable path

Use the compact checklist. For low-risk work, one relevant manual check plus diff review may be enough.

### Fastest high-usage path

Ask Codex to generate a review packet, then use a fresh review session for risky diffs. Do not outsource final acceptance.

### Low-attention path

Low-attention work must produce a review packet. If no evidence is available, the work is not ready to accept.

### Production-quality path

Require branch/PR review, relevant checks, security-sensitive review where applicable, rollback notes, and durable guidance updates after repeated failures.

## Stable Core

- Review evidence, not confidence.
- Risk determines checklist depth.
- Small diffs and clean Git checkpoints make review cheaper.
- A checklist is useful only when it can block acceptance.
- After-action learning should become durable guidance when repeated.

## Volatile Surface

- Exact Codex review UI.
- GitHub PR review UI details.
- Current command names for checks.
- Codex final-report behavior.
- Product-native checklist features.

## Obsolescence Watch

Review this chapter when Codex or GitHub introduces reliable built-in review packets/checklists that change how users collect acceptance evidence.

## Evidence and Sources

- `openai.codex.best_practices` — official OpenAI source for validation, review, reusable guidance, and treating Codex as a teammate.
- `openai.codex.workflows` — official OpenAI source for verification and command-output reporting in example workflows.
- `openai.codex.app_review` — official OpenAI source for Codex app review and diff inspection.
- `openai.codex.github_review` — official OpenAI source for Codex GitHub PR review behavior.
- `openai.codex.security` — official OpenAI source for security review positioning and limitations.
- `github.docs.pull_requests` — official GitHub source for PR review surfaces and merge context.
- `git.docs.status` — official Git source for checking working tree status.
- `git.docs.diff` — official Git source for diff review.
- Maintainer synthesis: checklist structure derived from prior VCB chapters and stable engineering practice.

## Related Topics

- `vcb.chapter.reviewing_codex_output`
- `vcb.chapter.git_discipline`
- `vcb.chapter.acceptance_criteria`
- `vcb.chapter.failure_modes_codex_work`
- `vcb.chapter.security_for_vibe_coders`
- `vcb.concepts.diff`
- `vcb.concepts.rollback`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.senior_engineer_checklist -->
