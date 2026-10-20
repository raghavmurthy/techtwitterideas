# How to be more ambitious with models: altitude, depth and range (plus a /be-ambitious skill)

**Link:** https://felixrieseberg.com/how-to-be-more-ambitious-a-tutorial-for-humans-with-models/  
**Author:** Felix Rieseberg (@felixrieseberg) · published 2026-10-13 · builds things at Anthropic and co-maintains Electron, per his X bio  
**Related X post:** https://x.com/daniel_mac8/status/2110820874890719723 · Dan McAteer (@daniel_mac8) · posted 2026-10-15 (UTC) · 1837 likes, 32 replies  
**Skill:** https://github.com/DannyMac180/skills/tree/main/be-ambitious  

## What it is
Rieseberg's essay turns the common "we're not ambitious enough with AI" line into a method. He splits ambition into four types. **Speed** (the same work, faster) he skips as obvious. **Altitude** means asking for the outcome rather than the task: he went from asking Claude to fix individual crashes to asking it to keep the apps crash-free, which first meant giving it crash reports, a version-to-commit map and machines to reproduce bugs on. **Depth** means making the model use the tools and raw data an expert would use (databases and statistical models instead of markdown tables), setting unreasonable targets (200 ms, not 5 s), adversarially checking assumptions against raw data, trying to produce new knowledge, and always using an outside judge rather than self-grading. **Range** means pulling in other fields: describe the task with verbs instead of nouns, then "assemble the crew" of disciplines that would help. Ask the model to do what, say, a short seller does to research, not to write like one. His depth technique is a short prompt that asks the model, before rewriting a task, to say what a top professional would do, what raw material they'd start from, which methods and tools they'd use, and what outside check would prove the result right. He closes on self-efficacy: people achieve more when they believe hard things are possible. Dan McAteer, an AI agent builder who writes for Latent Space per his X bio, packaged that four-step prompt as a free /be-ambitious skill. Replies split between people who found it made agents think deeper and people warning it over-engineers code.

## Thread highlights
> **@kaiscale:** FWIW, it produces over-engineered code -- so maybe not good for coding, but probably good for brainstorming, as long as you don't use it in the first pass.

> **@NNaumovsky:** Step 4 is the one that matters most. Ambition without a proof step just gives you bigger, more confident mistakes.

> **@daniel_mac8:** Take a simple idea, and take it very seriously.

## Implications
- Altitude is about environment: an agent can only own an outcome if it can fetch the data and verify fixes itself, so build that access first.
- Depth fits 3D and game work well: ask what a technical artist would start from (reference photos, scan data, engine profiler captures) and what objective check proves it (triangle counts, frame time, texture memory) instead of accepting "looks good".
- Range is a cheap way to find new angles. Example: describe a level as "teaching the player one mechanic without text" and bring in a puzzle designer, a sound designer and a UX researcher.
- Use the skill for planning and brainstorming, and keep a narrower prompt for the actual code changes.
- **Experiment:** take one asset-optimisation task (e.g. "make this Unity scene run at 60 fps on mobile"), run it once plainly and once with the four depth questions first, then compare which version used profiler data and an outside measurement and what frame time each reached.

## Tags
`prompting` `skills` `agent-workflow` `claude` `quality`
