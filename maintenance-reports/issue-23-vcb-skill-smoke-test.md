---
id: vcb.maintenance.issue_23_vcb_skill_smoke_test
title: Issue 23 VCB Skill Smoke Test
artifact_type: maintenance_report
status: validation_passed
created_on: 2026-06-12
branch: refine-vcb-source-selection-policy
---

# Issue 23 VCB Skill Smoke Test

Issue: https://github.com/frnklfrwsr/vibe-coding-bible/issues/23

Related PR: https://github.com/frnklfrwsr/vibe-coding-bible/pull/22

Date: 2026-06-12

Branch: `refine-vcb-source-selection-policy`

## Scope

This report records the first real cross-project smoke test of the repo-local `$vcb-reference` skill added in PR #22. It does not integrate Issue #23 into VCB content, add a field-practice card, change field-practice status, or change the default contribution mode.

## Smoke-Test Assessment

The external project Codex agent mostly followed the intended VCB route:

- Activated the `$vcb-reference` skill.
- Classified the task as a contribution / field observation.
- Retrieved a narrow contribution route instead of ingesting the whole repository.
- Used `AI_START_HERE.md` -> `CONTRIBUTION_MODES.md` -> `CONTRIBUTING.md` -> `.github/ISSUE_TEMPLATE/usage-insight.yml`.
- Respected `VCB:STOP_RETRIEVAL` behavior by stopping after the needed contribution route.
- Did not upload raw private reports or project-sensitive details.
- Submitted Issue #23 as a sanitized `E4_COMMUNITY_FIELD_REPORT` usage insight.

## Refinement Needed

The agent first searched for a local VCB repository before using GitHub. That is acceptable when a fresh local clone is clearly available, but the skill and entryway should define source-selection behavior explicitly so future agents do not rely on stale local files.

This PR adds the policy that:

- `https://github.com/frnklfrwsr/vibe-coding-bible` is the canonical VCB repository.
- A local VCB clone may be used for fast retrieval only when it is clearly the VCB repo and reasonably current.
- If local VCB is missing, stale, dirty in governance or contribution files, or uncertain, agents should use the public GitHub repo.
- Public submissions should always target the canonical GitHub repo.
- If local and public versions disagree, public GitHub wins for contribution templates, governance files, and issue or PR destination.
- Agents should ask before posting when unsure.

## Recommendation

Leave Issue #23 open as a usage insight and possible workflow-pattern / field-practice candidate. It should remain `E4_COMMUNITY_FIELD_REPORT` evidence unless reproduced locally or supported by additional independent reports.

## Files Changed

- `.agents/skills/vcb-reference/SKILL.md`
- `AI_START_HERE.md`
- `USE_VCB_WITH_AI.md`
- `docs/use-with-ai.md`
- `docs/use-with-codex.md`
- `maintenance-reports/issue-23-vcb-skill-smoke-test.md`
- `manifest.json`
- `TREE.txt`

No substantive VCB topic, chapter, shortcut, tool, pricing, or field-practice content was changed.

## Validation

Baseline validation passed on synced `main` before this report and policy refinement:

```text
VCB validation passed
active chapter/topic files validated: 244
shortcut IDs registered: 98
tool IDs registered: 75
pricing snapshots active: 2
```

Post-change docs build passed:

```text
INFO    -  Documentation built in 0.79 seconds
```

Post-change validator passed:

```text
VCB validation passed
active chapter/topic files validated: 244
shortcut IDs registered: 98
tool IDs registered: 75
pricing snapshots active: 2
```
