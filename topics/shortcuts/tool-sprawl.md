<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.tool_sprawl version=0.1.0 -->
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
id: vcb.shortcut.tool_sprawl
title: Tool Sprawl
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- tool stacks
- plugins
- MCP servers
- skills
- external developer tools
- team workflows
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- tools
- mcp
- plugins
- budget
- supply_chain
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: HIGH_RISK_SHORTCUT
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- one new tool at a time
- name owner and job
- define exit criteria
- review permissions and data flow
shortcut_profiles:
- vcb.shortcut.tool_sprawl
durable_principles:
- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed
  review
likely_to_change:
- plugin ecosystem curation
- MCP server availability
- tool authentication models
- marketplace trust signals
obsolete_when:
- Codex and tool ecosystems provide reliable provenance, least-privilege default access,
  usage/value telemetry, and automatic stale-tool retirement
related_topics:
- vcb.codex.mcp
- vcb.codex.skills
- vcb.constraints.scope_budget
- vcb.shortcut.unofficial_tools
- vcb.failure.dependency_bloat
---

# Tool Sprawl

> Summary:
> Tool sprawl is adding more AI, MCP, plugin, CI, browser, design, or monitoring tools before the current tool stack has proven a repeated need.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.tool_sprawl.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Tool sprawl is when the workflow gets more impressive-looking but less controllable. Each tool adds setup, permissions, failure modes, and maintenance.

### Why it matters

Agentic tools are not passive bookmarks. They can add instructions, external context, commands, credentials, network calls, and supply-chain dependencies.

### What good looks like

Good: “Add one tool to solve one repeated bottleneck. Document what it reads, what it can change, who owns it, and when to remove it.”

### What bad looks like

Bad: “Install five helper tools in a week, give them broad access, and then blame Codex when output becomes inconsistent.”

### Minimal example

Before adding a design MCP, docs MCP, browser MCP, and release plugin, pick the one blocking the current milestone and leave the rest disabled.

### Checklist

- state the tool’s job in one sentence
- review permissions and data sharing
- test with fake or read-only data
- measure whether it saves repeated work
- remove unused tools

<!-- VCB:END_SECTION id=vcb.shortcut.tool_sprawl.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.tool_sprawl.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that tools are liabilities until they prove repeated value. Tool count is not engineering maturity.

### Diagnostic questions

- What repeated bottleneck does this tool remove?
- What does it read, write, run, or send externally?
- What existing tool already does 80% of this?
- What is the uninstall path?

### Coaching tactics

- force a one-tool experiment window
- compare against a no-new-tool path
- require owner/source/exit path in a tool decision note
- prefer official surfaces first

### Red flags

- tool added because it is trendy
- no one can describe permissions
- tool requires secrets for first trial
- multiple overlapping tools enabled simultaneously

### Prompt pattern

```text
Evaluate this proposed tool addition. Identify the repeated bottleneck, existing alternatives, permissions, data flow, credential needs, supply-chain risk, cheapest no-new-tool path, trial success metric, owner, and removal plan.
```

<!-- VCB:END_SECTION id=vcb.shortcut.tool_sprawl.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the minimum viable tool stack. Add tools only when they reduce repeated work more than they add setup, review, permission, and maintenance cost.

### What people often do instead

People buy or install tools as a substitute for defining the next milestone and the evidence needed to finish it.

### When the shortcut may be acceptable

Acceptable in a sandbox if the tool has no real secrets, no production access, no shared repo impact, and an explicit deletion plan.

### When it becomes a bad trade

Bad when tool count hides the actual problem: unclear scope, weak tests, no acceptance criteria, or insufficient review capacity.

### Risk profile

- Probability: medium in prototypes; high when teams chase productivity tools without ownership.
- Impact: medium for wasted time; high when tools get credentials or write access.
- Recoverability: medium if tools are isolated; low if credentials/data were exposed or workflows now depend on them.

### Blast radius

Tool sprawl can affect prompts, agent actions, data exposure, CI behavior, review packets, and team norms.

### Minimum guardrails

- one new tool at a time
- name owner and job
- define exit criteria
- review permissions and data flow

### Recovery plan

1. Freeze new tool installation.
2. List enabled tools, permissions, owners, and last useful run.
3. Disable anything without current value.
4. Rotate credentials if external tools saw sensitive data.
5. Rebuild the workflow around one smallest tool path.

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

- plugin ecosystem curation
- MCP server availability
- tool authentication models
- marketplace trust signals

## Obsolescence Watch

This card should be revised if:

- Codex and tool ecosystems provide reliable provenance, least-privilege default access, usage/value telemetry, and automatic stale-tool retirement

## Evidence and Sources

- `openai.codex.mcp` — Official OpenAI Codex MCP guidance for third-party tools/context, config.toml server configuration, authentication, allow/deny tools, approval modes, and plugin-provided servers.
- `openai.codex.plugins` — Official OpenAI Codex plugin guidance for plugin bundles, skills, apps, MCP servers, installation, disabling, uninstalling, and external service policy surfaces.
- `openai.codex.skills` — Official OpenAI Codex skills guidance for SKILL.md structure, progressive disclosure, invocation, skill locations, plugin distribution, and best practices.
- `owasp.top10_2025_supply_chain` — Official OWASP supply-chain guidance for risk from third-party code, tooling, dependencies, weak change tracking, and CI/CD security failures.
- `owasp.llm_prompt_injection` — Official OWASP LLM prompt-injection guidance for external content/tool-output risk, source separation, least privilege, and human-in-the-loop controls.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.mcp`
- `vcb.codex.skills`
- `vcb.constraints.scope_budget`
- `vcb.shortcut.unofficial_tools`
- `vcb.failure.dependency_bloat`


<!-- VCB:STOP_RETRIEVAL reason="tool_sprawl_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.tool_sprawl -->
