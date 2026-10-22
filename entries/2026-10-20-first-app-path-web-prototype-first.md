# Starting a first app today: web prototype first, one flow at a time

**X post:** https://x.com/PrajwalTomar_/status/2112521739976716525  
**Author:** Prajwal Tomar (@PrajwalTomar_) · posted 2026-10-20 (UTC) · 90 likes, 4 replies  

## What it is
The author, who runs a mobile app studio, summarises a thread by a developer who says he has built apps since 2009 and shipped 100+ apps with about 6M organic downloads, describing the path he'd follow if starting today. The steps as summarised: pick a category someone already validated and find your angle, since demand, pricing and complaints are already visible; build a quick web prototype in about two days and test it with real users for a week before building the real app; map the app flow by flow on paper (onboarding, sign-up, payments, the core) and write the spec with Claude; choose a builder where you plug in your own model and keep your code instead of paying credits forever; and build one flow at a time, never the whole app in one prompt, expecting about 30% of the time to go to debugging. The author adds that prompting a whole app at once feels great for a day and then costs weeks of fixes, and advises getting it in front of 5 or 6 TestFlight users before launch. The original thread wasn't read here.

## Thread highlights
> **@RuthlessCaine:** the step id add is day one, not after launch: open the short video accounts the same week as the web prototype. by the time the app ships you already know which hook gets people to click

> **@tsubasaaix:** The one-flow-at-a-time rule seems to apply outside code too. Is the launch version of that mistake trying to market to everyone at once

## Implications
- **Mobile games:** a browser build of the core loop (WebGL or three.js) is a fast way to test whether the mechanic is fun before committing to a native Unity build and store submission.
- **Agent workflows:** "one flow per prompt" matches what works for agents: small, testable slices rather than one huge generation.
- **Experiment:** build a two-day web prototype of one core mechanic, share it with five people, and decide from their play sessions whether to start the native build.

## Tags
`launch` `mobile` `prototyping` `vibe-coding` `agent-workflow`
