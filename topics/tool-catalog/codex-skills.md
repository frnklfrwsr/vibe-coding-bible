<!-- VCB:BEGIN_TOPIC id=tool.codex_skills version=0.1.0 -->
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
id: tool.codex_skills
title: Codex Skills
name: Codex Skills
category: codex_customization_skills
setup_effort: 'medium: requires a proven workflow, clear trigger description, boundaries, and optional assets or scripts'
maintenance_effort: 'medium to high: skills need pruning, trigger tuning, versioning, and overlap audits'
debugging_effort: 'medium: failures may come from poor descriptions, hidden assumptions, stale instructions, or script behavior'
lock_in_risk: 'moderate: reusable-agent skill concepts are portable, but Codex skill discovery and invocation behavior are first-party mechanics'
hidden_cost_risk: 'medium to high: skill sprawl hides context cost and makes the wrong reusable workflow easy to invoke'
codex_integration_value: strong for mature repeatable workflows that need consistent instructions across Codex surfaces
best_for:
- repeated workflows
- domain-specific review patterns
- team-standard output formats
- reusable maintenance procedures
not_for:
- one-off prompts
- unclear workflows
- skills that duplicate each other
- risky scripts without owner and review
integrates_with_codex:
- Codex App
- Codex CLI
- Codex IDE Extension
- Plugins
- AGENTS.md
hidden_costs:
- skill sprawl
- stale descriptions
- duplicated workflows
- unreviewed scripts or assets
applies_to:
- reusable workflows
- team playbooks
- domain procedures
- Codex customization
shortcut_profiles:
- vcb.shortcut.skill_overkill
- vcb.shortcut.skill_sprawl
- vcb.shortcut.process_overhead_for_tiny_project
- vcb.shortcut.copy_pasting_playbook_blindly
durable_principles:
- Package a workflow only after it has proven repeatable.
- Descriptions are routing contracts; vague descriptions select the wrong skill.
- A skill should reduce context noise, not hide unreviewed process.
likely_to_change:
- skill file format, locations, invocation affordances, progressive-disclosure behavior, plugin packaging, warnings, and client support
obsolete_when:
- OpenAI retires Codex Skills or replaces them with another documented reusable workflow mechanism.
related_topics:
- tool.codex_agents_md
- tool.codex_mcp
- vcb.codex.skills
- vcb.shortcut.skill_overkill
- vcb.shortcut.skill_sprawl
- vcb.chapter.prompt_library_to_team_workflow
---

# Codex Skills

> Summary:
> Codex Skills package repeatable workflows and domain expertise so Codex can use reusable instructions without pasting them into every prompt.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_skills.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex Skills are reusable workflow packages. A skill gives Codex scoped instructions and optional supporting resources for a task that repeats often enough to deserve packaging.

### Why it matters

Skills matter because repeated workflow prompts become inconsistent. A good skill makes a repeated process discoverable and reviewable without stuffing every task with the full procedure.

### What good looks like

A good skill has a narrow trigger, a clear non-trigger, short instructions, and testable output expectations.

### What bad looks like

A bad skill is created after one task, overlaps several existing skills, has vague trigger wording, or hides risky scripts behind a friendly name.

### Minimal example

After the same release-note workflow has been used several times, convert it into a skill with input requirements, output format, and review checklist.

### Best-fit cases

- repeated workflows
- domain-specific review patterns
- team-standard output formats
- reusable maintenance procedures

### Not-fit cases

- one-off prompts
- unclear workflows
- skills that duplicate each other
- risky scripts without owner and review

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: requires a proven workflow, clear trigger description, boundaries, and optional assets or scripts |
| Maintenance effort | medium to high: skills need pruning, trigger tuning, versioning, and overlap audits |
| Debugging effort | medium: failures may come from poor descriptions, hidden assumptions, stale instructions, or script behavior |
| Lock-in risk | moderate: reusable-agent skill concepts are portable, but Codex skill discovery and invocation behavior are first-party mechanics |
| Hidden cost risk | medium to high: skill sprawl hides context cost and makes the wrong reusable workflow easy to invoke |

### Checklist

- choose this customization/control surface only when the task repeats or the risk boundary matters
- write the intended scope, allowed actions, and forbidden zones before using it
- keep volatile product mechanics out of stable repo guidance unless source-checked
- require evidence before accepting any change that uses this surface
- review official OpenAI docs before relying on current setup behavior

<!-- VCB:END_SECTION id=tool.codex_skills.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_skills.ai_coach -->
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
Before creating a skill, prove this workflow has repeated. Define trigger, non-trigger, required inputs, output format, review checklist, and owner. If it is one-off, return a prompt snippet instead of a skill.
```

### Red flags

- the human wants a durable control layer before the workflow is proven
- the control affects secrets, auth, production, external tools, or recurring mutation
- the user cannot name the owner, rollback plan, or review evidence
- the instruction is vague enough that Codex cannot verify compliance

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, config keys, hook event names, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_skills.ai_coach -->

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

- `vcb.shortcut.skill_overkill`
- `vcb.shortcut.skill_sprawl`
- `vcb.shortcut.process_overhead_for_tiny_project`
- `vcb.shortcut.copy_pasting_playbook_blindly`

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

- skill sprawl
- stale descriptions
- duplicated workflows
- unreviewed scripts or assets

## Stable Core

- Package a workflow only after it has proven repeatable.
- Descriptions are routing contracts; vague descriptions select the wrong skill.
- A skill should reduce context noise, not hide unreviewed process.

## Volatile Surface

- skill file format, locations, invocation affordances, progressive-disclosure behavior, plugin packaging, warnings, and client support

Exact prices, plan packaging, usage-credit quantities, feature availability, command flags, config keys, hook event names, model menus, context limits, UI labels, setup mechanics, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires Codex Skills or replaces them with another documented reusable workflow mechanism.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.skills` — official/synthesis source anchor for this tool card.
- `openai.codex.customization` — official/synthesis source anchor for this tool card.
- `openai.codex.plugins` — official/synthesis source anchor for this tool card.
- `openai.codex.best_practices` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex_agents_md`
- `tool.codex_mcp`
- `vcb.codex.skills`
- `vcb.shortcut.skill_overkill`
- `vcb.shortcut.skill_sprawl`
- `vcb.chapter.prompt_library_to_team_workflow`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_skills -->
