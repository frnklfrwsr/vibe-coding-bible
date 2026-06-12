<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.skipping_setup version=0.1.0 -->
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
id: vcb.shortcut.skipping_setup
title: Skipping Setup
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex CLI
- Codex IDE
- Codex Cloud
- new repositories
- onboarding
- setup commands
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- setup
- configuration
- onboarding
- verification
risk_level:
  prototype: LOW_RISK_SHORTCUT
  personal_tool: LOW_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- read setup docs before edits
- identify install/dev/test commands
- run one smallest setup verification
- record missing setup facts
shortcut_profiles:
- vcb.shortcut.skipping_setup
durable_principles:
- durable setup and process guidance should reduce repeated friction, not become invisible risk
- persistent configuration should be conservative by default and explicit when risky
- external tools and automation outputs need provenance, scope, and verification boundaries
likely_to_change:
- current Codex setup UI and command helpers
- project package-manager conventions
- cloud environment setup behavior
- local service availability
obsolete_when:
- Codex reliably infers, verifies, and records project setup without human review
related_topics:
- vcb.codex.config
- vcb.codex.agents_md
- vcb.workflow.unknown_codebase
- vcb.constraints.scope_budget
- vcb.failure.done_claim_without_evidence
---

# Skipping Setup

> Summary:
> Skipping setup is the shortcut of asking Codex to edit before either of you know how the project installs, runs, tests, or builds.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skipping_setup.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Skipping setup means you jump straight to implementation in a repo whose install, run, test, build, environment, or service dependencies are still unknown.

### Why it matters

The first failure is usually not the code change. It is the wrong command, missing env var, wrong package manager, stale local service, or a test suite that was never available to the agent.

### What good looks like

Good: “Before editing, identify setup commands, package manager, test command, required services, and the smallest verification we can run.”

### What bad looks like

Bad: “Just change the feature. We will figure out how to run it later.”

### Minimal example

In a new web repo, first ask for package manager, start command, test command, and one smoke check before asking Codex to change routes or components.

### Checklist

- find install/start/test/build commands
- identify required environment variables without exposing values
- ask what cannot be run locally or in cloud
- run one cheap setup or smoke check
- save durable setup notes only after they are confirmed

<!-- VCB:END_SECTION id=vcb.shortcut.skipping_setup.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.skipping_setup.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to replace the shortcut with the smallest durable control that reduces repeated setup/config/process risk without turning the workflow into bureaucracy.

### Diagnostic questions

- Has Codex identified the project manager, setup commands, and verification commands?
- Is the user editing because setup feels boring?
- Can the task be done in read-only map mode first?
- What setup fact would make the proposed patch invalid?

### Coaching tactics

- turn “just code it” into a two-step setup map then patch
- require one command/output or an explicit not-run reason
- separate missing setup from code failure
- write durable setup guidance only after confirmation

### Red flags

- Codex edits before identifying how to run the project
- unknown package manager or lockfile ignored
- real env vars requested just to inspect setup
- setup failure treated as application failure

### Prompt pattern

```text
Map this project setup before editing. Identify package manager, install/start/test/build commands, required services, missing env vars by name only, and the smallest verification command. Do not change code yet.
```

<!-- VCB:END_SECTION id=vcb.shortcut.skipping_setup.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the registered best-practice alternative: setup inspection + durable project guidance. Keep the process artifact narrow, verified, and tied to a repeated failure or durable project rule.

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

- read setup docs before edits
- identify install/dev/test commands
- run one smallest setup verification
- record missing setup facts

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

- current Codex setup UI and command helpers
- project package-manager conventions
- cloud environment setup behavior
- local service availability

## Obsolescence Watch

This card should be revised if:

- Codex reliably infers, verifies, and records project setup without human review

## Evidence and Sources

- `openai.codex.config_basic` — Official OpenAI Codex config basics for config precedence, trusted project layers, approvals, sandbox, profiles, and web-search caveats.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for goal/context/constraints/done-when prompts, testing, and review.
- `openai.codex.workflows` — Official OpenAI Codex workflow guidance for context, definition of done, reproduction, and verification loops.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.config`
- `vcb.codex.agents_md`
- `vcb.workflow.unknown_codebase`
- `vcb.constraints.scope_budget`
- `vcb.failure.done_claim_without_evidence`


<!-- VCB:STOP_RETRIEVAL reason="skipping_setup_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.skipping_setup -->
