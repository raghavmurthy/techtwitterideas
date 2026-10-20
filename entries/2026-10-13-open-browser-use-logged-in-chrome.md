# open-browser-use: agents drive your real, logged-in Chrome over MCP

**X post:** https://x.com/DivyanshT91162/status/2109918301455516002  
**Author:** divyansh tiwari (@DivyanshT91162) · posted 2026-10-13 (UTC) · 57 likes, 17 replies  
**Repo:** https://github.com/open-browser-use/open-browser-use  

## What it is
An open-source tool, written in Rust and TypeScript and exposed over MCP, that lets coding agents (Codex, Claude Code, Cursor, Gemini CLI) control the Chrome you already use, with your existing sessions, instead of a fresh browser with no logins. The post's examples are downloading invoices from email and totalling them, scraping dashboards that have no export button, filling multi-step forms from PDF data, and resuming a browser task across turns. It runs locally with no cloud account, is in public preview for macOS and Linux, and has an early reinforcement-learning environment with structured actions and observations. The replies are almost all about the same thing: real sessions are the whole point and also the whole risk.

## Thread highlights
> **@atharvaadhumal:** The scary part is prompt injection with your cookies attached. A page can hide instructions the agent reads, so I'd want a per-domain allowlist and a confirm step before anything that sends or pays.

> **@timwork_notes:** i'd also give it its own chrome profile with just the 2 or 3 sites it needs logged in, so a weird page can't wander into your bank tab

> **@JoePro:** Mine never touch my daily Chrome. They run on their own Linux box with their own browser.

## Implications
- Logged-in browser control turns "no API" web tools (asset stores, ad dashboards, store consoles, analytics) into something an agent can actually work with.
- The safe setup is a dedicated Chrome profile logged into only the sites the task needs, read-only tasks first, and a human confirm step before anything that pays, sends or deletes.
- For game dev: a scoped profile could let an agent pull sales and review data from storefront dashboards, or download purchased asset packs into a Unity or Blender project.
- **Experiment:** create a separate Chrome profile logged into one asset store only, have an agent download three purchased low-poly packs and import them into a Unity project, and log every page it visits; check whether the log shows any page outside the allowlist.

## Tags
`browser` `mcp` `agents` `agent-tooling` `security` `open-source`
