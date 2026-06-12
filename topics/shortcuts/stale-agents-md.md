<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.stale_agents_md version=0.1.0 -->
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
id: vcb.shortcut.stale_agents_md
title: Stale AGENTS.md
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- AGENTS.md
- repo guidance
- maintenance
- setup commands
- team conventions
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- agents_md
- maintenance
- stale_context
- process
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- review guidance after stack changes
- mark command verification dates
- delete superseded rules
- tie rules to owners or source files
shortcut_profiles:
- vcb.shortcut.stale_agents_md
durable_principles:
- durable setup and process guidance should reduce repeated friction, not become invisible risk
- persistent configuration should be conservative by default and explicit when risky
- external tools and automation outputs need provenance, scope, and verification boundaries
likely_to_change:
- AGENTS discovery and precedence behavior
- repository command names
- team conventions
- project structure
obsolete_when:
- project guidance can be automatically validated against current repo state and command output
related_topics:
- vcb.codex.agents_md
- vcb.shortcut.overstuffing_agents_md
- vcb.failure.context_pollution
- vcb.constraints.build_vs_maintenance
- vcb.workflow.documentation_updates
---

# Stale AGENTS.md

> Summary:
> Stale AGENTS.md is the shortcut of treating old agent instructions as trustworthy after the repo, tooling, or team process has changed.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.stale_agents_md.human -->
## 1. For the Human: Plain-Language Concept

### What this means

It means Codex follows commands, style rules, or danger-zone notes that were once true but are now wrong, incomplete, or superseded.

### Why it matters

Stale guidance is worse than missing guidance because it looks authoritative. The agent may confidently run old commands or avoid the wrong files.

### What good looks like

Good: “Review AGENTS.md when setup changes, tests move, services split, or security rules change.”

### What bad looks like

Bad: “This file has been here for months, so it must still be right.”

### Minimal example

If a repo migrates from npm to pnpm, a stale AGENTS.md that still says npm install will waste runs and can corrupt lockfiles.

### Checklist

- compare instructions with current package files and docs
- remove obsolete commands
- update verification dates
- check nested overrides
- ask Codex to report contradictions before edits

<!-- VCB:END_SECTION id=vcb.shortcut.stale_agents_md.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.stale_agents_md.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to replace the shortcut with the smallest durable control that reduces repeated setup/config/process risk without turning the workflow into bureaucracy.

### Diagnostic questions

- When was the guidance last verified?
- Did recent dependency, test, or deployment changes make commands stale?
- Are nested overrides still closer to the right code?
- Does the file cite current source files?

### Coaching tactics

- tie guidance review to maintenance phase changes
- ask for contradiction scan against repo files
- keep a small verified-command block
- delete rules with no current owner or evidence

### Red flags

- old package-manager commands
- references to deleted directories
- deprecated test scripts
- security exceptions with no date or owner

### Prompt pattern

```text
Check AGENTS.md against the current repo. Find stale commands, deleted paths, contradicted rules, and missing verification dates. Propose a minimal patch that updates or removes stale guidance before coding.
```

<!-- VCB:END_SECTION id=vcb.shortcut.stale_agents_md.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the registered best-practice alternative: regular AGENTS.md pruning and source review. Keep the process artifact narrow, verified, and tied to a repeated failure or durable project rule.

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

- review guidance after stack changes
- mark command verification dates
- delete superseded rules
- tie rules to owners or source files

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

- AGENTS discovery and precedence behavior
- repository command names
- team conventions
- project structure

## Obsolescence Watch

This card should be revised if:

- project guidance can be automatically validated against current repo state and command output

## Evidence and Sources

- `openai.codex.agents_md` — Official OpenAI Codex AGENTS.md guidance for discovery, layering, overrides, and durable repo instructions.
- `openai.codex.config_basic` — Official OpenAI Codex config basics for config precedence, trusted project layers, approvals, sandbox, profiles, and web-search caveats.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.agents_md`
- `vcb.shortcut.overstuffing_agents_md`
- `vcb.failure.context_pollution`
- `vcb.constraints.build_vs_maintenance`
- `vcb.workflow.documentation_updates`


<!-- VCB:STOP_RETRIEVAL reason="stale_agents_md_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.stale_agents_md -->
