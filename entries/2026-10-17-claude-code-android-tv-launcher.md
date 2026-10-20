# Claude Code replaces an ad-heavy Android TV launcher

**X post:** https://x.com/gathint/status/2111379569030939102  
**Author:** Gathin (Ø,G) (@gathint) · posted 2026-10-17 (UTC) · 18108 likes, 471 replies  

## What it is
@gathint gave Claude Code a TV's model number; it found the TV on the local network, removed 25 manufacturer packages that showed sponsored ads before Netflix, and wrote a new launcher that looks like Apple TV's. In a self-reply he published the prompt, launcher source and the gotchas he hit (github.com/Gathin23/tv-vibehack), says it works on any Android TV / Google TV and that everything is reversible.

## Thread highlights
> **@gathint:** Prompt, launcher source and the gotchas I hit are all here. works on any Android TV / Google TV, everything is reversible

## Implications
- A clear example of agents doing device-level work over the network with adb-style access, and of why reversibility should be designed in.
- Same pattern applies to test devices for mobile games: an agent can set up a clean Android test device.
- **Experiment:** on a spare Android device, have an agent strip preinstalled bloat and install a game build, logging every change so it can be undone.

## Tags
`claude-code` `android` `devices` `agents`
