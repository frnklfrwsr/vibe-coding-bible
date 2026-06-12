<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.context_dumping version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
last_reviewed: '2026-06-09'
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
  shortcut harm reduction
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
id: vcb.shortcut.context_dumping
title: Context Dumping
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- prompting
- long threads
- Codex Cloud
- subagents
- MCP context
- debugging
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- context
- prompting
- usage_burn
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: HIGH_RISK_SHORTCUT
  security_sensitive: DO_NOT_DO_IN_PRODUCTION
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: true
  requires_expertise_if_data_migration: false
minimum_guardrails:
- curated context packet
- stale-context labels
- task-specific goal
- missing-info questions
- thread reset when context rots
shortcut_profiles:
- vcb.shortcut.context_dumping
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls
  than prototypes
likely_to_change:
- context-window behavior
- Codex UI attachment mechanisms
- subagent/context-compaction features
- model-specific sensitivity to stale context
obsolete_when:
- agents can reliably separate relevant, stale, adversarial, and contradictory context
  without human curation
related_topics:
- vcb.prompting.context_management
- vcb.prompting.four_part_prompt
- vcb.failure.context_pollution
- vcb.constraints.usage_burn
- vcb.constraints.scope_budget
- vcb.codex.agents_md
---

# Context Dumping

> Summary:
> Context dumping is pasting or attaching excessive, stale, contradictory, or irrelevant information instead of giving Codex a curated task packet.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.context_dumping.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut feels safe because “more context” seems better. In practice, dumping everything can bury the important facts, increase usage burn, and steer Codex toward stale assumptions.

### Why it matters

Codex needs the right context, not maximum context. Noisy context creates hidden instructions, outdated goals, irrelevant errors, and false constraints.

### What good looks like

Good: “Here are the relevant files, current error, desired behavior, constraints, forbidden areas, and done-when check.”

### What bad looks like

Bad: “Here is the entire chat, old logs, unrelated files, and every idea I had. Fix it.”

### Minimal example

For a failing login test, provide the failing test, auth handler, recent diff, and exact command output; do not paste the whole app and last week’s unrelated deployment log.

### Checklist

- name the current task
- include only relevant files/logs/errors
- mark stale context explicitly
- separate facts from guesses
- reset the thread when prior context becomes misleading

<!-- VCB:END_SECTION id=vcb.shortcut.context_dumping.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.context_dumping.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that context is an input budget and a steering system. More input can make output worse.

### Diagnostic questions

- Which context is necessary for this next decision?
- What old context may now be false?
- Are there contradictory instructions?
- Is the user compensating for a vague goal by dumping files?
- Can the agent ask for missing context instead of guessing?

### Coaching tactics

- ask for a context packet before implementation
- split logs into relevant excerpts
- request assumptions and missing-info questions
- reset stale threads after major direction changes
- use AGENTS.md for durable rules, prompts for task-specific facts

### Red flags

- entire repo pasted for one bug
- old instructions conflict with new goal
- multiple tasks in one context blob
- Codex cites irrelevant files
- retry loops get longer but not more precise

### Prompt pattern

```text
Use only this curated context packet. Identify any missing context before editing. Ignore stale or unrelated material. If the packet is insufficient, ask for the specific file, log, command, or decision you need.
```

<!-- VCB:END_SECTION id=vcb.shortcut.context_dumping.ai_coach -->

## Shortcut Reality

### Ideal practice

Use the best-practice alternative named in `SHORTCUT_REGISTER.md`, then scale the guardrails by project phase, blast radius, and recoverability.

### What people often do instead

They take the shortcut because it reduces immediate friction: fewer prompts, fewer checks, fewer approvals, less review, or a faster-looking result.

### When the shortcut may be acceptable

Acceptable for disposable prototypes, throwaway local experiments, or tightly isolated work where rollback is trivial, no real users or secrets are involved, and the output is not treated as production evidence.

### When it becomes a bad trade

Bad when the task touches production, auth, payments, data deletion, secrets, CI permissions, public documentation, dependency supply chain, or a diff too broad for available review.

### Risk profile

- Probability: medium for disciplined small tasks; high when prompts are vague, permissions are broad, or review is deferred.
- Impact: low for local throwaways; high for production, team repos, security-sensitive systems, and public releases.
- Recoverability: good before merge with a clean branch; worse after release, data migration, dependency rollout, credential exposure, or undocumented behavior change.

### Blast radius

The shortcut can spread from one fast turn into merged code, stale tests, false release notes, hidden security exposure, future debugging assumptions, and more expensive recovery work.

### Minimum guardrails

- curated context packet
- stale-context labels
- task-specific goal
- missing-info questions
- thread reset when context rots

### Recovery plan

1. Stop the current run or merge path.
2. Create or restore a Git checkpoint.
3. Ask Codex for a risk and evidence table for the shortcut taken.
4. Run the smallest relevant verification or review pass.
5. Revert, isolate, or split the work if evidence is missing.
6. Update the prompt, AGENTS.md guidance, or workflow checklist so the same shortcut has a guardrail next time.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest guardrail that can catch the likely failure before spending on retries, broad context, or recovery.

### Fastest high-usage path

High-throughput users can spend more turns, but should spend them on bounded checks, comparison, or review rather than broad unverified mutation.

### Low-attention path

Low-attention delegation is only safe when scope, permissions, and stop conditions are narrower than they would be in supervised work.

### Production-quality path

Production work requires explicit evidence, diff review, rollback planning, and refusal to treat summaries as approval.

### Prototype versus production

Prototype shortcuts can be rational when they are isolated and disposable. Production shortcuts need documented guardrails or rejection.

### Maintenance phase

Maintenance work should reduce repeated shortcut risk by encoding durable commands, review criteria, and do-not rules after the shortcut recurs.

## Stable Core

- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls than prototypes

## Volatile Surface

- context-window behavior
- Codex UI attachment mechanisms
- subagent/context-compaction features
- model-specific sensitivity to stale context

## Obsolescence Watch

This card should be revised if:

- agents can reliably separate relevant, stale, adversarial, and contradictory context without human curation

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, done-when criteria, testing, review, and permission posture.
- `openai.codex.prompting` — Official OpenAI Codex prompting guidance for focused steps, context, and task loop behavior.
- `openai.codex.subagent_concepts` — Official OpenAI Codex subagent concepts guidance for context pollution, context rot, and parallel analysis boundaries.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.prompting.context_management`
- `vcb.prompting.four_part_prompt`
- `vcb.failure.context_pollution`
- `vcb.constraints.usage_burn`
- `vcb.constraints.scope_budget`
- `vcb.codex.agents_md`

<!-- VCB:STOP_RETRIEVAL reason="context_dumping_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.context_dumping -->
