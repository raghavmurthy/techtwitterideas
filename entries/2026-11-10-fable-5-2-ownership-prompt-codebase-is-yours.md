# Tell the model the codebase is its own: Anthropic's ownership tip for Fable 5.2

**X post:** https://x.com/simonw/status/2120029347948220500  
**Author:** Simon Willison (@simonw) · posted 2026-11-10 (UTC) · 4,710 likes, 430 replies  
**Source:** https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5-2 (Anthropic's prompting guide for Claude Fable 5.2, section "Say who owns the code")

## What it is
Simon Willison, creator of Datasette and co-creator of Django per his X bio, pointed to a tip in Anthropic's new prompting guide for Claude Fable 5.2: telling the model that the codebase is its own makes it less cautious about improving existing code.

The guide explains the behaviour. In Anthropic's testing on small coding tasks, Fable 5.2 tended to add to the existing structure when the prompt said nothing about ownership or framed the code as someone else's, even when that meant duplicating code. When the prompt said the code was the model's own, it often consolidated duplicated code and sometimes made related fixes without being asked. Anthropic reports that duplicated code was merged into one shared function in under 10 percent of runs without the ownership sentence and in about 75 percent of runs with it. The guide's recommended sentence says the model is the owner and long-term maintainer of the codebase and that its design is up to it.

In a follow-up the next day, Willison noted that Anthropic had changed the recommended wording from the shorter "this codebase is yours" to that longer owner-and-maintainer sentence. He also remarked that the guides make it clear Anthropic is as surprised by its new models' quirks as everyone else.

Replies mostly agree, with a consistent caveat: ownership without limits means the model may refactor things you rely on, so pair it with tests and clear boundaries.

## Thread highlights
> **@simonw:** Huh, they've changed the recommended prompt to "You are the owner and long-term maintainer of this codebase, and its design is up to you."

> **@simonw:** Something I enjoy about these prompting guides is that it's VERY clear from reading them that Anthropic are just as surprised by the idiosyncrasies of their new models as we are

> **@muhdarifx:** "Be careful" in a prompt tends to read as "change as little as possible." I'd pair "this codebase is yours" with a hard fence though: tests must pass and no public API changes without asking. Ownership plus limits.

> **@orionxaus:** the timid default is why you get a new helper sitting next to the old one instead of the old one fixed. id pair it with 'run the tests before and after' so owning it doesnt turn into rewriting it

> **@LLMpsycho:** the caveat below that tip is doing some work: about 1.5x output tokens and occasional unrequested behavior changes. worth testing on a branch before making it the default.

> **@NoahDorfman:** curious if it holds up when there's one thing it truly can't touch, like a data format already sitting on users' phones. "this codebase is yours" plus a short no-go list feels like the right combo

## Implications
- **Duplicate helpers are a symptom of framing:** if an agent keeps adding a second utility next to an existing one, the prompt may be telling it the code isn't its to change. An ownership line in the project instructions file targets that directly.
- **Ownership needs a fence:** combine the ownership sentence with a short no-go list (save-file formats, public APIs, network protocols, anything already on players' devices) and a rule that tests must pass before and after.
- **Unity and game code:** gameplay projects accumulate near-duplicate MonoBehaviours, input handlers and UI scripts. An agent that consolidates them is useful, but serialized fields and prefab references break silently when scripts are merged or renamed, so list those as untouchable.
- **Asset and compression scripts:** Blender export and mesh-compression scripts tend to be copy-pasted per asset type; an agent told it owns the pipeline is more likely to merge them into one parameterised tool.
- **Experiment:** pick one small refactor task with known duplication (for example two similar Unity editor scripts), run it twice on separate branches, once with no ownership line and once with the guide's owner-and-maintainer sentence plus a three-item no-go list. Compare whether duplication was merged, the diff size, token use, and whether tests and prefab references still work.

## Tags
`prompting` `claude` `agent-workflow` `refactoring` `code-quality` `unity` `testing`
