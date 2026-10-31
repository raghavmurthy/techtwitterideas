# Redesigning a "vibecoded" app screen with a design-reference MCP and skills

**X post:** https://x.com/jaimintf/status/2115839512828100690  
**Author:** jaimin (@jaimintf) · posted 2026-10-29 (UTC) · 2,619 likes, 38 replies  

## What it is
jaimin, founder of Appllama per his X bio, posts a 14-second video captioned "deslop any vibecoded app". It shows a study app's home screen being reworked step by step, with checklists beside the phone for spacing (gap, gutter, padding, width, corner radius), colour (canvas, shadow, button, accent), type (font and sizes) and symbols (tabs, icons, mascot), ending with a darker, more distinctive design and a new streaks block. In a reply he gives the prompt he used: use the Appllama MCP and skills and redesign the home screen with two named popular apps as references. Appllama's site describes itself as a library of 81,600+ screens from 1,770+ top-grossing iOS apps; the linked appllama-skills GitHub repo describes agent skills that turn those app patterns into native-quality mobile screens. Appllama is the author's own product, so this is a demo, not an independent test.

## Thread highlights
> **@jaimintf:** prompt: use appllama mcp & skills, redesign the home screen referencing go club & suno.

> **@kihaki:** Congrats your app now looks like ✨ vibecoded slop✨

> **@jmdevlabs:** So then all apps will look like the appllama design?

> **@aannuujX:** had paid for it, hardly does anything that it claims it does

> **@vladchai:** What is the difference from mobbin?

## Implications
- **Give the agent references, not adjectives:** "redesign like these two apps" plus a design-reference source gives the model concrete spacing, colour and type decisions to copy, which is where generic AI UI usually falls down.
- **Work in token passes:** the video's order (spacing, then colour, then type, then symbols) is a sensible checklist for any UI pass, including Unity UI Toolkit or uGUI menus.
- **Sameness risk:** replies worry every app will converge on the same look; references should be chosen for fit, not just popularity.
- **Experiment:** take one menu screen of a game, write its spacing, colour and type values into a small token file, then ask an agent to redesign it against two chosen reference apps, changing only one token group per pass. Compare before and after screenshots with a few players.

## Tags
`ui` `design` `mobile` `mcp` `skills` `ios` `vibe-coding`
