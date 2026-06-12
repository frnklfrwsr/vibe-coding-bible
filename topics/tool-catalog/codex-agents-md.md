<!-- VCB:BEGIN_TOPIC id=tool.codex_agents_md version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
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
evidence_scope: official OpenAI/Codex tool documentation plus VCB maintainer synthesis for setup, risk, budget, and coaching guidance
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
type: tool_card
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
last_pricing_reviewed: '2026-06-10'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
id: tool.codex_agents_md
title: Codex AGENTS.md
name: Codex AGENTS.md
category: codex_customization_guidance
setup_effort: 'low to medium: requires curating durable repo rules and placing guidance where it applies'
maintenance_effort: 'medium: guidance must be pruned when commands, architecture, or team norms change'
debugging_effort: 'low to medium: failures usually come from missing, stale, contradictory, or overbroad instructions'
lock_in_risk: 'low: project guidance is plain text, but Codex-specific discovery and precedence behavior are first-party mechanics'
hidden_cost_risk: 'medium: stale guidance burns usage, causes wrong edits, and makes every future task noisier'
codex_integration_value: strong for reducing repeated setup/context errors across Codex App, CLI, IDE, and cloud tasks
best_for:
- long-lived repositories
- teams with repeated Codex corrections
- repo-specific commands and conventions
- review expectations that should persist across surfaces
not_for:
- throwaway one-file experiments
- temporary project notes
- large context dumps
- secrets or private operational details
integrates_with_codex:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub Review
hidden_costs:
- guidance drift
- overloaded context
- contradictory nested rules
- false confidence from stale commands
applies_to:
- repositories
- durable project guidance
- team conventions
- review instructions
shortcut_profiles:
- vcb.shortcut.skipping_agents_md
- vcb.shortcut.overstuffing_agents_md
- vcb.shortcut.stale_agents_md
- vcb.shortcut.context_dumping
durable_principles:
- Durable repo guidance should be short, current, and testable.
- Repeated Codex mistakes belong in guidance only after they are recurring.
- Guidance is not evidence; diffs and checks still decide whether work is done.
likely_to_change:
- AGENTS.md discovery order, fallback names, size limits, override behavior, loaded-instruction reporting, and interaction with config, skills, hooks, and cloud surfaces
obsolete_when:
- OpenAI replaces AGENTS.md with another documented durable instruction mechanism or changes guidance discovery materially.
related_topics:
- tool.codex
- tool.codex_config
- tool.codex_skills
- tool.codex_hooks
- vcb.codex.agents_md
- vcb.shortcut.skipping_agents_md
- vcb.shortcut.stale_agents_md
---

# Codex AGENTS.md

> Summary:
> AGENTS.md is the durable instruction layer for repo guidance that Codex should apply before work starts.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_agents_md.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

AGENTS.md is a project guidance file. It carries durable instructions such as repo layout, test commands, review expectations, dependency rules, and local conventions so the user does not retype them every task.

### Why it matters

It matters because repeated corrections are expensive. Good guidance turns recurring feedback into a short operating manual; bad guidance pollutes every task with stale or untestable rules.

### What good looks like

Good AGENTS.md guidance is concise, current, local to the scope where it applies, and written as rules Codex can actually follow or verify.

### What bad looks like

Bad AGENTS.md guidance is a dumping ground for old plans, huge architecture essays, contradictory commands, or vague preferences that hide what evidence proves done.

### Minimal example

If Codex repeatedly edits generated files, add a durable rule naming the generated directory, the allowed source directory, and the checks required before completion.

### Best-fit cases

- long-lived repositories
- teams with repeated Codex corrections
- repo-specific commands and conventions
- review expectations that should persist across surfaces

### Not-fit cases

- throwaway one-file experiments
- temporary project notes
- large context dumps
- secrets or private operational details

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | low to medium: requires curating durable repo rules and placing guidance where it applies |
| Maintenance effort | medium: guidance must be pruned when commands, architecture, or team norms change |
| Debugging effort | low to medium: failures usually come from missing, stale, contradictory, or overbroad instructions |
| Lock-in risk | low: project guidance is plain text, but Codex-specific discovery and precedence behavior are first-party mechanics |
| Hidden cost risk | medium: stale guidance burns usage, causes wrong edits, and makes every future task noisier |

### Checklist

- choose this customization/control surface only when the task repeats or the risk boundary matters
- write the intended scope, allowed actions, and forbidden zones before using it
- keep volatile product mechanics out of stable repo guidance unless source-checked
- require evidence before accepting any change that uses this surface
- review official OpenAI docs before relying on current setup behavior

<!-- VCB:END_SECTION id=tool.codex_agents_md.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_agents_md.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach this as a Codex control surface. The goal is to make repeated behavior safer and more consistent without hiding risk behind configuration or reusable process.

### Diagnostic questions

- Is the user solving a repeated problem or just avoiding a one-time prompt?
- Which primary Codex surface will this control layer affect?
- What permission, context, external-tool, or lifecycle boundary changes?
- What artifact proves the control worked: diff, report, log, citation, test output, or review note?
- What should stop the workflow immediately?

### Coaching tactics

- route surface-choice questions through `tool.codex` first, then this customization/control card if relevant
- separate stable workflow principles from volatile setup mechanics
- prefer narrow, testable rules over broad policy prose
- pair every shortcut warning with the smallest guardrail that changes the risk profile
- require human review when secrets, account authority, production state, external tools, or persistent data are involved

### Prompt pattern

```text
Review or draft AGENTS.md for this repo. Include only durable rules: repo layout, setup/check commands, do-not-touch areas, review expectations, dependency rules, and done criteria. Remove stale or temporary context.
```

### Red flags

- the human wants a durable control layer before the workflow is proven
- the control affects secrets, auth, production, external tools, or recurring mutation
- the user cannot name the owner, rollback plan, or review evidence
- the instruction is vague enough that Codex cannot verify compliance

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, config keys, hook event names, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_agents_md.ai_coach -->

## Shortcut Reality

### The ideal practice

Use this tool only after the durable behavior, trust boundary, evidence requirement, and owner are clear.

### What users often do instead

Users often add a durable control layer because it feels professional, then discover that stale defaults, broad instructions, external-tool access, reusable workflows, or lifecycle scripts have multiplied the review problem.

### When the shortcut may be acceptable

The shortcut can be acceptable for a low-risk repo, a proven workflow, read-only/report-first behavior, or a disposable prototype where rollback is trivial and no sensitive state is exposed.

### When it becomes a bad trade

It becomes a bad trade when the control can mutate broad code, touch credentials, connect external systems, hide stale assumptions, or create false confidence without reviewable evidence.

### Relevant shortcut cards

- `vcb.shortcut.skipping_agents_md`
- `vcb.shortcut.overstuffing_agents_md`
- `vcb.shortcut.stale_agents_md`
- `vcb.shortcut.context_dumping`

### Minimum guardrails

- one purpose per control layer
- explicit owner and review cadence
- narrow permissions and scoped data access
- evidence packet before acceptance
- rollback plan before production or shared-team use

### Recovery plan

Disable or revert the control layer, preserve the transcript/logs/config diff, inspect affected output, rotate exposed secrets if needed, remove broad approvals, and restart with a smaller tested rule.

## Budget and Constraint Notes

### Cheapest reliable path

Use prompts and AGENTS.md-style durable guidance first. Add config, skills, MCP, or hooks only when repeated work or risk justifies the maintenance cost.

### Fastest high-usage path

Use this control surface when it reduces repeated setup and review noise. If it adds hidden context, external calls, or brittle checks, it creates speed theater rather than throughput.

### Low-attention path

Low-attention use requires narrow scope, stop conditions, and reviewable output. A durable control layer does not make unattended mutation safe by itself.

### Production-quality path

Production use requires least privilege, source-checked mechanics, testable rules, auditability, and human acceptance based on artifacts rather than summaries.

### Hidden costs to watch

- guidance drift
- overloaded context
- contradictory nested rules
- false confidence from stale commands

## Stable Core

- Durable repo guidance should be short, current, and testable.
- Repeated Codex mistakes belong in guidance only after they are recurring.
- Guidance is not evidence; diffs and checks still decide whether work is done.

## Volatile Surface

- AGENTS.md discovery order, fallback names, size limits, override behavior, loaded-instruction reporting, and interaction with config, skills, hooks, and cloud surfaces

Exact prices, plan packaging, usage-credit quantities, feature availability, command flags, config keys, hook event names, model menus, context limits, UI labels, setup mechanics, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI replaces AGENTS.md with another documented durable instruction mechanism or changes guidance discovery materially.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.agents_md` — official/synthesis source anchor for this tool card.
- `openai.codex.customization` — official/synthesis source anchor for this tool card.
- `openai.codex.best_practices` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex`
- `tool.codex_config`
- `tool.codex_skills`
- `tool.codex_hooks`
- `vcb.codex.agents_md`
- `vcb.shortcut.skipping_agents_md`
- `vcb.shortcut.stale_agents_md`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_agents_md -->
