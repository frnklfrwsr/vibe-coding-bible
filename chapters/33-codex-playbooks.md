<!-- VCB:BEGIN_TOPIC id=vcb.chapter.codex_playbooks version=0.1.0 -->
---
id: vcb.chapter.codex_playbooks
title: "Chapter 33 — The Codex Playbooks"
type: chapter
chapter_number: 33
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
- GitHub PR review
- Computer Use
- CI
- skills
- automations

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
- major_refactor
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.copy_pasting_playbook_blindly
- vcb.shortcut.overusing_one_playbook
- vcb.shortcut.one_big_prompt
- vcb.shortcut.skipping_plan

durable_principles:
- A playbook is a starting shape, not a substitute for judgment.
- Good playbooks include goal, context, constraints, done criteria, checks, and review gates.
- Risk changes the playbook.

likely_to_change:
- exact commands
- Codex UI invocation syntax
- surface-specific shortcuts
- plugin/skill names
- current product feature names

obsolete_when:
- Codex ships an official playbook format that supersedes this chapter.
- Core workflow recipes become available as first-class product templates.

related_topics:
- vcb.chapter.understanding_unknown_codebase
- vcb.chapter.feature_slicing
- vcb.chapter.debugging_with_reproduction
- vcb.chapter.writing_updating_tests
- vcb.chapter.frontend_work
- vcb.chapter.reviewing_codex_output
- vcb.chapter.github_pr_review_with_codex
- vcb.chapter.ci_noninteractive_github_actions
- vcb.chapter.automations_recurring_work
- vcb.chapter.security_for_vibe_coders
- vcb.chapter.dependency_package_framework_decisions
- vcb.chapter.failure_modes_codex_work
- vcb.chapter.first_serious_app
---


> Summary:
> Playbooks are copyable starting recipes for common Codex work. They are not universal laws; an AI coach should adapt them by risk, budget, surface, context, and project phase.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.codex_playbooks.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A playbook is a reusable recipe. It tells you how to start a common Codex task without inventing the workflow from scratch every time.

Good playbooks do three things:

1. They help you start faster.
2. They prevent common omissions.
3. They leave evidence you can review.

They do **not** replace judgment. You still adjust the playbook for project risk, budget, attention level, and what can go wrong.

### How to use a playbook

Before using any playbook, fill in these fields:

```text
Project type:
Risk level:
Attention mode:
Budget posture:
Allowed files/areas:
Forbidden files/areas:
Done when:
Rollback path:
```

If you cannot fill those in, the playbook is not ready for implementation.

### Playbook: new project bootstrap

Use when you are creating a new repo or project from zero and need the smallest maintainable starting structure.

```text
Goal:
Bootstrap a new project/repo with the smallest maintainable starting structure for [app/tool/library].

Context:
Product idea:
Preferred stack, if any:
Constraints:
Must avoid:

Constraints:
- Do not add unnecessary dependencies.
- Keep setup/run/test commands simple.
- Add README or starter instructions.
- Add AGENTS.md only if this project will continue beyond a throwaway prototype.
- Use fake credentials and example environment variables only.
- Do not wire real payments, production services, or real user data into the bootstrap.

Done when:
- Project can install/start/build or run its first check.
- Basic file structure is explained.
- README has setup/run/check commands.
- Initial Git checkpoint is recommended.
- Known shortcuts and next hardening steps are listed.
```

AI coach note: keep this playbook distinct from the MVP prototype playbook. Bootstrap creates the clean starting repo and first commands; MVP prototype proves a product loop.

### Playbook: unknown repo tour

Use when you inherit or open a repo you do not understand.

```text
Read-only. Do not edit files.

Goal:
Map this codebase enough for a first safe change.

Context:
Start at the repo root. Inspect manifests, README, config, routes/entrypoints, tests, and package scripts.

Return:
- app purpose,
- package manager and commands,
- main entrypoints,
- request/data flow,
- test structure,
- risky areas,
- 5 files worth reading first,
- unknowns to verify.

Cite files/functions for every claim.
```

### Playbook: small feature slice

```text
Goal:
Implement only milestone 1: [single visible behavior].

Context:
Relevant files: [files].
Existing pattern to follow: [file].

Constraints:
- No new dependencies.
- Do not change public API shape unless specified.
- Do not touch auth, billing, migrations, deployment config, or secrets.
- Keep the diff reviewable.

Done when:
- Behavior works for [specific case].
- Relevant tests/checks pass or failures are reported with output.
- Final report lists files changed, checks run, and known gaps.
```

### Playbook: reproducible bug fix

```text
Bug:
[description]

Repro:
1. ...
2. ...
3. ...

Expected:
[expected]
Actual:
[actual]

Constraints:
- Reproduce before patching if feasible.
- Explain root cause before final patch.
- Keep fix minimal.
- Add or update regression coverage if feasible.

Done when:
- Repro no longer fails.
- Relevant check passes.
- Final report includes root cause, changed files, and check output.
```

### Playbook: add tests

```text
Goal:
Add behavior-focused tests for [feature/bug].

Context:
Relevant implementation: [files].
Nearby test examples: [files].
Behavior to prove: [behavior].

Constraints:
- Follow existing test style.
- Do not weaken existing assertions.
- Do not over-mock the behavior under test.
- If this is a bug, show the test fails before the fix when feasible.

Done when:
- Test proves the behavior, not just implementation details.
- Test command result is reported.
```

### Playbook: refactor safely

```text
Plan only first.

Goal:
Refactor [specific boundary] without behavior changes.

Return a plan with:
- current responsibilities,
- files affected,
- public behavior that must stay unchanged,
- checks/tests to run,
- rollback point,
- smallest first slice.

After approval, implement only the first slice.
```

### Playbook: frontend from screenshot

```text
Goal:
Implement this UI from the attached screenshot/design.

Context:
Use existing components and design tokens from [files].

Constraints:
- Include loading, empty, error, success, disabled, mobile, and keyboard states if relevant.
- Preserve existing routes/API behavior.
- Do not add UI libraries without approval.

Done when:
- Browser route is listed.
- Screenshots or visual notes compare expected vs actual.
- Responsive and accessibility basics are checked.
```

### Playbook: review local diff

```text
Review only. Do not edit files.

Inspect the current diff and classify:
- scope creep,
- deleted logic,
- weakened tests,
- new dependencies,
- auth/security/data behavior,
- migration/deployment/config changes,
- missing checks.

Return blocking issues first. Then non-blocking suggestions.
```

### Playbook: PR review

```text
Review this PR as an additional signal, not merge approval.
Focus on serious issues:
- regressions,
- missing tests,
- security concerns,
- data loss,
- deployment risk,
- behavior changes not described by the PR.

Return file-specific findings with severity and evidence.
```

### Playbook: CI failure triage

```text
Read-only first.

Goal:
Explain why CI failed and propose the smallest fix.

Context:
CI log: [paste/link]
Recent commits/PR: [context]

Return:
- failing job/step,
- likely root cause,
- files likely involved,
- whether it is flaky or deterministic,
- minimal fix plan,
- check to rerun.
```

### Playbook: create a skill

```text
We have repeated this workflow at least three times: [workflow].

Draft a narrow skill for it.
The skill must include:
- when to use it,
- when not to use it,
- required inputs,
- steps,
- verification,
- final report format,
- safety constraints.

Keep it small. Do not include unrelated workflows.
```

### Playbook: create an automation

```text
Design a report-only automation for [recurring task].

It must include:
- trigger/cadence,
- scope,
- data it may read,
- data it must not touch,
- report format,
- what counts as signal vs noise,
- stop condition,
- first-run manual review plan.

Do not auto-mutate until this report-only version has proven useful.
```


### Playbook: generate release notes

```text
Goal:
Generate release notes for [version/date range/release branch].

Context:
Use the provided commits, merged PRs, issue links, changelog fragments, and product notes.

Constraints:
- Do not invent user impact.
- Separate user-visible changes from internal maintenance.
- Flag breaking changes, migrations, known issues, and follow-up work.
- Keep marketing language out unless requested.

Done when:
- Notes are grouped into features, fixes, docs, internal changes, and known issues.
- Every important claim traces back to a commit, PR, issue, or file.
- Risky or incomplete items are clearly labeled.
```

### Playbook: investigate production error

```text
Read-only first. Do not patch yet.

Goal:
Investigate this production error and propose the safest response.

Context:
Error/log/alert: [paste]
Deployment window: [time]
Affected route/job/user action: [context]
Recent changes: [commits/PRs]

Return:
- timeline,
- symptoms,
- likely blast radius,
- top hypotheses with evidence,
- missing evidence to collect,
- safest immediate mitigation,
- rollback options,
- what not to change yet.

Done when:
- The first response is evidence-based and reversible.
- Any proposed patch is scoped to one hypothesis.
```

### Playbook: add API endpoint

```text
Goal:
Add one API endpoint: [method/path/purpose].

Context:
Existing nearby endpoints: [files].
Data model/service layer: [files].
Expected request/response examples: [examples].

Constraints:
- Follow existing routing, validation, error, logging, and auth patterns.
- Do not change unrelated endpoints.
- Do not weaken authentication or authorization.
- Add or update tests for success, validation failure, unauthorized/forbidden, and not-found/error behavior where relevant.

Done when:
- Endpoint behavior matches the examples.
- Relevant tests/checks pass or failures are reported with output.
- Final report names security and compatibility risks.
```

### Playbook: migrate dependency

```text
Plan only first.

Goal:
Migrate [dependency] from [current] to [target].

Return:
- current usage sites,
- reason for migration,
- breaking-change risks,
- lockfile/build impact,
- smallest migration slice,
- tests/checks to run,
- rollback path,
- whether this should be split into multiple PRs.

After approval:
Implement only the first safe slice. Do not combine dependency migration with unrelated refactors.
```

### Playbook: remove dead code

```text
Goal:
Remove dead code from [area].

Context:
Candidate files/symbols: [files/symbols].

Constraints:
- Prove the code is unused before deleting.
- Check references, exports, routes, scripts, tests, build config, and runtime entrypoints.
- Do not remove public API behavior without explicit approval.
- Keep deletion diff small.

Done when:
- Removal evidence is listed.
- Relevant build/tests pass.
- Rollback is straightforward.
```

### Playbook: improve docs

```text
Goal:
Improve documentation for [setup/workflow/API/feature].

Context:
Current docs: [files].
Source of truth in code/config/tests: [files].

Constraints:
- Do not invent features or commands.
- Cite files or commands that prove the documented behavior.
- Include prerequisites, commands, common failure cases, and known limitations.
- Keep docs aligned with current repo behavior.

Done when:
- A new user can follow the docs without hidden assumptions.
- Changed docs match current code/config.
```

### Playbook: build MVP prototype

```text
Goal:
Build the smallest vertical slice that proves the product loop: [user action] → [system response] → [visible value].

Context:
Product idea: [summary].
Target user: [user].
Critical path: [one flow].

Constraints:
- Use fake data unless explicitly told otherwise.
- Avoid production secrets, payments, and irreversible external side effects.
- Prefer fewer moving parts and fewer dependencies.
- Mark prototype debt clearly.

Done when:
- One complete flow works locally.
- Setup/run instructions are present.
- Known shortcuts and rebuild/hardening needs are listed.
```

### Playbook: harden auth-sensitive code

```text
Security review first. Do not implement until the risk map is clear.

Goal:
Harden auth-sensitive behavior in [area].

Context:
Auth/session/token/permission files: [files].
User roles and sensitive data: [summary].
Relevant routes/actions: [files].

Return before patching:
- authentication boundary,
- authorization checks,
- session/token handling,
- data exposure paths,
- abuse cases,
- tests/checks needed,
- rollback and monitoring plan,
- red lines that require human approval.

Done when:
- Security-sensitive behavior is tested or manually verified.
- Final report explains what was protected and what remains risky.
```

### Checklist

Before running a playbook:

- Is this the right playbook?
- Is the task small enough?
- Did you mark forbidden areas?
- Did you define done?
- Did you choose the right surface?
- Is this supervised, review-later, or unattended?
- Is rollback clear?
<!-- VCB:END_SECTION id=vcb.chapter.codex_playbooks.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.codex_playbooks.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the AI coach to select and adapt playbooks rather than dumping a generic recipe. A playbook must be modified by task shape, risk, attention, and budget.

### Diagnose the human’s current model

Ask:

- Is the user asking for a task or asking for a workflow?
- Is the repo known or unknown?
- Is the work implementation, review, debugging, security, CI, GUI, or documentation?
- What could go wrong if the playbook is too broad?
- What must be proven before the work is accepted?

### Explanation strategy

Use the phrase: **"Pick the playbook, then tune the dials."**

The dials are:

- project type;
- risk level;
- attention mode;
- budget posture;
- allowed files;
- forbidden files;
- checks;
- rollback.

### Useful metaphors

- **Playbook:** recipe card.
- **Risk tuning:** changing oven temperature for the actual dish.
- **Done criteria:** the toothpick test.
- **Rollback:** having a spare cake before serving customers.

### Coaching tactics

- Route to the smallest playbook that fits.
- For high risk, add planning/review/security steps.
- For low budget, remove broad exploration and best-of-N work.
- For low attention, require final reports and stronger isolation.
- For production, add branch, checks, PR review, and rollback.

### Prompt patterns

```text
Select the right VCB playbook for this task.
Then adapt it for:
- project type:
- risk:
- usage budget:
- attention mode:
- forbidden areas:
Return the final prompt only.
```

```text
Compress this playbook for a constrained user.
Keep the minimum reliable steps and remove optional exploration.
Do not remove verification.
```

### Red flags to call out directly

- The user copy-pastes a broad playbook into a security-sensitive task.
- The playbook has no done criteria.
- The playbook asks for implementation before context.
- The user wants best-of-N without diff review.
- The user treats a prototype playbook as production hardening.

### Exercises

Take the same feature request and adapt the feature-slice playbook for: throwaway prototype, public app, and auth/payment system.
<!-- VCB:END_SECTION id=vcb.chapter.codex_playbooks.ai_coach -->

## Shortcut Reality

### The ideal practice

Use playbooks as starting recipes, then adapt them to the actual task and risk.

### What users often do instead

Users copy a playbook blindly, remove the verification parts, or use one giant playbook for every task.

### When the shortcut may be fine

Blind playbook use can be fine for local demos and learning projects when the blast radius is small and recovery is easy.

### When the shortcut is a bad idea

It is a bad idea for production, security-sensitive changes, data migrations, auth/payment logic, release automation, and large refactors.

### Risk profile

- Probability of failure: medium when playbooks are not tuned.
- Impact if it fails: low in prototypes; high in production.
- Ease of recovery: high with Git checkpoints; lower with external services or data changes.
- Blast radius: depends on task scope and permissions.
- Skill needed to recover: rises with production integration and security risk.
- Hidden cost: false sense of process.

### Minimum guardrails

- Fill in project type, risk, attention, and done criteria.
- Add forbidden areas.
- Keep verification.
- Use review-only playbooks before mutation when risk is unclear.
- Commit or branch before broad work.

### Recovery plan

If a playbook causes bad output, stop using it as a universal prompt. Identify which dial was wrong: scope, risk, context, checks, or surface. Update the playbook or split it into narrower playbooks.

### AI coach guidance

Never hand the user a playbook without adapting it to the current risk level.

## Budget and Constraint Notes

### Cheapest reliable path

Use one narrow playbook and one relevant check. Avoid best-of-N, broad exploration, and multi-agent work unless the risk justifies it.

### Fastest high-usage path

Use multiple playbooks in sequence: plan, implementation, fresh review, test hardening, and final report. Keep write work isolated.

### Low-attention path

Use report-only or branch-only playbooks with explicit final reports. Avoid unattended mutation on high-risk areas.

### Production-quality path

Use playbooks with PR review, relevant automated checks, security review where relevant, rollback notes, and durable guidance updates after repeated issues.

## Stable Core

- Reusable workflows reduce cognitive load.
- Good playbooks include context, constraints, done criteria, verification, and review.
- Playbooks are not universal; risk changes the recipe.
- The right playbook produces reviewable evidence.

## Volatile Surface

- Exact Codex commands, UI affordances, and product surfaces.
- Product-native template systems.
- Tool-specific playbook syntax.
- Current best use-case pages and official examples.

## Obsolescence Watch

Review this chapter if OpenAI publishes a first-class Codex playbook/template format, or if existing workflow examples materially change.

## Evidence and Sources

- `openai.codex.workflows` — official OpenAI source for end-to-end workflow examples, context notes, and verification steps.
- `openai.codex.use_cases.codebase_onboarding` — official OpenAI source for codebase understanding workflows.
- `openai.codex.use_cases.follow_goals` — official OpenAI source for long-running goals, stopping conditions, and checkpoint loops.
- `openai.codex.use_cases.frontend_designs` — official OpenAI source for screenshot/design-to-code and visual checks.
- `openai.codex.use_cases.refactor_your_codebase` — official OpenAI source for small reviewable refactor passes.
- `openai.codex.github_review` — official OpenAI source for Codex GitHub PR review.
- `openai.codex.noninteractive` — official OpenAI source for non-interactive Codex and automation workflows.
- `openai.codex.app_automations` — official OpenAI source for scheduled recurring Codex work.
- Maintainer synthesis: playbook structure derived from prior VCB chapters.

## Related Topics

- `vcb.chapter.understanding_unknown_codebase`
- `vcb.chapter.feature_slicing`
- `vcb.chapter.debugging_with_reproduction`
- `vcb.chapter.writing_updating_tests`
- `vcb.chapter.frontend_work`
- `vcb.chapter.reviewing_codex_output`
- `vcb.chapter.github_pr_review_with_codex`
- `vcb.chapter.ci_noninteractive_github_actions`
- `vcb.chapter.automations_recurring_work`
- `vcb.chapter.security_for_vibe_coders`
- `vcb.chapter.dependency_package_framework_decisions`
- `vcb.chapter.failure_modes_codex_work`
- `vcb.chapter.first_serious_app`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.codex_playbooks -->
