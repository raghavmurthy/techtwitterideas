# Pixel Match: local image-to-3D that keeps source pixels after retopo

**X post:** https://x.com/Bingeljell/status/2105364806379151765  
**Author:** Nikhil Shahane (@Bingeljell) · posted 2026-09-30 (UTC) · 574 likes, 20 replies  

## What it is
Nikhil (@Bingeljell) added a 'Pixel Match' feature to his open image-to-3dlab: it projects the actual source-image pixels onto the generated mesh, even after retopology to ~5k faces, so text, logos and fine detail survive. Output is low-poly, riggable and animatable. Runs locally on Mac + NVIDIA; he frames it as 'one step closer to Tripo / Meshy level', i.e. still behind commercial tools.

## Thread highlights
- @Bingeljell: “Perfect tree to bark up :D  Coth / armour / gear is all on my list - but it's something I want to pick up once I get multi-view and better topology done. Goal is this week.  I literally have a bunch of SIGGRAPH papers to go through. Best way to help is if you ”
- @Bingeljell: “Oh sweet! Thank you for this, checking it out. I was working on doing a custom paint via a Pixel Match so any models paint step wouldn't be required.”
- @henkjan: “Skipping paint in the model means your mesh quality has to survive without that correction pass covering topology errors the UV can't fix.”

## Implications
- Free, local route to low-poly (~5k face) game props that keep painted detail, text and logos, a common failure of open image-to-3D tools.
- Reprojecting detail after aggressive decimation is conceptually close to distillation/quantisation in model compression: keep the signal, drop the parameters.
- **Experiment:** run three concept images (prop, plant, character) through image-to-3dlab with Pixel Match, import at 5k faces into Unity or Godot, and compare readability and draw cost on a phone against a Meshy/Tripo export.

## Tags
`image-to-3d` `low-poly` `local-models` `blender` `asset-pipeline`
