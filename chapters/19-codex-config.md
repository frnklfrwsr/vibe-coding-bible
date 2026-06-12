<!-- VCB:BEGIN_TOPIC id=vcb.chapter.codex_config_defaults version=0.1.0 -->
---
id: vcb.chapter.codex_config_defaults
title: "Chapter 19 — Codex Config: Making Good Defaults Automatic"
type: chapter
chapter_number: 19
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex CLI
- Codex IDE Extension
- Codex App
- configuration profiles
- sandbox defaults
- approval defaults
- MCP server configuration

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: STABLE

budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget

cost_postures:
- cheapest_reliable
- balanced
- fastest_possible
- unattended_high_throughput
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

shortcut_profiles:
- vcb.shortcut.default_config_forever
- vcb.shortcut.broad_agent_permissions

durable_principles:
- Configuration is for defaults that should apply before a prompt starts.
- Use profiles to separate risky, review-heavy, and low-friction workflows.
- Project config should not carry secrets or credential-routing policy.
- Permissions and approvals should match blast radius, not convenience.

likely_to_change:
- config file locations
- config precedence
- profile loading behavior
- exact config keys
- managed configuration behavior
- model/provider options

obsolete_when:
- Codex no longer uses TOML configuration layers.
- A new official config system replaces user/project/profile config behavior.
- Approval and sandbox defaults are no longer configured through Codex config files.

related_topics:
- vcb.chapter.agents_md_operating_manual
- vcb.chapter.sandboxing_and_approvals
- vcb.chapter.mcp_external_tools
- vcb.chapter.hooks_deterministic_guardrails
- vcb.codex.config
- vcb.safety.sandboxing_and_approvals
- vcb.shortcut.broad_agent_permissions
---

> Summary:
> Codex config is where repeated runtime choices become defaults: permissions, approval behavior, profiles, and tool wiring. Prompts say what to do; config says how Codex is allowed to operate by default.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.codex_config_defaults.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Codex config is the settings layer that controls how Codex starts before you type a task.

A prompt is for the job. Config is for the workshop setup: which bench you use, what tools are available, what doors are locked, and when the assistant must ask before doing something risky.

### Why it matters

Bad defaults create repeated risk:

- every session starts with too much access,
- every task asks the same approval questions,
- every repo inherits the wrong assumptions,
- a prototype setting leaks into a production repo,
- a local-only tool gets network or filesystem access it does not need.

Good config reduces friction without removing safety.

### The mental model

Use config for defaults, not task intent.

| Need | Put it where? |
|---|---|
| “Fix this bug” | prompt |
| “This repo uses pnpm” | AGENTS.md or project guidance |
| “Use workspace-write and ask for network” | config/profile |
| “Run this release checklist” | skill |
| “Block pasted secrets before tool use” | hook |

### Good default profiles

Most users eventually need more than one operating mode:

- **read-only review** — inspect, explain, and report without edits.
- **normal workspace** — edit project files, ask before risky commands.
- **dependency/migration caution** — stricter approval around installs, migrations, and generated scripts.
- **isolated full-access spike** — only for disposable containers, fake credentials, and no real secrets.

Do not make the risky profile the default because it is convenient once.

### Minimal example concept

Do not treat this as a permanent exact config recipe; check the current official docs before copying exact keys.

```toml
# User-level default idea
approval_policy = "on-request"
sandbox_mode = "workspace-write"

# Use stricter project or profile settings for risky repos.
```

The exact keys and allowed values are product details. The stable rule is: make the safest useful behavior the default, and use explicit profiles for exceptions.

### What good looks like

Good config:

- starts in a safe default mode,
- separates prototype and production workflows,
- keeps project rules with the project,
- avoids storing secrets,
- makes risky modes explicit,
- uses profiles instead of constantly editing one global file,
- is reviewed when official config docs change.

### What bad looks like

Bad config:

- uses one global setup for every repo,
- defaults to broad access because approvals are annoying,
- silently grants network or external-file access,
- hides project policy in one developer’s machine,
- encodes model or UI advice that has gone stale,
- relies on old keys no longer supported.

### Checklist

Before changing config:

- Is this a default or just one task’s instruction?
- Should it be user-level, project-level, or profile-specific?
- Does this setting increase filesystem, network, credential, or command risk?
- Does the repo contain real secrets or production data?
- Can another person understand why this default exists?
- Do official docs still support the exact key?

<!-- VCB:END_SECTION id=vcb.chapter.codex_config_defaults.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.codex_config_defaults.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use config for repeatable operating modes while keeping risk-sensitive behavior explicit and reviewable.

### Diagnose the human’s current model

Ask:

- “Are you changing config because this should always happen, or because this one task is annoying?”
- “Which repo should this setting apply to?”
- “What is the blast radius if Codex uses this setting in the wrong project?”
- “Do you need a new profile instead of editing the default?”
- “Does this belong in AGENTS.md, config, a skill, or a hook?”

### Explanation strategy

Separate four layers:

1. **Prompt:** task-specific intent.
2. **AGENTS.md:** repo rules and commands.
3. **Config/profile:** default runtime behavior and tool wiring.
4. **Hook:** deterministic enforcement.

Then map the user’s desired behavior to the lowest layer that solves it without over-scoping.

### Useful metaphors

- **Driving mode:** eco, sport, snow, and track modes are not moral choices; they are different defaults for different conditions.
- **Circuit breaker panel:** defaults determine what power is available before anyone starts work.
- **Tool belt:** carry what you use often, not every tool in the garage.

### Coaching tactics

- Push for read-only profiles when the user wants analysis.
- Push for project-local guidance when the rule is repo-specific.
- Push for stricter defaults when real secrets/user data/money are present.
- Warn when a convenience default would be unsafe if accidentally reused.
- Avoid hardcoding exact current keys unless you have verified official docs.

### Prompt patterns

```text
Inspect my current Codex operating assumptions.
Do not change config yet.
Recommend which settings belong in:
- user config,
- project config,
- named profiles,
- AGENTS.md,
- skills,
- hooks.
For each recommendation, include blast radius and why it belongs there.
```

```text
Create a safe profile strategy for this repo.
I need:
- read-only review,
- normal implementation,
- risky dependency/migration review.
Do not include secrets.
Flag any exact config key that must be checked against current Codex docs.
```

### Red flags to call out directly

- “You are using config to hide a risky shortcut.”
- “This belongs in project guidance, not global config.”
- “Full access should not be your default on a machine with secrets.”
- “This exact key may be stale; verify it before committing docs.”
- “A hook is safer if the rule must be enforced every time.”

### Exercises

1. List the user’s three most common Codex modes.
2. Assign each mode a profile name.
3. Identify which mode is safe as default.
4. Identify which mode requires isolation.
5. Write a short README note explaining when to use each profile.

<!-- VCB:END_SECTION id=vcb.chapter.codex_config_defaults.ai_coach -->

## Shortcut Reality

### The ideal practice

Use safe defaults, named profiles for distinct workflows, and project-local guidance for repo-specific behavior.

### What users often do instead

They keep one global config forever, loosen permissions to avoid prompts, or copy a config snippet from a tutorial without understanding the blast radius.

### When the shortcut may be fine

Using default config is fine when:

- the repo is tiny,
- the work is supervised,
- no real secrets or production data are available,
- the task is read-only or local-only,
- you are still learning what settings matter.

### When the shortcut is a bad idea

It is a bad idea when:

- broad access becomes the default,
- production repos share prototype defaults,
- network/package-install behavior is enabled without review,
- project-specific policy lives only on one developer’s machine,
- a team assumes everyone has the same local config.

### Risk profile

- Probability of failure: low to medium; higher when defaults are copied across projects.
- Impact if it fails: high if broad access meets secrets, production config, migrations, or package installs.
- Ease of recovery: medium for local edits; poor for leaked credentials or destructive commands.
- Blast radius: machine-wide for user config; repo-specific for project config; task-specific for CLI overrides.
- Skill needed to recover: medium to high when permissions or credentials are involved.
- Hidden cost: repeated approvals if too strict; hidden risk if too loose.

### Minimum guardrails

- Keep the normal default conservative.
- Use named profiles for risky modes.
- Keep project policy in repo-controlled guidance when possible.
- Do not store secrets in config.
- Check official docs before documenting exact keys.
- Use isolation before broad access.

### Recovery plan

1. Stop active Codex sessions using the bad config.
2. Review what files, commands, network calls, or package changes occurred.
3. Rotate credentials if secrets may have been exposed.
4. Restore safe defaults.
5. Add a profile or hook so the mistake is not repeated.

### AI coach guidance

Do not recommend loosening config just because the human is impatient. Recommend the narrowest setting that removes real friction without increasing blast radius beyond the task.

## Budget and Constraint Notes

### Cheapest reliable path

Use one conservative default and a small number of explicit profiles. This avoids wasting usage on repeated approvals while preventing accidental risky modes.

### Fastest high-usage path

Create task-specific profiles: implementation, review, dependency audit, migration planning, and isolated spike. Use them aggressively but keep high-risk profiles out of normal default use.

### Low-attention path

Prefer stricter approvals, read-only or workspace-limited modes, no broad network/package operations by default, and final reports that name commands run.

### Production-quality path

Document the profile strategy, align project guidance and config, review changes to config like code, and use managed/team controls where appropriate.

## Stable Core

- Defaults shape behavior before prompts start.
- The safest useful default is better than the most permissive default.
- Profiles reduce friction without making risky behavior universal.
- Project-specific rules should travel with the project when possible.
- Config cannot replace review, tests, Git checkpoints, or sandboxing.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Exact config file locations, precedence order, profile loading behavior, key names, and managed-configuration behavior are Codex product details. Verify official Codex config documentation before publishing executable config snippets.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes Codex config precedence or file locations.
- Profile behavior changes.
- New managed/team configuration mechanisms replace local config patterns.
- Sandbox or approval settings move to a different official surface.
- Model/provider configuration changes materially.

## Evidence and Sources

- `openai.codex.config_basic` — official OpenAI Codex source for user/project config layers, trust behavior, and current precedence.
- `openai.codex.config_advanced` — official OpenAI Codex source for profiles, one-off overrides, project config behavior, and hooks/config layering.
- `openai.codex.config_reference` — official OpenAI Codex reference for exact keys; treat exact keys as volatile.
- `openai.codex.sandboxing` and `openai.codex.permissions` — official OpenAI Codex anchors for sandbox and approval concepts tied to configuration.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: defaults should match blast radius and project risk.

No exact pricing, model-routing advice, or plan-specific limits are included.

## Related Topics

- `vcb.chapter.agents_md_operating_manual`
- `vcb.chapter.sandboxing_and_approvals`
- `vcb.chapter.mcp_external_tools`
- `vcb.chapter.hooks_deterministic_guardrails`
- `vcb.codex.config`
- `vcb.safety.sandboxing_and_approvals`
- `vcb.shortcut.default_config_forever`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.codex_config_defaults -->
