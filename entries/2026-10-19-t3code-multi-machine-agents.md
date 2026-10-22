# T3 Code impressions: multi-machine, multi-provider agent threads

**X post:** https://x.com/tenobrus/status/2112215624852328782  
**Author:** Tenobrus (@tenobrus) · posted 2026-10-19 (UTC) · 851 likes, 70 replies  

## What it is
A detailed first-day review of t3code, an open-source agent app, by a user running several machines. Positives: the smoothest setup the author has seen for linking multiple computers over Tailscale and working on threads remotely, including on mobile, which he says beats first-party apps; reliable cross-agent communication where each provider (Claude Code, Codex) keeps its normal tools but can start and query threads of other models; support for multiple subscriptions; and a snappy UI that doesn't feel vibe-coded. Negatives: threads on different machines couldn't contact each other at all (a PR chain for this was in progress, and he had Claude finish the feature locally since the app is open source); and he dislikes the opinionated design, especially the sidebar. He ended up building his own agent harness using t3code as the backend, saying coding models may now be just fast enough to make that worthwhile.

## Thread highlights
> **@unstoppableweb:** we're releasing multi-computer support

> **@zollicoff_:** you just have to pair each computer to each computer, (like both directions between two). just successfully tested this in my setup

> **@_m16b:** Computer use was another big thing; I ended up hacking together a web UI over Tailscale for agents to use chromium+virtual desktops

## Implications
- **Agent workflows:** running agents on a desktop with a GPU (for Unity or Blender) while steering from a laptop or phone is exactly the multi-machine case this targets.
- **Tooling:** cross-provider threads (one model building, another reviewing) without a stripped-down harness is the feature to look for in any agent front-end.
- **Experiment:** link two machines, run a Blender-scripting agent on the stronger one, and steer it from the other for a day; note latency and what breaks.

## Tags
`agent-tooling` `claude-code` `codex` `multi-machine` `open-source`
