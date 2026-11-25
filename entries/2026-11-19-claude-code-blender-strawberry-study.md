# Two weeks, 3,958 prompts and ~8.9B tokens: a logged case study of AI agents building a procedural Blender fruit add-on

**X post:** https://x.com/IntCyberDigest/status/2123287906139754795  
**Author:** International Cyber Digest (@IntCyberDigest) · posted 2026-11-19 (UTC) · 1,737 likes, 106 replies  
**Source:** the post, the source it links in its own reply (the creator's case study at https://strawberry-methodology.pages.dev/) and the creator's own posts; the 38-second video was not watched here

## What it is
International Cyber Digest, which describes itself in its X bio as independent reporting on cybersecurity, tech, AI and digital policy, reports that someone burned about 8.9 billion tokens getting Claude Code to make a single strawberry in Blender, citing the creator's own write-up: two weeks, 3,958 prompts and 17,453 tool calls. The creator, a video artist posting as @TheBigFlatNow1, had earlier shown the result as a procedural strawberry built from 64 geometry-node trees and 7,000+ nodes, and he confirmed in the replies that he made it.

The write-up is more interesting than the headline. It is a case study, counted and written by AI models at the creator's request, of how one person and several coding agents (two Claude models in Claude Code and a GPT model in Codex CLI) turned an unpaid strawberry animation job into a Blender add-on that generates fruit you can cut open, plus a 38-second intro film. Key points it reports:
- **Where the tokens went:** most of the 8.9 billion are the same conversation re-sent with every request and read from a cache; the Claude models processed about 1.5 billion tokens, nearly all cache reads, and wrote about 10.8 million. Half of the monthly flat subscription fees came to about €159.
- **How the work went:** 42 sessions; an agent typically made 2 tool calls before the human wrote again, and 74% of the human's prompts arrived while an agent was still working.
- **Where it broke:** in at least 20 episodes an agent's check or reassuring report was followed by a fault the human found by looking; in at least 24 an agent reported a false status; in at least 37 the human stopped or objected to work he hadn't asked for; messages reached the wrong agent at least 17 times. The study stresses these are selected cases, not error rates.
- **Who did what:** the human more often requested, proposed, judged by looking, decided and stopped; agents more often built, measured and named causes. The requirements formed through results and failures, not in the first request.
- **Caveats it states itself:** one case, no control run, coded by models of the agents' own families, and commissioned by the creator, who sells the add-on to paying supporters.

## Thread highlights
> **@TheBigFlatNow1:** Creator here. Thanks for reposting :)

> **@AIDecoded0:** Most of those tokens are probably the same context getting read again and again. Every tool call is a new model call, and the agent sends the conversation so far each time. 17,453 calls on a growing context adds up fast.

> **@aplomb2:** Most of a number like that is usually cache reads. In our team's Claude Code traffic, 93–98% of input tokens were cache reads, which bill at 10% of the input price. The part that hurts is cache writes

> **@RJuju37898:** The interesting part of the project shown here isn't the final strawberry. It's the fact that you have a tool that can create a custom strawberry instantly.

> **@the53thcard:** You don't know about geometry nodes do you?

## Implications
- **Agents can build real Blender tools, not just one-off meshes:** the output is a reusable, parameterised geometry-nodes generator (cut-open interiors, randomised shapes, Off/Fast/Exact interior modes), which is the kind of asset a game or animation pipeline can reuse.
- **Visual verification stays human:** the recurring failure was agents reporting success on something that looked wrong. For 3D work, render-and-look checks (screenshots, turntables) need to be part of the loop, ideally fed back to the agent.
- **Headline token counts mislead:** cached context dominates; the cost that matters is cache writes and subscription limits, not the raw total.
- **Multi-agent overhead is real:** misrouted messages and agents doing unrequested work were a big share of recorded breakdowns, so fewer agents with clear lanes may beat many in parallel.
- **Experiment:** have a coding agent build a small procedural geometry-nodes generator (a rock or a plant) as a Blender add-on, require it to render a screenshot after every change and attach it to its report, and log how often its "done" disagrees with what the picture shows.

## Tags
`blender` `geometry-nodes` `procedural` `claude-code` `agent-workflow` `cost` `tokens` `verification` `3d`
