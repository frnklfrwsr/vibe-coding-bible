<!-- VCB:BEGIN_TOPIC id=vcb.chapter.prompt_library_to_team_workflow version=0.1.0 -->
---
id: vcb.chapter.prompt_library_to_team_workflow
title: "Chapter 31 — From Prompt Library to Team Workflow"
type: chapter
chapter_number: 31
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
- AGENTS.md
- Codex config
- skills
- hooks
- automations
- CI
- teams

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
- vcb.shortcut.process_overhead_for_tiny_project
- vcb.shortcut.team_workflow_without_team
- vcb.shortcut.overstuffing_agents_md
- vcb.shortcut.stale_agents_md

durable_principles:
- Repeated instructions should become durable artifacts only when they solve repeated friction.
- A team workflow should encode behavior, not ceremony.
- Small accurate rules beat large stale manuals.

likely_to_change:
- Codex customization layers
- skill/plugin packaging
- automation UI and cadence controls
- team/workspace governance features
- exact config keys and commands

obsolete_when:
- Codex introduces an integrated team workflow primitive that replaces several current customization layers.
- Official customization guidance materially changes.

related_topics:
- vcb.chapter.four_part_prompt
- vcb.chapter.agents_md_operating_manual
- vcb.chapter.codex_config_defaults
- vcb.chapter.skills_reusable_workflows
- vcb.chapter.hooks_deterministic_guardrails
- vcb.chapter.automations_recurring_work
- vcb.chapter.ci_noninteractive_github_actions
---


> Summary:
> A prompt library becomes valuable only when repeated prompts turn into durable project behavior: AGENTS.md rules, config defaults, skills, hooks, automations, review guidance, and CI checks.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.prompt_library_to_team_workflow.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A prompt library is a drawer of reusable instructions. A team workflow is the system that makes the right instructions show up at the right time without everyone remembering to paste them.

The progression looks like this:

```text
one useful prompt
→ saved prompt snippet
→ AGENTS.md rule
→ config default
→ skill for repeated work
→ hook for deterministic guardrail
→ automation or CI job for recurring work
```

Do not treat that ladder as a checklist. It is not mature to add every layer. It is mature to notice repeated friction and move one step toward a durable fix.

### The mental model

Think of your project as a workshop. A prompt is a note you hand to a worker. `AGENTS.md` is the sign on the wall. Config is the default position of the machines. A skill is a labeled jig for a repeated job. A hook is a hard stop that prevents a dangerous move. Automation is a scheduled maintenance routine.

A good workflow makes the easy path the safe path.

### What belongs in a prompt library

Use prompt snippets for things that are useful but not always true:

- review this diff for auth and data risks;
- write a plan before editing;
- generate acceptance criteria for this feature;
- produce a bug repro checklist;
- summarize changed files and checks run;
- ask for a no-new-dependency solution first.

Prompt snippets are flexible. Keep them there until the rule becomes repeated and project-specific.

### What belongs in durable workflow

Move something out of the prompt library when it becomes a repeated project rule:

- test command always required before final report;
- no new production dependency without approval;
- use the existing design-system components;
- preserve public API shape unless explicitly told otherwise;
- never touch production deploy config in broad refactors;
- write changelog notes for user-visible changes.

Those belong in `AGENTS.md`, config, skills, hooks, or CI depending on how enforceable they need to be.

### The smallest useful workflow stack

For a solo serious app, a good starting point is:

1. A short `AGENTS.md` with repo layout, commands, conventions, done criteria, and forbidden areas.
2. A few saved prompts for planning, diff review, debugging, and final reports.
3. Config defaults for safer permissions and normal reasoning style.
4. One or two checks Codex can run reliably.
5. A habit: when Codex repeats the same mistake twice, convert the correction into durable guidance.

For a team, add:

- PR review guidance;
- CI checks that match the real release gate;
- ownership rules for risky areas;
- skills for repeated workflows;
- hooks only for rules that must not depend on the model remembering.

### What bad looks like

Bad workflow maturity looks busy but does not improve outcomes:

- 40 prompt snippets nobody uses;
- `AGENTS.md` full of vague advice like "write clean code";
- config nobody understands;
- brittle hooks that block normal work;
- automations that spam low-value findings;
- skills for rare tasks;
- team process copied from another repo without matching your risks.

If a workflow artifact does not reduce rework, prevent a recurring mistake, or make review easier, it is probably overhead.

### Monthly cleanup

Once a month, ask:

- Which prompt did we paste repeatedly?
- Which Codex mistake happened twice?
- Which rule is stale or contradicted by current code?
- Which automation produced noise?
- Which hook blocked real work?
- Which check actually prevented a bad merge?

Delete stale process. Keep the parts that earn their keep.
<!-- VCB:END_SECTION id=vcb.chapter.prompt_library_to_team_workflow.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.prompt_library_to_team_workflow.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that durable workflow is not bureaucracy. It is captured learning. The goal is to move repeated instructions from memory into the smallest durable artifact that reliably changes Codex behavior.

### Diagnose the human’s current model

Ask:

- Are they repeating the same prompt every session?
- Are they correcting the same Codex mistake repeatedly?
- Are they trying to solve a one-off problem with permanent process?
- Are they adding hooks/skills/automations because they sound advanced?
- Does the repo have a real definition of done?

### Explanation strategy

Use a ladder, not a sermon:

```text
prompt snippet → AGENTS.md → config → skill → hook → automation/CI
```

For each repeated problem, ask what the smallest durable fix is. Do not jump to hooks or automations if an `AGENTS.md` note or saved prompt would solve it.

### Useful metaphors

- **Prompt library:** sticky notes.
- **AGENTS.md:** workshop sign on the wall.
- **Config:** machine defaults.
- **Skill:** reusable jig for a repeated cut.
- **Hook:** physical guardrail on a saw.
- **Automation:** scheduled maintenance.

### Coaching tactics

- Turn repeated human corrections into candidate repo guidance.
- Keep durable rules short, concrete, and testable.
- Push back on process cosplay: process that does not reduce mistakes is clutter.
- Map each artifact to a failure it prevents.
- Ask for evidence before adding a new workflow layer.

### Prompt patterns

```text
Review our last three Codex corrections and propose the smallest durable workflow update.
Choose only one of: prompt snippet, AGENTS.md rule, config default, skill, hook, automation, or CI check.
Explain why that level is sufficient.
```

```text
Audit AGENTS.md and our prompt library.
Remove stale or vague guidance.
Keep only rules that are specific, current, and useful for Codex behavior.
Report what you removed and why.
```

### Red flags to call out directly

- The user wants a hook for a judgment problem.
- The user wants a skill before the workflow has repeated twice.
- The user is copying another team’s process without matching project risk.
- The user’s prompt library contains contradictory commands.
- The user treats automation volume as quality.

### Exercises

Have the human pick one repeated Codex failure and classify the smallest durable fix. Then ask Codex to draft only that fix, not a full process overhaul.
<!-- VCB:END_SECTION id=vcb.chapter.prompt_library_to_team_workflow.ai_coach -->

## Shortcut Reality

### The ideal practice

Keep ad hoc prompts for flexible work. Promote only repeated, stable, project-specific instructions into durable workflow artifacts.

### What users often do instead

Users either keep everything as copy/paste prompts forever, or they overcorrect and build a heavy process system before the project needs it.

### When the shortcut may be fine

For disposable prototypes, one-off demos, weekend apps, or solo experiments, a prompt library plus Git checkpoints may be enough.

### When the shortcut is a bad idea

Skipping durable workflow becomes expensive when multiple people or agents touch the repo, when checks differ by project, when review expectations are inconsistent, or when the repo has real users, secrets, payments, or production deploys.

### Risk profile

- Probability of failure: medium if repeated guidance stays manual.
- Impact if it fails: low for prototypes; high for team production repos.
- Ease of recovery: medium if changes are in Git; low if bad process silently shapes many tasks.
- Blast radius: grows with team size, automation, and production scope.
- Skill needed to recover: workflow design plus repo knowledge.
- Hidden cost: stale rules and process noise.

### Minimum guardrails

- Keep `AGENTS.md` short.
- Add durable rules only after repeated friction.
- Review workflow artifacts monthly.
- Make every durable rule concrete and testable.
- Do not automate a workflow that is still ambiguous.

### Recovery plan

If process gets heavy, pause new automation. List every guidance artifact, mark each as keep/delete/merge, remove contradictions, and keep only the artifacts that prevent specific recurring failures.

### AI coach guidance

Do not recommend more process by default. Recommend the smallest artifact that removes repeated work or risk.

## Budget and Constraint Notes

### Cheapest reliable path

Use four saved prompts: plan-only, implementation, review, and final report. Add a short `AGENTS.md` only when repeated instructions appear.

### Fastest high-usage path

Use multiple durable layers: `AGENTS.md`, config profiles, skills for repeated tasks, review agents, CI summaries, and automations. Keep each layer narrow.

### Low-attention path

Low-attention work needs stronger defaults: clear done criteria, final reports, bounded permissions, and report-only automations before mutation.

### Production-quality path

Production workflows need a written definition of done, stable checks, PR review expectations, dependency/security rules, rollback notes, and a recurring cleanup loop for stale guidance.

## Stable Core

- Repeated instructions should become durable only when repetition proves value.
- The smallest durable artifact is usually better than the most sophisticated artifact.
- Team workflow exists to reduce missed context, weak review, and repeated mistakes.
- Process should be deleted when it stops earning its cost.

## Volatile Surface

- Exact Codex customization surfaces.
- Config keys and UI locations.
- Skill/plugin packaging and invocation mechanics.
- Hook event schemas.
- Automation scheduling and inbox behavior.
- Workspace/team governance features.

## Obsolescence Watch

Review this chapter if Codex introduces a unified workflow/configuration layer that replaces current customization primitives, or if official guidance changes the relationship among `AGENTS.md`, config, skills, hooks, automations, and CI.

## Evidence and Sources

- `openai.codex.best_practices` — official OpenAI source for treating Codex like a teammate configured and improved over time, plus durable guidance through AGENTS.md, config, skills, MCP, and automations.
- `openai.codex.agents_md` — official OpenAI source for persistent repo guidance and instruction layering.
- `openai.codex.config_basic` — official OpenAI source for user/project configuration layers.
- `openai.codex.skills` — official OpenAI source for reusable workflow packages.
- `openai.codex.hooks` — official OpenAI source for deterministic lifecycle scripts.
- `openai.codex.app_automations` — official OpenAI source for recurring scheduled Codex tasks.
- `openai.codex.guide_ai_native_engineering_team` — official OpenAI source for team/process changes around agentic software development.
- Maintainer synthesis: stable engineering practice around process minimization, feedback loops, and captured learning.

## Related Topics

- `vcb.chapter.four_part_prompt`
- `vcb.chapter.agents_md_operating_manual`
- `vcb.chapter.codex_config_defaults`
- `vcb.chapter.skills_reusable_workflows`
- `vcb.chapter.hooks_deterministic_guardrails`
- `vcb.chapter.automations_recurring_work`
- `vcb.chapter.ci_noninteractive_github_actions`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.prompt_library_to_team_workflow -->
