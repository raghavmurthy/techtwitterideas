# DeepSeek V4.1 Flash vs Opus 5.5 on a one-prompt 3D Bowser test: $0.15 vs $3.85

**X post:** https://x.com/luckeyfaraday/status/2111522732668035503  
**Author:** Luckey Faraday (@luckeyfaraday) · posted 2026-10-17 (UTC) · 3,177 likes, 153 replies  

## What it is
A side-by-side video of DeepSeek V4.1 Flash and Claude Opus 5.5 each generating a 3D Bowser model in code from the same prompt. The headline is cost: $0.15 for DeepSeek versus $3.85 for Opus. The video itself wasn't reviewed here; replies describe both results as recognisable, with DeepSeek's shell denser and spikier and Opus's smoother. One reply notes DeepSeek used about twice the tokens and took about nine minutes longer but was still far cheaper.

## Thread highlights
> **@0ddscent:** the detail I keep staring at: DeepSeek used about twice the tokens and took 9 minutes longer, and it still cost $0.15.

> **@GideonEightySix:** I will say USE DSH harness, not anything else. it was weird that i got better results out of the harness.

> **@SuchCoolName:** Do Blender mcp

## Implications
- **3D / game dev:** for code-generated 3D (three.js scenes, procedural props), a cheap open model may be good enough for drafts, with a frontier model saved for the final pass.
- **Agent workflows:** the slower, token-heavier model still won on cost by about 25x, so latency, not price, becomes the trade-off for batch asset jobs.
- **Model choice:** one reply says the harness mattered as much as the model, so compare like for like.
- **Experiment:** run five low-poly prop prompts (barrel, crate, lantern, tree, rock) through both models in the same harness, export to glTF, and score them on polygon count, visual quality and cost per usable asset.

## Tags
`3d` `models` `cost` `benchmarks` `deepseek` `claude` `asset-pipeline`
