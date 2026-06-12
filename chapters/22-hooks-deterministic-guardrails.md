<!-- VCB:BEGIN_TOPIC id=vcb.chapter.hooks_deterministic_guardrails version=0.1.0 -->
---
id: vcb.chapter.hooks_deterministic_guardrails
title: "Chapter 22 — Hooks and Deterministic Guardrails"
type: chapter
chapter_number: 22
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
- hooks
- policy scripts
- validation scripts
- deterministic guardrails

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
- vcb.shortcut.brittle_hooks
- vcb.shortcut.hook_overreach
- vcb.shortcut.ignoring_lint_typecheck

durable_principles:
- Use hooks for rules that should not rely on the model remembering.
- Hooks should be fast, deterministic, visible, and easy to disable safely.
- A hook can enforce policy, but it can also block work if it is brittle or stale.
- Hooks are guardrails, not substitutes for tests, review, or judgment.

likely_to_change:
- hook events and payloads
- hook trust/review behavior
- hook config locations
- feature flag names
- managed hook policies
- parallel hook behavior

obsolete_when:
- Codex removes hooks or replaces them with a different deterministic policy mechanism.
- Hook event schemas change enough that examples are invalid.
- Trust/review behavior changes materially.

related_topics:
- vcb.chapter.codex_config_defaults
- vcb.chapter.agents_md_operating_manual
- vcb.chapter.skills_reusable_workflows
- vcb.chapter.mcp_external_tools
- vcb.chapter.acceptance_criteria
- vcb.codex.hooks
- vcb.safety.secrets
- vcb.workflow.testing
---

> Summary:
> Hooks are deterministic scripts in the Codex lifecycle. Use them for checks that should run because policy says so, not because the model happened to remember.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.hooks_deterministic_guardrails.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A hook is a script that runs at a defined point in the Codex workflow.

Prompts and AGENTS.md ask the model to behave. Hooks make a separate program check something. That is the difference between “please do not paste secrets” and “run a scanner before accepting this prompt.”

### Why it matters

Models forget, misunderstand, or comply inconsistently. Deterministic checks are useful when the rule is important enough that “the model usually follows it” is not good enough.

Good hook candidates:

- block obvious pasted secrets,
- log sessions for team review,
- run a validation check at stop time,
- enforce command policy,
- summarize sessions into a controlled memory file,
- prevent dangerous commands in sensitive repos,
- require final-report shape.

Bad hook candidates:

- subjective taste decisions,
- slow flaky checks,
- broad “review everything” scripts,
- checks nobody understands,
- scripts that mutate code unexpectedly,
- production deploy logic without strong review.

### The mental model

Use this distinction:

```text
AGENTS.md = instruction
Skill = reusable workflow
Hook = deterministic checkpoint
Test/CI = product behavior verification
```

A hook is a guardrail at the edge of the agent loop. It can catch policy failures before or after a tool action, but it should not become a hidden second agent making vague decisions.

### What good looks like

Good hooks are:

- narrow,
- fast,
- deterministic,
- visible to the team,
- versioned,
- easy to review,
- clear about pass/fail output,
- scoped to the risk they prevent.

### What bad looks like

Bad hooks are:

- slow enough to punish every task,
- flaky enough that people ignore them,
- secretive,
- too broad,
- hard to debug,
- allowed to mutate code unexpectedly,
- used to replace tests or human review.

### Minimal examples by purpose

Do not copy exact hook event syntax without checking current official docs. The stable pattern is:

- **Before tool use:** block commands that match known dangerous patterns.
- **Before prompt submission:** scan for accidental secrets.
- **After tool use:** capture command result metadata.
- **At stop:** verify final-report shape or run a lightweight repository validator.

### Checklist

Before adding a hook:

- What exact failure does it prevent?
- Is that failure important enough to enforce deterministically?
- Can the hook run quickly?
- Is the result objective?
- Can the user understand the error message?
- Does it avoid secrets and unexpected mutation?
- Is there a safe bypass path for emergencies?

<!-- VCB:END_SECTION id=vcb.chapter.hooks_deterministic_guardrails.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.hooks_deterministic_guardrails.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that hooks are for enforceable, deterministic guardrails; they are not a place to outsource vague judgment or bury policy.

### Diagnose the human’s current model

Ask:

- “Is this rule important enough to enforce every time?”
- “Can a script determine pass/fail objectively?”
- “Would AGENTS.md be enough?”
- “Would a test or CI job be more appropriate?”
- “What happens when this hook is wrong?”
- “Can a new teammate debug it?”

### Explanation strategy

Route rules by enforcement need:

- Reminder? Use AGENTS.md.
- Repeated procedure? Use a skill.
- External tool workflow? Use MCP plus a skill.
- Must always check? Use a hook.
- Must prove app behavior? Use tests/CI.

### Useful metaphors

- **Seatbelt chime:** annoying if overused, valuable when preventing serious harm.
- **Circuit breaker:** deterministic cutoff for dangerous conditions.
- **Preflight checklist:** objective checks before takeoff, not a philosophical review.

### Coaching tactics

- Keep the first hook read-only or report-only if possible.
- Prefer warnings before hard blocks until the rule is trusted.
- Make failure messages actionable.
- Version hooks with the repo when they are project policy.
- Avoid hooks that run network-heavy or flaky checks every turn.
- Use CI for expensive checks.
- Pair hooks with documentation so users understand the rule.

### Prompt patterns

```text
Evaluate whether this rule belongs in AGENTS.md, a skill, a hook, or CI.
Rule: [rule]
For each option, include:
- enforcement strength,
- false-positive risk,
- maintenance cost,
- blast radius if wrong,
- recommended implementation.
Do not write code yet.
```

```text
Design a minimal hook for this repo.
It should be deterministic, fast, read-only, and produce an actionable error message.
Start in warn-only mode unless the risk is secrets, destructive commands, or production credentials.
```

### Red flags to call out directly

- “This is subjective; a hook will be brittle.”
- “This belongs in CI, not every Codex turn.”
- “A hidden mutating hook is dangerous.”
- “If the hook blocks normal work, people will disable it.”
- “Use a warning first unless the risk is severe.”

### Exercises

1. Pick one repeated safety failure.
2. Decide whether it needs reminder, workflow, deterministic check, or CI.
3. Write the expected pass/fail criteria.
4. Draft the failure message.
5. Run it in report-only mode before enforcing.

<!-- VCB:END_SECTION id=vcb.chapter.hooks_deterministic_guardrails.ai_coach -->

## Shortcut Reality

### The ideal practice

Use hooks for small, objective, high-value checks that should not depend on model memory.

### What users often do instead

They either skip hooks entirely and rely on prompts, or they build large brittle hooks that block normal work and become another maintenance problem.

### When the shortcut may be fine

Skipping hooks is fine when:

- the repo is a prototype,
- the task is supervised,
- risk is low and recoverable,
- CI/tests already cover the relevant behavior,
- the rule is subjective or still changing.

### When the shortcut is a bad idea

Skipping deterministic guardrails is a bad idea when:

- secrets are repeatedly pasted,
- dangerous commands are common,
- low-attention work runs in sensitive repos,
- team policy must be enforced consistently,
- failures are hard to detect after the fact.

Hook overreach is also a bad idea when the hook is slow, flaky, subjective, or mutates code unexpectedly.

### Risk profile

- Probability of failure: low for narrow hooks; high for broad subjective hooks.
- Impact if it fails: medium for blocked work; high if a bad hook gives false confidence.
- Ease of recovery: high if hooks are versioned and easy to disable; low if hidden or managed poorly.
- Blast radius: repo/team-wide when shared.
- Skill needed to recover: medium; someone must debug the script and policy.
- Hidden cost: developer friction and maintenance burden.

### Minimum guardrails

- Start with a narrow rule.
- Prefer report-only before hard-block.
- Keep hooks fast.
- Make failure messages clear.
- Do not mutate code unexpectedly.
- Version and review hooks.
- Escalate to CI for expensive checks.

### Recovery plan

1. Disable or bypass the hook through the documented safe path.
2. Capture the failing input and expected behavior.
3. Fix the hook separately from the original code task.
4. Add a regression test for the hook if feasible.
5. Re-enable in warning mode before hard-blocking again.

### AI coach guidance

Do not recommend hooks as process decoration. Recommend them only where deterministic enforcement clearly lowers risk more than it adds friction.

## Budget and Constraint Notes

### Cheapest reliable path

Use AGENTS.md and existing tests first. Add one lightweight hook only when the same preventable failure keeps recurring.

### Fastest high-usage path

Use hooks to keep high-throughput Codex sessions inside known guardrails, especially around secret scanning, command policy, final-report shape, and cheap validation.

### Low-attention path

Use stronger deterministic checks before unattended work, but keep them narrow. Low attention needs stronger isolation and clearer stops, not giant brittle automation.

### Production-quality path

Version hooks, review them like code, keep sensitive checks deterministic, log meaningful decisions, and move heavy validation to CI.

## Stable Core

- Deterministic checks are stronger than model instructions for enforceable rules.
- Hooks should be narrow, fast, visible, and maintainable.
- Hooks complement tests, CI, review, and sandboxing; they do not replace them.
- False positives create pressure to disable guardrails.
- Hidden mutating hooks are dangerous.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Hook feature flags, config locations, lifecycle events, trust behavior, event payloads, and managed policy behavior are current Codex product details. Verify official docs before publishing executable hook examples.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when:

- OpenAI changes hook event names or payload schemas.
- Hook trust/review behavior changes.
- Hooks move from Codex config to another policy mechanism.
- Managed enterprise hook behavior changes.
- Official guidance changes recommended use cases for hooks.

## Evidence and Sources

- `openai.codex.hooks` — official OpenAI Codex source for hooks, lifecycle use cases, feature behavior, and trust/review mechanics.
- `openai.codex.config_advanced` — official OpenAI Codex source for hook locations and config-layer behavior.
- `openai.codex.config_reference` — official OpenAI Codex source for exact current hook configuration reference.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: deterministic guardrails should be narrow, objective, fast, and reviewable.

No hook examples here are presented as permanent API contracts.

## Related Topics

- `vcb.chapter.codex_config_defaults`
- `vcb.chapter.agents_md_operating_manual`
- `vcb.chapter.skills_reusable_workflows`
- `vcb.chapter.mcp_external_tools`
- `vcb.chapter.acceptance_criteria`
- `vcb.codex.hooks`
- `vcb.workflow.testing`
- `vcb.safety.secrets`
- `vcb.shortcut.brittle_hooks`
- `vcb.shortcut.hook_overreach`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.hooks_deterministic_guardrails -->
