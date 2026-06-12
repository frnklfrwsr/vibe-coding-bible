---
id: vcb.register.pricing_snapshots
title: PRICING_SNAPSHOT_REGISTER
artifact_type: register
version: 0.43.0-draft.chunk42
status: chunk_42_updated
created_on: 2026-06-08
last_verified: '2026-06-11'
next_review_due: '2026-07-11'
review_cadence: monthly
---

<!-- VCB:BEGIN_REGISTER id=vcb.register.pricing_snapshots version=0.43.0-draft.chunk42 -->

# PRICING_SNAPSHOT_REGISTER

**Purpose:** Track dated pricing snapshots. Exact prices, credits, limits, quotas, and plan packaging are not stable guidance.

## Current Snapshot Status

Chunk 12 captured the first exact OpenAI/Codex pricing snapshot. All other vendor pricing remains deferred until dedicated tool-card or pricing-snapshot work.

## Snapshot Files

| Snapshot ID | Snapshot file | Scope | Last checked | Next review | Status |
|---|---|---|---|---|---|
| `vcb.pricing_snapshot.openai_codex` | `pricing-snapshots/2026-06-09-openai-codex.md` | OpenAI / Codex plan, credit, and usage details | 2026-06-09 | 2026-07-09 | active_snapshot |
| `vcb.pricing_snapshot.ai_coding_tools` | `pricing-snapshots/2026-06-08-ai-coding-tools.md` | AI coding tools | not captured | TBD | deferred |
| `vcb.pricing_snapshot.hosting` | `pricing-snapshots/2026-06-08-hosting.md` | hosting/deployment tools | not captured | TBD | deferred |
| `vcb.pricing_snapshot.databases` | `pricing-snapshots/2026-06-08-databases.md` | database/backend tools | not captured | TBD | deferred |
| `vcb.pricing_snapshot.observability` | `pricing-snapshots/2026-06-08-observability.md` | observability/analytics tools | not captured | TBD | deferred |

## Snapshot Rules

- Store exact values only with retrieval date.
- Link official vendor page first.
- State what was not verified.
- Include next review date.
- Keep stable topic cards free of volatile exact pricing.
- Treat exact values in snapshots as stale after their review date.


## Chunk 42 Release-Candidate Disposition Note

Chunk 42 does not add pricing snapshots. It confirms the release-candidate disposition: `vcb.pricing_snapshot.openai_codex` remains the only active exact pricing snapshot, and non-OpenAI pricing categories remain deferred documented limitations. Stable prose must continue avoiding exact cross-vendor prices, quotas, credits, plan limits, and package claims unless a future editor-approved pricing-snapshot slice captures them.

## Chunk 41 Finalization Readiness Audit Note

Chunk 41 does not add pricing snapshots. Finalization audit state: 1 active pricing snapshot (`vcb.pricing_snapshot.openai_codex`) and 4 deferred pricing categories (`vcb.pricing_snapshot.ai_coding_tools`, `vcb.pricing_snapshot.hosting`, `vcb.pricing_snapshot.databases`, and `vcb.pricing_snapshot.observability`). Exact cross-vendor cost guidance is not release-ready until scoped pricing snapshots are captured or the release explicitly excludes exact pricing coverage.

<!-- VCB:STOP_RETRIEVAL reason="pricing_snapshot_register_complete" -->
<!-- VCB:END_REGISTER id=vcb.register.pricing_snapshots -->
