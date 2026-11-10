# Two codebase audit prompts: implicit state machines and unenforced invariants

**X post:** https://x.com/joshpuckett/status/2118942637688512989  
**Author:** joshpuckett (@joshpuckett) · posted 2026-11-07 (UTC) · 3,180 likes, 30 replies  
**Quotes:** https://x.com/steveruizok/status/2116552016218710389 (Steve Ruiz, @steveruizok, founder of tldraw per his X bio · 2026-10-31 · 8,386 likes)

## What it is
Two one-line prompts for a coding agent that ask it to audit a whole codebase rather than build something. Steve Ruiz posted the first: ask the agent to find all of the implicit state machines in the app. Josh Puckett, a designer, investor and advisor per his X bio, quoted it and added a second: ask the agent to find every invariant the app relies on but doesn't explicitly enforce.

An implicit state machine is behaviour that switches between modes (loading, editing, idle, error) but is spread across separate booleans, nullable fields and if-statements instead of one named state with defined transitions. An unenforced invariant is a rule the code assumes is always true, such as "the current step is never higher than the total", that nothing actually checks. Both are places where impossible combinations can sneak in, and both are hard for a human reviewer to spot because they are spread across many files. An agent that can read the whole codebase is well suited to listing them.

The replies are mostly people who ran the prompts and found them useful, plus a warning that the output is a list of candidates, not a list of bugs.

## Thread highlights
> **@jamonholmgren:** Hold my beer, I'm going in

> **@matthiasforstr:** invariant my recipe app relied on: the current step is never higher than the total. enforced by: nothing. discovered when it showed step 9 of 6.

> **@entrptaher:** I tried that one and found 400+ potential issues. I wonder how much I'll find with yours.

> **@archvalmiki:** Implicit state machines are logic that behaves like a state machine (different modes/behaviors that switch based on events) but is scattered across flags, ifs, variables, and event handlers instead of being explicit.

> **@Valuable:** I can't imagine how many projects right now are getting absurd levels of overkill explicit scaffolding structured around the most benign harmless "implicit states" just because some prompter was like "…fix it?!"

> **@kewinversi:** Nice! And what do you do with the invariants? «Fix it»?

## Implications
- **Audit, then triage:** these prompts produce a report, not a fix. One reply found 400+ candidates; most will be harmless. Rank by what breaks for a user (corrupted saves, stuck UI, wrong totals) and only convert the dangerous ones.
- **Games are full of implicit state:** player controllers, UI flows, dialogue, save/load and network sync often run on loose flags like `isJumping`, `isPaused`, `isLoading`. Unity projects especially tend to grow these across MonoBehaviours, coroutines and animator parameters, which an agent can cross-reference faster than a person.
- **Turn findings into checks, not just refactors:** an invariant that matters can become an assertion, a validation on load, or a test, which is cheaper than restructuring everything into explicit state machines.
- **Asset pipelines too:** Blender export and model-compression scripts rely on unstated rules (applied transforms, single UV set, triangle budgets, power-of-two textures). The invariant prompt can list them so they become pre-export checks.
- **Experiment:** run both prompts read-only on one Unity project (or one gameplay system), ask for the top 10 findings ranked by player-visible impact with file references, then fix only the top three: one explicit state enum, one runtime assertion, one test. Track whether related bug reports drop over the next two weeks.

## Tags
`prompting` `agent-workflow` `code-quality` `state-machines` `testing` `unity` `game-dev` `refactoring`
