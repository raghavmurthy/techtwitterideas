# CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive

**X post:** https://x.com/RoundtableSpace/status/2110645603029889500  
**Author:** 0xMarioNawfal - The Roundtable Show (@RoundtableSpace) · posted 2026-10-15 (UTC) · 561 likes, 55 replies  
**Repo:** https://github.com/HKUDS/CLI-Anything  

## What it is
CLI-Anything, an open-source project from HKUDS (University of Hong Kong data science lab), wraps desktop software in a command-line interface that coding agents can operate instead of clicking through a GUI. Ready-made wrappers exist for GIMP, Blender, LibreOffice and Calibre, plus a growing set of community ones. CLI-Hub works like an app store for these agent-ready tools, and a plugin can generate a CLI for an app that doesn't have one yet. It works with Claude Code, Cursor, Codex and others, but the real app still has to be installed. The post cites 52K+ GitHub stars and an Apache-2.0 license. (The post includes install commands; they're not reproduced here.)

## Thread highlights
> **@agentreadystack:** Desktop apps behind a CLI is the right abstraction. Agents already speak shell; they don't speak mouse. The risk is blast radius: once GIMP and LibreOffice are "just commands", you need the same deny-by-default you use for rm -rf.

> **@mlangXie:** Before giving an agent GIMP or Blender via CLI-Anything, I'd have it print the exact argv and the target file before each run. Desktop apps open your real files, not a sandboxed repo copy.

> **@zzyuw96:** Wrapping GUIs as CLIs is such a clean pattern for agents — text in, text out, easy to log and replay.

## Implications
- Text-in, text-out control is cheaper in tokens and easier to log and replay than screenshot-and-click agents, and it lets you diff what changed.
- For Blender pipelines it's an alternative to an MCP server: batch jobs like decimation, UV unwrapping, format conversion and turntable renders become scriptable commands an agent can chain.
- For compression and asset optimisation, the same wrappers can drive the steps around a model (texture resize in GIMP, mesh decimation in Blender) in one logged pipeline.
- Run it on copies of files, with a dry-run or print-the-command step before anything destructive, as the replies suggest.
- **Experiment:** have an agent use the Blender wrapper to take five high-poly props, decimate each to a triangle budget, bake a normal map, and export GLB; compare file sizes and render a before/after contact sheet.

## Tags
`blender` `agent-tooling` `agents` `cli` `open-source` `asset-pipeline` `compression`
