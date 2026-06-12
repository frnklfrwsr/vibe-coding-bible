<!-- VCB:BEGIN_TOPIC id=vcb.concepts.environment_variable version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
review_cadence: annual
audiences:
- human
- ai_coach
applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- Human software work
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
- emergency_hotfix
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.concepts.environment_variable
title: Environment Variable
type: concept
next_review_due: '2027-06-09'
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: concept definition anchored to official/vendor/expert sources; Codex-specific
  risk guidance is maintainer synthesis
stability:
  principle: CORE_ENGINEERING
  surface: STABLE
  pricing: STABLE
shortcut_profiles:
- vcb.shortcut.real_secrets_in_prototype
- vcb.shortcut.broad_agent_permissions
durable_principles:
- configuration should be separate from code
- secrets must not be committed or pasted into prompts
- example env files should use fake values
likely_to_change:
- hosting dashboard UI
- secret-management tools
- framework env naming rules
obsolete_when:
- apps stop needing environment-specific configuration
related_topics:
- vcb.concepts.authentication
- vcb.concepts.ci
- vcb.concepts.build_step
- vcb.chapter.sandboxing_and_approvals
---

> Summary:
> An environment variable is configuration outside the code, often used for secrets, URLs, feature settings, and environment-specific behavior.

## Quick Navigation
- For the Human
- For the AI Coach
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=vcb.concepts.environment_variable.human -->
## 1. For the Human: Plain-Language Concept

### What this means

An environment variable is a value your app reads from the environment instead of hardcoding it in source code. Examples: API keys, database URLs, app mode, service endpoints, and feature toggles.

### Why it matters

Environment variables are where many secrets live. Codex with broad access can read files or logs that contain them. Putting real values in prompts, Git, screenshots, or generated code can leak them.

### The mental model

Environment variables are labels taped to the room, not written into the recipe. The same recipe can run in local, staging, or production with different labels.

### What good looks like

- real secrets are never committed
- `.env.example` uses fake placeholder values
- server-only env vars do not leak to browser bundles
- CI secrets are scoped and reviewed

### What bad looks like

- real API keys in README or prompts
- Codex logs env values
- client bundle exposes server secret
- production and local envs confused

### Minimal example

Use `DATABASE_URL=postgres://example` in `.env.example`, not a real database password. The real value belongs in a secret store or local ignored `.env` file.

### Checklist

- Use fake values in examples.
- Never paste real secrets into Codex.
- Check which env vars are client-visible.
- Keep `.env` ignored.
- Rotate anything leaked.
<!-- VCB:END_SECTION id=vcb.concepts.environment_variable.human -->

<!-- VCB:BEGIN_SECTION id=vcb.concepts.environment_variable.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Treat env vars as config/secrets and stop Codex from exposing them through code, logs, or prompts.

### Diagnose the human’s current model

- What part of the concept is the human treating as magic?
- What evidence would show this is working?
- What is the risky production version of this concept?
- Can the human name the boundary, data, or check involved?

### Explanation strategy

Start with a concrete everyday analogy, then tie it to the exact files, commands, checks, or data flow Codex is likely to touch. Keep the explanation practical and risk-scaled.

### Useful metaphors

- Use one simple metaphor, then return to the actual repo.
- Treat the concept as an operational control, not trivia.

### Coaching tactics

- Ask Codex to inspect current project conventions before editing.
- Convert the concept into a small checklist.
- Escalate when the concept touches production, secrets, data, auth, payments, or CI.

### Prompt patterns

```text
Inspect environment variable usage and list which variables are secret, client-visible, required, optional, local-only, staging, or production. Do not print real values.
```

```text
Add `.env.example` with fake placeholders only. Do not include real credentials or tokens.
```

### Red flags to call out directly

- real secrets in prompt or code
- client-prefix used for server secret
- Codex outputs env values in final report
- full-access agent sees `.env` unnecessarily

### Exercises

- Ask the human to find one real example in their repo.
- Ask them what would break if this concept were wrong.
<!-- VCB:END_SECTION id=vcb.concepts.environment_variable.ai_coach -->

## Shortcut Reality

### The ideal practice

Separate config from code and keep secrets out of Codex-visible surfaces unless explicitly safe.

### What users often do instead

Users paste real keys so the prototype works immediately.

### When the shortcut may be fine

Throwaway local demo with fake keys.

### When the shortcut is a bad idea

Production credentials, payment keys, OAuth secrets, database URLs, CI tokens, or screenshots/logs containing secrets.

### Risk profile

- Probability of failure: medium
- Impact if it fails: severe for secret leaks
- Ease of recovery: low after exposure
- Blast radius: external services, data, billing
- Skill needed to recover: credential rotation and audit
- Hidden cost: leaked secrets may be copied into logs/history

### Minimum guardrails

- Use fake values.
- Keep `.env` ignored.
- Limit agent access to secret files.
- Use secret stores for CI/production.
- Rotate if leaked.

### Recovery plan

Revoke/rotate leaked secrets, purge from Git/logs where possible, audit service access, replace examples with fake values, and add ignore/hook/check rules.

### AI coach guidance

Do not lecture first. Classify the project risk, then move the human one guardrail level up. If this touches real users, secrets, money, auth, production data, migrations, or CI credentials, be direct and require evidence before acceptance.

## Budget and Constraint Notes

### Cheapest reliable path

Use this card to clarify the concept before asking Codex to edit. Spend one short inspection or explanation pass, then make the smallest verified change.

### Fastest high-usage path

Run a plan/implementation/review loop, but keep diffs isolated and require Codex to report the concept-specific risk areas before acceptance.

### Low-attention path

Low-attention work needs stronger written constraints, not broader trust. Require a final report with files changed, checks run, known gaps, and any concept-specific risk.

### Production-quality path

Use the concept as a release gate: define the boundary, verify the important cases, review the diff, and preserve rollback/recovery options.

## Stable Core

- configuration should be separate from code
- secrets must not be committed or pasted into prompts
- example env files should use fake values

## Volatile Surface

- hosting dashboard UI
- secret-management tools
- framework env naming rules

## Obsolescence Watch

Obsolete or review this topic when:

- apps stop needing environment-specific configuration

## Evidence and Sources

- `nodejs.docs_environment_variables` — official Node.js source anchor for environment variable behavior and `.env` conventions.
- `twelve_factor.config` — source anchor for this concept.
- `github.docs.actions_secrets` — source anchor for this concept.
- `openai.codex.agent_approvals_security` — source anchor for this concept.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for Codex-specific coaching, risk, and shortcut framing.

## Related Topics

- vcb.concepts.authentication
- vcb.concepts.ci
- vcb.concepts.build_step
- vcb.chapter.sandboxing_and_approvals

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.concepts.environment_variable -->
