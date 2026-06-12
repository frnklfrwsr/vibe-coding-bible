---
id: vcb.index.by_codex_surface
title: INDEX_BY_CODEX_SURFACE
artifact_type: index
version: 0.39.0-draft.chunk38
status: chunk_38_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_codex_surface version=0.39.0-draft.chunk38 -->

# INDEX_BY_CODEX_SURFACE

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Surface selection
- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation

- `tool.codex` → active: choose the primary Codex tool surface by task shape and risk
- `tool.codex_worktrees` → active: choose when parallel local/app tasks need isolated change areas
- `tool.codex_subagents` → active: choose when bounded parallel analysis or specialist review is useful
- `tool.codex_automations` → active: choose when a proven workflow should recur as report-first background work
- `tool.codex_computer_use` → active: choose when a narrow desktop GUI flow is required
- `tool.codex_browser` → active: choose for in-app rendered-page preview and browser verification without signed-in state
- `tool.codex_chrome_extension` → active: choose only when signed-in Chrome state is required
- `vcb.chapter.codex_surfaces` → active
- `vcb.chapter.codex_mental_model` → active

## Codex App and local orchestration
- `tool.codex_app` → active: desktop/local command center for supervised Codex work
- `tool.codex_worktrees` → active: app-managed isolation for parallel local work
- `tool.codex_automations` → active: app-managed recurring/background work after manual proof
- `tool.codex_browser` → active: app-contained browser preview and verification
- `tool.codex_computer_use` → active: app-mediated desktop/GUI operation when needed
- `vcb.chapter.codex_surfaces` → active
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.automations_recurring_work` → active
- `vcb.codex.app` → active

## Codex IDE Extension
- `tool.codex_ide_extension` → active: editor-context Codex surface
- `vcb.chapter.codex_surfaces` → active
- `vcb.chapter.context_management` → active
- `vcb.chapter.frontend_work` → active
- `vcb.codex.ide_extension` → active

## Codex CLI
- `tool.codex_cli` → active: terminal-native Codex surface
- `vcb.chapter.codex_surfaces` → active
- `vcb.chapter.installing_and_configuring_codex` → active
- `vcb.chapter.sandboxing_and_approvals` → active
- `vcb.codex.cli` → active

## Codex Cloud and worktrees
- `tool.codex_cloud` → active: cloud/background delegation tool card
- `tool.codex_worktrees` → active: local/app worktree isolation for reviewable parallel changes
- `tool.codex_subagents` → active: parallel specialist-agent analysis and bounded work
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.subagents_parallel_thinking` → active
- `vcb.chapter.ci_noninteractive_github_actions` → active
- `vcb.codex.cloud` → active
- `vcb.codex.subagents` → active

## GitHub review and PR surfaces
- `tool.codex_github_review` → active: PR review tool card
- `tool.github` → active: repository, branch, PR, review, and merge-gate source of truth for Codex-generated changes
- `vcb.chapter.github_pr_review_with_codex` → active fallback
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.concepts.pull_request` → active
- `vcb.codex.github_review` → active

## Non-interactive and CI surfaces
- `tool.codex_exec` → active: non-interactive CLI/CI tool card
- `tool.github_actions` → active: CI workflow/check evidence, token permissions, secrets, runners, and automation artifacts
- `vcb.chapter.ci_noninteractive_github_actions` → active fallback
- `vcb.chapter.codex_playbooks` → active
- `vcb.codex.noninteractive` → planned
- `vcb.codex.github_action` → planned

## Computer Use and browser surfaces
- `tool.codex_computer_use` → active: desktop GUI operation with app permissions and human supervision
- `tool.codex_browser` → active: in-app rendered-page preview, comments, screenshots, and browser verification
- `tool.codex_chrome_extension` → active: signed-in Chrome workflows with website approvals and account-risk controls
- `vcb.chapter.computer_use_browser_gui_tasks` → active
- `vcb.chapter.frontend_work` → active
- `vcb.codex.computer_use` → active
- `vcb.codex.browser` → planned companion feature route

## Codex Security and security review surfaces

- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation
- `tool.codex_cloud` → active: companion cloud environment and connected-repository surface
- `tool.codex_github_review` → active: companion PR-review signal surface
- `vcb.safety.security_review` → active: general security-review workflow fallback
- `vcb.chapter.security_for_vibe_coders` → active: narrative fallback

## Persistent customization surfaces
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.chapter.agents_md_operating_manual` → active
- `vcb.chapter.codex_config_defaults` → active
- `vcb.chapter.skills_reusable_workflows` → active
- `vcb.chapter.mcp_external_tools` → active
- `vcb.chapter.hooks_deterministic_guardrails` → active
- `vcb.codex.agents_md` → active
- `vcb.codex.config` → active
- `vcb.codex.skills` → active
- `vcb.codex.mcp` → active
- `vcb.codex.hooks` → active

## Cross-surface field practice and shortcut guidance

- `vcb.field.chatgpt_pm_codex_implementer` → active candidate: ChatGPT PM / Codex implementer split
- `vcb.field.fresh_agent_review` → active candidate: fresh independent agent/session diff review
- `vcb.field.context_reset_between_tasks` → active candidate: reset or summarize context between unrelated tasks
- `vcb.field.agents_md_first` → active candidate: minimal AGENTS.md early in durable repos
- `vcb.field.skeleton_todo_first` → active candidate: human skeleton/TODOs before agent implementation
- `vcb.field.strict_typecheck_lint_gates` → active candidate: typecheck/lint/test gates after agent changes
- `vcb.field.greenfield_vs_production_rule` → active candidate: explicit project phase and compatibility posture
- `vcb.field.lessons_file_loop` → active candidate: temporary lessons loop before durable guidance promotion
- `vcb.field.multi_agent_review_consensus` → active candidate: multi-agent review with evidence, not consensus-as-proof
- `vcb.chapter.field_notes_unofficial_practices` → active fallback
- `vcb.chapter.risk_managed_shortcuts` → active companion
- `vcb.chapter.maintaining_updating_bible` → active companion

## Cross-surface prompting and workflow cards
- `vcb.prompting.four_part_prompt` → active: works across app, CLI, IDE, and cloud prompts
- `vcb.prompting.plan_first` → active: plan gate before risky local or cloud work
- `vcb.prompting.context_management` → active: context packet and stale-context reset
- `vcb.prompting.acceptance_criteria` → active: done-when evidence for any surface
- `vcb.workflow.unknown_codebase` → active: read-only map before mutation
- `vcb.workflow.feature_slicing` → active: bounded feature delegation
- `vcb.workflow.bug_repro` → active: reproduce/patch/rerun loop
- `vcb.workflow.testing` → active: verification instructions for generated changes

## Concept cards useful across Codex surfaces
- Codex App / Cloud → `vcb.concepts.ci`, `vcb.concepts.observability`, `vcb.concepts.migration` → active
- Codex IDE / CLI → `vcb.concepts.typecheck`, `vcb.concepts.lint`, `vcb.concepts.build_step` → active
- GitHub Review / Actions → `vcb.concepts.test`, `vcb.concepts.dependency`, `vcb.concepts.ci` → active
- Browser/GUI work → `vcb.concepts.state`, `vcb.concepts.async`, `vcb.concepts.frontend_backend` → active

## Codex governance and maintenance surfaces
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `vcb.chapter.maintaining_updating_bible` → active fallback
- `SOURCE_REGISTER.md` → active companion register
- `DEPRECATION_REGISTER.md` → active companion register

## Active Codex Feature Cards
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.codex.app` → active
- `vcb.codex.cli` → active
- `vcb.codex.ide_extension` → active
- `vcb.codex.cloud` → active
- `vcb.codex.github_review` → active
- `vcb.codex.config` → active
- `vcb.codex.agents_md` → active
- `vcb.codex.skills` → active
- `vcb.codex.mcp` → active
- `vcb.codex.hooks` → active
- `vcb.codex.automations` → active
- `vcb.codex.subagents` → active
- `vcb.codex.computer_use` → active
- `vcb.codex.feature_maturity` → active companion
- `vcb.codex.changelog_monitoring` → active companion
## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Codex-surface routes for frontend, refactor, dependency, release, and documentation workflows
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## Codex failure-mode diagnosis
- `vcb.failure.hallucinated_apis` → active: plausible code claims need contract proof
- `vcb.failure.context_pollution` → active: Codex output degraded by stale/noisy context

## Failure-mode routes by Codex surface
- `vcb.chapter.failure_modes_codex_work` → active: chapter-level failure taxonomy
- `vcb.failure.hallucinated_apis` → active: applies across App, CLI, IDE, and Cloud work
- `vcb.failure.context_pollution` → active: applies especially to long threads, Cloud, and subagents
- `vcb.failure.ci_false_confidence` → active: applies to non-interactive and GitHub Action workflows

## Failure modes across Codex surfaces
- IDE/CLI local edits: `vcb.failure.hallucinated_apis`, `vcb.failure.context_pollution`, `vcb.failure.weakened_tests`
- GitHub review and CI: `vcb.failure.ci_false_confidence`, `vcb.failure.weakened_tests`
- Computer Use/browser UI: `vcb.failure.ui_taste_gap`
- Dependency/security surfaces: `vcb.failure.dependency_bloat`

## Constraint and budget routing by Codex surface

- Codex App / local work → `vcb.constraints.operating_mode`, `vcb.constraints.attention_budget`, `vcb.constraints.production_quality`
- Codex CLI / scripts → `vcb.constraints.usage_burn`, `vcb.constraints.recovery_budget`, `vcb.constraints.scope_budget`
- Codex Cloud / delegated work → `vcb.constraints.review_budget`, `vcb.constraints.attention_budget`, `vcb.constraints.operating_mode`
- GitHub review / PR work → `vcb.constraints.production_quality`, `vcb.constraints.recovery_budget`, `vcb.constraints.build_vs_maintenance`
- MCP/tool-heavy work → `vcb.constraints.usage_burn`, `vcb.constraints.operating_mode`, `vcb.constraints.review_budget`

## Shortcut Harm-Reduction by Codex Surface

- `vcb.shortcut.broad_agent_permissions` → active: CLI/IDE/App permission and sandbox controls
- `vcb.shortcut.unattended_long_runs` → active: Cloud/App/automation long-run controls
- `vcb.shortcut.reviewing_cloud_summary_only` → active: Cloud/Web and app returned-diff review controls
- `vcb.shortcut.context_dumping` → active: App/CLI/Cloud context-packet controls
- `vcb.shortcut.skipping_tests` → active: CLI/App verification guardrails
- `vcb.shortcut.accepting_looks_done` → active: final-response evidence guardrail across Codex surfaces
- `vcb.shortcut.broad_refactor` → active: IDE/App/CLI refactor-scope guardrail
- `vcb.shortcut.adding_dependencies_fast` → active: CLI/App dependency-install guardrail

## Security and permission shortcuts by Codex surface

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Setup/process shortcuts by Codex surface

- `vcb.shortcut.skipping_setup` → active: CLI/App/IDE setup inspection before edits.
- `vcb.shortcut.default_config_forever` → active: CLI/App/IDE config review at phase changes.
- `vcb.shortcut.skipping_agents_md` → active: AGENTS.md durable repo guidance omitted.
- `vcb.shortcut.overstuffing_agents_md` → active: AGENTS.md overloaded with non-durable context.
- `vcb.shortcut.stale_agents_md` → active: AGENTS.md guidance no longer matches repo reality.
- `vcb.shortcut.unofficial_tools` → active: MCP/plugins/external tools create trust boundaries.
- `vcb.shortcut.hook_overreach` → active: hooks overused as subjective policy gates.
- `vcb.shortcut.trusting_external_tool_output` → active: MCP/browser/search/plugin output accepted without verification.

## Codex skill, MCP, plugin, hook, and process shortcut routes

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## Codex routes for multi-AI/model-bias shortcuts

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

## Non-AI infrastructure tool companions for Codex surfaces

- `tool.github` → active: repository and PR source of truth for Codex-generated changes.
- `tool.github_actions` → active: CI/check evidence for Codex output and non-interactive reports.
- `tool.github_dependabot` → active: dependency-update PR queue that Codex can help review but not auto-approve.
- `tool.npm` → active: package scripts, manifests, lockfiles, and audit evidence used by Codex in JavaScript projects.
- `tool.playwright` → active: browser/UI verification evidence for Codex frontend work.
- `tool.openssf_scorecard` → active: supply-chain quality signals for Codex-assisted dependency and repository review.

## AI coding, AI IDE, and planning companions for Codex surfaces

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `vcb.chapter.when_to_use_other_ais` → active fallback
- `vcb.shortcut.parallel_agents_edit_same_files` → active companion


## Browser-dev, app-builder, and UI-generation companions for Codex surfaces

- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `tool.codex` → active companion: harden/review generated prototype code when it moves into a repo
- `tool.codex_ide_extension` → active companion: editor-context integration after app-builder output is in the repo
- `tool.codex_security` → active companion: security review for auth/data/payment-sensitive generated apps

<!-- VCB:STOP_RETRIEVAL reason="by_codex_surface_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_codex_surface -->
