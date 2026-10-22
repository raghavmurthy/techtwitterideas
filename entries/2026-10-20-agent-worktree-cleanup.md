# 190 GB of leftover agent worktrees: make cleanup part of the loop

**X post:** https://x.com/dennis_kortsch/status/2112589671268225171  
**Author:** Dennis Kortsch (@dennis_kortsch) · posted 2026-10-20 (UTC) · 1,122 likes, 88 replies  

## What it is
A short post: the author deleted 190 GB of Claude Code session worktrees and advises telling your agent to clean up after itself. Parallel agent sessions each get their own git worktree (and often their own build artifacts), and nothing removes them when the task ends. Replies add practical fixes: a CLAUDE.md line to prune worktrees when a task finishes, subagent hooks for cleanup, using git's own worktree remove and prune commands instead of deleting folders (so uncommitted work isn't lost silently), pointing Rust builds at one shared target directory, and an MIT-licensed open-source sweeper, amnesia-sweep, that shows a size-sorted tree of agent sessions, worktrees and caches across Claude Code, Codex, Cursor, Gemini CLI and others, with a preview before anything is deleted or archived.

## Thread highlights
> **@wshin84847:** run git worktree list, use git worktree remove on the merged ones, then git worktree prune. Don't let the agent rm -rf worktree folders, because any uncommitted work in them is gone for good.

> **@patidarbitrary:** cleanup should be part of the agent loop, not a monthly archaeology session

> **@hboon:** My coding agents' artifacts/ directory is at 210.72GB

> **@Giamme1:** What it never touches: settings, CLAUDE.md, skills, plugins, memory, auth, databases.

## Implications
- **Game dev:** Unity and Unreal projects have huge Library/Intermediate folders; one worktree per agent session multiplies that fast, so disk fills much quicker than in web projects.
- **Agent workflows:** add an end-of-task rule (remove the worktree if merged, otherwise report it) rather than relying on manual sweeps.
- **Experiment:** measure total worktree and cache size on your machine today, add a prune-on-finish rule to CLAUDE.md, and check the size again after a week of normal use.

## Tags
`claude-code` `worktrees` `agent-workflow` `disk` `ops`
