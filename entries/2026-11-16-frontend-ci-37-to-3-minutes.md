# Cutting CI from 37 minutes to about 3: a five-step recipe an agent can apply overnight

**X post:** https://x.com/getmateri/status/2122311870740656533  
**Author:** alex (@getmateri) · posted 2026-11-16 (UTC) · 1,388 likes, 14 replies  
**Source:** the post and the post it quotes, by Pontus Abrahamsson (@pontusab), https://x.com/pontusab/status/2121982070193058191 (2026-11-15, 4,445 likes, 113 replies)

## What it is
Pontus Abrahamsson, whose X bio says he is building Glass at Ramp and was previously at Midday, posted that his team's frontend CI now runs in under two minutes, and listed five changes:

1. Swap the TypeScript compiler check (tsc) for Bun's faster type check.
2. Use oxlint, a fast Rust-based linter, with every rule they can turn on.
3. Split tests into shards balanced by each test's recorded run time, so no shard waits on a slow straggler.
4. On pull requests, run only the tests the diff can actually reach.
5. Run lint, type check, build and tests in parallel instead of one after another.

Quoting that list, alex (@getmateri), co-founder of materi per his X bio, says he had Claude apply it to his own repo overnight and CI went from 37 minutes to 3. He gives no further detail on which steps mattered most. The timings are the authors' own and were not checked here.

## Thread highlights
> **@berlinagentlab:** "PRs run only the tests the diff can reach" is the one that actually pays off, sharding masks the problem but reachability kills it

> **@jonghyukbuilds:** Does it catch changes in shared config files too, or just imports?

> **@elad_bezalel:** You can define implicit dependencies between projects and files

> **@WaldemarEnns:** We reduced our CI time this year from ~30mins to ~5mins. Running linting, typechecks, formatting, unit-tests, component-tests, e2e-tests with playwright, CRAP scores, SonarQube and static analyzers for security.

> **@whichaiwon:** 37 to 3 deserves a safety check, ask claude which mistakes could now slip through

## Implications
- **CI speed is now an agent bottleneck:** when agents open many small PRs, a 30-minute pipeline is what limits throughput, not the model. Pontus's earlier post makes the same point: CI is now the most important thing to make fast.
- **Diff-aware test selection is the big lever, with a caveat:** it only works if the dependency graph knows about non-import dependencies (config files, CI YAML, assets). Mark those explicitly, as the replies point out.
- **Game projects have their own slow steps:** for Unity, the equivalents are splitting edit-mode and play-mode tests, caching the Library folder between runs, and running asset-import or Blender export validation only when asset folders change.
- **Experiment:** ask a coding agent to profile your current CI run and propose a plan along these five lines (faster checker, strict fast linter, time-balanced shards, diff-scoped tests, parallel stages) without changing anything. Apply it on a branch, then compare wall-clock time and run a deliberately broken commit through it to confirm the faster pipeline still catches it.

## Tags
`ci` `testing` `performance` `devops` `agent-workflow` `typescript` `linting` `unity`
