<!-- VCB:BEGIN_TOPIC id=vcb.chapter.security_for_vibe_coders version=0.1.0 -->
---
id: vcb.chapter.security_for_vibe_coders
title: "Chapter 25 — Security for Vibe Coders"
type: chapter
chapter_number: 25
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex Cloud
- GitHub
- security review
- web apps
- secrets
- auth
- payments
- user data
- prompt injection

source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
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
- vcb.shortcut.skipping_security_review
- vcb.shortcut.real_secrets_in_prototype
- vcb.shortcut.broad_agent_permissions
- vcb.shortcut.trusting_external_tool_output

durable_principles:
- Security risk increases when code touches real users, secrets, money, identity, permissions, files, external content, or persistent data.
- Codex can assist security review, but it cannot own security judgment without explicit threat context and evidence.
- Use fake data and isolated environments for prototype shortcuts.
- Treat external content as untrusted when connected to tools or network access.

likely_to_change:
- Codex Security product access and behavior
- security plugin/cloud feature maturity
- current OWASP category names
- threat landscape details
- browser/computer-use security affordances

obsolete_when:
- A future editor splits this chapter into topic cards for secrets, auth, authorization, uploads, injection, prompt injection, dependency security, and production red lines.
- Codex Security behavior or access changes materially.
- OWASP risk categories change enough that chapter wording needs update.

related_topics:
- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.chapter.sandboxing_and_approvals
- vcb.chapter.reviewing_codex_output
- vcb.chapter.github_pr_review_with_codex
- vcb.safety.secrets
- vcb.safety.prompt_injection
- vcb.safety.security_review
- vcb.safety.production_red_lines
---

> Summary:
> Security for vibe coders means knowing where fast AI-generated code can hurt real people, real money, real data, or real systems.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.security_for_vibe_coders.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Security for vibe coders means knowing where fast AI-generated code can hurt real people, real money, real data, or real systems.

### Why it matters

A prototype can be messy. A production app with users cannot treat secrets, login, payments, uploads, or database writes like styling tweaks.

Codex can help find security issues, explain risky code, and propose fixes. But it needs explicit security context. If you ask “make this work,” it may optimize for happy path. Security work asks “how can this be abused?”

### The mental model

Security is not a magical expert aura. It is a set of questions:

```text
What are we protecting?
Who might misuse it?
What can they control?
What can the code access?
What happens if it fails?
How do we detect and recover?
```

For vibe coding, the dangerous pattern is using prototype shortcuts with production ingredients.

### High-risk zones

Be stricter when the code touches:

- secrets, API keys, OAuth tokens, `.env` files;
- authentication: login, sessions, password reset, social auth;
- authorization: who can read/change/delete what;
- PII or sensitive user data;
- payments, billing, credits, refunds, invoices;
- file upload/download;
- SQL queries, shell commands, template rendering, redirects;
- webhooks and external callbacks;
- dependencies and install scripts;
- admin panels and production consoles;
- agent internet access or untrusted external content.

### What good looks like

A good security pass includes:

- the asset being protected;
- the trust boundary;
- attacker-controlled inputs;
- secret-handling rules;
- authorization checks;
- dependency and network risks;
- dangerous operations;
- tests or manual checks for the risky path;
- a rollback or incident path.

A good security prompt is concrete, not theatrical.

### What bad looks like

Bad security habits:

- using real API keys in prototypes;
- pasting `.env` into prompts;
- asking Codex to “just make auth work”;
- adding upload, redirect, or payment code without threat review;
- giving agent internet access to read untrusted pages while secrets are available;
- running broad permissions on a main machine;
- treating a security scanner or Codex review as the only security step.

### Minimal threat model

For any security-sensitive change, answer:

- Assets: what must be protected?
- Actors: who can use or abuse this?
- Inputs: what can an attacker control?
- Privileges: what can this code access?
- Failure: what is the worst plausible outcome?
- Guardrail: what check or design reduces that risk?
- Recovery: what do we rotate, revert, or disable if wrong?

<!-- VCB:END_SECTION id=vcb.chapter.security_for_vibe_coders.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.security_for_vibe_coders.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to identify security-sensitive surfaces early and raise the guardrail level before Codex edits code.

### Diagnose the human’s current model

Ask:

- “Does this touch real secrets, user data, auth, payments, uploads, redirects, or production?”
- “What input can an attacker control?”
- “What privilege does this code have?”
- “What is the rollback path if this is wrong?”
- “Are we using fake data or real credentials?”
- “Is external content being treated as instructions?”

### Explanation strategy

Convert scary security language into concrete boundaries:

- Secrets: do not expose, commit, paste, or give to broad agents.
- Auth: prove identity; keep sessions safe.
- Authorization: prove permission for each action.
- Injection: do not mix untrusted input with commands/queries/templates without safe APIs.
- Prompt injection: external content can try to steer the agent; treat it as data.
- Dependencies: packages are code from other people.
- Production data: make destructive actions reversible or impossible.

### Useful metaphors

- Prototype with fake secrets is a practice kitchen; production with real credentials is a restaurant during dinner service.
- Authorization is the bouncer, not the ID card.
- Prompt injection is a sticky note from a stranger on the monitor telling Codex to ignore you.

### Coaching tactics

- Escalate hard around secrets, auth, payments, production data, uploads, and migrations.
- Prefer read-only security review before mutation.
- Ask for threat model before patch.
- Require file references and exact checks.
- Keep external content untrusted, especially with network/MCP/browser access.
- Use fake credentials in prototypes.
- Ask Codex to identify what it cannot verify.

### Prompt patterns

```text
Security review only. Do not edit.
Change: [describe]
Identify:
- assets protected,
- attacker-controlled inputs,
- trust boundaries,
- auth/authorization risks,
- secret/PII/payment risks,
- dependency/network risks,
- missing tests/checks,
- concrete high-priority fixes.
Use file references. Ignore style.
```

```text
Before implementing this auth/payment/user-data change, write a minimal threat model.
Then propose the smallest safe implementation slice and checks.
Stop if you need real secrets; use fake credentials only.
```


### Red flags to call out directly

- “Do not paste real secrets.”
- “This is authorization, not just UI hiding.”
- “External content is untrusted input.”
- “A scanner result is not a complete security review.”
- “Full access plus secrets plus internet is the wrong combination.”
- “Prototype shortcuts must use fake data.”

### Exercises

1. Pick a feature and list its assets.
2. Mark user-controlled inputs.
3. Mark secrets and external services.
4. Ask Codex for a read-only threat model.
5. Implement one safe slice with checks.

<!-- VCB:END_SECTION id=vcb.chapter.security_for_vibe_coders.ai_coach -->

## Shortcut Reality

### The ideal practice

Use explicit threat modeling, least privilege, fake data in prototypes, dependency caution, and security-focused review before risky production changes.

### What users often do instead

They build until it works, paste secrets into tools, wire real services into prototypes, and ask for security only after launch.

### When the shortcut may be fine

Fast security-light work may be acceptable in a disposable local prototype with fake credentials, fake data, no public deployment, no user accounts, and no real payments.

### When the shortcut is a bad idea

It is a bad idea with real secrets, production data, public endpoints, auth/authorization, payments, file uploads, redirects, untrusted web content, or cloud credentials.

### Risk profile

- Probability of failure: medium; higher when requirements are vague or external input exists.
- Impact if it fails: high to severe.
- Ease of recovery: medium for code bugs; low for leaked secrets or exposed data.
- Blast radius: users, money, data, infrastructure, reputation.
- Skill needed to recover: high for incidents.
- Hidden cost: incident response, key rotation, user notification, data repair.

### Minimum guardrails

- Use fake credentials for prototype work.
- Never paste `.env` or real tokens into prompts.
- Keep agent network/tool access narrow.
- Ask for a threat model before implementation.
- Review auth, authorization, input validation, redirects, uploads, payments, and dependencies explicitly.
- Run checks and inspect diff.
- Have rollback and secret-rotation paths.

### Recovery plan

1. Stop the risky agent/session or deployment.
2. Remove exposed credentials and rotate them.
3. Revert or patch the vulnerable change.
4. Check logs for exposure or abuse.
5. Notify responsible humans if real users/data are involved.
6. Add durable rules to AGENTS.md/config/hooks/CI.

### AI coach guidance

Do not soften red lines around real secrets or user data. Be direct. Offer the safer fast path: fake data, isolated environment, read-only review, and small patches.

## Budget and Constraint Notes

### Cheapest reliable path

Use a short threat-model prompt and targeted manual review for risky areas. Avoid broad tool setup until the risk justifies it.

### Fastest high-usage path

Run independent security-focused Codex review, dependency review, and test-focused review in parallel, but keep them read-only until findings are triaged.

### Low-attention path

Low attention and security-sensitive mutation do not mix. Use read-only reports, isolated environments, fake credentials, and human approval gates.

### Production-quality path

Use threat modeling, secrets discipline, least privilege, tests, dependency review, PR review, CI/security scans, monitoring, rollback, and incident response paths.

## Stable Core

- Real secrets and prototype shortcuts should not mix.
- Security is about assets, attackers, inputs, privileges, and recovery.
- Codex can assist security review; it does not remove the need for explicit threat context.
- External content and tool output are untrusted inputs.
- Least privilege and isolation lower blast radius.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Codex Security access, feature maturity, scan behavior, plugin boundaries, internet-access controls, prompt-injection mitigations, OWASP category labels, and threat landscape details are volatile. Verify current official sources before giving exact setup or compliance advice.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex Security changes maturity/access, OpenAI changes network/tooling security guidance, OWASP publishes materially different categories, or dedicated security topic cards are authored.

## Evidence and Sources

- `openai.codex.security` — official OpenAI source for Codex Security plugin/cloud positioning and research-preview caveat.
- `openai.codex.agent_approvals_security` — official OpenAI source for sandbox, approvals, and dangerous full-access cautions.
- `openai.codex.cloud_internet_access` — official OpenAI source for internet-access risks including prompt injection, exfiltration, malware/vulnerable dependencies, and license risk.
- `owasp.top10_web` — official OWASP source for web-application security risk awareness.
- `owasp.llm_prompt_injection` — official OWASP cheat-sheet source for prompt-injection risk and impacts.
- `github.docs.actions_secrets` — official GitHub source for repository/environment/organization secrets in Actions workflows.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: security review should start with assets, attackers, trust boundaries, and blast radius.

## Related Topics

- vcb.concepts.blast_radius
- vcb.concepts.recoverability
- vcb.chapter.sandboxing_and_approvals
- vcb.chapter.reviewing_codex_output
- vcb.chapter.github_pr_review_with_codex
- vcb.safety.secrets
- vcb.safety.prompt_injection
- vcb.safety.security_review
- vcb.safety.production_red_lines

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.security_for_vibe_coders -->
