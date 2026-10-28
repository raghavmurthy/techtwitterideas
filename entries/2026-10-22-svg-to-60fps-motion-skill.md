# A Claude skill that turns an SVG into a 60 fps animation

**X post:** https://x.com/rossark0/status/2113149312163045837  
**Author:** ROSS (@rossark0) · posted 2026-10-22 (UTC) · 2,041 likes, 59 replies  

## What it is
An app builder shares a personal agent skill, `rossark-motion-skill`, that he says turns any SVG into a polished 60 fps animation, framed as a lighter alternative to Rive for making an app "feel alive". The demo is a video, which wasn't reviewed here. In replies he says the result is made with just Claude plus the skill (no other tool), that it is his own skill rather than a third-party product, and that the example is only a demonstration: you can draw and animate anything with it. A separate quote post by the same author adds only that it is "insane". The post does not link a public repo for the skill, so availability is unclear.

## Thread highlights
> **@rossark0:** Just claude + /rossark-motion-skill

> **@rossark0:** i mean, yeah. but i just used it as an example. you can draw and animate anything with it.

## Implications
- **UI polish for small teams:** an agent writing SVG and animation code directly can cover menu, loading and onboarding micro-animations without a dedicated motion tool.
- **Mobile and Unity:** vector animations are cheap to ship; the same idea could produce animated UI icons or splash art that is exported to sprite sheets or vector-animation formats for a game's menus.
- **Make your own:** since the skill itself isn't published, the transferable idea is the pattern: a skill that fixes frame rate, easing rules and file format so every generated animation is consistent.
- **Experiment:** write a short skill that tells your agent to take one SVG icon and output a 60 fps looping animation with fixed easing and duration rules, then compare its file size and smoothness with a hand-made Lottie or Rive version of the same icon.

## Tags
`skills` `animation` `svg` `ui` `mobile` `claude-code`
