<!-- VCB:BEGIN_TOPIC id=vcb.chapter.agents_md_operating_manual version=0.1.0 -->
---
id: vcb.chapter.agents_md_operating_manual
title: "Chapter 18 — AGENTS.md: Your Repo’s Operating Manual for Codex"
type: chapter
chapter_number: 18
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
- Codex Cloud
- repo instructions
- persistent guidance

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
- vcb.shortcut.skipping_agents_md
- vcb.shortcut.overstuffing_agents_md
- vcb.shortcut.using_existing_local_setup

durable_principles:
- Repeated project corrections should become durable repo guidance.
- Good project guidance is short, concrete, and testable.
- Persistent instructions should state commands, conventions, do-not rules, and definition-of-done expectations.
- Stale instructions are worse than missing instructions because they create false confidence.

likely_to_change:
- AGENTS.md discovery order and override behavior
- instruction size limits and fallback file names
- how Codex surfaces project guidance in app, CLI, IDE, and cloud contexts
- future repo-guidance formats

obsolete_when:
- Codex no longer uses project instruction files for durable repository guidance.
- A newer official project-guidance mechanism replaces AGENTS.md and is documented as the recommended path.

related_topics:
- vcb.chapter.installing_and_configuring_codex
- vcb.chapter.codex_config_defaults
- vcb.chapter.four_part_prompt
- vcb.chapter.acceptance_criteria
- vcb.chapter.git_discipline
- vcb.codex.agents_md
- vcb.codex.config
- vcb.codex.skills
---

> Summary:
> AGENTS.md is the repo’s operating manual for Codex: concise, durable instructions that keep the agent from needing the same correction every task.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.agents_md_operating_manual.human -->
## 1. For the Human: Plain-Language Concept

### What this means

AGENTS.md is where you put the project-specific guidance you keep repeating to Codex.

Think of it like the note taped to the inside of a workshop door: before anyone starts working, they read the house rules. It should not be a novel. It should tell Codex how this repo works and what “good work” means here.

### Why it matters

Without durable guidance, you pay the same cost repeatedly:

- Codex guesses the package manager.
- Codex runs the wrong checks.
- Codex adds dependencies too quickly.
- Codex misses project conventions.
- Codex treats prototypes and production code the same.
- You keep correcting the same mistake in every session.

A good AGENTS.md file converts repeated correction into reusable context.

### The mental model

Use this ladder:

1. **Prompt** — one task only.
2. **AGENTS.md** — project working agreements Codex should remember every task.
3. **Config** — default permissions, model/provider, profiles, and tool settings.
4. **Skill** — a reusable workflow Codex can invoke.
5. **Hook** — deterministic enforcement when model obedience is not enough.

AGENTS.md is not the place for everything. It is the place for stable repo facts and working rules.

### What belongs

Good candidates:

- repo layout and important directories,
- install/build/test/lint/typecheck commands,
- package manager expectations,
- architecture boundaries,
- testing expectations,
- PR or final-report expectations,
- dependency rules,
- security red lines,
- “do not change” behavior,
- conventions that differ from common defaults.

Bad candidates:

- giant product strategy docs,
- stale onboarding manuals,
- every preference you have ever had,
- vague advice like “write clean code,”
- secrets or credentials,
- exact UI instructions that change frequently,
- long generated prose nobody will maintain.

### Minimal example

```markdown
# AGENTS.md

## Repo facts
- Package manager: pnpm.
- Main app: apps/web.
- Shared UI components: packages/ui.

## Commands
- Install: pnpm install
- Typecheck: pnpm typecheck
- Test changed package: pnpm --filter <package> test
- Lint: pnpm lint

## Working rules
- Do not add production dependencies without explaining the no-new-dependency option first.
- Keep behavior changes separate from refactors.
- For bugs, reproduce or explain why local reproduction is not available before patching.
- Final report must include files changed, checks run, and known gaps.
```

### What good looks like

Good guidance is:

- short enough to scan,
- specific enough to change behavior,
- tied to real repo commands,
- updated after repeated mistakes,
- clear about red lines.

### What bad looks like

Bad guidance is:

- long and stale,
- generic motivational advice,
- contradictory with package scripts,
- full of old commands,
- stuffed with secrets,
- written once and never maintained.

### Checklist

Before adding a rule, ask:

- Will Codex need this in many tasks?
- Is it true for this repo now?
- Is it specific enough to act on?
- Can it be checked by a command, file path, or review step?
- Does it belong in AGENTS.md, or should it be a skill/config/hook instead?

<!-- VCB:END_SECTION id=vcb.chapter.agents_md_operating_manual.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.agents_md_operating_manual.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to turn repeated corrections into durable, minimal project instructions without turning the file into a dumping ground.

### Diagnose the human’s current model

Ask:

- “What correction have you given Codex more than twice?”
- “What command did Codex guess wrong?”
- “What dependency or architecture behavior do you want it to avoid by default?”
- “Is this rule stable, or is it only for this task?”
- “Would a new teammate understand this rule?”

### Explanation strategy

Use the ladder: prompt for one task, AGENTS.md for stable repo rules, config for default runtime behavior, skills for repeated workflows, hooks for deterministic enforcement.

Do not tell the user to put everything into AGENTS.md. That creates context pollution. Help them separate stable operating agreements from volatile task instructions.

### Useful metaphors

- **Workshop sign:** the rules everyone reads before touching tools.
- **Restaurant prep sheet:** what the team needs before service starts.
- **House style guide:** not every opinion, only the conventions that prevent rework.

### Coaching tactics

- Convert repeated corrections into one concrete rule.
- Delete rules that are not action-guiding.
- Prefer command names and file paths over abstract advice.
- Add “ask before” rules for dependencies, migrations, auth, secrets, and production config.
- Keep final-report expectations explicit.
- When guidance is stale, say so directly and update it before relying on it.

### Prompt patterns

```text
Read the existing project guidance. Then inspect package scripts and repo layout.
Propose a concise AGENTS.md update with only durable rules.
Separate:
- repo facts,
- commands,
- conventions,
- do-not rules,
- final-report expectations.
Do not include secrets or task-specific instructions.
```

```text
We keep correcting Codex about [repeated issue].
Turn that into one durable project instruction.
Make it specific, testable, and short.
```

### Red flags to call out directly

- “This is not a project rule; it is a one-time prompt.”
- “This rule is too vague to affect Codex behavior.”
- “This file is becoming stale context. Shorten it.”
- “Do not put secrets or credentials in project guidance.”
- “A hook is better than AGENTS.md if the rule must never be bypassed.”

### Exercises

1. Ask the human to list three repeated Codex mistakes.
2. Convert each into a one-line project rule.
3. Remove any rule that cannot be observed in a diff, command, or final report.
4. Ask Codex to summarize the resulting guidance before starting a task.

<!-- VCB:END_SECTION id=vcb.chapter.agents_md_operating_manual.ai_coach -->

## Shortcut Reality

### The ideal practice

Create a small AGENTS.md file early, update it when repeated mistakes appear, and prune stale rules monthly.

### What users often do instead

They skip persistent guidance, paste the same instructions repeatedly, or dump a huge README into AGENTS.md and hope Codex figures it out.

### When the shortcut may be fine

Skipping AGENTS.md is fine for:

- a one-file throwaway script,
- a disposable prototype,
- a repo you will never revisit,
- a short supervised task where all instructions fit cleanly in the prompt.

### When the shortcut is a bad idea

Skipping or overstuffing guidance is a bad idea when:

- the repo is long-lived,
- multiple Codex sessions will touch it,
- several people use the same repo,
- the project has custom commands,
- dependencies, migrations, auth, payments, or deployment rules matter.

### Risk profile

- Probability of failure: medium without durable guidance.
- Impact if it fails: low in prototypes; high in production repos with custom rules.
- Ease of recovery: medium if the diff is small and committed; poor if stale guidance caused broad edits.
- Blast radius: repo-wide when commands/conventions are wrong.
- Skill needed to recover: medium; the human must identify which guidance misled the agent.
- Hidden cost: repeated usage waste and repeated human correction.

### Minimum guardrails

- Add only stable repo facts.
- Keep the file short.
- Include real commands.
- State “ask before” rules for high-risk areas.
- Review the file after repeated failures.
- Delete stale or contradictory instructions.

### Recovery plan

1. Ask Codex to summarize what guidance it used.
2. Compare that against current package scripts and repo layout.
3. Remove stale rules.
4. Commit the guidance fix separately from code changes.
5. Re-run the original task with the corrected guidance.

### AI coach guidance

Do not shame the user for skipping AGENTS.md in a tiny project. Move them up one guardrail: if the same correction appears twice, put it in durable guidance.

## Budget and Constraint Notes

### Cheapest reliable path

Write a minimal AGENTS.md with commands, repo layout, dependency rules, and final-report expectations. This saves usage by reducing repeated setup chatter.

### Fastest high-usage path

Use Codex to inspect the repo and propose a guidance file, then use a separate review pass to remove stale or vague rules before committing.

### Low-attention path

Require final reports, changed-file lists, checks run, and “ask before” rules for dependencies, migrations, auth, production config, and secrets.

### Production-quality path

Treat AGENTS.md like code: review it, commit it, update it after incidents, and keep it aligned with real commands and CI.

## Stable Core

- Durable repo guidance reduces repeated context loss.
- Stable commands and conventions belong close to the repo.
- “Do not” rules are only useful when they are specific.
- Persistent guidance should be shorter than the docs it summarizes.
- Guidance must be maintained or it becomes context pollution.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Current Codex behavior around instruction discovery, override names, fallback names, file-size limits, and how project guidance loads across surfaces is product-specific. Verify against official OpenAI Codex docs before writing exact setup instructions.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes Codex project-guidance discovery behavior.
- AGENTS.md is renamed, superseded, or merged into another official customization layer.
- Codex starts automatically extracting durable project rules from repos with reliable user control.
- The official docs change guidance file precedence, size limits, or trust behavior.

## Evidence and Sources

- `openai.codex.agents_md` — official OpenAI Codex source for AGENTS guidance discovery, global/project layering, overrides, and current volatile mechanics.
- `openai.codex.best_practices` — official OpenAI Codex source for turning repeatable guidance into reusable project context and avoiding repeated prompt friction.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: stable guidance should be concise, accurate, reviewable, and close to the project it governs.

No community practice is promoted to official guidance here. Product-specific details are treated as volatile.

## Related Topics

- `vcb.chapter.codex_config_defaults`
- `vcb.chapter.skills_reusable_workflows`
- `vcb.chapter.hooks_deterministic_guardrails`
- `vcb.chapter.installing_and_configuring_codex`
- `vcb.chapter.acceptance_criteria`
- `vcb.codex.agents_md`
- `vcb.shortcut.skipping_agents_md`
- `vcb.shortcut.overstuffing_agents_md`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.agents_md_operating_manual -->
