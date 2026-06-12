<!-- VCB:BEGIN_TOPIC id=vcb.chapter.automations_recurring_work version=0.1.0 -->
---
id: vcb.chapter.automations_recurring_work
title: "Chapter 29 — Automations: Recurring Work Without Recurring Prompts"
type: chapter
chapter_number: 29
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex Automations
- recurring tasks
- skills
- worktrees
- background tasks
- reports
- maintenance workflows

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE

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
- mvp
- production_build
- maintenance
- emergency_hotfix

attention_modes:
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.automating_unstable_workflow
- vcb.shortcut.automation_spam
- vcb.shortcut.unattended_mutation
- vcb.shortcut.unattended_long_runs

durable_principles:
- Automate only stable, repeatable workflows.
- Start recurring work as report-only before mutation.
- A scheduled prompt needs a clear cadence, scope, and stop condition.
- Automations need an inbox, triage rule, and cleanup rule.

likely_to_change:
- automation setup UI and cadence options
- local/project-scoped execution behavior
- worktree/local-directory behavior
- automation inbox behavior
- skill invocation behavior inside automations
- plan/usage economics

obsolete_when:
- Codex Automations are replaced or materially change execution semantics.
- Recurring task behavior, worktree isolation, or inbox/report handling changes materially.
- Official guidance changes on automation candidates and safety patterns.

related_topics:
- vcb.chapter.skills_reusable_workflows
- vcb.chapter.hooks_deterministic_guardrails
- vcb.chapter.ci_noninteractive_github_actions
- vcb.chapter.reviewing_codex_output
- vcb.chapter.security_for_vibe_coders
- vcb.codex.automations
- vcb.workflow.ci_noninteractive
---

> Summary:
> Automations are scheduled Codex tasks. They are useful for recurring, stable work such as reports, triage, summaries, and checks. They are dangerous when the workflow is still ambiguous or destructive.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.automations_recurring_work.human -->
## 1. For the Human: Plain-Language Concept

### What this means

An automation is a Codex task that runs on a schedule or recurring cadence instead of you typing the prompt each time.

Use automations for work that is boring, repeatable, and checkable. Do not use them for vague product decisions or high-risk code changes.

### Why it matters

If you ask Codex to do the same useful report every week, turn it into an automation. If you are still figuring out the prompt, do not automate it yet.

Automation removes friction. It also removes the moment where a human normally stops and thinks. That means the prompt must be narrower and safer than an interactive prompt.

### The mental model

A skill defines the method. An automation defines the schedule.

```text
Skill: how to do the bug triage report.
Automation: run that triage every Monday morning.
```

If the method is unstable, scheduling it just creates recurring confusion.

### Good automation candidates

Good candidates:

- weekly release-note draft;
- dependency-change summary;
- recent failed-test summary;
- bug triage inbox report;
- stale issue summary;
- PR risk summary;
- docs drift report;
- recurring lint/test failure explanation;
- read-only security/dependency audit summary.

Bad candidates:

- “improve the app”;
- broad refactors;
- auth/payment/security mutations;
- production migrations;
- dependency upgrades with auto-merge;
- anything that keeps producing noisy low-value findings.

### Automation lifecycle

Use this ladder:

```text
Manual prompt -> saved prompt -> skill -> manual dry run -> scheduled report -> scheduled branch proposal -> guarded mutation
```

Most workflows should stop at scheduled report.

### What good looks like

A good automation has:

- narrow scope;
- stable prompt;
- clear cadence;
- safe environment;
- report destination;
- “nothing to report” behavior;
- no unnecessary secrets;
- worktree or branch isolation for changes;
- triage rule for findings;
- stop rule when noisy.

### Checklist

Before scheduling:

- Have I run the exact prompt manually?
- Did the prompt produce useful output more than once?
- Is this report-only or mutation?
- What project/environment does it run in?
- Does it need a skill?
- What files may it touch?
- What secrets can it see?
- Where do findings go?
- When should I disable it?

<!-- VCB:END_SECTION id=vcb.chapter.automations_recurring_work.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.automations_recurring_work.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to automate stable workflows, not unstable ambitions. The safest default is scheduled read-only reporting.

### Diagnose the human’s current model

Ask:

- “Have you run this manually and gotten useful results?”
- “Is the workflow stable enough to schedule?”
- “Should this use a skill?”
- “What is the cadence?”
- “Where do findings go?”
- “What happens when there is nothing useful to report?”
- “Can it mutate code, or only report?”
- “How will you stop automation spam?”

### Explanation strategy

Use a promotion path:

1. Run the prompt manually.
2. Improve it until output is consistently useful.
3. Turn repeated method into a skill if needed.
4. Schedule report-only automation.
5. Review findings for a few cycles.
6. Consider branch-only mutation only for narrow tasks.

### Useful metaphors

- Automations are smoke detectors: useful when tuned, miserable when noisy.
- Scheduling a bad prompt is setting an alarm clock to annoy yourself.
- Report-only automation is a lookout; auto-mutation is a machine with tools in its hands.

### Coaching tactics

- Reject automating vague work.
- Ask for a dry-run record before scheduling.
- Prefer skills for longer repeatable methods.
- Require report fields and triage rules.
- Use worktrees for automation changes in Git repos.
- Disable noisy automations instead of teaching users to ignore them.
- Escalate hard around secrets, production data, migrations, deployments, and broad dependency upgrades.

### Prompt patterns

```text
Design a safe Codex automation.

Recurring job:
[what should run]

Cadence:
[when]

Mode:
- report-only first

Context:
[project, files, issue query, logs, checks]

Output:
- summary
- findings
- severity
- evidence
- recommended action
- nothing-to-report behavior

Stop conditions:
- noisy/low-value output for two runs
- requires production secrets
- wants to mutate auth/payments/migrations/deploy config
```

```text
Turn this repeated prompt into an automation plan, but do not schedule or mutate anything yet. First identify whether it should be a saved prompt, skill, hook, CI job, or automation.
```

### Red flags to call out directly

- “Do not automate a workflow you have not tested manually.”
- “If the automation is noisy, it will train you to ignore it.”
- “Recurring mutation needs branch/worktree isolation and human review.”
- “Do not schedule vague product work.”
- “Automation should have a disable condition.”

### Exercises

1. Pick one repeated task and run it manually twice.
2. Convert the output to a fixed report format.
3. Decide whether it needs a skill.
4. Define cadence and inbox.
5. Write the stop rule.

<!-- VCB:END_SECTION id=vcb.chapter.automations_recurring_work.ai_coach -->

## Shortcut Reality

### The ideal practice

Automate only stable, low-risk, repeatable workflows after manual dry runs. Start report-only. Add mutation only for narrow, isolated, review-gated tasks.

### What users often do instead

They schedule a broad prompt too early, get noisy findings, ignore the inbox, or let recurring jobs mutate code before the workflow has proven value.

### When the shortcut may be fine

Fast automation experiments may be fine in a disposable project with report-only output, fake data, no secrets, and a manual trigger or short trial cadence.

### When the shortcut is a bad idea

It is a bad idea for ambiguous product work, broad refactors, auth/payments/security changes, migrations, deployment config, dependency upgrades, or any automation that can make changes without branch isolation and review.

### Risk profile

- Probability of failure: medium; high when the workflow is untested.
- Impact if it fails: low for report noise; high for recurring mutation.
- Ease of recovery: high for disabling reports; medium/low for bad repeated patches.
- Blast radius: inbox quality, repo branches, automation budget, production if mutation/deploy is enabled.
- Skill needed to recover: low for noise; high for secret/data/deploy incidents.
- Hidden cost: alert fatigue, wasted usage, stale prompts, invisible recurring work.

### Minimum guardrails

- Manual dry run first.
- Fixed report format.
- Report-only initial mode.
- Clear cadence and destination.
- No secrets unless justified.
- Worktree/branch isolation for changes.
- Disable condition.
- Human review before merge/deploy.

### Recovery plan

1. Disable the automation.
2. Archive or triage noisy findings.
3. Inspect any branches/changes it created.
4. Revert bad patches.
5. Narrow the prompt or convert it into a skill.
6. Re-enable report-only for one trial period.

### AI coach guidance

Suggest automations only after repeated work exists. If the user wants automation because it feels powerful, route them to saved prompts, skills, hooks, or CI first depending on the job shape.

## Budget and Constraint Notes

### Cheapest reliable path

Do not schedule many automations. Use saved prompts or manual report runs until the task proves recurring value.

### Fastest high-usage path

Use automations for dependency summaries, CI failure triage, release-note drafts, and recurring review reports. Keep mutation branch-scoped and review-gated.

### Low-attention path

Low-attention automations should produce short reports, not broad patches. They need a findings inbox and explicit stop rules.

### Production-quality path

Use stable prompts, skills where appropriate, worktree isolation, least privilege, human triage, and documented ownership for each automation.

## Stable Core

- Repetition is a prerequisite for automation.
- Report-only is safer than mutation.
- Noisy automation loses trust.
- Scheduled work needs an inbox and a stop rule.
- Skills define method; automations define cadence.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Codex Automation UI, scheduling cadence, background execution environment, local-project versus worktree behavior, inbox behavior, skill invocation inside automations, and plan/usage economics are volatile. Verify official OpenAI docs before giving setup instructions.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex Automations change scheduling behavior, worktree/local execution semantics, findings inbox behavior, skill integration, or official best-practice guidance.

## Evidence and Sources

- `openai.codex.app_automations` — official OpenAI source for scheduled recurring tasks, findings inbox behavior, worktree/local execution, and automation-skill combination.
- `openai.codex.best_practices` — official OpenAI source for using automations after workflows become repetitive and stable.
- `openai.codex.skills` — official OpenAI source for reusable workflow packages that can support recurring automation methods.
- `openai.codex.use_cases.automation_bug_triage` — official OpenAI source for recurring bug triage and alert/report workflows.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: automation should be promoted from tested manual workflow to scheduled report before mutation.

## Related Topics

- vcb.chapter.skills_reusable_workflows
- vcb.chapter.hooks_deterministic_guardrails
- vcb.chapter.ci_noninteractive_github_actions
- vcb.chapter.reviewing_codex_output
- vcb.chapter.security_for_vibe_coders
- vcb.codex.automations
- vcb.workflow.ci_noninteractive

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.automations_recurring_work -->
