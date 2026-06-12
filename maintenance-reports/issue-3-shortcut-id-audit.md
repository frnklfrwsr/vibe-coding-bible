# Issue #3 Shortcut ID Audit

Issue: https://github.com/frnklfrwsr/vibe-coding-bible/issues/3

Date: 2026-06-12

Branch: `issue-3-shortcut-id-audit`

## Objective

Audit high-priority planned shortcut IDs and promote or consolidate the routes most likely to help vibe coders avoid common failure patterns.

This was a bounded shortcut-layer update. It did not rewrite narrative chapters, tool cards, field-practice cards, pricing snapshots, source-register doctrine, release tags, or GitHub workflow behavior.

## Selection Criteria

Selected IDs were prioritized by:

- usefulness to common vibe-coding behavior;
- frequency of the behavior in real AI-assisted work;
- blast radius when the shortcut goes wrong;
- recoverability after a mistake;
- whether VCB lacked an active standalone card;
- whether an existing active card already covered the route well enough.

## Disposition Table

| Shortcut ID | Disposition | Result |
| --- | --- | --- |
| `vcb.shortcut.skipping_plan` | `promote_to_active_card` | New active shortcut card. |
| `vcb.shortcut.one_big_prompt` | `promote_to_active_card` | New active shortcut card. |
| `vcb.shortcut.vague_prompt` | `promote_to_active_card` | New active shortcut card. |
| `vcb.shortcut.accepting_diff_without_review` | `promote_to_active_card` | New active shortcut card. |
| `vcb.shortcut.ignoring_lint_typecheck` | `promote_to_active_card` | New active shortcut card. |
| `vcb.shortcut.coding_on_main` | `promote_to_active_card` | New active shortcut card. |
| `vcb.shortcut.manual_testing_only` | `promote_to_active_card` | New active shortcut card. |
| `vcb.shortcut.debugging_without_repro` | `promote_to_active_card` | New active shortcut card. |
| `vcb.shortcut.editing_before_understanding` | `companion_route` | Keep planned; route now to `vcb.workflow.unknown_codebase`, `vcb.shortcut.skipping_setup`, and related context cards. |
| `vcb.shortcut.eyeballing_ui` | `companion_route` | Keep planned; route now to `vcb.workflow.visual_qa`, `vcb.failure.ui_taste_gap`, and `vcb.shortcut.browser_clicking_without_repro`. |
| `vcb.shortcut.skipping_pr_review` | `companion_route` | Keep planned; route now to `vcb.shortcut.accepting_diff_without_review` and `vcb.workflow.github_pr_review`. |
| `vcb.shortcut.skipping_security_review` | `companion_route` | Keep planned; route now to `tool.codex_security`, `vcb.safety.security_review`, and `vcb.safety.production_red_lines`. |
| `vcb.shortcut.generated_prototype_as_production_foundation` | `defer` | Needs a later production-boundary card; current companion routes remain `vcb.constraints.build_vs_maintenance`, `vcb.constraints.production_quality`, and `vcb.shortcut.real_secrets_in_prototype`. |
| `vcb.shortcut.buying_tools_as_progress` | `defer` | Needs a later tool-selection shortcut; current companion routes remain `vcb.shortcut.tool_sprawl`, `vcb.chapter.tool_stack_catalog`, and cost-benefit guidance. |

## New Cards Created

- `topics/shortcuts/skipping-plan.md`
- `topics/shortcuts/one-big-prompt.md`
- `topics/shortcuts/vague-prompt.md`
- `topics/shortcuts/accepting-diff-without-review.md`
- `topics/shortcuts/ignoring-lint-typecheck.md`
- `topics/shortcuts/coding-on-main.md`
- `topics/shortcuts/manual-testing-only.md`
- `topics/shortcuts/debugging-without-repro.md`

## Routing Updates

Updated shortcut routing surfaces so the new active cards are reachable from:

- `SHORTCUT_REGISTER.md`
- `indexes/INDEX_BY_SHORTCUT.md`
- `indexes/INDEX_BY_RISK_LEVEL.md`
- `indexes/INDEX_BY_RECOVERABILITY.md`
- `indexes/INDEX_BY_PROJECT_TYPE.md`
- `indexes/INDEX_BY_TASK.md`
- `indexes/INDEX_BY_FAILURE_MODE.md`
- `indexes/INDEX_FOR_AI_COACHES.md`
- `llms.txt`
- `llms-full.txt`

## Deferred Follow-Up

The next shortcut audit can consider full cards for:

- `vcb.shortcut.editing_before_understanding`
- `vcb.shortcut.eyeballing_ui`
- `vcb.shortcut.skipping_pr_review`
- `vcb.shortcut.skipping_security_review`
- `vcb.shortcut.generated_prototype_as_production_foundation`
- `vcb.shortcut.buying_tools_as_progress`
- `vcb.shortcut.using_existing_local_setup`

## Files Changed

Expected file categories:

- eight new shortcut cards;
- shortcut register and routing indexes;
- LLM routing files;
- manifest inventory updates;
- validator update only if required for post-release shortcut counts;
- this maintenance report.

## Validation

Repository validator result: passed on 2026-06-12.

Validator summary:

- active chapter/topic files validated: 244;
- shortcut IDs registered: 98;
- tool IDs registered: 75;
- pricing snapshots active: 1.
