---
id: vcb.maintenance.issue_4_ai_coding_tools_pricing_snapshot
title: Issue #4 AI Coding Tools Pricing Snapshot
artifact_type: maintenance_report
created_on: 2026-06-12
branch: issue-4-ai-coding-tools-pricing-snapshot
status: validation_passed
---

# Issue #4 AI Coding Tools Pricing Snapshot

Issue: https://github.com/frnklfrwsr/vibe-coding-bible/issues/4

Branch: `issue-4-ai-coding-tools-pricing-snapshot`

Snapshot ID: `vcb.pricing_snapshot.ai_coding_tools`

Snapshot file: `pricing-snapshots/2026-06-12-ai-coding-tools.md`

## Method

- Reviewed active AI coding, AI IDE, browser-dev, app-builder, and UI-generation tool cards in `TOOL_REGISTER.md`.
- Included only active relevant tools already represented in the VCB tool layer.
- Checked official vendor pricing pages or official vendor docs only.
- Captured exact prices, credits, tokens, quotas, and plan packaging only in the dated pricing snapshot.
- Left Codex-specific OpenAI/Codex exact pricing to `vcb.pricing_snapshot.openai_codex`.
- Marked ChatGPT plan pricing as uncaptured; it is not owned by either active snapshot.
- Did not update stable cost-benefit prose with exact current prices.

## Tools Included

| Tool | VCB tool ID | Official pricing/source ID | Inclusion reason |
|---|---|---|---|
| Claude / Claude Code | `tool.claude` | `anthropic.pricing` | Active alternate AI review/coding tool; official page exposes Claude Code plan packaging. |
| Cursor | `tool.cursor` | `cursor.pricing` | Active AI IDE tool; official page exposes pricing and usage caveats. |
| GitHub Copilot | `tool.github_copilot` | `github.copilot.pricing`; `github.copilot.models_pricing`; `github.copilot.billing_individuals`; `github.copilot.billing_orgs` | Active AI IDE/GitHub-native assistant; official pages expose plan pricing and AI Credit mechanics. |
| Windsurf / Devin Desktop | `tool.windsurf` | `windsurf.pricing` | Active AI IDE tool now routed through Devin Desktop official pricing. |
| Replit | `tool.replit` | `replit.pricing` | Active browser-dev/app-building tool. |
| Lovable | `tool.lovable` | `lovable.pricing` | Active app-builder tool. |
| Bolt | `tool.bolt` | `bolt.pricing` | Active app-builder tool with token-based pricing. |
| v0 | `tool.v0` | `v0.pricing` | Active UI/app generation tool with plan and model-token pricing. |

## Tools Excluded

| Tool/category | Reason |
|---|---|
| OpenAI/Codex exact pricing | Codex-specific pricing is already covered by `vcb.pricing_snapshot.openai_codex`. |
| ChatGPT plan pricing | Not captured by either active snapshot; exact plan prices remain uncaptured until a scoped ChatGPT/OpenAI plan-pricing snapshot owns them. |
| Gemini Code Assist | No active `tool.gemini_code_assist` card was present in `TOOL_REGISTER.md`. |
| Hosting/deployment pricing | Deferred to `vcb.pricing_snapshot.hosting`. |
| Database/backend pricing | Deferred to `vcb.pricing_snapshot.databases`. |
| Observability/analytics pricing | Deferred to `vcb.pricing_snapshot.observability`. |
| Auth, payments, email, design, generic cloud, and other ecosystem pricing | Outside this bounded Part-of-Issue-#4 slice. |

## Official Sources Checked

| Source ID | Official source | Result |
|---|---|---|
| `anthropic.pricing` | https://claude.com/pricing | Captured visible Claude / Claude Code plan values and API-rate caveats. |
| `cursor.pricing` | https://cursor.com/pricing | Captured visible Hobby, Individual base, Teams, and Enterprise pricing; did not guess hidden tab prices. |
| `github.copilot.pricing` | https://github.com/features/copilot/plans | Captured visible individual plan prices, credits, feature packaging, and plan-pause caveats. |
| `github.copilot.models_pricing` | https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing | Captured GitHub AI Credits conversion and model-pricing mechanics. |
| `github.copilot.billing_individuals` | https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals | Captured individual AI Credit allowances and overage mechanics. |
| `github.copilot.billing_orgs` | https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises | Captured organization/enterprise AI Credit pooling and promotional allowance caveats. |
| `windsurf.pricing` | https://devin.ai/pricing | Captured Devin Desktop / Windsurf plan prices, team packaging, and quota caveats. |
| `replit.pricing` | https://replit.com/pricing | Captured Starter/Core/Pro/Enterprise prices and monthly credit amounts. |
| `lovable.pricing` | https://lovable.dev/pricing | Captured Pro/Business annual-billing prices, Enterprise platform-fee model, and visible credits. |
| `bolt.pricing` | https://bolt.new/pricing | Captured Free/Pro/Teams/Enterprise prices, token limits, and token-rollover caveats. |
| `v0.pricing` | https://v0.app/pricing | Captured Free/Team/Business/Enterprise prices, included credits, daily login credits, and visible model token rates. |

## Values Captured

- Visible self-serve monthly prices, annual-discount prices where stated, and custom/enterprise indicators.
- Visible included credits, tokens, quotas, and monthly/daily allotments.
- GitHub AI Credit conversion and credit allowances.
- v0 visible per-1M-token model rates.

## Values Not Captured

- Region-specific pricing, taxes, app-store billing, localized currencies, procurement terms, custom enterprise contracts, committed-spend discounts, full feature matrices, and exact values hidden behind account state or inaccessible UI tabs.
- Cursor Pro+/Ultra exact prices were not captured because the static official page did not expose them unambiguously.
- GitHub Copilot Business/Enterprise exact seat prices were not captured from the opened official sources; organization/enterprise AI Credit allowances were captured from official docs.
- ChatGPT plan pricing remains uncaptured because `vcb.pricing_snapshot.openai_codex` is Codex-specific.
- Lovable month-to-month prices were not captured; the official static text checked for Pro and Business was under the Annual billing selector.

## Files Changed

- `README.md`
- `PRICING_SNAPSHOT_REGISTER.md`
- `SOURCE_REGISTER.md`
- `indexes/INDEX_BY_STABILITY.md`
- `llms.txt`
- `llms-full.txt`
- `manifest.json`
- `TREE.txt`
- `pricing-snapshots/2026-06-12-ai-coding-tools.md`
- `maintenance-reports/issue-4-ai-coding-tools-pricing-snapshot.md`

## Source-Drift Watchlist

Not updated in this PR. Pricing pages are highly volatile and several are JS-heavy or account-sensitive; a bounded follow-up should decide whether to add these sources to the watcher and regenerate the baseline.

## Validator Result

`PYTHONPATH=C:\Users\toto2\Documents\Codex\2026-06-11\VCB-Project-Files\.test-tmp\validate_pydeps python scripts\validate_repository.py`

Result: passed.

- active chapter/topic files validated: 244
- shortcut IDs registered: 98
- tool IDs registered: 75
- pricing snapshots active: 2

## Remaining Deferred Pricing Categories

- `vcb.pricing_snapshot.hosting`
- `vcb.pricing_snapshot.databases`
- `vcb.pricing_snapshot.observability`

## Follow-Up Needed

- Continue Issue #4 with separate bounded pricing slices for hosting, databases, and observability.
- Consider a dedicated source-drift watcher update for official pricing URLs after deciding the desired polling/capture strategy.

<!-- VCB:STOP_RETRIEVAL reason="maintenance_report_complete" -->
