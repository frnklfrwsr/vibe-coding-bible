---
id: vcb.final_release_1.integrity
title: FINAL_RELEASE_1_INTEGRITY
artifact_type: final_release_integrity
version: 1.0.0-final.1.chunk44
status: chunk_44_updated
created_on: '2026-06-11'
last_verified: '2026-06-11'
review_cadence: once
---

<!-- VCB:BEGIN_INTEGRITY id=vcb.final_release_1.integrity version=1.0.0-final.1.chunk44 -->

# FINAL_RELEASE_1_INTEGRITY

## Scope

This file is the auditable integrity record for the Final Release 1 package. It records deterministic source-tree integrity data and the external checksum sidecar convention. It distinguishes the source-tree hash, the final zip hash, and any external `.sha256` sidecar. It does not embed the final zip SHA-256, because embedding a zip checksum inside the zip would change the zip being hashed.

## Integrity Record

| Field | Value |
|---|---|
| `final_release_label` | `Final Release 1` |
| `approved_source_baseline` | `vibe-coding-bible-release-candidate-1-revision-2-20260612T040000Z-authoritative.zip` |
| `canonical_package` | `vibe-coding-bible-final-release-1-20260612T050000Z-authoritative.zip` |
| `checksum_sidecar_convention` | `vibe-coding-bible-final-release-1-20260612T050000Z-authoritative.zip.sha256` |
| `source_file_count` | `333` |
| `manifest_source_files_match_actual` | `true` |
| `tree_txt_matches_actual` | `true` |
| `manifest_inventory_sha256` | `f60357a9381e09cd8292e68260f346068fb3f559530c201e02594a53d28e64a4` |
| `source_content_manifest_sha256_excluding_this_file` | `445869cfcf787dd2cbab04e2d55ab912d1253ae436f667d010fcfc66d65092ae` |
| `validator_output` | `VCB validation passed; active chapter/topic files validated: 236; shortcut IDs registered: 98; tool IDs registered: 75; pricing snapshots active: 1` |

## Deterministic Hash Inputs

- `manifest_inventory_sha256` is SHA-256 over the UTF-8 string formed by joining the sorted package-relative source-file paths with `\n` and appending a final `\n`.
- `source_content_manifest_sha256_excluding_this_file` is SHA-256 over the UTF-8 string formed by iterating package-relative source-file paths in ascending lexicographic order, excluding `FINAL_RELEASE_1_INTEGRITY.md`; for each remaining path, append `<file_sha256>  <package_relative_path>` where `<file_sha256>` is SHA-256 of that file's bytes; join those lines with `\n` and append a final `\n`.
- The final package SHA-256 is external to the source tree; verify it against the author submission checksum and, when supplied, the sidecar convention `vibe-coding-bible-final-release-1-20260612T050000Z-authoritative.zip.sha256`.

## Verification Commands

```bash
python scripts/validate_repository.py
sha256sum vibe-coding-bible-final-release-1-20260612T050000Z-authoritative.zip
# If the external sidecar is supplied beside the zip:
cat vibe-coding-bible-final-release-1-20260612T050000Z-authoritative.zip.sha256
```

<!-- VCB:STOP_RETRIEVAL reason="final_release_integrity_record_complete" -->
<!-- VCB:END_INTEGRITY id=vcb.final_release_1.integrity -->
