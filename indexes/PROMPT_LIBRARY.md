---
id: vcb.index.prompt_library
title: PROMPT_LIBRARY
artifact_type: index
version: 0.41.0-draft.chunk40
status: chunk_40_updated
created_on: '2026-06-08'
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: quarterly
---

<!-- VCB:BEGIN_INDEX id=vcb.index.prompt_library version=0.41.0-draft.chunk40 -->

# PROMPT_LIBRARY

> Status: Current routing index. Entries marked active have authored source files; entries marked planned are future routes.

## Work-order prompt skeleton
```text
Goal:
[What should be true after this task?]

Context:
[Files, logs, screenshots, routes, examples, constraints from AGENTS.md.]

Constraints:
[Allowed areas, forbidden areas, no new deps, compatibility, security, budget, attention mode.]

Done when:
[Observable behavior, checks, final report, known gaps.]
```
Routes: `vcb.chapter.four_part_prompt`, `vcb.prompting.four_part_prompt`, `vcb.prompting.acceptance_criteria`.

## Plan-only prompt
```text
Plan only. Do not edit files.
Identify likely files, current flow, risks, smallest safe milestone, checks, and rollback.
Reject vague plans. Ask questions only if blocked.
```
Routes: `vcb.chapter.plan_first_code_second`, `vcb.prompting.plan_first`, `vcb.prompting.context_management`.

## Read-only unknown-codebase prompt
```text
Read-only. Do not edit files.
Map the repo: purpose, entrypoints, package manager, commands, tests, data/request flow, risky areas, and files worth reading first.
Cite files/functions for each claim.
```
Routes: `vcb.chapter.understanding_unknown_codebase`, `vcb.workflow.unknown_codebase`.

## Feature-slice prompt
```text
Implement only the first visible milestone.
Keep the diff reviewable. Avoid new dependencies and forbidden areas.
Run the smallest relevant check and report changed files, checks, risks, and gaps.
```
Routes: `vcb.chapter.feature_slicing`, `vcb.workflow.feature_slicing`, `vcb.prompting.acceptance_criteria`.

## Bug reproduction prompt
```text
Start by reproducing the bug if feasible.
Then explain root cause, patch narrowly, add regression coverage when appropriate, rerun the same check, and report evidence.
```
Routes: `vcb.chapter.debugging_with_reproduction`, `vcb.workflow.bug_repro`.

## Test-writing prompt
```text
Add behavior-focused tests for this change.
Follow nearby test style. Do not weaken assertions. Prove the user-facing behavior, not just implementation details.
```
Routes: `vcb.chapter.writing_updating_tests`, `vcb.workflow.testing`.

## Frontend state-matrix prompt

Routes: `tool.figma` → active when design files, components, prototype flows, Dev Mode handoff, or screenshot/spec evidence are source material; `tool.v0` → active when UI generation, design-system screens, or frontend sketches are needed; `tool.playwright` → active when browser-check evidence, screenshots, traces, or end-to-end tests are needed; `tool.replit` → active companion for hosted browser demos; `tool.lovable` → active companion for app-builder UI/back-end flow checks; `tool.bolt` → active companion for browser app prototypes; `tool.github_actions` → active when checks run in CI; `vcb.workflow.frontend_work` → active companion; `vcb.workflow.visual_qa` → active companion; `vcb.workflow.accessibility_review` → active companion; `vcb.chapter.frontend_work` → active fallback.

```text
Implement or review this UI against loading, empty, error, success, disabled, mobile, keyboard, and accessibility basics.
Use existing components/design tokens and provide browser-check evidence.
```

## Refactor plan prompt
```text
Plan only first.
Refactor one named boundary without behavior change. List affected files, invariant behavior, checks, rollback point, and smallest first slice.
```
Routes: `vcb.chapter.refactoring_without_breaking_everything` → active.

## No-new-dependency prompt
```text
Solve this without adding a new dependency first.
If a dependency is still justified, explain alternatives, maintenance cost, security/license/bundle risk, and rollback.
```
Routes: `tool.npm` → active; `tool.github_dependabot` → active; `tool.openssf_scorecard` → active; `vcb.workflow.dependency_decisions` → active companion; `vcb.chapter.dependency_package_framework_decisions` → active fallback.

## Review-diff prompt
```text
Review the actual diff, not the summary.
Flag scope creep, deleted logic, weakened tests, new dependencies, auth/security/data behavior, migrations, deployment/config, and missing checks.
```
Routes: `vcb.chapter.reviewing_codex_output` → active.

## PR review prompt
```text
Review this PR as an additional signal, not merge approval.
Focus on serious regressions, missing tests, security issues, data loss, deployment risk, and behavior changes not described by the PR.
```
Routes: `tool.github` → active; `tool.github_actions` → active when checks/artifacts matter; `tool.codex_github_review` → active companion when Codex PR review is involved; `vcb.workflow.github_pr_review` → active companion; `vcb.chapter.github_pr_review_with_codex` → active fallback.

## Security review prompt
```text
Threat-model this change before style feedback.
Focus on secrets, auth, authorization, PII, payments, file uploads, redirects, injection, dependencies, and prompt-injection exposure.
```
Routes: `tool.codex_security` → active; `vcb.safety.security_review` → active companion; `vcb.chapter.security_for_vibe_coders` → active fallback.

## CI/non-interactive report prompt
```text
Run in report-only mode first.
Summarize findings, commands/checks, changed files if any, permissions used, secrets avoided, and the next safe mutation step.
```
Routes: `tool.github_actions` → active; `tool.codex_exec` → active companion; `vcb.workflow.ci_noninteractive` → active companion; `vcb.chapter.ci_noninteractive_github_actions` → active fallback.

## Cloud delegation prompt
Routes: `tool.codex_cloud` → active; `tool.codex_worktrees` → active; `vcb.shortcut.unattended_cloud_delegation` → active; `vcb.shortcut.ambiguous_cloud_task` → active; `vcb.shortcut.cloud_task_without_context` → active; `vcb.shortcut.parallel_cloud_sprawl` → active.
```text
Delegate only a scoped, branch/worktree-isolated task.
Do not touch secrets, production config, auth, billing, migrations, or deployment without stopping. Return a reviewable diff or report.
```
Routes: `vcb.chapter.cloud_delegation_parallel_work` → active.

## Subagent review prompt
Routes: `tool.codex_subagents` → active; `vcb.shortcut.conflicting_parallel_agents` → active; `vcb.shortcut.parallel_cloud_sprawl` → active; `vcb.shortcut.parallel_agents_edit_same_files` → active.
```text
Use subagents for independent analysis, not overlapping edits.
Assign each subagent one concern: security, tests, performance, docs, architecture, or failure modes. Merge findings by severity.
```
Routes: `vcb.shortcut.subagent_swarm` → active; `vcb.shortcut.parallel_agents_edit_same_files` → active; `vcb.chapter.subagents_parallel_thinking` → active.

## Automation design prompt
Routes: `tool.codex_automations` → active; `tool.codex_worktrees` → active; `vcb.shortcut.automation_spam` → active; `vcb.shortcut.automation_mutation_without_review` → active; `vcb.codex.automations` → active.
```text
Design a report-only automation first.
Define cadence, scope, allowed reads, forbidden actions, report format, signal/noise threshold, stop condition, and first-run manual review.
```
Routes: `vcb.chapter.automations_recurring_work` → active.

## Browser/GUI task prompt
Routes: `tool.codex_browser` → active; `tool.codex_computer_use` → active; `tool.codex_chrome_extension` → active; `vcb.shortcut.browser_clicking_without_repro` → active; `vcb.shortcut.logged_in_browser_secrets` → active; `vcb.codex.computer_use` → active.
```text
Use browser or GUI control only for the exact flow named here.
Avoid production consoles and sensitive logged-in state unless explicitly approved. Report screenshots/observations, steps, and risks.
```
Routes: `vcb.chapter.computer_use_browser_gui_tasks` → active.

## Team workflow promotion prompt
Routes: `tool.linear` → active when repeated workflow should become issue/project/status/team process; `tool.codex_agents_md` → active; `tool.codex_config` → active; `tool.codex_skills` → active; `tool.codex_hooks` → active; `tool.codex_mcp` → active; `tool.codex_automations` → active; `tool.codex_github_review` → active; `tool.codex_exec` → active; `vcb.chapter.prompt_library_to_team_workflow` → active fallback.

```text
We have repeated this mistake/workflow. Recommend the smallest durable artifact: prompt snippet, AGENTS.md rule, config default, skill, hook, automation, PR guidance, or CI check.
```

## Failure-mode diagnosis prompt
```text
Diagnose this Codex failure without blame.
Classify the likely failure mode, missing control, smallest correction, durable rule to add, and whether this needs a topic-card or playbook update.
Do not accept a generic "Codex messed up" explanation. Tie the diagnosis to evidence: diff, files, logs, tests, screenshots, dependency changes, or missing context.
```
Routes: `vcb.chapter.failure_modes_codex_work` → active; active atomic failure-mode routes:
- `vcb.failure.hallucinated_apis` → active: plausible API, route, field, package, flag, callback, or response-shape claim lacks contract evidence
- `vcb.failure.context_pollution` → active: stale, noisy, excessive, or contradictory context steers the run
- `vcb.failure.weakened_tests` → active: tests pass after assertions, mocks, snapshots, skips, or coverage are weakened
- `vcb.failure.broad_refactor_drift` → active: cleanup/refactor drifts into behavior change, migration, or rewrite
- `vcb.failure.dependency_bloat` → active: package/framework addition creates unjustified maintenance or supply-chain drag
- `vcb.failure.ui_taste_gap` → active: UI renders but lacks state, responsive, accessibility, or product-fit evidence
- `vcb.failure.ci_false_confidence` → active: green CI or agent summary is treated as broader proof than configured checks support
- `vcb.failure.done_claim_without_evidence` → active: completion claim is not backed by changed files, commands, screenshots, logs, or acceptance evidence

### Failure-mode selector prompt
```text
Pick the most likely VCB failure-mode card for this situation.

Situation:
Observed output:
Evidence available:
Evidence missing:
Risk area:

Return:
- primary failure mode,
- secondary failure mode, if any,
- the unsupported claim or shortcut,
- smallest evidence check,
- recovery action,
- durable guardrail to add.
```

## New project bootstrap prompt

Routes: `tool.docker` → active when reproducible local services, containers, or Dockerized setup matter; `tool.figma` → active when design/prototype/handoff evidence matters; `tool.linear` → active when issue/project ownership or team planning matters; `tool.vercel` → active when the app needs hosting/preview deployment; `tool.supabase` → active when backend/database/auth/storage is needed; `tool.clerk` → active when app auth/user management is needed; `tool.auth0` → active when IAM/API/enterprise auth is needed; `tool.stripe` → active when payments/subscriptions are in scope; `tool.sentry` → active when production error/performance evidence is needed; `tool.posthog` → active when product analytics/replay/feature flags are needed; `tool.github` → active; `tool.npm` → active; `tool.github_actions` → active; `tool.playwright` → active when web UI is in scope; `tool.codex_agents_md` → active companion; `vcb.chapter.codex_playbooks` → active fallback; `vcb.chapter.installing_and_configuring_codex` → active fallback; `vcb.chapter.first_serious_app` → active fallback.

```text
Goal:
Bootstrap a new project/repo with the smallest maintainable starting structure for [app/tool/library].

Context:
Product idea:
Preferred stack, if any:
Constraints:
Must avoid:

Constraints:
- Do not add unnecessary dependencies.
- Keep setup/run/test commands simple.
- Add README or starter instructions.
- Add AGENTS.md only if this project will continue beyond a throwaway prototype.
- Use fake credentials and example environment variables only.

Done when:
- Project can install/start/build or run its first check.
- Basic file structure is explained.
- README has setup/run/check commands.
- Initial Git checkpoint is recommended.
- Known shortcuts and next hardening steps are listed.
```

## Playbook selector prompt
```text
Select the smallest VCB playbook for this task and tune it for project type, risk level, budget posture, attention mode, forbidden areas, checks, and rollback.
```
Routes: `vcb.chapter.codex_playbooks` → active.

## Release notes playbook prompt
```text
Generate release notes from commits/PRs/issues.
Separate user-visible changes, fixes, breaking changes, migrations, known issues, and verification evidence. Do not invent impact not present in the source material.
```
Routes: `vcb.chapter.codex_playbooks` → active.

## Production-error investigation prompt
```text
Read-only first. Summarize symptoms, timeline, likely affected systems, likely root cause hypotheses, evidence needed, safe mitigation, rollback options, and what not to change yet.
```
Routes: `tool.sentry` → active for production error, trace, performance, release, and session-context evidence; `tool.posthog` → active companion for product-behavior, replay, funnel, and feature-flag context; `tool.vercel` → active companion for deployment, environment, runtime, logs, and rollback context; `tool.github_actions` → active companion when checks/release artifacts matter; `tool.supabase` → active when database/backend/RLS/functions are involved; `tool.stripe` → active when payment/subscription/webhook state is involved; `vcb.workflow.bug_repro` → active companion; `vcb.chapter.codex_playbooks` → active fallback; `vcb.chapter.debugging_with_reproduction` → active fallback.

## API endpoint prompt
```text
Add one endpoint only. Preserve existing API conventions, validation, auth/authorization behavior, tests, docs, and error states. State any compatibility risk.
```
Routes: `tool.supabase` → active when backend/database/functions/RLS/storage are involved; `tool.auth0` → active when API authorization, OAuth/OIDC, audiences, scopes, or resource-server behavior is involved; `tool.clerk` → active when session/user/org context owns app authentication; `tool.stripe` → active when payment, subscription, webhook, customer, or entitlement state is involved; `tool.sentry` → active when API error/tracing evidence is required; `vcb.failure.hallucinated_apis` → active companion; `vcb.safety.security_review` → active companion; `vcb.chapter.codex_playbooks` → active fallback; `vcb.chapter.security_for_vibe_coders` → active fallback.

## Dependency migration prompt
```text
Plan first. Identify current version/use sites, migration notes, breaking changes, lockfile impact, tests/checks, rollback path, and whether the migration should be split.
```
Routes: `tool.github_dependabot` → active when update/advisory PRs are involved; `tool.npm` → active for package manifests, scripts, lockfiles, installs, and audit evidence; `tool.openssf_scorecard` → active for supply-chain posture; `vcb.workflow.dependency_update_review` → active companion; `vcb.workflow.dependency_decisions` → active companion; `vcb.chapter.codex_playbooks` → active fallback; `vcb.chapter.dependency_package_framework_decisions` → active fallback.

## Dead-code removal prompt
```text
Prove code is unused before deleting. Check references, routes, exports, tests, build artifacts, runtime entrypoints, and rollback path. Keep the deletion diff small.
```
Routes: `vcb.chapter.codex_playbooks` → active; `vcb.chapter.refactoring_without_breaking_everything` → active.

## Docs improvement prompt
```text
Update docs from the current repo behavior. Cite files or commands. Do not invent features. Include setup, commands, edge cases, and known limitations.
```
Routes: `vcb.chapter.codex_playbooks` → active.

## MVP prototype prompt

Routes: `tool.figma` → active for prototype flow and design-intent evidence; `tool.linear` → active when MVP scope/ownership must be tracked; `tool.docker` → active when local services or reproducible setup are required; `tool.replit` → active for browser-hosted prototype/demo loops; `tool.lovable` → active for full-stack app-builder MVP sketches; `tool.bolt` → active for browser website/app/mobile prototypes; `tool.v0` → active for high-fidelity UI/frontend sketches; `vcb.constraints.build_vs_maintenance` → active companion; `vcb.chapter.codex_playbooks` → active fallback; `vcb.chapter.first_serious_app` → active fallback.

```text
Build a prototype plan for this MVP without pretending the prototype is production.
Idea:
User flow:
Data boundary: [fake / staging / production]
Allowed builder: [Replit / Lovable / Bolt / v0 / none]
Required evidence: [source/diff/browser screenshot/trace/test/PR]
Exit path: [discard / export / rewrite / harden / maintain]
List the smallest safe tool, the first slice, the review evidence, and what must happen before real users.
```

## Auth-sensitive hardening prompt

Routes: `tool.codex_security` → active; `tool.clerk` → active when Clerk owns authentication/session/user state; `tool.auth0` → active when Auth0 owns IAM/OIDC/OAuth/API access; `tool.supabase` → active when database/RLS/functions/storage are involved; `tool.stripe` → active when payments/subscriptions/entitlements are involved; `tool.sentry` → active when sensitive error/trace evidence must be filtered; `tool.posthog` → active when analytics/replay/flag privacy boundaries are involved; `vcb.safety.security_review` → active companion; `vcb.chapter.codex_playbooks` → active fallback; `vcb.chapter.security_for_vibe_coders` → active fallback.

```text
Do security review before implementation. Identify authn/authz boundaries, session/token handling, data access, abuse cases, tests, logging, rollback, and red lines.
```


## Production platform readiness prompt

Routes: `tool.vercel` → active for deployment and preview evidence; `tool.cloudflare` → active for DNS/CDN/edge/domain/routing evidence; `tool.netlify` → active for deploy previews/functions/deploy contexts; `tool.supabase` → active for backend/database/auth/storage; `tool.neon` → active for serverless Postgres branches/connections/migration evidence; `tool.clerk` → active for auth/user management; `tool.auth0` → active for IAM/API authorization; `tool.stripe` → active for payments/subscriptions; `tool.resend` → active for transactional email/templates/sending-domain evidence; `tool.sentry` → active for error/performance monitoring; `tool.posthog` → active for analytics/replay/feature flags; `vcb.chapter.first_serious_app` → active fallback; `vcb.chapter.senior_engineer_checklist` → active fallback.

```text
Before calling this production-ready, list the evidence for hosting, database, auth, payment, observability, analytics, rollback, privacy, secrets, and support. For each tool, identify owner, environment, fake-versus-real data boundary, verification artifact, and rollback or disable path.
```

## Senior checklist prompt
```text
Apply the senior checklist before accepting this work.
Check clean working tree, scope, done criteria, diff, tests/checks, dependencies, auth/security/data behavior, rollback, and durable guidance updates.
```
Routes: `tool.docker` → active for local reproducibility/containerized service evidence; `tool.figma` → active for design-handoff/UI-state evidence; `tool.linear` → active for issue/project/status ownership evidence; `tool.vercel` → active for deployment/environment/release evidence; `tool.supabase` → active for database/backend/auth/storage evidence; `tool.neon` → active for serverless Postgres, branches, connections, and migration evidence; `tool.clerk` → active when Clerk owns auth/user/session state; `tool.auth0` → active when Auth0 owns IAM/API authorization; `tool.stripe` → active when payments/subscriptions/webhooks are in scope; `tool.resend` → active when transactional email, templates, notifications, or delivery evidence is in scope; `tool.sentry` → active for production error/performance evidence; `tool.posthog` → active for analytics/replay/feature-flag evidence; `vcb.constraints.production_quality` → active companion; `vcb.constraints.recovery_budget` → active companion; `vcb.chapter.senior_engineer_checklist` → active fallback.

## Field-practice assessment prompt

Routes: `vcb.field.chatgpt_pm_codex_implementer`, `vcb.field.fresh_agent_review`, `vcb.field.context_reset_between_tasks`, `vcb.field.agents_md_first`, `vcb.field.skeleton_todo_first`, `vcb.field.strict_typecheck_lint_gates`, `vcb.field.greenfield_vs_production_rule`, `vcb.field.lessons_file_loop`, `vcb.field.multi_agent_review_consensus`, `vcb.field.contract_first_segmented_handoffs`; `vcb.chapter.field_notes_unofficial_practices` → active fallback; `vcb.chapter.maintaining_updating_bible` → active companion.

```text
Assess this Codex field practice before I adopt it.

Practice:
Source:
Project context:
Risk areas:

Return:
- evidence label,
- durable principle,
- volatile ritual,
- safest test,
- blast radius,
- recoverability,
- promotion rule,
- obsolescence trigger,
- decision: test, narrow, promote locally, or retire.
```

## Bible update prompt
Routes: `tool.codex_changelog_monitoring` → active; `tool.codex_feature_maturity` → active; `vcb.chapter.maintaining_updating_bible` → active fallback.

```text
Review this VCB topic for staleness.

Topic ID:
File:
Current date:
Relevant source IDs:

Update metadata first. Check official OpenAI/vendor docs. Separate stable principle from volatile product detail. Add deprecation notes instead of deleting obsolete guidance.
```
## Risk-managed shortcut prompt

- `vcb.chapter.risk_managed_shortcuts` → active

```text
I know this is a shortcut. Help me make it safer.

Project type:
What I want to skip:
What must not break:
Real users/data/secrets/money involved? yes/no
Current rollback path:

Give risk level, blast radius, recoverability, minimum guardrails, and recovery plan before proceeding.
```

## Operating mode selection prompt

- `vcb.chapter.choosing_codex_operating_mode` → active

```text
Choose the right Codex operating mode for this task.

Budget:
Human attention:
Project phase:
Project type:
Risk if wrong:
Recoverability:
Available tests/checks:

Recommend the smallest reliable workflow. State what to do in Codex, what to do manually, and where to spend or save usage.
```

## Tool cost-benefit prompt

Routes: `tool.docker` → active for local dev/container choice; `tool.figma` → active for design/prototyping handoff choice; `tool.linear` → active for project-management/workflow choice; `tool.replit` → active for browser-dev/hosted prototype tool choice; `tool.lovable` → active for app-builder/full-stack prototype tool choice; `tool.bolt` → active for browser app/mobile prototype tool choice; `tool.v0` → active for UI-generation/frontend sketch tool choice; `tool.chatgpt` → active for planning/explanation; `tool.claude` → active for alternate AI critique; `tool.cursor` → active for AI IDE implementation; `tool.github_copilot` → active for GitHub/IDE-native AI coding help; `tool.windsurf` → active for agentic AI IDE workflows; `vcb.chapter.tool_stack_catalog` → active fallback; `vcb.chapter.when_to_use_other_ais` → active fallback.

```text
Evaluate whether this tool is worth adding now.

Tool:
Milestone it helps reach:
Current alternative:
Setup cost:
Monthly cost or pricing volatility:
Maintenance cost:
Debugging cost:
Lock-in risk:
Hidden failure mode:

Recommend add now, delay, or replace with a simpler option. Do not recommend maximal stacks.
```

## Model limitation guardrail prompt

- `vcb.shortcut.trusting_estimates_before_inspection` → active: require evidence before accepting estimates
- `vcb.shortcut.ignoring_model_biases` → active: name model-bias risks before trusting confident output
- `vcb.shortcut.consensus_as_correctness` → active: separate multi-model agreement from verification
- `vcb.shortcut.best_of_n_without_review` → active: prevent best-looking answer selection without checks
- `vcb.shortcut.cherry_picking_ai_answers` → active: prevent confirmation-biased answer selection
- `vcb.chapter.what_codex_is_bad_at` → active
- `vcb.chapter.model_biases_failure_biases_bad_estimates` → active

```text
Before estimating or declaring this done, inspect the repo evidence.

List:
- files inspected,
- unknowns,
- assumptions,
- confidence level,
- checks needed,
- what could make the estimate wrong.

Treat final summaries as claims until supported by diff and command output.
```

## Workflow/prompting topic-card selector
- `vcb.prompting.four_part_prompt` → active
- `vcb.prompting.acceptance_criteria` → active
- `vcb.prompting.plan_first` → active
- `vcb.prompting.context_management` → active
- `vcb.workflow.unknown_codebase` → active
- `vcb.workflow.feature_slicing` → active
- `vcb.workflow.bug_repro` → active
- `vcb.workflow.testing` → active

```text
Choose the smallest prompt or workflow card for this task.

Task:
Repo/context:
Risk if wrong:
Available checks:

Return:
- which card to use first,
- the exact prompt skeleton to start from,
- what context is required,
- what done evidence must be produced,
- what shortcut this avoids.
```

## Foundational concept explainer prompt
- `vcb.concepts.api_basics` → active
- `vcb.concepts.frontend_backend` → active
- `vcb.concepts.database_schema` → active
- `vcb.concepts.authentication` → active
- `vcb.concepts.authorization` → active
- `vcb.concepts.state` → active
- `vcb.concepts.async` → active
- `vcb.concepts.dependency` → active
- `vcb.concepts.test` → active
- `vcb.concepts.typecheck` → active
- `vcb.concepts.lint` → active
- `vcb.concepts.migration` → active
- `vcb.concepts.environment_variable` → active
- `vcb.concepts.build_step` → active
- `vcb.concepts.ci` → active
- `vcb.concepts.feature_flag` → active
- `vcb.concepts.observability` → active

```text
Explain this concept before editing:
[concept name]

Use the VCB concept card if available.
Give me:
- what it means in plain language,
- what file or behavior in this repo it affects,
- what shortcut would be risky here,
- the smallest check that proves we handled it correctly.
```

## Codex feature selection prompt
- `tool.codex_feature_maturity` → active: Codex maturity-label governance, feature-readiness posture, fallback requirements, and review cadence
- `tool.codex_changelog_monitoring` → active: official Codex release monitoring, targeted VCB maintenance, deprecation watch, and source/route refreshes
- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

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
- `tool.codex_security` → active: Codex Security plugin/cloud scans, security diff review, finding validation, threat-model-informed triage, and reviewed fix preparation
- `vcb.codex.app` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.cli` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.ide_extension` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.cloud` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.github_review` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.config` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.agents_md` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.skills` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.mcp` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.hooks` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.automations` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.subagents` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.computer_use` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.feature_maturity` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.codex.changelog_monitoring` → active: companion feature mechanics and feature-specific prompt patterns
- `vcb.concepts.observability` → active
## Review, Safety, and Verification Workflow Cards

- `vcb.workflow.codex_output_review` → active: Codex output review by diff, checks, and risk
- `vcb.workflow.reviewing_diffs` → active: local diff review and hunk-level risk scan
- `vcb.workflow.github_pr_review` → active: Codex-assisted PR review without treating AI as approval
- `vcb.safety.security_review` → active: trust-boundary, auth, data, and exploitability review
- `vcb.safety.secrets` → active: credentials, tokens, CI secrets, browser/session exposure
- `vcb.workflow.ci_triage` → active: failed-check and log triage before mutation
- `vcb.workflow.ci_noninteractive` → active: Codex in CI with least privilege and auditable outputs
- `vcb.safety.production_red_lines` → active: hard-stop gates for production-risk work

## Frontend/refactor/dependency/docs workflow prompt cards
- `vcb.workflow.frontend_work` → active: frontend state, responsive behavior, and browser evidence
- `vcb.workflow.visual_qa` → active: screenshot and visual-regression review
- `vcb.workflow.accessibility_review` → active: accessibility checks, keyboard paths, labels, and WCAG-guided review
- `vcb.workflow.refactoring` → active: behavior-preserving refactor workflow with tests and diff review
- `vcb.workflow.dependency_decisions` → active: new dependency/package/framework decision workflow
- `vcb.workflow.dependency_update_review` → active: dependency update and lockfile review workflow
- `vcb.workflow.release_notes` → active: release-note drafting from verified change sources
- `vcb.workflow.documentation_updates` → active: documentation update workflow tied to code, docs, and release context

### Frontend verification prompt
```text
Goal: Verify this UI change across states, viewports, and interaction paths.
Context: Include target routes, screenshots/design references, commands, and constraints.
Constraints: Do not call it done from code inspection alone.
Done when: Report checked states, expected/actual, screenshots or browser evidence, accessibility notes, and remaining risks.
```
Routes: `vcb.workflow.frontend_work`; `vcb.workflow.visual_qa`; `vcb.workflow.accessibility_review`.

### Safe refactor prompt
```text
Refactor without changing observable behavior. First identify current behavior, risk points, tests/checks, smallest safe pass, and rollback path. Change only the agreed slice.
```
Routes: `vcb.workflow.refactoring`; `vcb.workflow.reviewing_diffs`; `vcb.workflow.testing`.

### Dependency review prompt
```text
Evaluate this dependency change before merging. Identify direct/transitive changes, lockfile impact, security/license risk, release-note evidence, compatibility risk, tests to run, and rollback.
```
Routes: `tool.github_dependabot` → active; `tool.npm` → active; `tool.openssf_scorecard` → active; `vcb.workflow.dependency_decisions` → active companion; `vcb.workflow.dependency_update_review` → active companion.

### Release notes and docs prompt
```text
Draft release notes or docs only from verified commits, PRs, code changes, and existing docs. Separate user-visible changes, breaking changes, migrations, fixes, known issues, and verification evidence.
```
Routes: `vcb.workflow.release_notes`; `vcb.workflow.documentation_updates`.

## Constraint and budget selector prompt

Routes:

- `vcb.constraints.operating_mode` → choose Codex surface, permission level, task size, and supervision rhythm
- `vcb.constraints.attention_budget` → adapt delegation to available human attention
- `vcb.constraints.usage_burn` → manage usage burn, retries, context size, and pricing-source checks
- `vcb.constraints.recovery_budget` → choose scope from rollback and repair cost
- `vcb.constraints.build_vs_maintenance` → adapt workflow by project phase
- `vcb.constraints.production_quality` → apply production-readiness evidence gate
- `vcb.constraints.scope_budget` → cheapest reliable workflow under constraint
- `vcb.constraints.review_budget` → high-throughput workflow with isolation and review bandwidth

Prompt:

```text
Before coding, identify the binding constraint for this task: money, usage, attention, time, review skill, recovery path, production risk, or project phase.
Then recommend:
1. Codex surface and permission level
2. task slice
3. context to provide and context to omit
4. expected usage/retry risk without quoting exact prices
5. required evidence before accepting completion
6. recovery plan
7. what must stay out of scope
Use current official sources or the dated pricing snapshot for exact pricing, limits, credits, or feature availability.
```

## Shortcut Harm-Reduction Prompt Selector

Use these atomic shortcut cards when the user is already moving fast and needs minimum guardrails instead of a lecture.

- `vcb.shortcut.skipping_tests` → active: ask for the smallest relevant verification command or manual flow
- `vcb.shortcut.accepting_looks_done` → active: ask for changed files, verification, skipped checks, and remaining risk
- `vcb.shortcut.broad_agent_permissions` → active: ask for minimum permission profile, forbidden areas, and approval gates
- `vcb.shortcut.unattended_long_runs` → active: ask for milestone, stop condition, isolation, and final evidence report
- `vcb.shortcut.broad_refactor` → active: ask for one refactor axis, behavior-preservation contract, and checks
- `vcb.shortcut.context_dumping` → active: ask for a curated context packet and source freshness labels
- `vcb.shortcut.adding_dependencies_fast` → active: ask for no-new-dependency first and a dependency decision memo
- `vcb.shortcut.reviewing_cloud_summary_only` → active: ask for a cloud-task review packet with diff, checks, artifacts, gaps, and out-of-scope edits

```text
The user is taking shortcut: [shortcut].
Do not moralize. Name the risk, identify blast radius, propose the minimum guardrail that changes the risk profile, and give a recovery path if they already took the shortcut.
```

## Codex maturity and changelog review prompt
Routes: `tool.codex_changelog_monitoring` → active; `tool.codex_feature_maturity` → active; `SOURCE_REGISTER.md` → active companion; `DEPRECATION_REGISTER.md` → active companion; `vcb.chapter.maintaining_updating_bible` → active fallback.

```text
Review current official Codex sources for [feature/surface/topic ID]. Classify each relevant update as no action, source-date refresh, volatile prose update, pricing snapshot review, deprecation/redirect update, semantic route repair, or new bounded-card proposal. Keep exact current labels, UI wording, command flags, and availability out of stable prose.
```

## Security and permission shortcut selector

Use when the human is about to grant a broad permission, expose a secret, run unattended mutation, or approve a sensitive app/browser/CI action.

```text
Classify this shortcut by blast radius: production GUI action, CI permission, CI secret, prototype secret, cloud secret, full-access automation, unattended mutation, or persistent app/site approval. Retrieve the matching `vcb.shortcut.*` card. Then give me: acceptable cases, bad-idea cases, minimum guardrails, recovery plan, and the smallest safer alternative.
```

Routes:

- `vcb.shortcut.production_console_computer_use` → active: production console computer use security/permission shortcut guardrails
- `vcb.shortcut.overbroad_ci_permissions` → active: overbroad ci permissions security/permission shortcut guardrails
- `vcb.shortcut.long_lived_ci_secrets` → active: long-lived ci secrets security/permission shortcut guardrails
- `vcb.shortcut.real_secrets_in_prototype` → active: real secrets in prototype security/permission shortcut guardrails
- `vcb.shortcut.cloud_work_with_real_secrets` → active: cloud work with real secrets security/permission shortcut guardrails
- `vcb.shortcut.full_access_automation` → active: full-access automation security/permission shortcut guardrails
- `vcb.shortcut.unattended_mutation` → active: unattended mutation security/permission shortcut guardrails
- `vcb.shortcut.always_allow_sensitive_apps` → active: always allow sensitive apps security/permission shortcut guardrails

## Setup/config/process shortcut selector

- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

Use when the user is taking a process shortcut around setup, config, AGENTS.md, hooks, external tools, or tool output.

Routes:

- `vcb.shortcut.skipping_setup` → active: require setup map before edit
- `vcb.shortcut.default_config_forever` → active: review config defaults and risky profiles
- `vcb.shortcut.skipping_agents_md` → active: promote repeated rules into minimal durable guidance
- `vcb.shortcut.overstuffing_agents_md` → active: prune AGENTS.md context dumps
- `vcb.shortcut.stale_agents_md` → active: verify old guidance against current repo
- `vcb.shortcut.unofficial_tools` → active: vet external tool source, permissions, credentials, and uninstall path
- `vcb.shortcut.hook_overreach` → active: keep hooks objective, fast, and scoped
- `vcb.shortcut.trusting_external_tool_output` → active: verify external tool output with source evidence before mutation

```text
The user is taking a setup/config/process shortcut: [shortcut]. Retrieve the matching Chunk 22 shortcut card. Give: acceptable cases, bad-idea cases, minimum guardrails, recovery plan, and the smallest durable process artifact that reduces future risk.
```

## Tool-sprawl/skill/process shortcut selector

- `tool.codex_agents_md` → active: durable repo/project guidance for repeated Codex expectations and local conventions
- `tool.codex_config` → active: user/project/profile defaults for approvals, sandbox posture, MCP, and repeatable Codex behavior
- `tool.codex_skills` → active: reusable workflow packages with scoped instructions, resources, and optional scripts
- `tool.codex_mcp` → active: external tool/context connections with server scope, auth, and provenance guardrails
- `tool.codex_hooks` → active: deterministic lifecycle scripts for narrow guardrails, logging, and validation checks

Use this when the human wants to add a skill, plugin, MCP server, hook, team process, or reusable playbook quickly.

```text
Classify this shortcut before we add durable process or tooling. Is it skill overkill, skill sprawl, tool sprawl, MCP sprawl, brittle hooks, process overhead for a tiny project, team workflow without a team, or blind playbook reuse? For the matching card, list acceptable case, bad trade, minimum guardrails, cheapest reliable path, and recovery plan.
```

- `vcb.shortcut.skill_overkill` → active: avoid creating a skill before a repeated workflow earns it
- `vcb.shortcut.skill_sprawl` → active: audit overlapping skills and disabled stale reusable workflows
- `vcb.shortcut.tool_sprawl` → active: add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: keep MCP servers scoped, allow-listed, and purpose-bound
- `vcb.shortcut.brittle_hooks` → active: keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: avoid heavyweight process before a tiny project earns it
- `vcb.shortcut.team_workflow_without_team` → active: use solo evidence workflow before team handoff process exists
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: tailor reusable playbooks to actual risk, scope, and done evidence

## Multi-AI/model-bias shortcut selector

Routes: `tool.chatgpt` → active; `tool.claude` → active; `tool.cursor` → active; `tool.github_copilot` → active; `tool.windsurf` → active; `vcb.shortcut.many_ais_same_files` → active companion; `vcb.shortcut.best_of_n_without_review` → active companion; `vcb.shortcut.consensus_as_correctness` → active companion; `vcb.shortcut.model_routing_guesswork` → active companion.

```text
I am using multiple AIs/models/agents for this task. Diagnose the shortcut risk. Route me to the relevant card: many AIs same files, parallel agents editing same files, best-of-N without review, cherry-picking AI answers, consensus as correctness, trusting estimates before inspection, ignoring model biases, model routing guesswork, or subagent swarm. Require evidence, file ownership, role separation, and one final integration/review gate.
```

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

## Repository/CI/dependency/QA tool-selection prompt

Routes: `tool.github` → active; `tool.github_actions` → active; `tool.github_dependabot` → active; `tool.npm` → active; `tool.playwright` → active; `tool.openssf_scorecard` → active.

```text
Choose the smallest repository/CI/dependency/QA tool for this job. Goal: [goal]. Repo state: [branch/PR/checks/package files]. Risk: [secrets/production/users/dependency/security]. Compare GitHub, GitHub Actions, Dependabot, npm, Playwright, and OpenSSF Scorecard. Recommend the smallest reliable evidence path, the review owner, and the rollback plan.
```

## AI coding/IDE/planning tool-selection prompt

Routes: `tool.chatgpt` → active for planning/explanation and source-backed synthesis; `tool.claude` → active for alternate AI critique; `tool.cursor` → active for AI IDE implementation; `tool.github_copilot` → active for GitHub/IDE-native AI coding help; `tool.windsurf` → active for agentic AI IDE workflows; `tool.codex` → active companion; `vcb.chapter.tool_stack_catalog` → active fallback; `vcb.chapter.when_to_use_other_ais` → active fallback.

```text
I need to choose an AI coding, AI IDE, planning, or alternate-review tool for this task. Compare only the smallest safe tool surfaces. Task: [task]. Repo state: [repo/PR/branch]. Required output: [plan/diff/review/checklist]. Risks: [secrets/users/money/production/dependencies]. Recommend the best tool, why not the others, the evidence artifact, and the review path.
```


## Browser-dev/app-builder/UI-generation tool-selection prompt

Routes: `tool.replit` → active; `tool.lovable` → active; `tool.bolt` → active; `tool.v0` → active; `tool.github` → active companion for repo ownership; `tool.npm` → active companion for dependency/package evidence; `tool.playwright` → active companion for browser evidence; `vcb.chapter.tool_stack_catalog` → active fallback.

```text
I need to choose a browser-dev, app-builder, or UI-generation tool for this task. Compare only Replit, Lovable, Bolt, and v0 unless another tool is explicitly necessary.
Goal:
Prototype or production-bound?
Data/secrets boundary:
Required artifact:
Review budget:
Exit path:
Recommend the smallest safe tool, why not the others, the evidence required, and what must happen before real users or production data.
```

## Local dev/design/project-management tool-selection prompt

Routes: `tool.docker` → active; `tool.figma` → active; `tool.linear` → active; `tool.github` → active companion for repo source-of-truth; `tool.github_actions` → active companion for CI/check evidence; `tool.playwright` → active companion for browser/design verification; `vcb.chapter.tool_stack_catalog` → active fallback.

```text
I need to choose or review a local-dev, design, or project-management tool for this task.
Goal:
Project phase:
Team size:
Risk if wrong:
Required artifact:
Review budget:

Compare Docker, Figma, and Linear only where relevant. Recommend the smallest safe tool path, what evidence it should produce, what it must not be trusted to prove, and what review/rollback path is required before handoff or production use.
```

## Hosting/backend/auth/payment/observability tool-selection prompt

Routes: `tool.vercel` → active; `tool.cloudflare` → active for DNS/CDN/edge/domain/routing; `tool.netlify` → active for deploy previews/functions/deploy contexts; `tool.supabase` → active; `tool.neon` → active for serverless Postgres/branching/preview databases; `tool.clerk` → active; `tool.auth0` → active; `tool.stripe` → active; `tool.resend` → active for transactional email/templates/sending domains; `tool.sentry` → active; `tool.posthog` → active; `vcb.chapter.tool_stack_catalog` → active fallback.

```text
Choose the smallest production-platform tool layer for this project. Separate hosting, database/backend, auth, payments, error monitoring, and product analytics. For each layer, say whether it is needed now, which tool owns it, what evidence proves it works, what data/secret/payment/user surface it can touch, and what can be deferred.
```

## Tool-catalog coverage audit prompt

Routes: `TOOL_REGISTER.md` → active coverage audit; `tool.cloudflare` → active for Cloudflare/edge/DNS; `tool.netlify` → active for Netlify/deploy previews/functions; `tool.neon` → active for Neon/Postgres branches; `tool.resend` → active for transactional email; `tool.vitest` → active for Vite-native tests; `tool.storybook` → active for component workshop/UI states.

```text
Audit this requested tool against the VCB tool catalog. First say whether the exact tool has an active card, deferred/planned row, alias/companion route, or explicit exclusion. Then choose the smallest active companion card, list what official docs must be checked, and state what evidence is required before trusting generated setup or output.
```

<!-- VCB:STOP_RETRIEVAL reason="prompt_library_complete" -->
<!-- VCB:END_INDEX id=vcb.index.prompt_library -->
