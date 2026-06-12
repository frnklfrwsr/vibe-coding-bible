<!-- VCB:BEGIN_TOPIC id=tool.codex_config version=0.1.0 -->
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
id: tool.codex_config
title: Codex Config
name: Codex Config
category: codex_customization_config
setup_effort: 'medium: requires understanding project risk, current config layers, trust posture, and which defaults should persist'
maintenance_effort: 'medium: defaults need review when project phase, permissions, models, tools, or team norms change'
debugging_effort: 'medium: failures may come from precedence, stale profiles, untrusted project layers, or conflicting local defaults'
lock_in_risk: 'moderate: config is first-party Codex behavior even when the underlying safety principles are portable'
hidden_cost_risk: 'high: permissive defaults can cause repeated broad access, unexpected tool use, or expensive recovery work'
codex_integration_value: strong for turning safe repeated behavior into defaults across Codex CLI and IDE surfaces
best_for:
- repeatable local Codex defaults
- project-specific permission posture
- separating prototype and production behavior
- shared team expectations for local clients
not_for:
- hiding risky permissions
- one global full-access habit
- untrusted project overrides
- memorizing volatile keys instead of checking docs
integrates_with_codex:
- Codex CLI
- Codex IDE Extension
- Codex App
- MCP
- Hooks
hidden_costs:
- stale profiles
- permission drift
- hard-to-debug precedence
- unsafe inherited defaults
applies_to:
- local Codex clients
- trusted projects
- team defaults
- risk-scaled operating modes
shortcut_profiles:
- vcb.shortcut.default_config_forever
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.full_access_automation
- vcb.shortcut.unattended_mutation
durable_principles:
- Defaults are policy; set them by risk class, not convenience.
- Project configuration should be trusted deliberately.
- Profiles are useful only when humans know which risk posture they selected.
likely_to_change:
- config file locations, precedence, exact keys, profile mechanics, sandbox and approval setting names, project-trust behavior, and managed-configuration behavior
obsolete_when:
- OpenAI replaces Codex config files/profiles with another documented configuration system or changes precedence materially.
related_topics:
- tool.codex_cli
- tool.codex_ide_extension
- tool.codex_mcp
- tool.codex_hooks
- vcb.codex.config
- vcb.constraints.operating_mode
- vcb.shortcut.default_config_forever
---

# Codex Config

> Summary:
> Codex config is the durable defaults layer for local/project behavior, permissions posture, profiles, and connected controls.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_config.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex config is the settings layer that makes repeated choices durable. It should encode defaults for how Codex operates in a user or project context without relying on memory or repeated prompt boilerplate.

### Why it matters

It matters because defaults quietly control risk. A safe default reduces repeated decisions; an overbroad default silently makes every future task more dangerous.

### What good looks like

Good config separates prototype speed from production caution, scopes project settings to trusted projects, and keeps risky overrides explicit.

### What bad looks like

Bad config uses one permissive global setup for every repo, including repositories with production credentials, sensitive data, or deployment paths.

### Minimal example

If a production repo needs stricter review, define a conservative default posture and use a separate explicitly named risky profile only for isolated prototypes.

### Best-fit cases

- repeatable local Codex defaults
- project-specific permission posture
- separating prototype and production behavior
- shared team expectations for local clients

### Not-fit cases

- hiding risky permissions
- one global full-access habit
- untrusted project overrides
- memorizing volatile keys instead of checking docs

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium: requires understanding project risk, current config layers, trust posture, and which defaults should persist |
| Maintenance effort | medium: defaults need review when project phase, permissions, models, tools, or team norms change |
| Debugging effort | medium: failures may come from precedence, stale profiles, untrusted project layers, or conflicting local defaults |
| Lock-in risk | moderate: config is first-party Codex behavior even when the underlying safety principles are portable |
| Hidden cost risk | high: permissive defaults can cause repeated broad access, unexpected tool use, or expensive recovery work |

### Checklist

- choose this customization/control surface only when the task repeats or the risk boundary matters
- write the intended scope, allowed actions, and forbidden zones before using it
- keep volatile product mechanics out of stable repo guidance unless source-checked
- require evidence before accepting any change that uses this surface
- review official OpenAI docs before relying on current setup behavior

<!-- VCB:END_SECTION id=tool.codex_config.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_config.ai_coach -->
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
Inspect current Codex configuration posture conceptually. Recommend the smallest durable default change that reduces repeated friction without broadening permissions, and list what must be verified against official docs before editing config.
```

### Red flags

- the human wants a durable control layer before the workflow is proven
- the control affects secrets, auth, production, external tools, or recurring mutation
- the user cannot name the owner, rollback plan, or review evidence
- the instruction is vague enough that Codex cannot verify compliance

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, config keys, hook event names, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_config.ai_coach -->

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

- `vcb.shortcut.default_config_forever`
- `vcb.shortcut.broad_agent_permissions`
- `vcb.shortcut.full_access_automation`
- `vcb.shortcut.unattended_mutation`

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

- stale profiles
- permission drift
- hard-to-debug precedence
- unsafe inherited defaults

## Stable Core

- Defaults are policy; set them by risk class, not convenience.
- Project configuration should be trusted deliberately.
- Profiles are useful only when humans know which risk posture they selected.

## Volatile Surface

- config file locations, precedence, exact keys, profile mechanics, sandbox and approval setting names, project-trust behavior, and managed-configuration behavior

Exact prices, plan packaging, usage-credit quantities, feature availability, command flags, config keys, hook event names, model menus, context limits, UI labels, setup mechanics, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI replaces Codex config files/profiles with another documented configuration system or changes precedence materially.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.config_basic` — official/synthesis source anchor for this tool card.
- `openai.codex.config_reference` — official/synthesis source anchor for this tool card.
- `openai.codex.config_advanced` — official/synthesis source anchor for this tool card.
- `openai.codex.agent_approvals_security` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex_cli`
- `tool.codex_ide_extension`
- `tool.codex_mcp`
- `tool.codex_hooks`
- `vcb.codex.config`
- `vcb.constraints.operating_mode`
- `vcb.shortcut.default_config_forever`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_config -->
