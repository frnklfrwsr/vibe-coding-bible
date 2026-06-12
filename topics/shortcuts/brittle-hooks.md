<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.brittle_hooks version=0.1.0 -->
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
id: vcb.shortcut.brittle_hooks
title: Brittle Hooks
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex hooks
- hooks.json
- config.toml
- validation scripts
- plugins
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- hooks
- automation
- guardrails
- maintenance
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: HIGH_RISK_SHORTCUT
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- keep hooks fast and deterministic
- start report-only
- pin stable paths
- review changed hooks before trust
shortcut_profiles:
- vcb.shortcut.brittle_hooks
durable_principles:
- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed
  review
likely_to_change:
- hook events and matcher behavior
- plugin-bundled hook mechanics
- managed hook policy controls
- trust-review UI
obsolete_when:
- Codex hooks provide first-class typed policy checks with reliability scoring, clear
  provenance, and automatic false-positive telemetry
related_topics:
- vcb.codex.hooks
- vcb.shortcut.hook_overreach
- vcb.workflow.ci_noninteractive
- vcb.safety.security_review
- vcb.constraints.review_budget
---

# Brittle Hooks

> Summary:
> Brittle hooks are Codex lifecycle scripts that are slow, flaky, environment-dependent, or too broad to trust as everyday guardrails.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.brittle_hooks.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Hooks are scripts that run during the Codex lifecycle. Brittle hooks fail for the wrong reasons or slow the workflow until people disable them.

### Why it matters

A guardrail that is noisy, nondeterministic, or environment-specific does not create safety. It creates bypass pressure.

### What good looks like

Good: “Use small objective hooks with stable paths, short timeouts, clear failure messages, and a trust review path when they change.”

### What bad looks like

Bad: “A hook calls a slow external service on every prompt, fails on one teammate’s machine, and blocks normal work with vague errors.”

### Minimal example

A fast hook that warns about secret-like text is useful. A hook that tries to decide product readiness from vague heuristics is brittle.

### Checklist

- one objective rule per hook
- fast local execution
- clear failure message
- stable path from repo root
- report-only before blocking

<!-- VCB:END_SECTION id=vcb.shortcut.brittle_hooks.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.brittle_hooks.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to distinguish deterministic guardrails from brittle process scripts.

### Diagnostic questions

- Does the hook check an objective condition?
- Can it run quickly on every relevant machine?
- What false positives will make people disable it?
- What happens when the hook changes?

### Coaching tactics

- move slow checks to CI or review prompts
- split broad hooks into narrow hooks
- add report-only mode before blocking
- document what the hook does not prove

### Red flags

- network call on every turn
- relative paths from unpredictable directories
- vague “policy failed” messages
- hook trusted without review after edits

### Prompt pattern

```text
Review these Codex hooks for brittleness. For each hook, assess objective rule, runtime cost, environment assumptions, false-positive risk, failure message, trust/review path, and whether it belongs in hooks, CI, or human review.
```

<!-- VCB:END_SECTION id=vcb.shortcut.brittle_hooks.ai_coach -->

## Shortcut Reality

### Ideal practice

Hooks should be boring: fast, deterministic, narrow, reviewable, and easy to disable or fix without losing the actual safety policy.

### What people often do instead

People turn hooks into a hidden automation layer because it feels safer than writing clear review rules or CI checks.

### When the shortcut may be acceptable

Acceptable for local experiments if the hook is non-blocking and the user treats failures as diagnostics, not release decisions.

### When it becomes a bad trade

Bad when hooks block production work unpredictably, hide policy logic in scripts nobody reviews, or become the only claimed security control.

### Risk profile

- Probability: medium when hooks grow from examples; high when teams keep adding rules without measuring noise.
- Impact: medium for local slowdown; high when brittle hooks cause bypasses or false security confidence.
- Recoverability: high if hooks are small and versioned; lower if many workflows rely on undocumented hook behavior.

### Blast radius

Brittle hooks can stall every Codex run or silently steer users away from useful guardrails.

### Minimum guardrails

- keep hooks fast and deterministic
- start report-only
- pin stable paths
- review changed hooks before trust

### Recovery plan

1. Temporarily disable or report-only the brittle hook.
2. Capture recent failures and false positives.
3. Move slow or subjective checks to CI/review.
4. Rewrite the hook around one objective rule.
5. Require trust review after changes.

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

- hook events and matcher behavior
- plugin-bundled hook mechanics
- managed hook policy controls
- trust-review UI

## Obsolescence Watch

This card should be revised if:

- Codex hooks provide first-class typed policy checks with reliability scoring, clear provenance, and automatic false-positive telemetry

## Evidence and Sources

- `openai.codex.hooks` — Official OpenAI Codex hooks guidance for lifecycle hooks, hook sources, trust review, plugin-bundled hooks, matchers, timeouts, and runtime behavior.
- `openai.codex.config_basic` — Official OpenAI Codex config basics for config precedence, trusted project layers, approval/sandbox settings, and project/user config boundaries.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approval, network, and full-access risk framing.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.hooks`
- `vcb.shortcut.hook_overreach`
- `vcb.workflow.ci_noninteractive`
- `vcb.safety.security_review`
- `vcb.constraints.review_budget`


<!-- VCB:STOP_RETRIEVAL reason="brittle_hooks_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.brittle_hooks -->
