# Concept art to playable 3D world via blockout + painted projection

**X post:** https://x.com/hakimieiqbal/status/2111428789272019234  
**Author:** Hakimi Eiqbal (@hakimieiqbal) · posted 2026-10-17 (UTC) · 1162 likes, 41 replies  

## What it is
@hakimieiqbal describes a pipeline: GPT generates a cel-shaded village concept; Opus 5.5 rebuilds the layout with simple 3D blocks and screenshots it from a fixed camera; GPT paints over the blockout using the concept art as reference; Opus writes a shader that projects that painting back onto the geometry. The result keeps the illustration's look but is walkable, and the same steps were repeated for interiors. Characters were generated with GPT Images and animated with Minimax H3. A reply questions whether the H3 animations are real rigged animation or limited video-based motion.

## Thread highlights
> **@blightwork:** H3 creates all of the walking, idle and action animations for every character? I thought it just was good for video. I'm guessing nothing is rigged and it's pretty limited?

## Implications
- A fast way to get a specific 2D art direction into a walkable low-poly scene without modeling every detail; projection holds best near the painted camera angle.
- Pairs naturally with Blender/Unity agent loops: the agent does blockout and shader, the image model does paint-over.
- **Experiment:** take one concept painting, have an agent block it out in Unity or Blender, paint over a fixed-camera screenshot, and project it back; check how far the camera can move before stretching shows.

## Tags
`3d` `asset-pipeline` `shaders` `concept-art` `claude`
