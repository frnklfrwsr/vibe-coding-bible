---
id: vcb.maintenance.issue_26_lightweight_contribution_and_integration_modes
title: Issue #26 Lightweight Contribution and Integration Modes
artifact_type: maintenance_report
date: 2026-06-13
branch: issue-26-lightweight-contribution-and-integration-modes
status: complete
---

# Issue #26 Lightweight Contribution and Integration Modes

Issue: https://github.com/frnklfrwsr/vibe-coding-bible/issues/26

Branch: `issue-26-lightweight-contribution-and-integration-modes`

## Objective

Resolve Issue #26 by documenting lightweight post-release contribution handling, VCB Parliamentarian / Constitutionalist checkpoints, ChatGPT web usage, and bounded subagent delegation without adding new VCB topic/card/chapter substance.

## Files created or updated

Created:

- `POST_RELEASE_CONTRIBUTION_WORKFLOW.md`
- `docs/vcb-parliamentarian.md`
- `docs/use-with-chatgpt-web.md`
- `SUBAGENT_DELEGATION_POLICY.md`
- `maintenance-reports/issue-26-lightweight-contribution-and-integration-modes.md`

Updated:

- `README.md`
- `AI_START_HERE.md`
- `USE_VCB_WITH_AI.md`
- `CONTRIBUTION_MODES.md`
- `llms.txt`
- `llms-full.txt`
- `docs/use-with-codex.md`
- `docs/use-with-ai.md`
- `docs/index.md`
- `mkdocs.yml`
- `manifest.json`
- `TREE.txt`

No new field-practice cards, shortcut cards, tool cards, pricing snapshots, release tags, or narrative chapter rewrites were added.

## Subagents used

- `vcb_route_auditor`: checked AI entryways, LLM maps, README, and docs routing for smallest-route preservation.
- `vcb_governance_auditor`: checked contribution workflow boundaries against the PR #25 / Issue #23 overhead pattern and candidate-card thresholds.
- `vcb_web_user_auditor`: dry-ran the ChatGPT web route as a public-GitHub, draft-only user flow.
- `vcb_parliamentarian_auditor`: reviewed advisory versus gatekeeping boundaries and custom-agent convention risk.

All subagents were read-only and did not edit files.

## Lightweight contribution workflow summary

The workflow defines four intake levels: issue/comment only, maintenance report only, candidate card, and full chunk-style metadata. Candidate cards require sanitized public-safe input, a reusable non-duplicative pattern, explicit evidence level, supported claims, clear route surfaces, and a maintainer decision that active retrieval is useful. The PR #25 pattern is documented as useful but too heavy as a default.

## Parliamentarian design summary

The Parliamentarian mode is a read-only checkpoint reviewer. It is advisory by default and gatekeeping only for sensitive transitions such as first mutation, dependency/tool adoption, PR creation, merge, deploy, release, production state, secrets, auth, payments, or CI credentials. This PR intentionally does not add `.codex/agents/vcb-parliamentarian.toml` because local inspection did not find a clear current project custom-agent convention for `.codex/agents/*.toml`.

## ChatGPT web mode summary

The ChatGPT web page gives a public-repo prompt, reinforces smallest-route retrieval from `AI_START_HERE.md`, and states that the default contribution mode is suggest/draft. Web agents that cannot write to GitHub should draft issue, comment, or PR text for user review rather than posting automatically.

## Subagent delegation policy summary

The policy limits subagents to bounded independent work, defaults to 1-3 agents, caps fanout at 4 unless explicitly requested, prefers the lowest capable available model for mechanical checks, and keeps final judgment with the parent agent.

## Validator result

Passed on 2026-06-13:

```text
VCB validation passed
active chapter/topic files validated: 245
shortcut IDs registered: 98
tool IDs registered: 75
pricing snapshots active: 2
```

## Docs build result

Initial docs build attempt failed because `mkdocs` was not on the default Python module path. No dependency was installed into the repo. Rerunning with the existing isolated dependency path passed on 2026-06-13:

```powershell
$env:PYTHONPATH='C:\Users\toto2\Documents\Codex\2026-06-11\VCB-Project-Files\.test-tmp\validate_pydeps'
python -m mkdocs build --strict --site-dir '..\.test-tmp\vcb-docs-site'
```

## Follow-up work

- If official Codex project custom-agent conventions become clear, consider adding a read-only Parliamentarian config in a separate PR.
- If repeated usage insights still create heavy metadata churn, convert this workflow into an issue-template checklist or maintainer triage checklist.

<!-- VCB:STOP_RETRIEVAL reason="issue_26_maintenance_report_complete" -->
