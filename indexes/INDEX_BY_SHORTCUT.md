---
id: vcb.index.by_shortcut
title: INDEX_BY_SHORTCUT
artifact_type: index
version: 0.39.0-draft.chunk38
status: chunk_38_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-10'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_shortcut version=0.39.0-draft.chunk38 -->

# INDEX_BY_SHORTCUT

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Prompting/workflow shortcut control cards
- `vcb.prompting.four_part_prompt` → active: control for vague-prompt and one-big-prompt shortcuts
- `vcb.prompting.plan_first` → active: control for skipping-plan shortcuts
- `vcb.prompting.context_management` → active: control for context-dumping shortcuts
- `vcb.prompting.acceptance_criteria` → active: control for accepting-looks-done shortcuts
- `vcb.workflow.unknown_codebase` → active: control for editing-before-understanding shortcuts
- `vcb.workflow.feature_slicing` → active: control for broad feature/prototype shortcuts
- `vcb.workflow.bug_repro` → active: control for debugging-without-repro shortcuts
- `vcb.workflow.testing` → active: control for skipping-tests and manual-testing-only shortcuts

## Prompting and planning shortcuts
- `vcb.shortcut.vague_prompt` → active: shortcut risk: underspecified work orders that make Codex guess goal, context, constraints, or done evidence
- `vcb.shortcut.skipping_plan` → active: shortcut risk: broad or risky work started before files, checks, and rollback are named
- `vcb.shortcut.context_dumping` → active: shortcut risk: stale, excessive, or contradictory context
- `vcb.shortcut.accepting_looks_done` → active: shortcut risk: polished done claims without evidence
- `vcb.chapter.four_part_prompt` → active
- `vcb.chapter.plan_first_code_second` → active
- `vcb.chapter.acceptance_criteria` → active

## Verification shortcuts
- `vcb.shortcut.skipping_tests` → active: shortcut risk: skipped verification and hidden regressions
- `vcb.shortcut.browser_clicking_without_repro` → active: browser/GUI verification requires exact repro steps, expected/actual behavior, and evidence before relying on screenshots
- `vcb.shortcut.screenshot_only_verification` → planned future companion; active browser/GUI repro route is listed immediately above
- `vcb.shortcut.manual_testing_only` → active: shortcut risk: one-time manual checks without repeatable verification
- `vcb.shortcut.accepting_diff_without_review` → active: shortcut risk: accepting changed files without scope, risk, and evidence review
- `vcb.chapter.writing_updating_tests` → active
- `vcb.chapter.reviewing_codex_output` → active

## Git and review shortcuts
- `vcb.shortcut.coding_on_main` → active: shortcut risk: mutating the canonical branch without branch/worktree isolation
- `vcb.shortcut.skipping_pr_review` → planned future companion; active review routes are `vcb.shortcut.accepting_diff_without_review` and `vcb.workflow.github_pr_review`
- `vcb.shortcut.accepting_codex_review_as_approval` → planned
- `vcb.chapter.git_discipline` → active
- `vcb.chapter.github_pr_review_with_codex` → active

## Setup, permission, and automation shortcuts
- `tool.codex_security` → active: security tooling route before skipping-security-review or summary-only shortcuts

- `vcb.shortcut.automation_spam` → active: recurring automations must be actionable and quiet when nothing changed
- `vcb.shortcut.automation_mutation_without_review` → active: scheduled/noninteractive mutation needs branch-only review gates
- `vcb.shortcut.logged_in_browser_secrets` → active: signed-in browser/GUI work needs fake/staging accounts and scoped approvals
- `vcb.shortcut.browser_clicking_without_repro` → active: browser/GUI work needs exact repro steps and evidence
- `vcb.shortcut.using_existing_local_setup` → planned
- `vcb.shortcut.skipping_setup` → active: Skipping Setup shortcut guardrails
- `vcb.shortcut.broad_agent_permissions` → active: shortcut risk: excessive filesystem, command, network, or tool permissions
- `vcb.shortcut.overbroad_ci_permissions` → active: CI permissions should be explicit, least-privilege, and scoped to the workflow job
- `vcb.shortcut.long_lived_ci_secrets` → active: CI secrets should be short-lived, rotated, scoped, or federated where possible
- `vcb.shortcut.real_secrets_in_prototype` → active: prototypes should use fake/local/test credentials and synthetic data
- `vcb.shortcut.unattended_mutation` → active: write-capable unattended work requires branch isolation and human review
- `vcb.shortcut.full_access_automation` → active: full-access automation requires least-privilege defaults and review gates
- `vcb.shortcut.always_allow_sensitive_apps` → active: persistent approvals for sensitive apps/sites require tight scope and revocation paths
- `vcb.chapter.sandboxing_and_approvals` → active
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.shortcut.default_config_forever` → active: review config by task risk instead of keeping defaults forever
- `vcb.shortcut.using_global_config_for_everything` → planned future companion; active config-default route is listed immediately above
- `vcb.shortcut.hook_overreach` → active: keep hooks narrow, objective, and reviewable

## Feature, debugging, refactor, and dependency shortcuts
- `vcb.shortcut.one_big_prompt` → active: shortcut risk: oversized prompts that produce broad unreviewable diffs
- `vcb.shortcut.editing_before_understanding` → planned future companion; active first routes are `vcb.workflow.unknown_codebase` and `vcb.shortcut.skipping_setup`
- `vcb.shortcut.debugging_without_repro` → active: shortcut risk: patching before expected/actual evidence or a failing command/path exists
- `vcb.shortcut.broad_refactor` → active: shortcut risk: cleanup drifting into behavior change
- `vcb.shortcut.adding_dependencies_fast` → active: shortcut risk: package bloat and supply-chain drag
- `vcb.shortcut.framework_churn` → planned
- `vcb.chapter.feature_slicing` → active
- `vcb.chapter.debugging_with_reproduction` → active
- `vcb.chapter.refactoring_without_breaking_everything` → active
- `vcb.chapter.dependency_package_framework_decisions` → active

## Persistent guidance and tool shortcuts
- `vcb.shortcut.skipping_agents_md` → active: add minimal durable project guidance after repeated friction
- `vcb.shortcut.overstuffing_agents_md` → active: keep AGENTS.md concise and durable
- `vcb.shortcut.stale_agents_md` → active: prune stale instructions and commands
- `vcb.shortcut.default_config_forever` → active: review config by task risk instead of keeping defaults forever
- `vcb.shortcut.using_global_config_for_everything` → planned future companion; active config-default route is listed immediately above
- `vcb.shortcut.unofficial_tools` → active: vet external tools before enabling them
- `vcb.shortcut.trusting_external_tool_output` → active: verify MCP/tool output before treating it as evidence
- `vcb.shortcut.hook_overreach` → active: hooks should be narrow deterministic guardrails, not broad policy engines
- `vcb.shortcut.skill_overkill` → active: avoid turning one-off prompts into durable skills before the workflow repeats and has stable trigger conditions
- `vcb.shortcut.tool_sprawl_mcp` → active: limit MCP servers/tools to the smallest trusted set needed for the workflow
- `vcb.shortcut.brittle_hooks` → active: keep hooks narrow, deterministic, reviewable, and easy to bypass safely
- `vcb.chapter.agents_md_operating_manual` → active
- `vcb.chapter.skills_reusable_workflows` → active
- `vcb.chapter.mcp_external_tools` → active
- `vcb.chapter.hooks_deterministic_guardrails` → active

## Advanced agentic workflow shortcuts
- `vcb.shortcut.parallel_cloud_sprawl` → active: parallel cloud task sprawl needs task matrix, isolated branches, and integration owner
- `vcb.shortcut.conflicting_parallel_agents` → active: parallel agents need disjoint write scopes or one integrator
- `vcb.shortcut.unattended_cloud_delegation` → active: cloud/background work needs stop conditions and review packet
- `vcb.shortcut.unattended_mutation` → active: unattended write-capable work needs isolation, explicit stop conditions, and human review
- `vcb.shortcut.full_access_automation` → active: full-access automation should be rejected unless the environment is controlled, reversible, and least-privilege alternatives are exhausted
- `vcb.shortcut.always_allow_sensitive_apps` → active: Always Allow decisions for sensitive apps/sites require narrow scope and revocation
- `vcb.shortcut.production_console_computer_use` → active: signed-in production console work should not be delegated as routine GUI automation
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud/background delegation should not receive real secrets or sensitive data
- `vcb.shortcut.reviewing_cloud_summary_only` → active: cloud work requires diff, check, and artifact review, not summary-only acceptance
- `vcb.shortcut.unattended_long_runs` → active: long runs need milestones, review packets, and stop conditions
- `vcb.shortcut.parallel_agents_edit_same_files` → active: use when parallel agents might mutate overlapping files or create merge/integration ambiguity
- `vcb.shortcut.many_ais_same_files` → active: use when multiple AI systems are asked to work against the same files without one owner and one integration path
- `vcb.shortcut.parallel_agents_same_files` → planned future companion; active many-AIs-same-files route is listed immediately above
- `vcb.shortcut.subagent_swarm` → active: use when too many agents/subagents are spawned without bounded roles, outputs, or integration rules
- `vcb.shortcut.cloud_task_without_context` → active: cloud/background tasks need a context packet before delegation
- `vcb.shortcut.parallel_tasks_same_files` → planned future companion; active same-file routes are listed immediately above
- `vcb.shortcut.automating_unstable_workflow` → planned
- `vcb.shortcut.automation_spam` → active: recurring automation should be quiet, deduplicated, and action-oriented
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.subagents_parallel_thinking` → active
- `vcb.chapter.automations_recurring_work` → active
- `vcb.chapter.computer_use_browser_gui_tasks` → active
- `vcb.shortcut.unofficial_tools` → active: unvetted tools change trust boundary
- `vcb.shortcut.trusting_external_tool_output` → active: tool output needs provenance and verification
- `vcb.shortcut.hook_overreach` → active: hooks should not replace CI or human judgment

## Project operating-system shortcuts
- `vcb.shortcut.process_overhead_for_tiny_project` → active: right-size process so tiny projects keep useful guardrails without fake ceremony
- `vcb.shortcut.team_workflow_without_team` → active: avoid copying team process into solo work when a lighter checklist would control the same risk
- `vcb.shortcut.ignoring_failure_mode` → planned
- `vcb.shortcut.treating_symptom_as_root_cause` → planned
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: adapt reusable playbooks to the current repo, stack, risk level, and available evidence before following them
- `vcb.shortcut.generated_prototype_as_production_foundation` → planned
- `vcb.shortcut.overbuilding_first_app` → planned
- `vcb.shortcut.skipping_senior_checklist` → planned
- `vcb.shortcut.checklist_theater` → planned
- `vcb.chapter.prompt_library_to_team_workflow` → active
- `vcb.chapter.failure_modes_codex_work` → active
- `vcb.chapter.codex_playbooks` → active
- `vcb.chapter.first_serious_app` → active
- `vcb.chapter.senior_engineer_checklist` → active

## Shortcut overview and harm reduction
- `vcb.chapter.risk_managed_shortcuts` → active
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active

## Field-practice shortcuts

- `vcb.field.chatgpt_pm_codex_implementer` → active needs_more_evidence: can become model-routing guesswork if planner output is not reconciled with repo facts
- `vcb.field.fresh_agent_review` → active reproduced: can become review theater if the fresh agent is treated as approval
- `vcb.field.context_reset_between_tasks` → active candidate: can become context loss if no handoff packet exists
- `vcb.field.agents_md_first` → active candidate: can become AGENTS.md overstuffing or stale guidance
- `vcb.field.skeleton_todo_first` → active candidate: can become fake completeness if TODOs are not verified
- `vcb.field.strict_typecheck_lint_gates` → active reproduced: can become check theater if gates are noisy or scoped wrong
- `vcb.field.greenfield_vs_production_rule` → active candidate: can become wrong-phase shortcut if phase is asserted without evidence
- `vcb.field.lessons_file_loop` → active candidate: can become permanent stale process if not pruned
- `vcb.field.multi_agent_review_consensus` → active needs_more_evidence: can become consensus-as-correctness
- `vcb.chapter.field_notes_unofficial_practices` → active fallback
- `vcb.shortcut.unofficial_tools` → active companion: unofficial tool adoption requires disposable evaluation and trust-boundary review
- `vcb.shortcut.trusting_external_tool_output` → active companion: external output requires provenance and verification

## Update-maintenance shortcuts
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `vcb.chapter.maintaining_updating_bible` → active
- `vcb.shortcut.stale_agents_md` → active: Stale AGENTS.md shortcut guardrails
- `vcb.shortcut.checklist_theater` → planned

## Constraint and cost shortcuts

- `vcb.shortcut.defaulting_to_high_throughput` → planned
- `vcb.shortcut.permanent_high_usage_plan` → planned
- `vcb.shortcut.over_optimizing_for_price` → planned
- `vcb.shortcut.skipping_maintenance_cleanup` → planned
- `vcb.shortcut.buying_tools_as_progress` → planned

## Shortcut routes clarified by foundational concept cards
- `vcb.shortcut.vague_prompt` → active: underspecified work-order guardrails; related active concept cards: `vcb.concepts.api_basics`, `vcb.concepts.frontend_backend`
- `vcb.shortcut.adding_dependencies_fast` → active: shortcut risk: package bloat and supply-chain drag
- `vcb.shortcut.skipping_tests` → active: shortcut risk: skipped verification and hidden regressions
- `vcb.shortcut.ignoring_lint_typecheck` → active: static-check guardrails; related active concept cards: `vcb.concepts.typecheck`, `vcb.concepts.lint`
- `vcb.shortcut.real_secrets_in_prototype` → active: keep real credentials out of prototypes; related active concept cards: `vcb.concepts.environment_variable`, `vcb.concepts.authentication`
- `vcb.shortcut.overbroad_ci_permissions` → active: narrow CI permissions; related active concept card: `vcb.concepts.ci`

## Shortcuts around Codex features

- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation

- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `tool.codex_worktrees` → active: worktree isolation for parallel local/app tasks and automation change separation
- `tool.codex_subagents` → active: parallel specialist agents for bounded analysis, exploration, and disjoint implementation work
- `tool.codex_automations` → active: recurring/report-first Codex background work with review owner and stop conditions
- `tool.codex_computer_use` → active: desktop GUI operation with app permissions, visible-state risk, and human supervision
- `tool.codex_browser` → active: in-app rendered-page preview, comments, screenshots, and browser verification
- `tool.codex_chrome_extension` → active: signed-in Chrome browser workflows with website approvals and account-risk controls

- `vcb.codex.app` → active: shortcut reality for Codex App
- `vcb.codex.cli` → active: shortcut reality for Codex CLI
- `vcb.codex.ide_extension` → active: shortcut reality for Codex IDE Extension
- `vcb.codex.cloud` → active: shortcut reality for Codex Cloud / Web
- `vcb.codex.github_review` → active: shortcut reality for Codex GitHub PR Review
- `vcb.codex.config` → active: shortcut reality for Codex Config
- `vcb.codex.agents_md` → active: shortcut reality for AGENTS.md
- `vcb.codex.skills` → active: shortcut reality for Codex Skills
- `vcb.codex.mcp` → active: shortcut reality for MCP for Codex
- `vcb.codex.hooks` → active: shortcut reality for Codex Hooks
- `vcb.codex.automations` → active: shortcut reality for Codex Automations
- `vcb.codex.subagents` → active: shortcut reality for Codex Subagents
- `vcb.codex.computer_use` → active: shortcut reality for Codex Computer Use
- `vcb.codex.feature_maturity` → active: shortcut reality for Codex Feature Maturity
- `vcb.codex.changelog_monitoring` → active: shortcut reality for Codex Changelog Monitoring

## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work


## Shortcut routes for frontend, refactor, dependency, release, and documentation workflows
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context


## Shortcut routes for active failure modes
- `vcb.failure.hallucinated_apis` → active: shortcut family is trusting plausible generated API claims without contract evidence
- `vcb.failure.context_pollution` → active: shortcut family is dumping stale or excessive context instead of curating a packet
- `vcb.failure.weakened_tests` → active: shortcut family is making checks pass by weakening tests
- `vcb.failure.broad_refactor_drift` → active: shortcut family is broad cleanup without behavior boundaries
- `vcb.failure.dependency_bloat` → active: shortcut family is adding packages/frameworks before proving need
- `vcb.failure.ui_taste_gap` → active: shortcut family is accepting UI from code inspection or one happy-path screenshot
- `vcb.failure.ci_false_confidence` → active: shortcut family is treating green configured checks as full verification
- `vcb.failure.done_claim_without_evidence` → active: shortcut family is accepting polished completion summaries without artifacts


## Constraint and budget shortcut routes

- `vcb.constraints.scope_budget` → controls over-optimizing for price, vague prompts, and skipped checks
- `vcb.constraints.review_budget` → controls defaulting to high throughput, parallel agent conflicts, and best-of-N without review
- `vcb.constraints.usage_burn` → controls context dumping, permanent high-usage plan habits, and unnecessary tool/MCP loading
- `vcb.constraints.attention_budget` → controls accepting looks-done summaries and low-attention review-later shortcuts
- `vcb.constraints.operating_mode` → controls broad permissions and wrong-surface defaults
- `vcb.constraints.recovery_budget` → controls coding on main, broad refactors, and unattended mutation
- `vcb.constraints.build_vs_maintenance` → controls prototype-to-production shortcut drift and maintenance cleanup debt
- `vcb.constraints.production_quality` → controls skipping senior checklist, security review, tests, and release gates

## Active shortcut harm-reduction cards

- `vcb.shortcut.skipping_tests` → active: risk-managed shortcut card for accepting changes without the smallest relevant verification
- `vcb.shortcut.accepting_looks_done` → active: risk-managed shortcut card for accepting polished output without completion evidence
- `vcb.shortcut.broad_agent_permissions` → active: risk-managed shortcut card for broad filesystem/network/tool/account access
- `vcb.shortcut.unattended_long_runs` → active: risk-managed shortcut card for long-running work without checkpoints
- `vcb.shortcut.broad_refactor` → active: risk-managed shortcut card for broad cleanup or refactor prompts
- `vcb.shortcut.context_dumping` → active: risk-managed shortcut card for noisy/stale prompt context
- `vcb.shortcut.adding_dependencies_fast` → active: risk-managed shortcut card for fast dependency additions
- `vcb.shortcut.reviewing_cloud_summary_only` → active: risk-managed shortcut card for cloud/background work reviewed only by summary

## Active Security and Permission Shortcut Cards

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Setup/config/process semantic shortcut routes

- `vcb.shortcut.skipping_setup` → route when the human wants Codex to edit before install/run/test/build facts are known
- `vcb.shortcut.default_config_forever` → route when old config defaults control every risk profile
- `vcb.shortcut.skipping_agents_md` → route when repeated project guidance stays in prompts instead of repo guidance
- `vcb.shortcut.overstuffing_agents_md` → route when AGENTS.md becomes a context dump
- `vcb.shortcut.stale_agents_md` → route when persistent guidance is outdated or contradicted
- `vcb.shortcut.unofficial_tools` → route when an external tool/plugin/MCP server is installed before trust review
- `vcb.shortcut.hook_overreach` → route when hooks are used as subjective policy or complete safety gate
- `vcb.shortcut.trusting_external_tool_output` → route when tool output is accepted without provenance or local verification

## Tool-sprawl, skill, MCP, and reusable workflow shortcut routes

- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence
## Multi-AI, answer-selection, and model-bias shortcut routes

- `vcb.shortcut.many_ais_same_files` → active: using multiple AI systems on the same files without one owner, one branch strategy, and one integration path
- `vcb.shortcut.parallel_agents_edit_same_files` → active: letting multiple agents mutate overlapping files at the same time and hoping the merge will be obvious later
- `vcb.shortcut.best_of_n_without_review` → active: asking several AIs for answers, then accepting the one that looks best without checking diffs, tests, source evidence, or risks
- `vcb.shortcut.cherry_picking_ai_answers` → active: choosing the answer that confirms your preferred plan instead of the answer with the best evidence
- `vcb.shortcut.consensus_as_correctness` → active: treating agreement between multiple AIs as proof that a claim, estimate, fix, or design is correct
- `vcb.shortcut.trusting_estimates_before_inspection` → active: believing an AI estimate before the model has inspected the actual code, dependencies, tests, constraints, and unknowns
- `vcb.shortcut.ignoring_model_biases` → active: forgetting that models can be biased toward plausible answers, overconfident summaries, common patterns, pleasing the user, and underestimating hidden project constraints
- `vcb.shortcut.model_routing_guesswork` → active: choosing a model, reasoning level, surface, or AI tool by brand feeling, stale advice, or price anxiety instead of current docs, task shape, risk, and evidence needs
- `vcb.shortcut.subagent_swarm` → active: spawning many subagents or custom agents before each has a bounded question, role, context, output format, and integration plan

## Parallel Cloud and Automation Shortcut Routes

- `vcb.shortcut.unattended_cloud_delegation` → active: bounded cloud/background delegation with branch/worktree isolation, stop conditions, and review packets
- `vcb.shortcut.ambiguous_cloud_task` → active: plan-first guardrails for vague cloud tasks before mutation
- `vcb.shortcut.cloud_task_without_context` → active: delegation packet and context-gap checks for cloud work
- `vcb.shortcut.parallel_cloud_sprawl` → active: task matrix, isolated branches/worktrees, and integration owner for parallel cloud work
- `vcb.shortcut.conflicting_parallel_agents` → active: one mutating owner per file/behavior and one integrator
- `vcb.shortcut.automation_spam` → active: recurring automations must be actionable, deduplicated, and quiet when nothing changed
- `vcb.shortcut.automation_mutation_without_review` → active: report/propose first; branch-only mutation with human review if unavoidable
- `vcb.shortcut.browser_clicking_without_repro` → active: exact GUI/browser repro and evidence before mutation
- `vcb.shortcut.logged_in_browser_secrets` → active: fake/staging accounts and scoped approvals for signed-in browser/GUI work

<!-- VCB:STOP_RETRIEVAL reason="by_shortcut_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_shortcut -->
