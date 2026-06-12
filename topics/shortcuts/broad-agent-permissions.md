<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.broad_agent_permissions version=0.1.0 -->
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
id: vcb.shortcut.broad_agent_permissions
title: Broad Agent Permissions
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex CLI
- Codex App
- non-interactive Codex
- MCP tools
- browser or GUI work
- automation
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- permissions
- sandbox
- secrets
- blast_radius
risk_level:
  prototype: HIGH_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: DO_NOT_DO_IN_PRODUCTION
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: false
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- read-only first
- workspace-write before full access
- no real secrets
- disposable environment for risky repos
- human approval for side effects
shortcut_profiles:
- vcb.shortcut.broad_agent_permissions
durable_principles:
- shortcut acceptability depends on blast radius, recoverability, and evidence quality
- the minimum guardrail should move the user at least one level up the guardrail ladder
- production, secrets, persistent data, and broad permissions require stronger controls
  than prototypes
likely_to_change:
- sandbox flag names
- approval policy names
- managed configuration behavior
- Codex default permissions
obsolete_when:
- agent permissions are formally verified and cannot touch secrets, production data,
  or unsafe side effects outside declared task boundaries
related_topics:
- vcb.chapter.sandboxing_and_approvals
- vcb.codex.config
- vcb.safety.secrets
- vcb.safety.production_red_lines
- vcb.constraints.operating_mode
- vcb.constraints.recovery_budget
---

# Broad Agent Permissions

> Summary:
> Broad agent permissions means giving Codex wide filesystem, network, command, browser, or credential access before the task requires it.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.broad_agent_permissions.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “Just let the agent do whatever it needs.” It feels fast because permission prompts disappear. It is dangerous because the blast radius expands faster than your review capacity.

### Why it matters

Permissions are not only convenience settings. They define what damage is possible if the prompt, repo, dependency script, tool output, or model plan is wrong.

### What good looks like

Good: “Start read-only or workspace-write with approvals; grant one exception only when the task proves it needs it.”

### What bad looks like

Bad: “Run full access with secrets loaded because approvals are annoying.”

### Minimal example

Let Codex edit a local branch and run tests inside the workspace; do not give full filesystem/network access just to update a small component.

### Checklist

- start with the narrowest sandbox that can work
- keep secrets out of broad-access environments
- approve side-effecting commands explicitly
- use disposable containers for risky repos
- review first runs before making the mode durable

<!-- VCB:END_SECTION id=vcb.shortcut.broad_agent_permissions.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.broad_agent_permissions.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to treat permission as a blast-radius dial, not a productivity badge.

### Diagnostic questions

- What exact permission is needed?
- Can the task be read-only first?
- Are real secrets, tokens, browser sessions, or production data visible?
- Can workspace-write solve it without full access?
- What happens if the agent follows malicious repo instructions?

### Coaching tactics

- ask for a permission justification before escalation
- prefer per-command approval over blanket access
- isolate risky repos in disposable containers
- remove secrets before broad access
- log and review first full-access runs

### Red flags

- danger-full-access for unknown repos
- approval_policy never with real secrets
- install scripts before inspection
- network access plus credentials
- production console or browser session visible

### Prompt pattern

```text
Use the narrowest safe permission mode. First inspect read-only and tell me exactly which edit, command, or network permission is needed. Do not request broad access unless you state the blast radius and safer alternative.
```

<!-- VCB:END_SECTION id=vcb.shortcut.broad_agent_permissions.ai_coach -->

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

- read-only first
- workspace-write before full access
- no real secrets
- disposable environment for risky repos
- human approval for side effects

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

- sandbox flag names
- approval policy names
- managed configuration behavior
- Codex default permissions

## Obsolescence Watch

This card should be revised if:

- agent permissions are formally verified and cannot touch secrets, production data, or unsafe side effects outside declared task boundaries

## Evidence and Sources

- `openai.codex.agent_approvals_security` — Official OpenAI Codex agent approvals and security guidance for sandbox, approval, and full-access risk.
- `openai.codex.sandboxing` — Official OpenAI Codex sandboxing concept guidance for read-only, workspace-write, approval, and full-access modes.
- `openai.codex.noninteractive` — Official OpenAI Codex non-interactive guidance for codex exec, sandbox defaults, automation, and structured outputs.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.chapter.sandboxing_and_approvals`
- `vcb.codex.config`
- `vcb.safety.secrets`
- `vcb.safety.production_red_lines`
- `vcb.constraints.operating_mode`
- `vcb.constraints.recovery_budget`

<!-- VCB:STOP_RETRIEVAL reason="broad_agent_permissions_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.broad_agent_permissions -->
