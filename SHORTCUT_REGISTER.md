---
id: vcb.register.shortcuts
title: SHORTCUT_REGISTER
artifact_type: register
version: 0.43.0-draft.chunk42
status: chunk_42_updated
created_on: 2026-06-08
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: monthly
---

<!-- VCB:BEGIN_REGISTER id=vcb.register.shortcuts version=0.43.0-draft.chunk42 -->

# SHORTCUT_REGISTER

**Purpose:** Treat shortcuts as first-class risk-managed guidance. The register does not moralize. It explains tradeoffs, blast radius, recoverability, minimum guardrails, and recovery plans.

## Guardrail Ladder

| Level | Guardrail | Meaning |
|---:|---|---|
| 0 | No guardrails | Ask Codex, accept output, hope. Only acceptable for disposable experiments. |
| 1 | Git checkpoint | Commit before task. Highest leverage for shortcut users. |
| 2 | Scope guardrail | Tell Codex what files and behavior it may touch. |
| 3 | Manual verification | Run the app and test the exact changed path. |
| 4 | Machine verification | Run typecheck, build, tests, or lint. |
| 5 | Independent review | Review the diff yourself or use a fresh agent. |
| 6 | Deployment guardrail | Staging, feature flags, backups, monitoring, rollback. |

## Shortcut Routing Table

| Shortcut ID | Planned file | Best-practice alternative | Prototype risk | Production risk | Recoverability | Minimum guardrail | Status |
|---|---|---|---|---|---|---|---|
| `vcb.shortcut.skipping_tests` | `topics/shortcuts/skipping-tests.md` | run relevant tests | low | high | medium | manual exact-flow test + typecheck/build | active |
| `vcb.shortcut.skipping_plan` | `topics/shortcuts/skipping-plan.md` | plan first for broad/risky work | low | medium/high | high if small | ask for likely files, checks, and rollback | planned |
| `vcb.shortcut.one_big_prompt` | `topics/shortcuts/one-big-prompt.md` | slice into milestones | medium | high | medium | branch + treat output as prototype | planned |
| `vcb.shortcut.context_dumping` | `topics/shortcuts/context-dumping.md` | curated context packet | medium | high | medium | one task packet + assumption list + reset stale thread | active |
| `vcb.shortcut.vague_prompt` | `topics/shortcuts/vague-prompt.md` | four-part prompt | low | medium/high | medium | add goal + done-when + forbidden areas | planned |
| `vcb.shortcut.broad_agent_permissions` | `topics/shortcuts/broad-agent-permissions.md` | sandbox + approvals | medium in isolation | severe | low if secrets exposed | disposable VM/container + fake credentials | active |
| `vcb.shortcut.accepting_diff_without_review` | `topics/shortcuts/accepting-diff-without-review.md` | review diff | medium | high | medium | inspect changed files and risky areas | planned |
| `vcb.shortcut.accepting_looks_done` | `topics/shortcuts/accepting-looks-done.md` | acceptance criteria + evidence review | medium | high | medium | require changed files, one relevant check, and known gaps | active |
| `vcb.shortcut.adding_dependencies_fast` | `topics/shortcuts/adding-dependencies-fast.md` | dependency review | low | high | medium | no-new-deps first + inspect package | active |
| `vcb.shortcut.ignoring_lint_typecheck` | `topics/shortcuts/ignoring-lint-typecheck.md` | fix changed-file errors | medium | high | high if early | separate old failures from new failures | planned |
| `vcb.shortcut.coding_on_main` | `topics/shortcuts/coding-on-main.md` | branch/worktree | low solo | high shared/prod | medium | commit first + no auto-deploy | planned |
| `vcb.shortcut.manual_testing_only` | `topics/shortcuts/manual-testing-only.md` | automated checks | low | high | medium | feature flag + rollback | planned |
| `vcb.shortcut.unofficial_tools` | `topics/shortcuts/unofficial-tools.md` | official surfaces | medium | severe | low if credential leak | disposable environment + revocable tokens | active |
| `vcb.shortcut.unattended_long_runs` | `topics/shortcuts/unattended-long-runs.md` | bounded milestones | medium | high | medium | isolated worktree + no secrets + final report | active |
| `vcb.shortcut.skipping_setup` | `topics/shortcuts/skipping-setup.md` | setup inspection + durable project guidance | low | high | medium | inspect setup + one verification command | active |
| `vcb.shortcut.using_existing_local_setup` | `topics/shortcuts/using-existing-local-setup.md` | setup inspection + reproducible environment notes | low | medium/high | medium | inspect setup, capture commands, and run one verification command | planned |
| `vcb.shortcut.editing_before_understanding` | `topics/shortcuts/editing-before-understanding.md` | read-only codebase map first | low if tiny/local | high in unknown production repos | medium if committed | read-only map + file citations + smallest first edit | planned |
| `vcb.shortcut.debugging_without_repro` | `topics/shortcuts/debugging-without-repro.md` | reproduce/trace root cause first | low for obvious stack traces | high for intermittent/stateful bugs | medium | preserve evidence + root-cause explanation + rerun nearest check | planned |
| `vcb.shortcut.eyeballing_ui` | `topics/shortcuts/eyeballing-ui.md` | visual acceptance criteria + browser checks | low | high | medium | screenshot/reference + desktop/mobile check + state list | planned |
| `vcb.shortcut.broad_refactor` | `topics/shortcuts/broad-refactor.md` | small behavior-preserving refactor passes | medium | high | medium if committed | branch + one pass + tests/checks + diff review | active |
| `vcb.shortcut.framework_churn` | `topics/shortcuts/framework-churn.md` | stay on current stack or run isolated decision spike | medium | severe | low/medium | separate spike + decision memo + rollback plan | planned |
| `vcb.shortcut.skipping_agents_md` | `topics/shortcuts/skipping-agents-md.md` | durable project guidance | low | medium/high | medium | add minimal commands + do-not rules after repeated mistakes | active |
| `vcb.shortcut.overstuffing_agents_md` | `topics/shortcuts/overstuffing-agents-md.md` | concise maintained repo guidance | medium | high | medium | prune stale rules + keep task-specific content in prompts | active |
| `vcb.shortcut.default_config_forever` | `topics/shortcuts/default-config-forever.md` | explicit safe profiles | low | high | medium | keep conservative default + create named risky profiles | active |
| `vcb.shortcut.using_global_config_for_everything` | `topics/shortcuts/using-global-config-for-everything.md` | project rules in repo-local guidance/config | low | medium/high | medium | keep project rules with the project | planned |
| `vcb.shortcut.skill_overkill` | `topics/shortcuts/skill-overkill.md` | create skills only for repeated workflows | low | medium | high | use saved prompt until workflow repeats | active |
| `vcb.shortcut.skill_sprawl` | `topics/shortcuts/skill-sprawl.md` | narrow one-job skills | medium | high | medium | audit overlap + add non-trigger cases | active |
| `vcb.shortcut.tool_sprawl_mcp` | `topics/shortcuts/tool-sprawl-mcp.md` | one high-value external tool at a time | medium | severe | low/medium | start read-only + document purpose + remove unused servers | active |
| `vcb.shortcut.trusting_external_tool_output` | `topics/shortcuts/trusting-external-tool-output.md` | verify external context and cite source records | medium | high | medium | treat external content as untrusted + require attribution | active |
| `vcb.shortcut.brittle_hooks` | `topics/shortcuts/brittle-hooks.md` | narrow deterministic guardrails | medium | high | high if easy to disable | start report-only + keep fast/objective | active |
| `vcb.shortcut.hook_overreach` | `topics/shortcuts/hook-overreach.md` | hooks only for enforceable objective rules | medium | high | medium | move subjective/heavy checks to review or CI | active |
| `vcb.shortcut.skipping_pr_review` | `topics/shortcuts/skipping-pr-review.md` | independent PR review | low | high | high before merge | request focused review for risky PRs | planned |
| `vcb.shortcut.accepting_codex_review_as_approval` | `topics/shortcuts/accepting-codex-review-as-approval.md` | human triage + merge ownership | medium | high | medium | treat Codex review as signal, not approval | planned |
| `vcb.shortcut.skipping_security_review` | `topics/shortcuts/skipping-security-review.md` | threat-model and security-focused review | medium | severe | low/medium | fake data + threat model + focused security pass | planned |
| `vcb.shortcut.real_secrets_in_prototype` | `topics/shortcuts/real-secrets-in-prototype.md` | fake credentials and isolated environments | severe | severe | low | use fake credentials; rotate immediately if exposed | active |
| `vcb.shortcut.unattended_mutation` | `topics/shortcuts/unattended-mutation.md` | read-only report/propose automation | medium | severe | medium/low | branch-only mutation + human review gate | active |
| `vcb.shortcut.overbroad_ci_permissions` | `topics/shortcuts/overbroad-ci-permissions.md` | least-privilege CI permissions | medium | severe | low if token abuse | explicit minimal token permissions | active |
| `vcb.shortcut.long_lived_ci_secrets` | `topics/shortcuts/long-lived-ci-secrets.md` | short-lived credentials/OIDC when available | medium | severe | low if leaked | use OIDC or scoped secrets; rotate on exposure | active |
| `vcb.shortcut.parallel_cloud_sprawl` | `topics/shortcuts/parallel-cloud-sprawl.md` | isolated scoped delegation plan | medium | high | medium | one task packet per branch/worktree + comparison rubric | active |
| `vcb.shortcut.best_of_n_without_review` | `topics/shortcuts/best-of-n-without-review.md` | compare diffs/checks before accepting | medium | high | medium | review each attempt by diff, checks, risks, and rollback | active |
| `vcb.shortcut.cloud_task_without_context` | `topics/shortcuts/cloud-task-without-context.md` | provide delegation packet and local context summary | medium | high | medium | include files, constraints, acceptance criteria, and forbidden areas | active |
| `vcb.shortcut.subagent_swarm` | `topics/shortcuts/subagent-swarm.md` | one agent per explicit concern | medium | high | medium | analysis-only first + severity/evidence report format | active |
| `vcb.shortcut.parallel_agents_edit_same_files` | `topics/shortcuts/parallel-agents-edit-same-files.md` | disjoint scopes or single integrator | medium | severe | low/medium | forbid overlap or use one integrator for edits | active |
| `vcb.shortcut.model_routing_guesswork` | `topics/shortcuts/model-routing-guesswork.md` | current source-verified model/surface guidance | medium | high | medium | avoid hardcoded model claims; use official current docs | active |
| `vcb.shortcut.automation_spam` | `topics/shortcuts/automation-spam.md` | useful findings inbox with silence behavior | low | medium/high | high | define actionable output and archive/silence criteria | active |
| `vcb.shortcut.automating_unstable_workflow` | `topics/shortcuts/automating-unstable-workflow.md` | manual dry run before scheduling | medium | high | medium | run manually, tighten prompt, schedule only stable report-only work | planned |
| `vcb.shortcut.automation_mutation_without_review` | `topics/shortcuts/automation-mutation-without-review.md` | report/propose before mutation | medium | severe | low/medium | branch-only mutation + owner + human review gate | active |
| `vcb.shortcut.gui_on_production` | `topics/shortcuts/gui-on-production.md` | staging/local GUI verification first | medium | severe | low | use staging/fake data + human present for production/admin flows | planned |
| `vcb.shortcut.logged_in_browser_secrets` | `topics/shortcuts/logged-in-browser-secrets.md` | fake/staging accounts and scoped app approvals | medium | severe | low | remove visible secrets/customer data; rotate if exposed | active |
| `vcb.shortcut.computer_use_without_scope` | `topics/shortcuts/computer-use-without-scope.md` | exact allowed app/site/window and forbidden actions | medium | high | medium | specify GUI steps, allowed surfaces, and proof required | planned |
| `vcb.shortcut.unattended_cloud_delegation` | `topics/shortcuts/unattended-cloud-delegation.md` | bounded cloud task with branch/worktree and final report | medium | high | medium | isolated worktree + do-not-touch list + human review before merge | active |
| `vcb.shortcut.conflicting_parallel_agents` | `topics/shortcuts/conflicting-parallel-agents.md` | one agent per boundary and one integrator | medium | high | medium/low | separate branches/worktrees + no shared-file edits | active |
| `vcb.shortcut.ambiguous_cloud_task` | `topics/shortcuts/ambiguous-cloud-task.md` | plan and define done before delegation | medium | high | medium | delegation brief + acceptance criteria + report-only if unclear | active |
| `vcb.shortcut.consensus_as_correctness` | `topics/shortcuts/consensus-as-correctness.md` | verify claims with evidence and checks | medium | high | medium | require file refs, tests, and diff review | active |
| `vcb.shortcut.full_access_automation` | `topics/shortcuts/full-access-automation.md` | least-privilege background automation | medium | severe | low | workspace/read-only defaults + explicit allowlist | active |
| `vcb.shortcut.logged_in_production_gui` | `topics/shortcuts/logged-in-production-gui.md` | staging/fake account GUI verification | medium | severe | low | fake/staging account + exact steps + no destructive actions | planned |
| `vcb.shortcut.always_allow_sensitive_apps` | `topics/shortcuts/always-allow-sensitive-apps.md` | per-task app approval and review | medium | severe | low | avoid Always Allow for sensitive apps; revoke after use | active |
| `vcb.shortcut.browser_clicking_without_repro` | `topics/shortcuts/browser-clicking-without-repro.md` | repro steps before browser operation | low/medium | high | medium | exact flow steps + expected/actual + screenshot/report | active |
| `vcb.shortcut.unbounded_cloud_delegation` | `topics/shortcuts/unbounded-cloud-delegation.md` | scoped cloud task packet + branch review | medium | high | medium if isolated | branch/worktree + forbidden areas + final report | planned |
| `vcb.shortcut.parallel_tasks_same_files` | `topics/shortcuts/parallel-tasks-same-files.md` | one agent per independent boundary | medium | high | medium/low | separate branches + no overlapping file ownership | planned |
| `vcb.shortcut.agents_editing_same_files` | `topics/shortcuts/agents-editing-same-files.md` | centralize editing or isolate branches | medium | high | medium/low | read-only subagents or separate worktrees | planned |
| `vcb.shortcut.gui_actions_in_production` | `topics/shortcuts/gui-actions-in-production.md` | staging/fake data + human-controlled production actions | medium | severe | low | stay present + forbid side effects unless approved | planned |
| `vcb.shortcut.exposing_sensitive_screen_context` | `topics/shortcuts/exposing-sensitive-screen-context.md` | close sensitive apps/tabs before GUI work | medium | severe | low | local/staging only + clear visible context | planned |
| `vcb.shortcut.parallel_conflict` | `topics/shortcuts/parallel-conflict.md` | one owner per file/area | medium | high | medium | no overlapping file ownership + integration plan | planned |
| `vcb.shortcut.parallel_editing_same_files` | `topics/shortcuts/parallel-editing-same-files.md` | analysis parallel, implementation serialized | medium | severe | low/medium | one integrator + no overlapping mutations | planned |
| `vcb.shortcut.logged_in_gui_production_actions` | `topics/shortcuts/logged-in-gui-production-actions.md` | local/staging GUI verification | high | severe | low | fake account + stop-before-sensitive-action | planned |
| `vcb.shortcut.browser_use_with_secrets` | `topics/shortcuts/browser-use-with-secrets.md` | no secrets in browser-operated flows | high | severe | low | hide/remove secrets + rotate on exposure | planned |
| `vcb.shortcut.unattended_gui_work` | `topics/shortcuts/unattended-gui-work.md` | supervised scoped GUI tasks | medium | high/severe | medium/low | exact steps + fake data + evidence capture | planned |
| `vcb.shortcut.reviewing_cloud_summary_only` | `topics/shortcuts/reviewing-cloud-summary-only.md` | review returned diff/checks | medium | high | medium | inspect changed files, checks, and out-of-scope edits | active |
| `vcb.shortcut.parallel_write_conflicts` | `topics/shortcuts/parallel-write-conflicts.md` | analysis-only or isolated write agents | medium | high | medium/low | prohibit shared-file edits unless isolated | planned |
| `vcb.shortcut.unreviewed_subagent_findings` | `topics/shortcuts/unreviewed-subagent-findings.md` | triaged findings with file evidence | medium | high | medium | require severity, evidence, and main-agent synthesis | planned |
| `vcb.shortcut.background_full_access` | `topics/shortcuts/background-full-access.md` | read-only or branch-only background work | high | severe | low/medium | avoid full access; isolate and review first runs | planned |
| `vcb.shortcut.logged_in_gui_control` | `topics/shortcuts/logged-in-gui-control.md` | staging/test account GUI pass | medium | severe | low/medium | fake account + explicit no-click zones + human present | planned |
| `vcb.shortcut.production_console_computer_use` | `topics/shortcuts/production-console-computer-use.md` | human-operated production admin with Codex observation/report | high | severe | low | report-only or human present; never unattended mutation | active |
| `vcb.shortcut.screenshot_only_verification` | `topics/shortcuts/screenshot-only-verification.md` | flow-based GUI/browser check | low | medium/high | medium | repro steps + expected/actual + one relevant check | planned |
| `vcb.shortcut.cloud_work_with_real_secrets` | `topics/shortcuts/cloud-work-with-real-secrets.md` | fake credentials and isolated cloud/task environments | high | severe | low | no real secrets in delegated cloud work; rotate on exposure | active |
| `vcb.shortcut.process_overhead_for_tiny_project` | `topics/shortcuts/process-overhead-for-tiny-project.md` | smallest durable artifact only after repeated friction | low | low/medium | high | keep prompt snippet until process earns its cost | active |
| `vcb.shortcut.team_workflow_without_team` | `topics/shortcuts/team-workflow-without-team.md` | solo workflow first, team process later | low | medium | high | do not add roles/process before repeated need | active |
| `vcb.shortcut.ignoring_failure_mode` | `topics/shortcuts/ignoring-failure-mode.md` | classify failure before retrying | medium | high | medium | name failure mode + missing control before new edits | planned |
| `vcb.shortcut.treating_symptom_as_root_cause` | `topics/shortcuts/treating-symptom-as-root-cause.md` | reproduce and explain root cause | medium | high | medium | require evidence and minimal fix plan | planned |
| `vcb.shortcut.copy_pasting_playbook_blindly` | `topics/shortcuts/copy-pasting-playbook-blindly.md` | tune playbook by risk/context/budget | low | medium/high | high if small | fill risk, forbidden areas, and done criteria first | active |
| `vcb.shortcut.overusing_one_playbook` | `topics/shortcuts/overusing-one-playbook.md` | select smallest matching playbook | low | medium | high | choose playbook by task shape and risk | planned |
| `vcb.shortcut.generated_prototype_as_production_foundation` | `topics/shortcuts/generated-prototype-as-production-foundation.md` | review/harden or rebuild prototype foundation | medium | high/severe | medium/low | fake data first + review dependencies/security/tests | planned |
| `vcb.shortcut.overbuilding_first_app` | `topics/shortcuts/overbuilding-first-app.md` | first vertical slice | medium | high | medium | one user, one workflow, one data path first | planned |
| `vcb.shortcut.skipping_senior_checklist` | `topics/shortcuts/skipping-senior-checklist.md` | risk-scaled before/during/after checklist | low | high | medium/high | review diff, checks, sensitive areas, and rollback | planned |
| `vcb.shortcut.checklist_theater` | `topics/shortcuts/checklist-theater.md` | evidence-based checklist use | medium | high | medium | require evidence for each checked item | planned |
| `vcb.shortcut.stale_agents_md` | `topics/shortcuts/stale-agents-md.md` | regular AGENTS.md pruning and source review | medium | high | medium | remove stale/contradictory rules and keep durable guidance current | active |


## Active Shortcut Cards

- `vcb.shortcut.skipping_tests` → active: `topics/shortcuts/skipping-tests.md` — risk-managed shortcut card for accepting changes without the smallest relevant verification
- `vcb.shortcut.accepting_looks_done` → active: `topics/shortcuts/accepting-looks-done.md` — risk-managed shortcut card for accepting polished output without completion evidence
- `vcb.shortcut.broad_agent_permissions` → active: `topics/shortcuts/broad-agent-permissions.md` — risk-managed shortcut card for broad filesystem/network/tool/account access
- `vcb.shortcut.unattended_long_runs` → active: `topics/shortcuts/unattended-long-runs.md` — risk-managed shortcut card for long-running work without checkpoints
- `vcb.shortcut.broad_refactor` → active: `topics/shortcuts/broad-refactor.md` — risk-managed shortcut card for broad cleanup or refactor prompts
- `vcb.shortcut.context_dumping` → active: `topics/shortcuts/context-dumping.md` — risk-managed shortcut card for noisy/stale prompt context
- `vcb.shortcut.adding_dependencies_fast` → active: `topics/shortcuts/adding-dependencies-fast.md` — risk-managed shortcut card for fast dependency additions
- `vcb.shortcut.reviewing_cloud_summary_only` → active: `topics/shortcuts/reviewing-cloud-summary-only.md` — risk-managed shortcut card for cloud/background work reviewed only by summary


## Active Security and Permission Shortcut Cards

- `vcb.shortcut.production_console_computer_use` → active: `topics/shortcuts/production-console-computer-use.md` — risk-managed shortcut card for production/admin console GUI actions
- `vcb.shortcut.overbroad_ci_permissions` → active: `topics/shortcuts/overbroad-ci-permissions.md` — risk-managed shortcut card for broad CI permissions
- `vcb.shortcut.long_lived_ci_secrets` → active: `topics/shortcuts/long-lived-ci-secrets.md` — risk-managed shortcut card for persistent CI/deployment secrets
- `vcb.shortcut.real_secrets_in_prototype` → active: `topics/shortcuts/real-secrets-in-prototype.md` — risk-managed shortcut card for real credentials in prototypes
- `vcb.shortcut.cloud_work_with_real_secrets` → active: `topics/shortcuts/cloud-work-with-real-secrets.md` — risk-managed shortcut card for real secrets in delegated cloud work
- `vcb.shortcut.full_access_automation` → active: `topics/shortcuts/full-access-automation.md` — risk-managed shortcut card for full-access automation
- `vcb.shortcut.unattended_mutation` → active: `topics/shortcuts/unattended-mutation.md` — risk-managed shortcut card for write-capable unattended work
- `vcb.shortcut.always_allow_sensitive_apps` → active: `topics/shortcuts/always-allow-sensitive-apps.md` — risk-managed shortcut card for persistent sensitive app/site approvals

## Active Setup, Configuration, and Process Shortcut Cards

- `vcb.shortcut.skipping_setup` → active: `topics/shortcuts/skipping-setup.md` — inspect setup before edits and run one smallest verification
- `vcb.shortcut.default_config_forever` → active: `topics/shortcuts/default-config-forever.md` — review Codex config defaults and risky profiles by project phase
- `vcb.shortcut.skipping_agents_md` → active: `topics/shortcuts/skipping-agents-md.md` — promote repeated project guidance into durable repo instructions
- `vcb.shortcut.overstuffing_agents_md` → active: `topics/shortcuts/overstuffing-agents-md.md` — prune AGENTS.md so durable guidance does not become context pollution
- `vcb.shortcut.stale_agents_md` → active: `topics/shortcuts/stale-agents-md.md` — verify old repo guidance before future agents follow it
- `vcb.shortcut.unofficial_tools` → active: `topics/shortcuts/unofficial-tools.md` — vet plugins, MCP servers, wrappers, extensions, and scripts before enabling
- `vcb.shortcut.hook_overreach` → active: `topics/shortcuts/hook-overreach.md` — keep hooks objective and narrow instead of treating them as complete policy
- `vcb.shortcut.trusting_external_tool_output` → active: `topics/shortcuts/trusting-external-tool-output.md` — verify MCP/plugin/web/tool output with source evidence before mutation

## Active Tool-Sprawl, Skill, and Reusable-Process Shortcut Cards

- `vcb.shortcut.skill_overkill` → active: `topics/shortcuts/skill-overkill.md` — create skills only for repeated workflows with stable triggers
- `vcb.shortcut.skill_sprawl` → active: `topics/shortcuts/skill-sprawl.md` — keep skill libraries narrow, distinct, and maintained
- `vcb.shortcut.tool_sprawl` → active: `topics/shortcuts/tool-sprawl.md` — add one tool at a time with owner, purpose, and exit path
- `vcb.shortcut.tool_sprawl_mcp` → active: `topics/shortcuts/tool-sprawl-mcp.md` — scope MCP servers, tools, credentials, and approvals tightly
- `vcb.shortcut.brittle_hooks` → active: `topics/shortcuts/brittle-hooks.md` — keep hooks fast, deterministic, report-first, and reviewed
- `vcb.shortcut.process_overhead_for_tiny_project` → active: `topics/shortcuts/process-overhead-for-tiny-project.md` — keep tiny projects on the smallest useful process artifact
- `vcb.shortcut.team_workflow_without_team` → active: `topics/shortcuts/team-workflow-without-team.md` — use solo evidence workflow before team handoffs exist
- `vcb.shortcut.copy_pasting_playbook_blindly` → active: `topics/shortcuts/copy-pasting-playbook-blindly.md` — tailor reusable playbooks before execution

## Active Parallel Cloud and Automation Shortcut Cards

- `vcb.shortcut.unattended_cloud_delegation` → active: `topics/shortcuts/unattended-cloud-delegation.md` — bounded cloud delegation with branch/worktree isolation, stop conditions, and review packet
- `vcb.shortcut.ambiguous_cloud_task` → active: `topics/shortcuts/ambiguous-cloud-task.md` — plan-first guardrails for vague background tasks before mutation
- `vcb.shortcut.cloud_task_without_context` → active: `topics/shortcuts/cloud-task-without-context.md` — delegation packet and context-gap checks before cloud work
- `vcb.shortcut.parallel_cloud_sprawl` → active: `topics/shortcuts/parallel-cloud-sprawl.md` — task matrix, isolated branches, and integration owner for parallel cloud work
- `vcb.shortcut.conflicting_parallel_agents` → active: `topics/shortcuts/conflicting-parallel-agents.md` — one mutating owner per file/behavior and one integrator
- `vcb.shortcut.automation_spam` → active: `topics/shortcuts/automation-spam.md` — recurring automation must be actionable, deduplicated, and quiet when nothing changed
- `vcb.shortcut.automation_mutation_without_review` → active: `topics/shortcuts/automation-mutation-without-review.md` — report/propose first; branch-only mutation with human review if mutation is unavoidable
- `vcb.shortcut.browser_clicking_without_repro` → active: `topics/shortcuts/browser-clicking-without-repro.md` — exact GUI/browser repro and before/after evidence before mutation
- `vcb.shortcut.logged_in_browser_secrets` → active: `topics/shortcuts/logged-in-browser-secrets.md` — fake/staging accounts and scoped approvals for signed-in browser/GUI work


## Shortcut Expansion Policy

Shortcut cards are first-class retrieval targets, but this register may list planned shortcut cards before full topic cards exist. Chapter 38 (`vcb.chapter.risk_managed_shortcuts`) is the active overview for harm-reduction guidance until individual shortcut cards are authored.

A shortcut entry is valid only when it includes:

- canonical `vcb.shortcut.*` ID;
- best-practice alternative;
- prototype risk;
- production risk;
- recoverability;
- minimum guardrail;
- status.

## Production Red-Line Shortcut Families

These shortcut families require strong escalation in AI-coach responses:

- real secrets in prompts, files, CI, browser, or GUI state;
- production data mutation;
- auth, authorization, payment, billing, health/legal/financial, or data-deletion changes;
- broad unattended mutation with network/write access;
- unknown install scripts with secrets or full access;
- long-lived CI/cloud credentials with overbroad permissions.

## Guardrail Escalation Rule

Do not demand perfect process for every shortcut. Move the user up at least one guardrail level, and escalate harder only when blast radius, recoverability, or hidden failure risk justifies it.

## Constraint, Cost, Multi-AI, and Model-Bias Shortcut Routes

| Shortcut ID | Planned file | Best-practice alternative | Prototype risk | Production risk | Recoverability | Minimum guardrail | Status |
|---|---|---|---|---|---|---|---|
| `vcb.shortcut.defaulting_to_high_throughput` | `topics/shortcuts/defaulting-to-high-throughput.md` | operating-mode selection | medium | medium/high | medium | choose mode by budget/risk/attention instead of plan status | planned |
| `vcb.shortcut.permanent_high_usage_plan` | `topics/shortcuts/permanent-high-usage-plan.md` | phase-based plan review | low | medium | high | set review date and downgrade/upgrade by phase | planned |
| `vcb.shortcut.over_optimizing_for_price` | `topics/shortcuts/over-optimizing-for-price.md` | cost-benefit analysis | low | medium | medium | include human time, rework, and recovery cost | planned |
| `vcb.shortcut.skipping_maintenance_cleanup` | `topics/shortcuts/skipping-maintenance-cleanup.md` | maintenance review | low | medium | medium | schedule source/index/register cleanup after phase changes | planned |
| `vcb.shortcut.tool_sprawl` | `topics/shortcuts/tool-sprawl.md` | minimum viable stack | medium | high | medium | add one tool at a time with owner, source, and exit path | active |
| `vcb.shortcut.buying_tools_as_progress` | `topics/shortcuts/buying-tools-as-progress.md` | cost-benefit analysis | medium | medium/high | high before production | require milestone and cheaper alternative before purchase | planned |
| `vcb.shortcut.many_ais_same_files` | `topics/shortcuts/many-ais-same-files.md` | one implementer + review roles | medium | high | medium | assign one mutating implementer; keep others read-only | active |
| `vcb.shortcut.parallel_agents_same_files` | `topics/shortcuts/parallel-agents-same-files.md` | avoid overlapping write agents | medium | high | low/medium | read-only subagents or isolated branches | planned |
| `vcb.shortcut.cherry_picking_ai_answers` | `topics/shortcuts/cherry-picking-ai-answers.md` | evidence-based review | medium | high | medium | choose by evidence, not by pleasing output | active |
| `vcb.shortcut.trusting_estimates_before_inspection` | `topics/shortcuts/trusting-estimates-before-inspection.md` | inspect before estimating | medium | high | medium | ask for unknowns and confidence after repo inspection | active |
| `vcb.shortcut.ignoring_model_biases` | `topics/shortcuts/ignoring-model-biases.md` | bias checklist | medium | high | medium | run bias-to-guardrail checklist before acceptance | active |

## Active Multi-AI and Model-Bias Shortcut Cards

- `vcb.shortcut.many_ais_same_files` → active: `topics/shortcuts/many-ais-same-files.md` — using multiple AI systems on the same files without one owner, one branch strategy, and one integration path
- `vcb.shortcut.parallel_agents_edit_same_files` → active: `topics/shortcuts/parallel-agents-edit-same-files.md` — letting multiple agents mutate overlapping files at the same time and hoping the merge will be obvious later
- `vcb.shortcut.best_of_n_without_review` → active: `topics/shortcuts/best-of-n-without-review.md` — asking several AIs for answers, then accepting the one that looks best without checking diffs, tests, source evidence, or risks
- `vcb.shortcut.cherry_picking_ai_answers` → active: `topics/shortcuts/cherry-picking-ai-answers.md` — choosing the answer that confirms your preferred plan instead of the answer with the best evidence
- `vcb.shortcut.consensus_as_correctness` → active: `topics/shortcuts/consensus-as-correctness.md` — treating agreement between multiple AIs as proof that a claim, estimate, fix, or design is correct
- `vcb.shortcut.trusting_estimates_before_inspection` → active: `topics/shortcuts/trusting-estimates-before-inspection.md` — believing an AI estimate before the model has inspected the actual code, dependencies, tests, constraints, and unknowns
- `vcb.shortcut.ignoring_model_biases` → active: `topics/shortcuts/ignoring-model-biases.md` — forgetting that models can be biased toward plausible answers, overconfident summaries, common patterns, pleasing the user, and underestimating hidden project constraints
- `vcb.shortcut.model_routing_guesswork` → active: `topics/shortcuts/model-routing-guesswork.md` — choosing a model, reasoning level, surface, or AI tool by brand feeling, stale advice, or price anxiety instead of current docs, task shape, risk, and evidence needs
- `vcb.shortcut.subagent_swarm` → active: `topics/shortcuts/subagent-swarm.md` — spawning many subagents or custom agents before each has a bounded question, role, context, output format, and integration plan

## Shortcut Card Typing

Shortcut topic cards must use:

```yaml
id: vcb.shortcut.<slug>
type: shortcut
shortcut_type: risk_managed_shortcut
```

This matches both the canonical topic namespace policy and `schemas/shortcut.schema.json`. Do not use `type: risk_managed_shortcut`; that value belongs in `shortcut_type`.

## Redirected Planned Aliases for Active Shortcut Cards

These IDs may remain as search terms or future companion placeholders, but routing surfaces must show the active canonical replacement first. Do not treat a redirected alias as the smallest active topic card.

| Active canonical route | Redirected / planned alias | Cleanup policy |
|---|---|---|
| active: `vcb.shortcut.default_config_forever` | alias: `vcb.shortcut.using_global_config_for_everything` | show active config-default route first |
| active: `vcb.shortcut.many_ais_same_files` | alias: `vcb.shortcut.parallel_agents_same_files` | show active many-AIs-same-files route first |
| active: `vcb.shortcut.parallel_agents_edit_same_files` | alias: `vcb.shortcut.parallel_tasks_same_files` | show active parallel-agent same-file route first |
| active: `vcb.shortcut.best_of_n_without_review` | alias: `vcb.shortcut.ai_answer_shopping` | show active answer-review route first |
| active: `vcb.shortcut.consensus_as_correctness` | alias: `vcb.shortcut.model_consensus` | show active consensus-is-not-evidence route first |
| active: `vcb.shortcut.trusting_estimates_before_inspection` | alias: `vcb.shortcut.ai_estimate_trust` | show active estimate-before-inspection route first |
| active: `vcb.shortcut.ignoring_model_biases` | alias: `vcb.shortcut.model_bias_blindness` | show active model-bias guardrail route first |
| active: `vcb.shortcut.unattended_cloud_delegation` | alias: `vcb.shortcut.unbounded_cloud_delegation` | show active cloud-delegation route first |
| active: `vcb.shortcut.cloud_task_without_context` | alias: `vcb.shortcut.background_handoff_risk` | show active cloud-context route first |
| active: `vcb.shortcut.conflicting_parallel_agents` | alias: `vcb.shortcut.parallel_conflict` | show active conflicting-agent route first |
| active: `vcb.shortcut.conflicting_parallel_agents` | alias: `vcb.shortcut.parallel_write_conflicts` | show active conflicting-agent route first |
| active: `vcb.shortcut.full_access_automation` | alias: `vcb.shortcut.background_full_access` | show active full-access automation route first |
| active: `vcb.shortcut.browser_clicking_without_repro` | alias: `vcb.shortcut.unattended_gui_work` | show active browser/GUI repro route first |
| active: `vcb.shortcut.logged_in_browser_secrets` | alias: `vcb.shortcut.browser_use_with_secrets` | show active logged-in browser/secrets route first |
| active: `vcb.shortcut.browser_clicking_without_repro` | alias: `vcb.shortcut.screenshot_only_verification` | show active browser/GUI repro route first |


## Chunk 42 Release-Candidate Disposition Note

Chunk 42 does not add, activate, retire, or deprecate shortcut IDs. It confirms the release-candidate disposition: 50 active shortcut rows and 48 planned shortcut rows are explicit; planned shortcut rows are documented future routes, not active doctrine, and do not block release-candidate packaging if this limitation remains visible.

## Chunk 41 Finalization Readiness Audit Note

Chunk 41 does not add, activate, retire, or deprecate shortcut IDs. The finalization-readiness audit confirms 50 active shortcut rows and 48 planned shortcut rows. Planned shortcuts remain future routes, not active doctrine.

<!-- VCB:STOP_RETRIEVAL reason="shortcut_register_complete" -->
<!-- VCB:END_REGISTER id=vcb.register.shortcuts -->
