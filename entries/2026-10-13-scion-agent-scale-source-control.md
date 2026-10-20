# Anthropic's Scion: source control rebuilt for agent-scale merges

**X post:** https://x.com/AnthropicAI/status/2110047081414987957  
**Author:** Anthropic (@AnthropicAI) · posted 2026-10-13 (UTC) · 25638 likes, 1158 replies  

## What it is
Anthropic says merges grew from ~2,500/day in May to 30,000+/day in September 2026, so it built Scion, an in-house version control system, and migrated its monorepo off git in five months with a team of seven. Per its engineering blog: clients are assumed always online, the server answers history/blame and performs commits and merges, all data is content-addressed and cached in tiers with 99%+ hit rates, checkouts are sparse or virtual, and infrastructure is 200x smaller than its old git mirrors with checkouts in seconds. Lessons: engineers mainly set design constraints and often told Claude 'no', adversarial review can over-engineer, single-component monitoring agents ('superfans') catch subtle issues, and a global merge-queue lock no longer fits. It says Scion isn't a general git replacement but expects similar problems elsewhere within 6–12 months.

## Thread highlights
> **@DSJayatillake:** Will this become built into the product? Tighter coupling between the agent harness and source control will inevitably be beneficial. More natural handling of how multiple agents work at the same time on the codebase will be very beneficial too, I am thinking of how agents message each other across claude code sessions right now being greatly enhanced. You could have a shared readable event bus of unmerged code changes that all agent sessions can see while developing to avoid conflicts. I am sure other possibilities abound.

> **@AlexChhk:** same take, visible beats locked. that's how i built concord: agents claim files before editing, get flagged on overlap, then wait or message the other agent, even across claude code + codex. open source:

## Implications
- Most teams won't need Scion, but the principles apply now: give agents server-side queries instead of full clones, and design CI for many parallel changes.
- Large binary game repos already strain git; sparse/virtual checkouts are relevant for agent sandboxes.
- **Experiment:** measure how long agent sandboxes spend cloning a game repo, then try sparse checkout of only the code folders and compare.

## Tags
`source-control` `agents` `infra` `ci`
