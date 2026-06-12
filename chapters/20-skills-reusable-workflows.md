<!-- VCB:BEGIN_TOPIC id=vcb.chapter.skills_reusable_workflows version=0.1.0 -->
---
id: vcb.chapter.skills_reusable_workflows
title: "Chapter 20 — Skills: Reusable Workflows for Repeated Tasks"
type: chapter
chapter_number: 20
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- reusable workflows
- skills
- team workflow

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
- vcb.shortcut.skill_overkill
- vcb.shortcut.skill_sprawl
- vcb.shortcut.vague_prompt

durable_principles:
- A skill packages a repeated workflow so Codex can apply it consistently.
- Skill descriptions are part of the routing interface, not decorative prose.
- Start with one clear job before adding scripts, references, or assets.
- Skills should reduce repeated prompts, not hide vague process.

likely_to_change:
- skill directory format
- skill discovery and invocation mechanics
- skill creator behavior
- global vs repo skill locations
- skill packaging and plugin behavior

obsolete_when:
- Codex replaces skills with a different official reusable-workflow mechanism.
- Skill trigger behavior changes enough that current description-writing advice is no longer accurate.

related_topics:
- vcb.chapter.agents_md_operating_manual
- vcb.chapter.codex_config_defaults
- vcb.chapter.mcp_external_tools
- vcb.chapter.hooks_deterministic_guardrails
- vcb.chapter.acceptance_criteria
- vcb.codex.skills
- vcb.codex.mcp
---

> Summary:
> A skill is a reusable Codex playbook for work you do repeatedly. If you keep pasting the same prompt or making the same correction, the workflow may deserve a skill.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.skills_reusable_workflows.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A skill is a reusable workflow package for Codex.

If AGENTS.md is the repo’s operating manual, a skill is a recipe card: “When doing this job, follow these steps, use these references, and produce this kind of output.”

### Why it matters

Repeated work wastes attention and usage when it stays as copy-paste prompts.

Good skill candidates:

- release note drafting,
- PR review against a checklist,
- migration planning,
- dependency audit reports,
- bug triage summaries,
- incident or log triage,
- standard debugging flow,
- docs update routine.

Bad skill candidates:

- one-off tasks,
- vague preferences,
- entire product strategy,
- workflows nobody has tried manually,
- giant process documents that Codex cannot reliably choose.

### The mental model

Use this path:

```text
Do it manually once → repeat it twice → tighten the prompt → turn it into a skill → test the trigger → improve from use.
```

Do not start by making a giant skill. Start with one job that has clear inputs and outputs.

### What a skill should contain

A good skill usually answers:

- When should Codex use this skill?
- When should it not use it?
- What inputs does it need?
- What files/tools should it inspect?
- What output format should it produce?
- What checks or review criteria apply?
- What should Codex avoid doing?

### Minimal skill concept

```markdown
---
name: dependency-audit-summary
description: Use when asked to review dependency risk in this repo. Do not use for installing packages.
---

Goal: produce a dependency risk summary.
Steps:
1. Inspect package manifests and lockfiles.
2. Identify changed or risky dependencies.
3. Do not run lifecycle scripts.
4. Report findings by severity.
5. Recommend next checks, not automatic fixes.
```

### What good looks like

Good skills are:

- narrow,
- named clearly,
- triggered by obvious task language,
- explicit about non-goals,
- tested on real tasks,
- improved after failures,
- not overloaded with every edge case.

### What bad looks like

Bad skills are:

- broad “do everything” agents,
- unclear descriptions,
- duplicate skills with overlapping names,
- scripts that run risky actions without guardrails,
- stale references,
- skills created before the workflow is understood.

### Checklist

Make a skill only when:

- the workflow repeats,
- the inputs and outputs are predictable,
- the task benefits from consistent steps,
- a long prompt keeps being reused,
- the skill can be tested on examples,
- the skill will reduce future confusion.

<!-- VCB:END_SECTION id=vcb.chapter.skills_reusable_workflows.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.skills_reusable_workflows.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use skills as compact reusable workflows, not as a dumping ground for vague preferences or premature process automation.

### Diagnose the human’s current model

Ask:

- “How many times have you run this workflow?”
- “What is the exact trigger phrase?”
- “What output should the skill always produce?”
- “What should it refuse or avoid?”
- “Could a plain AGENTS.md rule solve this instead?”
- “Does this need scripts or just instructions?”

### Explanation strategy

Explain the customization stack:

- AGENTS.md: durable repo rules.
- Config: runtime defaults.
- Skill: repeated workflow.
- MCP: external tool/context access.
- Hook: deterministic enforcement.

Then test whether the user’s desired behavior is truly a repeated workflow.

### Useful metaphors

- **Recipe card:** repeatable steps for a known dish.
- **Station checklist:** what to inspect before doing a specialized job.
- **Power tool jig:** useful when making the same cut repeatedly; overhead for one cut.

### Coaching tactics

- Start with an instruction-only skill.
- Make the description specific; it is part of routing.
- Include “do not use this skill when...” lines.
- Prefer one skill per job.
- Add scripts only when they improve reliability.
- Ask for examples and counterexamples.
- Test trigger behavior before sharing broadly.

### Prompt patterns

```text
We have repeated this workflow three times.
Turn it into a small Codex skill.
First list:
- trigger phrases,
- non-trigger cases,
- required inputs,
- expected output,
- risky actions to avoid.
Then draft the SKILL.md content.
Keep it instruction-only unless a script clearly improves reliability.
```

```text
Review this skill for trigger quality.
Does the description clearly say when to use it and when not to use it?
Find overlap with existing skills and suggest a narrower scope.
```

### Red flags to call out directly

- “This is not repeated enough to deserve a skill.”
- “The skill description is too vague to trigger reliably.”
- “This skill overlaps with another skill; merge or narrow it.”
- “Do not put dangerous commands in a skill without approval boundaries.”
- “A hook, not a skill, should enforce this rule.”

### Exercises

1. Pick one repeated workflow.
2. Write three trigger phrases and three non-trigger cases.
3. Draft an instruction-only skill.
4. Run it on one representative task.
5. Update the description based on whether Codex chose it correctly.

<!-- VCB:END_SECTION id=vcb.chapter.skills_reusable_workflows.ai_coach -->

## Shortcut Reality

### The ideal practice

Create skills only for repeated workflows with clear triggers, inputs, outputs, and guardrails.

### What users often do instead

They make skills too early, create overlapping skills, or bury a long prompt inside a skill before they understand the workflow.

### When the shortcut may be fine

Skipping skills is fine when:

- the workflow is rare,
- the prompt is short,
- the repo is temporary,
- you are still exploring the process,
- a simple AGENTS.md rule solves the issue.

Creating a rough local skill is fine when you are experimenting and it is not shared as team policy yet.

### When the shortcut is a bad idea

Skill overkill is a bad idea when:

- the skill hides risky commands,
- several skills overlap,
- the description is vague,
- the workflow changes every time,
- the team starts trusting an untested skill.

### Risk profile

- Probability of failure: medium for vague or overlapping skills.
- Impact if it fails: low for reports; high if scripts mutate code, dependencies, or deployment state.
- Ease of recovery: medium if skills are versioned and behavior is reviewable.
- Blast radius: one workflow at first; team-wide if shared.
- Skill needed to recover: medium; maintainers must debug trigger behavior and instructions.
- Hidden cost: skill sprawl and stale process.

### Minimum guardrails

- Start local.
- Keep the first version instruction-only.
- Include non-trigger cases.
- Avoid automatic destructive actions.
- Test on at least one real example before sharing.
- Keep skills one-job wide.

### Recovery plan

1. Disable or move the bad skill.
2. Identify whether the failure was trigger, instruction, or script behavior.
3. Narrow the description.
4. Add non-trigger examples.
5. Re-test on a representative task.
6. Share only after the skill behaves predictably.

### AI coach guidance

When a user wants a skill for a one-off task, push back. A good alternative is a saved prompt or AGENTS.md rule. Suggest a skill only when repetition is real.

## Budget and Constraint Notes

### Cheapest reliable path

Use saved prompts and AGENTS.md until a workflow repeats. Convert only high-friction repeated tasks into small instruction-only skills.

### Fastest high-usage path

Use skills for release notes, reviews, triage, migration plans, dependency audits, and other repeated jobs. Pair them with final reports and review workflows.

### Low-attention path

Skills must produce structured outputs, list actions taken, and avoid mutation unless the task explicitly approves it.

### Production-quality path

Version skills, test trigger behavior, review scripts, and keep skills scoped to one job. Treat shared skills like team tooling.

## Stable Core

- Repeated workflows should become reusable artifacts.
- Skill descriptions are routing surfaces.
- Narrow skills beat giant process bundles.
- Scripts increase power and risk.
- Skills should reduce repeated prompting, not replace judgment.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Skill file structure, invocation mechanisms, discovery locations, context-budget behavior, and packaging/plugin behavior are current Codex product details. Verify official OpenAI docs before publishing exact operational instructions.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes the official skill format or required metadata.
- Codex changes explicit or implicit skill invocation mechanics.
- Skill packaging moves into plugins or another official distribution format.
- Repo/user/admin/system skill locations change.
- The current skill creator workflow is replaced.

## Evidence and Sources

- `openai.codex.skills` — official OpenAI Codex source for skill structure, metadata, invocation, locations, and progressive disclosure.
- `openai.codex.use_cases.reusable_codex_skills` — official OpenAI Codex use-case source for saving workflows as skills.
- `openai.codex.customization` — official OpenAI Codex source for how skills fit with AGENTS guidance and MCP.
- `openai.codex.best_practices` — official OpenAI Codex source for turning repeatable work into focused skills.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: reusable workflow artifacts should be small, testable, and maintained.

No community trigger hacks are treated as official guidance.

## Related Topics

- `vcb.chapter.agents_md_operating_manual`
- `vcb.chapter.mcp_external_tools`
- `vcb.chapter.hooks_deterministic_guardrails`
- `vcb.chapter.acceptance_criteria`
- `vcb.codex.skills`
- `vcb.shortcut.skill_overkill`
- `vcb.shortcut.skill_sprawl`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.skills_reusable_workflows -->
