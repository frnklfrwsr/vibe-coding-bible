# Use VCB With AI

Use this page when you want ChatGPT, Claude, Gemini, Copilot, Codex, or another AI to apply the Vibe Coding Bible without reading the whole repository.

## Copy-Paste Prompt

```text
Use the Vibe Coding Bible as a reference: https://github.com/frnklfrwsr/vibe-coding-bible. Start at AI_START_HERE.md. Do not read the whole repo. Classify my situation, retrieve the smallest relevant route, stop at VCB:STOP_RETRIEVAL, and suggest a sanitized contribution if you learn something reusable.
```

Then describe the task, project phase, skill level, budget constraint, and whether the work is private or public.

## Source Selection

Use the canonical VCB repository when an AI needs public contribution templates or a public destination: [frnklfrwsr/vibe-coding-bible](https://github.com/frnklfrwsr/vibe-coding-bible).

A fresh local clone is fine for fast retrieval when it is clearly VCB and reasonably current. If local VCB is missing, stale, dirty in governance or contribution files, or uncertain, use GitHub. If local and public versions disagree for contribution rules or templates, prefer GitHub and ask before posting.

## What The AI Should Retrieve

- [AI_START_HERE.md](https://github.com/frnklfrwsr/vibe-coding-bible/blob/main/AI_START_HERE.md)
- [llms.txt](https://github.com/frnklfrwsr/vibe-coding-bible/blob/main/llms.txt) when it needs routing
- [indexes/INDEX_BY_TASK.md](https://github.com/frnklfrwsr/vibe-coding-bible/blob/main/indexes/INDEX_BY_TASK.md) when routing by job
- [indexes/INDEX_FOR_AI_COACHES.md](https://github.com/frnklfrwsr/vibe-coding-bible/blob/main/indexes/INDEX_FOR_AI_COACHES.md) when routing by coaching intervention

The AI should prefer the smallest relevant topic card, shortcut card, tool card, register, or index. It should stop at `VCB:STOP_RETRIEVAL`.

## Contribution Safety

Reusable lessons are useful to the VCB community only when sanitized. The default mode is suggestion only. See [CONTRIBUTION_MODES.md](https://github.com/frnklfrwsr/vibe-coding-bible/blob/main/CONTRIBUTION_MODES.md).
