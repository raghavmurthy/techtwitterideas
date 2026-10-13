# Claude Code hands off X research to GrokBot via a webhook skill

**X post:** https://x.com/rileybrown/status/2109352621081309215  
**Author:** Riley Brown (@rileybrown) · posted 2026-10-11 (UTC) · 1356 likes, 105 replies  

## What it is
@rileybrown shows a 'grokbot-webhook' skill that lets Claude Code delegate X/Twitter research to GrokBot, which has full access to X posts; Claude waits for the answer and then continues its task. The skill itself is linked from the post.

## Thread highlights
> **@zhodonx:** Bot is ridiculously good with x research it’s crazy

> **@heypearlai:** X research is where Grok has the edge, so handing that off makes sense. i’d love more tools that work together like this

> **@vsaietta:** claude doing the actual work while grok scrolls the timeline for it, fair split

## Implications
- A concrete multi-agent pattern: each agent handles what it has the best access to (here, live X data), and the main coding agent orchestrates.
- For game devs, the same handoff can pull community feedback or tool announcements into a coding session without leaving the terminal.
- **Experiment:** wire one research handoff into a Claude Code session (e.g. 'find recent posts about Blender MCP issues') and check whether the returned summary is accurate against the source posts.

## Tags
`claude-code` `multi-agent` `skills` `research`
