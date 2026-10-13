# Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets

**Link:** https://www.scenario.com/explorations/iso-cycles/  

## What it is
A Scenario case study where Claude Code drove the Scenario MCP to make isometric pixel-art heroes with walk, run, idle and attack cycles in 8 directions. GPT Image 2.5 Sunburst drew two angles per hero (SE/NE), Kling V3 I2V animated each facing 'on a treadmill', and a local script cut the cleanest loop window, pixelated to a 24-28 colour palette and mirrored three directions (5 drawings for 8 directions). It documents what failed (back views turning to profile, invented hidden props, glow spill on the key colour) and the cost: ~4,194 credits over 150 runs.

## Thread highlights
- Not an X post; no thread.

## Implications
- One of the most reusable recipes here: an agent + generation MCP pipeline for consistent animation sheets, with prompts and scripts in a downloadable ZIP.
- Prompt lesson: describe what the camera keeps seeing (e.g. 'the chest is never visible'), not just the facing.
- **Experiment:** run the recipe for one character in 4 directions; budget credits first.

## Tags
`mcp` `claude-code` `sprites` `animation` `asset-pipeline`
