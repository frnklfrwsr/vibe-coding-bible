---
id: vcb.index.by_tool_category
title: INDEX_BY_TOOL_CATEGORY
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.by_tool_category version=0.41.0-draft.chunk40 -->

# INDEX_BY_TOOL_CATEGORY

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Tool-Card Inventory Policy

- Canonical active tool-card inventory lives in `TOOL_REGISTER.md` and the consolidated `README.md` tool-card inventory.
- This index keeps semantic category routes and does not maintain generation-specific aggregate inventory blocks.
- When adding or activating tools, route the smallest active tool card inside the relevant semantic sections before chapter, workflow, shortcut, or planned fallbacks.

## Core Codex surfaces
- `tool.codex` → active: primary OpenAI/Codex tool-family card and surface-selection hub
- `tool.codex_app` → active: desktop/local command-center surface for supervised threads, review, Git, worktrees, and app/browser workflows
- `tool.codex_cli` → active: terminal-native local Codex surface for shell-backed repo work
- `tool.codex_ide_extension` → active: IDE-context surface for open files, selections, file references, and cloud handoff
- `tool.codex_cloud` → active: cloud/background delegation surface for isolated review-later tasks
- `tool.codex_github_review` → active: GitHub PR review signal, not merge approval
- `tool.codex_exec` → active: non-interactive Codex CLI mode for scripts, CI-style runs, and structured reports
- `tool.codex_worktrees` → active: worktree isolation for parallel local/app tasks and automation change separation
- `tool.codex_subagents` → active: parallel specialist agents for bounded analysis, exploration, and disjoint implementation work
- `tool.codex_automations` → active: recurring/report-first Codex background work with review owner and stop conditions
- `tool.codex_computer_use` → active: desktop GUI operation with app permissions, visible-state risk, and human supervision
- `tool.codex_browser` → active: in-app rendered-page preview, comments, screenshots, and browser verification
- `tool.codex_chrome_extension` → active: signed-in Chrome browser workflows with website approvals and account-risk controls

## Persistent guidance and customization tools
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks
## Review, security, and CI tools
- `tool.github` → active: repository collaboration, pull requests, branch protection, issues, and code-review source of truth
- `tool.github_actions` → active: CI workflows, check evidence, secrets, token permissions, and repository automation
- `tool.github_dependabot` → active: dependency alerts, security update PRs, version update PRs, and dependency-maintenance queue
- `tool.openssf_scorecard` → active: supply-chain health signals, repository hardening checks, and dependency-adoption risk review
- `tool.codex_github_review` → active
- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation
- `tool.codex_exec` → active

## Development-stack and verification tools

- `tool.playwright` → active: browser/end-to-end tests, screenshots, traces, and UI verification evidence
- `tool.vitest` → active: Vite-native unit/component tests, watch-mode feedback, test evidence, and CI-adjacent JavaScript verification
- `tool.storybook` → active: component workshop, isolated UI states, component documentation, interaction tests, and design-handoff evidence
- `tool.npm` → active: JavaScript package manifests, scripts, lockfiles, installs, and audit evidence
- `tool.github_dependabot` → active: dependency alerts, security update PRs, version update PRs, and dependency-maintenance queue
- `tool.openssf_scorecard` → active: supply-chain health signals, repository hardening checks, and dependency-adoption risk review

## Source/update maintenance tools
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `vcb.chapter.maintaining_updating_bible` → active
- `tool.github_actions` → active: CI workflow/check evidence and scheduled source/update maintenance automation
- `tool.codex_exec` → active
## Unofficial tool and external-content risk

- `vcb.field.chatgpt_pm_codex_implementer` → active needs_more_evidence when tool split between planning AI and Codex implementation is being evaluated
- `vcb.field.fresh_agent_review` → active reproduced when tool use includes independent AI review before commit
- `vcb.field.multi_agent_review_consensus` → active needs_more_evidence when multiple AI tools or agents are used for review
- `vcb.field.contract_first_segmented_handoffs` → active candidate when multi-tool planning-to-Codex handoffs need one reviewed segment contract
- `vcb.field.agents_md_first` and `vcb.field.lessons_file_loop` → active candidates when tool choice is becoming durable repo guidance
- `vcb.chapter.field_notes_unofficial_practices` → active fallback
- `vcb.chapter.risk_managed_shortcuts` → active companion
- `vcb.shortcut.unofficial_tools` → active: unofficial tool adoption requires disposable evaluation and trust-boundary review

## AI coding and planning tools

- `tool.chatgpt` → active: planning, explanation, product thinking, source-backed research synthesis, and data/document analysis before implementation
- `tool.claude` → active: alternate AI review, architecture critique, long-form explanation, and source-checked second-opinion analysis
- `tool.cursor` → active: AI IDE-native planning, local multi-file edits, diff review, and supervised agentic coding workflows
- `tool.github_copilot` → active: GitHub/IDE-native suggestions, chat, repository-connected coding help, and PR/branch-adjacent assistance
- `tool.windsurf` → active: agentic AI IDE workflows with Cascade-style planning, editing, tool calls, checkpoints, and plugin support
- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points


## Browser-dev, app-builder, and UI-generation tools

- `tool.replit` → active: browser-based prototyping, hosted development, learning apps, and quick demo publishing with review/exit-path guardrails
- `tool.lovable` → active: AI full-stack app-builder for product sketches, MVP flow validation, generated app review, and publish/handoff guardrails
- `tool.bolt` → active: browser-based website/app/mobile prototype builder with token, dependency, generated-code, and publish-review guardrails
- `tool.v0` → active: AI UI/frontend generation for high-fidelity screens, design-system prototypes, and reviewable frontend starting points
## Hosting backend auth payments and observability

- `tool.github` → active companion: repository hosting, branches, PRs, review, and merge-gate source of truth
- `tool.vercel` → active: hosting, preview deployments, environment separation, deployment evidence, and production promotion guardrails
- `tool.cloudflare` → active: DNS, CDN/security controls, Workers, Pages, edge deployment, and domain/routing evidence
- `tool.netlify` → active: site deploys, deploy previews, functions, deploy contexts, and rollback/deployment evidence
- `tool.supabase` → active: Postgres database/backend/auth/storage, schema/RLS, migrations, backups, functions, and data-access guardrails
- `tool.neon` → active: serverless Postgres, database branches, preview database workflows, connection evidence, and migration review
- `tool.stripe` → active: payments, subscriptions, checkout, webhooks, billing state, and real-money fulfillment guardrails
- `tool.clerk` → active: authentication, user management, sessions, organizations, and application identity guardrails
- `tool.auth0` → active: IAM, OAuth/OIDC, applications/APIs, enterprise/B2B identity, and authorization architecture guardrails
- `tool.sentry` → active: error monitoring, tracing, performance, release evidence, and production debugging guardrails
- `tool.posthog` → active: product analytics, event taxonomy, session replay, feature flags, experiments, and product-evidence guardrails
- `tool.resend` → active: transactional email API, sending-domain review, templates, delivery evidence, and notification workflows

## Local dev design and project management

- `tool.docker` → active: local containers, Dockerfiles, Compose service stacks, reproducible development environments, and isolation/rebuild evidence
- `tool.figma` → active: collaborative design files, components, prototypes, Dev Mode handoff, screenshots, and design-intent evidence
- `tool.linear` → active: issues, projects, teams, workflows, cycles, and product/team execution hygiene

## Deferred ecosystem coverage routes

- Hosting/deployment gaps → `tool.render`, `tool.railway`, `tool.fly_io`, `tool.firebase`, `tool.aws`, `tool.gcp`, `tool.azure`, and `tool.digitalocean` are deferred/planned in `TOOL_REGISTER.md`; use active companions such as `tool.cloudflare`, `tool.netlify`, `tool.vercel`, `tool.supabase`, and `tool.docker` first.
- Email gaps → `tool.postmark`, `tool.sendgrid`, and `tool.mailgun` are deferred/planned; use `tool.resend` as the active email-delivery route.
- Docs/project/secrets/observability/payments/testing gaps → deferred/planned rows exist in `TOOL_REGISTER.md`; use the listed active companion card until a future scoped card is authored.

## Workflow/prompting cards that choose tool behavior
- `vcb.prompting.four_part_prompt` → active: turns tool use into scoped work orders
- `vcb.prompting.plan_first` → active: decides when planning or mutation is appropriate
- `vcb.prompting.context_management` → active: decides what context/tools should be exposed
- `vcb.prompting.acceptance_criteria` → active: defines evidence for tool output
- `vcb.workflow.unknown_codebase` → active: read-only tool use before mutation
- `vcb.workflow.feature_slicing` → active: bounded implementation with minimal tool sprawl
- `vcb.workflow.bug_repro` → active: repro and check tools before speculative fixes
- `vcb.workflow.testing` → active: test/check tool routing

## Tool-category concept anchors
- API/backend tools → `vcb.concepts.api_basics`, `vcb.concepts.frontend_backend` → active
- Database/backend tools → `vcb.concepts.database_schema`, `vcb.concepts.migration` → active
- Auth tools → `vcb.concepts.authentication`, `vcb.concepts.authorization` → active
- Package/dependency tools → `vcb.concepts.dependency` → active
- CI/repo tools → `vcb.concepts.ci`, `vcb.concepts.test`, `vcb.concepts.typecheck`, `vcb.concepts.lint`, `vcb.concepts.build_step` → active
- Observability tools → `vcb.concepts.observability` → active
- Release/ops tools → `vcb.concepts.feature_flag`, `vcb.concepts.rollback` → active

## Codex built-in feature surfaces
- `tool.codex_worktrees` → active: worktree isolation for parallel local/app tasks and automation change separation
- `tool.codex_subagents` → active: parallel specialist agents for bounded analysis, exploration, and disjoint implementation work
- `tool.codex_automations` → active: recurring/report-first Codex background work with review owner and stop conditions
- `tool.codex_computer_use` → active: desktop GUI operation with app permissions, visible-state risk, and human supervision
- `tool.codex_browser` → active: in-app rendered-page preview, comments, screenshots, and browser verification
- `tool.codex_chrome_extension` → active: signed-in Chrome browser workflows with website approvals and account-risk controls
- `vcb.codex.app` → active
- `vcb.codex.cli` → active
- `vcb.codex.ide_extension` → active
- `vcb.codex.cloud` → active
- `vcb.codex.github_review` → active
- `vcb.codex.automations` → active
- `vcb.codex.subagents` → active
- `vcb.codex.computer_use` → active

## Codex feature/topic anchors
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

- `vcb.codex.app` → active: Codex App
- `vcb.codex.cli` → active: Codex CLI
- `vcb.codex.ide_extension` → active: Codex IDE Extension
- `vcb.codex.cloud` → active: Codex Cloud / Web
- `vcb.codex.github_review` → active: Codex GitHub PR Review
- `vcb.codex.config` → active: Codex Config
- `vcb.codex.agents_md` → active: AGENTS.md
- `vcb.codex.skills` → active: Codex Skills
- `vcb.codex.mcp` → active: MCP for Codex
- `vcb.codex.hooks` → active: Codex Hooks
- `vcb.codex.automations` → active: Codex Automations
- `vcb.codex.subagents` → active: Codex Subagents
- `vcb.codex.computer_use` → active: Codex Computer Use
- `vcb.codex.feature_maturity` → active: companion feature mechanics
- `vcb.codex.changelog_monitoring` → active: companion feature mechanics
## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Tool-category routes for frontend, refactor, dependency, release, and documentation workflows
- `tool.npm` → active: JavaScript package manifests, scripts, lockfiles, installs, and audit evidence
- `tool.playwright` → active: browser/end-to-end tests, screenshots, traces, and UI verification evidence
- `tool.github_dependabot` → active: dependency alerts, security update PRs, version update PRs, and dependency-maintenance queue
- `tool.openssf_scorecard` → active: supply-chain health signals, repository hardening checks, and dependency-adoption risk review
- `tool.github_actions` → active: CI workflows, check evidence, secrets, token permissions, and repository automation
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

## Failure-mode routes by tool category
- `vcb.failure.dependency_bloat` → active: package-manager and dependency tooling risk
- `vcb.failure.ui_taste_gap` → active: browser, screenshot, and accessibility tooling risk
- `vcb.failure.ci_false_confidence` → active: CI/action tooling risk

## Failure modes involving tools, checks, and automation
- `vcb.failure.hallucinated_apis` → typecheckers, generated clients, schemas, API docs
- `vcb.failure.weakened_tests` → test runners, coverage, CI logs
- `vcb.failure.dependency_bloat` → package managers, lockfiles, dependency review, audits
- `vcb.failure.ui_taste_gap` → browser tools, screenshots, visual comparison, accessibility tooling
- `vcb.failure.ci_false_confidence` → CI providers, GitHub Actions, Codex non-interactive mode

## Constraint and budget routes for tool choices

- Operating-mode tool choice → `vcb.constraints.operating_mode`
- Attention-constrained delegation → `vcb.constraints.attention_budget`
- Usage, pricing, credits, and API-key workflow → `vcb.constraints.usage_burn`
- Cheapest reliable tool path → `vcb.constraints.scope_budget`
- High-throughput tool stacks and parallel work → `vcb.constraints.review_budget`
- Production-readiness tool gate → `vcb.constraints.production_quality`
- Recovery-aware tool adoption → `vcb.constraints.recovery_budget`
- Phase-aware tool selection → `vcb.constraints.build_vs_maintenance`

## Shortcut Harm-Reduction for Codex and Tool Use

- `vcb.shortcut.skipping_tests` → active: skip-test shortcut; route to smallest relevant verification guardrail
- `vcb.shortcut.accepting_looks_done` → active: looks-done shortcut; route to completion-evidence gate
- `vcb.shortcut.broad_agent_permissions` → active: broad-permission shortcut; route to sandbox/approval and blast-radius controls
- `vcb.shortcut.unattended_long_runs` → active: unattended-run shortcut; route to milestones, isolation, and evidence reports
- `vcb.shortcut.broad_refactor` → active: broad-refactor shortcut; route to behavior-preserving refactor boundaries
- `vcb.shortcut.context_dumping` → active: context-dumping shortcut; route to curated context packet control
- `vcb.shortcut.adding_dependencies_fast` → active: fast dependency shortcut; route to package decision and lockfile review guardrails
- `vcb.shortcut.reviewing_cloud_summary_only` → active: cloud-summary-only shortcut; route to diff/check/artifact review guardrail

## Security and permission shortcut routes for Codex and CI tools

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Setup/process shortcuts by tool category

- `vcb.shortcut.skipping_setup` → active: setup, package-manager, build/test toolchain.
- `vcb.shortcut.default_config_forever` → active: Codex config, sandbox, approvals, hooks.
- `vcb.shortcut.skipping_agents_md` → active: repo guidance and project instructions.
- `vcb.shortcut.overstuffing_agents_md` → active: guidance/context management.
- `vcb.shortcut.stale_agents_md` → active: guidance maintenance.
- `vcb.shortcut.unofficial_tools` → active: external tools, MCP, plugins, wrappers.
- `vcb.shortcut.hook_overreach` → active: hook and automation guardrails.
- `vcb.shortcut.trusting_external_tool_output` → active: MCP, browser, search, shell, plugin, or third-party tool output.

## Tool-stack and extensibility shortcut routes

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## Tool category routes for multi-AI/model-bias shortcuts

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

<!-- VCB:STOP_RETRIEVAL reason="by_tool_category_complete" -->
<!-- VCB:END_INDEX id=vcb.index.by_tool_category -->
