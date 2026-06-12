---
id: vcb.register.sources
title: SOURCE_REGISTER
artifact_type: register
version: 1.0.1-postrelease.issue4
status: issue_4_ai_coding_tools_pricing_sources
created_on: '2026-06-08'
last_verified: '2026-06-12'
next_review_due: '2026-07-12'
review_cadence: monthly
---

<!-- VCB:BEGIN_REGISTER id=vcb.register.sources version=1.0.1-postrelease.issue4 -->

# SOURCE_REGISTER

**Purpose:** Track sources used by The Vibe Coding Bible and separate official guidance, official examples, local reproduction, expert reports, community field reports, speculation, and VCB synthesis.

## Source Record Rules

- OpenAI/Codex behavior must be checked against official OpenAI sources first.
- Vendor capabilities and pricing must be checked against official vendor sources first.
- Exact prices, exact limits, credits, and volatile rate data must go in dated pricing snapshots, not stable chapters.
- Community practices must be labeled as field reports and include reproducibility caveats.
- If an official source and field practice conflict, official behavior wins unless local repo evidence proves otherwise.
- Internal maintainer synthesis is not an evidence level. Do not label it as `E3_EXPERT_REPORT` unless it is tied to a named expert, blog, course, talk, or public practitioner.
- Use `evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE` or `source_kind: maintainer_synthesis` for durable control-loop guidance synthesized by maintainers, and cite component official/vendor/expert/community sources where available.

## Evidence Levels

| Level | Label | Meaning |
|---|---|---|
| E0 | `OFFICIAL_DOCS` | Official OpenAI docs, vendor docs, or release notes |
| E1 | `OFFICIAL_COOKBOOK` | Official tutorial, cookbook, or example |
| E2 | `REPRODUCED_LOCALLY` | Maintainer-tested in a controlled repo |
| E3 | `EXPERT_REPORT` | Named expert, blog, course, talk, or public practitioner |
| E4 | `COMMUNITY_FIELD_REPORT` | Forum, Discord, Reddit, Hacker News, anonymous user report |
| E5 | `SPECULATIVE` | Prediction, unverified tactic, emerging pattern |

## Internal Synthesis Basis Records

These records are maintainer-authored synthesis aids. They are not evidence levels and must not be used as substitutes for official product behavior, named expert reports, reproduced local tests, or community field reports.

| Synthesis ID | source_kind | evidence_basis | Status | Use for | Rules |
|---|---|---|---|---|---|
| `vcb.synthesis.stable_engineering_practice` | maintainer_synthesis | `VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE` | declared 2026-06-08 | durable control-loop framing, vibe-coder risk posture, acceptance criteria, blast-radius/recoverability thinking | Not an evidence level; not official product guidance; cite official/vendor/expert/community component sources for claims. |
| `vcb.synthesis.prompting_operator_practice` | maintainer_synthesis | `VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE` | declared 2026-06-08 | prompt work orders, plan-first gates, context packets, and acceptance criteria | Not an external E3 source; use only as evidence basis. |

## Canonical Source Table

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.blueprint.v1` | The Vibe Coding Bible — Source Blueprint | uploaded blueprint | internal governing spec | source of truth | architecture, required sections, taxonomies, chunk gate | stable for this production run |
| `vcb.register.editor_feedback_chunk_0` | Editor review for Chunk 0 | conversation/editor feedback | internal review | applied | Chunk 0 scaffold revisions | stable for this revision |
| `vcb.register.editor_feedback_chunk_1` | Editor review for Chunk 1 | conversation/editor feedback | internal review | applied | Chunk 1 routing revisions and approval | stable for this revision |
| `vcb.register.editor_feedback_chunk_2` | Editor review for Chunk 2 | conversation/editor feedback | internal review | applied | Chunk 2 source/evidence revisions and approval | stable for this revision |
| `vcb.register.editor_feedback_chunk_3` | Editor approval for Chunk 3 | conversation/editor feedback | internal review | applied | Chunk 4 gate and scope | stable for this revision |
| `vcb.register.editor_feedback_chunk_4` | Editor review for Chunk 4 | conversation/editor feedback | internal review | applied | Chunk 4 shortcut/source-register routing revision and approval | stable for this revision |
| `vcb.register.editor_feedback_chunk_5` | Editor approval for Chunk 4 / Chunk 5 gate | conversation/editor feedback | internal review | applied | Chunk 5 approved scope and non-scope | stable for this revision |
| `vcb.register.editor_feedback_chunk_6` | Editor approval for Chunk 5 / Chunk 6 gate | conversation/editor feedback | internal review | applied | Chunk 6 approved scope and non-scope | stable for this revision |
| `vcb.register.editor_feedback_chunk_13` | Editor approval for Chunk 13 / Chunk 14 gate | conversation/editor feedback | internal review | applied | Chunk 14 approved scope and non-scope | stable for this revision |
| `vcb.register.editor_feedback_chunk_14` | Editor approval for Chunk 14 / Chunk 15 gate | conversation/editor feedback | internal review | applied | Chunk 15 approved scope and non-scope | stable for this revision |
| `aws.well_architected.design_principles` | AWS Well-Architected Framework — Design principles | https://docs.aws.amazon.com/wellarchitected/latest/framework/oe-design-principles.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | small reversible changes, blast-radius reduction, faster reversal framing | stable concept / vendor docs volatile |
| `openai.codex.overview` | Codex overview | https://developers.openai.com/codex | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Codex positioning and high-level capabilities | volatile |
| `openai.codex.best_practices` | Codex best practices | https://developers.openai.com/codex/learn/best-practices | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | goal/context/constraints/done-when prompt pattern, plan-first guidance, reusable guidance, validation, review, session controls | volatile |
| `openai.codex.llms_txt` | Codex llms.txt | https://developers.openai.com/codex/llms.txt | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | LLM-friendly docs map pattern | volatile |
| `openai.codex.llms_full` | Codex llms-full.txt | https://developers.openai.com/codex/llms-full.txt | E0_OFFICIAL_DOCS | seed anchor checked; deep review deferred | combined Markdown export pattern | volatile |
| `openai.codex.app` | Codex app | https://developers.openai.com/codex/app | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | app surface positioning | volatile |
| `openai.codex.app_features` | Codex app features | https://developers.openai.com/codex/app/features | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | app feature categories and surface watchlist | volatile |
| `openai.codex.app_settings` | Codex app settings | https://developers.openai.com/codex/app/settings | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | app Git, MCP, browser, computer use, memory/settings categories | volatile |
| `openai.codex.ide` | Codex IDE extension | https://developers.openai.com/codex/ide | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | IDE surface positioning | volatile |
| `openai.codex.ide_features` | Codex IDE extension features | https://developers.openai.com/codex/ide/features | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | IDE agent mode, open-file context, approval behavior, local-to-cloud delegation, cloud task follow-up, web-search caveats | volatile |
| `openai.codex.ide_settings` | Codex IDE extension settings | https://developers.openai.com/codex/ide/settings | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | IDE settings and shared CLI config note | volatile |
| `openai.codex.cli` | Codex CLI | https://developers.openai.com/codex/cli | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | CLI surface positioning | volatile |
| `openai.codex.cli_features` | Codex CLI features | https://developers.openai.com/codex/cli/features | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | CLI approval modes, transcripts, non-interactive anchors | volatile |
| `openai.codex.cli_reference` | Command line options — Codex CLI | https://developers.openai.com/codex/cli/reference | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | codex doctor, codex exec, codex sandbox, login/logout, feature maturity of CLI commands | volatile |
| `openai.codex.cloud` | Codex web / cloud | https://developers.openai.com/codex/cloud | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | cloud/background tasks, parallel work, GitHub connection, PR creation | volatile |
| `openai.codex.github_review` | Codex code review in GitHub | https://developers.openai.com/codex/integrations/github | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | GitHub PR review surface | volatile |
| `openai.codex.sdk` | Codex SDK | https://developers.openai.com/codex/sdk | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | programmatic Codex control | volatile |
| `openai.codex.github_action` | Codex GitHub Action | https://developers.openai.com/codex/github-action | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | CI/CD and GitHub Actions surface anchor | volatile |
| `openai.codex.feature_maturity` | Codex Feature Maturity | https://developers.openai.com/codex/feature-maturity | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | interpreting Codex feature maturity labels and production-readiness posture | volatile |
| `openai.codex.agents_md` | Custom instructions with AGENTS.md | https://developers.openai.com/codex/guides/agents-md | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | persistent repo guidance and instruction layering | volatile |
| `openai.codex.changelog` | Codex changelog | https://developers.openai.com/codex/changelog | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | release monitoring, deprecation watch, and targeted source/route refreshes | highly volatile |
| `openai.codex.pricing` | Codex pricing | https://developers.openai.com/codex/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-09; exact values captured in `vcb.pricing_snapshot.openai_codex` | live pricing, plan limits, feature availability, and snapshot source | highly volatile |
| `openai.codex.quickstart` | Codex quickstart | https://developers.openai.com/codex/quickstart | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | app, IDE, CLI, and cloud setup flow; Git checkpoint recommendation | volatile |
| `openai.codex.config_basic` | Config basics | https://developers.openai.com/codex/config-basic | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | user/project config layers, trust behavior, precedence, approval and sandbox options | volatile |
| `openai.codex.config_reference` | Configuration Reference | https://developers.openai.com/codex/config-reference | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | config key reference for config.toml, requirements.toml, approval and sandbox settings | volatile |
| `openai.codex.config_advanced` | Advanced Configuration | https://developers.openai.com/codex/config-advanced | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | project root detection and advanced config behavior | volatile |
| `openai.codex.sandboxing` | Sandbox | https://developers.openai.com/codex/concepts/sandboxing | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | sandbox purpose, default local permissions, approval relationship | volatile |
| `openai.codex.agent_approvals_security` | Agent approvals & security | https://developers.openai.com/codex/agent-approvals-security | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | sandboxing, approvals, network controls, full access cautions, devcontainer notes | volatile |
| `openai.codex.permissions` | Permissions — Codex | https://developers.openai.com/codex/permissions | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | permission profiles, read-only/workspace/full-access policy concepts | volatile / beta |
| `openai.codex.rules` | Rules — Codex | https://developers.openai.com/codex/rules | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | command allow/prompt/forbid rules and safety policy syntax | volatile |
| `openai.codex.auto_review` | Auto-review — Codex sandboxing | https://developers.openai.com/codex/concepts/sandboxing/auto-review | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | reviewer-agent approval routing and caveats | volatile |
| `openai.codex.windows` | Windows — Codex | https://developers.openai.com/codex/windows | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | native Windows, elevated/unelevated sandbox, and WSL2 setup caveats | volatile |
| `openai.api.prompt_engineering` | Prompt engineering | https://developers.openai.com/api/docs/guides/prompt-engineering | E0_OFFICIAL_DOCS | seed anchor; not used in Chunk 4 prose | API prompt engineering cross-check if future API automation cards need it | volatile |
| `openai.help.truthfulness` | Does ChatGPT tell the truth? | https://help.openai.com/en/articles/8313428-does-chatgpt-tell-the-truth | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | hallucination/confident-wrong caveats | volatile |
| `openai.hallucinations` | Why language models hallucinate | https://openai.com/index/why-language-models-hallucinate/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | hallucination and guessing-incentive framing | volatile |
| `git.docs.home` | Git home / documentation entrypoint | https://git-scm.com/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | Git as distributed version control and documentation entrypoint | stable |
| `git.docs.status` | git-status documentation | https://git-scm.com/docs/git-status | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | working tree status and changed/untracked paths | stable |
| `git.docs.diff` | git-diff documentation | https://git-scm.com/docs/git-diff | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | diff concept | stable |
| `git.docs.glossary` | Git glossary | https://git-scm.com/docs/gitglossary | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | branch terminology | stable |
| `git.docs.branch_book` | Pro Git — Branches in a Nutshell | https://git-scm.com/book/en/v2/Git-Branching-Branches-in-a-Nutshell | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | branch as diverging from main line | stable |
| `git.docs.commit` | git-commit documentation | https://git-scm.com/docs/git-commit | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | commit/checkpoint concept | stable |
| `git.docs.restore` | git-restore documentation | https://git-scm.com/docs/git-restore | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | restoring tracked paths in working tree/index | stable |
| `git.docs.reset` | git-reset documentation | https://git-scm.com/docs/git-reset | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | reset behavior, soft/hard examples, shared-history cautions | stable |
| `git.docs.revert` | git-revert documentation | https://git-scm.com/docs/git-revert | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | revert as inverse commit | stable |
| `git.docs.reflog` | git-reflog documentation | https://git-scm.com/docs/git-reflog | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | reflog recovery concepts and local reference history | stable |
| `git.docs.worktree` | git-worktree documentation | https://git-scm.com/docs/git-worktree | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | multiple working trees and branch isolation | stable |
| `git.docs.switch` | git-switch documentation | https://git-scm.com/docs/git-switch | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | switching and creating branches | stable |
| `git.docs.stash` | git-stash documentation | https://git-scm.com/docs/git-stash | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | saving local modifications and returning to clean working tree | stable |
| `github.docs.pull_requests` | About pull requests | https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | pull request concept, files changed, checks, merge status | stable concept / UI volatile |
| `github.docs.branch_protection` | About protected branches | https://docs.github.com/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | branch protection, force-push restrictions, required checks/reviews | stable concept / UI volatile |
| `openai.codex.prompting` | Prompting — Codex | `https://developers.openai.com/codex/prompting` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | prompt/task loop, focused steps, verification, context, thread behavior, Goal mode watchlist | volatile |
| `openai.codex.use_cases.follow_goals` | Follow a goal — Codex use case | `https://developers.openai.com/codex/use-cases/follow-goals` | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | long-running goal work, verifiable stopping conditions, validation loop, checkpoint guidance | volatile |
| `openai.codex.use_cases.iterate_on_difficult_problems` | Iterate on difficult problems — Codex use case | `https://developers.openai.com/codex/use-cases/iterate-on-difficult-problems` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | scored improvement loops, reviewable artifacts, long-running iteration | volatile |
| `openai.codex.workflows` | Workflows — Codex | `https://developers.openai.com/codex/workflows` | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | explicit context, definition of done, local-to-cloud workflow examples, planning patterns | volatile |
| `openai.api.prompt_guidance` | Prompt guidance — OpenAI API | `https://developers.openai.com/api/docs/guides/prompt-guidance` | E0_OFFICIAL_DOCS | seed anchor; not used in Chunk 4 prose | API prompt guidance cross-check if future API automation cards need it | volatile |
| `openai.api.reasoning_best_practices` | Reasoning best practices — OpenAI API | `https://developers.openai.com/api/docs/guides/reasoning-best-practices` | E0_OFFICIAL_DOCS | seed anchor; not used in Chunk 4 prose | API reasoning/planning cross-check if future API automation cards need it | volatile |
| `openai.codex.follow_goals` | Follow a goal — Codex use case | alias:openai.codex.use_cases.follow_goals | E1_OFFICIAL_COOKBOOK | alias retained for older Chunk 4 references | goal objectives, validation, stopping conditions, checkpoints, progress reports | volatile |
| `openai.codex.exec_plans_cookbook` | Using PLANS.md for multi-hour problem solving | `https://developers.openai.com/cookbook/articles/codex_exec_plans` | E1_OFFICIAL_COOKBOOK | anchor checked 2026-06-08 | PLANS.md, long-running task plans, living plans, validation, and acceptance review | volatile / cookbook example |
| `openai.codex.iterate_difficult_problems` | Iterate on difficult problems — Codex use case | alias:openai.codex.use_cases.iterate_on_difficult_problems | E1_OFFICIAL_COOKBOOK | alias retained for older Chunk 4 references | evals, stopping rules, running logs, artifact inspection, iterative acceptance proof | volatile |
| `openai.codex.app_automations` | Automations — Codex app | `https://developers.openai.com/codex/app/automations` | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | scheduled recurring Codex tasks, inbox/triage behavior, worktree/local-project choices, project-scoped requirements | volatile |
| `openai.codex.use_cases.codebase_onboarding` | Understand large codebases — Codex use case | `https://developers.openai.com/codex/use-cases/codebase-onboarding` | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | mapping unfamiliar codebases, modules, data flow, and next files before editing | volatile |
| `openai.codex.use_cases.automation_bug_triage` | Automate bug triage — Codex use case | `https://developers.openai.com/codex/use-cases/automation-bug-triage` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | alerts, issues, failed checks, logs, chat reports, bug triage sweeps | volatile |
| `openai.codex.use_cases.qa_computer_use` | QA your app with Computer Use — Codex use case | `https://developers.openai.com/codex/use-cases/qa-your-app-with-computer-use` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | UI flow QA, bug reports with repro steps, expected result, actual result, and severity | volatile |
| `openai.codex.guide_ai_native_engineering_team` | Building an AI-Native Engineering Team — Codex guide | `https://developers.openai.com/codex/guides/build-ai-native-engineering-team` | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | tests as a source of truth when agents generate code quickly | volatile |
| `openai.codex.use_cases.frontend_designs` | Build responsive front-end designs — Codex use case | `https://developers.openai.com/codex/use-cases/frontend-designs` | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | screenshots/design briefs, responsive UI, visual checks, browser verification | volatile |
| `openai.codex.use_cases.make_granular_ui_changes` | Make granular UI changes — Codex use case | `https://developers.openai.com/codex/use-cases/make-granular-ui-changes` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | small UI adjustments, browser verification, focused iteration | volatile |
| `openai.codex.use_cases.figma_designs_to_code` | Turn Figma designs into code — Codex use case | `https://developers.openai.com/codex/use-cases/figma-designs-to-code` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | structured design context, Figma-to-code, Playwright/browser checks | volatile |
| `openai.codex.use_cases.refactor_your_codebase` | Refactor your codebase — Codex use case | `https://developers.openai.com/codex/use-cases/refactor-your-codebase` | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | dead-code removal, modernization, small reviewable behavior-preserving refactor passes | volatile |
| `openai.codex.use_cases.dependency_incident_audits` | Audit dependency incidents — Codex use case | `https://developers.openai.com/codex/use-cases/dependency-incident-audits` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | read-only dependency incident audits, exposure evidence, avoiding lifecycle execution before scope is known | volatile |
| `openai.codex.cloud_internet_access` | Agent internet access — Codex web | `https://developers.openai.com/codex/cloud/internet-access` | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | internet access defaults, allowlists, prompt injection, exfiltration, dependency and license risk | volatile |
| `openai.codex.cloud_environments` | Cloud environments — Codex web | `https://developers.openai.com/codex/cloud/environments` | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | setup scripts, dependency/tool installation, environment configuration, cloud task execution loop | volatile |
| `w3c.wcag22` | Web Content Accessibility Guidelines (WCAG) 2.2 | `https://www.w3.org/TR/WCAG22/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | accessibility recommendations and testable success criteria | stable standard / updates possible |
| `w3c.wcag_overview` | WCAG 2 Overview — W3C WAI | `https://www.w3.org/WAI/standards-guidelines/wcag/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | perceivable/operable/understandable/robust principles and conformance overview | stable standard / updates possible |
| `owasp.dependency_track` | OWASP Dependency-Track | `https://owasp.org/www-project-dependency-track/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | component analysis, SBOM-driven supply-chain risk monitoring | stable concept / tooling evolves |
| `owasp.dependency_graph_sbom` | Dependency Graph & SBOM Best Practices Cheat Sheet — OWASP | `https://cheatsheetseries.owasp.org/cheatsheets/Dependency_Graph_SBOM_Cheat_Sheet.html` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | SBOM and dependency graph framing for vulnerability management and incident response | stable concept / tooling evolves |
| `owasp.top10_2025_supply_chain` | OWASP Top 10 2025 — Software Supply Chain Failures | `https://owasp.org/Top10/2025/A03_2025-Software_Supply_Chain_Failures/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | supply-chain failures caused by vulnerabilities or malicious changes in third-party code/tools/dependencies | volatile / current Top 10 draft |
| `playwright.docs.visual_comparisons` | Playwright visual comparisons | `https://playwright.dev/docs/test-snapshots` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | screenshot visual comparison mechanics | volatile vendor docs |
| `playwright.docs.screenshots` | Playwright screenshots | `https://playwright.dev/docs/screenshots` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | screenshot capture mechanics | volatile vendor docs |
| `npm.docs.audit` | npm audit command | `https://docs.npmjs.com/cli/v8/commands/npm-audit/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | npm dependency vulnerability audit behavior | volatile command docs |
| `github.docs.dependabot_security_updates` | About Dependabot security updates | `https://docs.github.com/en/code-security/concepts/supply-chain-security/about-dependabot-security-updates` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | dependency security/version update PRs | stable concept / UI volatile |
| `github.docs.dependabot_alerts` | About Dependabot alerts | `https://docs.github.com/code-security/dependabot/dependabot-alerts/about-dependabot-alerts` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | vulnerable dependency alerts | stable concept / UI volatile |
| `openssf.scorecard` | OpenSSF Scorecard | `https://scorecard.dev/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | automated supply-chain checks for code, build, dependencies, testing, and maintenance | volatile project docs |
| `openai.codex.app_browser` | In-app browser — Codex app | `https://developers.openai.com/codex/app/browser` | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | in-app browser preview, browser use, screenshots, comments, signed-in-page limitations, untrusted page content | volatile |
| `openai.codex.chrome_extension` | Codex Chrome extension — Codex app | `https://developers.openai.com/codex/app/chrome-extension` | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | signed-in Chrome browser tasks, website approvals, browser-history risk, extension permissions | volatile |
| `openai.codex.remote_connections` | Remote connections — Codex | `https://developers.openai.com/codex/remote-connections` | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | mobile/remote host access, SSH-host projects, remote approvals, remote screenshots/diffs/results | volatile |
| `github.docs.dependency_review` | Dependency review — GitHub Docs | `https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-review` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | dependency diffs, vulnerability/license/age information, dependency review action enforcement | stable concept / UI volatile |
| `github.docs.dependency_graph` | Dependency graph — GitHub Docs | `https://docs.github.com/en/code-security/concepts/supply-chain-security/dependency-graph` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | dependency inventory, manifests/lockfiles, direct/transitive dependencies, vulnerabilities, SBOM export | stable concept / UI volatile |
| `github.docs.dependency_maintenance_best_practices` | Best practices for maintaining dependencies — GitHub Docs | `https://docs.github.com/en/code-security/concepts/supply-chain-security/best-practices-for-maintaining-dependencies` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | dependency graph, dependency review, Dependabot, advisory database maintenance workflows | stable concept / UI volatile |
| `w3c.wai.web_accessibility_intro` | Introduction to Web Accessibility — W3C WAI | `https://www.w3.org/WAI/fundamentals/accessibility-intro/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | accessibility definition and why bad design creates barriers | stable standard / content updated periodically |
| `w3c.wai.wcag22_quickref` | How to Meet WCAG 2.2 Quick Reference — W3C WAI | `https://www.w3.org/WAI/WCAG22/quickref/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | WCAG 2.2 success criteria, techniques, and accessibility checks | stable standard / content updated periodically |
| `npm.docs.scripts` | Scripts — npm Docs | `https://docs.npmjs.com/cli/using-npm/scripts/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | package scripts and lifecycle-script behavior | package-manager behavior volatile |
| `openai.codex.use_cases.web_development` | Web development — Codex use cases | `https://developers.openai.com/codex/use-cases/collections/web-development` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | screenshot/design-to-code, browser verification, web UI iteration, and preview workflows | volatile |
| `openai.codex.use_cases.ios_swiftui_view_refactor` | Refactor SwiftUI screens — Codex use case | `https://developers.openai.com/codex/use-cases/ios-swiftui-view-refactor` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | explicit intentional non-changes during safe UI refactors | volatile |
| `npm.docs.package_json` | package.json — npm Docs | `https://docs.npmjs.com/cli/v11/configuring-npm/package-json/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | dependencies/devDependencies and version ranges | stable concept / docs volatile |
| `npm.docs.package_lock` | package-lock.json — npm Docs | `https://docs.npmjs.com/cli/v8/configuring-npm/package-lock-json/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | lockfile purpose, exact dependency tree, install reproducibility, and diff visibility | stable concept / docs volatile |
| `npm.docs.security_audit` | Auditing package dependencies for security vulnerabilities — npm Docs | `https://docs.npmjs.com/auditing-package-dependencies-for-security-vulnerabilities/` | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | npm audit, vulnerability reports, and dependency-security review | volatile |
| `openai.codex.web_development` | Web development — Codex use-case collection | alias:openai.codex.use_cases.web_development | E0_OFFICIAL_DOCS | alias retained for older Chunk 6 references | targeted frontend changes, browser verification, and web-development use-case routing | volatile |
| `openai.codex.app_computer_use` | Computer Use — Codex app | `https://developers.openai.com/codex/app/computer-use` | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | screen interaction, screenshots, target-app context, and safety guidance for sensitive flows | volatile |
| `mdn.css.media_queries` | Using media queries — MDN Web Docs | `https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Media_queries/Using` | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | responsive design, viewport/device features, and user-preference media queries | stable concept / web-platform docs volatile |
| `martin_fowler.refactoring` | Refactoring — Martin Fowler | `https://martinfowler.com/refactoring/` | E3_EXPERT_REPORT | anchor checked 2026-06-08 | refactoring as disciplined restructuring without changing external behavior | stable expert report |
| `martin_fowler.preparatory_refactoring` | Preparatory refactoring example — Martin Fowler | `https://martinfowler.com/articles/preparatory-refactoring-example.html` | E3_EXPERT_REPORT | anchor checked 2026-06-08 | two-hats framing, behavior preservation, and green tests during refactoring | stable expert report |
| `openai.codex.skills` | Agent Skills — Codex | https://developers.openai.com/codex/skills | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | skill structure, metadata, invocation, locations, and progressive disclosure | volatile |
| `openai.codex.use_cases.reusable_codex_skills` | Save workflows as skills — Codex use case | https://developers.openai.com/codex/use-cases/reusable-codex-skills | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | turning repeated workflows into skill packages | volatile |
| `openai.codex.mcp` | Model Context Protocol — Codex | https://developers.openai.com/codex/mcp | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | MCP purpose, supported server types, authentication concepts, and server instructions | volatile |
| `openai.codex.hooks` | Hooks — Codex | https://developers.openai.com/codex/hooks | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | hook lifecycle, use cases, feature behavior, and trust/review mechanics | volatile |
| `openai.codex.customization` | Customization — Codex | https://developers.openai.com/codex/concepts/customization | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | relationship between AGENTS guidance, skills, MCP, progressive disclosure, and customization layers | volatile |
| `openai.codex.plugins` | Plugins — Codex | https://developers.openai.com/codex/plugins | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | plugin bundles, curated/shared plugins, apps, MCP servers, data-sharing policies, install/disable/uninstall behavior | volatile |
| `vcb.register.editor_feedback_chunk_7` | Editor approval for Chunk 6 / Chunk 7 gate | conversation/editor feedback | internal review | applied | Chunk 7 approved scope and non-scope | stable for this revision |
| `vcb.register.editor_feedback_chunk_8` | Editor approval for Chunk 7 / Chunk 8 gate | conversation/editor feedback | internal review | applied | Chunk 8 approved scope and non-scope | stable for this revision |
| `vcb.register.editor_feedback_chunk_9` | Editor approval for Chunk 8 / Chunk 9 gate | conversation/editor feedback | internal review | applied | Chunk 9 approved scope and non-scope | stable for this revision |
| `vcb.register.editor_feedback_chunk_9_revision` | Editor review for Chunk 9 routing/source hygiene revision | conversation/editor feedback | internal review | applied | Chunk 9 tool-register, source-register, and validator revision | stable for this revision |
| `openai.codex.app_review` | Review — Codex app | https://developers.openai.com/codex/app/review | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | Codex app review pane, Git-backed change inspection, diff scope | volatile |
| `openai.codex.use_cases.github_code_reviews` | Review GitHub pull requests — Codex use case | https://developers.openai.com/codex/use-cases/github-code-reviews | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | PR review use case, regressions, missing tests, risky behavior changes | volatile |
| `openai.codex.security` | Codex Security | https://developers.openai.com/codex/security | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Codex Security plugin/cloud, scan positioning, research-preview caveat | volatile |
| `openai.codex.noninteractive` | Non-interactive mode — Codex | https://developers.openai.com/codex/noninteractive | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | `codex exec`, scripts/CI use, sandbox defaults, structured output, automation auth guidance | volatile |
| `github.docs.actions_secure_use` | Secure use reference — GitHub Actions | https://docs.github.com/en/actions/reference/security/secure-use | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | GitHub Actions secure workflow practices, least privilege, secrets, third-party action risk | stable concept / docs volatile |
| `github.docs.github_token` | Use GITHUB_TOKEN for authentication in workflows | https://docs.github.com/actions/reference/authentication-in-a-workflow | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | GITHUB_TOKEN authentication and permissions for workflows | stable concept / docs volatile |
| `github.docs.actions_oidc` | Configuring OpenID Connect in cloud providers — GitHub Actions | https://docs.github.com/actions/deployment/security-hardening-your-deployments/configuring-openid-connect-in-cloud-providers | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | OIDC workflow authentication without long-lived cloud-provider secrets | stable concept / docs volatile |
| `github.docs.actions_secrets` | Using secrets in GitHub Actions | https://docs.github.com/actions/security-guides/using-secrets-in-github-actions | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | GitHub Actions repository, environment, and organization secrets | stable concept / docs volatile |
| `owasp.top10_web` | OWASP Top Ten Web Application Security Risks | https://owasp.org/www-project-top-ten/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | web application security risk awareness and common risk categories | stable standard / updates possible |
| `owasp.llm_prompt_injection` | LLM Prompt Injection Prevention Cheat Sheet — OWASP | https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | prompt injection risk, impacts, and mitigation framing for LLM applications | volatile security guidance |
| `openai.codex.app_worktrees` | Worktrees — Codex app | https://developers.openai.com/codex/app/worktrees | E0_OFFICIAL_DOCS | anchor checked 2026-06-10 | Codex app worktrees, parallel independent tasks, automation worktree behavior, handoff terminology | volatile |
| `openai.codex.subagents` | Subagents — Codex | https://developers.openai.com/codex/subagents | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | subagent workflows, custom agents, explicit triggering, orchestration, token-use caveats | volatile |
| `openai.codex.subagent_concepts` | Subagents concepts — Codex | https://developers.openai.com/codex/concepts/subagents | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | context pollution, context rot, parallel analysis, subagent terms, write-heavy workflow cautions | volatile |
| `openai.codex.use_cases.manage_your_inbox` | Manage your inbox — Codex use case | https://developers.openai.com/codex/use-cases/manage-your-inbox | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | scheduled triage, reviewable drafts, posting only when attention is needed | volatile |
| `openai.codex.use_cases.proactive_teammate` | Set up a teammate — Codex use case | https://developers.openai.com/codex/use-cases/proactive-teammate | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | connected work context, durable teammate thread, automation after context setup | volatile |
| `openai.codex.glossary` | Codex glossary | https://developers.openai.com/codex/glossary | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | Codex web, Codex-managed worktree, surface terminology | volatile |
| `openai.codex.productivity_collaboration` | Productivity and Collaboration — Codex use cases | https://developers.openai.com/codex/use-cases/collections/productivity-and-collaboration | E0_OFFICIAL_DOCS | anchor checked 2026-06-08 | Computer Use and app-spanning work use-case anchors | volatile |
| `vcb.register.editor_feedback_chunk_10` | Editor approval for Chunk 9 / Chunk 10 gate | conversation/editor feedback | internal review | applied | Chunk 10 approved scope and non-scope | stable for this revision |
| `openai.codex.use_cases.idea_to_proof_of_concept` | Get from idea to proof of concept — Codex use case | https://developers.openai.com/codex/use-cases/idea-to-proof-of-concept | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | smallest useful prototype, browser verification, visual direction, product idea validation | volatile |
| `openai.codex.use_cases.build_and_deploy_internal_apps` | Build and deploy internal apps — Codex use case | https://developers.openai.com/codex/use-cases/build-and-deploy-internal-apps | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | focused internal app workflow, main-flow testing, deployment iteration | volatile |
| `openai.codex.use_cases.update_documentation` | Keep documentation up-to-date — Codex use case | https://developers.openai.com/codex/use-cases/update-documentation | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | documentation update workflows and release/documentation automation | volatile |
| `openai.codex.use_cases.browser_games` | Create browser-based games — Codex use case | https://developers.openai.com/codex/use-cases/browser-games | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | first playable loop, browser testing, game/prototype planning | volatile |
| `vcb.register.editor_feedback_chunk_11` | Editor approval for Chunk 10 / Chunk 11 gate | conversation/editor feedback | internal review | applied | Chunk 11 approved scope and non-scope | stable for this revision |
| `openai.help.codex_chatgpt_plan` | Using Codex with your ChatGPT plan | https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | plan eligibility, agentic usage limits, data controls, workspace/admin notes | highly volatile |
| `openai.help.codex_rate_card` | Codex rate card | https://help.openai.com/en/articles/20001106-codex-rate-card | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | token-based Codex credit rates, credit usage caveats, legacy rate-card note | highly volatile |
| `openai.chatgpt.pricing` | ChatGPT pricing page | https://chatgpt.com/pricing/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | plan packaging, high-level plan features, individual/business plan positioning | highly volatile |
| `openai.codex.models` | Models — Codex | https://developers.openai.com/codex/models | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | current Codex model availability and configuration watchlist | volatile |
| `vcb.pricing_snapshot.openai_codex` | OpenAI/Codex pricing snapshot 2026-06-09 | pricing-snapshots/2026-06-09-openai-codex.md | E2_REPRODUCED_LOCALLY | snapshot captured 2026-06-09 | dated snapshot of volatile OpenAI/Codex credits, limits, and plan availability notes | highly volatile |
| `anthropic.pricing` | Claude pricing | https://claude.com/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | Claude / Claude Code plan packaging, Team and Enterprise pricing caveats, and API-rate anchors | highly volatile |
| `cursor.pricing` | Cursor pricing | https://cursor.com/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | Cursor plan packaging, included usage caveats, JSON-LD Individual offer prices, and Teams pricing | highly volatile |
| `github.copilot.pricing` | GitHub Copilot plans and pricing | https://github.com/features/copilot/plans | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | Copilot Free/Pro/Pro+/Max plan packaging and current plan availability caveats | highly volatile |
| `github.copilot.models_pricing` | Models and pricing for GitHub Copilot | https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | GitHub AI Credits conversion and per-model pricing mechanics | highly volatile |
| `github.copilot.billing_individuals` | Usage-based billing for individuals - GitHub Copilot | https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | individual Copilot AI Credit allowances and overage mechanics | highly volatile |
| `github.copilot.billing_orgs` | Usage-based billing for organizations and enterprises - GitHub Copilot | https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | organization and enterprise Copilot seat prices, AI Credit pooling, and allowances | highly volatile |
| `windsurf.pricing` | Devin / Windsurf pricing | https://devin.ai/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | Devin Desktop / Windsurf plan packaging, Teams minimum-charge model, quotas, and extra-usage caveats | highly volatile |
| `replit.pricing` | Replit pricing | https://replit.com/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | Replit Starter/Core/Pro/Enterprise pricing, monthly credits, and Agent-cost caveats | highly volatile |
| `lovable.pricing` | Lovable pricing | https://lovable.dev/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | Lovable Pro/Business/Enterprise pricing, credits, and Cloud + AI caveats | highly volatile |
| `bolt.pricing` | Bolt pricing | https://bolt.new/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | Bolt Free/Pro/Teams/Enterprise pricing, token limits, hosting, and token-rollover caveats | highly volatile |
| `v0.pricing` | v0 pricing | https://v0.app/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-12; exact values captured in `vcb.pricing_snapshot.ai_coding_tools` | v0 plan pricing, included credits, daily login credits, and model token rates | highly volatile |
| `vcb.pricing_snapshot.ai_coding_tools` | AI coding tools pricing snapshot 2026-06-12 | pricing-snapshots/2026-06-12-ai-coding-tools.md | E2_REPRODUCED_LOCALLY | snapshot captured 2026-06-12 from official vendor pricing pages/docs | dated snapshot of volatile non-OpenAI AI coding, AI IDE, browser-dev, app-builder, and UI-generation prices, credits, tokens, and caveats | highly volatile |
| `vercel.docs.environments` | Vercel Environments | https://vercel.com/docs/deployments/environments | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | preview environments, production/pre-production deployment concepts | volatile |
| `vercel.pricing` | Vercel Pricing | https://vercel.com/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | pricing and plan packaging anchor; exact values belong in snapshot | highly volatile |
| `supabase.docs.database` | Supabase Database overview | https://supabase.com/docs/guides/database/overview | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | Supabase project as full Postgres database; database/backend category anchor | volatile |
| `supabase.docs.auth` | Supabase Auth docs | https://supabase.com/docs/guides/auth | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | auth and user data in Supabase ecosystem | volatile |
| `supabase.pricing` | Supabase Pricing | https://supabase.com/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | pricing and plan packaging anchor; exact values belong in snapshot | highly volatile |
| `stripe.docs.subscriptions` | Stripe Subscriptions docs | https://docs.stripe.com/subscriptions | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | recurring payment/subscription workflow concepts | volatile |
| `stripe.pricing` | Stripe Pricing | https://stripe.com/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | payment pricing anchor; exact fees belong in snapshot | highly volatile |
| `github.docs.actions_billing` | GitHub Actions billing | https://docs.github.com/billing/managing-billing-for-github-actions/about-billing-for-github-actions | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | GitHub Actions billing, minutes, storage, quota concepts | highly volatile |
| `clerk.docs` | Clerk Docs | https://clerk.com/docs | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | authentication, user management, security, billing/deployment docs entrypoint | volatile |
| `auth0.pricing` | Auth0 Pricing | https://auth0.com/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | auth platform pricing and packaging anchor | highly volatile |
| `sentry.docs` | Sentry Docs | https://docs.sentry.io/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | error and performance monitoring concepts | volatile |
| `posthog.pricing` | PostHog Pricing | https://posthog.com/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | product analytics/session replay pricing anchor | highly volatile |

## Chunk 13 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `mdn.glossary.api` | API — MDN Glossary | https://developer.mozilla.org/en-US/docs/Glossary/API | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | API as software interface/contract concept | stable concept / MDN docs volatile |
| `mdn.learn_web_apis` | Introduction to web APIs — MDN | https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Client-side_APIs/Introduction | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | API basics and abstraction framing | stable concept / MDN docs volatile |
| `mdn.learn_web_development` | Learn web development — MDN | https://developer.mozilla.org/en-US/docs/Learn_web_development | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | frontend/web development learning categories and beginner terminology | stable concept / MDN docs volatile |
| `mdn.curriculum_frontend` | MDN Curriculum | https://developer.mozilla.org/en-US/curriculum/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | front-end developer skill structure and web fundamentals | stable concept / MDN docs volatile |
| `owasp.rest_security` | REST Security Cheat Sheet — OWASP | https://cheatsheetseries.owasp.org/cheatsheets/REST_Security_Cheat_Sheet.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | API security and authentication credential transport caveats | stable security guidance / updates possible |
| `postgres.docs.schemas` | PostgreSQL Schemas | https://www.postgresql.org/docs/current/ddl-schemas.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | database schema/namespace terminology and qualified names | stable concept / database docs volatile |
| `prisma.docs.schema` | Prisma schema overview | https://www.prisma.io/docs/orm/prisma-schema/overview | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | schema.prisma as configuration/data-model source | volatile vendor docs |
| `prisma.docs.models` | Prisma models | https://www.prisma.io/docs/orm/prisma-schema/data-model/models | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | data model and database schema source-of-truth framing | volatile vendor docs |
| `owasp.authentication_cheat_sheet` | Authentication Cheat Sheet — OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | authentication as verifying identity and authenticator validity | stable security guidance / updates possible |
| `owasp.session_management` | Session Management Cheat Sheet — OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Session_Management_Cheat_Sheet.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | session/token security concepts for authentication topics | stable security guidance / updates possible |
| `owasp.authorization_cheat_sheet` | Authorization Cheat Sheet — OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | authorization logic and access-control guidance | stable security guidance / updates possible |
| `react.docs.state_memory` | State: A Component's Memory — React | https://react.dev/learn/state-a-components-memory | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | state as component memory and remembering information between renders | stable concept / React docs volatile |
| `react.docs.managing_state` | Managing State — React | https://react.dev/learn/managing-state | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | organizing state, data flow, and duplicate-state bug framing | stable concept / React docs volatile |
| `mdn.js.promises` | Promise — MDN JavaScript Reference | https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Promise | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | eventual completion/failure of asynchronous operations | stable language concept / MDN docs volatile |
| `mdn.async_javascript` | Asynchronous JavaScript — MDN | https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Async_JS | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | synchronous/asynchronous programming, promises, async/await learning path | stable language concept / MDN docs volatile |
| `npm.docs.package_dependencies` | Specifying dependencies and devDependencies — npm Docs | https://docs.npmjs.com/specifying-dependencies-and-devdependencies-in-a-package-json-file/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | dependencies/devDependencies in package.json | stable package-manager concept / npm docs volatile |
| `typescript.docs.home` | TypeScript home | https://www.typescriptlang.org/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | TypeScript adds types and catches errors in editor/compiler workflows | stable concept / docs volatile |
| `typescript.docs.basic_types` | TypeScript Handbook — The Basics | https://www.typescriptlang.org/docs/handbook/2/basic-types.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | type checking and tsc compiler concept | stable concept / docs volatile |
| `eslint.docs.home` | ESLint home | https://eslint.org/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | ESLint as tool for finding/fixing JavaScript code problems | stable concept / docs volatile |
| `eslint.docs.latest` | ESLint documentation | https://eslint.org/docs/latest/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | pluggable configurable linter documentation anchor | stable concept / docs volatile |
| `liquibase.docs.intro` | Introduction to Liquibase | https://docs.liquibase.com/secure/implementation-guide-5-1-1/intro-to-liquibase | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | database changelog/change-set migration concepts | volatile vendor docs |
| `flyway.docs.migrations` | Flyway Migrations | https://documentation.red-gate.com/fd/migrations-271585107.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | migrations as incremental database changes tracked in version control | volatile vendor docs |
| `twelve_factor.config` | The Twelve-Factor App — Config | https://12factor.net/config | E3_EXPERT_REPORT | anchor checked 2026-06-09 | config in environment variables and separation from code | stable expert/practitioner guidance |
| `vite.docs.build` | Vite — Building for Production | https://vite.dev/guide/build | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | production build command and static bundle output framing | volatile vendor docs |
| `webpack.docs.concepts` | webpack concepts | https://webpack.js.org/concepts/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | module bundling, dependency graph, bundles, loaders/plugins/mode concepts | volatile vendor docs |
| `github.docs.actions_overview` | GitHub Actions documentation | https://docs.github.com/actions | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | workflow automation, CI/CD entrypoint | volatile vendor docs |
| `github.docs.actions_ci` | Continuous integration with GitHub Actions | https://docs.github.com/en/actions/get-started/continuous-integration | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | CI workflows that build code and run tests | volatile vendor docs |
| `martin_fowler.feature_toggles` | Feature Toggles — Martin Fowler | https://martinfowler.com/articles/feature-toggles.html | E3_EXPERT_REPORT | anchor checked 2026-06-09 | feature flags/toggles modifying system behavior without changing code; toggle complexity caveat | stable expert report |
| `opentelemetry.docs.what_is_opentelemetry` | What is OpenTelemetry? | https://opentelemetry.io/docs/what-is-opentelemetry/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | observability, telemetry, traces, metrics, logs, instrumentation | stable concept / docs volatile |
| `opentelemetry.docs.observability_primer` | Observability primer — OpenTelemetry | https://opentelemetry.io/docs/concepts/observability-primer/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | observability as understanding systems from outputs and answering unknown-unknowns | stable concept / docs volatile |
| `sentry.docs.platform` | Sentry platform docs | alias:sentry.docs | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | alias to `sentry.docs`; error monitoring and observability vendor anchor | volatile vendor docs |
| `vcb.register.editor_feedback_chunk_12` | Editor approval for Chunk 12 / Chunk 13 gate | conversation/editor feedback | internal review | applied | Chunk 13 approved scope and non-scope | stable for this revision |
| `jest.docs_getting_started` | Getting Started — Jest | https://jestjs.io/docs/getting-started | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | JavaScript testing framework setup/getting-started anchor for test concept | volatile vendor docs |
| `nodejs.docs_environment_variables` | Environment Variables — Node.js Docs | https://nodejs.org/api/environment_variables.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | process.env and dotenv/environment variable concepts | stable runtime concept / docs volatile |
| `openfeature.docs_intro` | Introduction — OpenFeature | https://openfeature.dev/docs/reference/intro/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | feature flags as runtime-controlled behavior and vendor-agnostic flag evaluation | stable feature-flag concept / docs volatile |

## Chunk 16 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_15` | Editor approval for Chunk 15 / Chunk 16 gate | conversation/editor feedback | internal review | applied | Chunk 16 approved scope and non-scope | stable for this revision |
| `openai.codex.security_plugin` | Codex Security plugin | https://developers.openai.com/codex/security/plugin | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Codex Security plugin review workflows, change-set scans, and fix-finding loop | volatile |
| `openai.codex.security_setup` | Codex Security setup | https://developers.openai.com/codex/security/setup | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Codex Security cloud setup, initial scans, finding review, and PR creation posture | volatile |
| `openai.codex.security_threat_model` | Improving the threat model — Codex Security | https://developers.openai.com/codex/security/threat-model | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | repository threat model context, entry points, trust boundaries, auth, and sensitive data paths | volatile |
| `openai.codex.security_faq` | FAQ — Codex Security | https://developers.openai.com/codex/security/faq | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | validation, isolation, patch-application boundaries, finding outputs, and manual-review limits | volatile |
| `owasp.secrets_management` | Secrets Management Cheat Sheet — OWASP | https://cheatsheetseries.owasp.org/cheatsheets/Secrets_Management_Cheat_Sheet.html | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | secret lifecycle, storage, rotation, auditing, and CI/CD secret guidance | stable security guidance / updates possible |


## Chunk 17 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_16` | Editor approval for Chunk 16 / Chunk 17 gate | conversation/editor feedback | internal review | applied | Chunk 17 approved scope and non-scope | stable for this revision |
| `playwright.docs.accessibility_testing` | Accessibility testing — Playwright | https://playwright.dev/docs/accessibility-testing | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | browser-automation accessibility testing and automated accessibility checks | volatile vendor docs |
| `github.docs.dependabot_version_updates` | About Dependabot version updates | https://docs.github.com/en/code-security/concepts/supply-chain-security/about-dependabot-version-updates | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | automated dependency version-update pull requests and update-review workflows | volatile vendor docs |
| `github.docs.release_notes_generated` | Automatically generated release notes | https://docs.github.com/en/repositories/releasing-projects-on-github/automatically-generated-release-notes | E0_OFFICIAL_DOCS | anchor checked 2026-06-09 | generated release notes, PR lists, changelog links, categories, and exclusions | volatile vendor docs |
| `keepachangelog.v1_1_0` | Keep a Changelog 1.1.0 | https://keepachangelog.com/en/1.1.0/ | E3_EXPERT_REPORT | anchor checked 2026-06-09 | human-readable chronological changelog categories and release-note discipline | stable practitioner guidance |


## Chunk 18 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_17` | Editor approval for Chunk 17 / Chunk 18 gate | conversation/editor feedback | internal review | applied | Chunk 18 approved scope and non-scope | stable for this revision |

## Chunk 19 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_18` | Editor approval for Chunk 18 / Chunk 19 gate | conversation/editor feedback | internal review | applied | Chunk 19 approved scope and non-scope | stable for this revision |

## Chunk 20 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_19` | Editor approval for Chunk 19 / Chunk 20 gate | conversation/editor feedback | internal review | applied | Chunk 20 approved scope and non-scope | stable for this revision |

## Chunk 21 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_20` | Editor approval for Chunk 20 / Chunk 21 gate | conversation/editor feedback | internal review | applied | Chunk 21 approved scope and non-scope | stable for this revision |




## Chunk 22 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_21` | Editor approval for Chunk 21 / Chunk 22 gate | conversation/editor feedback | internal review | applied | Chunk 22 approved scope and non-scope | stable for this revision |

## Chunk 23 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_22` | Editor approval for Chunk 22 / Chunk 23 gate | conversation/editor feedback | internal review | applied | Chunk 23 approved scope and non-scope | stable for this revision |

## Chunk 24 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_23` | Editor approval for Chunk 23 / Chunk 24 gate | conversation/editor feedback | internal review | applied | Chunk 24 approved scope and non-scope | stable for this revision |

## Chunk 25 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_24` | Editor approval for Chunk 24 / Chunk 25 gate | conversation/editor feedback | internal review | applied | Chunk 25 approved scope and non-scope | stable for this revision |

## Chunk 27 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_26` | Editor approval for Chunk 26 / Chunk 27 gate | conversation/editor feedback | internal review | applied | Chunk 27 approved scope and non-scope | stable for this revision |

## Chunk 28 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_27` | Editor approval for Chunk 27 / Chunk 28 gate | conversation/editor feedback | internal review | applied | Chunk 28 approved scope and non-scope | stable for this revision |

## Chunk 29 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_28` | Editor approval for Chunk 28 / Chunk 29 gate | conversation/editor feedback | internal review | applied | Chunk 29 approved scope and non-scope | stable for this revision |


## Chunk 30 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_29` | Editor approval for Chunk 29 / Chunk 30 gate | conversation/editor feedback | internal review | applied | Chunk 30 approved scope and non-scope | stable for this revision |


## Chunk 31 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_30` | Editor approval for Chunk 30 / Chunk 31 gate | conversation/editor feedback | internal review | applied | Chunk 31 approved scope and non-scope | stable for this revision |

## Chunk 32 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_31` | Editor approval for Chunk 31 / Chunk 32 gate | conversation/editor feedback | internal review | applied | Chunk 32 approved scope and non-scope | stable for this revision |
| `github.docs.repositories` | Repositories documentation — GitHub Docs | https://docs.github.com/en/repositories | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | GitHub repositories as project code collaboration and management surfaces | volatile vendor docs |
| `github.docs.actions_workflow_syntax` | Workflow syntax for GitHub Actions | https://docs.github.com/actions/using-workflows/workflow-syntax-for-github-actions | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | workflow files, jobs, events, permissions, and automation definitions | volatile vendor docs |
| `github.docs.dependabot_quickstart` | Dependabot quickstart guide | https://docs.github.com/en/code-security/tutorials/secure-your-dependencies/dependabot-quickstart-guide | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Dependabot feature family and setup/review entrypoint | volatile vendor docs |
| `playwright.docs.intro` | Playwright introduction | https://playwright.dev/docs/intro | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Playwright Test positioning, browser support, runner, assertions, isolation, and tooling | volatile project docs |
| `playwright.docs.writing_tests` | Writing tests — Playwright | https://playwright.dev/docs/writing-tests | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | browser action/assertion test-writing guidance and auto-wait expectations | volatile project docs |
| `playwright.docs.ci` | Continuous Integration — Playwright | https://playwright.dev/docs/ci | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | running Playwright tests in CI and browser dependency setup | volatile project docs |
| `openssf.scorecard_checks` | OpenSSF Scorecard check documentation | https://github.com/ossf/scorecard/blob/main/docs/checks.md | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Scorecard check categories, remediation guidance, and scoring/mechanics watchlist | volatile project docs |
| `openssf.scorecard_action` | OpenSSF Scorecard GitHub Action | https://github.com/ossf/scorecard-action | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Scorecard GitHub Action integration and CI publishing posture | volatile project docs |

## Chunk 33 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_32` | Editor approval for Chunk 32 / Chunk 33 gate | conversation/editor feedback | internal review | applied | Chunk 33 approved scope and non-scope | stable for this revision |
| `openai.help.chatgpt_capabilities` | ChatGPT Capabilities Overview | https://help.openai.com/en/articles/9260256-chatgpt-capabilities-overview | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | ChatGPT core capabilities, tools, projects, data-analysis, Canvas, files, and volatile capability posture | volatile OpenAI docs |
| `openai.help.chatgpt_projects` | Projects in ChatGPT | https://help.openai.com/en/articles/10169521-projects-in-chatgpt | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | ChatGPT project/workspace context, files, instructions, and collaboration posture | volatile OpenAI docs |
| `openai.help.chatgpt_data_analysis` | Data analysis with ChatGPT | https://help.openai.com/en/articles/8437071-data-analysis-with-chatgpt | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | ChatGPT file analysis, tables/charts, code-backed analysis, and review caveats | volatile OpenAI docs |
| `anthropic.docs.claude_intro` | Intro to Claude | https://platform.claude.com/docs/en/intro | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Claude capability overview and use as reasoning, analysis, coding, and AI-assistant surface | volatile vendor docs |
| `anthropic.docs.claude_code_overview` | Claude Code overview | https://code.claude.com/docs/en/overview | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Claude Code as agentic coding tool, file edits, command use, terminal/IDE/browser/desktop surfaces | volatile vendor docs |
| `anthropic.docs.prompt_engineering_overview` | Prompt engineering overview — Claude Docs | https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/overview | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | success criteria, evaluation-first prompt iteration, and prompt-engineering boundaries | volatile vendor docs |
| `anthropic.support.claude_projects` | What are projects? — Claude Help Center | https://support.claude.com/en/articles/9517075-what-are-projects | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Claude projects, knowledge context, instructions, and collaboration/visibility posture | volatile vendor docs |
| `cursor.docs.agent_overview` | Agent overview — Cursor Docs | https://cursor.com/docs/agent/overview | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Cursor agent as autonomous coding, terminal-command, and code-editing surface | volatile vendor docs |
| `cursor.docs.plan_mode` | Plan Mode — Cursor Docs | https://cursor.com/docs/agent/plan-mode | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Cursor plan-first/reviewable implementation planning posture | volatile vendor docs |
| `cursor.docs.agent_review` | Agent Review — Cursor Docs | https://cursor.com/docs/agent/agent-review | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Cursor review surface and agent-review workflow positioning | volatile vendor docs |
| `cursor.security` | Security — Cursor | https://cursor.com/security | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Cursor security, privacy, client/agent security, and data-control posture | volatile vendor docs |
| `github.docs.copilot_overview` | What is GitHub Copilot? | https://docs.github.com/en/copilot/get-started/what-is-github-copilot | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Copilot overview, IDE/repository assistance, chat, and agentic GitHub capabilities | volatile vendor docs |
| `github.docs.copilot_code_suggestions` | GitHub Copilot code suggestions | https://docs.github.com/en/copilot/concepts/completions/code-suggestions | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | inline suggestion behavior and IDE code-completion posture | volatile vendor docs |
| `github.docs.copilot_best_practices` | Best practices for using GitHub Copilot | https://docs.github.com/en/copilot/get-started/best-practices | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | choosing the right Copilot tool and treating Copilot output with appropriate review | volatile vendor docs |
| `github.docs.copilot_cloud_agent` | About GitHub Copilot cloud agent | https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-cloud-agent | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Copilot cloud agent planning, branch changes, review, and PR workflow posture | volatile vendor docs |
| `windsurf.docs.getting_started` | Welcome to Devin Desktop | https://docs.devin.ai/desktop/getting-started | E0_OFFICIAL_DOCS | canonical URL checked 2026-06-11; old URL redirected | Windsurf/Devin Desktop setup and AI IDE positioning | volatile vendor docs |
| `windsurf.docs.cascade` | Cascade Overview | https://docs.devin.ai/desktop/cascade/cascade | E0_OFFICIAL_DOCS | canonical URL checked 2026-06-11; old URL redirected | Cascade agentic coding, Code/Chat modes, tool calling, checkpoints, linter integration, and simultaneous Cascade behavior | volatile vendor docs |
| `windsurf.docs.plugins` | Welcome to Windsurf Plugins | https://docs.devin.ai/windsurf/plugins/getting-started | E0_OFFICIAL_DOCS | canonical URL checked 2026-06-11; old URL redirected | Windsurf plugin surfaces for IDE/editor coding assistance | volatile vendor docs |
| `windsurf.docs.admin_controls` | Guide for Admins — Devin Desktop | https://docs.devin.ai/desktop/guide-for-admins | E0_OFFICIAL_DOCS | canonical URL checked 2026-06-11; old URL redirected | organization feature toggles, admin controls, and data-privacy-sensitive feature posture | volatile vendor docs |
| `windsurf.docs.cascade_hooks` | Cascade Hooks | https://docs.devin.ai/desktop/cascade/hooks | E0_OFFICIAL_DOCS | canonical URL checked 2026-06-11; old URL redirected | Windsurf/Cascade lifecycle hooks, shell-script extensibility, and governance risk | volatile vendor docs |

## Chunk 34 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_33` | Editor approval for Chunk 33 / Chunk 34 gate | conversation/editor feedback | internal review | applied | Chunk 34 approved scope and non-scope | stable for this revision |
| `replit.docs.build_welcome` | Replit Docs — Build welcome | https://docs.replit.com/build/welcome | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Replit browser-based idea-to-app/product-building overview | volatile vendor docs |
| `replit.docs.agent_overview` | Replit Agent overview | https://docs.replit.com/references/agent/overview | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Replit Agent plain-language app/design/build positioning | volatile vendor docs |
| `replit.docs.first_app` | Build and publish your first app — Replit | https://docs.replit.com/build/your-first-app | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Replit build/test/publish loop and Agent handoff framing | volatile vendor docs |
| `replit.docs.publish` | Publish your app — Replit | https://docs.replit.com/build/publish-your-app | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Replit publishing/access posture and volatile deployment controls | volatile vendor docs |
| `replit.docs.effective_prompting` | Effective prompting with Replit AI | https://docs.replit.com/learn/effective-prompting | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Replit prompt quality, clear instructions, and app-building guidance | volatile vendor docs |
| `lovable.docs.welcome` | Welcome to Lovable | https://docs.lovable.dev/introduction/welcome | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Lovable full-stack AI development platform overview | volatile vendor docs |
| `lovable.docs.getting_started` | Quick start — Lovable | https://docs.lovable.dev/introduction/getting-started | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Lovable create/edit/full-stack/publish workflow overview | volatile vendor docs |
| `lovable.docs.cloud` | Lovable Cloud | https://docs.lovable.dev/integrations/cloud | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Lovable cloud/backend/auth/storage/function positioning | volatile vendor docs |
| `lovable.docs.best_practice` | Lovable best practices | https://docs.lovable.dev/tips-tricks/best-practice | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Lovable planning, knowledge, preview, and version-control practice anchor | volatile vendor docs |
| `lovable.docs.integrations` | Lovable integrations | https://docs.lovable.dev/integrations/introduction | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Lovable external tools, MCP, APIs, third-party service integration | volatile vendor docs |
| `bolt.docs.intro` | Introduction to Bolt | https://support.bolt.new/building/intro-bolt | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Bolt AI-powered website/web-app/mobile-app builder overview | volatile vendor docs |
| `bolt.docs.quickstart` | Bolt QuickStart guide | https://support.bolt.new/building/quickstart | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Bolt browser-based build/edit/publish quickstart workflow | volatile vendor docs |
| `bolt.docs.plan_app` | Plan your app — Bolt | https://support.bolt.new/building/build-your-first-app | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Bolt planning, web/mobile app target, and built-in hosting context | volatile vendor docs |
| `bolt.docs.tokens` | Tokens — Bolt | https://support.bolt.new/account-and-subscription/tokens | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Bolt token/usage-cost concept and budget volatility anchor | highly volatile vendor docs |
| `bolt.docs.glossary` | Glossary — Bolt | https://support.bolt.new/concepts/glossary | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Bolt full-stack/backend/frontend terminology and generated app scope | volatile vendor docs |
| `v0.docs.what_is_v0` | What is v0? | https://v0.app/docs | E0_OFFICIAL_DOCS | canonical URL checked 2026-06-11; old URL redirected | v0 AI agent/app/UI generation, live prototypes, deploy/PR positioning | volatile vendor docs |
| `v0.docs.design_systems` | Design systems — v0 Docs | https://v0.app/docs/design-systems | E0_OFFICIAL_DOCS | canonical URL checked 2026-06-11; old URL redirected | v0 Tailwind, shadcn/ui, registry, design-system context | volatile vendor docs |
| `v0.docs.figma` | Figma — v0 Docs | https://v0.app/docs/figma | E0_OFFICIAL_DOCS | canonical URL checked 2026-06-11; old URL redirected | v0 Figma/design-context to high-fidelity UI workflow | volatile vendor docs |
| `v0.docs.platform_api` | v0 Platform API overview | https://v0.app/docs/api/platform/overview | E0_OFFICIAL_DOCS | canonical URL checked 2026-06-11; old URL redirected | v0 programmatic code generation, project management, deployment workflow anchor | volatile vendor docs |

## Chunk 35 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_34` | Editor approval for Chunk 34 / Chunk 35 gate | conversation/editor feedback | internal review | applied | Chunk 35 approved scope and non-scope | stable for this revision |
| `vercel.docs.overview` | Vercel Documentation | https://vercel.com/docs | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Vercel platform overview, Git-connected deployment, preview environments, and marketplace/integration positioning | volatile vendor docs |
| `vercel.docs.deployments` | Deploying to Vercel | https://vercel.com/docs/deployments | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Vercel local/preview/production environments, deployment dashboard, resources, logs, and promotion workflow | volatile vendor docs |
| `vercel.docs.observability` | Vercel Observability | https://vercel.com/docs/observability | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Vercel project monitoring, traffic/performance insight, and production visibility posture | volatile vendor docs |
| `vercel.docs.analytics` | Vercel Web Analytics | https://vercel.com/docs/analytics | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Vercel Web Analytics usage for visitor/page/referrer/browser/device insight; exact pricing/limits excluded | volatile vendor docs |
| `supabase.docs.overview` | Supabase Docs | https://supabase.com/docs | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Supabase product surface: database, auth, storage, realtime, edge functions | volatile vendor docs |
| `supabase.docs.edge_functions` | Edge Functions — Supabase Docs | https://supabase.com/docs/guides/functions | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Supabase server-side TypeScript functions and webhook/third-party integration anchor | volatile vendor docs |
| `supabase.docs.secrets` | Environment Variables — Supabase Edge Functions | https://supabase.com/docs/guides/functions/secrets | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Supabase function secrets, publishable/anon/service-role key posture, and RLS bypass warning | volatile vendor docs |
| `clerk.docs.overview` | Welcome to Clerk Docs | alias:clerk.docs | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Clerk authentication, user management, sessions, organizations, UI/components, and deployment/auth guides | volatile vendor docs |
| `clerk.docs.user_management` | User management — Clerk Docs | https://clerk.com/docs/guides/users/managing | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Clerk dashboard/programmatic user management and profile/auth data workflows | volatile vendor docs |
| `clerk.docs.session_tokens` | Session tokens — Clerk Docs | https://clerk.com/docs/guides/sessions/session-tokens | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Clerk session tokens, backend request auth, JWT/session evidence, and volatile token mechanics | volatile vendor docs |
| `clerk.docs.organizations` | Organizations — Clerk Docs | https://clerk.com/docs/guides/organizations/overview | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Clerk organization roles/permissions and multi-tenant B2B app posture | volatile vendor docs |
| `clerk.docs.restrictions` | Restrictions — Clerk Docs | https://clerk.com/docs/guides/secure/restricting-access | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Clerk sign-up/sign-in restrictions and access-control surface | volatile vendor docs |
| `auth0.docs.get_started` | Get Started — Auth0 Docs | https://auth0.com/docs/get-started | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Auth0 IAM platform, app/API scenarios, and implementation quickstart posture | volatile vendor docs |
| `auth0.docs.flows` | Authentication and Authorization Flows — Auth0 Docs | https://auth0.com/docs/get-started/authentication-and-authorization-flow | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Auth0 OIDC/OAuth flow selection and application/API auth posture | volatile vendor docs |
| `auth0.docs.universal_login` | Auth0 Universal Login | https://auth0.com/docs/authenticate/login/auth0-universal-login | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Auth0 hosted login flow and authorization-server authentication surface | volatile vendor docs |
| `auth0.docs.apis` | APIs — Auth0 Docs | https://auth0.com/docs/get-started/apis | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Auth0 API/resource-server model and protected resource request anchor | volatile vendor docs |
| `auth0.docs.organizations` | Organizations login flows — Auth0 Docs | https://auth0.com/docs/manage-users/organizations/login-flows-for-organizations | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Auth0 organization/B2B login routing and identity-provider selection posture | volatile vendor docs |
| `stripe.docs.billing_quickstart` | Prebuilt subscription page with Stripe Checkout | https://docs.stripe.com/billing/quickstart | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Stripe Billing APIs, subscriptions/invoices/recurring payments, and Stripe-hosted Checkout posture | volatile vendor docs |
| `stripe.docs.webhooks` | Receive Stripe events in your webhook endpoint | https://docs.stripe.com/webhooks | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Stripe asynchronous event/webhook handling, HTTPS endpoint, and fulfillment evidence posture | volatile vendor docs |
| `stripe.docs.checkout` | Checkout — Stripe Documentation | https://docs.stripe.com/payments/checkout | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Stripe hosted checkout/payment collection posture; exact fees/features excluded | volatile vendor docs |
| `sentry.docs.overview` | Sentry Docs | alias:sentry.docs | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Sentry end-to-end distributed tracing, error/performance debugging, session replay/logs overview | volatile vendor docs |
| `sentry.docs.product` | Product walkthroughs — Sentry Docs | https://docs.sentry.io/product/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Sentry product positioning as software monitoring for errors, performance issues, traces, and observability | volatile vendor docs |
| `sentry.docs.performance` | Performance Monitoring — Sentry Docs | https://docs.sentry.io/product/sentry-basics/performance-monitoring/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Sentry performance monitoring, distributed tracing, bottleneck, and automated issue detection posture | volatile vendor docs |
| `sentry.docs.session_replay` | Session Replay — Sentry Docs | https://docs.sentry.io/product/explore/session-replay/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Sentry replay/debugging context and privacy-sensitive browser evidence posture | volatile vendor docs |
| `posthog.docs.overview` | PostHog Docs | https://posthog.com/docs | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | PostHog developer apps: product analytics, replay, feature flags, experiments, data warehouse, logs/tracing | volatile vendor docs |
| `posthog.docs.product_analytics` | Getting started with Product Analytics — PostHog Docs | https://posthog.com/docs/product-analytics/start-here | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | PostHog product analytics, funnels, retention, dashboards, replay/feature-flag integration; exact pricing excluded | volatile vendor docs |
| `posthog.docs.events` | Events — PostHog Docs | https://posthog.com/docs/data/events | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | PostHog event model, event properties, identity, and analytics-data posture | volatile vendor docs |
| `posthog.docs.feature_flags` | Feature flags — PostHog Docs | https://posthog.com/docs/feature-flags | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | PostHog feature flags, experiments, product analytics, replay, error-tracking, and rollout/revert context | volatile vendor docs |
| `posthog.docs.session_replay` | Getting started with Session Replay — PostHog Docs | https://posthog.com/docs/session-replay/start-here | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | PostHog session replay and user-behavior evidence posture | volatile vendor docs |

## Chunk 36 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_35` | Editor approval for Chunk 35 / Chunk 36 gate | conversation/editor feedback | internal review | applied | Chunk 36 approved scope and non-scope | stable for this revision |
| `docker.docs.overview` | What is Docker? — Docker Docs | https://docs.docker.com/get-started/docker-overview/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Docker platform, containers, images, registries, client/daemon, and lifecycle framing | volatile vendor docs |
| `docker.docs.compose` | Docker Compose — Docker Docs | https://docs.docker.com/compose/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | multi-container application orchestration and Compose surface/source-check posture | volatile vendor docs |
| `docker.docs.dockerfile` | Dockerfile reference — Docker Docs | https://docs.docker.com/reference/dockerfile/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Dockerfile/image-building mechanics and command/reference volatility | volatile vendor docs |
| `docker.docs.security` | Docker Engine security — Docker Docs | https://docs.docker.com/engine/security/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Docker/container isolation, daemon/host security posture, and container risk caveats | volatile vendor docs |
| `docker.pricing` | Docker Pricing | https://www.docker.com/pricing/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | pricing, plan, and Docker Desktop licensing anchor; exact values belong in snapshots | highly volatile |
| `figma.docs.design` | Figma Design | https://www.figma.com/design/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | collaborative design, prototyping, product-development, and design-handoff positioning | volatile vendor docs |
| `figma.help.prototyping` | Guide to prototyping in Figma | https://help.figma.com/hc/en-us/articles/360040314193-Guide-to-prototyping-in-Figma | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | prototype flows, interactions, stakeholder feedback, and design-review evidence | volatile vendor docs |
| `figma.help.components` | Guide to components in Figma | https://help.figma.com/hc/en-us/articles/360038662654-Guide-to-components-in-Figma | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | components, instances, libraries, variants, and design-system consistency | volatile vendor docs |
| `figma.help.dev_mode` | Guide to Dev Mode — Figma Help Center | https://help.figma.com/hc/en-us/articles/15023124644247-Guide-to-Dev-Mode | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Dev Mode inspection, ready-for-development status, annotations, linked tickets, and handoff mechanics | volatile vendor docs |
| `figma.pricing` | Figma Pricing | https://www.figma.com/pricing/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | pricing and seat/package anchor; exact values belong in snapshots | highly volatile |
| `linear.docs.concepts` | Concepts — Linear Docs | https://linear.app/docs/conceptual-model | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | workspace, teams, issues, projects, cycles, views, and conceptual model | volatile vendor docs |
| `linear.docs.projects` | Projects — Linear Docs | https://linear.app/docs/projects | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | projects, outcomes, project leads, shared projects, views, milestones, and scope | volatile vendor docs |
| `linear.docs.teams` | Teams — Linear Docs | https://linear.app/docs/teams | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | teams, team-scoped work, workflows, cycles, project relationships, and workspace organization | volatile vendor docs |
| `linear.docs.issue_status` | Issue status — Linear Docs | https://linear.app/docs/configuring-workflows | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | issue statuses, workflow state, and team-specific status mechanics | volatile vendor docs |
| `linear.docs.cycles` | Cycles — Linear Docs | https://linear.app/docs/use-cycles | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | cycle cadence, team planning periods, and workflow timing mechanics | volatile vendor docs |
| `linear.pricing` | Linear Pricing | https://linear.app/pricing | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | pricing and plan/package anchor; exact values belong in snapshots | highly volatile |

## Chunk 37 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_36` | Editor approval for Chunk 36 / Chunk 37 gate | conversation/editor feedback | internal review | applied | Chunk 37 approved cleanup scope and non-scope | stable for this revision |

- Chunk 37 performs repository-contract cleanup only. It adds no new product facts, pricing facts, capability claims, or tool cards. It canonicalizes official redirecting Windsurf/Devin and v0 source URLs after verifying that the old URLs redirect to official docs.devin.ai and v0.app destinations, and it preserves existing source IDs so active card evidence remains stable.


## Chunk 38 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_37` | Editor approval for Chunk 37 / Chunk 38 gate | conversation/editor feedback | internal review | applied | Chunk 38 approved field-practice candidate-card scope and non-scope | stable for this revision |

- Chunk 38 authors candidate field-practice cards from FIELD_PRACTICES. It refreshes selected official OpenAI/Codex anchors used as principle support, while preserving the field-practice evidence status as candidate/community-reported rather than official or locally reproduced. No new external source IDs are required for this slice.

## Chunk 40 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_39` | Editor approval for Chunk 39 / Chunk 40 gate | conversation/editor feedback | internal review | applied | Chunk 40 approved coverage-gap audit scope and non-scope | stable for this revision |
| `vcb.register.editor_feedback_chunk_40` | Editor approval for Chunk 40 / Chunk 41 gate | conversation/editor feedback | internal review | applied | Chunk 41 finalization-readiness audit scope and non-scope | stable for this revision |
| `cloudflare.docs.developer_overview` | Cloudflare Developer Docs | https://developers.cloudflare.com/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Cloudflare developer platform, edge/web app delivery, and current product-surface source anchor | volatile vendor docs |
| `cloudflare.docs.workers` | Cloudflare Workers Docs | https://developers.cloudflare.com/workers/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Workers serverless app/runtime positioning and source-checked mechanics | volatile vendor docs |
| `cloudflare.docs.pages` | Cloudflare Pages Docs | https://developers.cloudflare.com/pages/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Pages frontend deployment, Workers/Pages relationship, and app-hosting posture | volatile vendor docs |
| `cloudflare.docs.dns` | Cloudflare DNS Docs | https://developers.cloudflare.com/dns/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | DNS/domain/routing posture and volatile domain/DNS mechanics | volatile vendor docs |
| `netlify.docs.overview` | Netlify Documentation | https://docs.netlify.com/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Netlify platform source anchor and current documentation index | volatile vendor docs |
| `netlify.docs.deploy_overview` | Deploy overview — Netlify Docs | https://docs.netlify.com/deploy/deploy-overview/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | deploys, deploy contexts, branches, permissions, and deployment evidence | volatile vendor docs |
| `netlify.docs.functions_overview` | Functions overview — Netlify Docs | https://docs.netlify.com/build/functions/overview/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Netlify Functions, deploy previews, rollback, and full-stack/serverless behavior | volatile vendor docs |
| `netlify.docs.environment_variables` | Environment variables overview — Netlify Docs | https://docs.netlify.com/build/environment-variables/overview/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | environment variables, deploy contexts, and secret/config review posture | volatile vendor docs |
| `neon.docs.introduction` | Neon documentation | https://neon.com/docs/introduction | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Neon Postgres platform positioning, serverless/branchable backend posture, and current docs source anchor | volatile vendor docs |
| `neon.docs.connect` | Connect to Neon — Neon Docs | https://neon.com/docs/connect/connect-intro | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | database connection approaches, connection evidence, and volatile setup mechanics | volatile vendor docs |
| `neon.docs.branching` | Branching — Neon Docs | https://neon.com/docs/introduction/branching | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | database branching, preview data, copy-on-write clone posture, and migration-test evidence | volatile vendor docs |
| `resend.docs.introduction` | Introduction — Resend Docs | https://resend.com/docs/introduction | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Resend product/docs anchor and developer email API posture | volatile vendor docs |
| `resend.docs.send_email` | Send Email — Resend Docs | https://resend.com/docs/api-reference/emails/send-email | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | send-email API behavior, request/response mechanics, and source-checked email integration | volatile vendor docs |
| `resend.docs.templates` | Templates — Resend Docs | https://resend.com/docs/dashboard/templates/introduction | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | template-driven transactional email and variable substitution mechanics | volatile vendor docs |
| `vitest.docs.guide` | Getting Started — Vitest Guide | https://vitest.dev/guide/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Vitest testing framework positioning and Vite-native test-runner mechanics | volatile project docs |
| `vitest.docs.browser_component_testing` | Component Testing — Vitest Guide | https://vitest.dev/guide/browser/component-testing | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | browser/component testing support and source-checked scope limits | volatile project docs |
| `vitest.docs.api_test` | Test API — Vitest Docs | https://vitest.dev/api/test | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | test API mechanics and source-checked exact syntax/reference behavior | volatile project docs |
| `storybook.docs.overview` | Storybook | https://storybook.js.org/ | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Storybook frontend workshop/product positioning for components, pages, testing, and docs | volatile project docs |
| `storybook.docs.get_started` | Get started with Storybook — Storybook docs | https://storybook.js.org/docs | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | isolated UI states, component/page development, and docs source anchor | volatile project docs |
| `storybook.docs.writing_tests` | How to test UIs with Storybook — Storybook docs | https://storybook.js.org/docs/writing-tests | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | Storybook testing and Vitest-addon integration posture | volatile project docs |
| `storybook.docs.test_runner` | Test runner — Storybook docs | https://storybook.js.org/docs/writing-tests/integrations/test-runner | E0_OFFICIAL_DOCS | anchor checked 2026-06-11 | story execution in browser/CI and test-runner limitations | volatile project docs |

- Chunk 40 adds a bounded coverage-gap audit plus six active ecosystem tool cards. It intentionally creates planned/deferred and alias/companion register rows for important missing ecosystem tools so the tool catalog does not imply exhaustive coverage. Exact pricing, limits, quotas, UI labels, setup mechanics, current feature availability, and policy defaults remain volatile or snapshot-only.


## Chunk 42 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_41` | Editor approval for Chunk 41 / Chunk 42 gate | conversation/editor feedback | internal review | applied | Chunk 42 release-candidate scope/disposition cleanup scope and non-scope | stable for this revision |

- Chunk 42 is repository-contract cleanup only. It adds no new product/vendor facts, pricing facts, model-availability claims, tool cards, field-practice cards, shortcut cards, or narrative chapters.

## Chunk 43 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_42` | Editor approval for Chunk 42 / Chunk 43 gate | conversation/editor feedback | internal review | applied | Chunk 43 release-candidate packaging-only scope and non-scope | stable for this revision |

- Chunk 43 is packaging-only release-candidate artifact creation and verification. It adds no product/vendor facts, pricing claims, model-availability claims, cards, source-map migration, or narrative content.


## Chunk 44 Source Records

| Source ID | Title | URL / Location | Evidence | Verification status | Use for | Volatility |
|---|---|---|---|---|---|---|
| `vcb.register.editor_feedback_chunk_43` | Editor approval for Chunk 43 / Chunk 44 final-release packaging gate | conversation/editor feedback | internal review | applied | Chunk 44 packaging-only final-release scope and non-scope | stable for this revision |

- Chunk 44 is packaging-only final-release artifact creation and verification from the approved RC1 revision 2 package. It adds no product/vendor facts, pricing claims, model-availability claims, cards, source-map migration, or narrative content.

## Notes

- Chunk 15 reuses existing OpenAI Codex source IDs for workflow/prompting topic cards; no new external source IDs were required.
- Exact OpenAI plan limits, credits, and pricing are intentionally not captured in stable chapters. Create dated pricing snapshots when needed.
- OpenAI/Codex surface facts are volatile. Re-check source anchors before writing setup instructions, commands, plan access, model advice, or UI directions.
- Chunk 16 adds/reuses official OpenAI, GitHub, Git, and OWASP source IDs for review, safety, CI, and production-risk workflow cards. Exact feature availability, UI labels, commands, plan packaging, and limits remain volatile and must be checked against official sources.
- Chunk 17 adds/reuses official OpenAI, GitHub, npm, MDN, W3C/WAI, Playwright, and named practitioner source IDs for frontend verification, accessibility, refactoring, dependency review, release notes, and documentation workflows.
- Chunk 18 reuses official OpenAI/Codex, GitHub, npm, MDN, Playwright, Jest, TypeScript, W3C/WAI, and named practitioner/expert source IDs for failure-mode topic cards; no exact pricing, plan, or limit claims are introduced.
- Chunk 19 reuses official OpenAI/Codex best-practice, workflow, feature-maturity, pricing, and Help Center source IDs, the active dated OpenAI/Codex pricing snapshot, the GitHub pull-request review anchor, and VCB synthesis; exact prices, limits, credits, and model-routing details remain snapshot-only.
- Chunk 20 adds the editor-feedback gate source and reuses official OpenAI/Codex, Martin Fowler, and VCB synthesis anchors for eight bounded shortcut harm-reduction cards; it does not start full shortcut-card expansion.
- Chunk 21 adds the editor-feedback gate source and reuses official OpenAI/Codex, GitHub Actions, OWASP, and VCB synthesis anchors for bounded security/permission shortcut harm-reduction cards; exact product behavior, UI labels, permission defaults, and secret-management mechanics remain source-checked volatile details.


- Chunk 22 adds the editor-feedback gate source and reuses official OpenAI/Codex, OWASP, and VCB synthesis anchors for bounded setup/configuration/process shortcut harm-reduction cards; exact product behavior, config keys, hook mechanics, MCP/tool behavior, plugin behavior, UI labels, and permission defaults remain source-checked volatile details.
- Chunk 23 adds the editor-feedback gate source and reuses official OpenAI/Codex skills, MCP, plugins, hooks, best-practices, workflow, configuration, and security anchors plus OWASP anchors where external tool/context risk is discussed; it does not start full tool-card or field-practice expansion.
- Chunk 24 adds/reuses official OpenAI/Codex best-practices, subagents, model, and Help Center truthfulness anchors for bounded multi-AI/model-bias shortcut cards.
- Chunk 25 adds the editor-feedback gate source and reuses official OpenAI/Codex cloud, cloud-environment, automations, worktree, non-interactive, browser, Chrome extension, Computer Use, approvals/security, and best-practices anchors for bounded parallel/cloud/automation shortcut cards.

- Chunk 27 adds the editor-feedback gate source and reuses official OpenAI/Codex app, CLI, IDE, cloud, GitHub review, non-interactive, CLI reference, approvals/security, feature-maturity, pricing, best-practices, and pricing snapshot anchors for bounded first-party primary Codex tool cards. Exact pricing, plan limits, credit values, model availability, context-window numbers, UI labels, commands, and flags remain volatile or snapshot-only.

- Chunk 28 adds the editor-feedback gate source and reuses official OpenAI/Codex worktrees, subagents, automations, Computer Use, in-app browser, Chrome extension, app settings, app features, best-practices, and pricing snapshot anchors for bounded first-party adjunct Codex tool cards. Exact pricing, plan limits, credit values, model availability, context-window numbers, UI mechanics, commands, and flags remain volatile or snapshot-only.

- Chunk 29 adds the editor-feedback gate source and reuses official OpenAI/Codex AGENTS.md, config, skills, MCP, hooks, customization, approvals/security, plugins, and best-practices anchors for bounded first-party customization/control Codex tool cards. Exact config keys, hook event names, command flags, UI labels, model availability, context-window numbers, pricing, plan limits, and credit values remain volatile or snapshot-only.

- Chunk 30 adds the editor-feedback gate source, refreshes official OpenAI/Codex Security anchors, and adds the Codex Security FAQ source for bounded first-party Codex Security tool-card guidance. Exact access, feature maturity, UI labels, setup mechanics, scan behavior, pricing, plan limits, credit values, command/config details, and model availability remain volatile or snapshot-only.

- Chunk 31 adds the editor-feedback gate source and refreshes official OpenAI/Codex Feature Maturity and Codex Changelog anchors for bounded first-party Codex governance/maintenance tool-card guidance. It reuses existing Codex overview and documentation-update workflow anchors without changing their older checked dates. Exact maturity labels, release dates, current feature statuses, UI labels, availability, model availability, pricing, plan limits, credit values, and context-window values remain volatile or snapshot-only.

- Chunk 32 adds the editor-feedback gate source, adds official GitHub repository/workflow/Dependabot, Playwright, and OpenSSF Scorecard anchors, and refreshes reused GitHub, npm, Playwright, and OpenSSF source rows for bounded repository/CI/dependency/QA tool-card guidance. Exact pricing, plan limits, quota limits, command flags, UI labels, permission defaults, vulnerability-scoring details, and setup mechanics remain volatile or snapshot-only.

- Chunk 33 adds the editor-feedback gate source and official OpenAI/ChatGPT, Anthropic/Claude, Cursor, GitHub Copilot, and Windsurf/Devin anchors for bounded AI coding, AI IDE, and AI planning tool-card guidance. Exact pricing, plan limits, quota limits, model availability, UI labels, IDE-extension mechanics, context-window values, feature names, default permissions, and current capability claims remain volatile or snapshot-only.

- Chunk 34 adds the editor-feedback gate source and official Replit, Lovable, Bolt, and v0/Vercel anchors for bounded browser-dev, app-builder, and UI-generation tool-card guidance. Exact pricing, plan limits, quota limits, model availability, UI labels, hosting/runtime limits, app-generation mechanics, deployment mechanics, integration limits, export behavior, and current capability claims remain volatile or snapshot-only.
- Chunk 35 adds the editor-feedback gate source and adds/reuses official Vercel, Supabase, Clerk, Auth0, Stripe, Sentry, and PostHog anchors for bounded hosting, backend/database/auth, payment, observability, and product-analytics tool-card guidance. Exact pricing, plan limits, quota limits, current UI labels, deployment limits, database limits, auth/session defaults, payment fees, observability retention limits, analytics/event-volume limits, SDK setup mechanics, and current feature availability remain volatile or snapshot-only.

- Chunk 36 adds the editor-feedback gate source and official Docker, Figma, and Linear anchors for bounded local dev/container, design/prototyping, and project-management tool-card guidance. Exact pricing, plan limits, seat limits, quota limits, Docker Desktop licensing details, current UI labels, command flags, Compose/build/runtime defaults, container/security defaults, Figma feature availability, export/dev-mode mechanics, Linear workflow/status mechanics, integrations, automation behavior, and current capability claims remain volatile or snapshot-only.

- Chunk 38 adds the editor-feedback gate source and reuses and refreshes selected official OpenAI/Codex and existing vendor anchors as principle support for bounded field-practice candidate cards. The cards remain candidate status; no local reproduction or official endorsement is claimed.

<!-- VCB:STOP_RETRIEVAL reason="source_register_complete" -->
<!-- VCB:END_REGISTER id=vcb.register.sources -->
