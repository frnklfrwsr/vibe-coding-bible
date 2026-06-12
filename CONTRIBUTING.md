# Contributing

The Vibe Coding Bible is an AI-native knowledge base with strict routing, source, evidence, and retrieval rules. Contributions should improve the repository without weakening the distinction between official guidance, maintainer synthesis, field reports, and speculation.

## Before Opening a Pull Request

Identify the change type:

- official source update
- field-practice proposal
- tool-card update
- shortcut-card update
- pricing snapshot update
- index/routing fix
- validator/schema change
- typo/readability change
- license/governance change
- other

Use the evidence-level taxonomy already used by the repository. Add or update `SOURCE_REGISTER.md` for new sources, and keep source IDs stable where possible.

Update relevant indexes and routes when adding, moving, renaming, activating, planning, or deferring cards. Preserve VCB markers and `STOP_RETRIEVAL` boundaries.

Run:

```powershell
python scripts/validate_repository.py
```

## Repository Rules

- Do not promote community field practice to official best practice without evidence.
- Date volatile pricing, tool, model, availability, UI, and limit claims.
- Update `llms.txt` and `llms-full.txt` when retrieval routes change.
- Update `manifest.json` and registers when active, planned, deferred, candidate, or deprecated status changes.
- Keep official guidance, maintainer synthesis, field reports, and speculation clearly separated.
- Avoid adding broad new content in the same pull request as routing, schema, or validator changes unless the scope is explicit.
- Keep changes narrow enough for reviewers to verify source posture, routing, and validator coverage.

## Licensing

By contributing written content, you agree that it may be distributed under the Creative Commons Attribution 4.0 International license described in `LICENSE.md`.

By contributing scripts, schemas, workflow code, validator code, or executable/support code, you agree that it may be distributed under the MIT License described in `LICENSE-CODE.md`.
