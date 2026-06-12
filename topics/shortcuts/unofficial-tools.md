<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.unofficial_tools version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex setup, configuration, customization, tool, and security guidance plus official vendor security documentation where cited; VCB maintainer synthesis for process/setup shortcut harm reduction
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
id: vcb.shortcut.unofficial_tools
title: Unofficial Tools
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- plugins
- MCP servers
- skills
- CLI extensions
- third-party tools
- setup scripts
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- tools
- plugins
- mcp
- supply_chain
- credentials
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: DO_NOT_DO_IN_PRODUCTION
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- prefer official/curated surfaces
- read-only disposable environment first
- revocable tokens only
- inspect install scripts and permissions
shortcut_profiles:
- vcb.shortcut.unofficial_tools
durable_principles:
- durable setup and process guidance should reduce repeated friction, not become invisible risk
- persistent configuration should be conservative by default and explicit when risky
- external tools and automation outputs need provenance, scope, and verification boundaries
likely_to_change:
- Codex plugin directory behavior
- MCP authentication and tool allow-listing options
- third-party package ownership
- marketplace curation and sharing models
obsolete_when:
- Codex plugin/tool ecosystems provide strong verified provenance, least-privilege defaults, and automatic risk scoring for every external tool
related_topics:
- vcb.codex.mcp
- vcb.codex.skills
- vcb.codex.config
- vcb.shortcut.adding_dependencies_fast
- vcb.failure.dependency_bloat
- vcb.safety.secrets
---

# Unofficial Tools

> Summary:
> Unofficial tools is the shortcut of installing third-party plugins, MCP servers, scripts, or wrappers before you know what they can read, write, run, or exfiltrate.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.unofficial_tools.human -->
## 1. For the Human: Plain-Language Concept

### What this means

The tool may be useful, but the shortcut is treating installation as harmless because it promises faster Codex work.

### Why it matters

External tools expand the agent’s action surface. They can add commands, network paths, OAuth scopes, data-sharing policies, and supply-chain dependencies outside the repo diff.

### What good looks like

Good: “Use official or curated tools first. If an unofficial tool is necessary, test it read-only in a disposable environment with fake or revocable credentials.”

### What bad looks like

Bad: “Install this random MCP server with my real repo and tokens because a forum said it improves context.”

### Minimal example

Before connecting an unofficial documentation MCP server, inspect the package/source, run it without secrets, and restrict enabled tools to the task-specific subset.

### Checklist

- identify source, owner, and update channel
- inspect requested scopes and install commands
- run in disposable/read-only mode first
- use fake or revocable credentials
- remove the tool if it is not used

<!-- VCB:END_SECTION id=vcb.shortcut.unofficial_tools.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.unofficial_tools.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to replace the shortcut with the smallest durable control that reduces repeated setup/config/process risk without turning the workflow into bureaucracy.

### Diagnostic questions

- Is the tool official, curated, internal, or random?
- What data can it read and what actions can it take?
- Does it require OAuth, tokens, env vars, or network access?
- Can the same task be done with existing official surfaces?

### Coaching tactics

- ask for a tool decision memo before install
- prefer one tool at a time
- require exit criteria and uninstall path
- separate tool usefulness from trustworthiness

### Red flags

- npx/curl install with no inspection
- real tokens in env for first run
- broad OAuth scopes
- tool asks for repo write access for read-only work

### Prompt pattern

```text
Evaluate this unofficial Codex tool before installation. Identify source, maintainer, install path, permissions, network access, credentials, data it can read/write, safer official alternatives, disposable test plan, and uninstall path.
```

<!-- VCB:END_SECTION id=vcb.shortcut.unofficial_tools.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the registered best-practice alternative: official surfaces. Keep the process artifact narrow, verified, and tied to a repeated failure or durable project rule.

### What people often do instead

They avoid setup/config/process work because it feels slower than asking Codex to proceed. The shortcut saves a few minutes now and often creates repeated retries, stale assumptions, or permission mistakes later.

### When the shortcut may be acceptable

Acceptable for disposable local experiments where no real credentials, production systems, shared repos, or durable guidance are involved, and where the user explicitly labels the result as unverified.

### When it becomes a bad trade

Bad when the shortcut affects production, CI, credentials, external tools, persistent repo guidance, team workflows, broad permissions, or any task that future agents will inherit as context.

### Risk profile

- Probability: medium when the repo is small and the human is supervising; high when setup is unknown, instructions are stale, or external tools are trusted without review.
- Impact: low for throwaway tasks; high for shared repos, production-adjacent work, CI, secrets, and persistent configuration.
- Recoverability: good with a clean branch and explicit notes; worse when stale guidance or permissive config quietly influences many later runs.

### Blast radius

The shortcut can spread from one run into every future Codex session through config, AGENTS.md, hooks, plugins, MCP servers, setup scripts, and copied process rules.

### Minimum guardrails

- prefer official/curated surfaces
- read-only disposable environment first
- revocable tokens only
- inspect install scripts and permissions

### Recovery plan

1. Stop the current run or tool/config change.
2. Capture the current config, guidance, hook, or tool state.
3. Restore a Git checkpoint or create a branch before edits.
4. Ask Codex for a risk table: what assumed setup/config/tool fact, what evidence, what possible stale state.
5. Replace the shortcut with the smallest durable guardrail.
6. Record what remains unverified and schedule cleanup if the artifact will persist.

## Budget and Constraint Notes

### Cheapest reliable path

Spend one short turn on setup/config/tool inspection before paying for retries. The cheapest reliable path is usually a verified command, a short AGENTS.md rule, a conservative config default, or a read-only tool check.

### Fastest high-usage path

High-throughput users should template the safe setup path: named config profiles, short guidance files, verified setup commands, and tool allow-lists. Do not spend throughput generating large process documents that nobody maintains.

### Low-attention path

Low-attention delegation requires stricter defaults than supervised work: read-only first, report-only hooks where possible, no real secrets, bounded tools, and explicit stop conditions.

### Production-quality path

Production-quality work requires current setup facts, least-privilege config, maintained AGENTS.md guidance, reviewed hooks/tools, and evidence that external tool output was verified before mutation.

### Prototype versus production

A prototype can skip durable process if it is disposable. The moment the work becomes a shared repo, team workflow, cloud task, CI path, or production candidate, the setup/config guidance must become explicit and reviewed.

### Maintenance phase

Maintenance is where this shortcut class either pays off or compounds. Review persistent guidance, config, hooks, and tools after stack changes, repeated agent mistakes, team onboarding, and production incidents.

## Stable Core

- durable setup and process guidance should reduce repeated friction, not become invisible risk
- persistent configuration should be conservative by default and explicit when risky
- external tools and automation outputs need provenance, scope, and verification boundaries

## Volatile Surface

- Codex plugin directory behavior
- MCP authentication and tool allow-listing options
- third-party package ownership
- marketplace curation and sharing models

## Obsolescence Watch

This card should be revised if:

- Codex plugin/tool ecosystems provide strong verified provenance, least-privilege defaults, and automatic risk scoring for every external tool

## Evidence and Sources

- `openai.codex.plugins` — Official OpenAI Codex plugin guidance for bundled skills, apps, MCP servers, marketplace sources, data sharing, install, disable, and uninstall behavior.
- `openai.codex.mcp` — Official OpenAI Codex MCP guidance for server types, instructions, authentication, env vars, and tool allow/deny controls.
- `openai.codex.skills` — Official OpenAI Codex skills guidance for reusable instructions, scripts, and task-specific capabilities.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `owasp.top10_2025_supply_chain` — OWASP Top 10 2025 supply-chain failure guidance for third-party code/tool/dependency risk.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.mcp`
- `vcb.codex.skills`
- `vcb.codex.config`
- `vcb.shortcut.adding_dependencies_fast`
- `vcb.failure.dependency_bloat`
- `vcb.safety.secrets`


<!-- VCB:STOP_RETRIEVAL reason="unofficial_tools_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.unofficial_tools -->
