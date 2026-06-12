# Issue #6 Fresh-LLM Retrieval Smoke Test

## Scope

Issue URL: https://github.com/frnklfrwsr/vibe-coding-bible/issues/6

Date: 2026-06-12

Branch: `issue-6-fresh-llm-retrieval-smoke-test`

This smoke test checks whether a fresh AI/LLM coach can use the public VCB repository routing surfaces to retrieve the right context without reading the entire corpus. This is a retrieval-quality test only. It does not expand VCB content, add cards, change field-practice status, update pricing, start watchers, touch release tags, or create a release.

## Method

I acted as a fresh AI coach starting from public entrypoints and route surfaces: `README.md`, `llms.txt`, `llms-full.txt`, and targeted indexes. For each question, I followed the smallest route that pointed to active cards or active index entries, retrieved only the final relevant card(s), and stopped at `VCB:STOP_RETRIEVAL` unless the question required a companion route to answer safely.

The test intentionally avoided reading the entire topic/chapter corpus. Targeted searches were used only to confirm candidate route names and to avoid missing an existing active route. Each final answer path was evaluated for:

- smallest useful context;
- `VCB:STOP_RETRIEVAL` behavior;
- unrelated context mixing;
- clarity for a human reader and usefulness for an AI coach;
- pass/fail outcome and exact route defect if any.

## Test Matrix

| # | Test question | Starting route | Final retrieved files | STOP_RETRIEVAL respected? | Result | Notes |
|---|---|---|---|---|---|---|
| 1 | I want to skip tests on a prototype. Is that okay? | `llms.txt` -> shortcut harm-reduction route for skipping tests -> `vcb.shortcut.skipping_tests` | `topics/shortcuts/skipping-tests.md` | Yes: stopped at `skipping_tests_shortcut_complete`. | PASS | Smallest useful context: yes. Unrelated context mixed in: no. The card directly answers that prototype shortcuts can be rational only when isolated/disposable and still need the smallest meaningful guardrail plus an explicit not-verified note. |
| 2 | Codex added a dependency I did not ask for. What should I do? | `llms.txt` failure-mode/dependency route plus `indexes/INDEX_BY_TASK.md` "Choose dependencies, packages, or frameworks" -> `vcb.failure.dependency_bloat` | `topics/failure-modes/dependency-bloat.md` | Yes: stopped at `topic_complete`. | PASS | Smallest useful context: yes. Unrelated context mixed in: no. The card gives the correct recovery path: freeze further use, inspect package/lockfile diff, compare built-in/existing/new dependency options, check security/update risk, and plan rollback. |
| 3 | I am on a constrained plan. How should I use Codex cheaply? | `indexes/INDEX_FOR_AI_COACHES.md` "Human is budget-constrained" -> `vcb.constraints.scope_budget` and `vcb.constraints.usage_burn` | `topics/constraints/scope-budget.md`; `topics/constraints/usage-burn.md` | Yes: stopped at `constraint_topic_complete` in both cards. | PASS | Smallest useful context: yes. Unrelated context mixed in: no. The pair is needed: `scope_budget` explains one-slice task shaping, while `usage_burn` explains context, retry, parallelism, and pricing-snapshot posture without freezing exact plan limits. |
| 4 | I want to use ChatGPT as PM and Codex as implementer. Where is that covered? | `llms.txt` Field Practice Candidate Fast Routing -> PM/planning model plus Codex implementation split -> `vcb.field.chatgpt_pm_codex_implementer` | `topics/field-practices/chatgpt-pm-codex-implementer.md` | Yes: stopped at `field_practice_card_complete`. | PASS | Smallest useful context: yes. Unrelated context mixed in: no. The route preserves candidate status and `E4_COMMUNITY_FIELD_REPORT`, so the answer remains useful without promoting the practice as official guidance. |
| 5 | How should an AI coach decide when to stop retrieving more context? | `README.md` Retrieval Rules -> `llms.txt` Retrieval Rule -> `vcb.prompting.context_management` for coach context-selection guidance | `README.md`; `llms.txt`; `topics/prompting/context-management.md` | Yes: stopped at `repository_root_complete`, `llms_routing_complete`, and `topic_complete`. | PASS | Smallest useful context: yes. Unrelated context mixed in: no. The route answers: use indexes to find the smallest useful file, stop at `VCB:STOP_RETRIEVAL`, and only broaden when the task explicitly needs related topics or missing context would change the plan. |
| 6 | Codex says the task is done, but I do not trust it. Where should I look? | `llms.txt` failure-mode route plus `indexes/INDEX_BY_TASK.md` "Review Codex output or a PR" -> `vcb.failure.done_claim_without_evidence` | `topics/failure-modes/done-claim-without-evidence.md` | Yes: stopped at `failure_mode_card_complete`. | PASS | Smallest useful context: yes. Unrelated context mixed in: no. The card directly covers unsupported completion summaries and gives the completion-evidence table an AI coach should ask for. |
| 7 | I want to use a new external tool with Codex. What risk checks apply? | `llms.txt` MCP/external-tool route and setup/process shortcut route -> `tool.codex_mcp` plus `vcb.shortcut.unofficial_tools` | `topics/tool-catalog/codex-mcp.md`; `topics/shortcuts/unofficial-tools.md` | Yes: stopped at `tool_card_complete` and `unofficial_tools_shortcut_complete`. | PASS | Smallest useful context: yes. Unrelated context mixed in: no. The tool card covers the Codex MCP trust boundary; the shortcut card supplies the adoption checklist for source, owner, scopes, credentials, disposable/read-only testing, and uninstall path. |

## Findings

All seven smoke-test questions passed. The public routing surfaces consistently led to active topic, tool, shortcut, constraint, or field-practice cards without requiring full-corpus ingestion.

`VCB:STOP_RETRIEVAL` behavior was usable and clear. Each final card or route surface provided a stop marker. Related-topic lists were helpful as optional companions, but none of the seven tests required broad chapter fallback or unrelated context.

The strongest retrieval paths were `llms.txt` for direct LLM routing, `indexes/INDEX_FOR_AI_COACHES.md` for coach-intent routing, and `indexes/INDEX_BY_TASK.md` for task confirmation. `README.md` remained useful as the public root because it states the retrieval rules and points to the right entrypoints.

## Routing Defects

None found.

No stale route, missing active route, planned/deferred-as-active route, or route pointing away from the most relevant active topic card was found during this smoke test.

## Follow-Up Issues Needed

None.

No routing defects were found, so no follow-up GitHub issues are needed or proposed from this PR.

## Files Changed

This maintenance report was added:

- `maintenance-reports/issue-6-fresh-llm-retrieval-smoke-test.md`

The repository source inventory was updated because the validator requires every source file to be represented in `manifest.json`:

- `manifest.json`

No route, index, `llms.txt`, `llms-full.txt`, topic, chapter, shortcut, tool, pricing, field-practice, tag, or release file was changed as part of the retrieval test.

## Validation

Baseline validation passed on synced `main` before report creation using temporary validator dependencies installed outside the repo source tree at:

`C:\Users\toto2\Documents\Codex\2026-06-11\VCB-Project-Files\.test-tmp\validate_pydeps`

Baseline command:

```powershell
$env:PYTHONPATH = "C:\Users\toto2\Documents\Codex\2026-06-11\VCB-Project-Files\.test-tmp\validate_pydeps"
python scripts/validate_repository.py
```

Baseline result:

```text
VCB validation passed
active chapter/topic files validated: 236
shortcut IDs registered: 98
tool IDs registered: 75
pricing snapshots active: 1
```

Post-report validation passed after adding the maintenance report and updating manifest/source-inventory metadata:

```text
VCB validation passed
active chapter/topic files validated: 236
shortcut IDs registered: 98
tool IDs registered: 75
pricing snapshots active: 1
```

## Conclusion

Issue #6 retrieval smoke testing passed for all seven questions. The public VCB repository can route a fresh AI coach to the right small context without reading the entire corpus. No concrete routing defect was found, no route fix was made, and no substantive VCB content was changed.
