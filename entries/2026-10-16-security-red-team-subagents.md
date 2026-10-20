# Have subagents red-team a site before shipping

**X post:** https://x.com/Voxyz_ai/status/2111079716832886886  
**Author:** Vox (@Voxyz_ai) · posted 2026-10-16 (UTC) · 3391 likes, 97 replies  

## What it is
@Voxyz_ai suggests having Claude Code send three subagents with separate test accounts (two users and an admin) to actually run 14 attacks against a vibe-coded site, collect proof, then fix everything. Categories: impersonating other users (direct database queries with the public key, swapping IDs, privilege escalation, reusing reset links); bypassing UI limits (calling APIs directly, exceeding credit with parallel requests, malformed input, open redirects); attacks from outside (script injection, server-side request forgery, cache leaks across users, unauthenticated preview links, and hidden prompt injection against AI features). Every finding must be reproduced, re-tested with the protection temporarily removed, and saved as a script. He stresses safety limits: test accounts only, no real users or third-party services, payments in test mode, and never against a production database.

## Thread highlights
- No notable replies came back from X search for this thread.

## Implications
- Game backends (leaderboards, IAP receipts, cloud saves) have the same ID-swap and parallel-request weaknesses.
- **Experiment:** in a staging environment with test accounts, have one subagent try to edit another player's cloud save and to double-spend a currency grant with parallel requests; save each as a regression script.

## Tags
`security` `claude-code` `subagents` `testing`
