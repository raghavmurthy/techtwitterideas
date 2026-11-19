# Mining 60 days of agent PRs to turn repeat mistakes into types, lint rules and tests

**X post:** https://x.com/LimestoneHQ/status/2122729161999688139  
**Author:** Limestone Digital (@LimestoneHQ) · posted 2026-11-17 (UTC) · 1,162 likes, 39 replies  
**Source:** the post and the author's thread continuation (the full prompt was only partly readable)

## What it is
Limestone Digital, which describes itself in its X bio as an AI implementation partner, shares a prompt for Claude Code that reviews the last 60 days of coding-agent work and turns each repeated mistake into a lint rule, a test or a type, instead of yet another line in CLAUDE.md. Their reasoning, from the thread: every line of the root CLAUDE.md loads into every session, and they cite Anthropic's docs as advising to keep it under 200 lines because longer files reduce adherence, while a CI check runs on every PR regardless.

For each repeated mistake they rank fixes by strength, starting with "make it impossible" through a type or structural change, then a lint rule or test. The prompt's task, as far as it is visible: find the mistakes coding agents made in the last 60 days, propose the strongest fix for each one that repeats, and change nothing until the user approves. It identifies agent-authored PRs by signals such as AI co-author trailers, bot authors or AI labels.

They suggest running it in Claude Code's plan permission mode with the GitHub CLI signed in, watching the commands it runs (it reads PRs through the CLI), choosing to approve edits manually, and approving only diffs you agree with, then repeating it each quarter. The rest of the thread is promotion for their services.

## Thread highlights
> **@fajarhide:** "never print secrets" sat in my CLAUDE.md and the agent still leaked six times in a month. moved it into a PreToolUse hook that denies the command before it runs

> **@zhangliang0115:** A hook that exits with code 2 blocks the call and sends its stderr back to the model, so I put the reason in there and it stops retrying the same command.

> **@sebuzdugan:** unless the generated test fails on the original bug, it adds confidence without catching regressions

> **@YuanZhu56611658:** Agents often turn a one-off symptom into a permanent rule, and several rules end up conflicting so new sessions become afraid to change code. Keep only the ones a human confirmed actually recur. (translated from Chinese)

> **@ivibecode:** This is just going to increase token consumption. Okay, cool, now you have lint rules that prints into context when not even applicable.

> **@callmedraxxx:** worth pointing it at the human PRs too. half the repeat mistakes in most repos are ours

## Implications
- **Same idea as the "trust pyramid" talk, made operational:** a review prompt that mines git history gives you a concrete backlog of rules to move from prose into code.
- **Verify each new test against the original bug:** as one reply says, a test that would not have failed on the old mistake is decoration.
- **Hooks are the middle ground:** for behaviours that are not code (printing secrets, running destructive commands), a pre-tool hook that blocks and explains is stronger than an instruction.
- **Unity angle:** typical repeat agent mistakes in game code (allocations in Update, missing null checks on serialized fields, editing generated files, forgetting .meta files) can each become an analyzer, an edit-mode test or a CI check.
- **Experiment:** run a read-only, plan-mode review over the last 60 days of agent-authored PRs in one repo, ask for the top five repeat mistakes with the strongest proposed fix for each, and implement only those where you can show the new check fails on the original commit.

## Tags
`agent-workflow` `claude-code` `linting` `testing` `code-quality` `agents-md` `hooks` `static-analysis`
