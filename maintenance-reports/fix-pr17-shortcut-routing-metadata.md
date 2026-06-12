# Fix PR #17 Shortcut Routing and Metadata

Primary PR: https://github.com/frnklfrwsr/vibe-coding-bible/pull/17

Date: 2026-06-12

Branch: `fix-pr17-shortcut-routing-metadata`

## Objective

Address unresolved Codex Review feedback from PR #17 and verify related PR #1 and PR #13 feedback against current `main`, without changing substantive VCB card or chapter content.

## Codex Review Feedback Audit

| Source PR | Comment topic | Current status | Action |
|---|---|---|---|
| PR #1 | Update stale package inventory counts | still_relevant_fix_in_this_pr | Preserve Final Release 1 package counts as historical and add live repository inventory metadata. |
| PR #1 | Regenerate the inventory support file | still_relevant_fix_in_this_pr | Regenerate `TREE.txt` from the live repository inventory and validate it against actual files. |
| PR #13 | Fix `mkdocs.yml` `edit_uri` to include `docs/` | already_fixed_in_current_main | Verified `edit_uri: edit/main/docs/`. No action in this PR. |
| PR #13 | Keep package inventory counters consistent | already_fixed_then_overlapped_by_current_metadata_split | Current source inventory is live; this PR separates it from the historical final-release package record. |
| PR #13 | Scope Pages write/OIDC permissions to deploy job | already_fixed_in_current_main | Verified workflow-level permissions are read-only and deploy job owns Pages/OIDC write permissions. |
| PR #17 | Add promoted shortcuts to root README routing | still_relevant_fix_in_this_pr | Add a concise post-release shortcut-audit route section for the eight promoted cards. |
| PR #17 | Regenerate `TREE.txt` with the new files | still_relevant_fix_in_this_pr | Regenerate `TREE.txt` with governance, docs, maintenance, and Issue #3 shortcut files. |
| PR #17 | Route all promoted cards in `INDEX_FOR_AI_COACHES.md` | still_relevant_fix_in_this_pr | Add direct AI-coach routes for the six missing promoted cards; keep the two existing routes. |
| PR #17 | Update all historical shortcut-count checks | still_relevant_fix_in_this_pr | Replace raw 50/48 shortcut expectations with a named historical register snapshot and validate live counts separately. |
| PR #17 | Keep final-release package counts historical | still_relevant_fix_in_this_pr | Keep `manifest.package` tied to the Final Release 1 zip and move current counts to live repository inventory metadata. |

## Files Changed

- `README.md`
- `TREE.txt`
- `indexes/INDEX_FOR_AI_COACHES.md`
- `manifest.json`
- `scripts/validate_repository.py`
- `maintenance-reports/fix-pr17-shortcut-routing-metadata.md`

## Validation

- Baseline validation on synced `main`: `VCB validation passed`.
- Final validation on this branch: `VCB validation passed`; active chapter/topic files validated: 244; shortcut IDs registered: 98; tool IDs registered: 75; pricing snapshots active: 1.

## Codex Review Status

PR #18 first automated Codex Review left one actionable comment on the Chunk 41 validator count check. The branch now removes the live-register-to-historical-snapshot comparison for Chunk 41 while preserving live register validation and historical package snapshots separately. Follow-up Codex Review is pending after the fix commit.

## Follow-Up

No new follow-up issue is required for the reviewed PR #1, PR #13, or PR #17 comments after this branch, unless Codex Review on the new PR identifies a fresh actionable issue.
