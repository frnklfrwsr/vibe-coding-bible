# Use VCB With ChatGPT Web

Use this page when ChatGPT web or another web agent is helping you apply VCB from public GitHub access.

Public repository:

[https://github.com/frnklfrwsr/vibe-coding-bible](https://github.com/frnklfrwsr/vibe-coding-bible)

## Copy-paste prompt

```text
Use the Vibe Coding Bible as a reference:
https://github.com/frnklfrwsr/vibe-coding-bible

Start at AI_START_HERE.md.
Do not read the whole repo.
Classify my situation.
Retrieve only the smallest relevant files.
Stop at VCB:STOP_RETRIEVAL.
If you learn something reusable, draft a sanitized VCB contribution for me to review.
```

## Retrieval rules

- Start at `AI_START_HERE.md`.
- Do not ingest the whole repository.
- Classify the user's situation before opening more files.
- Retrieve the smallest route that can answer the task.
- Stop at `VCB:STOP_RETRIEVAL` unless the user explicitly asks for related context.
- Use the public GitHub repository when a local clone is unavailable or cannot be verified as fresh.

## Contribution mode

The default contribution mode is suggest or draft. A web agent should not open issues, post comments, or create pull requests unless the user clearly asks for that public action and the tools/permissions are available.

If the web agent cannot write to GitHub, it should draft issue, comment, or PR text for the user to review and paste.

## Draft-only contribution template

```text
Suggested VCB contribution type:

Sanitized observation:

Why it is reusable:

Evidence level:

Private details removed:

Suggested destination:
```

## When to stop

Stop after the smallest route answers the task or after a draft contribution is ready for human review. Do not keep traversing VCB looking for more supporting files unless the user asks for broader context.

<!-- VCB:STOP_RETRIEVAL reason="chatgpt_web_usage_complete" -->
