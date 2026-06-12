<!-- VCB:BEGIN_TOPIC id=vcb.chapter.maintaining_updating_bible version=0.1.0 -->
---
id: vcb.chapter.maintaining_updating_bible
title: "Chapter 37 — Maintaining and Updating the Bible"
type: chapter
chapter_number: 37
version: 0.1.0
last_verified: '2026-06-09'
next_review_due: '2026-09-09'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Codex CLI
- Codex IDE Extension
- Codex Cloud
- GitHub
- documentation
- all project types

source_status:
  official_openai: true
  official_vendor: false
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: AGENTIC_PRINCIPLE
  surface: MODERATE
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
- vcb.shortcut.stale_agents_md
- vcb.shortcut.checklist_theater
- vcb.shortcut.process_overhead_for_tiny_project

durable_principles:
- Metadata makes staleness visible.
- Deprecation beats silent deletion.
- Source registers and indexes are part of the content.

likely_to_change:
- source-map conventions
- Codex feature maturity labels
- changelog behavior
- validator implementation

obsolete_when:
- Official source maps and product docs adopt a new durable update convention.
- Repository schema changes make this protocol incomplete.

related_topics:
- vcb.chapter.field_notes_unofficial_practices
- vcb.chapter.risk_managed_shortcuts
- vcb.chapter.how_to_use_this_bible
- vcb.chapter.prompt_library_to_team_workflow
- vcb.chapter.codex_playbooks
---

> Summary:
> The Bible must be maintained like software. This chapter defines the update loop: source check, metadata, prose, indexes, deprecation, changelog, validation, and editor gate.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.maintaining_updating_bible.human -->
## 1. For the Human: Plain-Language Concept


### What this means

This Bible is a living manual. AI-coding advice decays because products change, models change, UI changes, pricing changes, and users discover new practices.

A stale Bible is worse than a short Bible. It gives confident old advice.

### The maintenance loop

Use this loop:

```text
Find stale topic → check official source → compare against prose → update metadata → update prose → update indexes/registers → changelog → editor review
```

Do not silently rewrite history. If advice becomes obsolete, mark it deprecated and point to the replacement.

### What to review first

Review high-change content first:

| Topic type | Why it decays | Review posture |
|---|---|---|
| Pricing, credits, plan access | can change without stable principle changing | snapshot-only |
| UI names and commands | product surface changes quickly | monthly/volatile |
| model-specific advice | model behavior changes | monthly/watch |
| community tactics | anecdotal and fragile | monthly/watch |
| security threats | threat landscape changes | quarterly or sooner |
| Git/diff/recoverability concepts | durable engineering concepts | annual/semiannual |

### Source conflict rule

When sources disagree, use this priority order:

1. Current official OpenAI docs for Codex behavior.
2. Current official vendor docs for vendor/tool behavior.
3. Local repo evidence for what actually happens in the project.
4. Named expert/practitioner reports.
5. Community reports.
6. Speculation.

Do not use a community workaround to contradict official product behavior unless the workaround is explicitly labeled and tested.

### Metadata comes before prose

Before rewriting a topic, update or check:

- `last_verified`;
- `next_review_due`;
- `review_cadence`;
- `evidence_level`;
- `source_kind`;
- `stability`;
- `likely_to_change`;
- `obsolete_when`;
- `related_topics`;
- source register records.

### Deprecation is not deletion

Do not delete obsolete guidance without a trail. Users and AI coaches need to understand why the old advice changed.

A good deprecation note says:

```text
Deprecated on:
Replaced by:
Reason:
Migration note:
```

### Update checklist

```text
[ ] Topic still matches current official docs.
[ ] Product-specific details are still current or marked volatile.
[ ] Exact pricing/limits are not in stable prose.
[ ] Community practices remain labeled.
[ ] Deprecated advice has replacement route.
[ ] Indexes route to current IDs.
[ ] Source register has current source status.
[ ] Changelog entry exists.
[ ] Validator passes.
```

<!-- VCB:END_SECTION id=vcb.chapter.maintaining_updating_bible.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.maintaining_updating_bible.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human


### Teaching objective

Teach the AI maintainer to update the Bible like source code: preserve traceability, avoid quiet drift, and keep metadata reliable.

### Diagnose the maintenance task

Ask:

- Is this a stable principle update or a volatile product detail update?
- Which topic IDs are affected?
- Which official sources need re-checking?
- Is any field practice being promoted, downgraded, or deprecated?
- Do indexes/registers/schemas need to change?
- Is the change broad enough to need a changelog entry?

### Explanation strategy

Use the "source control for advice" metaphor:

> The Bible is code for future humans and AIs. If advice changes, leave a commit trail: source, reason, replacement, and review date.

### Update workflow for the AI maintainer

```text
1. Read manifest.json.
2. Identify affected topic IDs.
3. Check official OpenAI docs first for Codex behavior.
4. Check Codex changelog and feature maturity when product features are involved.
5. Check vendor docs for non-OpenAI tools.
6. Compare current sources to topic prose.
7. Update frontmatter before prose.
8. Update SOURCE_REGISTER.md.
9. Update indexes and related_topics.
10. Deprecate instead of deleting obsolete guidance.
11. Run scripts/validate_repository.py.
12. Produce a chunk report and stop for editor review.
```

### Useful metaphors

- **Weather versus climate:** stable principles are climate; UI/pricing/model details are weather.
- **Source map:** indexes and manifest are the map. If the map lies, retrieval fails.
- **Museum label:** deprecated guidance stays visible with a label explaining why it moved.

### Prompt pattern: stale topic review

```text
Review this VCB topic for staleness.

Topic ID:
File:
Current date:
Relevant source IDs:

Tasks:
- identify stable principles that should remain,
- identify volatile claims that require current source verification,
- compare against official OpenAI/vendor docs first,
- list prose changes,
- list metadata changes,
- list index/register/deprecation updates,
- do not change exact pricing unless creating a dated pricing snapshot.
```

### Prompt pattern: source conflict resolution

```text
Resolve this source conflict for the Bible.

Claim:
Existing source:
New source:
Source types:
- official docs?
- official cookbook/use case?
- local reproduction?
- named expert?
- community report?
- speculation?

Decide:
- which source wins,
- whether the old claim is deprecated or narrowed,
- whether this is stable or volatile,
- what source-register and changelog changes are needed.
```

### Red flags to call out directly

- The maintainer updates prose but not metadata.
- The maintainer changes IDs without redirects.
- The maintainer removes obsolete content without deprecation trail.
- Pricing or plan details leak into stable chapters.
- A field practice is promoted without reproduction or strong source support.
- The source register contains duplicate ambiguous records.

### Exercises

Have the maintainer choose one volatile topic and fill this table:

```text
Topic ID:
Current claim:
Source checked:
Stable principle:
Volatile detail:
Action: keep / update / deprecate / split
Next review date:
```

<!-- VCB:END_SECTION id=vcb.chapter.maintaining_updating_bible.ai_coach -->

## Shortcut Reality


### The ideal practice

Update the Bible through metadata, sources, prose, indexes, changelog, validation, and editor review.

### What users often do instead

They patch the sentence that looked wrong and ignore the routing/source consequences.

### When the shortcut may be fine

Tiny typo fixes can be direct if they do not change meaning, sources, IDs, or routing.

### When the shortcut is a bad idea

It is a bad idea when the change affects:

- Codex product behavior;
- pricing, usage, or plan details;
- security guidance;
- shortcut risk labels;
- topic IDs;
- source evidence levels;
- indexes or related topics.

### Risk profile

- Probability of failure: high when metadata is skipped.
- Impact if it fails: medium for isolated prose; high for source/register/index drift.
- Ease of recovery: medium if changelog exists; low if obsolete content was silently removed.
- Blast radius: repository-wide for manifest/index/source-register errors.
- Hidden cost: future AI coaches retrieve stale or wrong guidance.

### Minimum guardrails

- Update frontmatter before prose.
- Update source register when evidence changes.
- Update indexes when IDs/routes change.
- Add deprecation records for replaced guidance.
- Run validator.
- Stop at editor review.

### Recovery plan

If an update caused drift:

1. Identify mismatched IDs, source records, or metadata.
2. Restore the last clean route if needed.
3. Add redirects/deprecation notes if an ID changed.
4. Re-run validation.
5. Add changelog note explaining the correction.

### AI coach guidance

Say:

```text
This is not just a wording edit. It changes source status/routing. Update metadata and indexes first, then prose.
```


## Budget and Constraint Notes


### Cheapest reliable path

Review only topics due for review or touched by the current change. Do not re-audit the whole Bible every time.

### Fastest high-usage path

Use separate agents for source comparison, index drift detection, and prose editing, then integrate with one maintainer pass.

### Low-attention path

Low-attention updates should be report-only unless the change is typo-level. Product/source updates need human review.

### Production-quality path

For high-risk guidance, require official source verification, metadata update, deprecation trail, index update, validator pass, and editor approval.


## Stable Core


- Advice decays; metadata makes decay visible.
- Official Codex facts require official Codex sources.
- Deprecated guidance should point to replacement guidance.
- Indexes and manifest are source maps, not decorative files.
- Exact prices and limits belong in dated snapshots, not stable chapters.


## Volatile Surface


- Codex UI labels, command names, settings paths, maturity labels, and plan packaging.
- Model-specific reliability claims.
- Pricing, credits, and limits.
- Community tactics and undocumented behavior.
- Tool catalog pricing and feature availability.


## Obsolescence Watch


This chapter itself needs review when:

- the repository schema changes;
- official Codex docs change update/source-map conventions;
- `llms.txt` conventions materially change;
- the validator adds or removes required checks;
- pricing snapshot workflow changes.


## Evidence and Sources


- `vcb.blueprint.v1` — governing blueprint for update protocol, evidence ladder, stable/volatile separation, and chunk stop gate.
- `openai.codex.changelog` — official source for Codex product changes and review triggers.
- `openai.codex.feature_maturity` — official source for feature maturity labels and volatility interpretation.
- `openai.codex.llms_txt` and `openai.codex.llms_full` — official source-map patterns for LLM-ingestible docs.
- `openai.codex.use_cases.update_documentation` — official example source for keeping documentation aligned with source changes.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for repository update workflow; not external evidence.


## Related Topics


- `vcb.chapter.field_notes_unofficial_practices`
- `vcb.chapter.risk_managed_shortcuts`
- `vcb.chapter.how_to_use_this_bible`
- `vcb.chapter.prompt_library_to_team_workflow`
- `vcb.chapter.agents_md_operating_manual`
- `vcb.chapter.codex_playbooks`


<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.maintaining_updating_bible -->
