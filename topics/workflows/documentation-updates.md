<!-- VCB:BEGIN_TOPIC id=vcb.workflow.documentation_updates version=0.1.0 -->
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
evidence_scope: official OpenAI/Codex documentation-update guidance plus VCB maintainer
  synthesis
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
id: vcb.workflow.documentation_updates
title: Documentation Update Workflow with Codex
type: workflow
review_cadence: quarterly
next_review_due: '2026-09-09'
applies_to:
- Codex App
- Codex Cloud
- AGENTS.md
- Skills
- Developer docs
- README files
- Runbooks
stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
  pricing: VOLATILE
shortcut_profiles:
- vcb.shortcut.accepting_looks_done
- vcb.shortcut.context_dumping
- vcb.shortcut.checklist_theater
- vcb.shortcut.stale_agents_md
durable_principles:
- docs should change with user-facing behavior
- documentation claims need trusted sources
- focused docs edits beat broad rewrites
likely_to_change:
- Codex documentation use-case behavior
- docs build commands
- repository docs structure
- public feature status
- automation/skill behavior
obsolete_when:
- documentation stays accurate automatically without source comparison or human review
related_topics:
- vcb.chapter.prompt_library_to_team_workflow
- vcb.codex.agents_md
- vcb.codex.skills
- vcb.workflow.release_notes
- vcb.workflow.reviewing_diffs
- vcb.prompting.context_management
---

> Summary:
> Documentation update workflow uses Codex to compare code, docs, release notes, and PR context, then draft focused documentation changes with verified public claims.

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

<!-- VCB:BEGIN_SECTION id=vcb.workflow.documentation_updates.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Documentation updates keep README files, developer docs, examples, runbooks, migration notes, and public docs aligned with what the code actually does.

### Why it matters

Codex can draft docs quickly, but it can also invent certainty or include private/internal context if you give it too much unfiltered context.

### The mental model

Docs are the contract people read when the code is not in front of them. A stale contract is worse than no contract when people trust it.

### What good looks like

Good: “Update only docs affected by this PR. Search for existing mentions, preserve structure and terminology, exclude private roadmap context, run docs checks, and list claims you could not verify.”

### What bad looks like

Bad: “Update the docs” leading to a broad rewrite, new unsupported claims, and changed terminology.

### Minimal example

Give Codex changed code, affected docs, public context, forbidden private context, audience, terminology rules, and docs checks.

### Checklist

- source change or behavior change is named
- affected docs are discovered before editing
- existing structure/terminology/frontmatter preserved
- public vs private context separated
- claims are supported by code/docs/PRs
- docs checks run when available
- unverified claims are listed
<!-- VCB:END_SECTION id=vcb.workflow.documentation_updates.human -->

<!-- VCB:BEGIN_SECTION id=vcb.workflow.documentation_updates.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach the human to use Codex for focused docs maintenance rather than broad prose rewrites.

### Diagnose the human’s current model

- What changed in user-visible behavior?
- Which docs mention this behavior?
- Which claims are public and verified?
- What terminology must stay consistent?
- Which docs build/check command applies?

### Explanation strategy

Make Codex map docs before drafting. Require a claim/source table for public docs. Preserve frontmatter, headings, examples, and cross-links unless the task explicitly changes them.

### Useful metaphor

Documentation is a signpost. A prettier sign pointing the wrong way is still dangerous.

### Coaching tactics

- search docs before editing
- draft smallest useful patch
- ban private customer/roadmap leakage
- separate docs update from release-note draft
- promote repeated docs workflows into skills or AGENTS.md rules

### Prompt patterns

```text
Update documentation for [change]. Sources: changed code/tests, PR/issue, existing docs, public release notes. First map affected docs and claims. Then update only necessary sections, preserve structure/terminology/frontmatter/cross-links, exclude private context, run docs checks, and report verified claims plus uncertain claims.
```

### Red flags to call out directly

- docs rewrite unrelated sections
- Codex invents availability or pricing
- private context appears in public docs
- examples no longer compile
- frontmatter or links are broken

### Exercises

- Ask the human to turn a PR diff into affected-docs search terms.
- Have them review a docs patch for unsupported claims.
- Practice splitting release notes from permanent docs.
<!-- VCB:END_SECTION id=vcb.workflow.documentation_updates.ai_coach -->

## Shortcut Reality

### The ideal practice

Map affected docs, make focused edits, verify claims, run docs checks, and record gaps.

### What users often do instead

Users skip docs or ask Codex for a broad docs refresh after the code has drifted.

### When the shortcut may be fine

Skipping docs may be fine for private experiments or internal throwaway prototypes.

### When the shortcut is a bad idea

It is a bad trade for public APIs, config changes, CLI commands, migrations, security behavior, pricing/limits, onboarding, or support-heavy products.

### Risk profile

- Probability of failure: High risk of stale or invented docs when docs are updated late or broadly.
- Impact if it fails: Impact includes user confusion, support burden, broken examples, and bad operational decisions.
- Ease of recovery: Good if claims are traceable; poor when broad rewrites obscure what changed.
- Blast radius: The blast radius is every user or teammate who relies on the stale or unsupported doc path.
- Skill needed to recover: Low for small README edits; medium for docs-system changes; high for public API/reference docs.
- Hidden cost: Support tickets, onboarding friction, broken examples, and repeated “tribal knowledge” repairs.

### Minimum guardrails

- map before editing
- claim/source table for public docs
- preserve structure
- exclude private context
- run docs checks or state why not

### Recovery plan

- Identify docs touched by the behavior.
- Revert unsupported broad rewrites.
- Patch high-impact public claims first.
- Run docs build/link/example checks.
- Add a docs-update rule to AGENTS.md or a skill.

## Budget and Constraint Notes

### Cheapest reliable path

Update the one doc page or README section directly affected by the change and list unverified claims.

### Fastest high-usage path

Use Codex to map affected docs and draft focused patches, then human-review public claims.

### Low-attention path

Low-attention docs automation should draft only, never publish public docs without review.

### Production-quality path

Production docs need source-backed claims, build/link/example checks, public/private context filtering, and owner approval for availability/security/pricing statements.

### Prototype versus production

Prototype docs can be lightweight notes. Production and maintenance docs need repeatable update rules and stale-doc detection.

### Maintenance phase

In maintenance, docs cost drops when every user-facing PR asks whether docs, examples, runbooks, and release notes need updates.

## Stable Core

- docs should change with user-facing behavior
- documentation claims need trusted sources
- focused docs edits beat broad rewrites

## Volatile Surface

- Codex documentation use-case behavior
- docs build commands
- repository docs structure
- public feature status
- automation/skill behavior

Review volatile details against official sources before freezing commands, UI labels, plan packaging, feature availability, model advice, package metadata, or exact tool behavior.

## Obsolescence Watch

- documentation stays accurate automatically without source comparison or human review

## Evidence and Sources

- `openai.codex.use_cases.update_documentation` — Official OpenAI Codex use case for keeping documentation current from code, docs, release notes, and PR context.
- `openai.codex.best_practices` — Official OpenAI Codex best-practices guidance for prompt structure, planning, review, reusable skills, and verification.
- `vcb.synthesis.stable_engineering_practice` — VCB maintainer synthesis for durable control-loop, risk, budget, and review discipline.

## Related Topics

- `vcb.chapter.prompt_library_to_team_workflow`
- `vcb.codex.agents_md`
- `vcb.codex.skills`
- `vcb.workflow.release_notes`
- `vcb.workflow.reviewing_diffs`
- `vcb.prompting.context_management`

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" -->
<!-- VCB:END_TOPIC id=vcb.workflow.documentation_updates -->
