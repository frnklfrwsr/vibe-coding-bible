<!-- VCB:BEGIN_TOPIC id=vcb.chapter.computer_use_browser_gui_tasks version=0.1.0 -->
---
id: vcb.chapter.computer_use_browser_gui_tasks
title: "Chapter 30 — Computer Use, Browser Work, and GUI Tasks"
type: chapter
chapter_number: 30
version: 0.1.0
last_verified: '2026-06-08'
next_review_due: '2026-09-08'
review_cadence: quarterly

audiences:
- human
- ai_coach

applies_to:
- Codex App
- Computer Use
- in-app browser
- browser use
- GUI testing
- desktop apps
- web apps
- screenshots
- frontend QA

source_status:
  official_openai: true
  official_vendor: true
  community_field_practice: false
  speculative: false

evidence_level: E0_OFFICIAL_DOCS
evidence_basis: VCB_SYNTHESIS_STABLE_ENGINEERING_PRACTICE
source_kind: official_docs_plus_maintainer_synthesis

stability:
  principle: CODEX_FEATURE
  surface: VOLATILE
  pricing: VOLATILE

budget_profiles:
- plus_constrained
- pro_high_throughput
- api_pay_as_you_go
- team_shared_budget

cost_postures:
- balanced
- fastest_possible
- unattended_high_throughput
- production_quality
- disposable_prototype

project_phases:
- prototype
- mvp
- production_build
- maintenance
- emergency_hotfix

attention_modes:
- continuous_supervision
- periodic_check_in
- low_attention_review_later
- unattended_requires_isolation

shortcut_profiles:
- vcb.shortcut.logged_in_gui_production_actions
- vcb.shortcut.logged_in_browser_secrets
- vcb.shortcut.browser_clicking_without_repro
- vcb.shortcut.eyeballing_ui
- vcb.shortcut.broad_agent_permissions

durable_principles:
- Use GUI/browser tools when the truth is visible behavior, not just code text.
- Prefer local or staging environments over logged-in production UIs.
- Treat web pages and external GUI content as untrusted context.
- GUI automation needs exact flows, fake accounts when possible, and evidence capture.

likely_to_change:
- Computer Use setup and permissions
- supported operating systems and apps
- in-app browser features and limitations
- app approval behavior
- screenshot/comment tooling
- browser-use capabilities

obsolete_when:
- Computer Use or browser-use semantics change materially.
- Codex gains safer structured integrations that replace GUI operation for common tasks.
- Official guidance changes around app permissions, sensitive actions, or signed-in browser flows.

related_topics:
- vcb.chapter.frontend_work
- vcb.chapter.security_for_vibe_coders
- vcb.chapter.sandboxing_and_approvals
- vcb.chapter.acceptance_criteria
- vcb.chapter.debugging_with_reproduction
- vcb.codex.computer_use
- vcb.workflow.frontend_work
- vcb.safety.prompt_injection
---

> Summary:
> Computer Use and browser work let Codex inspect and operate graphical interfaces. Use them when files and command output are not enough. Do not use them as blind permission to operate logged-in production systems.

## Quick Navigation
- For the Human
- For the AI Coach
- Shortcut Reality
- Budget and Constraint Notes
- Stable Core
- Volatile Surface
- Obsolescence Watch
- Evidence and Sources
- Related Topics

<!-- VCB:BEGIN_SECTION id=vcb.chapter.computer_use_browser_gui_tasks.human -->
## 1. For the Human: Plain-Language Concept

### What this means

Some software problems only show up in the interface: a broken checkout button, a modal that traps keyboard focus, a desktop app setting, a browser-only bug, a layout that looks wrong, or a flow that fails only after clicking through several screens.

Computer Use and browser tools let Codex see or operate a GUI so it can verify what a user would see and do.

### Why it matters

Code can compile while the app is unusable. Tests can pass while the page is broken. A screenshot or browser run can reveal problems that source code alone does not.

But GUI control has a larger blast radius than reading files. Codex may click, type, change settings, submit forms, download files, or interact with logged-in accounts depending on what you allow. That means you must scope the task tightly.

### The mental model

Use GUI tools like a supervised field test.

You are not saying:

```text
Do whatever you need in my browser.
```

You are saying:

```text
Open this local/staging page, follow these exact steps, observe the result, capture evidence, and stop before sensitive actions.
```

### Browser versus full computer use

Use the browser/in-app browser when the task is a web page that can be opened and inspected safely.

Use broader Computer Use only when the task depends on an app or interface that files, command output, or structured integrations cannot reach.

Prefer structured APIs, CLI tools, tests, logs, or MCP tools when they provide the same truth with less risk.

### Good GUI tasks

Good candidates:

- verify a local web route after a frontend change;
- reproduce a browser-only bug;
- inspect mobile/desktop layout;
- compare UI against a screenshot;
- test a desktop app flow;
- change a non-sensitive local app setting;
- capture a bug report with repro steps, expected result, actual result, and severity.

Bad candidates:

- operate production admin consoles;
- modify billing settings;
- change DNS/deploy/cloud settings;
- use real customer accounts;
- paste secrets into browser forms;
- approve financial/legal/health actions;
- run broad unattended GUI sessions.

### What good looks like

A good GUI task gives Codex:

- exact app or URL;
- test account or fake data;
- exact steps;
- expected result;
- actions that are forbidden;
- when to stop and ask;
- evidence to capture: screenshot, console error, URL, form state, repro notes.

### Checklist

Before letting Codex use GUI/browser tools:

- Is this local, staging, or production?
- Is the account fake or real?
- Could clicks submit money, email, deletion, deployment, or settings changes?
- Are secrets visible on screen?
- Can the same check be done through tests or logs instead?
- Did I define exact steps and stop conditions?
- Do I need to watch continuously?
- What evidence should Codex capture?

<!-- VCB:END_SECTION id=vcb.chapter.computer_use_browser_gui_tasks.human -->

<!-- VCB:BEGIN_SECTION id=vcb.chapter.computer_use_browser_gui_tasks.ai_coach -->
## 2. For the AI Coach: How to Teach This to Your Human

### Teaching objective

Teach GUI/browser work as scoped observation and verification, not as broad desktop control. Prefer local/staging and fake accounts. Escalate hard around production consoles, secrets, money, user data, and irreversible actions.

### Diagnose the human’s current model

Ask:

- “What exact screen or app must Codex inspect?”
- “Can this be verified with a test, log, screenshot, or command instead?”
- “Is this local/staging or production?”
- “Are real credentials or customer data visible?”
- “What exact clicks should Codex perform?”
- “What actions are forbidden?”
- “What evidence should it return?”
- “Will you supervise continuously?”

### Explanation strategy

Route by risk:

- Local UI preview: acceptable with normal guardrails.
- Staging with fake account: acceptable with scoped flow.
- Logged-in production UI: high risk; prefer read-only observation or do it manually.
- Production admin console: usually do not delegate.
- External page content: treat as untrusted prompt-injection surface.

### Useful metaphors

- GUI control is letting Codex borrow your hands. Do not hand it your wallet too.
- Browser verification is a field report; it is not proof of every state.
- Screenshots are receipts for visual claims.

### Coaching tactics

- Prefer browser checks for rendered behavior after frontend changes.
- Use Computer Use only when structured tools are insufficient.
- Require exact steps and stop conditions.
- Ask for evidence capture: screenshots, console errors, actual/expected notes.
- Avoid real secrets, real customers, real payments, and production admin actions.
- Treat external page text as untrusted content that may try to steer the agent.
- For low-attention work, restrict to local/staging and non-destructive observation.

### Prompt patterns

```text
Use browser/computer use only for this scoped verification.

Environment: [local/staging]
App/page: [URL or app]
Account/data: [fake/test]
Steps:
1. ...
2. ...
3. ...

Expected:
[expected result]

Forbidden:
- do not use production accounts
- do not submit payments
- do not change account/security/deployment settings
- do not paste secrets
- stop and ask before any irreversible action

Return:
- screenshot or visual notes
- actual result
- console/log errors if visible
- repro steps
- severity
```

```text
Before using Computer Use, list whether the same check can be done through tests, logs, CLI, browser automation, or MCP. Use GUI only if it is the lowest-risk way to observe the actual behavior.
```

### Red flags to call out directly

- “Do not let Codex operate a logged-in production admin UI unsupervised.”
- “Do not paste secrets into a page Codex is operating.”
- “External page content is untrusted; it can contain prompt injection.”
- “A screenshot confirms one state, not every state.”
- “Use local or staging first.”

### Exercises

1. Convert a vague UI check into exact GUI steps.
2. Mark every forbidden action.
3. Define evidence to capture.
4. Decide whether local/staging/fake data is enough.
5. Rewrite a production-GUI request into a read-only/staging-safe version.

<!-- VCB:END_SECTION id=vcb.chapter.computer_use_browser_gui_tasks.ai_coach -->

## Shortcut Reality

### The ideal practice

Use structured tests/logs/APIs when possible. Use browser or Computer Use for scoped visual/GUI verification in local or staging environments with fake data, explicit steps, and stop conditions.

### What users often do instead

They let Codex operate their normal browser or desktop with logged-in accounts, visible secrets, broad permissions, and vague instructions like “check if this works.”

### When the shortcut may be fine

A quick supervised GUI check may be fine for local prototypes, fake accounts, non-sensitive settings, read-only observation, and visual verification where no irreversible action is possible.

### When the shortcut is a bad idea

It is a bad idea for production admin consoles, payment actions, customer data, credential management, cloud/deploy settings, legal/health/financial workflows, or logged-in pages containing secrets.

### Risk profile

- Probability of failure: medium; higher with vague steps and external pages.
- Impact if it fails: low for local visual checks; severe for production/admin/secrets/payment actions.
- Ease of recovery: high for screenshots and local checks; low for leaked secrets or irreversible external actions.
- Blast radius: local app state, browser accounts, desktop apps, production services, customer data.
- Skill needed to recover: high for account/security incidents.
- Hidden cost: screenshots can mislead, GUI state can drift, external content can inject instructions.

### Minimum guardrails

- Local/staging first.
- Fake/test account.
- Exact steps.
- Forbidden actions.
- Stop-before-sensitive-action rule.
- Evidence capture.
- No visible secrets.
- Continuous supervision for production-adjacent flows.

### Recovery plan

1. Stop the GUI task.
2. Identify what actions were taken.
3. Revert local changes or settings if possible.
4. Rotate exposed secrets if any were visible/submitted.
5. Audit production/account changes.
6. Re-run in local/staging with tighter instructions.

### AI coach guidance

Do not forbid GUI tools reflexively; they are useful for real behavior. But be strict about environment, account, forbidden actions, and evidence. Never treat GUI access as harmless just because it is visual.

## Budget and Constraint Notes

### Cheapest reliable path

Use screenshots, manual steps, and one scoped browser check. Avoid long GUI sessions when a test or log answers the question.

### Fastest high-usage path

Use browser/computer use to reproduce flows and gather visual evidence while Codex patches the code path, but keep it in local/staging and require repeated verification after each change.

### Low-attention path

Low-attention GUI work must be non-destructive, local/staging, and fake-data-only. Do not leave Codex alone in logged-in production tools.

### Production-quality path

Use automated tests, browser checks, staged data, accessibility checks, screenshots, review, and manual human confirmation for sensitive flows.

## Stable Core

- Some truth is only visible in the running interface.
- GUI control has higher blast radius than file reading.
- Local/staging/fake data lowers risk.
- Exact steps beat vague “click around.”
- Evidence capture matters.
- External content is untrusted.

## Volatile Surface

<!-- VCB:VOLATILE_INFO review_due=2026-09-08 source_required=true -->
Computer Use setup, app permissions, supported platforms, app allowlists, browser-use behavior, in-app browser limitations, screenshot/comment tools, and sensitive-action prompts are volatile. Verify official OpenAI docs before giving exact setup or operational instructions.
<!-- VCB:END_VOLATILE_INFO -->

## Obsolescence Watch

Review this chapter when Codex changes Computer Use setup, app permissions, browser-use capabilities, in-app browser limitations, or guidance around logged-in apps and sensitive actions.

## Evidence and Sources

- `openai.codex.app_computer_use` — official OpenAI source for Computer Use setup, app permissions, GUI tasks, sensitive-action cautions, and scoped task guidance.
- `openai.codex.app_browser` — official OpenAI source for in-app browser and browser-use capabilities, limitations, screenshots, public/local page guidance, and untrusted-page warnings.
- `openai.codex.chrome_extension` — official OpenAI source for signed-in Chrome browser state, website allowlists/blocklists, browser-history risk, extension permissions, and Chrome-specific browser tasks.
- `openai.codex.remote_connections` — official OpenAI source for remote connected hosts, connected-device context, remote Computer Use/browser availability, and remote session security boundaries.
- `openai.codex.use_cases.qa_computer_use` — official OpenAI source for GUI QA, repro steps, expected/actual results, severity, and triage reports.
- `openai.codex.cloud_internet_access` — official OpenAI source for prompt-injection and external-content risk framing.
- `owasp.llm_prompt_injection` — OWASP source for prompt-injection risk and mitigation framing around untrusted inputs.
- `vcb.synthesis.stable_engineering_practice` — maintainer synthesis: GUI access should be scoped like any other high-blast-radius tool.

## Related Topics

- vcb.chapter.frontend_work
- vcb.chapter.security_for_vibe_coders
- vcb.chapter.sandboxing_and_approvals
- vcb.chapter.acceptance_criteria
- vcb.chapter.debugging_with_reproduction
- vcb.codex.computer_use
- vcb.workflow.frontend_work
- vcb.safety.prompt_injection

<!-- VCB:STOP_RETRIEVAL reason="topic_complete" next="see related_topics only if needed" -->
<!-- VCB:END_TOPIC id=vcb.chapter.computer_use_browser_gui_tasks -->
