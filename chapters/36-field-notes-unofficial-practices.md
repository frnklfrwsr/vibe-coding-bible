<!-- VCB:BEGIN_TOPIC id=vcb.chapter.field_notes_unofficial_practices version=0.1.1 -->
---
id: vcb.chapter.field_notes_unofficial_practices
title: "Chapter 36 — Field Notes: Unofficial and User-Discovered Codex Practices"
type: chapter
chapter_number: 36
version: 0.1.1
last_verified: '2026-06-11'
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
  community_field_practice: true
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
evidence_scope: policy framework; individual field practices use canonical labels such as E4_COMMUNITY_FIELD_REPORT, E2_REPRODUCED_LOCALLY, and E3_EXPERT_REPORT as labeled
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
- vcb.shortcut.unofficial_tools
- vcb.shortcut.trusting_external_tool_output
- vcb.shortcut.tool_sprawl_mcp
- vcb.shortcut.unattended_long_runs

durable_principles:
- Field practices are hypotheses until labeled and tested.
- Official docs win for product behavior.
- Local evidence wins for local repo truth.

likely_to_change:
- community reports
- undocumented rituals
- model-specific tactics
- product UI mechanics

obsolete_when:
- Official Codex docs fully replace a tactic.
- Local reproduction fails repeatedly.
- The tactic depends on a removed product behavior.

related_topics:
- vcb.chapter.maintaining_updating_bible
- vcb.chapter.risk_managed_shortcuts
- vcb.chapter.agents_md_operating_manual
- vcb.chapter.skills_reusable_workflows
- vcb.chapter.failure_modes_codex_work
---

> Summary:
> Field practices are useful only when labeled. This chapter teaches how to treat unofficial Codex tactics as experiments instead of turning anecdotes into hidden best practices.

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

<!-- VCB:BEGIN_SECTION id=vcb.chapter.field_notes_unofficial_practices.human -->
## 1. For the Human: Plain-Language Concept


### What this means

Field practices are tactics people discover while using Codex in real projects. They are not the same thing as official guidance.

A field practice can be useful before it is officially documented. It can also be wrong, outdated, cargo-culted, or safe only in one repo. Treat it like a workshop tip, not a law of physics.

### The simple rule

Use this ladder:

```text
Official docs explain product behavior.
Local repo evidence explains your project.
Field reports suggest experiments.
Speculation goes on a watchlist.
```

If someone says, "Everyone is doing this with Codex," that is not enough. The useful question is:

```text
Can we test the tactic safely in this repo without risking real users, secrets, money, or production data?
```

### Field practice versus official guidance

| Claim type | What it means | How to use it |
|---|---|---|
| Official guidance | OpenAI or vendor documents the behavior | Use as the product-behavior anchor, but still check dates. |
| Official example | OpenAI or vendor shows a recipe | Treat as a supported example, not a universal law. |
| Reproduced locally | Bible maintainers tested it in a controlled repo | Use with stated limits. |
| Named expert report | A named practitioner explains the tactic publicly | Treat as practitioner advice. Test before standardizing. |
| Community field report | Anonymous/community report | Treat as anecdotal. Use only in low-risk experiments. |
| Speculation | Prediction or emerging hunch | Do not treat as advice yet. Watch for evidence. |

### Candidate field practices in this Bible

These are tracked as candidate practices, not official best practices:

| Candidate practice | Durable principle | Current posture |
|---|---|---|
| ChatGPT as PM, Codex as implementer | Separate product thinking from repo-aware implementation | candidate / anecdotal until reproduced |
| Fresh-agent review before commit | Independent review catches different mistakes | candidate / useful when diff risk is moderate or high |
| `AGENTS.md` first | Durable repo context reduces repeated prompting | supported in principle by official persistent-guidance docs; exact workflow still repo-specific |
| Context reset between unrelated tasks | Old assumptions can pollute new work | candidate / treat as context hygiene |
| Skeleton/TODO-first workflow | Human constrains shape before agent fills details | candidate / useful for vague greenfield work |
| Strict typecheck/lint/test gates | Machine checks constrain fast code generation | stable engineering principle; exact gates are local |
| Greenfield vs production compatibility rule | Tell Codex whether backward compatibility matters | stable project-context principle |
| Lessons file / self-improvement loop | Repeated corrections should become durable guidance | partially overlaps with `AGENTS.md`, skills, and config |
| Multi-agent review/consensus | Independent perspectives can find different failures | useful only when scoped; expensive and noisy if overused |

### How to test a field practice safely

Use the smallest safe experiment:

1. Pick one low-risk task.
2. Commit before the experiment.
3. State what success would look like.
4. Run the practice once.
5. Compare against a normal workflow.
6. Record what improved, what got worse, and what was repo-specific.
7. Do not promote it unless it repeats.

### What bad looks like

Bad field-practice adoption sounds like:

```text
A Reddit thread said to always clear context, so I reset every task even when Codex already has useful state.
```

or:

```text
A YouTube video said to run five agents in parallel, so I did that on production auth code.
```

The problem is not that the tactic is always false. The problem is that the user skipped evidence, risk, and fit.

### What good looks like

Good field-practice adoption sounds like:

```text
This is an anecdotal practice. We will try it on a small branch, compare the diff quality, and record whether it helped. It does not become repo guidance unless it works twice and does not add new risk.
```

<!-- VCB:END_SECTION id=vcb.chapter.field_notes_unofficial_practices.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.field_notes_unofficial_practices.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human


### Teaching objective

Teach the human to use field practices as testable hypotheses. Do not let unofficial tactics become hidden law.

### Diagnose the human's current model

Ask:

- Where did this tactic come from?
- Is it official docs, a named practitioner, community anecdote, or speculation?
- What exact behavior is the tactic supposed to improve?
- Can we test it in a disposable branch or low-risk task?
- What would make us stop using it?

### Explanation strategy

Use a lab metaphor:

> A field practice is a lab note from another team. It may be valuable, but you still have to run the experiment in your environment.

Separate three layers:

1. **Product behavior:** what Codex officially supports.
2. **Engineering principle:** the durable reason a tactic might work.
3. **Local ritual:** the exact steps users copy.

The local ritual is usually the most volatile part.

### Useful metaphors

- **Trail map:** field reports show where someone else found a path; they do not guarantee the bridge is still there.
- **Folk medicine:** some folk remedies work; some are superstition. Test before prescribing.
- **Lab notebook:** useful observations need conditions, date, expected effect, and result.

### Coaching tactics

When the user cites a field practice, label it immediately:

```text
Evidence label: E4_COMMUNITY_FIELD_REPORT for the practice ritual unless the exact practice has qualifying E2_REPRODUCED_LOCALLY or E3_EXPERT_REPORT evidence. E0_OFFICIAL_DOCS can support product mechanics or principles, but it does not automatically promote a community ritual.
```

Then convert it into an experiment:

```text
Let's test this on one small task. Success means smaller diff, fewer corrections, or better verification. If it does not improve one of those, we do not promote it.
```

### Prompt pattern: field-practice assessment

```text
Assess this Codex field practice before I adopt it.

Practice:
[describe tactic]

Source:
[official docs / named expert / community report / unknown]

Project context:
[prototype / personal tool / production / security-sensitive]

Evaluate:
- evidence label,
- durable principle if any,
- volatile ritual,
- safest way to test it,
- blast radius,
- recoverability,
- when to reject it,
- whether it belongs in AGENTS.md, a skill, a hook, or nowhere yet.
```

### Red flags to call out directly

- The user treats an anonymous post as official product behavior.
- The tactic asks for broad permissions, real secrets, or production access.
- The tactic makes Codex more autonomous without adding review or recovery.
- The tactic adds process but does not reduce repeated mistakes.
- The practice worked once, but the user wants to encode it permanently.

### Exercises

Have the human pick one candidate practice and classify it:

```text
Source type:
Evidence level:
Risk level:
Expected benefit:
Safe experiment:
Promotion rule:
Obsolescence trigger:
```

<!-- VCB:END_SECTION id=vcb.chapter.field_notes_unofficial_practices.ai_coach -->

## Shortcut Reality


### The ideal practice

Use official docs for product behavior, local evidence for repo behavior, and field practices only as labeled experiments.

### What users often do instead

Users copy a tactic because it sounds clever, recent, or widely repeated.

### When the shortcut may be fine

It may be fine when:

- the task is a disposable prototype;
- the repo is local-only;
- the practice is reversible;
- the experiment is isolated in a branch/worktree;
- no real secrets, users, money, or production data are involved.

### When the shortcut is a bad idea

It is a bad idea when:

- the tactic changes permissions, networking, dependencies, CI, deployment, auth, payments, or data handling;
- the user cannot explain why it should work;
- the source is anonymous and unreproduced;
- the tactic makes review harder;
- failure would be hard to detect.

### Risk profile

- Probability of failure: medium for untested tactics.
- Impact if it fails: low in throwaway repos; high in production or security-sensitive systems.
- Ease of recovery: high if branch/commit exists; low if it affects secrets, data, or CI credentials.
- Blast radius: depends on environment and permissions.
- Skill needed to recover: low for prompt/process mistakes; high for dependency/security/production mistakes.
- Hidden cost: cargo-cult process that wastes future Codex usage.

### Minimum guardrails

- Label the evidence level.
- Test on one low-risk task.
- Commit first.
- Keep the experiment out of production.
- Record result and conditions.
- Do not promote after one lucky success.

### Recovery plan

If a field practice creates bad output:

1. Stop the tactic.
2. Inspect the diff.
3. Revert or isolate the branch.
4. Record why it failed.
5. Add a deprecation/watch note if the tactic was in guidance.

### AI coach guidance

Do not argue that unofficial practices are useless. That is false. Say:

```text
This may be useful, but right now it is a hypothesis. Let's test it with a small blast radius before turning it into repo policy.
```


## Budget and Constraint Notes


### Cheapest reliable path

Do not chase every new tactic. Use field practices only when they solve a repeated friction point.

### Fastest high-usage path

High-throughput users may test multiple practices in parallel, but each test needs isolated branches/worktrees and a comparison standard.

### Low-attention path

Do not adopt new field practices in low-attention mode unless they are read-only, report-only, or already reproduced locally.

### Production-quality path

Field practices must pass evidence labeling, local reproduction or strong named-source support, and explicit risk review before they become production repo guidance.


## Stable Core


- Official docs win for product behavior.
- Local repo tests win for local truth.
- Community tactics are hypotheses until labeled and tested.
- Durable principles should be separated from volatile rituals.
- Practices need obsolescence triggers.


## Volatile Surface


- Current Codex UI or command rituals.
- Model-specific prompting incantations.
- Unofficial wrapper/tool tactics.
- Community claims about rate limits, model routing, or hidden behaviors.
- Exact context reset, memory, and compaction rituals.


## Obsolescence Watch


Review a field practice when:

- official Codex docs add or remove a related feature;
- a changelog contradicts the tactic;
- a practice stops reproducing locally;
- the tactic depends on UI behavior, model behavior, or undocumented side effects;
- multiple independent reports converge or diverge.


## Evidence and Sources


- `vcb.blueprint.v1` — governing blueprint for field-practice policy, candidate practices, evidence labels, and community-source caveats.
- `openai.codex.best_practices` — official source for reusable guidance, planning, validation, and turning repeated patterns into durable project guidance.
- `openai.codex.customization` — official source supporting the feedback-loop pattern of capturing repeated corrections in durable guidance.
- `openai.codex.use_cases.reusable_codex_skills` — official example source for turning repeated workflows into skills.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis for field-practice triage; not external evidence.

Community field practices in this chapter remain candidate practices unless later tied to named sources, independent reports, or local reproduction.


## Related Topics


- `vcb.chapter.maintaining_updating_bible`
- `vcb.chapter.risk_managed_shortcuts`
- `vcb.chapter.agents_md_operating_manual`
- `vcb.chapter.skills_reusable_workflows`
- `vcb.chapter.failure_modes_codex_work`
- `vcb.concepts.blast_radius`
- `vcb.concepts.recoverability`


<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.field_notes_unofficial_practices -->
