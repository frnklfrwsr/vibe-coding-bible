<!-- VCB:BEGIN_TOPIC id=vcb.safety.secrets version=0.1.0 -->
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
id: vcb.safety.secrets
title: Secrets and Credentials Safety Workflow
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Environment variables
- GitHub Actions
- CI
- Codex Cloud
- Codex CLI
- Codex Computer Use
- External APIs
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.real_secrets_in_prototype
- vcb.shortcut.long_lived_ci_secrets
- vcb.shortcut.overbroad_ci_permissions
- vcb.shortcut.logged_in_browser_secrets
- vcb.shortcut.cloud_work_with_real_secrets
durable_principles:
- secrets are liabilities, not convenience strings
- fake credentials are the default for prototypes
- leaked secrets require rotation, not just deletion
likely_to_change:
- secret-manager UI
- CI secret mechanics
- Codex environment configuration
- browser/session handling
- provider token formats
obsolete_when:
- real credentials can be safely exposed to arbitrary tools without leak or misuse risk
related_topics:
- vcb.chapter.security_for_vibe_coders
- vcb.safety.security_review
- vcb.safety.production_red_lines
- vcb.workflow.ci_noninteractive
- vcb.codex.computer_use
- vcb.codex.cloud
---

> Summary:
> Secrets safety means keeping API keys, tokens, passwords, cookies, session data, and production credentials out of code, prompts, logs, screenshots, and broad agent access.

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

<!-- VCB:BEGIN_SECTION id=vcb.safety.secrets.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A secret is any value that lets someone access something: API key, token, password, cookie, SSH key, database URL, session, private certificate, or production credential. Secrets safety is keeping those values out of places Codex, logs, screenshots, Git history, and strangers can see.

### Why it matters

A leaked secret is not just embarrassing. It may let someone spend money, read data, write to production, impersonate users, or compromise infrastructure. Deleting the line from code does not invalidate the exposed credential.

### The mental model

A secret is a key. If you copy the key into a public notebook, deleting the notebook page does not change the lock.

### What good looks like

Good: “Use fake test credentials. Read required variable names from `.env.example`. Do not print secret values. If a real secret appears, stop and tell me to rotate it.”

### What bad looks like

Bad: Pasting production API keys into a prompt, screenshot, GitHub issue, CI log, or Codex-accessible file for convenience.

### Minimal example

For a Stripe integration prototype, use test-mode keys stored in local environment variables, commit only `.env.example`, and make Codex read variable names without seeing live secrets.

### Checklist

- never commit real secrets
- use fake/test credentials for prototypes
- commit names and examples, not values
- keep CI permissions least-privilege
- avoid long-lived cloud credentials where short-lived auth exists
- do not expose logged-in browser sessions to broad GUI tasks
- rotate immediately after exposure
<!-- VCB:END_SECTION id=vcb.safety.secrets.human -->

<!-- VCB:BEGIN_SECTION id=vcb.safety.secrets.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to identify secrets early and route them through safer storage, fake values, or scoped access.

### Diagnose the human’s current model

- What credentials does this task need?
- Can the task use fake or test-mode values?
- Will Codex see the value or only the variable name?
- Could logs, screenshots, or CI output reveal it?
- What is the rotation plan if it leaks?

### Explanation strategy

Make secret handling a pre-task gate. Decide whether the task can run with fake data. If real access is required, narrow scope, avoid printing values, prefer environment variables or secret stores, and keep a rotation path ready.

### Useful metaphor

Secrets are radioactive. Distance, shielding, and short exposure matter.

### Coaching tactics

- replace real values with placeholders before sharing context
- ask Codex to inspect variable names and config shape, not values
- create `.env.example` patterns for local work
- prefer scoped tokens and short-lived credentials
- force immediate stop/rotate behavior on exposure

### Prompt patterns

```text
Before editing, identify any secrets or credentials this task might touch.
Use placeholders or test credentials only. Do not print, copy, log, commit, screenshot, or summarize secret values.
If you encounter a real secret, stop, name the location without repeating the value, and provide a rotation/removal checklist.
```

### Red flags to call out directly

- API key pasted into prompt or issue
- secret appears in Git diff, test fixture, screenshot, browser session, or CI log
- Codex asks for production credentials to debug locally
- workflow uses broad write token where read-only would work
- “we deleted it from the file” treated as sufficient after exposure

### Exercises

- Ask the human to mark secrets in a sample `.env` file.
- Have them convert real config into `.env.example` safely.
- Practice a leaked-secret response: remove, rotate, audit, and add prevention.
<!-- VCB:END_SECTION id=vcb.safety.secrets.ai_coach -->

## Shortcut Reality

### The ideal practice

Keep real secrets outside code and prompts, expose only what is necessary, and rotate on any leak.

### What users often do instead

Users paste real credentials into Codex or commit them during prototypes because it is faster.

### When the shortcut may be fine

Using dummy secrets, test-mode keys, or throwaway local credentials may be fine when they cannot access real money, users, or production data.

### When the shortcut is a bad idea

Real production secrets in prompts, Git history, screenshots, logs, CI output, browser automation, or broad cloud tasks are bad tradeoffs.

### Risk profile

- Probability of failure: Medium to high; secrets leak through copy/paste, logs, screenshots, generated files, and CI output.
- Impact if it fails: High; a valid credential can cause data exposure, spend, account takeover, or infrastructure mutation.
- Ease of recovery: Poor if rotation is slow or exposure scope is unknown; better when tokens are scoped and short-lived.
- Blast radius: Everything reachable by the credential and any downstream systems trusting it.
- Skill needed to recover: Medium for prevention; high for incident response when production credentials or user data are involved.
- Hidden cost: Forced rotation, audit work, billing abuse, incident response, and trust damage.

### Minimum guardrails

- use fake/test credentials by default
- commit `.env.example`, not `.env`
- scope CI permissions narrowly
- avoid logging secret values
- use short-lived or OIDC-based auth where available
- rotate immediately on exposure

### Recovery plan

- Stop sharing the value.
- Revoke or rotate the credential.
- Search Git history, logs, CI output, and screenshots for exposure.
- Audit access during the exposure window.
- Add prevention: ignore file, secret scanner, scoped token, or prompt rule.

## Budget and Constraint Notes

### Cheapest reliable path

Use fake data, local placeholders, and `.env.example` so Codex can work without real values.

### Fastest high-usage path

High-throughput users should standardize secret-handling instructions in AGENTS.md and CI templates.

### Low-attention path

Low-attention tasks must not receive real secrets or logged-in production sessions.

### Production-quality path

Production work requires scoped credentials, secret storage, audited access, no value exposure, and fast rotation capability.

### Prototype versus production

Prototype with fake or test-mode credentials. Production credentials need policy, storage, audit, and recovery.

### Maintenance phase

In maintenance, budget for rotation, audit, and secret-removal cleanup; the cost of a leaked credential grows the longer it lives.

## Stable Core

- secrets should not be committed or pasted
- exposure requires rotation
- least privilege reduces blast radius

## Volatile Surface

- CI secret UI
- provider token formats
- Codex environment-secret behavior
- OIDC setup flows
- secret-scanning coverage

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- GitHub secret-management behavior changes
- OpenAI Codex environment handling changes
- provider rotates to short-lived auth defaults

## Evidence and Sources

- `github.docs.actions_secrets` — Official GitHub Actions guidance for using secrets.
- `github.docs.actions_secure_use` — Official GitHub Actions secure-use reference.
- `github.docs.actions_oidc` — Official GitHub Actions OIDC guidance for avoiding long-lived cloud credentials.
- `openai.codex.agent_approvals_security` — Official OpenAI Codex guidance for approvals, access, and safety posture.
- `owasp.secrets_management` — OWASP Secrets Management Cheat Sheet guidance.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.security_for_vibe_coders`
- `vcb.safety.security_review`
- `vcb.safety.production_red_lines`
- `vcb.workflow.ci_noninteractive`
- `vcb.codex.computer_use`
- `vcb.codex.cloud`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.safety.secrets -->
