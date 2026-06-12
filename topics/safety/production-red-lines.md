<!-- VCB:BEGIN_TOPIC id=vcb.safety.production_red_lines version=0.1.0 -->
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
id: vcb.safety.production_red_lines
title: Production Red Lines for AI-Assisted Work
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Production systems
- Codex App
- Codex Cloud
- Codex CLI
- Computer Use
- CI
- GitHub
- Deployments
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.gui_on_production
- vcb.shortcut.full_access_automation
- vcb.shortcut.logged_in_production_gui
- vcb.shortcut.production_console_computer_use
- vcb.shortcut.unattended_mutation
- vcb.shortcut.accepting_diff_without_review
durable_principles:
- production work needs explicit gates
- real users, real data, real money, and real credentials change the rules
- recovery planning is part of doing the work
likely_to_change:
- deployment platform controls
- Codex approval modes
- Computer Use capabilities
- CI enforcement mechanics
- branch protection UI
obsolete_when:
- production environments can be safely changed by AI without human risk judgment, audit, or rollback
related_topics:
- vcb.chapter.senior_engineer_checklist
- vcb.safety.security_review
- vcb.safety.secrets
- vcb.workflow.ci_noninteractive
- vcb.codex.computer_use
- vcb.concepts.rollback
---

> Summary:
> Production red lines are the hard stop conditions where Codex work must slow down, isolate, or require human approval before touching real users, money, data, credentials, or deployments.

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

<!-- VCB:BEGIN_SECTION id=vcb.safety.production_red_lines.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A production red line is a condition that changes “let Codex try it” into “stop and add controls.” Red lines include real users, production data, money movement, secrets, admin consoles, database migrations, deployments, broad permissions, and irreversible actions.

### Why it matters

The same shortcut that is harmless in a toy app can become an incident in production. Red lines prevent speed from crossing into unrecoverable damage.

### The mental model

Prototype work is a workshop. Production is a live hospital. You can experiment in the workshop; you do not experiment on patients.

### What good looks like

Good: “This touches production data and auth. Work on a branch with fake data first. Plan only until we define tests, rollback, permissions, and human approval.”

### What bad looks like

Bad: Letting Codex use a logged-in production console, full-access CLI mode, or privileged CI token to “just fix it quickly.”

### Minimal example

A database migration that deletes columns needs a red-line gate: backup, migration plan, rollback, staged deploy, tests, and human approval. Codex may draft the plan; it should not execute blindly.

### Checklist

- identify whether real users, data, money, or credentials are involved
- switch to plan-only when red lines appear
- use fake/staging data before production
- require human approval for destructive or irreversible steps
- confirm rollback or mitigation before deploy
- keep audit trail of actions and commands
- never let GUI/account automation perform sensitive production actions unattended
<!-- VCB:END_SECTION id=vcb.safety.production_red_lines.human -->

<!-- VCB:BEGIN_SECTION id=vcb.safety.production_red_lines.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to detect production risk early and change operating mode before damage is possible.

### Diagnose the human’s current model

- Is this connected to real users, money, data, credentials, or production systems?
- Can the change be reversed quickly?
- What is the blast radius if Codex is wrong?
- Who approves destructive or privileged action?
- What evidence proves the change before deploy?

### Explanation strategy

Use a red-line decision tree. When a red line is present, move Codex to plan/review mode, narrow permissions, isolate environment, require verification, and define rollback before mutation.

### Useful metaphor

A red line is not a suggestion. It is the guardrail before the cliff.

### Coaching tactics

- ask production-risk questions before accepting a task
- force plan-only for destructive or privileged actions
- replace production credentials/data with staging or fake equivalents
- require rollback path in the prompt and final report
- escalate GUI/account actions and CI write permissions immediately

### Prompt patterns

```text
Before doing anything, classify this task for production red lines: real users, production data, money, credentials, admin access, deployment, destructive migration, or irreversible action.
If any red line is present, do not mutate. Return a plan with risks, required approvals, verification, rollback, and safer staging/fake-data path.
```

### Red flags to call out directly

- Codex operating with full access on production systems
- logged-in GUI control over billing, auth, cloud, or database consoles
- real secrets or user data in prompts/screenshots/logs
- database migration without rollback or backup
- deployment or merge based only on AI summary

### Exercises

- Ask the human to classify five tasks as prototype-safe or red-line production work.
- Have them write a rollback plan before allowing any edit.
- Practice turning a “quick prod fix” into plan-only plus staged verification.
<!-- VCB:END_SECTION id=vcb.safety.production_red_lines.ai_coach -->

## Shortcut Reality

### The ideal practice

Detect production red lines before mutation, isolate work, require evidence, and keep humans responsible for approval and rollback.

### What users often do instead

Users treat production like a local prototype when the fix feels urgent.

### When the shortcut may be fine

Some lightweight Codex help is fine in production contexts when it is read-only: summarizing logs, drafting plans, explaining diffs, or writing checklists.

### When the shortcut is a bad idea

Unattended mutation, broad permissions, real secrets, logged-in production GUI actions, destructive migrations, or deployment without review are bad trades.

### Risk profile

- Probability of failure: Medium; urgency and confidence create shortcuts exactly when risk is highest.
- Impact if it fails: Severe: outage, data loss, data exposure, billing damage, account compromise, or irreversible customer impact.
- Ease of recovery: Good only with backups, rollback, feature flags, branch isolation, and audit logs; poor for leaked secrets or destructive data loss.
- Blast radius: Real users, production data, credentials, money movement, deploy pipeline, and connected third-party systems.
- Skill needed to recover: High; production recovery requires system knowledge, incident process, and authority.
- Hidden cost: Incident response, customer support, compliance exposure, trust damage, and long-term cleanup.

### Minimum guardrails

- plan-only first
- use staging/fake data
- require human approval
- run targeted and release checks
- prepare rollback/rotation/backup
- keep audit trail
- avoid unattended GUI or full-access automation

### Recovery plan

- Stop the agent and freeze new changes.
- Assess blast radius and impacted assets.
- Revert or roll back if safe.
- Rotate secrets if exposed.
- Communicate incident status through the project’s process.
- Add a red-line gate to prevent recurrence.

## Budget and Constraint Notes

### Cheapest reliable path

Use Codex for read-only analysis, plan drafting, and rollback checklist creation before touching production.

### Fastest high-usage path

High-throughput teams should encode red-line gates in AGENTS.md, CI, branch protection, and review templates.

### Low-attention path

Low-attention production mutation is not acceptable. Low-attention read-only analysis may be acceptable with sanitized data.

### Production-quality path

Production work needs explicit owner, approvals, least privilege, verification, audit trail, and rollback.

### Prototype versus production

Prototype freedoms stop at production boundaries. Once real users, data, credentials, or money appear, the operating mode changes.

### Maintenance phase

In maintenance, red lines should be documented and rehearsed; controls that only live in memory fail during urgent incidents.

## Stable Core

- production changes require gates
- irreversible actions need approval and rollback planning
- read-only assistance is safer than unattended mutation

## Volatile Surface

- Codex approval modes
- Computer Use capabilities
- deployment provider controls
- branch protection UI
- CI permission syntax

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex introduces new production-safety controls
- deployment platforms change rollback or approval features
- project risk profile changes from prototype to production

## Evidence and Sources

- `openai.codex.agent_approvals_security` — Official OpenAI Codex approvals and security guidance.
- `openai.codex.cloud_internet_access` — Official OpenAI Codex cloud internet-access risk guidance.
- `openai.codex.app_computer_use` — Official OpenAI Codex Computer Use safety guidance.
- `github.docs.branch_protection` — Official GitHub branch-protection documentation.
- `github.docs.actions_secure_use` — Official GitHub Actions secure-use reference.
- `owasp.top10_web` — OWASP Top Ten web application risk reference.
- `owasp.secrets_management` — OWASP Secrets Management Cheat Sheet guidance.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.senior_engineer_checklist`
- `vcb.safety.security_review`
- `vcb.safety.secrets`
- `vcb.workflow.ci_noninteractive`
- `vcb.codex.computer_use`
- `vcb.concepts.rollback`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.safety.production_red_lines -->
