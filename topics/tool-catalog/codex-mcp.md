<!-- VCB:BEGIN_TOPIC id=tool.codex_mcp version=0.1.0 -->
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
id: tool.codex_mcp
title: Codex MCP
name: Codex MCP
category: codex_external_tool_context
setup_effort: 'medium to high: requires server selection, auth scope, configuration, provenance rules, and test prompts'
maintenance_effort: 'high: servers, credentials, schemas, rate limits, and instructions drift'
debugging_effort: 'high: failures may be server, auth, schema, network, prompt-injection, stale context, or Codex-routing related'
lock_in_risk: 'moderate: MCP is an ecosystem protocol, but Codex configuration and client behavior are first-party mechanics'
hidden_cost_risk: 'high: every connected server can add permission, trust, context, maintenance, and review cost'
codex_integration_value: strong when a bounded external context/tool connection removes repeated manual lookup or system switching
best_for:
- external documentation/context lookup
- bounded internal tools
- shared systems with clear auth scope
- repeatable workflows needing structured external context
not_for:
- untrusted servers
- broad account authority
- secret-heavy workflows without review
- tools whose output cannot be verified
integrates_with_codex:
- Codex CLI
- Codex IDE Extension
- Codex App
- config layers
- external systems
hidden_costs:
- credential management
- server sprawl
- tool-output verification
- prompt-injection and exfiltration review
applies_to:
- external tools
- documentation/context servers
- team systems
- Codex customization
shortcut_profiles:
- vcb.shortcut.tool_sprawl_mcp
- vcb.shortcut.unofficial_tools
- vcb.shortcut.trusting_external_tool_output
- vcb.shortcut.broad_agent_permissions
durable_principles:
- Connect the minimum external authority needed for the task.
- Treat tool output as evidence to verify, not as automatic truth.
- MCP is a trust boundary, not just a convenience layer.
likely_to_change:
- MCP configuration mechanics, authentication patterns, server types, client support, tool schemas, security defaults, and marketplace/plugin distribution
obsolete_when:
- OpenAI replaces Codex MCP support with another documented external-tool connection mechanism or materially changes the trust model.
related_topics:
- tool.codex_config
- tool.codex_skills
- vcb.codex.mcp
- vcb.shortcut.tool_sprawl_mcp
- vcb.shortcut.trusting_external_tool_output
- vcb.safety.secrets
---

# Codex MCP

> Summary:
> Codex MCP connects Codex to external tools or context servers, increasing capability and blast radius at the same time.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_mcp.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

MCP is the external-tool/context connection layer for Codex. It lets Codex access approved servers that expose tools, resources, or context outside the local prompt.

### Why it matters

It matters because external tools can improve retrieval and operations, but they also introduce auth, provenance, rate-limit, and prompt-injection risk.

### What good looks like

Good MCP use starts with one scoped server, clear instructions, least privilege, and evidence review before acting on tool output.

### What bad looks like

Bad MCP use connects many servers because they look useful, forwards broad environment access, or treats external-tool output as verified truth.

### Minimal example

For documentation lookup, attach one read-only docs server with explicit source expectations, then require Codex to cite source names and separate retrieved facts from its own inference.

### Best-fit cases

- external documentation/context lookup
- bounded internal tools
- shared systems with clear auth scope
- repeatable workflows needing structured external context

### Not-fit cases

- untrusted servers
- broad account authority
- secret-heavy workflows without review
- tools whose output cannot be verified

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium to high: requires server selection, auth scope, configuration, provenance rules, and test prompts |
| Maintenance effort | high: servers, credentials, schemas, rate limits, and instructions drift |
| Debugging effort | high: failures may be server, auth, schema, network, prompt-injection, stale context, or Codex-routing related |
| Lock-in risk | moderate: MCP is an ecosystem protocol, but Codex configuration and client behavior are first-party mechanics |
| Hidden cost risk | high: every connected server can add permission, trust, context, maintenance, and review cost |

### Checklist

- choose this customization/control surface only when the task repeats or the risk boundary matters
- write the intended scope, allowed actions, and forbidden zones before using it
- keep volatile product mechanics out of stable repo guidance unless source-checked
- require evidence before accepting any change that uses this surface
- review official OpenAI docs before relying on current setup behavior

<!-- VCB:END_SECTION id=tool.codex_mcp.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_mcp.ai_coach -->
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
Evaluate this MCP server before enabling it. State purpose, permissions, auth scope, data it can see, output verification plan, owner, exit path, and the first low-risk test task.
```

### Red flags

- the human wants a durable control layer before the workflow is proven
- the control affects secrets, auth, production, external tools, or recurring mutation
- the user cannot name the owner, rollback plan, or review evidence
- the instruction is vague enough that Codex cannot verify compliance

### Intervention rule

When the human asks for current feature availability, exact prices, plan limits, credits, model availability, UI mechanics, command flags, config keys, hook event names, or context-window numbers, route to official OpenAI sources or a dated pricing/volatile snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_mcp.ai_coach -->

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

- `vcb.shortcut.tool_sprawl_mcp`
- `vcb.shortcut.unofficial_tools`
- `vcb.shortcut.trusting_external_tool_output`
- `vcb.shortcut.broad_agent_permissions`

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

- credential management
- server sprawl
- tool-output verification
- prompt-injection and exfiltration review

## Stable Core

- Connect the minimum external authority needed for the task.
- Treat tool output as evidence to verify, not as automatic truth.
- MCP is a trust boundary, not just a convenience layer.

## Volatile Surface

- MCP configuration mechanics, authentication patterns, server types, client support, tool schemas, security defaults, and marketplace/plugin distribution

Exact prices, plan packaging, usage-credit quantities, feature availability, command flags, config keys, hook event names, model menus, context limits, UI labels, setup mechanics, and current defaults must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI replaces Codex MCP support with another documented external-tool connection mechanism or materially changes the trust model.

Review official OpenAI Codex docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.mcp` — official/synthesis source anchor for this tool card.
- `openai.codex.config_basic` — official/synthesis source anchor for this tool card.
- `openai.codex.customization` — official/synthesis source anchor for this tool card.
- `openai.codex.agent_approvals_security` — official/synthesis source anchor for this tool card.
- `vcb.synthesis.stable_engineering_practice` — official/synthesis source anchor for this tool card.

## Related Topics

- `tool.codex_config`
- `tool.codex_skills`
- `vcb.codex.mcp`
- `vcb.shortcut.tool_sprawl_mcp`
- `vcb.shortcut.trusting_external_tool_output`
- `vcb.safety.secrets`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_mcp -->
