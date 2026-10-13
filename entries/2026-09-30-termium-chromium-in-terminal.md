# Termium: Chromium inside the terminal (OSS, MIT)

**X post:** https://x.com/codr_1/status/2105265191986598158  
**Author:** Vess Bakalov (@codr_1) · posted 2026-09-30 (UTC) · 547 likes, 48 replies  

## What it is
@codr_1 released Termium, which renders real Chromium pages and tabs inside a terminal with keyboard control, open source under MIT (termium.dev). He says it took a couple of years on and off; replies mention Sixel encoding as the hard part.

## Thread highlights
> **@codr_1:** Mostly life. It honestly was more off than on. But. Sixel encoding is not the faint of heart. Also - I kept hoping Chromium would open more APIs exposing the frame buffer. Right now I am basically doing a screenshot and it is slow. Playing with some vide…

> **@francorobles:** I can see a smooth interaction between a cli and this or I could be wrong.

> **@brubiscoitinho:** chromium in a terminal for 2 years on and off, respect. was the latency or the rendering that ate most of the time?

## Implications
- Could let headless coding agents view a web page (e.g. a WebGL game build) over SSH without a desktop.
- **Experiment:** try Termium over SSH on a WebGL build and check whether it works for an agent screenshot loop.

## Tags
`terminal` `browser` `agent-tooling`
