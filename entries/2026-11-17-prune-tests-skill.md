# prune-tests: an agent skill that deletes tests guarding no real behaviour

**X post:** https://x.com/mazeincoding/status/2122718134679298058  
**Author:** Maze (@mazeincoding) · posted 2026-11-17 (UTC) · 3,978 likes, 80 replies  
**Source:** https://github.com/caldoai/skills/blob/main/skills/prune-tests/SKILL.md (the skill file linked by the author in the thread)

## What it is
Maze released a slash-command skill called prune-tests for finding and removing tests that change whenever the code does, check that deleted features are gone, or can never fail. It answers a common complaint, quoted in the post, that agents asked to remove something add thousands of lines of tests asserting it no longer exists.

The skill's rule is that a test is kept only if it depends on intended behaviour: it should change only when that behaviour changes, and fail only on a regression. It prunes three kinds of tests:

- **Tests that depend on the past:** asserting removed code stays gone, or a moved module is absent from its old path. Bringing code back would be a decision, not a regression.
- **Tests that depend on nothing:** testing the browser itself (a button renders, a click fires), mocking the unit under test and asserting the mock, or asserting what the type system already guarantees.
- **Tests that depend on the implementation:** expected values computed with the same logic as the code, or assertions on private state, internal call order or which helper ran.

It also removes duplicate tests, rewrites tests that do cover real behaviour against that behaviour, and deletes production code that existed only for the removed tests. The author says it works well in agent reviews and can run over a whole codebase if you have tokens to spare.

## Thread highlights
> **@dudu9854:** The "can never fail" category seems the clearest win. For tests that change with the code, I'd want a mutation check before pruning: some are brittle, but some are documenting a real contract.

> **@SydlaAI:** The test that can never fail usually had no spec behind it. Tests tied to a written acceptance criterion are much harder to make useless.

> **@0Tokenzo:** most AI-written test suites need this. models love writing tests that assert the code does what the code does

> **@ThisIsSingleton:** Dang it has a @snyksec critical risk level due to prompt injection detected in the skill instructions

## Implications
- **Agent-written suites rot fast:** the three categories are a clear review checklist even without the skill.
- **Read before installing:** one reply reports a security scanner flagged the skill; review any third-party skill file yourself before adding it to an agent.
- **Game code fit:** Unity test suites often assert private fields or component call order; rewriting those against observable outcomes (score, position, saved state) makes refactors cheaper.
- **Guard against over-pruning:** run mutation testing or at least a deliberately broken build before and after pruning to confirm real coverage did not drop.
- **Experiment:** on one test folder, ask an agent to classify every test into keep, rewrite or delete using these three categories, without changing files. Spot-check ten verdicts, apply the rest on a branch, and compare test count, run time and whether a few injected bugs are still caught.

## Tags
`testing` `skills` `agent-workflow` `code-quality` `refactoring` `claude-code` `unity`
