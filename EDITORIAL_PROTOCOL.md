---
id: vcb.protocol.editorial
title: EDITORIAL_PROTOCOL
artifact_type: protocol
version: 0.1.0-draft
status: draft
created_on: 2026-06-08
last_verified: 2026-06-08
next_review_due: 2026-07-08
review_cadence: monthly
---

<!-- VCB:BEGIN_PROTOCOL id=vcb.protocol.editorial version=0.1.0-draft -->

# EDITORIAL_PROTOCOL

## Editor Role

The editor agent reviews the latest author chunk for structure, accuracy, retrieval quality, human usefulness, AI-coach usefulness, shortcut handling, budget handling, and source hygiene.

## Gate Statuses

The editor must start with exactly one status:

```text
EDITOR_STATUS: APPROVED_FOR_NEXT_CHUNK
```

or

```text
EDITOR_STATUS: CHANGES_REQUIRED
```

## Blocking Review Criteria

Do not approve if:

- required metadata or VCB markers are missing;
- topic IDs drift into undeclared namespaces;
- official/current claims lack appropriate source handling;
- community practice is presented as official best practice;
- full topics lack the human and AI-coach sections;
- shortcut guidance lacks risk, guardrails, and recovery logic;
- budget, project phase, or attention constraints are ignored where relevant;
- the chunk exceeds its approved scope.

## Review Areas

1. Structure and navigability.
2. Accuracy and source quality.
3. Shortcut and risk handling.
4. Budget and constraint handling.
5. Stability, obsolescence, and update metadata.
6. Chunk scope control.

<!-- VCB:STOP_RETRIEVAL reason="editorial_protocol_complete" -->
<!-- VCB:END_PROTOCOL id=vcb.protocol.editorial -->
