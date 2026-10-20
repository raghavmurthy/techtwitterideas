# Have subagents audit 20 web performance issues

**X post:** https://x.com/Voxyz_ai/status/2110083153930920113  
**Author:** Vox (@Voxyz_ai) · posted 2026-10-13 (UTC) · 1184 likes, 32 replies  

## What it is
@Voxyz_ai suggests having Claude Code send four subagents to check 20 performance issues in a vibe-coded site, then fix them in one pass. Groups: images and fonts (WebP/AVIF at display size, lazy loading, framework font loading, removing unused third-party scripts); frontend code (bundle analysis, dynamic imports, server-fetched first data, streaming AI answers, skeletons); database and APIs (indexes including those used by row-level security, N+1 fixes, pagination, caching only non-user data, background jobs); servers and network (co-locating functions with the database, static/ISR pages, parallel API calls, testing on a throttled low-end Android). He recommends measuring with Lighthouse before and after and not removing features for speed. A reply notes the main above-the-fold image must not be lazy-loaded.

## Thread highlights
> **@ApogeeIS:** I would still confirm the LCP element itself does not carry loading="lazy", which is a common lab and field regression:

## Implications
- Same audit shape applies to game web builds and store sites: assets, bundle, backend, network.
- **Experiment:** run a measured before/after Lighthouse pass on a game's landing page using these four groups as separate agent tasks.

## Tags
`performance` `subagents` `web` `checklist`
