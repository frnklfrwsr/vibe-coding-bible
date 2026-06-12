<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.automation_spam version=0.1.0 -->
---
version: 0.1.0
last_verified: '2026-06-10'
last_reviewed: '2026-06-10'
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
  parallel, cloud, automation, and GUI/browser shortcut harm reduction
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
id: vcb.shortcut.automation_spam
title: Automation Spam
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex Cloud
- Codex App
- Codex Automations
- Codex CLI non-interactive mode
- Computer Use
- browser/GUI tasks
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- parallel_cloud_automation
- delegation
- automation
- browser_gui
- blast_radius
risk_level:
  prototype: MODERATE_RISK_SHORTCUT
  personal_tool: HIGH_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: DO_NOT_DO_IN_PRODUCTION
  security_sensitive: NEVER_WITH_REAL_SECRETS_OR_USER_DATA
recoverability:
  easy_if_committed: false
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- actionable-output definition
- silence/archive criteria
- duplicate suppression
- owner/severity fields
- scheduled usefulness review
shortcut_profiles:
- vcb.shortcut.automation_spam
durable_principles:
- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
likely_to_change:
- automation scheduling controls
- inbox/triage UI
- integration behavior
- model and reasoning defaults for scheduled tasks
obsolete_when:
- automation systems reliably learn actionability, dedupe across runs, and suppress noise
  without explicit user rules
related_topics:
- vcb.codex.automations
- vcb.constraints.attention_budget
- vcb.constraints.usage_burn
- vcb.shortcut.unattended_long_runs
- vcb.shortcut.skill_sprawl
- vcb.workflow.ci_triage
---

# Automation Spam

> Summary:
> Automation Spam means scheduling recurring AI checks that produce noise, duplicated findings, vague reports, or inbox clutter faster than humans can act on them.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.automation_spam.human -->
## 1. For the Human: Plain-Language Concept

### What this means

This shortcut says: “Automate it so I do not have to think about it.” Automation helps when the output is actionable. It fails when it creates a second inbox of low-quality summaries, repeated warnings, and stale tasks.

### Why it matters

Recurring work competes for attention. A noisy automation trains humans to ignore it, which is worse than having no automation because real findings get buried with spam.

### What good looks like

Good: “Run weekly dependency triage and report only new actionable items with owner, source, severity, and suggested next step; archive when nothing changed.”

### What bad looks like

Bad: “Every morning, summarize the repo and tell me anything interesting.”

### Minimal example

An automation that reports failed CI with links and suspected owner is useful. An automation that posts “repo looks mostly healthy” every day is noise.

### Checklist

- define what counts as actionable
- archive or stay silent when nothing changed
- deduplicate repeated findings
- include owner/source/severity
- review automation usefulness on a schedule

<!-- VCB:END_SECTION id=vcb.shortcut.automation_spam.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.automation_spam.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach that automation must protect attention. A useful automation is allowed to be quiet.

### Diagnostic questions

- What decision should this automation help with?
- What output should be suppressed?
- Who acts on findings?
- How are repeats deduplicated?
- When should the automation be retired?

### Coaching tactics

- write silence criteria
- start with report-only manual dry runs
- make output structured and owner-oriented
- set review dates
- delete automations that create no decisions

### Red flags

- automation posts every run even with no findings
- findings have no owner or next action
- same issue repeats without state tracking
- human stops reading reports
- automation scope grows to “watch everything”

### Prompt pattern

```text
Design this automation as an attention filter. Define actionable findings, silence/archive behavior, duplicate handling, owner/severity fields, and retirement criteria. Start report-only and include examples of messages that should not be posted.
```

<!-- VCB:END_SECTION id=vcb.shortcut.automation_spam.ai_coach -->

## Shortcut Reality

### Ideal practice

Automate stable, repeatable checks that produce actionable, deduplicated findings and stay silent when there is nothing useful.

### What people often do instead

They schedule broad recurring summaries because setting up automation feels like progress.

### When the shortcut may be acceptable

Acceptable for low-risk report-only monitoring with clear suppression and review rules.

### When it becomes a bad trade

Bad when the automation creates noise, mutates state, touches sensitive accounts, or becomes a substitute for ownership.

### Risk profile

- Probability: medium for first automations; high when output criteria are vague.
- Impact: medium for attention debt; high when critical alerts are buried.
- Recoverability: high if deleted early; medium once teams rely on noisy reports.

### Blast radius

The shortcut can create alert fatigue, missed important findings, duplicated work, and stale automation that keeps consuming usage and attention.

### Minimum guardrails

- actionable-output definition
- silence/archive criteria
- duplicate suppression
- owner/severity fields
- scheduled usefulness review

### Recovery plan

1. Pause the automation.
2. Review the last runs and classify useful versus noisy output.
3. Rewrite the prompt with silence and dedupe rules.
4. Delete or narrow automations with no decision value.
5. Restart report-only and review after a small number of runs.

## Budget and Constraint Notes

### Cheapest reliable path

Write the smallest task packet, isolation rule, and review packet requirement before launching the agent. This costs less than reconciling a broad or unsafe background result.

### Fastest high-usage path

High-throughput users should track automation value by decisions created, not messages generated.

### Low-attention path

Low-attention users need stricter silence behavior because they will not triage a noisy inbox.

### Production-quality path

Production work requires human ownership of sensitive actions, branch/worktree isolation, least privilege, explicit evidence, and rollback or revocation planning.

### Prototype versus production

Prototype shortcuts are acceptable only when the environment, accounts, credentials, and data are fake or disposable. Production shortcuts need hard gates or refusal.

### Maintenance phase

Maintenance should remove stale automations, prune approvals, archive obsolete branches, update task templates, and encode safer defaults when the same shortcut repeats.

## Stable Core

- parallelism increases review and integration load unless scopes are disjoint
- background and non-interactive mutation require stronger isolation than supervised work
- browser, GUI, cloud, and automation surfaces need explicit blast-radius and recovery controls
- the minimum guardrail should move the user at least one level up the guardrail ladder

## Volatile Surface

- automation scheduling controls
- inbox/triage UI
- integration behavior
- model and reasoning defaults for scheduled tasks

## Obsolescence Watch

This card should be revised if:

- automation systems reliably learn actionability, dedupe across runs, and suppress noise without explicit user rules

## Evidence and Sources

- `openai.codex.app_automations` — Official OpenAI Codex automations guidance for scheduled background tasks, inbox behavior, and worktree/local-project choices.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for context, constraints, done-when criteria, planning, validation, and review.
- `openai.codex.use_cases.proactive_teammate` — Official OpenAI Codex use-case guidance for automation after durable work context setup.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.codex.automations`
- `vcb.constraints.attention_budget`
- `vcb.constraints.usage_burn`
- `vcb.shortcut.unattended_long_runs`
- `vcb.shortcut.skill_sprawl`
- `vcb.workflow.ci_triage`

<!-- VCB:STOP_RETRIEVAL reason="automation_spam_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.automation_spam -->
