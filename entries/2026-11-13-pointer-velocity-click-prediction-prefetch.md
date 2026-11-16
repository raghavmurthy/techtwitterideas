# Predicting the next click from pointer velocity, then prefetching on it

**X post:** https://x.com/JohnPhamous/status/2121305863449366854  
**Author:** John Phamous (@JohnPhamous) · posted 2026-11-13 (UTC) · 3,834 likes, 125 replies  
**Follow-ups:** https://x.com/ndrewpignanelli/status/2121367321298276658 (prefetch benchmark, 3,346 likes) · https://x.com/Bart_Spaans/status/2121539365696385246 (existing library)  
**Source:** https://github.com/spaansba/ForesightJS (ForesightJS, an open-source intent-prediction library)

## What it is
John Phamous, who lists Vercel in his X bio, posted a short demo of a UI that uses the pointer's velocity to predict which button the user is about to click, before the cursor reaches it.

Andrew Pignanelli (@ndrewpignanelli), CEO of @intelligenceco per his X bio, quoted it with the idea of using the prediction for prefetching, and posted a small results table from his own test of page loads:

- No prefetch: median 776 ms, p95 823 ms
- Hover prefetch (the current approach): median 667 ms, p95 733 ms
- Hover plus pointer prediction: median 400 ms, p95 601 ms

So in his test, starting the fetch on the predicted target instead of on hover cut the median by roughly 40 percent compared with hover alone. Only the table was shared, not the test setup, so treat the numbers as one person's measurement.

Replying to him, Bart Spaans (@Bart_Spaans), creator of ForesightJS per his X bio, pointed out that a library for this already exists. According to its README, ForesightJS predicts user intent to prefetch content before it's needed, starting earlier than hover prefetching and loading less than viewport prefetching. On desktop it uses mouse trajectory, keyboard navigation and scroll; on touch devices, where there is no cursor, it falls back to viewport-enter and touch-start events. It ships a framework-agnostic core plus React, Vue, Angular and Astro packages, and dev tools that draw the predicted trajectory and element bounds.

## Thread highlights
> **@ndrewpignanelli:** thought: "oh you could use this for prefetch" and tested it... holy shit

> **@Bart_Spaans:** I made [ForesightJS] a while back! Let me know if anything is missing/unclear

> **@danbillson:** surely this could be a behaviour in ui sdk

> **@aarondelasy:** that's a brilliant idea, we now need a lib for this

> **@plzreturnmy_cd_:** honestly i'd make it a cone just in case

> **@Lucasdickey:** I took some inspiration from you here on velocity and friction associated with an interactive flipboard animation I'm working on.

## Implications
- **Latency hiding is a design tool, not only an infra one:** in that one test, predicting intent saved about 270 ms at the median over hover prefetch, which is more than many backend optimisations give. Any UI that loads something on click (store pages, level select, asset previews) can start the work as soon as the intent is likely.
- **Game menus and editors:** in a Unity or web game, the same idea applies to warming up the next screen: begin loading an Addressables bundle, a scene or a thumbnail set when the pointer is heading toward a level tile, and cancel if it veers away. Players feel menus as "instant" without the full asset being resident.
- **Mobile has no pointer:** on phones the useful signals are viewport entry and touch start, as ForesightJS does.
- **Budget the misses:** prediction means some fetches are wasted. Keep prefetches cheap (metadata, compressed thumbnails, low-poly previews) and load the full-quality asset only on confirm.
- **Agent-built UIs:** if agents generate the UI, intent prefetching is a behaviour to ask for explicitly, since it won't appear by default.
- **Experiment:** in one menu with at least six targets, log time from click to fully drawn for three variants (no prefetch, prefetch on hover or pointer-enter, prefetch on predicted target from pointer velocity) over 50 clicks each, and also count wasted prefetches. Keep the variant only if the median gain is clear and the wasted bytes stay small.

## Tags
`ui` `performance` `web` `prefetch` `prediction` `open-source` `game-dev` `mobile`
