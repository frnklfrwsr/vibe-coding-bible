<!-- VCB:BEGIN_TOPIC id=tool.codex_security version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-11'
last_reviewed: '2026-06-11'
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
evidence_scope: official OpenAI/Codex Security documentation plus VCB maintainer synthesis for review workflow, risk, budget, and coaching guidance
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
type: tool_card
status: active
review_cadence: monthly
next_review_due: '2026-07-11'
last_pricing_reviewed: '2026-06-11'
pricing_volatility: very_high
pricing_snapshot_required: true
pricing_snapshot_ids:
- vcb.pricing_snapshot.openai_codex
stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: HIGHLY_VOLATILE
id: tool.codex_security
title: Codex Security
name: Codex Security
category: codex_security_review
setup_effort: 'medium to high: requires authorized repository access, Codex Cloud or plugin setup, review owner, threat-model context, and findings triage workflow'
maintenance_effort: 'high: threat models, repository environments, access, scan scope, finding review process, and fix validation must track code and product changes'
debugging_effort: 'high: results may depend on repository setup, scan scope, generated threat model quality, validation artifacts, dependency behavior, and human severity judgment'
lock_in_risk: 'moderate to high: the workflow depends on first-party Codex Security plugin/cloud behavior and GitHub/Codex integration mechanics'
hidden_cost_risk: 'high: broad scans, noisy findings, stale threat models, over-trusted patches, and delayed triage can consume review capacity without reducing real risk'
codex_integration_value: strong when it is treated as evidence-backed security review assistance, not as final security approval
best_for:
- authorized repository security scans
- security-focused diff review
- vulnerability backlog triage
- finding validation and reproduction evidence
- minimal patch preparation for human review
- threat-model-informed prioritization
not_for:
- unauthorized code assessment
- replacing manual security review
- compliance certification
- penetration testing by itself
- unreviewed patch application
- scanning production secrets or sensitive data unnecessarily
integrates_with_codex:
- Codex Security plugin
- Codex Security cloud
- Codex Cloud environments
- GitHub repositories
- threat model review
- human security review
- pull request workflow
hidden_costs:
- initial scan and backfill delay
- review queue noise
- false negatives and unvalidated findings
- patch review burden
- threat model maintenance
- security owner time
applies_to:
- security scans
- security diff review
- vulnerability remediation
- threat models
- GitHub repository review
- security finding triage
shortcut_profiles:
- vcb.shortcut.cloud_work_with_real_secrets
- vcb.shortcut.reviewing_cloud_summary_only
- vcb.shortcut.trusting_external_tool_output
- vcb.shortcut.overbroad_ci_permissions
- vcb.shortcut.long_lived_ci_secrets
durable_principles:
- Security tooling produces evidence, not permission to skip security ownership.
- A finding is useful only when it includes affected code, exploitability context, severity, and a reviewable fix path.
- Threat-model context improves security review because generic scanning cannot know business-critical assets by itself.
likely_to_change:
- Codex Security access, plugin installation flow, cloud scan setup, supported workflows, finding fields, severity labels, validation mechanics, UI labels, and GitHub integration behavior
obsolete_when:
- OpenAI retires Codex Security or replaces it with another first-party security-review product that no longer supports plugin/cloud security review workflows.
related_topics:
- tool.codex_cloud
- tool.codex_github_review
- tool.codex_agents_md
- tool.codex_config
- vcb.safety.security_review
- vcb.safety.secrets
- vcb.safety.production_red_lines
- vcb.workflow.reviewing_diffs
- vcb.workflow.github_pr_review
- vcb.shortcut.reviewing_cloud_summary_only
- vcb.shortcut.trusting_external_tool_output
- vcb.shortcut.cloud_work_with_real_secrets
---

# Codex Security

> Summary:
> Codex Security is a first-party Codex security-review surface for authorized repositories, security-focused diffs, vulnerability findings, threat-model-informed triage, and reviewed fix preparation.

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

<!-- VCB:BEGIN_SECTION id=tool.codex_security.human -->
## 1. For the Human: Plain-Language Concept

### What this tool is

Codex Security is a Codex security-review tool. It helps inspect code you are authorized to assess, find likely vulnerabilities, validate plausible issues where possible, review security-sensitive diffs, and prepare small fixes for human review.

There are two related ideas:

- **Codex Security plugin:** security-review workflows inside a Codex thread for a local/open repository.
- **Codex Security cloud:** security scans for connected GitHub repositories through Codex Web / Codex Cloud.

### Why it matters

Normal “does this work?” review misses security bugs. A feature can pass tests and still leak data, skip authorization, mishandle untrusted input, expose secrets, or create a dangerous dependency path.

Codex Security matters because it gives you a security-focused review pass with code context, threat-model context, validation evidence when available, and patch suggestions that a human can inspect.

### What good looks like

Good use looks like this:

1. You scan only code you are authorized to review.
2. You give Codex Security enough context about entry points, trust boundaries, sensitive data, privileged actions, and business-critical paths.
3. You review findings by evidence and exploitability, not by scary wording.
4. You fix one finding at a time with minimal diffs.
5. You require regression evidence before accepting the fix.

### What bad looks like

Bad use looks like this:

- “Run a security scan and make everything secure.”
- Accepting a proposed patch without reviewing the changed trust boundary.
- Treating “no findings” as proof that the app is safe.
- Running broad scans without an owner to triage them.
- Giving a security tool access to unnecessary secrets, production data, or account authority.

### Minimal example

A new file-upload endpoint should trigger a focused security scan for upload parsing, content-type assumptions, path traversal, auth/authorization checks, size limits, storage permissions, logging, and negative tests.

A useful finding should say what code is affected, why it is exploitable or risky, what evidence was collected, what the smallest fix is, and how the fix was checked.

### Best-fit cases

- authorized repository security scans
- security-focused diff review
- vulnerability backlog triage
- finding validation and reproduction evidence
- minimal patch preparation for human review
- threat-model-informed prioritization

### Not-fit cases

- unauthorized code assessment
- replacing manual security review
- compliance certification
- penetration testing by itself
- unreviewed patch application
- scanning production secrets or sensitive data unnecessarily

### Setup, maintenance, and debugging effort

| Dimension | Practical read |
|---|---|
| Setup effort | medium to high: requires authorized repository access, Codex Cloud or plugin setup, review owner, threat-model context, and findings triage workflow |
| Maintenance effort | high: threat models, repository environments, access, scan scope, finding review process, and fix validation must track code and product changes |
| Debugging effort | high: results may depend on repository setup, scan scope, generated threat model quality, validation artifacts, dependency behavior, and human severity judgment |
| Lock-in risk | moderate to high: the workflow depends on first-party Codex Security plugin/cloud behavior and GitHub/Codex integration mechanics |
| Hidden cost risk | high: broad scans, noisy findings, stale threat models, over-trusted patches, and delayed triage can consume review capacity without reducing real risk |

### Checklist

- confirm you are authorized to assess the repository
- choose the narrowest useful workflow: diff review, path scan, deep scan, or one finding fix
- write threat-model context before trusting scan priority
- separate confirmed findings from unvalidated suspicions
- require file/path evidence, exploit sketch, severity, and fix verification
- review every proposed patch as a normal code change
- keep secrets, production data, and account authority out of the scan unless explicitly required and approved

<!-- VCB:END_SECTION id=tool.codex_security.human -->

<!-- VCB:BEGIN_SECTION id=tool.codex_security.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach Codex Security as a security-review assistance tool. The goal is to improve evidence, triage, and fix discipline without letting the human outsource security ownership.

### Diagnostic questions

- Is the repository authorized for security assessment?
- Is the user asking for a repository-wide scan, a changed-code review, or one finding fix?
- What are the entry points, trust boundaries, auth assumptions, sensitive data paths, and privileged actions?
- Who will triage findings and approve severity?
- What artifact will prove a fix: diff, reproduction, validation log, negative test, or manual review note?
- Does the scan need secrets or production data, or can it run with fake/local/staging context?

### Coaching tactics

- route “run Codex Security” requests to `tool.codex_security` before generic security chapters
- force a threat-model paragraph before broad scans
- push broad scans into report-first mode unless a specific approved finding is being fixed
- keep patch generation separate from patch acceptance
- ask for evidence packets, not summaries
- escalate secrets, auth, payments, user data, production state, or irreversible changes to a human owner

### Prompt pattern

```text
Use Codex Security on this authorized repository/change.
Scope: [repo/path/diff/finding].
Threat model: [entry points, trust boundaries, auth assumptions, sensitive data, privileged actions].
Return: confirmed findings, unvalidated candidates, evidence paths, exploit sketch, severity reasoning, smallest fix option, and verification steps.
Do not apply patches until I review the finding and proposed diff.
```

### Red flags

- the human asks for a security guarantee
- the scan target is not authorized
- there is no review owner for findings
- the threat model is missing or generic
- a proposed patch changes broad auth, secrets, payments, or data paths without tests
- the human treats a scan summary as a merge approval

### Intervention rule

When the human asks for current Codex Security availability, exact workflow names, UI labels, setup mechanics, scan behavior, supported plans, pricing, model availability, or command/config details, route to official OpenAI sources or a dated snapshot instead of answering from memory.

<!-- VCB:END_SECTION id=tool.codex_security.ai_coach -->

## Shortcut Reality

### The ideal practice

Use Codex Security as a focused security review assistant. Feed it scoped code and threat-model context, inspect evidence-backed findings, fix one issue at a time, and keep human security ownership intact.

### What users often do instead

Users often run a broad scan, accept the most alarming summary, ask Codex to patch many findings at once, or treat a clean scan as proof that no security issue exists.

### When the shortcut may be acceptable

A lightweight Codex Security pass can be acceptable for a low-risk prototype, a small diff, a local repository with fake data, or a report-only scan where the result is explicitly advisory.

### When it becomes a bad trade

It becomes a bad trade when the scan involves secrets, user data, production infrastructure, auth, payments, admin actions, compliance claims, broad patches, or unowned findings.

### Relevant shortcut cards

- `vcb.shortcut.cloud_work_with_real_secrets`
- `vcb.shortcut.reviewing_cloud_summary_only`
- `vcb.shortcut.trusting_external_tool_output`
- `vcb.shortcut.overbroad_ci_permissions`
- `vcb.shortcut.long_lived_ci_secrets`

### Minimum guardrails

- authorization confirmed before scanning
- one scan scope and one review owner
- threat-model context captured before broad scan priority is trusted
- report-first output by default
- no auto-accepted patches
- regression or reproduction evidence for accepted fixes
- secrets and production data excluded unless explicitly approved

### Recovery plan

Stop the scan or patch loop, preserve reports and proposed diffs, revoke unnecessary access, rotate exposed secrets if any were included, split findings into one issue per fix, rerun validation on the specific finding, and require human review before merge.

## Budget and Constraint Notes

### Cheapest reliable path

Use the normal `vcb.safety.security_review` checklist and focused diff review first. Add Codex Security when the risk justifies scan setup, threat-model work, and human triage time.

### Fastest high-usage path

Use Codex Security for high-signal report-first scans, security-focused diffs, and bounded finding fixes. Do not batch unrelated patches; that creates review debt instead of speed.

### Low-attention path

Low-attention use is acceptable only for report generation with a named review owner. Write-capable remediation, auth changes, secrets, payments, and production-sensitive fixes require active review.

### Production-quality path

Production use requires authorized repository scope, maintained threat model, least-privilege environment, evidence-backed findings, minimal patches, negative tests where relevant, and human acceptance of severity and fix.

### Hidden costs to watch

- initial scan and backfill delay
- review queue noise
- false negatives and unvalidated findings
- patch review burden
- threat model maintenance
- security owner time

## Stable Core

- Security tooling produces evidence, not permission to skip security ownership.
- A finding is useful only when it includes affected code, exploitability context, severity, and a reviewable fix path.
- Threat-model context improves security review because generic scanning cannot know business-critical assets by itself.

## Volatile Surface

- Codex Security access, plugin installation flow, cloud scan setup, supported workflows, finding fields, severity labels, validation mechanics, UI labels, and GitHub integration behavior

Exact availability, feature maturity, UI labels, setup mechanics, scan behavior, workflow names, pricing, plan limits, usage-credit quantities, model availability, command/config details, and context-window numbers must be checked against official OpenAI sources and dated snapshots.

## Obsolescence Watch

This card becomes obsolete when: OpenAI retires Codex Security or replaces it with another first-party security-review product that no longer supports plugin/cloud security review workflows.

Review official OpenAI Codex Security docs before relying on current mechanics.

## Evidence and Sources

- `openai.codex.security` — official source anchor for Codex Security overview and cloud positioning.
- `openai.codex.security_plugin` — official source anchor for plugin workflows, scans, diff review, and fix-finding loop.
- `openai.codex.security_setup` — official source anchor for cloud setup, initial scans, threat-model review, findings, and PR creation posture.
- `openai.codex.security_threat_model` — official source anchor for threat-model context and prioritization.
- `openai.codex.security_faq` — official source anchor for validation, isolation, patch-application boundaries, and manual-review limits.
- `openai.codex.agent_approvals_security` — official source anchor for Codex sandboxing, approvals, and network-access posture.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for durable control-loop, review, blast-radius, and recovery guidance.

## Related Topics

- `tool.codex_cloud`
- `tool.codex_github_review`
- `tool.codex_agents_md`
- `tool.codex_config`
- `vcb.safety.security_review`
- `vcb.safety.secrets`
- `vcb.safety.production_red_lines`
- `vcb.workflow.reviewing_diffs`
- `vcb.workflow.github_pr_review`
- `vcb.shortcut.reviewing_cloud_summary_only`
- `vcb.shortcut.trusting_external_tool_output`
- `vcb.shortcut.cloud_work_with_real_secrets`

<!-- VCB:STOP_RETRIEVAL reason="tool_card_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=tool.codex_security -->
