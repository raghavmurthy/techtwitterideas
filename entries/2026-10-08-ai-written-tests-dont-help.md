# Evidence: agent-written unit/integration tests don't improve success

**X post:** https://x.com/kunchenguid/status/2108030810691629403  
**Author:** Kun Chen (@kunchenguid) · posted 2026-10-08 (UTC) · 2804 likes, 459 replies  

## What it is
@kunchenguid on the DeepSWE eval: banning Sonnet 5.5 from writing tests gave slightly higher success (not significant) with significantly less time and tokens. Tests written by the 'tests allowed' arm (65% unit, 35% integration) didn't help, and disabling existing tests on a 44-task subset didn't change success either. His explanation: agent tests just restate the agent's own interpretation; E2E tests were barely written so remain untested.

## Thread highlights
- @rupeshpoojary_: “Agreed. Locking existing tests only preserves the checks you already have. New behavior needs new tests for invalid inputs, failures, boundaries, and repeated calls. I’d agree those expectations before implementation, then check that the tests catch deliberate”
- @pat_nadolny: “did you try using 2 different agent session? one writes tests and the other writes implementation”
- @stellachenyl: “Tbh tests are good but you have to add to the tests and tell the AI to write NEW tests that are based on what a real QA would demand  Not just happy path  AI likes to write happy path tests”

## Implications
- Supports telling agents not to write tests for trivial changes. Replies push back that human-specified and E2E tests still matter; in engines, designer-written play-mode checks are likely worth more than agent unit tests.
- **Experiment:** for two weeks, forbid agent-authored unit tests and give the agent 3 hand-written play-mode smoke checks; compare regressions.

## Tags
`testing` `coding-agents` `evals`
