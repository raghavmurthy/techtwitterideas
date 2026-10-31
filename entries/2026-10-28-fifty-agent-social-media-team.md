# A 50-agent social media research team in Claude Code, built around one context file

**X post:** https://x.com/dsqjaffa/status/2115541614986711387  
**Author:** jaffa (@dsqjaffa) · posted 2026-10-28 (UTC) · 622 likes, 13 replies  

## What it is
jaffa, co-founder of the social listening tool Virlo per his X bio, posts a tree of a "social media marketing team" of 50 Claude Code agents in 10 departments of five, and links a long X Article explaining it. The article is openly promotional: most agents depend on Virlo's video database and API, connected to Claude as a connector or MCP server, so read it as a vendor's playbook.

The structure is still a useful pattern. Each agent is one short file with a name, one job and its allowed tools; each department gets a skill folder holding a workflow, a template, a task recipe and an audit. Every agent reads a single niche context file, which Claude builds by interviewing the user one question at a time and marking anything unknown as a gap instead of inventing it. The departments run in order: niche research and competitor tracking (research), then outlier videos, outlier creators, hooks and formats/trends (intelligence), then scripts and "scaling" one winner into several ideas (production), then a Monday report and content operations. Two ideas stand out: ranking a video by how far it beats that creator's own typical views rather than by raw views, and a rules file where every correction the user makes becomes a rule the agents read before each task. The article also says nothing gets posted without the user's approval. In a reply, the author puts the running cost at a Claude subscription plus about $10 a month of Virlo API use.

## Thread highlights
> **@dsqjaffa:** you plug the agents directly into an API for social media data

> **@kuronovaX:** If u need so many agents , it’s a waste of everything - quality of output , tokens , context loss - this is just bad

> **@shreyaksingh:** 50 agents is the easy part now. The bottleneck is the one human who has to review what all 50 produce every week, that's where most of these setups quietly die

> **@jiang_yi62072:** High views with weak saves/shares usually just signal broad distribution, not a repeatable hook structure worth scaling.

## Implications
- **Context file plus rules file:** one shared brief that every agent reads, and a running list of corrections turned into rules, is the reusable part, whatever the domain.
- **Relative ranking beats raw numbers:** "how much better than this creator usually does" finds ideas that worked on their own merit, which is the same logic a small game studio needs when studying devlogs or trailer clips.
- **Count the review cost:** replies point out that 50 agents mostly means 50 outputs for one human to check; fewer, broader agents may be cheaper in tokens and attention.
- **Experiment:** for a game's short-form marketing, build only three pieces: a context file made by interview, an outlier pass that ranks clips in the genre by views relative to each creator's median, and a rules file updated after each review. Compare a week of picks against picks by raw view count.

## Tags
`agents` `claude-code` `skills` `marketing` `content` `ugc` `agent-workflow`
