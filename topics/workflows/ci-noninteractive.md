<!-- VCB:BEGIN_TOPIC id=vcb.workflow.ci_noninteractive version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-09'
audiences:
- human
- ai_coach
source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false
evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis
evidence_scope: official OpenAI/Codex and vendor documentation anchors plus VCB maintainer synthesis for risk, budget, and coaching guidance
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
id: vcb.workflow.ci_noninteractive
title: Non-Interactive Codex in CI Workflow
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex CLI
- codex exec
- GitHub Actions
- CI
- Automation
- Pull requests
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.unattended_mutation
- vcb.shortcut.overbroad_ci_permissions
- vcb.shortcut.long_lived_ci_secrets
- vcb.shortcut.full_access_automation
- vcb.shortcut.broad_agent_permissions
durable_principles:
- unattended mutation needs isolation and review
- CI credentials should be least-privilege
- automation outputs must be auditable
likely_to_change:
- codex exec options
- GitHub Action configuration
- sandbox/approval defaults
- CI permissions syntax
- model and feature availability
obsolete_when:
- unattended CI agents can safely mutate production code without permissions, review, or audit concerns
related_topics:
- vcb.chapter.ci_noninteractive_github_actions
- vcb.workflow.ci_triage
- vcb.safety.secrets
- vcb.safety.production_red_lines
- vcb.codex.cli
- vcb.codex.cloud
---

> Summary:
> Non-interactive Codex in CI can run scripted agent work, but it needs tight permissions, sandboxing, explicit outputs, and human-controlled merge gates.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.ci_noninteractive.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Non-interactive Codex means running Codex from scripts or CI instead of chatting with it. It can analyze, patch, or report inside a workflow. Because nobody is watching each step, permissions and output rules matter more.

### Why it matters

CI agents run with repository and secret access. A convenient automation can mutate code, leak credentials, post noisy comments, or bypass review if it is not constrained.

### The mental model

A non-interactive agent is a robot in the factory after hours. Give it a small station, not keys to the whole building.

### What good looks like

Good: “Run Codex in read-only triage mode. It may summarize failures and propose patches, but must not push, merge, post broadly, or expose secrets.”

### What bad looks like

Bad: A CI job with broad write token, real secrets, network access, and auto-commit behavior on arbitrary PRs.

### Minimal example

For failed-check triage, CI can let Codex read logs and produce a Markdown report artifact. A human then decides whether to apply a patch.

### Checklist

- decide read-only versus write mode explicitly
- set least-privilege GitHub token permissions
- avoid long-lived cloud secrets where possible
- restrict who or what can trigger the workflow
- capture outputs as artifacts or PR comments
- require human review before merge
- do not give full access to untrusted PR code
<!-- VCB:END_SECTION id=vcb.workflow.ci_noninteractive.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.ci_noninteractive.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human that non-interactive Codex is an automation and security-design problem, not just a prompt problem.

### Diagnose the human’s current model

- What can the CI token read or write?
- Who can trigger the workflow?
- Can untrusted code influence the prompt or environment?
- Are secrets exposed to the job?
- What artifact proves what Codex did?
- Is merge still gated by humans/checks?

### Explanation strategy

Start in read-only report mode. Add write capability only after the workflow produces useful, low-noise reports and only with narrow permissions. Treat external input and PR content as untrusted.

### Useful metaphor

Do not hand the intern a production deploy key because they are good at summaries.

### Coaching tactics

- default to report-only automation
- pin or restrict workflow actions where practical
- use least-privilege token permissions
- avoid passing secrets to jobs that process untrusted changes
- capture command output and diff artifacts
- require branch/PR review gates for mutations

### Prompt patterns

```text
Run in CI triage mode.
Allowed: read repository files, logs, and failing check output; produce a report artifact with findings and suggested patch.
Forbidden: pushing commits, posting credentials, changing workflow permissions, disabling checks, merging, or exposing secret values.
Output JSON/Markdown with evidence, confidence, and next action.
```

### Red flags to call out directly

- write token available for untrusted PRs
- workflow uses full access or danger mode casually
- long-lived cloud credentials in CI
- Codex can disable checks that guard its own output
- automation mutates protected branches without human review

### Exercises

- Ask the human to mark every permission a workflow really needs.
- Have them rewrite an auto-fix workflow into report-only mode.
- Practice identifying prompt-injection paths from PR content into CI agent behavior.
<!-- VCB:END_SECTION id=vcb.workflow.ci_noninteractive.ai_coach -->

## Shortcut Reality

### The ideal practice

Run non-interactive Codex with explicit mode, least privilege, isolated environment, auditable output, and human-controlled merge gates.

### What users often do instead

Users turn on auto-fix or broad CI automation before they have a stable triage workflow.

### When the shortcut may be fine

Report-only CI use with no secrets, no write permission, and clear artifacts is usually a reasonable early step.

### When the shortcut is a bad idea

Auto-mutation with broad permissions, long-lived secrets, untrusted PR input, or production deploy access is a bad trade.

### Risk profile

- Probability of failure: Medium to high depending on permissions, triggers, and secret exposure.
- Impact if it fails: High if the workflow can write code, leak secrets, alter CI policy, or trigger deployments.
- Ease of recovery: Good for report-only artifacts; poor for leaked secrets or pushed bad commits from privileged automation.
- Blast radius: Repository contents, CI credentials, PR comments, protected branches, deployment paths, and connected cloud accounts.
- Skill needed to recover: High; safe CI agent design requires understanding permissions, triggers, secrets, and review gates.
- Hidden cost: Noisy automation, expensive runs, weakened branch protection, credential exposure, and difficult audits.

### Minimum guardrails

- start report-only
- set minimal token permissions
- restrict triggers
- avoid real secrets for untrusted inputs
- capture artifacts and logs
- require human review for write or merge actions

### Recovery plan

- Disable the workflow.
- Rotate exposed credentials.
- Audit workflow runs and pushed commits.
- Revert unauthorized changes.
- Reintroduce automation in read-only mode with narrower permissions.

## Budget and Constraint Notes

### Cheapest reliable path

Use Codex to produce CI reports only, then manually apply fixes.

### Fastest high-usage path

High-throughput teams can graduate to controlled patch generation after report-only runs prove high signal and low noise.

### Low-attention path

Low-attention CI automation must be isolated, auditable, and blocked from merging or deploying without independent gates.

### Production-quality path

Production CI integration requires least privilege, secret discipline, protected branches, review gates, and incident rollback.

### Prototype versus production

Prototype automation can run locally or report-only. Production automation needs security review like any other privileged system.

### Maintenance phase

In maintenance, budget for workflow review, permission audits, and log inspection; unattended agents become infrastructure, not one-off scripts.

## Stable Core

- unattended agents need least privilege
- CI output must be auditable
- merge authority should stay outside the agent

## Volatile Surface

- Codex non-interactive CLI options
- Codex GitHub Action syntax
- GitHub token permission defaults
- sandbox and safety-strategy options
- CI provider behavior

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex GitHub Action changes safety defaults
- GitHub changes token or secret behavior
- OpenAI changes non-interactive mode flags or supported outputs

## Evidence and Sources

- `openai.codex.noninteractive` — Official OpenAI Codex non-interactive mode guidance.
- `openai.codex.github_action` — Official OpenAI Codex GitHub Action guidance.
- `github.docs.actions_secure_use` — Official GitHub Actions secure-use reference.
- `github.docs.github_token` — Official GitHub GITHUB_TOKEN permissions guidance.
- `github.docs.actions_secrets` — Official GitHub Actions secrets guidance.
- `github.docs.actions_oidc` — Official GitHub Actions OIDC guidance.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.ci_noninteractive_github_actions`
- `vcb.workflow.ci_triage`
- `vcb.safety.secrets`
- `vcb.safety.production_red_lines`
- `vcb.codex.cli`
- `vcb.codex.cloud`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.ci_noninteractive -->
