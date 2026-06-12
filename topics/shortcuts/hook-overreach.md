<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.hook_overreach version=0.1.0 -->
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
id: vcb.shortcut.hook_overreach
title: Hook Overreach
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- hooks
- config.toml
- hooks.json
- team standards
- validation scripts
- Codex CLI
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- hooks
- automation
- guardrails
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
- start report-only
- keep hooks objective and fast
- review hook definitions before trusting
- move subjective checks to review or CI
shortcut_profiles:
- vcb.shortcut.hook_overreach
durable_principles:
- durable setup and process guidance should reduce repeated friction, not become invisible risk
- persistent configuration should be conservative by default and explicit when risky
- external tools and automation outputs need provenance, scope, and verification boundaries
likely_to_change:
- Codex hook event names and lifecycle behavior
- hook trust/review UI
- managed hook policy controls
- team hook performance
obsolete_when:
- Codex hooks become formally verified, tamper-resistant policy controls with reliable proof of coverage
related_topics:
- vcb.codex.hooks
- vcb.codex.config
- vcb.safety.security_review
- vcb.shortcut.broad_agent_permissions
- vcb.workflow.ci_noninteractive
---

# Hook Overreach

> Summary:
> Hook overreach is the shortcut of turning hooks into a giant policy engine for subjective, slow, or security-critical decisions they cannot reliably enforce.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.hook_overreach.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Hooks are useful deterministic guardrails, but overreach happens when they try to replace human review, threat modeling, CI, or product judgment.

### Why it matters

A hook that is noisy, slow, brittle, or too broad gets disabled. A hook treated as a complete security boundary creates false confidence.

### What good looks like

Good: “Use hooks for fast objective checks and reminders; use CI, review, and policy for heavier judgment.”

### What bad looks like

Bad: “Our hook says no secrets, so we no longer need review.”

### Minimal example

A PreToolUse hook can block obvious secret-looking prompt text, but it should not be the only control for real credential exposure or production deployment.

### Checklist

- define one objective rule per hook
- start in report-only mode when possible
- measure false positives
- review changed hooks before trusting
- document what the hook does not prove

<!-- VCB:END_SECTION id=vcb.shortcut.hook_overreach.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.hook_overreach.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to replace the shortcut with the smallest durable control that reduces repeated setup/config/process risk without turning the workflow into bureaucracy.

### Diagnostic questions

- Is the rule deterministic and cheap?
- Can the hook explain failures clearly?
- Would false positives make users disable it?
- Is the hook being treated as proof of safety?

### Coaching tactics

- move subjective rules to review prompts or CI
- split broad hooks into narrow checks
- require trust review for changed hooks
- add “not a complete security control” language

### Red flags

- hook calls slow external services every turn
- hook blocks broad categories with vague messages
- changed hook trusted without review
- team treats hook pass as release approval

### Prompt pattern

```text
Review these Codex hooks for overreach. For each hook, classify objective/subjective, speed, false-positive risk, bypass risk, evidence produced, and what still needs CI or human review.
```

<!-- VCB:END_SECTION id=vcb.shortcut.hook_overreach.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the registered best-practice alternative: hooks only for enforceable objective rules. Keep the process artifact narrow, verified, and tied to a repeated failure or durable project rule.

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

- start report-only
- keep hooks objective and fast
- review hook definitions before trusting
- move subjective checks to review or CI

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

- Codex hook event names and lifecycle behavior
- hook trust/review UI
- managed hook policy controls
- team hook performance

## Obsolescence Watch

This card should be revised if:

- Codex hooks become formally verified, tamper-resistant policy controls with reliable proof of coverage

## Evidence and Sources

- `openai.codex.hooks` — Official OpenAI Codex hooks guidance for lifecycle hooks, hook sources, trust review, managed hooks, and hook runtime behavior.
- `openai.codex.config_basic` — Official OpenAI Codex config basics for config precedence, trusted project layers, approvals, sandbox, profiles, and web-search caveats.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approvals, network controls, and full-access risk.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.hooks`
- `vcb.codex.config`
- `vcb.safety.security_review`
- `vcb.shortcut.broad_agent_permissions`
- `vcb.workflow.ci_noninteractive`


<!-- VCB:STOP_RETRIEVAL reason="hook_overreach_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.hook_overreach -->
