# Genex 0.1.10: an open-source desktop app for making games with any AI, now on Windows

**X post:** https://x.com/genex_games/status/2112276766718845024  
**Author:** Genex (@genex_games) · posted 2026-10-19 (UTC) · 1,036 likes, 27 replies  
**Link:** https://genex.games/desktop  

## What it is
Genex announces version 0.1.10 of its open-source desktop app for making games with any AI model, now available on Windows. In replies the team describes it as a harness built specifically for game creation that works with any AI subscription or a local model, learns from each run, ships built-in plugins for Unity, Unreal, Godot and Blender, and routes game-dev work (3D models, animation, sound) to suitable tools. They say you could wire most of it yourself with Claude Code and a Godot MCP, but Genex does it out of the box: it installs Godot, the agent plays and screenshots the game, generates 3D models and sounds, and a team of agents tests and improves the game for hours.

## Thread highlights
> **@genex_games:** It's a harness built especially for making games with any AI sub or local model.

> **@genex_games:** You can wire most of it yourself with Claude Code + a Godot MCP. Genex gives it out of the box: it installs Godot, the agent plays and screenshots the game, makes 3D models and sounds, and a team of agents tests and improves it for hours.

> **@onemanarmy85:** Ive had terrible results with it uven when using tripo any resource where i can learn best przctices?

> **@devheb:** The description and docs need an update!

## Implications
- **Game dev:** the "agent plays and screenshots its own build" loop is the key idea; it gives the model visual feedback instead of only compiler output.
- **Unity/Blender:** built-in Unity and Blender plugins make it a candidate for comparison with a custom Claude Code setup, but one user reports poor results with generated 3D, so treat it as early software.
- **Local models:** support for local models matters for long autonomous test runs where API cost adds up.
- **Experiment:** give Genex and a plain Claude Code + engine MCP setup the same one-screen game brief, cap both at an hour, and compare playability and how many fixes each needed.

## Tags
`game-dev` `agents` `open-source` `unity` `godot` `blender` `local-models`
