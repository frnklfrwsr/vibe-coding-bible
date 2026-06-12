---
id: vcb.register.deprecations
title: DEPRECATION_REGISTER
artifact_type: register
version: 0.27.0-draft.chunk26
status: chunk_26_updated
created_on: 2026-06-08
last_verified: '2026-06-10'
next_review_due: '2026-07-10'
review_cadence: monthly
---

<!-- VCB:BEGIN_REGISTER id=vcb.register.deprecations version=0.27.0-draft.chunk26 -->

# DEPRECATION_REGISTER

**Purpose:** Preserve obsolete guidance with migration notes instead of silently deleting it.

## Active Deprecations

No authored topic cards are deprecated in Chunk 26. This register now also records redirected planned aliases so retrieval does not route to stale placeholder IDs when an active canonical card exists.


## Shortcut Alias Redirects Hardened in Chunk 26

These are not deprecated authored cards. They are planned aliases, near-duplicates, or old search terms that must resolve to the active canonical route shown here.

| Redirected / planned alias | Active canonical route | Reason |
|---|---|---|
| `vcb.shortcut.using_global_config_for_everything` | `vcb.shortcut.default_config_forever` | active card covers default/config convenience risk |
| `vcb.shortcut.parallel_agents_same_files` | `vcb.shortcut.many_ais_same_files` | active card covers multi-AI same-file ownership risk |
| `vcb.shortcut.parallel_tasks_same_files` | `vcb.shortcut.parallel_agents_edit_same_files` | active card covers overlapping parallel-agent file edits |
| `vcb.shortcut.ai_answer_shopping` | `vcb.shortcut.best_of_n_without_review` | active card covers best-of-N answer selection without review |
| `vcb.shortcut.model_consensus` | `vcb.shortcut.consensus_as_correctness` | active card covers AI agreement misread as correctness |
| `vcb.shortcut.ai_estimate_trust` | `vcb.shortcut.trusting_estimates_before_inspection` | active card covers estimates accepted before inspection |
| `vcb.shortcut.model_bias_blindness` | `vcb.shortcut.ignoring_model_biases` | active card covers model-bias blind spots |
| `vcb.shortcut.unbounded_cloud_delegation` | `vcb.shortcut.unattended_cloud_delegation` | active card covers unbounded unattended cloud delegation |
| `vcb.shortcut.background_handoff_risk` | `vcb.shortcut.cloud_task_without_context` | active card covers poor cloud/background handoff context |
| `vcb.shortcut.parallel_conflict` | `vcb.shortcut.conflicting_parallel_agents` | active card covers parallel-agent conflict |
| `vcb.shortcut.parallel_write_conflicts` | `vcb.shortcut.conflicting_parallel_agents` | active card covers write-conflict coordination |
| `vcb.shortcut.background_full_access` | `vcb.shortcut.full_access_automation` | active card covers excessive background/full-access automation |
| `vcb.shortcut.unattended_gui_work` | `vcb.shortcut.browser_clicking_without_repro` | active card covers unsupervised GUI work without repro/evidence |
| `vcb.shortcut.browser_use_with_secrets` | `vcb.shortcut.logged_in_browser_secrets` | active card covers signed-in browser/secret exposure risk |
| `vcb.shortcut.screenshot_only_verification` | `vcb.shortcut.browser_clicking_without_repro` | active card covers GUI/browser verification by exact repro, not screenshots alone |

## Reserved Redirects From Chunk 0 Namespace Cleanup

These redirects prevent planned index drift from becoming future retrieval ambiguity. Every row in this table must be backed by `manifest.topic_namespace_policy.topic_id_redirects`; no row may redirect an ID to itself.

| Old / drift ID | Replacement ID | Reason |
|---|---|---|
| `vcb.shortcuts.risk_managed_shortcuts` | `vcb.register.shortcuts` | plural shortcut namespace routes to the shortcut register |
| `vcb.shortcuts.shortcut_register` | `vcb.register.shortcuts` | plural shortcut namespace routes to the shortcut register |
| `vcb.shortcuts.skipping_tests` | `vcb.shortcut.skipping_tests` | canonical shortcut namespace is singular |
| `vcb.shortcuts.broad_agent_permissions` | `vcb.shortcut.broad_agent_permissions` | canonical shortcut namespace is singular |
| `vcb.shortcuts.unattended_long_runs` | `vcb.shortcut.unattended_long_runs` | canonical shortcut namespace is singular |
| `vcb.shortcuts.accepting_looks_done` | `vcb.shortcut.accepting_looks_done` | canonical shortcut namespace is singular |
| `vcb.shortcuts.broad_refactor` | `vcb.shortcut.broad_refactor` | canonical shortcut namespace is singular |
| `vcb.shortcuts.context_dumping` | `vcb.shortcut.context_dumping` | canonical shortcut namespace is singular |
| `vcb.shortcuts.adding_dependencies_fast` | `vcb.shortcut.adding_dependencies_fast` | canonical shortcut namespace is singular |
| `vcb.shortcuts.reviewing_cloud_summary_only` | `vcb.shortcut.reviewing_cloud_summary_only` | canonical shortcut namespace is singular |
| `vcb.workflow.subagents` | `vcb.codex.subagents` | subagents are Codex feature topics |
| `vcb.security.secrets` | `vcb.safety.secrets` | security-sensitive guidance lives under safety namespace |
| `vcb.dependencies.no_new_deps` | `vcb.workflow.dependency_decisions` | dependency decisions are workflow topics |
| `vcb.review.diff_review` | `vcb.workflow.reviewing_diffs` | diff review is workflow guidance |
| `vcb.git.small_diffs` | `vcb.workflow.reviewing_diffs` | small-diff guidance routes to diff review workflow |
| `vcb.testing.regression_tests` | `vcb.workflow.testing` | testing is workflow guidance |

<!-- VCB:STOP_RETRIEVAL reason="deprecation_register_complete" -->
<!-- VCB:END_REGISTER id=vcb.register.deprecations -->
