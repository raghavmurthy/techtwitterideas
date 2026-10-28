# Overnight agent runs: skip subagents to save usage

**X post:** https://x.com/rohit3a/status/2113579599624114313  
**Author:** rohit (@rohit3a) · posted 2026-10-23 (UTC) · 1,251 likes, 103 replies  

## What it is
A founder and designer argues against letting coding agents spawn subagents on overnight runs unless you have several subscriptions. His reasoning: subagents mainly buy speed or extra thoroughness, and overnight speed doesn't matter. For tasks of a few hours, he suggests giving the job to Opus 5.5 on its highest effort setting and telling it not to use subagents. He says Opus 5.5 can spawn 10 to 12 subagents, which can spawn their own, and that this can burn through most of a usage allowance by morning. In replies he says he tracks usage with a custom tool, and concedes after testing that a subagent's first request costs around 40K tokens, but argues it adds up because each subagent has to rediscover context.

## Thread highlights
> **@rohit3a:** depending on how many you're running, and how much the subagents need to basically rediscover all the context, it does add up.

> **@maheshkamalakar:** Have you compared both setups on the same task and starting commit? Total usage plus the fixes needed the next morning would be more useful than agent count alone.

> **@skoftsoftware:** Targetted delegation of specific tasks to selected (other) models, if done in a good way, can significantly increase quality output aswell as save costs aswell.

## Implications
- **Long unattended jobs:** batch work such as asset conversion, refactors or test writing that runs overnight should be set up to minimise fan-out, since wall-clock time is free but usage isn't.
- **Measure, don't guess:** the claim is anecdotal; the useful comparison is total usage plus the fixes needed the next morning, on the same task and starting commit.
- **Delegation still has a place:** routing narrow sub-tasks to cheaper models can save usage, so the rule is about uncontrolled spawning, not subagents in general.
- **Experiment:** run the same overnight task twice from the same commit, once with subagents allowed and once with them disabled, and record usage consumed, tests passing and fixes needed in the morning.

## Tags
`agent-workflow` `subagents` `cost` `claude-code` `usage-limits`
