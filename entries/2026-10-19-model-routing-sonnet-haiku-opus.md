# Routing Claude Code work across Sonnet, Haiku and Opus by job

**X post:** https://x.com/thedelost/status/2112294434780131625  
**Author:** delost (@thedelost) · posted 2026-10-19 (UTC) · 757 likes, 35 replies  

## What it is
A post describing a three-model Claude Code setup: Sonnet 5.5 runs the main session and writes code, Haiku 5.5 subagents do read-only repo search, call-site grep and diff audits (the audit in its own worktree), and Opus 5.5 acts as an on-call advisor. Opus is only consulted at three moments: before a plan is locked, when the same error appears twice, and before declaring the work done. The post also adds a CLAUDE.md rule to delegate repo searches and test runs to the Haiku subagents to keep the main context small, and mentions routing very fast decisions (tool choice, path, retry) through a model it calls JEV.

The post frames this as "Anthropic just shared" a trick and gives a launch flag for an advisor model. Neither claim is backed by the source it quotes, which is a third-party long-form course promoting a paid quant-trading data service; the flag wasn't verified here. The routing idea stands on its own regardless.

## Thread highlights
> **@pi_himself:** Routing only saves where the cheap model's output stays small. Raw tool output still lands in the expensive model's context, so trim it before the handoff.

> **@soflark76:** Routing by task assumes you can predict which task needs which model, but you usually only learn that after the first attempt fails.

> **@runtimetoys:** routing by task type only works if the orchestrator actually knows what task it's looking at. in my logs it mislabels half the time. did anyone measure the real token drop, not just the demo?

## Implications
- **Agent workflows:** the "only call the expensive model at checkpoints" rule (plan lock, repeated error, sign-off) is the most reusable part and needs no special flag.
- **Cost:** replies point out that savings disappear if cheap subagents dump raw output into the main context; summarise before handing back.
- **Experiment:** create one cheap read-only search subagent and one audit subagent for a Unity or Blender-scripting repo, run a week of normal tasks, and compare token spend and task success against the previous week.

## Tags
`claude-code` `subagents` `cost` `model-routing` `agent-workflow`
