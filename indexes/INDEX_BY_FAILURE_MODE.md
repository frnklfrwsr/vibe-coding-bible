---
id: vcb.index.by_failure_mode
title: INDEX_BY_FAILURE_MODE
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_failure_mode version=0.41.0-draft.chunk40 -->

# INDEX_BY_FAILURE_MODE

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Prompting/workflow controls for common failure modes
- `vcb.prompting.four_part_prompt` → active: vague prompt / broad instruction control
- `vcb.prompting.acceptance_criteria` → active: “looks done” and unverified summary control
- `vcb.prompting.plan_first` → active: wrong architecture and broad-edit control
- `vcb.prompting.context_management` → active: stale/missing context control
- `vcb.workflow.unknown_codebase` → active: editing-before-understanding control
- `vcb.workflow.feature_slicing` → active: one-giant-diff control
- `vcb.workflow.bug_repro` → active: symptom-patch control
- `vcb.workflow.testing` → active: weakened/skipped test control

## Codex summary sounds done but the diff says otherwise
- `vcb.failure.done_claim_without_evidence` → active: completion summary must be backed by diff, changed files, commands, logs, screenshots, or acceptance evidence
- `vcb.concepts.diff` → active
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.chapter.senior_engineer_checklist` → active

## Codex edits unrelated files or scope creeps
- `vcb.chapter.four_part_prompt` → active
- `vcb.chapter.plan_first_code_second` → active
- `vcb.chapter.git_discipline` → active
- `vcb.failure.scope_creep` → planned

## Codex patches without reproducing the bug
- `vcb.failure.done_claim_without_evidence` → active: bug-fix claims need repro/check output before acceptance
- `vcb.chapter.debugging_with_reproduction` → active
- `vcb.chapter.writing_updating_tests` → active
- `vcb.shortcut.debugging_without_repro` → planned

## Codex weakens or deletes tests
- `vcb.chapter.writing_updating_tests` → active
- `vcb.chapter.reviewing_codex_output` → active
- `vcb.failure.weakened_tests` → active: tests loosened, deleted, skipped, or over-mocked to pass

## Codex adds unnecessary dependencies

- `tool.npm` → active: dependency manifests, lockfiles, package scripts, install behavior, and audit evidence
- `tool.github_dependabot` → active: dependency alert/update PR review queue
- `tool.openssf_scorecard` → active: supply-chain health signal for dependency-adoption risk
- `vcb.failure.dependency_bloat` → active: dependency additions create maintenance, security, and lockfile drag
- `vcb.chapter.dependency_package_framework_decisions` → active fallback
- `vcb.chapter.security_for_vibe_coders` → active fallback

## Codex creates a broad risky refactor
- `vcb.chapter.refactoring_without_breaking_everything` → active
- `vcb.concepts.blast_radius` → active
- `vcb.concepts.recoverability` → active
- `vcb.failure.broad_refactor_drift` → active: broad refactors hide behavior changes and rewrite drift

## Context is missing, stale, or polluted
- `vcb.chapter.context_management` → active
- `vcb.chapter.understanding_unknown_codebase` → active
- `vcb.failure.context_pollution` → active: stale, noisy, excessive, or contradictory context steers wrong edits
- `vcb.shortcut.skipping_setup` → active: missing setup context leads to plausible but unverified edits
- `vcb.shortcut.overstuffing_agents_md` → active: overstuffed AGENTS.md pollutes context
- `vcb.shortcut.stale_agents_md` → active: stale project guidance creates wrong assumptions

## UI works but has poor taste, states, or accessibility

- `tool.figma` → active: design files, components, prototype flows, Dev Mode handoff, screenshots, and design-intent evidence for UI-state and design-code drift review
- `tool.v0` → active: UI generation must still cover states, responsiveness, accessibility, design-system fit, and reviewable code
- `tool.playwright` → active: browser/end-to-end evidence, screenshots, traces, and UI verification
- `tool.replit` → active companion: hosted preview/demo needs state and browser evidence
- `tool.lovable` → active companion: generated full-stack UI needs backend/state/access review
- `tool.bolt` → active companion: generated app UI needs browser, dependency, and code review
- `vcb.failure.ui_taste_gap` → active: UI looks functional but lacks product feel/states/accessibility/responsiveness
- `vcb.workflow.frontend_work` → active companion
- `vcb.workflow.visual_qa` → active companion
- `vcb.workflow.accessibility_review` → active companion

## Security-sensitive behavior is under-specified

- `tool.clerk` → active: auth/session/user/org access boundaries must be specified and tested
- `tool.auth0` → active: IAM/OIDC/OAuth/API authorization boundaries must be specified and validated
- `tool.supabase` → active: RLS, data access, service-role keys, functions, and storage policy boundaries must be specified
- `tool.stripe` → active: payment, subscription, webhook, customer, and entitlement boundaries must be specified
- `tool.codex_security` → active companion: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation
- `vcb.shortcut.real_secrets_in_prototype` → active: real-secret prototype shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud-secret exposure shortcut guardrails
- `vcb.shortcut.production_console_computer_use` → active: production GUI side-effect guardrails
- `vcb.chapter.security_for_vibe_coders` → active fallback
- `vcb.chapter.sandboxing_and_approvals` → active fallback
- `vcb.safety.security_review` → active companion
- `vcb.failure.security_regression` → planned
- `vcb.shortcut.default_config_forever` → active: unreviewed config can overexpose risky work
- `vcb.shortcut.unofficial_tools` → active: unvetted tools change trust boundaries

## CI passes but does not prove the risk

- `tool.github_actions` → active: CI workflow/check evidence, token permissions, secrets, runners, and artifact review
- `tool.playwright` → active companion when browser/UI evidence is part of the claimed proof
- `tool.codex_security` → active: green checks do not replace security finding validation and threat-boundary review
- `vcb.failure.ci_false_confidence` → active: green checks, skipped jobs, summaries, or broad permissions create unsupported confidence
- `vcb.workflow.ci_triage` → active companion
- `vcb.workflow.ci_noninteractive` → active companion

## CI or automation mutates too much

- `tool.github_actions` → active: CI automation permissions, workflow mutation, secret exposure, and release-gate risk
- `vcb.shortcut.automation_mutation_without_review` → active: scheduled/noninteractive mutation lacks human review gate
- `vcb.shortcut.automation_spam` → active: recurring automation creates noisy, unactionable output
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad CI permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: persistent CI secret shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation shortcut guardrails
- `vcb.chapter.ci_noninteractive_github_actions` → active fallback
- `vcb.chapter.automations_recurring_work` → active fallback
- `vcb.failure.ci_false_confidence` → active: green or automated checks treated as broader proof than they are

## Cloud, subagent, or GUI work runs too broadly
- `vcb.shortcut.unattended_cloud_delegation` → active: background cloud task has too much scope or no stop condition
- `vcb.shortcut.ambiguous_cloud_task` → active: cloud work starts from vague goal and invents scope
- `vcb.shortcut.cloud_task_without_context` → active: cloud work lacks branch, repro, files, constraints, or checks
- `vcb.shortcut.parallel_cloud_sprawl` → active: too many parallel cloud branches without rubric/integrator
- `vcb.shortcut.conflicting_parallel_agents` → active: multiple agents mutate overlapping files or behavior
- `vcb.shortcut.browser_clicking_without_repro` → active: GUI/browser task clicks without a reproducible flow
- `vcb.shortcut.logged_in_browser_secrets` → active: signed-in browser exposes secrets, customer data, or account authority
- `vcb.shortcut.always_allow_sensitive_apps` → active: persistent sensitive app/site approval guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: real secrets in delegated cloud work guardrails
- `vcb.shortcut.production_console_computer_use` → active: production console Computer Use guardrails
- `vcb.chapter.cloud_delegation_parallel_work` → active
- `vcb.chapter.subagents_parallel_thinking` → active
- `vcb.chapter.computer_use_browser_gui_tasks` → active
- `vcb.chapter.failure_modes_codex_work` → active

## Team workflow creates ceremony without reducing risk
- `tool.linear` → active: issue/project/workflow ownership, status hygiene, cycle/project scope, and evidence-backed team execution before adding ceremony
- `vcb.chapter.prompt_library_to_team_workflow` → active fallback
- `vcb.chapter.codex_playbooks` → active fallback
- `vcb.shortcut.team_workflow_without_team` → active companion: avoid copying team process into solo work when a lighter checklist would control the same risk

## Community tactic treated as official guidance

- `vcb.field.chatgpt_pm_codex_implementer` → active candidate: ChatGPT PM / Codex implementer split
- `vcb.field.fresh_agent_review` → active candidate: fresh independent agent/session diff review
- `vcb.field.context_reset_between_tasks` → active candidate: reset or summarize context between unrelated tasks
- `vcb.field.agents_md_first` → active candidate: minimal AGENTS.md early in durable repos
- `vcb.field.skeleton_todo_first` → active candidate: human skeleton/TODOs before agent implementation
- `vcb.field.strict_typecheck_lint_gates` → active candidate: typecheck/lint/test gates after agent changes
- `vcb.field.greenfield_vs_production_rule` → active candidate: explicit project phase and compatibility posture
- `vcb.field.lessons_file_loop` → active candidate: temporary lessons loop before durable guidance promotion
- `vcb.field.multi_agent_review_consensus` → active candidate: multi-agent review with evidence, not consensus-as-proof
- `vcb.chapter.field_notes_unofficial_practices` → active fallback: evidence labels, promotion rules, and non-promotion policy
- `vcb.chapter.maintaining_updating_bible` → active companion: source/register hygiene when a tactic changes status

## Bible guidance became stale
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `vcb.chapter.maintaining_updating_bible` → active
- `vcb.chapter.how_to_use_this_bible` → active
- `vcb.shortcut.stale_agents_md` → active: stale AGENTS.md needs pruning and source review

## Shortcut with no recovery path
- `vcb.chapter.risk_managed_shortcuts` → active
- `vcb.concepts.recoverability` → active
- `vcb.concepts.rollback` → active

## Bad estimates and confident wrong summaries
- `vcb.shortcut.trusting_estimates_before_inspection` → active: estimates accepted before repo/code/test/dependency inspection
- `vcb.shortcut.ignoring_model_biases` → active: confident output may reflect plausible-pattern, user-pleasing, or summary bias
- `vcb.shortcut.consensus_as_correctness` → active: multiple AI answers agree but have not been independently verified
- `vcb.shortcut.best_of_n_without_review` → active: answer-shopping replaces diff, source, and check review
- `vcb.shortcut.cherry_picking_ai_answers` → active: preferred answers are selected without evidence-backed review
- `vcb.failure.done_claim_without_evidence` → active: confident summaries require artifact-backed evidence
- `vcb.chapter.what_codex_is_bad_at` → active
- `vcb.chapter.model_biases_failure_biases_bad_estimates` → active
- `vcb.concepts.diff` → active

## Tool sprawl and AI-tool chaos

- `tool.docker` → active: local dev/container tool can hide environment, image, host, secrets, and CI parity risk
- `tool.figma` → active: design/prototype tool can hide screenshot overtrust, stale specs, and design-code drift
- `tool.linear` → active: project-management tool can hide ticket/status theater and missing evidence ownership
- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `tool.chatgpt` → active companion: planning/explanation tool-choice risk
- `tool.claude` → active companion: alternate AI review and multi-AI comparison risk
- `tool.cursor` → active companion: AI IDE local-edit risk
- `tool.github_copilot` → active companion: autocomplete/IDE-native AI risk
- `tool.windsurf` → active companion: agentic AI IDE risk
- `vcb.shortcut.tool_sprawl` → active companion: keep the tool stack small enough to audit, revoke, and explain
- `vcb.shortcut.unofficial_tools` → active companion: unofficial tool adoption without trust review
- `vcb.shortcut.trusting_external_tool_output` → active companion: external tool output treated as verified truth
- `vcb.chapter.tool_stack_catalog` → active fallback
- `vcb.chapter.cost_benefit_analysis` → active fallback

## Codex invents APIs, routes, fields, packages, or options
- `vcb.failure.hallucinated_apis` → active: plausible API or SDK contract lacks local/vendor evidence
- `vcb.concepts.api_basics` → active
- `vcb.workflow.testing` → active

## Plausible APIs, weak tests, and hidden gaps
- `vcb.chapter.what_codex_is_bad_at` → active
- `vcb.chapter.model_biases_failure_biases_bad_estimates` → active
- `vcb.chapter.writing_updating_tests` → active
- `vcb.chapter.security_for_vibe_coders` → active
- `vcb.failure.hallucinated_apis` → active: plausible but fake API contracts hidden in code
- `vcb.failure.weakened_tests` → active: false green builds from weaker tests

## Foundational concept failures
- `vcb.concepts.api_basics` → active: Codex invents API routes, fields, or response shapes
- `vcb.concepts.frontend_backend` → active: frontend-only fixes hide backend/security bugs
- `vcb.concepts.database_schema` → active: persistent data shape changes are made casually
- `vcb.concepts.authentication` → active: fake login or leaked session/token handling
- `vcb.concepts.authorization` → active: UI hiding is mistaken for permission enforcement
- `vcb.concepts.state` → active: stale or duplicated UI/server state
- `vcb.concepts.async` → active: race conditions, stale responses, arbitrary sleeps
- `vcb.concepts.dependency` → active: unnecessary packages and supply-chain drag
- `vcb.concepts.test` → active: weak or deleted tests produce false confidence
- `vcb.concepts.typecheck` → active: type errors silenced instead of fixed
- `vcb.concepts.lint` → active: broad disable comments hide code-quality issues
- `vcb.concepts.migration` → active: unsafe data/schema changes
- `vcb.concepts.environment_variable` → active: secrets/config leak into code, prompts, logs, or CI
- `vcb.concepts.build_step` → active: dev server success mistaken for deployable build
- `vcb.concepts.ci` → active: CI bypassed or over-permissioned
- `vcb.concepts.feature_flag` → active: flags become stale or mistaken for security boundaries
- `vcb.concepts.observability` → active: production claims lack logs/metrics/traces/errors

## Codex feature misuse

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

- `vcb.codex.app` → active: misuse and recovery guidance
- `vcb.codex.cli` → active: misuse and recovery guidance
- `vcb.codex.ide_extension` → active: misuse and recovery guidance
- `vcb.codex.cloud` → active: misuse and recovery guidance
- `vcb.codex.github_review` → active: misuse and recovery guidance
- `vcb.codex.config` → active: misuse and recovery guidance
- `vcb.codex.agents_md` → active: misuse and recovery guidance
- `vcb.codex.skills` → active: misuse and recovery guidance
- `vcb.codex.mcp` → active: misuse and recovery guidance
- `vcb.codex.hooks` → active: misuse and recovery guidance
- `vcb.codex.automations` → active: misuse and recovery guidance
- `vcb.codex.subagents` → active: misuse and recovery guidance
- `vcb.codex.computer_use` → active: misuse and recovery guidance
- `vcb.codex.feature_maturity` → active: misuse and recovery guidance
- `vcb.codex.changelog_monitoring` → active: misuse and recovery guidance

## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Failure-mode routes for frontend, refactor, dependency, release, and documentation workflows
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## Active Failure-Mode Topic Cards
- `vcb.failure.hallucinated_apis` → active: hallucinated APIs and fake interface contracts
- `vcb.failure.context_pollution` → active: stale, noisy, excessive, or contradictory context
- `vcb.failure.weakened_tests` → active: tests changed to pass without proving behavior
- `vcb.failure.broad_refactor_drift` → active: refactor work drifting into behavior change or rewrite
- `vcb.failure.dependency_bloat` → active: unnecessary dependencies and supply-chain drag
- `vcb.failure.ui_taste_gap` → active: frontend work that renders but lacks state, responsive, accessibility, or polish evidence
- `vcb.failure.ci_false_confidence` → active: green CI mistaken for complete verification
- `vcb.failure.done_claim_without_evidence` → active: done claim without artifact evidence

## Constraint and budget failure modes

- `vcb.constraints.operating_mode` → active: wrong Codex surface or permission mode causes excess blast radius
- `vcb.constraints.attention_budget` → active: low attention mistaken for permission to skip review
- `vcb.constraints.usage_burn` → active: vague prompts, context dumps, unnecessary MCP servers, or retries burn usage
- `vcb.constraints.recovery_budget` → active: fast work exceeds rollback and repair capacity
- `vcb.constraints.build_vs_maintenance` → active: prototype habits leak into maintenance or production
- `vcb.constraints.production_quality` → active: generated work treated as production-ready without evidence
- `vcb.constraints.scope_budget` → active: over-optimizing for price creates expensive recovery work
- `vcb.constraints.review_budget` → active: high-throughput work creates review debt, conflicts, or duplicated effort

## Shortcut Harm-Reduction Routes

- `vcb.shortcut.skipping_tests` → active: prevents weakened tests, false confidence, and unsupported done claims
- `vcb.shortcut.accepting_looks_done` → active: prevents unsupported completion claims
- `vcb.shortcut.broad_agent_permissions` → active: prevents blast-radius and secret-exposure escalation
- `vcb.shortcut.unattended_long_runs` → active: prevents low-attention drift, hidden assumptions, and large unreviewable diffs
- `vcb.shortcut.broad_refactor` → active: prevents broad-refactor drift
- `vcb.shortcut.context_dumping` → active: prevents context pollution
- `vcb.shortcut.adding_dependencies_fast` → active: prevents dependency bloat and supply-chain drag
- `vcb.shortcut.reviewing_cloud_summary_only` → active: prevents done claims without diff/check evidence

## Security and permission shortcut failure modes

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Setup/config/process failure routes

- `vcb.shortcut.skipping_setup` → active: setup facts missing before edits, tests, or build verification
- `vcb.shortcut.default_config_forever` → active: stale defaults silently widen permissions or miss changed repo risk
- `vcb.shortcut.skipping_agents_md` → active: repeated project rules stay in fragile prompt memory instead of durable guidance
- `vcb.shortcut.overstuffing_agents_md` → active: durable guidance becomes noisy context pollution
- `vcb.shortcut.stale_agents_md` → active: old commands and rules mislead future agent work
- `vcb.shortcut.unofficial_tools` → active: unvetted tools introduce supply-chain, credential, or data-sharing risk
- `vcb.shortcut.hook_overreach` → active: hooks create false confidence when used beyond objective guardrails
- `vcb.shortcut.trusting_external_tool_output` → active: external tool output is treated as proof without provenance or local verification

## Tool sprawl, brittle process, and reusable workflow failure modes

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## Multi-AI and model-bias failure routes

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

## Repository, CI, dependency, and QA tool failure routes

- `tool.github_actions` → active: CI false confidence, overbroad workflow permissions, flaky checks, and secret exposure routes.
- `tool.github_dependabot` → active: dependency-update PR overtrust, advisory panic-merge, and update queue fatigue routes.
- `tool.npm` → active: dependency bloat, lockfile drift, audit overtrust, and opaque package script routes.
- `tool.playwright` → active: brittle browser tests, screenshot-only verification, and UI evidence gaps.
- `tool.openssf_scorecard` → active: supply-chain score overtrust and automated health-signal misuse.
- `tool.github` → active: direct-to-main mutation, oversized PRs, branch-rule drift, and lost review evidence.

## AI tool selection and multi-AI failures

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `vcb.shortcut.model_routing_guesswork` → active companion
- `vcb.shortcut.consensus_as_correctness` → active companion
- `vcb.shortcut.many_ais_same_files` → active companion


## Generated prototype becomes production foundation

- `tool.figma` → active companion: design/prototype intent must be checked against implementation and browser evidence before production use
- `tool.docker` → active companion: generated prototype dependencies and services need reproducible, reviewable local setup before hardening
- `tool.linear` → active companion: production-hardening work needs issue ownership, scope, and acceptance evidence
- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
- `vcb.shortcut.real_secrets_in_prototype` → active: prototype secrets/data boundary
- `vcb.constraints.production_quality` → active companion: production-readiness evidence
- `vcb.chapter.first_serious_app` → active fallback

## Foundational failure-mode concepts

- `tool.supabase` → active: database/schema/RLS/backend mistakes can create persistent data failures
- `tool.clerk` → active: auth/session/user/org mistakes can create access failures
- `tool.auth0` → active: IAM/OIDC/OAuth/API mistakes can create authorization failures
- `tool.stripe` → active: payment/subscription/webhook mistakes can create customer and revenue failures
- `tool.sentry` → active: missing error/trace/release evidence makes production failures harder to diagnose
- `tool.posthog` → active: bad event taxonomy, replay, or flags can produce false product conclusions
- `tool.vercel` → active: deployment/environment mistakes can mask production-readiness failures
- `vcb.concepts.frontend_backend` → active: frontend-only fixes hide backend/security bugs
- `vcb.concepts.database_schema` → active: persistent data shape changes are made casually
- `vcb.concepts.authentication` → active: identity proof is confused with access permission
- `vcb.concepts.authorization` → active: missing permission checks expose protected actions
- `vcb.concepts.environment_variable` → active: secrets leak through configs, logs, or prompts
- `vcb.concepts.observability` → active: production claims lack logs/metrics/traces/errors

## Local environment, design-handoff, and planning-tool failures

- `tool.docker` → active: environment drift, container works-on-my-machine failures, image provenance gaps, unsafe mounts/ports, and secret leakage into Docker artifacts
- `tool.figma` → active: design handoff drift, missing states, prototype-overtrust, screenshot-only acceptance, and design-code mismatch
- `tool.linear` → active: stale tickets, status theater, missing owners, overloaded projects, and planning without acceptance evidence
- `tool.github_actions` → active companion when container/setup checks or workflow evidence matter
- `tool.playwright` → active companion when Figma/UI evidence must be verified in the browser
- `vcb.shortcut.trusting_external_tool_output` → active companion
- `vcb.chapter.tool_stack_catalog` → active fallback

## Hosting, backend/auth, payment, observability, and analytics failure routes

- `tool.vercel` → active: hosting, preview deployments, environment separation, deployment evidence, and production promotion guardrails
- `tool.supabase` → active: Postgres database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access guardrails
- `tool.clerk` → active: authentication, user management, sessions, organizations, and application identity guardrails
- `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, enterprise/B2B identity, and authorization architecture guardrails
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, and real-money fulfillment guardrails
- `tool.sentry` → active: error monitoring, tracing, performance, release evidence, and production debugging guardrails
- `tool.posthog` → active: product analytics, event taxonomy, session replay, feature flags, experiments, and product-evidence guardrails

## Ecosystem coverage failure modes

- `tool.cloudflare` → active: DNS/CDN/cache/edge routing works in summary but breaks production traffic, security posture, or rollback.
- `tool.netlify` → active: deploy preview/function/environment context differs from production or hides release risk.
- `tool.neon` → active: database branch, migration, connection, or preview-data workflow is mistaken for production-safe data change.
- `tool.resend` → active: transactional email integration sends to real users, leaks data, or lacks delivery/error evidence.
- `tool.vitest` → active: unit/component tests pass but are weak, misconfigured, or treated as full product proof.
- `tool.storybook` → active: isolated UI stories look correct while app states, accessibility, or design-code drift remain untested.
- Deferred ecosystem tool → `TOOL_REGISTER.md` coverage audit first; use companion card and current vendor docs instead of pretending no route exists.

<!-- VCB:STOP_RETRIEVAL reason="by_failure_mode_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_failure_mode -->
