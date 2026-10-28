# Anthropic donates the Agent Skills standard to the Agentic AI Foundation

**X post:** https://x.com/ClaudeDevs/status/2113328526413996100  
**Author:** ClaudeDevs (@ClaudeDevs) · posted 2026-10-22 (UTC) · 8,734 likes, 296 replies  

## What it is
Anthropic's developer account announces that the Agent Skills standard (folders with a `SKILL.md` that describe how an agent should do a task) is being donated to the Agentic AI Foundation, the same foundation that MCP was donated to. The post says more than 70 agent platforms have adopted the standard since December 2025, including ChatGPT, Cursor, GitHub Copilot and VS Code. In the author's own follow-ups: existing skills keep working and licences don't change; anyone can use or contribute to the standard without joining the foundation; it will be governed by a technical steering committee with engineers from Anthropic, Earendil (Pi), Google, Microsoft, OpenAI and OpenCode; and the committee's first priority is a roadmap with versioned releases, a formal proposal process, and security guidance for skill authors and users. The spec lives at agentskills.io, with a longer write-up on Anthropic's blog.

## Thread highlights
> **@OnFinality:** Standardizing skills across 70+ platforms is the hard part; the real test is whether a skill authored for one agent runtime behaves the same in another.

> **@bluesky_2009:** Hoping the folder convention converges too so we don't maintain .claude/skills and .agents/skills side by side.

> **@SnarkyCoder418:** How about you rename CLAUDE.md into AGENTS.md? Since you suddenly start caring about standards now.

## Implications
- **Agent workflows:** skills are now a vendor-neutral format, so a well-written skill for a Blender export step or a Unity build check can be reused across Claude Code, Codex, Cursor and Copilot instead of being rewritten per tool.
- **Portability is still unproven:** replies point out that the same skill may behave differently across runtimes, and folder locations still differ between tools. Keep skills small and test them in each tool you use.
- **Security guidance is coming:** a formal security section for skill authors is on the roadmap; until then, review what each skill touches (files, commands, network) before installing it.
- **Experiment:** take one skill you already use (for example a model-compression or asset-export checklist), run it unchanged in two different agent tools on the same task, and note what breaks. Whatever breaks is what needs to move into the skill's own instructions or scripts.

## Tags
`skills` `agent-tooling` `standards` `claude-code` `codex` `agents`
