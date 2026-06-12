---
id: vcb.repo.root
title: The Vibe Coding Bible
artifact_type: repository_root
version: 1.0.0-final.1.chunk44
status: chunk_44_updated
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: monthly
---

<!-- VCB:BEGIN_REPOSITORY_ROOT id=vcb.repo.root version=1.0.0-final.1.chunk44 -->

# The Vibe Coding Bible

**Status:** living Markdown source package.  
**Canonical review package:** one timestamped authoritative zip.  
**Primary readers:** humans building software with Codex, and AI coaches helping those humans use Codex safely and effectively.

## What This Repository Is

The Vibe Coding Bible is an AI-native, human-readable knowledge base for vibe coders using Codex. The source is modular, indexed, source-aware, and review-gated.

The durable thesis:

> Vibe coding works when speed is wrapped in an engineering control loop: intent, context, plan, patch, verification, review, recovery, and durable learning.

## Current Chunk

**Chunk ID:** `chunk_44_final_release_packaging`  
**Scope:** packaging-only final-release artifact creation and verification from approved Release Candidate 1 revision 2.  
**Final-release status:** this package is **Final Release 1** produced from the approved RC gate.  
**Explicit non-scope:** no new tool cards, field-practice cards, shortcut cards, pricing snapshots, broad workflow expansion, broad security/secrets expansion, broad tool-catalog expansion, source-map migration, or narrative chapters.

## Retrieval Rules

1. Prefer atomic topic cards over long chapters when both exist.
2. Use indexes to route to the smallest useful file.
3. Stop at `VCB:STOP_RETRIEVAL` unless the user explicitly needs related topics.
4. Treat Codex product details, exact commands, pricing, limits, UI labels, and model advice as volatile unless confirmed against current official sources.
5. Treat internal maintainer synthesis as synthesis, not as `E3_EXPERT_REPORT` evidence.

## Primary Entry Points

| Need | Start here |
|---|---|
| Machine-readable source map | `manifest.json` |
| Human overview | `README.md` |
| LLM routing | `llms.txt` |
| Source/evidence rules | `SOURCE_REGISTER.md` |
| Topic authoring rules | `AUTHORING_PROTOCOL.md` |
| Editor gate rules | `EDITORIAL_PROTOCOL.md` |
| Shortcut layer | `SHORTCUT_REGISTER.md`, `indexes/INDEX_BY_SHORTCUT.md` |
| Tool layer | `TOOL_REGISTER.md`, `indexes/INDEX_BY_TOOL_CATEGORY.md` |

## Public Repository Support

Licensing and contribution rules are documented in `LICENSE.md`, `LICENSE-CODE.md`, `NOTICE.md`, `CONTRIBUTING.md`, and `SECURITY.md`.

## Human-Readable Docs Site

A minimal GitHub Pages site is configured at `mkdocs.yml` and `docs/` to provide reader-friendly navigation for humans.

The GitHub Markdown repository remains the canonical source of truth. The docs site links back to canonical source files rather than duplicating the full VCB corpus.

## Active Chapters

| Chapter | ID | File |
|---|---|---|
| 0 | `vcb.chapter.how_to_use_this_bible` | `chapters/00-how-to-use-this-bible.md` |
| 1 | `vcb.chapter.codex_mental_model` | `chapters/01-codex-mental-model.md` |
| 2 | `vcb.chapter.vibe_coder_advantage_and_risk` | `chapters/02-vibe-coder-advantage-and-risk.md` |
| 3 | `vcb.chapter.codex_surfaces` | `chapters/03-codex-surfaces.md` |
| 4 | `vcb.chapter.installing_and_configuring_codex` | `chapters/04-installing-and-configuring-codex.md` |
| 5 | `vcb.chapter.sandboxing_and_approvals` | `chapters/05-sandboxing-and-approvals.md` |
| 6 | `vcb.chapter.git_discipline` | `chapters/06-git-discipline.md` |
| 7 | `vcb.chapter.four_part_prompt` | `chapters/07-four-part-prompt.md` |
| 8 | `vcb.chapter.plan_first_code_second` | `chapters/08-plan-first-code-second.md` |
| 9 | `vcb.chapter.context_management` | `chapters/09-context-management.md` |
| 10 | `vcb.chapter.acceptance_criteria` | `chapters/10-acceptance-criteria.md` |
| 11 | `vcb.chapter.understanding_unknown_codebase` | `chapters/11-understanding-an-unknown-codebase.md` |
| 12 | `vcb.chapter.feature_slicing` | `chapters/12-building-feature-small-slices.md` |
| 13 | `vcb.chapter.debugging_with_reproduction` | `chapters/13-debugging-with-reproduction.md` |
| 14 | `vcb.chapter.writing_updating_tests` | `chapters/14-writing-updating-tests.md` |
| 15 | `vcb.chapter.frontend_work` | `chapters/15-frontend-work.md` |
| 16 | `vcb.chapter.refactoring_without_breaking_everything` | `chapters/16-refactoring-without-breaking-everything.md` |
| 17 | `vcb.chapter.dependency_package_framework_decisions` | `chapters/17-dependency-package-framework-decisions.md` |
| 18 | `vcb.chapter.agents_md_operating_manual` | `chapters/18-agents-md.md` |
| 19 | `vcb.chapter.codex_config_defaults` | `chapters/19-codex-config.md` |
| 20 | `vcb.chapter.skills_reusable_workflows` | `chapters/20-skills-reusable-workflows.md` |
| 21 | `vcb.chapter.mcp_external_tools` | `chapters/21-mcp-external-tools.md` |
| 22 | `vcb.chapter.hooks_deterministic_guardrails` | `chapters/22-hooks-deterministic-guardrails.md` |
| 23 | `vcb.chapter.reviewing_codex_output` | `chapters/23-reviewing-codex-output-like-senior-engineer.md` |
| 24 | `vcb.chapter.github_pr_review_with_codex` | `chapters/24-github-pr-review-with-codex.md` |
| 25 | `vcb.chapter.security_for_vibe_coders` | `chapters/25-security-for-vibe-coders.md` |
| 26 | `vcb.chapter.ci_noninteractive_github_actions` | `chapters/26-ci-non-interactive-codex-github-actions.md` |
| 27 | `vcb.chapter.cloud_delegation_parallel_work` | `chapters/27-cloud-delegation-parallel-work.md` |
| 28 | `vcb.chapter.subagents_parallel_thinking` | `chapters/28-subagents-parallel-thinking.md` |
| 29 | `vcb.chapter.automations_recurring_work` | `chapters/29-automations-recurring-work.md` |
| 30 | `vcb.chapter.computer_use_browser_gui_tasks` | `chapters/30-computer-use-browser-gui-tasks.md` |
| 31 | `vcb.chapter.prompt_library_to_team_workflow` | `chapters/31-from-prompt-library-to-team-workflow.md` |
| 32 | `vcb.chapter.failure_modes_codex_work` | `chapters/32-failure-modes-codex-work-goes-wrong.md` |
| 33 | `vcb.chapter.codex_playbooks` | `chapters/33-codex-playbooks.md` |
| 34 | `vcb.chapter.first_serious_app` | `chapters/34-building-first-serious-app-with-codex.md` |
| 35 | `vcb.chapter.senior_engineer_checklist` | `chapters/35-senior-engineer-checklist.md` |
| 36 | `vcb.chapter.field_notes_unofficial_practices` | `chapters/36-field-notes-unofficial-practices.md` |
| 37 | `vcb.chapter.maintaining_updating_bible` | `chapters/37-maintaining-and-updating-the-bible.md` |
| 38 | `vcb.chapter.risk_managed_shortcuts` | `chapters/38-risk-managed-shortcuts.md` |
| 39 | `vcb.chapter.choosing_codex_operating_mode` | `chapters/39-choosing-codex-operating-mode.md` |
| 40 | `vcb.chapter.budget_aware_codex_workflows` | `chapters/40-budget-aware-codex-workflows.md` |
| 41 | `vcb.chapter.build_phase_vs_maintenance_phase` | `chapters/41-build-phase-vs-maintenance-phase.md` |
| 42 | `vcb.chapter.tool_stack_catalog` | `chapters/42-tool-stack-catalog.md` |
| 43 | `vcb.chapter.cost_benefit_analysis` | `chapters/43-cost-benefit-analysis-for-vibe-coders.md` |
| 44 | `vcb.chapter.when_to_use_other_ais` | `chapters/44-when-to-use-other-ais-with-codex.md` |
| 45 | `vcb.chapter.what_codex_is_bad_at` | `chapters/45-what-codex-is-bad-at.md` |
| 46 | `vcb.chapter.model_biases_failure_biases_bad_estimates` | `chapters/46-model-biases-failure-biases-bad-estimates.md` |

## Active Concept Cards

- `vcb.concepts.diff` — `topics/concepts/diff.md`
- `vcb.concepts.blast_radius` — `topics/concepts/blast-radius.md`
- `vcb.concepts.recoverability` — `topics/concepts/recoverability.md`
- `vcb.concepts.rollback` — `topics/concepts/rollback.md`
- `vcb.concepts.git_branch` — `topics/concepts/git-branch.md`
- `vcb.concepts.pull_request` — `topics/concepts/pull-request.md`
- `vcb.concepts.api_basics` — `topics/concepts/api-basics.md`
- `vcb.concepts.frontend_backend` — `topics/concepts/frontend-backend.md`
- `vcb.concepts.database_schema` — `topics/concepts/database-schema.md`
- `vcb.concepts.authentication` — `topics/concepts/authentication.md`
- `vcb.concepts.authorization` — `topics/concepts/authorization.md`
- `vcb.concepts.state` — `topics/concepts/state.md`
- `vcb.concepts.async` — `topics/concepts/async.md`
- `vcb.concepts.dependency` — `topics/concepts/dependency.md`
- `vcb.concepts.test` — `topics/concepts/test.md`
- `vcb.concepts.typecheck` — `topics/concepts/typecheck.md`
- `vcb.concepts.lint` — `topics/concepts/lint.md`
- `vcb.concepts.migration` — `topics/concepts/migration.md`
- `vcb.concepts.environment_variable` — `topics/concepts/environment-variable.md`
- `vcb.concepts.build_step` — `topics/concepts/build-step.md`
- `vcb.concepts.ci` — `topics/concepts/ci.md`
- `vcb.concepts.feature_flag` — `topics/concepts/feature-flag.md`
- `vcb.concepts.observability` — `topics/concepts/observability.md`





## Active Codex Feature Cards

- `vcb.codex.app` — `topics/codex/app.md`
- `vcb.codex.cli` — `topics/codex/cli.md`
- `vcb.codex.ide_extension` — `topics/codex/ide-extension.md`
- `vcb.codex.cloud` — `topics/codex/cloud.md`
- `vcb.codex.github_review` — `topics/codex/github-review.md`
- `vcb.codex.config` — `topics/codex/config.md`
- `vcb.codex.agents_md` — `topics/codex/agents-md.md`
- `vcb.codex.skills` — `topics/codex/skills.md`
- `vcb.codex.mcp` — `topics/codex/mcp.md`
- `vcb.codex.hooks` — `topics/codex/hooks.md`
- `vcb.codex.automations` — `topics/codex/automations.md`
- `vcb.codex.subagents` — `topics/codex/subagents.md`
- `vcb.codex.computer_use` — `topics/codex/computer-use.md`
- `vcb.codex.feature_maturity` — `topics/codex/feature-maturity.md`
- `vcb.codex.changelog_monitoring` — `topics/codex/changelog-monitoring.md`

## Active Workflow and Prompting Topic Cards

- `vcb.prompting.four_part_prompt` — `topics/prompting/four-part-prompt.md`
- `vcb.prompting.acceptance_criteria` — `topics/prompting/acceptance-criteria.md`
- `vcb.prompting.plan_first` — `topics/prompting/plan-first.md`
- `vcb.prompting.context_management` — `topics/prompting/context-management.md`
- `vcb.workflow.unknown_codebase` — `topics/workflows/unknown-codebase.md`
- `vcb.workflow.feature_slicing` — `topics/workflows/feature-slicing.md`
- `vcb.workflow.bug_repro` — `topics/workflows/bug-repro.md`
- `vcb.workflow.testing` — `topics/workflows/testing.md`


## Active Review, Safety, and Verification Workflow Topic Cards

- `vcb.workflow.codex_output_review` — `topics/workflows/codex-output-review.md`
- `vcb.workflow.reviewing_diffs` — `topics/workflows/reviewing-diffs.md`
- `vcb.workflow.github_pr_review` — `topics/workflows/github-pr-review.md`
- `vcb.safety.security_review` — `topics/safety/security-review.md`
- `vcb.safety.secrets` — `topics/safety/secrets.md`
- `vcb.workflow.ci_triage` — `topics/workflows/ci-triage.md`
- `vcb.workflow.ci_noninteractive` — `topics/workflows/ci-noninteractive.md`
- `vcb.safety.production_red_lines` — `topics/safety/production-red-lines.md`

## Active Frontend, Refactor, Dependency, and Documentation Workflow Topic Cards

- `vcb.workflow.frontend_work` — `topics/workflows/frontend-work.md`
- `vcb.workflow.visual_qa` — `topics/workflows/visual-qa.md`
- `vcb.workflow.accessibility_review` — `topics/workflows/accessibility-review.md`
- `vcb.workflow.refactoring` — `topics/workflows/refactoring.md`
- `vcb.workflow.dependency_decisions` — `topics/workflows/dependency-decisions.md`
- `vcb.workflow.dependency_update_review` — `topics/workflows/dependency-update-review.md`
- `vcb.workflow.release_notes` — `topics/workflows/release-notes.md`
- `vcb.workflow.documentation_updates` — `topics/workflows/documentation-updates.md`

## Active Failure-Mode Topic Cards

- `vcb.failure.hallucinated_apis` — `topics/failure-modes/hallucinated-apis.md`
- `vcb.failure.context_pollution` — `topics/failure-modes/context-pollution.md`
- `vcb.failure.weakened_tests` — `topics/failure-modes/weakened-tests.md`
- `vcb.failure.broad_refactor_drift` — `topics/failure-modes/broad-refactor-drift.md`
- `vcb.failure.dependency_bloat` — `topics/failure-modes/dependency-bloat.md`
- `vcb.failure.ui_taste_gap` — `topics/failure-modes/ui-taste-gap.md`
- `vcb.failure.ci_false_confidence` — `topics/failure-modes/ci-false-confidence.md`
- `vcb.failure.done_claim_without_evidence` — `topics/failure-modes/done-claim-without-evidence.md`

## Active Constraint and Budget Topic Cards

- `vcb.constraints.operating_mode` — `Operating Mode` — `topics/constraints/operating-mode.md`
- `vcb.constraints.attention_budget` — `Attention Budget` — `topics/constraints/attention-budget.md`
- `vcb.constraints.usage_burn` — `Usage Burn` — `topics/constraints/usage-burn.md`
- `vcb.constraints.recovery_budget` — `Recovery Budget` — `topics/constraints/recovery-budget.md`
- `vcb.constraints.build_vs_maintenance` — `Build Vs Maintenance` — `topics/constraints/build-vs-maintenance.md`
- `vcb.constraints.production_quality` — `Production Quality Constraints` — `topics/constraints/production-quality-constraints.md`
- `vcb.constraints.scope_budget` — `Scope Budget` — `topics/constraints/scope-budget.md`
- `vcb.constraints.review_budget` — `Review Budget` — `topics/constraints/review-budget.md`



## Active Shortcut Harm-Reduction Topic Cards

- `vcb.shortcut.skipping_tests` — `Skipping Tests` — `topics/shortcuts/skipping-tests.md`
- `vcb.shortcut.accepting_looks_done` — `Accepting “Looks Done”` — `topics/shortcuts/accepting-looks-done.md`
- `vcb.shortcut.broad_agent_permissions` — `Broad Agent Permissions` — `topics/shortcuts/broad-agent-permissions.md`
- `vcb.shortcut.unattended_long_runs` — `Unattended Long Runs` — `topics/shortcuts/unattended-long-runs.md`
- `vcb.shortcut.broad_refactor` — `Broad Refactor` — `topics/shortcuts/broad-refactor.md`
- `vcb.shortcut.context_dumping` — `Context Dumping` — `topics/shortcuts/context-dumping.md`
- `vcb.shortcut.adding_dependencies_fast` — `Adding Dependencies Fast` — `topics/shortcuts/adding-dependencies-fast.md`
- `vcb.shortcut.reviewing_cloud_summary_only` — `Reviewing Cloud Summary Only` — `topics/shortcuts/reviewing-cloud-summary-only.md`


## Active Security and Permission Shortcut Cards

- `vcb.shortcut.production_console_computer_use` — `Production Console Computer Use` — `topics/shortcuts/production-console-computer-use.md`
- `vcb.shortcut.overbroad_ci_permissions` — `Overbroad CI Permissions` — `topics/shortcuts/overbroad-ci-permissions.md`
- `vcb.shortcut.long_lived_ci_secrets` — `Long-Lived CI Secrets` — `topics/shortcuts/long-lived-ci-secrets.md`
- `vcb.shortcut.real_secrets_in_prototype` — `Real Secrets in Prototype` — `topics/shortcuts/real-secrets-in-prototype.md`
- `vcb.shortcut.cloud_work_with_real_secrets` — `Cloud Work with Real Secrets` — `topics/shortcuts/cloud-work-with-real-secrets.md`
- `vcb.shortcut.full_access_automation` — `Full-Access Automation` — `topics/shortcuts/full-access-automation.md`
- `vcb.shortcut.unattended_mutation` — `Unattended Mutation` — `topics/shortcuts/unattended-mutation.md`
- `vcb.shortcut.always_allow_sensitive_apps` — `Always Allow Sensitive Apps` — `topics/shortcuts/always-allow-sensitive-apps.md`

## Active Setup, Configuration, and Process Shortcut Cards

- `vcb.shortcut.skipping_setup` — `Skipping Setup` — `topics/shortcuts/skipping-setup.md`
- `vcb.shortcut.default_config_forever` — `Default Config Forever` — `topics/shortcuts/default-config-forever.md`
- `vcb.shortcut.skipping_agents_md` — `Skipping AGENTS.md` — `topics/shortcuts/skipping-agents-md.md`
- `vcb.shortcut.overstuffing_agents_md` — `Overstuffing AGENTS.md` — `topics/shortcuts/overstuffing-agents-md.md`
- `vcb.shortcut.stale_agents_md` — `Stale AGENTS.md` — `topics/shortcuts/stale-agents-md.md`
- `vcb.shortcut.unofficial_tools` — `Unofficial Tools` — `topics/shortcuts/unofficial-tools.md`
- `vcb.shortcut.hook_overreach` — `Hook Overreach` — `topics/shortcuts/hook-overreach.md`
- `vcb.shortcut.trusting_external_tool_output` — `Trusting External Tool Output` — `topics/shortcuts/trusting-external-tool-output.md`

## Active Tool-Sprawl, Skill, and Reusable-Process Shortcut Topic Cards

- `vcb.shortcut.skill_overkill` — `topics/shortcuts/skill-overkill.md`
- `vcb.shortcut.skill_sprawl` — `topics/shortcuts/skill-sprawl.md`
- `vcb.shortcut.tool_sprawl` — `topics/shortcuts/tool-sprawl.md`
- `vcb.shortcut.tool_sprawl_mcp` — `topics/shortcuts/tool-sprawl-mcp.md`
- `vcb.shortcut.brittle_hooks` — `topics/shortcuts/brittle-hooks.md`
- `vcb.shortcut.process_overhead_for_tiny_project` — `topics/shortcuts/process-overhead-for-tiny-project.md`
- `vcb.shortcut.team_workflow_without_team` — `topics/shortcuts/team-workflow-without-team.md`
- `vcb.shortcut.copy_pasting_playbook_blindly` — `topics/shortcuts/copy-pasting-playbook-blindly.md`


## Active Multi-AI and Model-Bias Shortcut Topic Cards

- `vcb.shortcut.many_ais_same_files` — `topics/shortcuts/many-ais-same-files.md`
- `vcb.shortcut.parallel_agents_edit_same_files` — `topics/shortcuts/parallel-agents-edit-same-files.md`
- `vcb.shortcut.best_of_n_without_review` — `topics/shortcuts/best-of-n-without-review.md`
- `vcb.shortcut.cherry_picking_ai_answers` — `topics/shortcuts/cherry-picking-ai-answers.md`
- `vcb.shortcut.consensus_as_correctness` — `topics/shortcuts/consensus-as-correctness.md`
- `vcb.shortcut.trusting_estimates_before_inspection` — `topics/shortcuts/trusting-estimates-before-inspection.md`
- `vcb.shortcut.ignoring_model_biases` — `topics/shortcuts/ignoring-model-biases.md`
- `vcb.shortcut.model_routing_guesswork` — `topics/shortcuts/model-routing-guesswork.md`
- `vcb.shortcut.subagent_swarm` — `topics/shortcuts/subagent-swarm.md`

## Active Parallel Cloud and Automation Shortcut Topic Cards

- `vcb.shortcut.unattended_cloud_delegation` — `topics/shortcuts/unattended-cloud-delegation.md`
- `vcb.shortcut.ambiguous_cloud_task` — `topics/shortcuts/ambiguous-cloud-task.md`
- `vcb.shortcut.cloud_task_without_context` — `topics/shortcuts/cloud-task-without-context.md`
- `vcb.shortcut.parallel_cloud_sprawl` — `topics/shortcuts/parallel-cloud-sprawl.md`
- `vcb.shortcut.conflicting_parallel_agents` — `topics/shortcuts/conflicting-parallel-agents.md`
- `vcb.shortcut.automation_spam` — `topics/shortcuts/automation-spam.md`
- `vcb.shortcut.automation_mutation_without_review` — `topics/shortcuts/automation-mutation-without-review.md`
- `vcb.shortcut.browser_clicking_without_repro` — `topics/shortcuts/browser-clicking-without-repro.md`
- `vcb.shortcut.logged_in_browser_secrets` — `topics/shortcuts/logged-in-browser-secrets.md`

## Active Tool Cards

Canonical active tool-card inventory. Current catalog state: **52 active tool cards; 23 deferred/planned ecosystem IDs**. Use `TOOL_REGISTER.md` for register metadata and deferred/planned coverage; use semantic indexes for smallest-card routing. This section remains the canonical active inventory and should not be split back into generation-specific blocks.

### First-party OpenAI/Codex
- `tool.codex` — `topics/tool-catalog/codex.md` — repo-aware coding agent, implementation, review, cloud/local workflows.
- `tool.codex_app` — `topics/tool-catalog/codex-app.md` — desktop command-center surface for local projects, threads, review, worktrees, and automations.
- `tool.codex_cli` — `topics/tool-catalog/codex-cli.md` — terminal-native local Codex work, commands, scripting, and non-interactive entrypoint.
- `tool.codex_ide_extension` — `topics/tool-catalog/codex-ide-extension.md` — side-by-side IDE workflow with open-file/selection context and cloud delegation.
- `tool.codex_cloud` — `topics/tool-catalog/codex-cloud.md` — background cloud tasks, PR proposals, isolated high-throughput work.
- `tool.codex_github_review` — `topics/tool-catalog/codex-github-review.md` — GitHub PR review, automatic review, review guidelines.
- `tool.codex_exec` — `topics/tool-catalog/codex-exec.md` — non-interactive scripts and CI tasks.
- `tool.codex_worktrees` — `topics/tool-catalog/codex-worktrees.md` — parallel local/app tasks without disturbing active checkout.
- `tool.codex_subagents` — `topics/tool-catalog/codex-subagents.md` — parallel analysis, custom agents, specialist reports.
- `tool.codex_automations` — `topics/tool-catalog/codex-automations.md` — scheduled recurring tasks and findings inbox.
- `tool.codex_computer_use` — `topics/tool-catalog/codex-computer-use.md` — desktop app/browser/GUI operation and verification.
- `tool.codex_browser` — `topics/tool-catalog/codex-browser.md` — in-app browser preview, comments, browser verification.
- `tool.codex_chrome_extension` — `topics/tool-catalog/codex-chrome-extension.md` — signed-in Chrome browser tasks, website allowlists/blocklists, browser-history and account-context risk.
- `tool.codex_agents_md` — `topics/tool-catalog/codex-agents-md.md` — durable repo guidance and project operating manuals.
- `tool.codex_config` — `topics/tool-catalog/codex-config.md` — local/project/profile configuration defaults.
- `tool.codex_skills` — `topics/tool-catalog/codex-skills.md` — reusable workflow packages.
- `tool.codex_mcp` — `topics/tool-catalog/codex-mcp.md` — external tool and context connections.
- `tool.codex_hooks` — `topics/tool-catalog/codex-hooks.md` — deterministic lifecycle guardrails.
- `tool.codex_security` — `topics/tool-catalog/codex-security.md` — Codex Security plugin/cloud security review workflows, finding review, and reviewed fix preparation.
- `tool.codex_feature_maturity` — `topics/tool-catalog/codex-feature-maturity.md` — maturity-label governance for Codex feature reliability, fallback posture, and production-readiness review.
- `tool.codex_changelog_monitoring` — `topics/tool-catalog/codex-changelog-monitoring.md` — official Codex changelog monitoring for Bible maintenance, deprecation watch, and route/source refreshes.

### Repository, CI, dependency, and QA
- `tool.github` — `topics/tool-catalog/github.md` — version control, PRs, issues, code review, Actions integration.
- `tool.github_actions` — `topics/tool-catalog/github-actions.md` — CI workflows, secrets, token permissions, OIDC, Codex GitHub Action.
- `tool.github_dependabot` — `topics/tool-catalog/github-dependabot.md` — vulnerable dependency alerts and update PRs.
- `tool.npm` — `topics/tool-catalog/npm.md` — dependency manifests, install behavior, audit reports.
- `tool.playwright` — `topics/tool-catalog/playwright.md` — screenshot capture, visual comparisons, browser checks.
- `tool.vitest` — `topics/tool-catalog/vitest.md` — Vite-native unit/component tests, watch-mode feedback, test evidence, and CI-adjacent JavaScript verification.
- `tool.storybook` — `topics/tool-catalog/storybook.md` — component workshop, isolated UI states, component documentation, interaction tests, and design-handoff evidence.
- `tool.openssf_scorecard` — `topics/tool-catalog/openssf-scorecard.md` — dependency/project health and supply-chain risk signals.

### AI coding, AI IDE, and AI planning
- `tool.chatgpt` — `topics/tool-catalog/chatgpt.md` — product thinking, planning, explanation, PM-style prompt shaping, source-backed research, and data/document analysis.
- `tool.claude` — `topics/tool-catalog/claude.md` — independent architecture/review perspective, long-form explanation, and source-verified critique.
- `tool.cursor` — `topics/tool-catalog/cursor.md` — IDE-native coding assistance, local file editing, plan-first agent work, and diff review.
- `tool.github_copilot` — `topics/tool-catalog/github-copilot.md` — GitHub/IDE-native autocomplete, chat, repository-connected assistance, and agentic branch/PR workflows.
- `tool.windsurf` — `topics/tool-catalog/windsurf.md` — agentic AI IDE workflow, Cascade planning/editing, checkpoints, tool calls, and plugin support.

### Browser-dev, app-builder, and UI generation
- `tool.replit` — `topics/tool-catalog/replit.md` — browser-based prototyping, hosted development, learning apps, and quick demo publishing.
- `tool.lovable` — `topics/tool-catalog/lovable.md` — AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails.
- `tool.bolt` — `topics/tool-catalog/bolt.md` — browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails.
- `tool.v0` — `topics/tool-catalog/v0.md` — AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points.

### Hosting, backend/auth, payment, observability, and analytics
- `tool.vercel` — `topics/tool-catalog/vercel.md` — hosting, preview deployments, production deployment evidence, and environment separation.
- `tool.cloudflare` — `topics/tool-catalog/cloudflare.md` — DNS, CDN/security controls, Workers, Pages, edge deployment, and domain/routing evidence.
- `tool.netlify` — `topics/tool-catalog/netlify.md` — site deploys, deploy previews, functions, deploy contexts, and rollback/deployment evidence.
- `tool.supabase` — `topics/tool-catalog/supabase.md` — Postgres database, backend/auth/storage, RLS-aware app data, and MVP backend review.
- `tool.neon` — `topics/tool-catalog/neon.md` — serverless Postgres, database branches, preview database workflows, connection evidence, and migration review.
- `tool.clerk` — `topics/tool-catalog/clerk.md` — authentication, user management, sessions, organizations, and auth UI workflows.
- `tool.auth0` — `topics/tool-catalog/auth0.md` — IAM, OAuth/OIDC, applications/APIs, enterprise/B2B auth, and authorization architecture.
- `tool.stripe` — `topics/tool-catalog/stripe.md` — payments, subscriptions, checkout, webhooks, billing objects, and real-money state review.
- `tool.sentry` — `topics/tool-catalog/sentry.md` — error monitoring, tracing, performance, session replay, release evidence, and incident debugging.
- `tool.posthog` — `topics/tool-catalog/posthog.md` — product analytics, event taxonomy, session replay, feature flags, experiments, and product evidence.
- `tool.resend` — `topics/tool-catalog/resend.md` — transactional email API, sending-domain review, templates, delivery evidence, and notification workflows.

### Local dev, design, and project management
- `tool.docker` — `topics/tool-catalog/docker.md` — reproducible local services, Dockerfiles, Compose stacks, containerized dev/test environments, and isolation/rebuild evidence.
- `tool.figma` — `topics/tool-catalog/figma.md` — collaborative design files, components, prototypes, Dev Mode handoff, screenshots, and design-intent evidence.
- `tool.linear` — `topics/tool-catalog/linear.md` — issues, projects, teams, workflows, cycles, planning status, and product/team execution hygiene.


## Deferred Ecosystem Coverage

Chunk 40 confirms that the tool catalog is curated, not exhaustive. The following important ecosystem areas are intentionally tracked as deferred/planned or alias/companion routes in `TOOL_REGISTER.md`: Render, Railway, Fly.io, Firebase, AWS, GCP, Azure, DigitalOcean, Postmark, SendGrid, Mailgun, Notion, Google Docs, Jira, 1Password, Doppler, Infisical, Better Stack, Datadog, Paddle, Lemon Squeezy, Jest, and Cypress. Use active companion cards first until a future editor-approved chunk authors full cards or grouped category cards.

GitHub Issues routes through active `tool.github`; GitHub Secrets routes through active `tool.github_actions`; one-card-per-cloud-service coverage is explicitly excluded until a scoped cloud-service-family slice is approved.

## Final Release Package Status

Chunk 44 packages **Final Release 1** as a packaging-only artifact from approved Release Candidate 1 revision 2. This package does not add cards, pricing snapshots, broad workflow expansion, broad security/secrets expansion, broad tool-catalog expansion, source-map migration, or narrative chapters.

**Final release artifact:** `vibe-coding-bible-final-release-1-20260612T050000Z-authoritative.zip`  
**Approved source baseline:** `vibe-coding-bible-release-candidate-1-revision-2-20260612T040000Z-authoritative.zip`  
**Final release state:** final-release package produced from the approved RC gate; package acceptance remains subject to the active editor gate.

The final release preserves the documented limitations approved through the RC gate:

- exact non-OpenAI pricing snapshots remain deferred;
- the tool catalog is curated, not exhaustive: **52 active tool cards; 23 deferred/planned ecosystem IDs**;
- all nine field-practice retrieval cards remain candidate-only and are not promoted, reproduced, retired, or deprecated;
- changelog ordering follows the documented review-trail convention rather than strict newest-first chronological normalization.

Use `CHUNK_44_REPORT.md` for final-release packaging verification, package hygiene, and the final packaging result. Use `FINAL_RELEASE_1_INTEGRITY.md` for source-tree integrity verification. The final zip SHA-256 is external to the source tree by design; verify it against the author submission checksum or, when supplied, the external sidecar convention `vibe-coding-bible-final-release-1-20260612T050000Z-authoritative.zip.sha256`. `CHUNK_43_REPORT.md` and `RELEASE_CANDIDATE_1_INTEGRITY.md` remain historical records for the approved RC baseline.

## Post-Release Shortcut Audit Routes

This repository is the living source package. Issue #3 promoted eight high-priority shortcut cards after the original Final Release 1 package, so use the live source inventory for post-release routes while preserving `FINAL_RELEASE_1_INTEGRITY.md` as the historical package record.

- `vcb.shortcut.skipping_plan` - `topics/shortcuts/skipping-plan.md`
- `vcb.shortcut.one_big_prompt` - `topics/shortcuts/one-big-prompt.md`
- `vcb.shortcut.vague_prompt` - `topics/shortcuts/vague-prompt.md`
- `vcb.shortcut.accepting_diff_without_review` - `topics/shortcuts/accepting-diff-without-review.md`
- `vcb.shortcut.ignoring_lint_typecheck` - `topics/shortcuts/ignoring-lint-typecheck.md`
- `vcb.shortcut.coding_on_main` - `topics/shortcuts/coding-on-main.md`
- `vcb.shortcut.manual_testing_only` - `topics/shortcuts/manual-testing-only.md`
- `vcb.shortcut.debugging_without_repro` - `topics/shortcuts/debugging-without-repro.md`

## Active Field Practice Candidate Cards

These cards are active retrieval targets, but their practice status remains candidate. Do not present them as official best practice or as locally reproduced unless a later evidence review changes the status.

- `vcb.field.chatgpt_pm_codex_implementer` — `topics/field-practices/chatgpt-pm-codex-implementer.md` — active candidate: ChatGPT PM / Codex implementer split.
- `vcb.field.fresh_agent_review` — `topics/field-practices/fresh-agent-review.md` — active candidate: fresh independent agent/session diff review.
- `vcb.field.context_reset_between_tasks` — `topics/field-practices/context-reset-between-tasks.md` — active candidate: reset or summarize context between unrelated tasks.
- `vcb.field.agents_md_first` — `topics/field-practices/agents-md-first.md` — active candidate: minimal AGENTS.md early in durable repos.
- `vcb.field.skeleton_todo_first` — `topics/field-practices/skeleton-todo-first.md` — active candidate: human skeleton/TODOs before agent implementation.
- `vcb.field.strict_typecheck_lint_gates` — `topics/field-practices/strict-typecheck-lint-gates.md` — active candidate: typecheck/lint/test gates after agent changes.
- `vcb.field.greenfield_vs_production_rule` — `topics/field-practices/greenfield-vs-production-rule.md` — active candidate: explicit project phase and compatibility posture.
- `vcb.field.lessons_file_loop` — `topics/field-practices/lessons-file-loop.md` — active candidate: temporary lessons loop before durable guidance promotion.
- `vcb.field.multi_agent_review_consensus` — `topics/field-practices/multi-agent-review-consensus.md` — active candidate: multi-agent review with evidence, not consensus-as-proof.

## Chunk Gate

The author must stop after each chunk and wait for editor review. If the editor returns `CHANGES_REQUIRED`, revise only the current chunk.

## Next Chunk

Recommended next chunk after approval: `post_release_maintenance_requires_editor_scope`.

After Final Release 1, new work remains blocked until an editor provides a scoped post-release maintenance, errata, pricing-refresh, source-refresh, or content-expansion slice. Do not add cards, pricing snapshots, source-map migrations, broad workflow expansion, broad security/secrets expansion, broad tool-catalog expansion, or narrative chapters without explicit editor scope.

<!-- VCB:STOP_RETRIEVAL reason="repository_root_complete" -->
<!-- VCB:END_REPOSITORY_ROOT id=vcb.repo.root -->
