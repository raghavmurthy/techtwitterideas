# A roundup of large agent and skill repos for Claude Code (and which are actually Anthropic's)

**X post:** https://x.com/romandevz/status/2111867588405862713  
**Author:** Rodev (@romandevz) · posted 2026-10-18 (UTC) · 5,206 likes, 89 replies  

## What it is
A Spanish-language post claiming "Anthropic has published 400+ ready-to-use agents and skills", then listing five GitHub collections with star counts as given in the post:

- **agency-agents** (msitarzewski, ~158k stars): about 170 agents organised like a company (engineering, design, marketing, sales, product, testing, security, support), with extra packs for finance, health and game development, compatible with 15+ tools.
- A plugin collection (~40k stars): 202 agents, 184 skills and 105 commands across 94 Claude Code plugins, covering languages, code review, debugging, infrastructure, security and testing; install only what you need.
- **knowledge-work-plugins** (~26k stars): Anthropic's own plugins grouped by function (sales, support, product, marketing, legal, finance, data).
- **claude-quickstarts** (~18k stars): runnable reference agents such as a daily Slack/GitHub digest, scheduled Sentry triage, Slack and Linear bots, a support agent and a financial-data analyst.
- A ~103k-star set of 25 skills attributed to Anthropic engineers, covering the dev cycle (interview-me, spec writing, test-driven development, browser testing, security review, CI/CD).

The author suggests starting with claude-quickstarts. The headline is misleading: a reply points out that only knowledge-work-plugins and the quickstarts are Anthropic repos; the rest are community projects.

## Thread highlights
> **@davidpintoi:** Ojo: de esa lista, solo knowledge-work-plugins y los quickstarts son repos de Anthropic; los otros son de la comunidad. Valen igual, pero conviene saber de quién es el código que vas a instalar.

> **@agentloopkn:** 170 agent roles organized like a company is a folder structure, not a system. ask me again when half of them pass the same eval.

> **@picazo_dev:** Catálogo brutal, pero tirar 400 skills al modelo no es orquestar.

## Implications
- **Agent workflows:** the official quickstarts are the most useful starting point because each is a complete, runnable agent to study and take apart.
- **Security:** skills and plugins can run code; check who owns a repo before installing, especially when a post attributes community code to a vendor.
- **Game dev:** agency-agents reportedly has a game-development pack; worth reading for role prompts (designer, QA) even if not installed wholesale.
- **Experiment:** pick one quickstart (the scheduled triage agent) and adapt it to triage crash reports or build failures for a game project, keeping it read-only.

## Tags
`agents` `skills` `plugins` `claude-code` `resources` `security`
