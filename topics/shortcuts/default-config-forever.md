<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.default_config_forever version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex setup, configuration, customization, tool, and security guidance; VCB maintainer synthesis for process/setup shortcut harm reduction
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
id: vcb.shortcut.default_config_forever
title: Default Config Forever
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- config.toml
- permission profiles
- sandbox settings
- approval policy
- Codex CLI
- Codex IDE
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- configuration
- permissions
- maintenance
- operating_mode
risk_level:
  prototype: LOW_RISK_SHORTCUT
  personal_tool: LOW_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- conservative default profile
- named risky profile for explicit tasks
- quarterly config review
- record why each override exists
shortcut_profiles:
- vcb.shortcut.default_config_forever
durable_principles:
- durable setup and process guidance should reduce repeated friction, not become invisible risk
- persistent configuration should be conservative by default and explicit when risky
- external tools and automation outputs need provenance, scope, and verification boundaries
likely_to_change:
- Codex config key names and defaults
- approval-policy behavior
- sandbox/profile names
- managed configuration controls
obsolete_when:
- Codex configs become self-auditing and automatically risk-adaptive by task and project phase
related_topics:
- vcb.codex.config
- vcb.codex.feature_maturity
- vcb.constraints.operating_mode
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.full_access_automation
---

# Default Config Forever

> Summary:
> Default config forever is the shortcut of leaving Codex settings unchanged after the project, risk level, or team workflow has changed.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.default_config_forever.human -->
## 1. For the Human: Plain-Language Concept

### What this means

It means one old configuration keeps controlling every task: prototypes, production fixes, security work, and low-attention delegation all inherit the same model, sandbox, approval, and tool defaults.

### Why it matters

Config is a risk boundary. A permissive default becomes invisible, while an overly restrictive default creates friction that users bypass with one-off risky overrides.

### What good looks like

Good: “Keep the default conservative. Use named profiles for risky or high-throughput modes and review them when the project phase changes.”

### What bad looks like

Bad: “I set this once during the prototype. It is probably fine for production.”

### Minimal example

A user who needed full access for a throwaway migration should move that into a named profile, not keep it as the default for all future repo work.

### Checklist

- check current sandbox and approval defaults
- separate safe default from risky profile
- remove obsolete overrides
- document why each profile exists
- review config after prototype-to-production transition

<!-- VCB:END_SECTION id=vcb.shortcut.default_config_forever.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.default_config_forever.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to replace the shortcut with the smallest durable control that reduces repeated setup/config/process risk without turning the workflow into bureaucracy.

### Diagnostic questions

- Is the same config used for prototype and production tasks?
- Are approvals disabled because they were annoying once?
- Are risky profiles named and explicit?
- Does project-local config override the user default safely?

### Coaching tactics

- make the safe path the default path
- move exceptional permissions into named profiles
- ask for config diff before changing permissions
- schedule a maintenance review when project phase changes

### Red flags

- approval_policy never used as blanket default
- danger-full-access in routine config
- unknown project-local config trusted automatically
- old config copied into every repo

### Prompt pattern

```text
Review this Codex config for current project phase. Identify safe defaults, risky overrides, stale values, project-local rules, and named profiles needed for exceptional tasks. Do not widen permissions as a default.
```

<!-- VCB:END_SECTION id=vcb.shortcut.default_config_forever.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the registered best-practice alternative: explicit safe profiles. Keep the process artifact narrow, verified, and tied to a repeated failure or durable project rule.

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

- conservative default profile
- named risky profile for explicit tasks
- quarterly config review
- record why each override exists

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

- Codex config key names and defaults
- approval-policy behavior
- sandbox/profile names
- managed configuration controls

## Obsolescence Watch

This card should be revised if:

- Codex configs become self-auditing and automatically risk-adaptive by task and project phase

## Evidence and Sources

- `openai.codex.config_basic` — Official OpenAI Codex config basics for config precedence, trusted project layers, approvals, sandbox, profiles, and web-search caveats.
- `openai.codex.config_reference` — Official OpenAI Codex configuration reference for config.toml and requirements.toml keys.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.config`
- `vcb.codex.feature_maturity`
- `vcb.constraints.operating_mode`
- `vcb.shortcut.broad_agent_permissions`
- `vcb.shortcut.full_access_automation`


<!-- VCB:STOP_RETRIEVAL reason="default_config_forever_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.default_config_forever -->
