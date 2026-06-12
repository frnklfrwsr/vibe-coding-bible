---
id: vcb.protocol.update
title: UPDATE_PROTOCOL
artifact_type: protocol
version: 0.12.0-draft.chunk11
status: chunk_11_updated
created_on: 2026-06-08
last_verified: 2026-06-09
next_review_due: 2026-07-09
review_cadence: monthly
---

<!-- VCB:BEGIN_PROTOCOL id=vcb.protocol.update version=0.12.0-draft.chunk11 -->

# UPDATE_PROTOCOL

## Priority Order

1. Preserve accuracy.
2. Separate official guidance from field practice.
3. Mark obsolete guidance instead of silently deleting it.
4. Update metadata before prose.
5. Add changelog entries for meaningful changes.

## Update Steps

1. Read `manifest.json`.
2. Find topics where `next_review_due <= today`.
3. Prioritize topics with volatile markers: `MODEL_SPECIFIC`, `CODEX_UI_OR_COMMAND`, `COMMUNITY_HACK`, `SPECULATIVE`, or high pricing volatility.
4. Check official OpenAI Codex docs first for Codex behavior.
5. Check Codex changelog and feature-maturity pages for product changes.
6. Check official vendor pricing pages for tool/pricing updates.
7. Compare official guidance against field practice.
8. Keep community tactics labeled unless reproduced locally or corroborated by multiple independent reports.
9. Update frontmatter: `last_verified`, `next_review_due`, `evidence_level`, `source_kind`, `stability`, `obsolete_when`.
10. Update prose and source records.
11. Update indexes, related topics, and registers.
12. Add `CHANGELOG.md` entry.
13. Add deprecated items to `DEPRECATION_REGISTER.md` with replacement IDs.
14. Run `scripts/validate_repository.py`.
15. Stop for editor review.

## Field Practice Promotion Rule

Do not promote anonymous or community field practice directly into stable guidance. Promotion requires at least one of:

- current official OpenAI/vendor support;
- local reproduction with conditions documented;
- named practitioner/expert source plus clear caveat;
- multiple independent community reports, still labeled as anecdotal until tested.

## Shortcut Update Rule

When shortcut guidance changes, update both the prose and `SHORTCUT_REGISTER.md`. Any new shortcut ID must use the canonical `vcb.shortcut.*` namespace and include risk, production risk, recoverability, and minimum guardrail.

## Pricing Rule

Do not hardcode exact current pricing, credits, limits, plan quotas, or feature packaging into stable topic cards. Create a dated pricing snapshot instead.

## Namespace Rule During Updates

Do not create ad hoc topic namespaces. Use the canonical namespace policy in `manifest.json` and `AUTHORING_PROTOCOL.md`.

<!-- VCB:STOP_RETRIEVAL reason="update_protocol_complete" -->
<!-- VCB:END_PROTOCOL id=vcb.protocol.update -->
