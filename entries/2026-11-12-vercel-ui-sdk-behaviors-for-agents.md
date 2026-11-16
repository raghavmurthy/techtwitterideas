# Vercel's UI SDK: accessible behaviours as primitives, for agents to compose into components

**X post:** https://x.com/vercel/status/2120950020249895314 (with a follow-up linking the repo: https://x.com/vercel/status/2120950032014963054)  
**Author:** Vercel (@vercel) · posted 2026-11-12 (UTC) · 6,517 likes, 215 replies  
**Source:** https://github.com/vercel-labs/ui (Apache-2.0, beta, about 5,000 GitHub stars at time of writing)

## What it is
Vercel announced the UI SDK with a short demo video and a follow-up post linking the repository. The README calls it "a library of behaviors for agents to build the next generation of user interfaces."

Instead of shipping finished components, it ships behaviours: keyboard navigation, focus, selection, dismissal, popups, drag and drop, and the ARIA attributes each needs, all in a core package with adapters for React, Vue, Svelte, Solid and Web Components. A component is defined once as a primitive (its state, its API and its named parts, or "slots"), then rendered in any of the five frameworks with the same parts. The README's example splits an environment selector into three behaviours: a popup, a selection and a typeahead.

The pitch is explicitly aimed at coding agents: the README says you don't need to learn how to write primitives because your agents will, and it provides an agent skill for that. It is in beta under Vercel's beta terms, so the API may change.

## Thread highlights
> **@iamrakhmatov:** Because the same behavior is shared between multiple components, so instead of creating 10 component primitives you create 2 behavior primitives so that agent could create that 10 component primitives itself and then build the actual UI component composing them together.

> **@salleedesign:** But what's the difference with just taking a shadcn base component (or any other) and build your own component from there? I still don't get the value for this.

> **@Ritchie40652966:** I have One shotted an ecommerce port. Really inpressed. Ui SDK Is awesome. Vue support Is what its makes perfect.

> **@danbillson:** surely this could be a behaviour in ui sdk

## Implications
- **Agents are bad at the invisible parts of UI:** focus traps, Escape-to-dismiss, typeahead and ARIA are what generated UIs usually miss. Giving the agent tested behaviours to compose means it only writes layout and styling, and accessibility comes along by default.
- **Fewer, smaller building blocks:** as one reply puts it, two behaviour primitives can cover ten components. That is a smaller surface for an agent to learn and for a reviewer to check.
- **Game and tool UIs:** web-based level editors, asset browsers and in-browser game menus need exactly these behaviours (drag and drop, selection, popups, keyboard navigation). For Unity UI the library itself doesn't apply, but the pattern does: define reusable behaviour scripts (selectable, dismissible, draggable) and let the agent compose prefabs from them instead of writing a new script per widget.
- **Beta caution:** the API can change, and the sceptical replies are fair; for a simple site a finished component library may still be faster.
- **Experiment:** ask an agent to build the same small asset-browser panel (searchable list, selection, a context popup, drag to reorder) twice, once from scratch and once using the UI SDK behaviours and its skill. Compare lines of code, keyboard-only usability, and screen-reader output for both.

## Tags
`ui` `agents` `skills` `web` `accessibility` `open-source` `design-system`
