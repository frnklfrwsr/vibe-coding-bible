---
id: vcb.pricing_snapshot.ai_coding_tools
title: AI Coding Tools Pricing Snapshot - 2026-06-12
artifact_type: pricing_snapshot
snapshot_date: 2026-06-12
vendor: Multiple official AI coding and app-building vendors
official_source_url: https://claude.com/pricing
additional_official_sources:
  - https://cursor.com/pricing
  - https://github.com/features/copilot/plans
  - https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing
  - https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals
  - https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises
  - https://devin.ai/pricing
  - https://replit.com/pricing
  - https://lovable.dev/pricing
  - https://bolt.new/pricing
  - https://v0.app/pricing
last_verified: 2026-06-12
next_review_due: 2026-07-12
review_cadence: monthly
pricing_volatility: very_high
status: active_snapshot
---

<!-- VCB:BEGIN_PRICING_SNAPSHOT id=vcb.pricing_snapshot.ai_coding_tools version=0.1.0 date=2026-06-12 -->

# AI Coding Tools Pricing Snapshot - 2026-06-12

> This file is a dated volatile snapshot. It is allowed to contain exact current values. Do not copy exact prices, credits, quotas, token limits, plan packaging, or usage tables into stable chapters without linking back to this snapshot and marking the prose volatile.

## Snapshot Scope

This snapshot records official pricing anchors checked on 2026-06-12 for active VCB AI coding, AI IDE, browser-dev, app-builder, and UI-generation tools:

- Claude / Claude Code
- Cursor
- GitHub Copilot
- Windsurf / Devin Desktop
- Replit
- Lovable
- Bolt
- v0

OpenAI/Codex exact pricing is excluded because `vcb.pricing_snapshot.openai_codex` owns the Codex-specific rate-card and usage scope. ChatGPT plan pricing is not captured by either active snapshot and remains uncaptured until a scoped ChatGPT/OpenAI plan-pricing snapshot is approved. Gemini Code Assist is excluded because no active `tool.gemini_code_assist` card is present in `TOOL_REGISTER.md`.

Hosting, database, observability, auth, payments, email, design, and generic cloud pricing remain out of scope for this Part-of-Issue-#4 slice.

## Official Sources Checked

| Source ID | URL | Use |
|---|---|---|
| `anthropic.pricing` | https://claude.com/pricing | Claude plan pricing, Claude Code inclusion, Team/Enterprise packaging, API-rate caveats |
| `cursor.pricing` | https://cursor.com/pricing | Cursor Hobby/Individual/Teams/Enterprise pricing and usage caveats |
| `github.copilot.pricing` | https://github.com/features/copilot/plans | GitHub Copilot individual plan pricing, plan pauses, credits, feature packaging |
| `github.copilot.models_pricing` | https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing | GitHub AI Credits conversion and per-model pricing concept |
| `github.copilot.billing_individuals` | https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-individuals | Individual-plan AI credit allowances and overage mechanics |
| `github.copilot.billing_orgs` | https://docs.github.com/en/copilot/concepts/billing/usage-based-billing-for-organizations-and-enterprises | Organization/enterprise AI credit pooling and allowances |
| `windsurf.pricing` | https://devin.ai/pricing | Windsurf/Devin Desktop plan pricing, team packaging, usage-overage caveats |
| `replit.pricing` | https://replit.com/pricing | Replit Starter/Core/Pro/Enterprise pricing and credits |
| `lovable.pricing` | https://lovable.dev/pricing | Lovable Pro/Business/Enterprise pricing and credits |
| `bolt.pricing` | https://bolt.new/pricing | Bolt Free/Pro/Teams/Enterprise pricing, token limits, hosting/package notes |
| `v0.pricing` | https://v0.app/pricing | v0 Free/Team/Business/Enterprise pricing, included credits, model token rates |

## Snapshot Table

| Tool | Official source | Plans / pricing model | Exact values captured | Not captured / caveats | Last checked | Next review |
|---|---|---|---|---|---|---|
| Claude / Claude Code | `anthropic.pricing` | Subscription plans plus API-rate usage for some business tiers | Free `$0`; Pro `$17/month` with annual subscription discount (`$200` billed up front) or `$20` monthly; Max from `$100/month`; Team standard seat `$20/seat/month` annual or `$25` monthly; Team premium seat `$100/seat/month` annual or `$125` monthly; Enterprise seat price plus usage at API rates, with visible `$20/seat` starting point; Claude Code included in Pro, Team, and related higher tiers where stated | Taxes, regional pricing, education pricing, exact usage-limit quantities, enterprise negotiated terms, and full API model-rate table not reproduced here | 2026-06-12 | 2026-07-12 |
| Cursor | `cursor.pricing` | AI IDE subscription plans with included usage and usage-based overage | Hobby Free; visible Individual base price `$20/month`; Teams `$40/user/month`; Enterprise Custom | Static page exposed Individual/Teams pricing but did not clearly expose exact prices for every tabbed Individual tier such as Pro+/Ultra; exact included model-usage quantities and overage rates not captured | 2026-06-12 | 2026-07-12 |
| GitHub Copilot | `github.copilot.pricing`; `github.copilot.models_pricing`; `github.copilot.billing_individuals`; `github.copilot.billing_orgs` | Individual subscriptions plus AI Credits; organization/enterprise credits are pooled | Pro `$10 USD/user/month` with `$15` monthly total credits; Pro+ `$39 USD/user/month` with `$70` monthly total credits; Max `$100 USD/user/month` with `$200` monthly total credits; individual credit allowances: Pro `1,500`, Pro+ `7,000`, Max `20,000`; `1 AI credit = $0.01 USD`; org pooled monthly credits: Business `1,900` per user, Enterprise `3,900` per user; promotional org amounts through 2026-09-01: Business `3,000`, Enterprise `7,000` per user | Copilot Pro/Pro+/Max sign-ups were marked temporarily paused on the official page; Business/Enterprise exact seat prices were not captured from the opened sources; full model-token table not reproduced | 2026-06-12 | 2026-07-12 |
| Windsurf / Devin Desktop | `windsurf.pricing` | Individual and team subscriptions with quotas; extra usage can be purchased at API pricing | Free `$0`; Pro `$20/month`; Max `$200/month`; Teams `$80/month` for team plan plus `$40/month` per full dev seat; Enterprise `Let's talk`; compare table shows Free/Pro/Max members `1`, Team unlimited flex seats plus paid full users, Enterprise unlimited | Exact quota sizes, API-pricing overage rates, region/tax effects, and enterprise terms not captured | 2026-06-12 | 2026-07-12 |
| Replit | `replit.pricing` | Browser-dev/app-building subscriptions with monthly credits | Starter Free; Replit Core `$25/month` or `$20/month` billed annually with `$25` monthly credits; Replit Pro `$100/month` or `$95/month` billed annually with `$100` monthly credits; Enterprise Custom | Exact pay-as-you-go effort pricing, tax, enterprise seat terms, and full hosting/runtime add-on cost details not captured | 2026-06-12 | 2026-07-12 |
| Lovable | `lovable.pricing` | App-builder subscription shared across unlimited users plus credits | Pro `$25/month` with the official page set to Annual billing, `100 credits/month`, plus `5 daily credits` up to `150/month`; Business `$50/month` with the official page set to Annual billing, `100 credits/month`; Enterprise platform fee based on company size with volume-based credit pricing | Month-to-month Lovable prices were not captured; Free-plan exact limits, Cloud + AI usage-based rates, student discount terms, enterprise price, taxes, and custom add-ons not captured | 2026-06-12 | 2026-07-12 |
| Bolt | `bolt.pricing` | Browser app-builder subscriptions with tokens, hosting, and database packaging | Free `$0`, `300K` token daily limit, `1M` tokens/month; Pro `$25/month` billed monthly, starts at `10M` tokens/month and no daily token limit; Teams `$30/month/member` billed monthly; Enterprise Custom | Annual discount exact values, token top-up prices, enterprise terms, hosting/database add-on limits, and promotional domain details not captured | 2026-06-12 | 2026-07-12 |
| v0 | `v0.pricing` | UI/app generation plans with included credits plus per-model token rates | Free `$0/month`, `$5` included monthly credits, `7` messages/day; Team `$30/user/month`, `$30` included monthly credits per user plus `$2` free daily credits on login per user; Business `$100/user/month`, `$30` included monthly credits per user plus `$2` daily login credits; Enterprise Custom Pricing; model rates captured: v0 Mini input/cache-write/cache-read/output `$1/$1.25/$0.10/$5` per 1M tokens; v0 Pro `$3/$3.75/$0.30/$15`; v0 Max `$5/$6.25/$0.50/$25`; v0 Max Fast `$10/$12.50/$1/$50` | On-demand credit purchase details, expiration behavior, taxes, Vercel account coupling, enterprise terms, and future model changes not captured | 2026-06-12 | 2026-07-12 |

## Exact Values Captured

- Current self-serve monthly or annual-discount plan prices visible in the official pages above.
- Current included credits or tokens where the official page exposed them in accessible static text.
- Current GitHub AI Credit conversion and selected credit allowances from official GitHub Docs.
- v0 model token rates visible in the official pricing page.

## Values Not Captured

- Region-specific prices, taxes, app-store billing differences, currency localization, and purchasing-power adjustments.
- Negotiated enterprise terms, committed-spend discounts, seat minimums not visible in the official static text, procurement terms, or custom security/compliance add-ons.
- Complete feature matrices for every plan.
- Complete model-rate tables except the v0 rates explicitly listed above and GitHub credit mechanics summarized above.
- Usage amounts hidden behind account state, UI tabs that did not render unambiguously in static text, or vendor pages that require account-specific configuration.
- ChatGPT plan pricing. `vcb.pricing_snapshot.openai_codex` is Codex-specific and does not freeze exact ChatGPT plan prices.
- Lovable month-to-month prices; the official static text checked for Pro and Business was under the Annual billing selector.
- Hosting, database, observability, auth, payment, email, design, or cloud-platform pricing outside this snapshot's AI-coding/app-builder scope.

## Plan, Credit, and Quota Caveats

- Most AI coding tools now combine subscription pricing with credits, tokens, quotas, flex allotments, or usage-based overage. Monthly plan price is not total cost for heavy agentic work.
- Agentic tasks can consume more credits or tokens than chat/autocomplete because they read files, make multiple model calls, run tools, and preserve context.
- App builders may bundle hosting, database, domains, or publishing features with AI credits. Treat those bundled surfaces as convenience packaging until a hosting/database pricing snapshot covers them.
- Enterprise, team, and compliance plans can change procurement, data-control, security, and administrative behavior in ways not represented by simple price rows.

## Stable Routing Policy

Stable topic cards should route exact non-OpenAI AI-coding-tool prices, credits, quotas, and plan packaging to this dated snapshot. They should not duplicate exact current values in durable prose. ChatGPT plan pricing is not covered by this snapshot and should stay uncaptured until a scoped snapshot owns it.

## Obsolescence Watch

This snapshot is obsolete when:

- any listed vendor changes plan names, plan prices, credits, tokens, quotas, or included model access;
- any listed vendor replaces credit/token billing with a new unit;
- Cursor exposes new unambiguous Pro+/Ultra pricing not captured here;
- GitHub changes Copilot AI Credit allowances, pauses/unpauses sign-ups, or changes model pricing;
- Windsurf/Devin Desktop changes product naming, plan packaging, or overage pricing;
- a newer `vcb.pricing_snapshot.ai_coding_tools` file is accepted.

<!-- VCB:STOP_RETRIEVAL reason="pricing_snapshot_complete" -->
<!-- VCB:END_PRICING_SNAPSHOT id=vcb.pricing_snapshot.ai_coding_tools -->
