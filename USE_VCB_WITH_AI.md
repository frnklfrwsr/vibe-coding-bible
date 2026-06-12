# Use VCB With AI

The fastest way to use the Vibe Coding Bible is to give your AI one instruction: start at `AI_START_HERE.md`, choose the smallest route, and stop when the route is complete.

## Fastest Way With Any AI

Copy this prompt into ChatGPT, Claude, Gemini, Copilot, or another web AI:

```text
Use the Vibe Coding Bible as a reference: https://github.com/frnklfrwsr/vibe-coding-bible. Start at AI_START_HERE.md. Do not read the whole repo. Classify my situation, retrieve the smallest relevant route, stop at VCB:STOP_RETRIEVAL, and suggest a sanitized contribution if you learn something reusable.
```

Then describe your task in one or two paragraphs. Include whether you are new to coding, new to Codex, working in a new project, debugging an existing project, low on budget, or comparing tools.

## Fastest Way With Codex

If the repository is available locally, tell Codex:

```text
Use the Vibe Coding Bible as a reference. Start at AI_START_HERE.md. Do not read the whole repo. Classify my situation, retrieve the smallest relevant route, stop at VCB:STOP_RETRIEVAL, and suggest a sanitized contribution if you learn something reusable.
```

If Codex skills are available, use the VCB skill:

```text
Use $vcb-reference for this task.
```

The skill lives at:

```text
.agents/skills/vcb-reference/SKILL.md
```

## What The AI Should Do

- Start with `AI_START_HERE.md`.
- Classify your situation before retrieving more files.
- Prefer topic cards, shortcut cards, tool cards, registers, and indexes over long chapters.
- Read only the smallest files needed.
- Stop at `VCB:STOP_RETRIEVAL` unless you explicitly ask for related context.
- Preserve source status: official docs, maintainer synthesis, candidate field report, reproduced field report, or speculation.
- Suggest safe contribution opportunities only when a reusable lesson appears.

## What Not To Do

- Do not ask the AI to summarize the entire repository.
- Do not paste the whole repository into a chat.
- Do not treat candidate field practices as official best practices.
- Do not freeze exact volatile pricing, limits, or UI labels into stable advice without checking current official sources.
- Do not let an AI publish private project details as a public VCB contribution.

## Safe Contribution Path

The default contribution mode is `suggest`.

That means the AI may say: "This looks like a reusable VCB lesson. Consider filing a sanitized usage insight." It must not post publicly or open a PR unless you explicitly ask and the content is safe.

Use `CONTRIBUTION_MODES.md` for privacy rules and `.github/ISSUE_TEMPLATE/usage-insight.yml` for sanitized usage observations.

<!-- VCB:STOP_RETRIEVAL reason="human_ai_usage_guide_complete" -->
