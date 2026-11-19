# Localising app subscription prices by purchasing power, with an agent doing the tier maths

**X post:** https://x.com/MaxHirsch13/status/2122848863304217045  
**Author:** max (@MaxHirsch13) · posted 2026-11-18 (UTC) · 139 likes, 14 replies  
**Source:** the post itself

## What it is
max, who says in his X bio that he builds mobile apps, suggests having an agent localise subscription prices for every App Store and Google Play storefront. His brief, paraphrased: use purchasing power parity (PPP) and GDP per capita relative to the US as the baseline, group countries into four or five tiers with a fixed multiplier each, never go below 20 percent of the US price, and round each price to a natural local price point that matches the stores' available price tiers. He frames it as a way to maximise revenue; he gives no before-and-after numbers.

## Thread highlights
> **@ezyxbt:** Worth comparing the tiers against Apple's own auto-generated local prices before overriding them, so you know which markets you're actually discounting further.

> **@RummenigeBV:** I'd add a usage-cost floor to this. my F1 app has an AI race engineer, so dropping a subscription to 20% of the US price doesn't make the model calls 80% cheaper

> **@wangyan_im:** ppp pricing converts way better abroad, but the tiers drift as exchange rates move and nobody rechecks them

> **@RyanBuildsApps:** Curious how you handle existing subscribers when you localize. Grandfather them at the old price, or let the new tier kick in on renewal?

> **@PaulBuilds00:** does ppp pricing actually lift revenue or just installs?

## Implications
- **Mobile games and apps sell worldwide by default:** the stores' automatic conversions follow exchange rates, not purchasing power, so many markets see prices that are high locally.
- **Floor by cost, not just by percentage:** if each user triggers paid AI or server calls, set the minimum from unit cost, as one reply points out.
- **Treat it as an experiment, not a rule:** measure revenue per storefront, not installs, and schedule a recheck because exchange rates drift.
- **Experiment:** have an agent produce a proposed price table (tiers, multipliers, rounded local prices) next to the stores' current auto-generated prices, apply it to a handful of storefronts only, and compare revenue per visitor against untouched storefronts for a month.

## Tags
`pricing` `monetization` `mobile` `app-store` `launch` `agent-workflow` `game-dev`
