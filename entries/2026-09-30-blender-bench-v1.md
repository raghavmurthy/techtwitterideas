# Blender Bench v1: frontier LLMs on 20 real Blender workflows

**X post:** https://x.com/refresh_dev/status/2105359734287249559  
**Author:** Refresh (@refresh_dev) · posted 2026-09-30 (UTC) · 658 likes, 48 replies  

## What it is
@refresh_dev released Blender Bench v1, a benchmark of frontier LLMs on 20 realistic 3D production workflows (animation, modeling, rigging, cloth, surfacing). GPT-6 Astra leads overall; Claude Opus 5.5 wins modeling and cloth simulation.

## Thread highlights
- No notable replies came back from X search for this thread.

## Implications
- Suggests routing Blender MCP tasks by model: Opus 5.5 for modeling/cloth, GPT-6 Astra for broader workflows, rather than one model for everything.
- With only 20 workflows, rankings may flip under different scoring; treat as a hint.
- **Experiment:** run one real task (model + rig a small creature) through Blender MCP with both models and log time, retries and token cost.

## Tags
`blender` `benchmark` `mcp` `3d-agents`
