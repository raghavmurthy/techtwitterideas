# A 25-point security brief to give a coding agent before shipping a vibe-coded app

**X post:** https://x.com/suraj_sharma14/status/2122510031145046125  
**Author:** Suraj Sharma (@suraj_sharma14) · posted 2026-11-17 (UTC) · 990 likes, 57 replies  
**Source:** the post and the author's replies

## What it is
Suraj Sharma, whose X bio says he helps builders get into AI, startups and global opportunities, shares a pre-launch security brief for Claude, grouped into five areas (paraphrased here, not reproduced):

- **Access:** proper authentication, hashed passwords, locked-down admin routes, secure session cookies, expiring password-reset links.
- **Secrets:** move keys and secrets out of the code, review every environment variable, scan git history for leaked secrets, revoke and replace anything exposed.
- **Data:** secure the database, parameterised queries, server-side validation of every form, limits on upload types and sizes, server-side verification of prices and payments.
- **Web:** HTTPS, XSS and CSRF protection, restricted CORS, security headers, rate limiting.
- **Before launch:** debug mode off in production, vulnerable dependencies updated, unused packages removed, exposed files checked, suspicious activity logged and monitored, every protection tested, and a report of what was found and fixed.

In replies he adds that a fresh-session review catches assumptions the original coding session missed, that Supabase row-level security matters more than a secure frontend, that storage bucket permissions are separate from table permissions, that environment-variable changes should be explained before they are applied, and that a confident AI answer is not a security guarantee, so verify independently before shipping.

## Thread highlights
> **@Warditor:** One step I'd add at the end: don't take the report's word for it. Make a second test account and try to read or edit the first account's data. If you can, it isn't fixed.

> **@AuditDaas:** People lock down the users table, then leave a public bucket full of ID scans next to it. Private buckets + signed URLs, every time.

> **@marginmints:** I would run a security scan before and after the prompt and count the flaws left.

> **@nistrax:** so the security plan is just ask claude nicely and hope it remembers the admin routes

## Implications
- **A checklist is a starting point, not proof:** pair it with an actual attack pass (this repo's "Have subagents red-team a site before shipping" entry) and an independent scanner.
- **Games with backends have the same holes:** leaderboards, cloud saves, receipts and in-game purchases need server-side validation of scores and prices, rate limits and private storage for user uploads.
- **Secrets in game builds are easy to leak:** keys embedded in a Unity build can be extracted from the binary; keep them server-side.
- **Experiment:** run this five-area audit with a coding agent in a fresh session, then verify three findings yourself with a second test account (cross-account read, price tampering, rate-limit bypass) and record which "fixed" items still fail.

## Tags
`security` `checklist` `launch` `vibe-coding` `agent-workflow` `backend` `game-dev`
