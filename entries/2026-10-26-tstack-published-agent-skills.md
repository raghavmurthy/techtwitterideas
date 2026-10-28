# tstack: Theo publishes the agent skills he uses daily

**X post:** https://x.com/theo/status/2114623574371963360  
**Author:** Theo - t3.gg (@theo) · posted 2026-10-26 (UTC) · 2,603 likes, 204 replies  

## What it is
Theo, CEO of T3 Code and T3 Chat per his X bio, announces tstack, an MIT-licensed repo (github.com/t3dotgg/tstack) of the agent skills he uses every day, for Claude Code and Codex. Per the README the skills are mostly about getting a change all the way to a merged pull request: `full-send` proves, reviews, files, watches and merges a change with nobody watching; `full-stop` does the same but stops when the PR is ready for a human to merge; `council` gets reviews from three models from different providers and loops until they agree; `sol-loop` loops a review with another model until both agents agree; `file-pr` writes short PRs that lead with the problem; `babysit-pr` watches CI and review bots and fixes real findings; `takeover` finishes someone else's PR while keeping their credit; `modernize` rebases an old PR and decides whether it should still exist; and `leaving-pr-comments` formats comments the agent posts. Several skills call others, and the reviewer skills need access to other providers' models. The README suggests keeping personal settings, such as which models sit on the council, in your own agent instructions file so the skills can be updated cleanly.

## Thread highlights
> **@KyleHovance:** My favorite line in sol-loop is telling the reviewer to prefer deleting code over adding a new helper or option, and capping it at 3 rounds.

> **@xiaoba_ai:** A 3-line "what this touches" header at the top of each SKILL.md (files, commands, network) would save people a lot of reading.

> **@sreeakkineni:** I'd be careful with full-send, since my own review loop ran five rounds on a delete-my-account change and still had 11 findings open when it hit the round cap

## Implications
- **Review loops across models:** having a second model from another provider review the first one's change, with a round cap and a bias toward deleting code, is a cheap way to cut agent-added bloat.
- **Know what a skill does before installing:** skills that push or merge are fine in your own repo but risky elsewhere; read each `SKILL.md` and check what it touches.
- **Game and tool repos:** for a Unity or Blender tooling repo, a "stop when ready for human merge" mode is the safer default than fully unattended merging.
- **Experiment:** adapt only the cross-model review loop: after an agent finishes a change in your repo, have a second model review it with a three-round cap and a "prefer deleting code" rule, and compare lines added against a single-model run.

## Tags
`skills` `agent-workflow` `code-review` `github` `claude-code` `codex` `open-source`
