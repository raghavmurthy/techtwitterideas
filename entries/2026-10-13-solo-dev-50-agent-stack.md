# Solo developer's 50-agent stack: $545k MRR, 1,089 PRs in a week

**X post:** https://x.com/navuud/status/2109913381780250640  
**Author:** navuud (@navuud) · posted 2026-10-13 (UTC) · 556 likes, 72 replies  

## What it is
@navuud describes running a 1M+ line app as the only full-time developer, with 1,089 PRs merged in 7 days (his numbers). The stack: 50+ parallel agents on a home Linux server, multiple Claude/Codex/SuperGrok plans, Slack/Telegram instead of a terminal or IDE, Linear as the bots' issue tracker, preview environments, self-hosted Mac minis for iOS builds and end-to-end iPhone tests, Sentry, an orchestrator agent that never touches code, a 5-stage planning harness, reviews by a different model than the author, Greptile, and a watcher that auto-reverts web merges if real users start failing within 24 hours.

## Thread highlights
- No notable replies came back from X search for this thread.

## Implications
- The transferable ideas are structural: plan before code, never let the authoring model approve its own PR, and auto-revert on real-user failure signals.
- For game teams, the Mac-mini iOS build farm with end-to-end device journeys is the piece most studios lack.
- **Experiment:** add a second-model review step to an engine project's PRs (e.g. Claude writes, Codex reviews) for two weeks and count the bugs it catches before merge.

## Tags
`agent-workflow` `orchestration` `code-review` `ci`
