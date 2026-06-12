<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.skipping_agents_md version=0.1.0 -->
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
id: vcb.shortcut.skipping_agents_md
title: Skipping AGENTS.md
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- AGENTS.md
- repo guidance
- team conventions
- setup commands
- Codex CLI
- Codex Cloud
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- agents_md
- durable_guidance
- setup
- team_workflow
risk_level:
  prototype: LOW_RISK_SHORTCUT
  personal_tool: LOW_RISK_SHORTCUT
  internal_tool: MODERATE_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- add minimal commands after repeated mistakes
- include do-not rules for risky areas
- keep project facts in repo guidance
- confirm Codex loads the file
shortcut_profiles:
- vcb.shortcut.skipping_agents_md
durable_principles:
- durable setup and process guidance should reduce repeated friction, not become invisible risk
- persistent configuration should be conservative by default and explicit when risky
- external tools and automation outputs need provenance, scope, and verification boundaries
likely_to_change:
- AGENTS discovery rules and byte limits
- fallback instruction filenames
- Codex clients that read project guidance
- team naming conventions
obsolete_when:
- agent clients consistently infer and persist verified repo conventions without explicit guidance files
related_topics:
- vcb.codex.agents_md
- vcb.codex.config
- vcb.shortcut.overstuffing_agents_md
- vcb.shortcut.stale_agents_md
- vcb.constraints.build_vs_maintenance
---

# Skipping AGENTS.md

> Summary:
> Skipping AGENTS.md is the shortcut of repeatedly telling Codex the same project rules in prompts instead of making durable repo guidance.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skipping_agents_md.human -->
## 1. For the Human: Plain-Language Concept

### What this means

It means the project has stable conventions, commands, or danger zones, but every session starts from scratch because there is no maintained AGENTS.md guidance.

### Why it matters

Repeated prompt-only guidance is easy to forget, inconsistent across teammates, and invisible to background/cloud work that starts in a fresh context.

### What good looks like

Good: “After the second repeated setup or style mistake, add a short AGENTS.md rule and verify Codex loads it.”

### What bad looks like

Bad: “I will remember to paste our conventions every time.”

### Minimal example

If Codex keeps using npm in a pnpm repo, add a short package-manager rule to AGENTS.md instead of correcting each run manually.

### Checklist

- add only stable project rules
- include setup/test commands that are known to work
- add do-not rules for dangerous directories/services
- verify instruction loading
- keep task-specific details in prompts

<!-- VCB:END_SECTION id=vcb.shortcut.skipping_agents_md.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skipping_agents_md.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to replace the shortcut with the smallest durable control that reduces repeated setup/config/process risk without turning the workflow into bureaucracy.

### Diagnostic questions

- Is the same correction repeated across sessions?
- Would a new teammate or cloud task need this rule?
- Is the rule durable or just task-specific?
- Can the project rule be shorter?

### Coaching tactics

- promote repeated corrections into AGENTS.md
- start with minimal sections: setup, tests, style, danger zones
- ask Codex to list loaded instruction sources
- keep AGENTS.md small enough to stay trustworthy

### Red flags

- same setup correction appears in every prompt
- cloud task misses local convention
- no do-not rules for payments/auth/data
- project guidance lives only in one person’s memory

### Prompt pattern

```text
Draft a minimal AGENTS.md for this repo using only durable project facts: setup commands, test commands, style rules, and do-not zones. Exclude task-specific instructions and mark unknown commands as unverified.
```

<!-- VCB:END_SECTION id=vcb.shortcut.skipping_agents_md.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the registered best-practice alternative: durable project guidance. Keep the process artifact narrow, verified, and tied to a repeated failure or durable project rule.

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

- add minimal commands after repeated mistakes
- include do-not rules for risky areas
- keep project facts in repo guidance
- confirm Codex loads the file

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

- AGENTS discovery rules and byte limits
- fallback instruction filenames
- Codex clients that read project guidance
- team naming conventions

## Obsolescence Watch

This card should be revised if:

- agent clients consistently infer and persist verified repo conventions without explicit guidance files

## Evidence and Sources

- `openai.codex.agents_md` — Official OpenAI Codex AGENTS.md guidance for discovery, layering, overrides, and durable repo instructions.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for goal/context/constraints/done-when prompts, testing, and review.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.agents_md`
- `vcb.codex.config`
- `vcb.shortcut.overstuffing_agents_md`
- `vcb.shortcut.stale_agents_md`
- `vcb.constraints.build_vs_maintenance`


<!-- VCB:STOP_RETRIEVAL reason="skipping_agents_md_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.skipping_agents_md -->
