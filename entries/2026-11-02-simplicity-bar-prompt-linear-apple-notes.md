# Naming a simplicity bar in a UI prompt: "as simple as Linear's site or Apple Notes"

**X post:** https://x.com/Voxyz_ai/status/2117281830449942825  
**Author:** Vox (@Voxyz_ai) · posted 2026-11-02 (UTC) · 5,927 likes, 137 replies  

## What it is
A short prompt the author suggests giving a coding agent before building a new website or app. It names two well-known products as the quality bar and asks for simplicity at every layer: purpose, architecture, design and implementation. It then tells the agent to cut decorative copy such as taglines and helper text. The text available through the public API is truncated after that point, so the full list of cuts isn't covered here.

> **@Voxyz_ai:** "I want this to be as perfect as Linear's website or Apple Notes: simple purpose, simple architecture, simple design, simple implementation. Cut taglines, helper text…"

The replies split between people who found naming a reference useful and people who called the post engagement bait with thin results. The most useful pushback is that some helper text carries real information and shouldn't be cut blindly.

## Thread highlights
> **@OnFinality:** Naming a reference like that does more than a pile of adjectives. It gives the model a bar to hit instead of a vibe to imitate.

> **@Torerone:** Cut taglines and helper text is such a good line to give it. Most AI built sites look AI because they have 10 sections saying the same thing, and simple is honestly harder to get out of it than busy.

> **@withtimon:** Sometimes the helper text is the product. 'Only you can see this' or 'This will send an email' carries information the layout can't supply. I'd cut repeated instructions before cutting consequences.

> **@Sandip_Lawate:** agree on cutting clutter. just wouldn't remove helper text blindly, sometimes one clear line saves the user a lot of guessing.

> **@thetiktokwiz:** this applies to ecommerce stores too. clean design is great, but people should never have to guess what the product does or where to buy it

> **@Halfcycleai:** "Simple architecture" in a prompt is a wish the agent grades itself on. Simple comes from deciding what the app is for before any code, then a reviewer that did not write it saying no.

## Implications
- **References beat adjectives:** naming a concrete product as the bar gives an agent something to compare against, which is more useful than words like "clean" or "modern". The same works for game UI: name the menu or HUD style you want matched.
- **Cut repetition, keep consequences:** the strongest reply draws a useful line. Remove taglines and repeated instructions, but keep the one-line notes that explain what an action will do (sends an email, deletes a save, spends currency).
- **Simplicity needs a check, not just a wish:** an agent will happily claim it built something simple. A separate review pass, or a second model that didn't write the code, is a better test than the prompt itself.
- **Experiment:** take one existing settings or store screen in a mobile or Unity UI and ask an agent for two redesigns, one with a plain "make it clean" prompt and one naming a specific reference product plus "cut taglines and repeated helper text, keep any text that explains a consequence". Compare the element count, the copy that was kept and how quickly a first-time tester completes one task on each.

## Tags
`prompting` `ui` `design` `vibe-coding` `agent-workflow` `claude-code` `codex`
