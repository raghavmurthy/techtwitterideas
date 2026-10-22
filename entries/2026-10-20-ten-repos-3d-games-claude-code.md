# 10 free repos for building 3D games with Claude Code

**X post:** https://x.com/doncoderlione/status/2112638459089150151  
**Author:** Don Coderlione (@doncoderlione) · posted 2026-10-20 (UTC) · 1,992 likes, 19 replies  

## What it is
A Turkish-language list of ten open-source projects the author says shorten AI-assisted 3D game development (links are in the original post):

1. **Gamedev Agent Skills:** 74 game-dev skills with a router that detects the engine (Godot, Unity, Unreal, Phaser, PixiJS, three.js, Bevy, pygame, LÖVE, Roblox) and loads the matching skill; works across Claude Code, Cursor, Codex, Copilot and Gemini CLI.
2. **MCP Unity:** connects an agent to the Unity Editor to build scenes, change objects, assign materials, run tests and read console errors.
3. **Godot MCP:** the same for Godot: create scenes, add nodes, run the project, read debug output.
4. **TripoSR:** single image to 3D model; the author says it's for prototyping props, not final assets.
5. **Drei:** ready-made React Three Fiber helpers (camera controls, environment, sky, shadows, model loading).
6. **React Three Rapier:** rigid bodies, collisions and joints without writing a physics engine.
7. **Yuka:** NPC behaviour: steering, pathfinding, perception, state machines.
8. **three.quarks:** particles for three.js (sparks, smoke, magic trails) with a visual editor.
9. **React Postprocessing:** bloom, depth of field, grain and vignette; the author calls it the layer that stops a game looking "cheap".
10. **Colyseus:** multiplayer rooms, matchmaking, reconnection and automatic state sync.

The author says in a reply (translated) that he used Unity MCP and the gamedev agent skills on his last game and plans Colyseus for its online architecture.

## Thread highlights
> **@doncoderlione:** Son oyunumda unity mcp ve gamedev agent kullandım. Online mimarisi için de colyseus u kullanacağım

> **@CodingAndSuch:** 3-4 skills max. Anything else is overkill

> **@itsthedonhashim:** watch out for feature creep! easy to get carried away adding stuff to your game when these tools make it so quick.

## Implications
- **Unity:** MCP Unity plus an engine-aware skill pack is the closest thing to a ready-made agent setup for Unity scenes; worth comparing against any in-house editor bridge.
- **3D pipeline:** TripoSR is positioned for blockout props only, which fits a low-poly workflow where final assets are hand-cleaned in Blender.
- **Agent workflows:** one reply argues for 3–4 skills at most; a 74-skill pack relies on its router to avoid flooding context, so test whether it actually loads only one skill at a time.
- **Experiment:** install MCP Unity in a throwaway project and have an agent build a small test scene (terrain, three props, one material swap, one play-mode test), timing it against doing the same by hand.

## Tags
`game-dev` `unity` `godot` `threejs` `mcp` `skills` `open-source` `resources`
