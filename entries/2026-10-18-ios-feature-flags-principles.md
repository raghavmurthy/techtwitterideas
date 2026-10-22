# Seven principles for feature flags at scale on iOS

**X post:** https://x.com/navuud/status/2111701128903799113  
**Author:** navuud (@navuud) · posted 2026-10-18 (UTC) · 266 likes, 6 replies  

## What it is
A "note to self", quoting another developer's setup, that boils feature flags at scale on iOS down to seven principles: keep values out of the code so live events, segmentation and A/B tests can change server-side; use a lightweight client SDK with local caching; bucket users deterministically so each user sees the same variant across sessions; define targeting rules from user attributes; send exposure events to analytics (PostHog or Amplitude are suggested); handle version compatibility with safe fallback defaults; and run a cleanup routine so dead flags don't pile up.

## Thread highlights
> **@icysaas:** 1. is a gray area with the new apple rules

> **@hecodesforme:** I'd give every flag an expiry date the day it's created, cleanup never happens otherwise

> **@firtoz:** Just use posthog dude

> **@jeremyklar:** Very easy to do in firebase

## Implications
- **Mobile games:** live events and difficulty or economy tuning are classic server-side flags, but under Apple's new hidden-features guideline (see the 2.5.19 entries) remote switches that reveal unreviewed features are risky; tuning existing content is safer.
- **Unity:** deterministic bucketing plus cached defaults is the core of any remote-config setup, whether hand-built or via a hosted service.
- **Experiment:** add an expiry date field to every flag in your remote config and a weekly check that lists expired flags still referenced in code.

## Tags
`ios` `feature-flags` `ab-testing` `live-ops` `mobile`
