# "All Code Is Slop (Except Mine)": a recap of Lauren Tan's talk on agents merging thousands of PRs

**X post:** https://x.com/huxlab/status/2122525595322204273  
**Author:** Hux (@huxlab) · posted 2026-11-17 (UTC) · 6,176 likes, 175 replies  
**Source:** the post (written in Chinese, paraphrased here in English) and the talk clip it attaches; the full talk was not watched here

## What it is
Hux, whose X bio describes him as a former Alibaba technical expert with eight years in engineering management, summarises a 17-minute talk by Lauren Tan (@poteto) at the AI Engineer Code Summit. According to his recap, she said she personally merged about 3,000 pull requests to production in the previous month (about 11,000 across her team) with a revert rate of roughly 0.5 percent, mostly written, verified and merged by agents while she slept. He lists four ideas from the talk:

1. **The codebase is the biggest input.** Agents copy what they see, so rather than writing rules in docs, close off the error-prone paths physically. His examples: banning `useEffect` in product code, making cross-process imports fail, and banning almost all comments.
2. **Turn every agent mistake into a lint rule, not an AGENTS.md line.** Natural-language rules are the most fragile layer; each correction becomes a deterministic static check or architectural constraint so the same mistake cannot reach a commit.
3. **Make the agent prove its work at runtime.** The agent must run tests, take screenshots, record video and, where possible, use formal verification to show the feature works.
4. **Build a trust pyramid from the bottom up:** codebase constraints, then static analysis, then runtime verification, then human review last.

His closing line is that the gap in human-agent collaboration is not model intelligence but whether the environment makes the shortest path the correct one: write constraints into code, not into documents. This repo already has her earlier written version of the pyramid (see the entry "How to trust agents' work: the inverse pyramid"). The PR counts are as reported in the recap and were not checked here.

## Thread highlights
> **@ziguai20:** 0.5% counts PRs that were reverted, which is not the same as only 0.5% of the code having bugs; problems fixed by later patches don't land in that metric. (translated from Chinese)

> **@staroaeg:** 3,000 PRs is impressive, but I'd rather see the incident rate, review cost and the maintenance bill six months later. (translated from Chinese)

> **@WarrenWiens:** This quote ""All code is slop, except mine." - does NOT appear in this video.

> **@nanika_is_what:** Writing things in agents.md is like making a wish. (translated from Chinese)

## Implications
- **Rules belong in the compiler, analyzers and tests:** in a Unity project that means assembly definitions to block forbidden references, Roslyn analyzers for banned APIs (for example `FindObjectOfType` in hot paths or `Update` allocations), and edit-mode tests for invariants.
- **Runtime proof fits games well:** an agent can run a scene headless, capture screenshots or a short clip, and compare frame-time numbers, which is stronger evidence than "it compiles".
- **Watch the metric:** revert rate understates bugs, as one reply notes; track follow-up fix commits as well.
- **Experiment:** pick one mistake your coding agent has made at least twice and replace the AGENTS.md line about it with a check that fails the build (an analyzer, a lint rule or a test). Then delete the prose rule and see whether the mistake recurs over two weeks.

## Tags
`agent-workflow` `code-quality` `static-analysis` `linting` `testing` `agents-md` `unity` `verification`
