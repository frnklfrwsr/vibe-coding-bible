<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.overstuffing_agents_md version=0.1.0 -->
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
id: vcb.shortcut.overstuffing_agents_md
title: Overstuffing AGENTS.md
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- AGENTS.md
- repo guidance
- custom instructions
- context management
- team workflow
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- agents_md
- context_management
- maintenance
- instruction_quality
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
- keep durable rules only
- move task details into prompts
- split local overrides near specialized code
- prune contradictions
shortcut_profiles:
- vcb.shortcut.overstuffing_agents_md
durable_principles:
- durable setup and process guidance should reduce repeated friction, not become invisible risk
- persistent configuration should be conservative by default and explicit when risky
- external tools and automation outputs need provenance, scope, and verification boundaries
likely_to_change:
- AGENTS size limits and discovery behavior
- Codex customization surfaces
- team override patterns
- repo-specific instruction hierarchy
obsolete_when:
- agent instruction systems reliably rank, deduplicate, and expire persistent guidance without human maintenance
related_topics:
- vcb.codex.agents_md
- vcb.prompting.context_management
- vcb.failure.context_pollution
- vcb.shortcut.context_dumping
- vcb.shortcut.stale_agents_md
---

# Overstuffing AGENTS.md

> Summary:
> Overstuffing AGENTS.md is the shortcut of dumping every preference, task detail, and past lesson into persistent guidance until Codex cannot tell what matters.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.overstuffing_agents_md.human -->
## 1. For the Human: Plain-Language Concept

### What this means

It turns AGENTS.md from an operating manual into a junk drawer. Durable commands, stale experiments, subjective preferences, and one-off instructions compete for attention.

### Why it matters

Persistent guidance is powerful because it loads before work starts. That also means bad, stale, or contradictory guidance pollutes every run.

### What good looks like

Good: “Keep AGENTS.md short, durable, repo-specific, and split specialized rules into nested files only when needed.”

### What bad looks like

Bad: “Paste the entire architecture doc, backlog, bug list, and all previous prompts into AGENTS.md.”

### Minimal example

A payments subdirectory can have a specific override for payment tests; the repo root should not carry every team’s one-off deployment checklist.

### Checklist

- remove task-specific instructions
- remove stale commands and abandoned plans
- resolve contradictions
- keep high-priority safety rules near the top
- use nested guidance for specialized areas

<!-- VCB:END_SECTION id=vcb.shortcut.overstuffing_agents_md.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.overstuffing_agents_md.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to replace the shortcut with the smallest durable control that reduces repeated setup/config/process risk without turning the workflow into bureaucracy.

### Diagnostic questions

- Is AGENTS.md longer because the team is avoiding context curation?
- Are contradictory rules present?
- Does the file include instructions that expire after one task?
- Would a fresh agent know which rules are highest priority?

### Coaching tactics

- ask for an AGENTS.md diet pass
- separate durable rules from current-task context
- turn long sections into links or nested guidance
- require a before/after rule list with removals explained

### Red flags

- architecture dump in persistent instructions
- outdated commands retained “just in case”
- rules with no owner or source
- task ticket content embedded permanently

### Prompt pattern

```text
Audit this AGENTS.md. Classify each instruction as durable, task-specific, stale, contradictory, or too broad. Produce a concise replacement that keeps only durable repo rules and moves task context back into prompts.
```

<!-- VCB:END_SECTION id=vcb.shortcut.overstuffing_agents_md.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the registered best-practice alternative: concise maintained repo guidance. Keep the process artifact narrow, verified, and tied to a repeated failure or durable project rule.

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

- keep durable rules only
- move task details into prompts
- split local overrides near specialized code
- prune contradictions

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

- AGENTS size limits and discovery behavior
- Codex customization surfaces
- team override patterns
- repo-specific instruction hierarchy

## Obsolescence Watch

This card should be revised if:

- agent instruction systems reliably rank, deduplicate, and expire persistent guidance without human maintenance

## Evidence and Sources

- `openai.codex.agents_md` — Official OpenAI Codex AGENTS.md guidance for discovery, layering, overrides, and durable repo instructions.
- `openai.codex.customization` — Official OpenAI Codex customization guidance for AGENTS, skills, MCP, and progressive-disclosure layers.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.agents_md`
- `vcb.prompting.context_management`
- `vcb.failure.context_pollution`
- `vcb.shortcut.context_dumping`
- `vcb.shortcut.stale_agents_md`


<!-- VCB:STOP_RETRIEVAL reason="overstuffing_agents_md_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.overstuffing_agents_md -->
