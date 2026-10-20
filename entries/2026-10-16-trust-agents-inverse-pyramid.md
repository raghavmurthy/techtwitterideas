# How to trust agents' work: the inverse pyramid

**X post:** https://x.com/poteto/status/2111133080526495985  
**Author:** lauren (@poteto) · posted 2026-10-16 (UTC) · 6675 likes, 589 replies  

## What it is
lauren (@poteto), React compiler core team and previously at Cursor, Meta and Netflix per her X bio, lays out four layers for trusting agent output, with most effort at the top: (1) codebase improvements, since agents copy what exists, so better architecture, stronger types and clear boundaries make the easy path the right one; (2) static analysis such as lint rules, tests, CI and formal verification as token-efficient checks; (3) prose such as comments, rules, AGENTS.md and skills, used minimally for things that need judgment; (4) human review, the hardest to scale, best spent designing an environment where agents do the right thing by default. She then suggests having an agent study past review feedback and commits to find common agent pitfalls and propose refactors, using her pstack plugin (the post includes a ready-made prompt, not reproduced here).

## Thread highlights
- No notable replies came back from X search for this thread.

## Implications
- For game codebases: enforce rules in code (types, asmdef boundaries, analyzers) before writing them in AGENTS.md.
- **Experiment:** take the three most common agent mistakes in a Unity project and replace each with a compile-time or lint check instead of a written rule, then count recurrences over two weeks.

## Tags
`agent-workflow` `code-quality` `agents-md` `static-analysis`
