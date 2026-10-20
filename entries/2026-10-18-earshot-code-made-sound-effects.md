# earshot v0.3: 201 code-made sound effects, timed to the exact frame

**X post:** https://x.com/LexnLin/status/2111927727318245426  
**Author:** Leon Lin (@LexnLin) · posted 2026-10-18 (UTC) · 5844 likes, 116 replies  
**Repo:** https://github.com/Leonxlnx/earshot  

## What it is
earshot is a local tool (CLI, Python API and MCP) that designs sound effects in code and checks them by measurement instead of using a generative audio model, running on CPU. Version 0.3 adds a library of 201 procedurally made sounds (whooshes, impacts, UI clicks, taps, pops, dings, typing, glitches, logo stings), "earshot kit" to generate a whole matching sound kit, and an improved "earshot sfx" that places a sound's measured onset or peak on an exact video frame. It now powers the audio in cinetic, the same author's agent skill for code-made motion design (Remotion or HyperFrames), where one timeline file drives both picture and sound so every hit lands on its frame. The cinetic docs favour restraint: one soft sound per text fragment, near-silence while it is read, and one big hit for the reveal.

## Thread highlights
> **@colinarms:** We've struggled w/ stock Opus 5.5-generated sound effects for our videos at @paragraph_xyz. Gave it a try w/ Earshot and it sounded much better!

> **@stupidhumandev:** I spent 15 years as a sound designer - I presumed no one had cracked this sort of thing yet.

> **@WildHoney_xy:** For motion work, I'd put repeatable timing ahead of a bigger sound catalog. Keeping a cue attached to the right event through revisions is the part I'd want to stress-test.

## Implications
- Procedural, parameterised SFX are tiny compared with recorded WAV libraries: a sound kit stored as parameters plus a renderer is a form of audio compression, and variations come free.
- For game dev, a code-made kit gives consistent UI and feedback sounds, and measured onsets help line sounds up with animation events in Unity.
- For agent-made trailers and devlogs, pairing it with Remotion or HyperFrames means picture and sound come from one cue list, so re-edits don't break sync.
- **Experiment:** generate a small UI kit (click, hover, confirm, error, coin) with earshot for a Unity prototype, compare total size against an equivalent stock WAV pack, and wire each sound to an animation event to check frame-accurate timing.

## Tags
`audio` `sfx` `motion-graphics` `game-dev` `mcp` `compression` `open-source`
