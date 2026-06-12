---
id: vcb.release_candidate_1.integrity
title: RELEASE_CANDIDATE_1_INTEGRITY
artifact_type: release_candidate_integrity
version: 1.0.0-rc.1.chunk43.revision2
status: chunk_43_updated
created_on: '2026-06-11'
last_verified: '2026-06-11'
review_cadence: once
---

<!-- VCB:BEGIN_INTEGRITY id=vcb.release_candidate_1.integrity version=1.0.0-rc.1.chunk43.revision2 -->

# RELEASE_CANDIDATE_1_INTEGRITY

## Scope

This file is the auditable integrity record for the Release Candidate 1 revision package. It records deterministic source-tree integrity data and the external checksum sidecar convention. It distinguishes the source-tree hash, the final zip hash, and any external `.sha256` sidecar. It does not embed the final zip SHA-256, because embedding a zip checksum inside the zip would change the zip being hashed.

## Integrity Record

| Field | Value |
|---|---|
| `release_candidate_label` | `Release Candidate 1` |
| `revision` | `revision_2` |
| `canonical_package` | `vibe-coding-bible-release-candidate-1-revision-2-20260612T040000Z-authoritative.zip` |
| `checksum_sidecar_convention` | `vibe-coding-bible-release-candidate-1-revision-2-20260612T040000Z-authoritative.zip.sha256` |
| `source_file_count` | `331` |
| `manifest_source_files_match_actual` | `true` |
| `tree_txt_matches_actual` | `true` |
| `manifest_inventory_sha256` | `e763c932507d38cc6929cee721b624f61eb5fbbfb2c946d95dc2b6abfe5ebd66` |
| `source_content_manifest_sha256_excluding_this_file` | `8df569687ed2ecb039025772bc115975a9c60e240cc87c7f1c97b52473af88f1` |
| `validator_output` | `VCB validation passed; active chapter/topic files validated: 236; shortcut IDs registered: 98; tool IDs registered: 75; pricing snapshots active: 1` |

## Deterministic Hash Inputs

- `manifest_inventory_sha256` is SHA-256 over the UTF-8 string formed by joining the sorted package-relative source-file paths with `\n` and appending a final `\n`.
- `source_content_manifest_sha256_excluding_this_file` is SHA-256 over the UTF-8 string formed by iterating package-relative source-file paths in ascending lexicographic order, excluding `RELEASE_CANDIDATE_1_INTEGRITY.md`; for each remaining path, append `<file_sha256>  <package_relative_path>` where `<file_sha256>` is SHA-256 of that file's bytes; join those lines with `\n` and append a final `\n`.
- The final package SHA-256 is external to the source tree; verify it against the author submission checksum and, when supplied, the sidecar convention `vibe-coding-bible-release-candidate-1-revision-2-20260612T040000Z-authoritative.zip.sha256`.

## Verification Commands

```bash
python scripts/validate_repository.py
sha256sum vibe-coding-bible-release-candidate-1-revision-2-20260612T040000Z-authoritative.zip
# If the external sidecar is supplied beside the zip:
cat vibe-coding-bible-release-candidate-1-revision-2-20260612T040000Z-authoritative.zip.sha256
```

<!-- VCB:STOP_RETRIEVAL reason="release_candidate_integrity_record_complete" -->
<!-- VCB:END_INTEGRITY id=vcb.release_candidate_1.integrity -->
