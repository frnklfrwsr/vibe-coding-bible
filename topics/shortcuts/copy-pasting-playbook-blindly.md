<!-- VCB:BEGIN_TOPIC id=vcb.shortcut.copy_pasting_playbook_blindly version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex skills, MCP, plugins, hooks, best-practices,
  workflow, configuration, and security guidance; official vendor/security documentation
  where cited; VCB maintainer synthesis for tool-sprawl, skill, and process shortcut
  harm reduction
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
id: vcb.shortcut.copy_pasting_playbook_blindly
title: Copy-Pasting Playbook Blindly
type: shortcut
shortcut_type: risk_managed_shortcut
status: active
review_cadence: quarterly
next_review_due: '2026-09-10'
applies_to:
- Codex playbooks
- prompt libraries
- team workflow templates
- reusable process
- AI coach prompts
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: STABLE
shortcut_category:
- playbooks
- reusable_workflows
- process
- prompting
risk_level:
  prototype: LOW_RISK_SHORTCUT
  personal_tool: MODERATE_RISK_SHORTCUT
  internal_tool: HIGH_RISK_SHORTCUT
  public_app: HIGH_RISK_SHORTCUT
  security_sensitive: HIGH_RISK_SHORTCUT
recoverability:
  easy_if_committed: true
  easy_if_no_git_checkpoint: false
  requires_expertise_if_data_migration: true
minimum_guardrails:
- fill context before use
- adapt risk and forbidden areas
- state done evidence
- remove irrelevant steps
shortcut_profiles:
- vcb.shortcut.copy_pasting_playbook_blindly
durable_principles:
- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed
  review
likely_to_change:
- Codex playbook examples
- workflow templates
- team prompt-library conventions
- best-practice wording
obsolete_when:
- Codex can reliably auto-tailor playbooks to repository context, risk class, available
  checks, and recovery constraints before execution
related_topics:
- vcb.chapter.codex_playbooks
- vcb.prompting.four_part_prompt
- vcb.prompting.acceptance_criteria
- vcb.constraints.scope_budget
- vcb.failure.done_claim_without_evidence
---

# Copy-Pasting Playbook Blindly

> Summary:
> Copy-pasting playbook blindly is applying a reusable Codex workflow template without adapting risk, scope, repo context, constraints, and done evidence.

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

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.copy_pasting_playbook_blindly.human -->
## 1. For the Human: Plain-Language Concept

### What this means

A playbook is a starting route, not a commandment. The shortcut is pasting it into Codex without filling in the project-specific facts that make it safe.

### Why it matters

Reusable workflows are useful only when they are fitted to task size, risk, constraints, files, checks, and forbidden areas. Blind reuse can create false confidence.

### What good looks like

Good: “Start from a playbook, then fill goal, context, constraints, done-when evidence, risk level, and what must not change.”

### What bad looks like

Bad: “Paste a full production hardening playbook into a toy prototype, or paste a quick prototype playbook into auth/payment code.”

### Minimal example

Before using a dependency-migration playbook, add the package name, current version, target version, lockfile policy, tests to run, rollback plan, and no-touch areas.

### Checklist

- name the task type
- delete irrelevant steps
- add repo-specific files and commands
- set risk level
- define evidence of done

<!-- VCB:END_SECTION id=vcb.shortcut.copy_pasting_playbook_blindly.human -->

<!-- VCB:BEGIN_SECTION id=vcb.shortcut.copy_pasting_playbook_blindly.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to adapt reusable workflows by risk and context instead of mistaking template length for quality.

### Diagnostic questions

- What part of the playbook does not apply?
- What project facts are missing?
- What risk level is this task?
- What evidence will prove the playbook succeeded?

### Coaching tactics

- ask Codex to tailor the playbook before executing
- force removal of irrelevant steps
- add forbidden areas and rollback plan
- separate “template” from “ready prompt”

### Red flags

- playbook pasted unchanged
- no repo files or commands named
- risk level omitted
- done criteria generic or vibe-based

### Prompt pattern

```text
Tailor this Codex playbook before execution. Remove irrelevant steps, add project-specific context, risk level, forbidden areas, smallest checks, acceptance evidence, rollback plan, and any open assumptions that must be confirmed first.
```

<!-- VCB:END_SECTION id=vcb.shortcut.copy_pasting_playbook_blindly.ai_coach -->

## Shortcut Reality

### Ideal practice

Use playbooks as reusable structure, then specialize them to the actual repo, risk, budget, and evidence target.

### What people often do instead

People paste long templates because they look rigorous, then skip the tailoring that creates actual control.

### When the shortcut may be acceptable

Acceptable for low-risk learning tasks when the user labels the result as a draft and does not claim production readiness.

### When it becomes a bad trade

Bad when a blind playbook touches production, security, dependencies, data, migrations, CI, or broad refactors.

### Risk profile

- Probability: medium whenever prompt libraries grow; high when users copy from examples under time pressure.
- Impact: low for practice tasks; high when the wrong playbook drives risky edits.
- Recoverability: high if no edits yet; medium after branch edits; low after merge/deploy.

### Blast radius

A mismatched playbook can route Codex into the wrong workflow and make the human review the wrong evidence.

### Minimum guardrails

- fill context before use
- adapt risk and forbidden areas
- state done evidence
- remove irrelevant steps

### Recovery plan

1. Stop before execution if possible.
2. Ask Codex to list missing project facts.
3. Retune the playbook by risk and task type.
4. Re-run with scoped files and checks.
5. Review diffs against the tailored acceptance criteria.

## Budget and Constraint Notes

### Cheapest reliable path

Use the smallest durable artifact that prevents the next likely mistake. That may be a saved prompt, one disabled-by-default skill, one scoped MCP server, one report-only hook, or one short workflow note.

### Fastest high-usage path

High-throughput users should template only the workflows that repeat. Spend throughput on clear inputs, expected outputs, and review evidence rather than on broad libraries of tools, skills, hooks, or ceremonies.

### Low-attention path

Low-attention delegation needs stricter defaults: fewer enabled tools, explicit triggers, report-only or read-only behavior first, branch isolation, and a required review packet before mutation is accepted.

### Production-quality path

Production-quality work requires provenance, least privilege, maintained guidance, current setup facts, artifact-backed review, and deletion or disablement paths for unused process surfaces.

### Prototype versus production

A prototype may stay light and messy if it is disposable. Once the work becomes shared, persistent, security-sensitive, or production-bound, the shortcut needs explicit boundaries and review evidence.

### Maintenance phase

Maintenance is where tool/process shortcuts compound. Review skills, hooks, MCP servers, plugins, tool choices, and reusable workflows after stack changes, onboarding, incidents, repeated failures, and major phase transitions.

## Stable Core

- reuse should reduce repeated risk, not create hidden process drag
- tools, skills, hooks, and workflows need ownership, scope, and deletion criteria
- external tool/context surfaces require provenance, least privilege, and evidence-backed review

## Volatile Surface

- Codex playbook examples
- workflow templates
- team prompt-library conventions
- best-practice wording

## Obsolescence Watch

This card should be revised if:

- Codex can reliably auto-tailor playbooks to repository context, risk class, available checks, and recovery constraints before execution

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for goals, context, constraints, done-when criteria, planning, checks, review, and reusable project guidance.
- `openai.codex.workflows` — Official OpenAI Codex workflows guidance for explicit context, definition of done, local/cloud task packets, reproduction, checks, and review patterns.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, recoverability, and review discipline.

## Related Topics

- `vcb.chapter.codex_playbooks`
- `vcb.prompting.four_part_prompt`
- `vcb.prompting.acceptance_criteria`
- `vcb.constraints.scope_budget`
- `vcb.failure.done_claim_without_evidence`


<!-- VCB:STOP_RETRIEVAL reason="copy_pasting_playbook_blindly_shortcut_complete" -->
<!-- VCB:END_TOPIC id=vcb.shortcut.copy_pasting_playbook_blindly -->
