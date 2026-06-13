# Use VCB With Codex

Use this page when Codex is helping you apply the Vibe Coding Bible to a repository task.

## Fast Prompt

```text
Use the Vibe Coding Bible as a reference. Start at AI_START_HERE.md. Do not read the whole repo. Classify my situation, retrieve the smallest relevant route, stop at VCB:STOP_RETRIEVAL, and suggest a sanitized contribution if you learn something reusable.
```

## Codex Skill

If skills are available, ask Codex to use:

```text
$vcb-reference
```

The repository skill file is:

```text
.agents/skills/vcb-reference/SKILL.md
```

The skill tells Codex to classify the situation, route through `AI_START_HERE.md` and the LLM maps, retrieve only the smallest useful VCB files, respect stop markers, preserve evidence status, and suggest only sanitized contributions by default.

## Source Selection

The canonical VCB repository is `https://github.com/frnklfrwsr/vibe-coding-bible`.

Codex may use a fresh local VCB clone for fast retrieval when it is clearly VCB and reasonably current. If local VCB is missing, stale, dirty in governance or contribution files, or uncertain, use the public GitHub repo.

For public issues, comments, and PRs, target the canonical GitHub repo. If local and public files disagree, prefer GitHub for contribution templates, governance files, and destination. Ask before posting when unsure.

## Good Codex Workflow

1. Tell Codex your situation: new project, existing bug, low budget, tool choice, shortcut risk, or contribution.
2. Let Codex retrieve the smallest VCB route.
3. Ask Codex to apply the guidance to your current repo or plan.
4. Ask for verification steps before accepting code changes.
5. If a reusable lesson appears, ask Codex to draft a sanitized usage insight instead of publishing private details.

## What To Avoid

- Do not ask Codex to ingest the full VCB repository.
- Do not use VCB as permission to skip review.
- Do not let Codex publish private project details as a public contribution.
