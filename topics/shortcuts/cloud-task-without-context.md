<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.cloud_task_without_context version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex guidance plus VCB maintainer synthesis for risk-managed
  parallel, cloud, automation, and GUI/browser shortcut harm reduction
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
id: vcb.shortcut.cloud_task_without_context
title: Cloud Task Without Context
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex Cloud
- Codex App
- Codex Automations
- Codex CLI non-interactive mode
- Computer Use
- browser/GUI tasks
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- parallel_cloud_automation
- delegation
- automation
- browser_gui
- blast_radius
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: false
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- delegation packet
- context gap questions
- branch/base state named
- verification command named
- do-not-touch list
shortcut_profiles:
- vcb.shortcut.cloud_task_without_context
durable_principles:
- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
likely_to_change:
- cloud environment setup
- automatic dependency installation
- internet and secret handling in cloud environments
- cloud follow-up mechanics
obsolete_when:
- cloud tasks can automatically capture complete relevant local context, repo state, and verification
  requirements without oversharing secrets
related_topics:
- vcb.codex.cloud
- vcb.codex.agents_md
- vcb.prompting.context_management
- vcb.workflow.bug_repro
- vcb.shortcut.ambiguous_cloud_task
- vcb.failure.context_pollution
---

# Cloud Task Without Context

> Summary:
> Cloud Task Without Context means starting background work without the local facts, repo state, examples, constraints, and verification commands the agent needs to stay aligned.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.cloud_task_without_context.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut assumes the cloud agent sees the same situation you see. It may not know your local uncommitted changes, the exact repro, the failing command, the design example, the branch constraint, or the files you already ruled out.

### Why it matters

Cloud environments can be powerful but they are still separate execution contexts. Missing context turns delegation into guesswork and makes the final summary sound more complete than the actual evidence.

### What good looks like

Good: “Use this branch, these files, this failing command, these constraints, and these done-when checks. Do not touch the listed areas.”

### What bad looks like

Bad: “You know the app. Fix the bug in the cloud.”

### Minimal example

For a flaky checkout bug, include the route, failing steps, logs, relevant components, environment assumptions, and the smallest check to rerun.

### Checklist

- include branch/base state
- include repro or target behavior
- name relevant files and examples
- include constraints and forbidden areas
- include verification commands and evidence expectations

<!-- VCB:END_SECTION id=vcb.shortcut.cloud_task_without_context.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.cloud_task_without_context.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat cloud delegation like handing work to a teammate who starts from a clean machine and needs a packet.

### Diagnostic questions

- What local facts would be lost in the cloud?
- Are there uncommitted changes or local-only config?
- Which files are known relevant?
- What command or flow proves the result?
- What should Codex not infer?

### Coaching tactics

- ask for a delegation packet
- copy only relevant logs and examples
- state local-vs-cloud assumptions
- include environment setup caveats
- require missing-context questions before edits

### Red flags

- “just fix it in the cloud”
- bug only exists in local state but no repro is given
- task depends on a screenshot or browser state not attached
- no setup or test command
- agent is expected to infer product intent

### Prompt pattern

```text
Create a cloud task packet before starting: repo/branch, local state assumptions, relevant files, repro steps, expected versus actual behavior, constraints, forbidden areas, setup notes, verification commands, and evidence required. If any required context is missing, ask before editing.
```

<!-- VCB:END_SECTION id=vcb.shortcut.cloud_task_without_context.ai_coach -->

## Shortcut Reality

### Ideal practice

Send a bounded task packet that gives the cloud agent enough context to act without inventing scope.

### What people often do instead

They delegate with only the goal and assume the agent will rediscover all local context.

### When the shortcut may be acceptable

Acceptable for simple read-only repo exploration or tiny docs edits where missing local context cannot affect correctness.

### When it becomes a bad trade

Bad for bugs, UI flows, environment-specific behavior, migrations, config, CI, and any work tied to local state.

### Risk profile

- Probability: medium for simple cloud tasks; high when the task came from local debugging or screenshots.
- Impact: medium to high depending on environment mismatch and affected files.
- Recoverability: medium if branch-isolated; low if missing context causes broad wrong assumptions.

### Blast radius

The shortcut can produce a clean-looking branch that solves the wrong problem, ignores the real repro, or changes stable code to fit an imagined environment.

### Minimum guardrails

- delegation packet
- context gap questions
- branch/base state named
- verification command named
- do-not-touch list

### Recovery plan

1. Ask the agent to list assumptions and context it lacked.
2. Compare output to the real repro or local state.
3. Revert changes based on false assumptions.
4. Create a complete task packet and rerun only the smallest slice.
5. Update AGENTS.md or prompt templates if the same missing-context issue repeats.

## Budget and Constraint Notes

### Cheapest reliable path

Write the smallest task packet, isolation rule, and review packet requirement before launching the agent. This costs less than reconciling a broad or unsafe background result.

### Fastest high-usage path

A reusable delegation-packet template is cheaper than repeated cloud reruns caused by missing context.

### Low-attention path

Low-attention users should invest context upfront because they will not be present to correct early assumptions.

### Production-quality path

Production work requires human ownership of sensitive actions, branch/worktree isolation, least privilege, explicit evidence, and rollback or revocation planning.

### Prototype versus production

Prototype shortcuts are acceptable only when the environment, accounts, credentials, and data are fake or disposable. Production shortcuts need hard gates or refusal.

### Maintenance phase

Maintenance should remove stale automations, prune approvals, archive obsolete branches, update task templates, and encode safer defaults when the same shortcut repeats.

## Stable Core

- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
- the minimum guardrail should move the user at least one level up the guardrail ladder

## Volatile Surface

- cloud environment setup
- automatic dependency installation
- internet and secret handling in cloud environments
- cloud follow-up mechanics

## Obsolescence Watch

This card should be revised if:

- cloud tasks can automatically capture complete relevant local context, repo state, and verification requirements without oversharing secrets

## Evidence and Sources

- `openai.codex.cloud_environments` — Official OpenAI Codex cloud-environment guidance for containers, branch checkout, setup, environment variables, secrets, and task loop behavior.
- `openai.codex.cloud` — Official OpenAI Codex cloud guidance for delegated background and parallel cloud task shape.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for context, constraints, done-when criteria, planning, validation, and review.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.cloud`
- `vcb.codex.agents_md`
- `vcb.prompting.context_management`
- `vcb.workflow.bug_repro`
- `vcb.shortcut.ambiguous_cloud_task`
- `vcb.failure.context_pollution`

<!-- VCB:STOP_RETRIEVAL reason="cloud_task_without_context_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.cloud_task_without_context -->
