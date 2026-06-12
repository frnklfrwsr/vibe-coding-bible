<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.tool_sprawl_mcp version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI/Codex skills, MCP, plugins, hooks, best-practices,
  workflow, configuration, and security guidance; official vendor/security documentation
  where cited; VCB maintainer synthesis for tool-sprawl, skill, and process shortcut
  harm reduction
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
id: vcb.shortcut.tool_sprawl_mcp
title: MCP Tool Sprawl
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- MCP servers
- config.toml
- tool allow-lists
- OAuth/bearer-token integrations
- plugins
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- mcp
- tools
- credentials
- external_context
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- one MCP server at a time
- enabled_tools allow-list
- prompt approval for mutating tools
- disable unused servers
shortcut_profiles:
- vcb.shortcut.tool_sprawl_mcp
durable_principles:
- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed
  review
likely_to_change:
- MCP authentication options
- tool approval modes
- server instruction behavior
- plugin-provided MCP controls
obsolete_when:
- MCP tooling gains reliable permission visualization, provenance checks, and automatic
  least-privilege recommendations per task
related_topics:
- vcb.codex.mcp
- vcb.codex.config
- vcb.shortcut.unofficial_tools
- vcb.shortcut.trusting_external_tool_output
- vcb.shortcut.cloud_work_with_real_secrets
---

# MCP Tool Sprawl

> Summary:
> MCP tool sprawl is connecting too many MCP servers or enabling too many MCP tools before each server has a clear job, permission boundary, and verification path.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.tool_sprawl_mcp.human -->
## 1. For the Human: Plain-Language Concept

### What this means

MCP gives Codex access to external tools and context. The shortcut is treating every useful server as safe to connect at once.

### Why it matters

Each MCP server can add tool instructions, authentication, environment variables, network access, and tool approval choices. More servers mean more ways to call the wrong tool or trust the wrong context.

### What good looks like

Good: “Connect one MCP server for one task. Use tool allow-lists, prompt approvals for mutation, and disable the server when the task is done.”

### What bad looks like

Bad: “Connect docs, browser, issue tracker, design, logs, and repo tools all at once with broad approval modes before knowing which one the task needs.”

### Minimal example

For a docs lookup task, enable only the docs MCP search/read tools. Do not also enable issue-write, browser-click, and deployment tools.

### Checklist

- name the server’s job
- list enabled tools
- set approval mode by tool risk
- avoid real secrets for first run
- disable the server after the task if not needed

<!-- VCB:END_SECTION id=vcb.shortcut.tool_sprawl_mcp.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.tool_sprawl_mcp.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat MCP as an access boundary, not just context enrichment.

### Diagnostic questions

- Which server is necessary for this task?
- Which tools are read-only?
- Which tools can mutate state?
- What credentials or env vars does the server receive?

### Coaching tactics

- start with read-only tools
- deny or disable mutating tools until needed
- separate documentation MCP from action MCP
- require source citations for external context

### Red flags

- multiple MCP servers enabled by default
- approval mode set to approve for unfamiliar tools
- bearer tokens or OAuth scopes used in a disposable experiment
- tool output accepted without source check

### Prompt pattern

```text
Review this Codex MCP configuration. For each server, list purpose, transport, credentials, enabled tools, disabled tools, default approval mode, mutating tools, prompt-injection risk, and recommended least-privilege configuration.
```

<!-- VCB:END_SECTION id=vcb.shortcut.tool_sprawl_mcp.ai_coach -->

## Shortcut Reality

### Ideal practice

Use MCP as a deliberate bridge: one server, one purpose, least privilege, source attribution, and clear off-switch.

### What people often do instead

People connect many servers so Codex “has everything,” then lose track of what context or tool action influenced the result.

### When the shortcut may be acceptable

Acceptable for read-only local experiments with fake data, no secrets, explicit tool allow-lists, and manual approval for anything state-changing.

### When it becomes a bad trade

Bad when MCP servers touch production logs, issue trackers, browsers, design files, customer data, cloud resources, or secrets without a narrow purpose and approval boundary.

### Risk profile

- Probability: high when users discover MCP through examples and install several servers quickly.
- Impact: medium for noisy context; severe for secret exposure or wrong external mutation.
- Recoverability: medium for disabled servers; low if credentials or external systems were changed.

### Blast radius

MCP sprawl can expose data, route Codex through external instructions, and let tool output steer code without review.

### Minimum guardrails

- one MCP server at a time
- enabled_tools allow-list
- prompt approval for mutating tools
- disable unused servers

### Recovery plan

1. Disable all nonessential MCP servers.
2. Re-enable one server with allow-listed tools.
3. Rotate exposed tokens if necessary.
4. Re-run affected tasks with source citations and tool-call review.
5. Document the server’s job and removal trigger.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest durable artifact that prevents the next likely mistake. That may be a saved prompt, one disabled-by-default skill, one scoped MCP server, one report-only hook, or one short workflow note.

### Fastest high-usage path

High-throughput users should template only the workflows that repeat. Spend throughput on clear inputs, expected outputs, and review evidence rather than on broad libraries of tools, skills, hooks, or ceremonies.

### Low-attention path

Low-attention delegation needs stricter defaults: fewer enabled tools, explicit triggers, report-only or read-only behavior first, branch isolation, and a required review packet before mutation is accepted.

### Production-quality path

Production-quality work requires provenance, least privilege, maintained guidance, current setup facts, artifact-backed review, and deletion or disablement paths for unused process surfaces.

### Prototype versus production

A prototype may stay light and messy if it is disposable. Once the work becomes shared, persistent, security-sensitive, or production-bound, the shortcut needs explicit boundaries and review evidence.

### Maintenance phase

Maintenance is where tool/process shortcuts compound. Review skills, hooks, MCP servers, plugins, tool choices, and reusable workflows after stack changes, onboarding, incidents, repeated failures, and major phase transitions.

## Stable Core

- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed review

## Volatile Surface

- MCP authentication options
- tool approval modes
- server instruction behavior
- plugin-provided MCP controls

## Obsolescence Watch

This card should be revised if:

- MCP tooling gains reliable permission visualization, provenance checks, and automatic least-privilege recommendations per task

## Evidence and Sources

- `openai.codex.mcp` — Official OpenAI Codex MCP guidance for third-party tools/context, config.toml server configuration, authentication, allow/deny tools, approval modes, and plugin-provided servers.
- `openai.codex.config_basic` — Official OpenAI Codex config basics for config precedence, trusted project layers, approval/sandbox settings, and project/user config boundaries.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approval, network, and full-access risk framing.
- `owasp.llm_prompt_injection` — Official OWASP LLM prompt-injection guidance for external content/tool-output risk, source separation, least privilege, and human-in-the-loop controls.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.mcp`
- `vcb.codex.config`
- `vcb.shortcut.unofficial_tools`
- `vcb.shortcut.trusting_external_tool_output`
- `vcb.shortcut.cloud_work_with_real_secrets`


<!-- VCB:STOP_RETRIEVAL reason="tool_sprawl_mcp_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.tool_sprawl_mcp -->
