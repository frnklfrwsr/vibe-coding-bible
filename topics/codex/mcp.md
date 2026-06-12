<!-- VCB:BEGIN_TOPIC id=vcb.codex.mcp version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
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
evidence_scope: official OpenAI product behavior anchors plus VCB maintainer synthesis
  for risk, workflow, and coaching guidance
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
id: vcb.codex.mcp
title: MCP for Codex
type: codex_feature
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex CLI
- Codex IDE Extension
- MCP servers
- External tools
- Developer tooling
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.tool_sprawl_mcp
- vcb.shortcut.trusting_external_tool_output
- vcb.shortcut.broad_agent_permissions
durable_principles:
- external tools should be added only when they unlock a real workflow
- external content and tool output are not automatically trusted
- least privilege applies to tools as well as files and commands
likely_to_change:
- MCP server setup methods
- authentication and OAuth details
- enabled/disabled tool configuration
- server instruction behavior
obsolete_when:
- Codex no longer supports MCP or tool connection mechanisms change materially
related_topics:
- vcb.chapter.mcp_external_tools
- vcb.codex.config
- vcb.codex.skills
- vcb.codex.hooks
- vcb.safety.prompt_injection
- vcb.chapter.tool_stack_catalog
---

> Summary:
> MCP gives Codex access to external tools and context, such as documentation, browser/devtools surfaces, Figma-like tools, or internal systems.

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

<!-- VCB:BEGIN_SECTION id=vcb.codex.mcp.human -->
## 1. For the Human: Plain-Language Concept

### What this means

MCP is a way to connect Codex to tools outside the codebase. Instead of copying information manually, you can let Codex ask an external source or operate a developer tool through a controlled interface.

### Why it matters

MCP matters because the best context is often outside the repo: design files, docs, logs, issues, or browser state. It also matters because every tool you add expands what Codex can see or do.

### The mental model

MCP is adding doors to the room Codex works in. More doors can help, but each one needs a lock, label, and reason to exist.

### What good looks like

Good use: connect one high-value read-only documentation or logging source, constrain allowed tools, and ask Codex to cite what it used.

### What bad looks like

Bad use: connect many powerful tools with broad credentials and then ask for low-attention production changes.

### Minimal example

Example: connect a docs MCP server for framework documentation so Codex can avoid stale API guesses while implementing a narrow change.

### Checklist

- Name the task and the Codex surface explicitly.
- Confirm whether the work is prototype, maintenance, production, or emergency work.
- Choose permissions and attention level before starting.
- Require a diff, report, or artifact that proves what changed.
- Review volatile details against official docs before freezing commands or UI instructions.
<!-- VCB:END_SECTION id=vcb.codex.mcp.human -->

<!-- VCB:BEGIN_SECTION id=vcb.codex.mcp.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach MCP as capability plus attack surface. Add tools only for concrete workflow value.

### Diagnose the human’s current model

- What information or action does this MCP server unlock?
- Can it be read-only first?
- What credentials does it expose?
- Can tool calls be allowlisted or approval-gated?

### Explanation strategy

Start with task/surface fit. Explain what this Codex feature is good at, what it does not prove, and which guardrails become mandatory as blast radius grows. Tie the explanation to the user’s actual repository, risk level, and attention budget.

### Useful metaphors

MCP is a keyring. A useful key opens the right door. A giant keyring on the wrong person is a security problem.

### Coaching tactics

- Ask the user what surface they are actually using before giving feature-specific advice.
- Separate stable workflow principle from volatile product mechanics.
- Convert broad requests into scoped work orders with explicit done-when criteria.
- Escalate hard for production, secrets, auth, payments, migrations, CI credentials, browser state, or unattended mutation.
- Prefer reviewable artifacts over confident summaries.

### Prompt patterns

```text
Evaluate this MCP server before adding it. Identify what workflow it enables, whether read-only access is enough, what credentials it needs, what prompt-injection risk exists, and what tool allowlist/approval policy should apply.
```

### Red flags to call out directly

- adding tools because they are cool
- tool access to production data without explicit need
- untrusted external content driving code changes
- MCP output accepted without source checking

### Exercises

1. Ask the human to choose this feature for one low-risk task and one high-risk task, then explain what guardrails change.
2. Ask the human to name which part of this feature is stable principle and which part must be rechecked against official docs.
3. Ask the human to write a final-report template for work done through this feature.
<!-- VCB:END_SECTION id=vcb.codex.mcp.ai_coach -->

## Shortcut Reality

### The ideal practice

Use MCP sparingly for high-value external context or tools, with least privilege and clear approval boundaries.

### What users often do instead

Users often wire in many tools quickly because it feels like more intelligence.

### When the shortcut may be fine

A quick MCP experiment can be fine with fake data, read-only access, and disposable credentials.

### When the shortcut is a bad idea

It is dangerous with real secrets, customer data, production admin tools, or untrusted external content that can steer Codex.

### Risk profile

- Probability of failure: Medium failure probability from noisy or malicious context
- Impact if it fails: rises sharply with production data, secrets, real users, payments, auth, CI credentials, or deployment paths.
- Ease of recovery: good only when work is branch-isolated, committed, fake-data backed, and reviewable.
- Blast radius: small for local prototypes; large for shared repos, cloud work, external tools, GUI control, and automated mutation.
- Skill needed to recover: low for small Git-backed diffs; medium/high for secrets, data, deployment, or account-state mistakes.
- Hidden cost: stale configuration, noisy automation, false confidence, usage burn, and future maintenance load.

### Minimum guardrails

- start read-only
- use least-privilege credentials
- allowlist tools where possible
- treat external content as untrusted
- review tool calls and final diff

### Recovery plan

Disable the MCP server, revoke tokens, inspect logs/tool calls, remove contaminated changes, and re-enable only the minimum tools needed.

### AI coach guidance

Do not moralize the shortcut. Name the tradeoff, reduce blast radius, improve recoverability, and require the smallest guardrail that changes the risk profile.

## Budget and Constraint Notes

### Cheapest reliable path

Use this feature for one narrow task with curated context, conservative permissions, and one relevant check. Do not spend usage exploring broad unknowns unless the task is important enough to justify it.

### Fastest high-usage path

Use this feature aggressively only with branch/worktree isolation, clear acceptance criteria, structured final reports, and independent review for risky diffs.

### Low-attention path

Low-attention work requires stronger isolation, report-only or read-only posture when possible, fake credentials, and a final report that names files changed, checks run, unresolved risks, and review needs.

### Production-quality path

Use least privilege, clear done-when criteria, Git checkpoints, tests/build/lint where relevant, diff review, source-register discipline, and a rollback plan before accepting work.

## Stable Core

- external tools should be added only when they unlock a real workflow
- external content and tool output are not automatically trusted
- least privilege applies to tools as well as files and commands

## Volatile Surface

- MCP server setup methods
- authentication and OAuth details
- enabled/disabled tool configuration
- server instruction behavior

## Obsolescence Watch

- Codex no longer supports MCP or tool connection mechanisms change materially

## Evidence and Sources

- `openai.codex.mcp` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.customization` — official source anchor for this card's current Codex feature behavior.
- `openai.codex.cloud_internet_access` — official source anchor for this card's current Codex feature behavior.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for blast radius, recoverability, workflow fit, and AI-coach intervention guidance.

## Related Topics

- `vcb.chapter.mcp_external_tools`
- `vcb.codex.config`
- `vcb.codex.skills`
- `vcb.codex.hooks`
- `vcb.safety.prompt_injection`
- `vcb.chapter.tool_stack_catalog`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.codex.mcp -->
