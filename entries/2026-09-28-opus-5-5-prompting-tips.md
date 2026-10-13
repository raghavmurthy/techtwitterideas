# Opus 5.5 prompting tips from Anthropic's guide (summary)

**X post:** https://x.com/ishuagra02/status/2104561675412120058  
**Author:** Ishu Agrawal (@ishuagra02) · posted 2026-09-28 (UTC) · 7 likes, 0 replies  

## What it is
@ishuagra02 summarises Anthropic's Opus 5.5 prompting guide: asking it to 'think carefully' adds latency without quality gains; long autonomous runs can stop early unless progress is tracked or the done-state is defined; in multi-agent setups, give a time budget and have subagents report elapsed time against it; with connected data, ask it to explore before acting; for frontend design, name specific unwanted patterns instead of saying 'avoid AI slop'. His TL;DR: ask it to look around rather than think carefully.

## Thread highlights
- No notable replies came back from X search for this thread.

## Implications
- Defining the done-state up front fits engine tasks well (e.g. 'scene opens, no console errors, prefab count matches').
- Time budgets per subagent help when parallel agents handle Blender asset and code tasks together.
- **Experiment:** rewrite one recurring Unity agent prompt to define the completed state and list banned UI patterns, then compare early-stop rate and rework over 5 runs.

## Tags
`claude` `prompting` `multi-agent` `workflow`
