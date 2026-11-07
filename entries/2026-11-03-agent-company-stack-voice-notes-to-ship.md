# Running a company as voice notes and inference: one founder’s full agent stack

**X post:** https://x.com/gregisenberg/status/2117734977312047537  
**Author:** GREG ISENBERG (@gregisenberg) · posted 2026-11-03 (UTC) · 5,830 likes, 566 replies  

## What it is
Greg Isenberg, who drops startup ideas daily, hosts a startup-ideas podcast and is CEO of Late Checkout (building companies such as IdeaBrowser) per his X bio, describes how he runs a 50-plus-person, 12-country company while talking to agents more than to human teammates. The long post is a stage-by-stage tool list, framed as dystopian but concrete.

Design starts with a voice note into an assistant, a grill-me skill that interrogates the idea before build, a Linear ticket via MCP, competitor research with search/crawl agents, review mining (G2, Reddit, App Store) for the ten most-repeated complaints, and current docs via Context7. UI work uses Claude Code plus a paper MCP, four screen versions before code, Anthropic’s frontend-design skill plus an in-house design-system skill, and CleanShot references (“make it feel like this”). Build uses T3 Code as the control surface (including from a phone), a parallel agent fleet each in its own git worktree, a codebase knowledge graph so agents navigate instead of guessing, tool-output compression for token headroom, LSP plugins, a security guidance hook, Supabase and Stripe MCPs, GitHub for PRs and Vercel for previews, with overnight loops reviewed over coffee. User testing runs a light headless browser fleet with impatient, confused and phone personas, plus Playwright and Chrome DevTools MCP. Bugs go Sentry MCP to a fix PR in minutes for human approve. Data: PostHog funnel cron, session-replay digests when a step drops more than 10%, Monday cancellation reasons from Stripe. Agent infrastructure includes per-agent computers, inboxes and phone numbers, connectors, and a git-backed markdown wiki for decisions. Skills cover writing voice, design system, specs and a skill-creator so agents write new skills. Operating rules: one agent per platform, cheap models for triage and a strong model for anything that ships, LLM-judge scores under 8 sent back, nightly five-line logs, and every mistake turned into a skill. Humans get a cleaned “version 5” for creative feedback and relationships; a human PM still reviews the funnel weekly while agents review it every morning. Closing line: running a company is now voice notes and inference.

## Thread highlights
> **@1PasswordDev:** If agents are part of the team, they need the same care as people. Their own identity, the right access, and a way to take it away when the job is done.

> **@zuoshi_ai:** The quiet shift: coordination moved from Slack to agents. The scarce skill now is writing a brief so clear a voice note can become a shippable spec—without a 12-person meeting.

> **@tobiaswup:** Which steps still need a human sign-off before something ships or touches customers?

> **@kadenc4_s:** Who fixes it at 3am when the agent breaks? That's the real test.

> **@kadenfhq43:** 50 people and you talk to bots more than them. That's not dystopian, that's a leak. What's the actual bottleneck - the team, or the handoffs?

> **@pixeltablehq:** here we keep agent outputs in a table and the score is a computed column, so every new row gets judged on insert and the under-8 ones are just a query.

## Implications
- **Pipeline over prompt:** the reusable idea is a path from voice brief to grilled spec to parallel worktrees to preview to funnel review, with humans at creative and customer edges rather than typing every ticket.
- **Identity and revoke:** replies stress that agents need named identity, scoped access and a kill switch, same as contractors, before they touch billing or production.
- **Handoffs are the leak:** talking to agents more than teammates can mean either leverage or a broken human coordination surface; measure which handoffs still fail at odd hours.
- **Experiment:** for one game or app feature, copy only four pieces of the stack for a week: a grill-me brief before any code, one agent per worktree, an LLM judge that rejects under-8 outputs, and a morning funnel or playtest digest. Compare cycle time and revert rate to the previous week’s ad-hoc agent use.

## Tags
`agent-workflow` `agents` `skills` `mcp` `claude-code` `worktrees` `ops` `startup`
