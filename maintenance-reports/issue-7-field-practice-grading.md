---
id: vcb.maintenance.issue_7_field_practice_grading
title: Issue 7 Field-Practice Grading
artifact_type: maintenance_report
status: validation_passed
created_on: 2026-06-12
branch: issue-7-field-practice-grading
---

# Issue 7 Field-Practice Grading

Issue: https://github.com/frnklfrwsr/vibe-coding-bible/issues/7

Date: 2026-06-12

Branch: `issue-7-field-practice-grading`

## Method

- Reviewed `FIELD_PRACTICES.md`, all nine cards under `topics/field-practices/`, source IDs in `SOURCE_REGISTER.md`, current LLM routes, indexes, docs navigation, manifest live inventory, and validator expectations.
- Reused existing source IDs; no new external source IDs were introduced.
- Checked official OpenAI/Codex source anchors as mechanics or principle support only. They do not automatically promote community rituals into official VCB guidance.
- Claimed `reproduced` only where the result is bounded to this repository workflow: PR #18 independent Codex Review and the VCB validator gate.
- Preserved historical Final Release 1 package records; live post-release status counts are tracked separately.

## Status Table

| Field practice | Prior status | New status | Evidence level | Reproduction status | Official-doc support | Community support | Risk notes | Action |
|---|---|---|---|---|---|---|---|---|
| ChatGPT PM -> Codex implementer | candidate | needs_more_evidence | E4_COMMUNITY_FIELD_REPORT | Not reproduced; broad cross-surface workflow was not bounded enough for a local claim | `openai.help.chatgpt_capabilities`, `openai.codex.best_practices`, `openai.codex.overview` support mechanics/principles only | Maintainer synthesis and community field-practice posture | Plan drift, model-routing guesswork, stale assumptions | Updated status and caveat; no promotion |
| Fresh-agent review | candidate | reproduced | E2_REPRODUCED_LOCALLY | Bounded local reproduction: PR #18 Codex Review independently found an actionable validator issue | `openai.codex.github_review`, `openai.codex.use_cases.github_code_reviews`, `openai.help.truthfulness` support review mechanics and caution | Community field-practice posture remains relevant | Review theater if treated as approval | Updated status to reproduced with bounded note; no promotion |
| Context reset between tasks | candidate | candidate | E4_COMMUNITY_FIELD_REPORT | Not reproduced in a controlled prompt comparison | `openai.codex.prompting`, `openai.codex.subagent_concepts`, `openai.codex.best_practices` support context mechanics/principles | Maintainer synthesis and community field-practice posture | Context loss if reset lacks a handoff packet | Kept candidate; added audit note |
| AGENTS.md first | candidate | candidate | E4_COMMUNITY_FIELD_REPORT | Not reproduced in a controlled AGENTS.md comparison | `openai.codex.agents_md`, `openai.codex.best_practices`, `openai.codex.customization` support AGENTS.md mechanics/principles | Maintainer synthesis and community field-practice posture | Stale or overstuffed durable guidance | Kept candidate; added audit note |
| Skeleton/TODO first | candidate | candidate | E4_COMMUNITY_FIELD_REPORT | Not reproduced in comparable project slice | `openai.codex.best_practices`, `openai.codex.prompting` support constraints/planning principles only | Maintainer synthesis and community field-practice posture | Fake completeness if TODOs are not verified | Kept candidate; added audit note |
| Strict typecheck/lint gates | candidate | reproduced | E2_REPRODUCED_LOCALLY | Bounded local reproduction: VCB validator gate is a machine-verifiable check run before and after changes | `openai.codex.best_practices`, `github.docs.actions_ci`, `typescript.docs.basic_types`, `eslint.docs.latest`, `jest.docs_getting_started` support check mechanics | Community field-practice posture remains relevant | Check theater if gates are noisy or mis-scoped | Updated status to reproduced with bounded note; no promotion |
| Greenfield vs production rule | candidate | candidate | E4_COMMUNITY_FIELD_REPORT | Not reproduced in controlled prompt comparison | `openai.codex.best_practices`, `openai.codex.prompting` support prompt constraints/principles only | Maintainer synthesis and community field-practice posture | Wrong-phase assumptions can under-review production work | Kept candidate; added audit note |
| Lessons file loop | candidate | candidate | E4_COMMUNITY_FIELD_REPORT | Not reproduced as a durable-loop outcome | `openai.codex.agents_md`, `openai.codex.customization`, `openai.codex.skills`, `openai.codex.best_practices` support durable-guidance mechanics | Maintainer synthesis and community field-practice posture | Permanent stale process if not pruned | Kept candidate; added audit note |
| Multi-agent review/consensus | candidate | needs_more_evidence | E4_COMMUNITY_FIELD_REPORT | Not reproduced; no controlled single-review baseline comparison | `openai.codex.subagents`, `openai.codex.subagent_concepts`, `openai.help.truthfulness` support mechanics/cautions only | Maintainer synthesis and community field-practice posture | Consensus-as-correctness and duplicated blind spots | Updated status and caveat; no promotion |

## Evidence Summary

- Reproduced: `vcb.field.fresh_agent_review`, `vcb.field.strict_typecheck_lint_gates`.
- Candidate: `vcb.field.context_reset_between_tasks`, `vcb.field.agents_md_first`, `vcb.field.skeleton_todo_first`, `vcb.field.greenfield_vs_production_rule`, `vcb.field.lessons_file_loop`.
- Needs more evidence: `vcb.field.chatgpt_pm_codex_implementer`, `vcb.field.multi_agent_review_consensus`.
- Promoted: none.
- Deferred: none.
- Retired: none.

No community practice was promoted to official best practice.

## Reproduction And Verification Notes

- Fresh-agent review is reproduced only in the bounded PR-review sense: PR #18 received an independent Codex Review comment that identified a real validator/status-count issue, which was fixed before merge.
- Strict typecheck/lint gates are reproduced only in the bounded VCB sense: the repository validator is a machine-verifiable check used before and after metadata changes. This does not prove every project lint/typecheck stack is reliable.
- The remaining seven practices either stayed candidate or moved to needs_more_evidence because this audit did not include controlled comparisons, repeated trials, or independent named-practitioner evidence for the exact ritual.

## Files Changed

- `FIELD_PRACTICES.md`
- `README.md`
- `docs/navigation/field-practices.md`
- `indexes/*.md` field-practice routes
- `llms.txt`
- `llms-full.txt`
- `topics/field-practices/*.md`
- `manifest.json`
- `TREE.txt`
- `maintenance-reports/issue-7-field-practice-grading.md`

## Validator Result

Passed on 2026-06-12:

```text
VCB validation passed
active chapter/topic files validated: 244
shortcut IDs registered: 98
tool IDs registered: 75
pricing snapshots active: 1
```

## Follow-Up Issues Needed

- None required for this audit.
- Future promotion would require controlled local comparisons, repeated reproduction, or named independent practitioner evidence for the exact practice.

AUTHOR_STATUS: READY_FOR_PR
