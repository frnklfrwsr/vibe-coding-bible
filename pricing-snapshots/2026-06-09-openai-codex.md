---
id: vcb.pricing_snapshot.openai_codex
title: OpenAI/Codex Pricing Snapshot — 2026-06-09
artifact_type: pricing_snapshot
snapshot_date: 2026-06-09
vendor: OpenAI
official_source_url: https://developers.openai.com/codex/pricing
additional_official_sources:
  - https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan
  - https://help.openai.com/en/articles/20001106-codex-rate-card
  - https://chatgpt.com/pricing/
last_verified: 2026-06-09
next_review_due: 2026-07-09
review_cadence: monthly
pricing_volatility: very_high
status: active_snapshot
---

<!-- VCB:BEGIN_PRICING_SNAPSHOT id=vcb.pricing_snapshot.openai_codex version=0.1.0 date=2026-06-09 -->

# OpenAI/Codex Pricing Snapshot — 2026-06-09

> This file is a dated volatile snapshot. It is allowed to contain exact current values. Do not copy exact prices, credits, rate limits, model names, plan packaging, or quota tables into stable chapters without linking back to this snapshot and marking the prose volatile.

## Snapshot Scope

This snapshot records official OpenAI/Codex pricing and usage anchors checked on 2026-06-09. It is intentionally narrow: OpenAI/Codex only. Other vendor pricing snapshots are deferred.

## Official Sources Checked

| Source ID | URL | Use |
|---|---|---|
| `openai.codex.pricing` | https://developers.openai.com/codex/pricing | Codex pricing, plan-feature availability, local/cloud/code-review limit tables |
| `openai.help.codex_chatgpt_plan` | https://help.openai.com/en/articles/11369540-using-codex-with-your-chatgpt-plan | Plan usage limits, agentic usage sharing, data-control notes |
| `openai.help.codex_rate_card` | https://help.openai.com/en/articles/20001106-codex-rate-card | Token-based Codex credit rate card |
| `openai.chatgpt.pricing` | https://chatgpt.com/pricing/ | ChatGPT plan packaging overview |

## Captured Current Facts

- Codex usage limits depend on plan and count toward agentic usage; the number of usable messages varies by task size, complexity, and where the work runs.
- Some Plus and Pro users can add credits after reaching Codex limits; other users may need to upgrade or wait for reset.
- Codex credit usage is token-based: credits per million input tokens, cached input tokens, and output tokens.
- The Help Center rate card states current credit rates by model family; rates and model availability are volatile.
- The Codex pricing page includes current local-message, cloud-task, and code-review ranges by plan/model; those ranges are volatile and must be rechecked before use in cost advice.

## Exact Rate Card Values Captured

| Model / mode | Input tokens | Cached input tokens | Output tokens | Notes |
|---|---:|---:|---:|---|
| GPT-5.5 | 125 credits / 1M | 12.50 credits / 1M | 750 credits / 1M | official rate-card value checked 2026-06-09 |
| GPT-5.5 Cyber | 500 credits / 1M | 50 credits / 1M | 3,000 credits / 1M | special-program availability note in source |
| GPT-5.4 | 62.50 credits / 1M | 6.250 credits / 1M | 375 credits / 1M | official rate-card value checked 2026-06-09 |
| GPT-5.4-Mini | 18.75 credits / 1M | 1.875 credits / 1M | 113 credits / 1M | official rate-card value checked 2026-06-09 |
| GPT-5.3-Codex | 43.75 credits / 1M | 4.375 credits / 1M | 350 credits / 1M | code review uses GPT-5.3-Codex according to source |
| GPT-5.2 | 43.75 credits / 1M | 4.375 credits / 1M | 350 credits / 1M | official rate-card value checked 2026-06-09 |
| GPT-5.3-Codex-Spark | research preview | research preview | research preview | source says rates are not final |

## Limit Snapshot Policy

The Codex pricing page currently shows plan/model usage ranges. This snapshot does not freeze those full tables into every chapter. Chapter 40 links here and tells AI coaches to verify the live pricing page before advising on exact plan decisions.

## What Was Not Captured

- Non-OpenAI vendor pricing.
- Exact current prices for all tools in the tool stack catalog.
- Exhaustive plan-feature matrices.
- Workspace-specific enterprise terms.
- Region-specific pricing or taxes.

## Obsolescence Watch

This snapshot is obsolete when:

- OpenAI changes Codex rate-card values.
- ChatGPT plan packaging changes.
- Codex model names, limits, or credit behavior changes.
- Official docs replace token-based credits with another mechanism.
- A newer OpenAI/Codex pricing snapshot is accepted.

<!-- VCB:STOP_RETRIEVAL reason="pricing_snapshot_complete" -->
<!-- VCB:END_PRICING_SNAPSHOT id=vcb.pricing_snapshot.openai_codex -->
