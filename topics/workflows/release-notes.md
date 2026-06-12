<!-- VCB:BEGIN_TOPIC id=vcb.workflow.release_notes version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex documentation/workflow anchors plus GitHub release-note
  documentation and changelog expert-practice guidance
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
- prototype
- mvp
- production_build
- maintenance
- major_refactor
attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation
id: vcb.workflow.release_notes
title: Release Notes Workflow with Codex
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex Cloud
- GitHub Releases
- Pull requests
- Documentation
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.checklist_theater
- vcb.shortcut.automation_spam
- vcb.shortcut.context_dumping
durable_principles:
- release notes are for users and operators
- only user-facing or operationally relevant changes belong
- generated notes need source verification
likely_to_change:
- GitHub release UI
- auto-generated release-note behavior
- project release categories
- Codex skill/automation behavior
- public feature status
obsolete_when:
- release tooling can produce complete accurate user-facing notes without project
  context or human review
related_topics:
- vcb.chapter.prompt_library_to_team_workflow
- vcb.workflow.documentation_updates
- vcb.workflow.github_pr_review
- vcb.workflow.reviewing_diffs
- vcb.codex.skills
- vcb.codex.automations
---

> Summary:
> Release notes workflow uses Codex to turn merged changes into human-readable release information while separating user-facing changes from internal noise and unverified claims.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.release_notes.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Release notes explain what changed in a release for the people who need to use, deploy, support, or understand it.

### Why it matters

Codex can summarize commits quickly, but raw commit summaries often include internal noise and miss user impact.

### The mental model

Release notes are a shipping label. They should tell the receiver what matters, not list every screw used in the box.

### What good looks like

Good: “Draft release notes from merged PRs since v1.4.0. Include user-facing changes, breaking changes, migrations, fixes, known issues, and verification status. Exclude private/internal-only context.”

### What bad looks like

Bad: Publishing generated commit summaries with unverified claims, internal codenames, and no breaking-change callouts.

### Minimal example

Give Codex the version range, PRs/commits, public feature status, categories, audience, excluded private context, and verification requirement.

### Checklist

- version range or release boundary named
- audience is clear
- breaking changes and migrations are explicit
- user-facing changes separated from internal chores
- known issues are listed when relevant
- claims are traceable to PRs/docs/tests
- private or unreleased context is excluded
<!-- VCB:END_SECTION id=vcb.workflow.release_notes.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.release_notes.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to make release notes accurate, scoped, and user-centered.

### Diagnose the human’s current model

- Who is the audience?
- What changed for users or operators?
- What is breaking or requires action?
- Which claims are verified?
- What private context must be excluded?

### Explanation strategy

Ask Codex to classify changes before drafting. Use categories such as Added, Changed, Fixed, Security, Deprecated, Removed, Known Issues, and Migration Notes only when they fit the project.

### Useful metaphor

Release notes are the map at the trailhead, not the raw GPS log.

### Coaching tactics

- separate classification from prose
- trace bullets to PRs or docs
- flag unverified claims
- keep internal chores out unless they affect operators
- turn recurring release-note drafting into a skill

### Prompt patterns

```text
Draft release notes for [range/version]. Sources: PRs, commits, docs, issues, tests. First classify changes by user impact, breaking/migration risk, security, fixes, known issues, and internal-only noise. Then write concise notes for [audience]. Exclude private roadmap/customer/internal context. Cite source PRs/commits in the draft notes or handoff.
```

### Red flags to call out directly

- generated notes include every commit
- breaking changes are buried
- unreleased/private roadmap appears
- security fix is vague or over-disclosed
- notes claim behavior not supported by PRs or docs

### Exercises

- Ask the human to remove internal noise from commit summaries.
- Have them classify PRs by release-note category.
- Review generated notes for unsupported claims.
<!-- VCB:END_SECTION id=vcb.workflow.release_notes.ai_coach -->

## Shortcut Reality

### The ideal practice

Generate a draft from source changes, then verify user-facing claims and publish only reviewed notes.

### What users often do instead

Users paste auto-generated release notes without editing.

### When the shortcut may be fine

Auto-generated notes can be fine for internal prereleases or low-stakes projects when clearly labeled.

### When the shortcut is a bad idea

It is a bad trade for public releases, breaking changes, security fixes, migrations, paid products, or regulated/customer-facing software.

### Risk profile

- Probability of failure: Medium risk of omissions and unsupported claims; high risk when changes are broad.
- Impact if it fails: Impact includes user confusion, support burden, missed migration steps, and accidental disclosure.
- Ease of recovery: Good before publication; medium after publication; poor after users act on wrong notes.
- Blast radius: The blast radius is every user/operator who relies on the notes to upgrade, deploy, or explain the release.
- Skill needed to recover: Low for drafting; medium for classification; high for security/breaking-change communication.
- Hidden cost: Support tickets, correction posts, trust loss, and stale public docs.

### Minimum guardrails

- classify before drafting
- trace claims to source PRs/docs/tests
- call out breaking changes
- exclude private context
- human publish approval

### Recovery plan

- Correct the release notes.
- Add missing migration/breaking-change details.
- Notify affected users/operators if needed.
- Update docs/changelog.
- Improve the release-note prompt or skill.

## Budget and Constraint Notes

### Cheapest reliable path

Use Codex to classify merged PRs, then human-edit a short release note for only user-facing changes.

### Fastest high-usage path

High-throughput teams can automate drafts, but keep human approval for public release notes and breaking/security sections.

### Low-attention path

Low-attention release-note automation should draft only and flag uncertain claims. It should not publish.

### Production-quality path

Production releases need verified claims, migration/breaking sections, known issues, and owner approval.

### Prototype versus production

Prototype release notes can be informal. Production and maintenance release notes need traceability and repeatable categories.

### Maintenance phase

In maintenance, release-note cost drops when PR labels, changelog categories, and docs expectations are standardized.

## Stable Core

- release notes are for users and operators
- only user-facing or operationally relevant changes belong
- generated notes need source verification

## Volatile Surface

- GitHub release UI
- auto-generated release-note behavior
- project release categories
- Codex skill/automation behavior
- public feature status

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- release tooling can produce complete accurate user-facing notes without project context or human review

## Evidence and Sources

- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, review, reusable skills, and verification.
- `openai.codex.use_cases.update_documentation` — Official OpenAI Codex use case for keeping documentation current from code, docs, release notes, and PR context.
- `github.docs.release_notes_generated` — Official GitHub documentation for automatically generated release notes.
- `keepachangelog.v1_1_0` — Practitioner changelog guidance for human-readable chronological release notes.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, and review discipline.

## Related Topics

- `vcb.chapter.prompt_library_to_team_workflow`
- `vcb.workflow.documentation_updates`
- `vcb.workflow.github_pr_review`
- `vcb.workflow.reviewing_diffs`
- `vcb.codex.skills`
- `vcb.codex.automations`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.release_notes -->
