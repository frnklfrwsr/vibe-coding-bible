<!-- VCB:BEGIN_TOPIC id=vcb.safety.security_review version=0.1.0 -->
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
id: vcb.safety.security_review
title: Security Review Workflow for Vibe Coders
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex CLI
- Codex Cloud
- Codex Security
- Web apps
- APIs
- Pull requests
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.skipping_security_review
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.accepting_diff_without_review
- vcb.shortcut.real_secrets_in_prototype
durable_principles:
- security review follows trust boundaries and data flow
- security findings need evidence and severity
- AI security review assists but does not replace ownership
likely_to_change:
- Codex Security availability
- security-scan UI
- finding severity labels
- supported languages/frameworks
- repository integration mechanics
obsolete_when:
- software changes can be proven non-exploitable automatically before merge
related_topics:
- vcb.chapter.security_for_vibe_coders
- vcb.safety.secrets
- vcb.safety.production_red_lines
- vcb.workflow.reviewing_diffs
- vcb.codex.feature_maturity
- vcb.codex.github_review
---

> Summary:
> Security review checks whether a Codex change creates exploitable behavior, leaks data, weakens trust boundaries, or hides dangerous assumptions.

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

<!-- VCB:BEGIN_SECTION id=vcb.safety.security_review.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Security review means looking for ways the change could be abused. You are not only asking “does this work?” You are asking “what could an attacker, malicious input, confused user, or exposed credential do with this?”

### Why it matters

Vibe coding can create working features that quietly weaken authorization, leak secrets, trust untrusted input, disable validation, or expose data. Those bugs are expensive because they can damage users before anyone notices.

### The mental model

Security review is checking the locks after a renovation. The new room may look good, but the door might now open from the alley.

### What good looks like

Good: “Review this diff for authentication, authorization, untrusted input, sensitive data exposure, secrets, dependency risk, and missing negative tests. Return only evidence-backed findings with severity.”

### What bad looks like

Bad: “Make it secure” after the code is already broad, merged, and deployed.

### Minimal example

A new admin endpoint should trigger checks for who can call it, how authorization is enforced, what input is trusted, what data is returned, how errors are logged, and whether tests cover unauthorized access.

### Checklist

- identify trust boundaries and entry points
- check auth and authorization changes
- trace sensitive data and logs
- look for secrets in code, config, prompts, screenshots, and CI
- review dependencies and external calls
- require negative tests or equivalent evidence for risky paths
- label severity and evidence separately from guesses
<!-- VCB:END_SECTION id=vcb.safety.security_review.human -->

<!-- VCB:BEGIN_SECTION id=vcb.safety.security_review.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to review security by data flow, trust boundary, and exploitability rather than by generic fear.

### Diagnose the human’s current model

- What new entry point or permission was added?
- What data becomes readable, writable, logged, or exported?
- Which inputs are untrusted?
- What could a normal user now do that they should not?
- Does the finding have concrete evidence or only vibes?

### Explanation strategy

Make security review concrete. Start from assets, actors, entry points, trust boundaries, and changed code. Use Codex to enumerate risks and run targeted checks, but require human review for severity, business context, and production decisions.

### Useful metaphor

Security review is a threat model with receipts: each concern should point to code, input, permission, or data.

### Coaching tactics

- ask for threat model before patching high-risk code
- separate confirmed findings from hypotheses
- request smallest safe fixes before broad rewrites
- require negative tests for auth/authorization regressions
- escalate immediately for secrets, production data, or permission broadening

### Prompt patterns

```text
Security-review this change.
Focus on: entry points, trust boundaries, auth/authz, untrusted input, sensitive data, secrets, logging, dependencies, and missing negative tests.
For each finding, provide severity, evidence path/file/line or behavior, exploit sketch, smallest fix, and verification check. Separate confirmed facts from guesses.
```

### Red flags to call out directly

- security review happens after deployment only
- Codex claims “secure” without evidence
- auth or authorization changed without negative tests
- logs or screenshots include secrets or user data
- new dependency or external tool gets broad permissions

### Exercises

- Ask the human to draw entry point → validation → permission → data flow for one route.
- Have them convert a vague security concern into a testable finding.
- Ask them to rank three findings by exploitability and blast radius.
<!-- VCB:END_SECTION id=vcb.safety.security_review.ai_coach -->

## Shortcut Reality

### The ideal practice

Run security review before merging risky changes and use evidence-backed findings to drive small fixes.

### What users often do instead

Users rely on Codex to “make it secure” or skip security because the feature works.

### When the shortcut may be fine

A lightweight checklist may be acceptable for throwaway local prototypes with fake data, no network exposure, and no real credentials.

### When the shortcut is a bad idea

Skipping security review is a bad trade for auth, authorization, payments, user data, file uploads, webhooks, admin tools, external tools, CI credentials, dependencies, or production systems.

### Risk profile

- Probability of failure: Medium for ordinary changes; high when permissions, input handling, secrets, dependencies, or data paths change.
- Impact if it fails: Potentially severe: account compromise, data exposure, credential leakage, supply-chain risk, or unauthorized actions.
- Ease of recovery: Good before merge; poor after secrets leak, data exposure, or exploited production behavior.
- Blast radius: All users, data, systems, credentials, and downstream integrations reachable through the changed trust boundary.
- Skill needed to recover: High for subtle auth/data issues; medium for checklist-driven review of common risks.
- Hidden cost: Incident response cost, forced credential rotation, reputational damage, and long-lived vulnerable patterns.

### Minimum guardrails

- use fake data and fake credentials in prototypes
- run a focused security review on risky diffs
- require negative tests for auth-sensitive behavior
- keep findings evidence-backed
- rotate immediately if a secret was exposed

### Recovery plan

- Stop deployment or revert.
- Identify exposed assets and credentials.
- Patch the smallest confirmed issue.
- Rotate leaked secrets and invalidate affected sessions/tokens.
- Add regression checks and update review guidance.

## Budget and Constraint Notes

### Cheapest reliable path

Use a focused checklist on the specific changed trust boundary instead of broad generic scanning.

### Fastest high-usage path

High-throughput users can run Codex Security or Codex review as a first pass, then human-review high-severity findings.

### Low-attention path

Low-attention security review is not acceptable for real secrets, production data, payments, auth, or admin actions.

### Production-quality path

Production security review needs clear owner, evidence-backed findings, negative tests where feasible, secret-handling discipline, and rollback/rotation readiness.

### Prototype versus production

Prototype security can use fake data and no real credentials. Production security must assume hostile inputs and real consequences.

### Maintenance phase

In maintenance, security review should track recurring risk areas, accepted exceptions, and follow-up dates instead of treating each patch as isolated.

## Stable Core

- security follows trust boundaries
- findings need evidence
- secrets and production data change the risk class immediately

## Volatile Surface

- Codex Security feature maturity
- supported scan surfaces
- finding severity labels
- cloud/plugin setup
- security-model improvements

Review volatile details against official sources before freezing commands, UI labels, model advice, plan packaging, context limits, or feature availability.

## Obsolescence Watch

- Codex Security graduates or changes behavior
- new OWASP guidance changes common-risk categories
- repository architecture changes trust boundaries

## Evidence and Sources

- `openai.codex.security` — Official OpenAI Codex Security overview for security scanning posture.
- `openai.codex.security_plugin` — Official OpenAI Codex Security plugin guidance for reviewing change sets and fixing findings.
- `openai.codex.security_setup` — Official OpenAI Codex Security setup guidance for cloud scans and finding review.
- `openai.codex.security_threat_model` — Official OpenAI Codex Security threat-model guidance.
- `owasp.top10_web` — OWASP Top Ten web application risk reference.
- `owasp.llm_prompt_injection` — OWASP LLM prompt-injection guidance for LLM-connected applications.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable software-engineering practice, risk, and review discipline.

## Related Topics

- `vcb.chapter.security_for_vibe_coders`
- `vcb.safety.secrets`
- `vcb.safety.production_red_lines`
- `vcb.workflow.reviewing_diffs`
- `vcb.codex.github_review`
- `vcb.codex.feature_maturity`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.safety.security_review -->
