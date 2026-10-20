# Claude Code idle compaction saves uncached-input cost

**X post:** https://x.com/SemiAnalysis_/status/2110444144233480309  
**Author:** SemiAnalysis (@SemiAnalysis_) · posted 2026-10-14 (UTC) · 282 likes, 35 replies  

## What it is
@SemiAnalysis_ reports that Claude Code 2.1.299 added idle compaction: sessions with 200k+ context compact automatically after ~54 minutes idle, refreshing the one-hour cache TTL so users don't pay for uncached input when they return. Lydia Hallie (@lydiahallie) of the Claude Code team announced it the same day and added that Claude then continues from a summary rather than the full context; it can be switched off in settings and the token threshold changed via an environment variable.

## Thread highlights
> **@lydiahallie:** It does mean that Claude continues from a summary instead of your full context though.

## Implications
- Long Unity/Blender agent sessions often sit idle; compaction cuts cost but drops detail, so put important state in files, not only in the conversation.
- **Experiment:** leave a long session idle past an hour with and without idle compaction, then ask detailed questions about earlier work and compare accuracy and usage.

## Tags
`claude-code` `context` `cost`
