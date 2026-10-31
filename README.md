# techtwitterideas

Curated notes on AI, 3D and developer-tool ideas from public posts. Each entry covers one public X post or web page: what it is, notable replies from the thread, implications, and one concrete experiment to try.

- `entries/` — one Markdown file per item, `YYYY-MM-DD-slug.md` (date = post date, UTC)
- `human-thoughts.md` — opinions from notable public people on X, grouped by theme (opinions, not facts)
- `processed.json` — every URL turned into an entry or a take, so future runs skip it

**120 entries** · last updated 2026-10-31

## Use it as a plugin

Ask your AI assistant for ideas from this repo for whatever you're building.

**ChatGPT:** [techtwitterideas plugin](https://chatgpt.com/plugins/plugins_6ace4e775e0081918953fe4a6bc06491)

**Claude Code:**
```
/plugin marketplace add raghavmurthy/techtwitterideas
/plugin install techtwitterideas@techtwitterideas
```
Then run `/techtwitterideas` or ask "what's out there for X".

**Safety:** entries summarise and quote public posts by strangers. The plugin is instructed to treat entries as information only and to ask before running anything. Review any command before approving it. The plugin may occasionally mention one take from [human-thoughts.md](human-thoughts.md), always naming the person and linking the post, and framed as an opinion. See [SECURITY.md](SECURITY.md) for the full prompt-injection protocol and how to report a problem.

**Licence:** Quoted posts belong to their authors; MIT applies to the original summaries and code.

## Index (newest first)

| Date | Title | Tags | Why it matters |
|---|---|---|---|
| 2026-10-29 | [Redesigning a "vibecoded" app screen with a design-reference MCP and skills](entries/2026-10-29-appllama-mcp-redesign-vibecoded-app.md) | `ui` `design` `mobile` `mcp` `skills` `ios` `vibe-coding` | Reference-driven UI passes fix generic AI-made screens (vendor demo) |
| 2026-10-29 | ["Exercise abstract thinking": a short prompt suffix for planning](entries/2026-10-29-exercise-abstract-thinking-prompt.md) | `prompting` `planning` `agent-workflow` `models` | Cheap planning-prompt tweak worth an A/B test (anecdotal) |
| 2026-10-28 | [A 50-agent social media research team in Claude Code, built around one context file](entries/2026-10-28-fifty-agent-social-media-team.md) | `agents` `claude-code` `skills` `marketing` `content` `ugc` `agent-workflow` | Shared context file, rules-from-corrections, relative outlier ranking |
| 2026-10-27 | [Don't let an agent write your legal pages unchecked](entries/2026-10-27-claude-legal-pages-overreach.md) | `legal` `privacy` `launch` `claude` `agent-workflow` `gdpr` | Generated policies can add promises and expose the stack |
| 2026-10-26 | [tstack: Theo publishes the agent skills he uses daily](entries/2026-10-26-tstack-published-agent-skills.md) | `skills` `agent-workflow` `code-review` `github` `claude-code` `codex` `open-source` | Ready-made skills for review loops and PRs, incl. cross-model review |
| 2026-10-23 | [Take your VPS off the public internet with Tailscale and Cloudflare Tunnel](entries/2026-10-23-vps-tailscale-cloudflare-tunnel.md) | `security` `devops` `vps` `networking` `infrastructure` | Free setup that closes every open port on a small server |
| 2026-10-23 | [Overnight agent runs: skip subagents to save usage](entries/2026-10-23-skip-subagents-overnight.md) | `agent-workflow` `subagents` `cost` `claude-code` `usage-limits` | Unattended runs don't need speed; subagent fan-out burns usage |
| 2026-10-22 | [Anthropic donates the Agent Skills standard to the Agentic AI Foundation](entries/2026-10-22-agent-skills-donated-to-aaif.md) | `skills` `agent-tooling` `standards` `claude-code` `codex` `agents` | Skills become a vendor-neutral format across 70+ agent tools |
| 2026-10-22 | [A Claude skill that turns an SVG into a 60 fps animation](entries/2026-10-22-svg-to-60fps-motion-skill.md) | `skills` `animation` `svg` `ui` `mobile` `claude-code` | Agent-made UI motion without a dedicated animation tool |
| 2026-10-20 | [Epic's Unreal Engine skills plugin lets Claude Code drive a running Unreal Editor](entries/2026-10-20-epic-unreal-engine-claude-code-plugin.md) | `unreal` `mcp` `game-dev` `claude-code` `agent-tooling` `skills` | Agent edits a live Unreal Editor; copyable list/describe/call tool pattern |
| 2026-10-20 | [10 free repos for building 3D games with Claude Code](entries/2026-10-20-ten-repos-3d-games-claude-code.md) | `game-dev` `unity` `godot` `threejs` `mcp` `skills` `open-source` `resources` | Open-source stack for agent-built 3D games, incl. Unity MCP |
| 2026-10-20 | [190 GB of leftover agent worktrees: make cleanup part of the loop](entries/2026-10-20-agent-worktree-cleanup.md) | `claude-code` `worktrees` `agent-workflow` `disk` `ops` | Leftover agent worktrees eat disk; prune on finish |
| 2026-10-20 | [Analysing 4.5M TikToks: viral UGC isn't luck, and it isn't the format](entries/2026-10-20-tiktok-ugc-virality-analysis.md) | `marketing` `ugc` `tiktok` `mobile` `growth` | Story and creator over format for UGC (hypothesis) |
| 2026-10-20 | [Starting a first app today: web prototype first, one flow at a time](entries/2026-10-20-first-app-path-web-prototype-first.md) | `launch` `mobile` `prototyping` `vibe-coding` `agent-workflow` | Validate on web first, build one flow at a time |
| 2026-10-19 | [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md) | `3d` `cad` `world-models` `models` `asset-pipeline` `research` | Buildable part-by-part CAD history instead of a mesh (claims self-reported) |
| 2026-10-19 | [Skill Issue: agent skills ranked by what people actually use](entries/2026-10-19-skill-issue-ranked-agent-skills.md) | `skills` `resources` `design` `agents` | See which agent skills are widely used before writing your own |
| 2026-10-19 | [Genex 0.1.10: an open-source desktop app for making games with any AI, now on Windows](entries/2026-10-19-genex-open-source-ai-game-maker.md) | `game-dev` `agents` `open-source` `unity` `godot` `blender` `local-models` | Game-specific agent harness that plays and tests its own builds |
| 2026-10-19 | [Routing Claude Code work across Sonnet, Haiku and Opus by job](entries/2026-10-19-model-routing-sonnet-haiku-opus.md) | `claude-code` `subagents` `cost` `model-routing` `agent-workflow` | Call the expensive model only at checkpoints |
| 2026-10-19 | [A benchmark of how models handle pushback: GPT-4o caves, Opus 5.5 digs in](entries/2026-10-19-sycophancy-pushback-benchmark.md) | `models` `benchmarks` `sycophancy` `claude` `agent-workflow` | Models differ on caving vs ignoring valid corrections |
| 2026-10-19 | [T3 Code impressions: multi-machine, multi-provider agent threads](entries/2026-10-19-t3code-multi-machine-agents.md) | `agent-tooling` `claude-code` `codex` `multi-machine` `open-source` | Steer agents across machines and providers |
| 2026-10-19 | [The "boring pages" an AI-built app still needs before launch](entries/2026-10-19-legal-pages-before-launch.md) | `launch` `legal` `privacy` `checklist` `app-store` | Privacy, deletion and refund pages stores and Stripe expect |
| 2026-10-18 | [10 resources for AI-assisted 3D and animated web design](entries/2026-10-18-web-3d-design-resource-list.md) | `web-design` `threejs` `motion` `resources` | Reference set for 3D/motion web pages |
| 2026-10-18 | [Checklist for fast App Store approval](entries/2026-10-18-apple-fast-approval-checklist.md) | `app-store` `ios` `launch` `subscriptions` | Concrete App Review checklist |
| 2026-10-18 | [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md) | `audio` `sfx` `motion-graphics` `game-dev` `mcp` `compression` `open-source` | Procedural, frame-synced SFX for trailers and game UI |
| 2026-10-18 | [A roundup of large agent and skill repos for Claude Code (and which are actually Anthropic's)](entries/2026-10-18-agent-and-skill-repo-roundup.md) | `agents` `skills` `plugins` `claude-code` `resources` `security` | Which big skill repos are official vs community |
| 2026-10-18 | [Phishing emails that target the AI reading your inbox](entries/2026-10-18-email-prompt-injection-ai-assistants.md) | `security` `prompt-injection` `email` `agents` | Hidden instructions in email aimed at AI assistants |
| 2026-10-18 | [Rejected under 2.5.19 for test switches left in a release build](entries/2026-10-18-hidden-test-switches-app-review.md) | `app-store` `ios` `compliance` `unity` `release` | Strip debug switches before upload; scan strings |
| 2026-10-18 | [Seven principles for feature flags at scale on iOS](entries/2026-10-18-ios-feature-flags-principles.md) | `ios` `feature-flags` `ab-testing` `live-ops` `mobile` | Remote-config checklist, with the new Apple rule in mind |
| 2026-10-18 | [A self-maintaining second-brain wiki run by three bots: reader, librarian, checker](entries/2026-10-18-three-bot-second-brain-wiki.md) | `knowledge-base` `memory` `agents` `agent-workflow` `wiki` | Collect/write/doubt split for a self-maintaining wiki |
| 2026-10-17 | [10 open-source repos for an AI content pipeline](entries/2026-10-17-open-source-content-factory-repos.md) | `content` `video` `audio` `open-source` | Open-source stack for devlogs and trailers |
| 2026-10-17 | [Concept art to playable 3D world via blockout + painted projection](entries/2026-10-17-concept-art-to-playable-3d.md) | `3d` `asset-pipeline` `shaders` `concept-art` `claude` | Turn concept art into a walkable 3D scene |
| 2026-10-17 | [Claude Code replaces an ad-heavy Android TV launcher](entries/2026-10-17-claude-code-android-tv-launcher.md) | `claude-code` `android` `devices` `agents` | Agent-driven device setup, reversible |
| 2026-10-17 | [Apple updates App Review Guidelines amid developer account terminations](entries/2026-10-17-app-review-guidelines-update.md) | `app-store` `ios` `compliance` | New App Review rules on hidden features and assets |
| 2026-10-17 | [Design inspiration sites, including DESIGN.md files for agents](entries/2026-10-17-ai-design-inspiration-sites.md) | `design` `resources` `agents-md` `ui` | DESIGN.md files to steer agent-built UI |
| 2026-10-17 | [DeepSeek V4.1 Flash vs Opus 5.5 on a one-prompt 3D Bowser test: $0.15 vs $3.85](entries/2026-10-17-deepseek-flash-vs-opus-bowser-3d.md) | `3d` `models` `cost` `benchmarks` `deepseek` `claude` `asset-pipeline` | ~25x cheaper code-generated 3D drafts |
| 2026-10-16 | [How to trust agents' work: the inverse pyramid](entries/2026-10-16-trust-agents-inverse-pyramid.md) | `agent-workflow` `code-quality` `agents-md` `static-analysis` | Put effort into code and checks, not prose |
| 2026-10-16 | [Have subagents red-team a site before shipping](entries/2026-10-16-security-red-team-subagents.md) | `security` `claude-code` `subagents` `testing` | Agent red-team checklist for backends |
| 2026-10-16 | [Lessons from a vibe-coded iOS app with 4K Reddit-only downloads](entries/2026-10-16-reddit-4k-downloads-ios-app.md) | `launch` `analytics` `marketing` `agents` | Design first, analytics day one |
| 2026-10-16 | [Gemini 4 Argon builds a Subway Surfers-style flying runner](entries/2026-10-16-gemini-flying-roadster-runner.md) | `game-dev` `prototyping` `gemini` `browser-games` | Runner prototype with code to study |
| 2026-10-16 | [A 25-minute animated episode written entirely as code by Opus](entries/2026-10-16-claude-coded-anime-episode.md) | `animation` `claude` `threejs` `cost` | Cost benchmark for code-made animation |
| 2026-10-16 | [App Store Review Guideline 2.5.19 and remote config / A/B testing](entries/2026-10-16-app-store-guideline-2-5-19.md) | `app-store` `ios` `ab-testing` `compliance` | Possible impact on paywall A/B tests |
| 2026-10-15 | [How Block Blast! designs losses around ads](entries/2026-10-15-block-blast-ad-design-breakdown.md) | `game-design` `monetization` `mobile` `ads` | Casual game monetisation teardown |
| 2026-10-15 | [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md) | `blender` `agent-tooling` `agents` `cli` `open-source` `asset-pipeline` `compression` | Scriptable Blender/GIMP for agent asset pipelines |
| 2026-10-15 | [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md) | `checklist` `launch` `security` `vibe-coding` `ops` `testing` | Pre-launch audit list for AI-built apps |
| 2026-10-14 | [How Railway grew via AI recommendations (AI SEO)](entries/2026-10-14-railway-ai-seo-playbook.md) | `seo` `ai-search` `docs` `growth` | Docs for agents as a growth channel |
| 2026-10-14 | [Claude Code idle compaction saves uncached-input cost](entries/2026-10-14-claude-code-idle-compaction.md) | `claude-code` `context` `cost` | Cheaper idle sessions, at the cost of detail |
| 2026-10-13 | [X research skill + media download for video editing workflows](entries/2026-10-13-x-research-skill-video-workflows.md) | `claude-code` `research` `video` `skills` | Agent research feeding video edits |
| 2026-10-13 | [Solo developer's 50-agent stack: $545k MRR, 1,089 PRs in a week](entries/2026-10-13-solo-dev-50-agent-stack.md) | `agent-workflow` `orchestration` `code-review` `ci` | Blueprint for running many agents with review and auto-revert |
| 2026-10-13 | [Anthropic's Scion: source control rebuilt for agent-scale merges](entries/2026-10-13-scion-agent-scale-source-control.md) | `source-control` `agents` `infra` `ci` | Agent-scale infra lessons from Anthropic |
| 2026-10-13 | [Have subagents audit 20 web performance issues](entries/2026-10-13-perf-audit-subagents.md) | `performance` `subagents` `web` `checklist` | Structured perf audit by agent groups |
| 2026-10-13 | [An indie developer's ranking of mobile app marketing channels](entries/2026-10-13-mobile-app-marketing-channels.md) | `marketing` `mobile` `ugc` `aso` | Channel map for mobile launches |
| 2026-10-13 | [The Little Prince as a 3D story game in 16 days with Opus, Tripo and Blender](entries/2026-10-13-little-prince-3d-story-game.md) | `game-dev` `3d` `image-to-3d` `blender` `claude` | Solo 3D game in 16 days, workflow promised |
| 2026-10-13 | [Google Play lets you install private vibe-coded apps](entries/2026-10-13-google-play-private-vibe-coded-apps.md) | `android` `google-play` `distribution` `prototyping` | Easier private Android installs, new game discovery |
| 2026-10-13 | [Codex memory: swap the default memory models in config](entries/2026-10-13-codex-memory-model-upgrade.md) | `codex` `memory` `config` `agent-workflow` | Possibly better long-term agent memory via config |
| 2026-10-13 | [Apple Search Ads playbook for indie apps](entries/2026-10-13-apple-search-ads-playbook.md) | `marketing` `app-store` `ads` `ios` | Step-by-step Apple Search Ads start |
| 2026-10-13 | [How to be more ambitious with models: altitude, depth and range (plus a /be-ambitious skill)](entries/2026-10-13-be-ambitious-with-models.md) | `prompting` `skills` `agent-workflow` `claude` `quality` | A method for asking models for expert-level work |
| 2026-10-13 | [open-browser-use: agents drive your real, logged-in Chrome over MCP](entries/2026-10-13-open-browser-use-logged-in-chrome.md) | `browser` `mcp` `agents` `agent-tooling` `security` `open-source` | Agents on no-API web tools, with real-session risks |
| 2026-10-12 | [20 speed fixes for vibe-coded apps](entries/2026-10-12-speedmaxxing-vibe-coded-apps.md) | `performance` `mobile` `checklist` | Performance checklist |
| 2026-10-12 | [Don't report instantly cancelled trials to Meta](entries/2026-10-12-meta-ads-filter-instant-cancels.md) | `ads` `subscriptions` `analytics` | Feed ad algorithms only the events you want |
| 2026-10-11 | [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md) | `pdf` `docs` `context` `tools` | Fast PDF to Markdown for agent context |
| 2026-10-11 | [Claude Code hands off X research to GrokBot via a webhook skill](entries/2026-10-11-claude-code-grokbot-handoff.md) | `claude-code` `multi-agent` `skills` `research` | Agent-to-agent handoff for live X research |
| 2026-10-11 | [Submit sitemaps to Bing Webmaster Tools and IndexNow](entries/2026-10-11-bing-indexnow-sitemap.md) | `seo` `indexing` `marketing` | Cheap discoverability for game/tool sites |
| 2026-10-10 | [Railway free Linux VMs with Claude Code/Codex preinstalled](entries/2026-10-10-railway-free-agent-vms.md) | `sandbox` `agents` `infra` | Disposable agent sandboxes |
| 2026-10-10 | [Prompt: output architecture as a C4 model in HTML (Japanese)](entries/2026-10-10-c4-architecture-html-prompt.md) | `architecture` `prompts` `docs` | One-prompt architecture overview |
| 2026-10-10 | [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md) | `audio` `tts` `music` `open-source` | Open-source audio stack for game narration and ambience |
| 2026-10-09 | [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md) | `launch` `checklist` `security` | Launch checklist |
| 2026-10-09 | [Sound-design prompt for Opus/Fable motion design](entries/2026-10-09-opus-sound-design-prompt.md) | `audio` `motion-graphics` `prompts` | Sound ordering for AI promos |
| 2026-10-09 | [break-ui skill throws worst-case realistic data at a UI](entries/2026-10-09-break-ui-skill-praise.md) | `skills` `ui` `testing` | Second endorsement of break-ui |
| 2026-10-09 | [Avoiding Apple rejections for 'spam/slop' apps](entries/2026-10-09-apple-app-review-slop-rejections.md) | `app-store` `ios` `mobile` `launch` | Pass App Review with proof of original work |
| 2026-10-09 | [anti-slop: filters generic AI-generated UI, text and code](entries/2026-10-09-anti-slop-filter.md) | `writing` `quality` `skills` | Keep copy from reading as AI-generic |
| 2026-10-08 | [Tencent Hy-MT2: 440 MB offline translator, 33 languages (Turkish post)](entries/2026-10-08-tencent-hy-mt2-offline-translator.md) | `translation` `on-device` `localization` | Local translation for localisation drafts |
| 2026-10-08 | [Qwen3.5 9B distilled from Kimi k3 (GGUF)](entries/2026-10-08-qwen3-5-9b-kimi-distill.md) | `local-models` `distillation` `compression` `coding` | Local 9B distilled coding model |
| 2026-10-08 | [Primitives → skills → feature loop against AI slop](entries/2026-10-08-primitives-skills-loop.md) | `skills` `agents-md` `workflow` | Make agents reuse a project's own building blocks |
| 2026-10-08 | [Build ChatGPT plugins: point Codex at openai/mcp-extensions](entries/2026-10-08-openai-mcp-extensions-chatgpt-plugins.md) | `chatgpt-plugin` `mcp` `distribution` | ChatGPT plugin as a distribution channel |
| 2026-10-08 | [oh-my-mermaid: architecture diagrams from a codebase via Claude Code](entries/2026-10-08-oh-my-mermaid-architecture-diagrams.md) | `diagrams` `claude-code` `docs` | Diagram the codebase for agents |
| 2026-10-08 | [NeuDecide: 43 MB speech-to-tool-call model on one CPU thread](entries/2026-10-08-neudecide-audio-tool-calls.md) | `voice` `on-device` `compression` `tool-calling` | Offline voice commands in 43 MB |
| 2026-10-08 | [Launch video from HTML + GSAP rendered by HyperFrames](entries/2026-10-08-hyperframes-launch-video.md) | `motion-graphics` `video` `claude` `marketing` | Free scripted launch videos |
| 2026-10-08 | [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md) | `ios` `testing` `agents` `mobile` | Agents can play-test iOS builds |
| 2026-10-08 | [Evidence: agent-written unit/integration tests don't improve success](entries/2026-10-08-ai-written-tests-dont-help.md) | `testing` `coding-agents` `evals` | Stop paying tokens for agent unit tests |
| 2026-10-08 | [20 repos for agent-made motion design (claude-motion, HyperFrames, Remotion, GSAP)](entries/2026-10-08-20-motion-design-repos.md) | `motion-graphics` `skills` `video` `marketing` | Motion design stack for agents |
| 2026-10-07 | [ruNNtime: porting new models to the browser with Claude](entries/2026-10-07-ruNNtime-browser-models.md) | `on-device` `browser` `model-porting` | Fast model porting to new runtimes |
| 2026-10-07 | [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md) | `tts` `on-device` `compression` `audio` | 9 MB offline TTS for in-game narration |
| 2026-10-07 | [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md) | `video-editing` `claude` `ffmpeg` `marketing` | Claude-driven video editing for devlogs |
| 2026-10-07 | [SEO: agent-assisted backlink outreach](entries/2026-10-07-agent-backlink-outreach.md) | `seo` `marketing` `agents` | Agent-assisted SEO outreach for launch |
| 2026-10-06 | [6 legal traps in AI-built apps (COPPA, GDPR fonts, CIPA, CAN-SPAM)](entries/2026-10-06-vibe-coded-app-legal-traps.md) | `legal` `launch` `subscriptions` `privacy` | Legal checklist before launch |
| 2026-10-06 | [Claude Startups program expands](entries/2026-10-06-claude-startups-program.md) | `claude` `startup-programs` `credits` | Free Claude Team + credits: apply |
| 2026-10-05 | [Leviathan: agents search huge databases in ~436 tokens](entries/2026-10-05-leviathan-agent-indexer.md) | `agent-tooling` `retrieval` `context` | Token-cheap search for agents |
| 2026-10-05 | [Ask: a dataset of 1-10k beautiful landing pages](entries/2026-10-05-landing-page-dataset-ask.md) | `design` `landing-page` | Question only; see Designeer |
| 2026-10-05 | [Hugging Bay: searchable model hub with checksums, torrents and MCP](entries/2026-10-05-hugging-bay-model-hub.md) | `models` `mcp` `licensing` | Agent-searchable models with license info |
| 2026-10-05 | [Graphical: design visual languages and style components for coding agents](entries/2026-10-05-graphical-visual-language-tool.md) | `design-system` `ui` `agents` | Visual language agents can follow |
| 2026-10-04 | [Emil Kowalski skills: /mobile-native and /break-ui](entries/2026-10-04-emil-kowalski-mobile-native-break-ui.md) | `skills` `ui` `mobile` `claude-code` | Stress-test UI with a skill |
| 2026-10-04 | [Coding agent harness tier list ('Very important discussion')](entries/2026-10-04-coding-agent-tier-list.md) | `coding-agents` `harness` `comparison` | Which agent harness to use |
| 2026-10-04 | [Codex usage resets can only be used near the limit](entries/2026-10-04-codex-reset-caveat.md) | `codex` `limits` `ops` | Codex resets aren't banked capacity |
| 2026-10-04 | [A CLAUDE.md built from Boris Cherny's workflow tips](entries/2026-10-04-claude-md-best-practices.md) | `claude-code` `claude-md` `workflow` | Starter CLAUDE.md template |
| 2026-10-04 | [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md) | `claude-code` `claude-md` `workflow` `unity` | The core Claude Code habits |
| 2026-10-04 | [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md) | `agents-md` `claude-code` `codex` `workflow` | Stop pre-launch over-engineering |
| 2026-10-03 | [image-blaster: photo to explorable 3D world (repost of a May demo)](entries/2026-10-03-image-blaster-photo-to-3d-world.md) | `world-gen` `gaussian-splat` `3d` `environment` | Quick environment prototypes from a photo |
| 2026-10-03 | [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md) | `blender` `mcp` `image-to-3d` `3d-agents` | Multi-view reference to 3D via Blender MCP |
| 2026-10-03 | [Designeer: curated hub of design galleries, components, AI tools and MCP servers](entries/2026-10-03-designeer-design-resource-hub.md) | `design` `resources` `mcp` | Design reference index for store/landing pages |
| 2026-10-03 | ['I may have vibe coded the best thing ever' (video only)](entries/2026-10-03-armand-vibe-coded-setup.md) | `workstation` `music` `vibe-coding` | Workstation idea (video only) |
| 2026-10-03 | [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md) | `claude` `prompts` `threejs` `motion-graphics` | Prompt library for 3D/motion demos |
| 2026-10-02 | [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md) | `claude-code` `context` `unity` `workflow` | Cut tokens by fixing where agents get lost |
| 2026-10-02 | [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md) | `game-dev` `threejs` `blender` `claude` | Reference project: AI-built 3D game with source |
| 2026-10-02 | [Decision models on-device in llama.cpp (Kev-4B GGUF)](entries/2026-10-02-kev-4b-llamacpp.md) | `local-models` `on-device` `llama-cpp` `compression` | On-device small models via llama.cpp |
| 2026-10-02 | [FreeVideo: local video generation on 8GB VRAM](entries/2026-10-02-freevideo-local-video-gen.md) | `video-gen` `local-models` `comfyui` | Local video gen for ambient loops |
| 2026-10-02 | [Claude Code built-in plugin: You Should Know](entries/2026-10-02-claude-code-you-should-know-plugin.md) | `claude-code` `plugin` `workflow` | Surface missed warnings in long agent runs |
| 2026-10-01 | [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md) | `claude-code` `skills` `mcp` `game-dev` | Template for agent asset→test loops in games |
| 2026-10-01 | [Template 'matrix' shipping: reskinning app templates at scale (Chinese post)](entries/2026-10-01-template-matrix-shipping.md) | `strategy` `mobile` `templates` | Make non-core systems a reusable template |
| 2026-10-01 | [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md) | `cost` `claude` `openai` `subscriptions` | Which subscription is cheapest for heavy agent use |
| 2026-10-01 | [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md) | `mcp` `claude-code` `sprites` `animation` `asset-pipeline` | Agent + MCP recipe for consistent animated sprites |
| 2026-10-01 | [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md) | `video-editing` `mcp` `open-source` `marketing` | Agent-drivable video editor for trailers |
| 2026-10-01 | [Mixar: a team of AI agents that model, texture and light a 3D scene](entries/2026-10-01-mixar-multi-agent-3d.md) | `3d-agents` `scene-generation` `multi-agent` | Multi-agent 3D scene generation |
| 2026-10-01 | [Cloudflare drops 'clef' on Hugging Face (Apache 2.0)](entries/2026-10-01-cloudflare-clef-hf.md) | `open-weights` `huggingface` | Apache 2.0 Cloudflare model, check model card |
| 2026-10-01 | [Claude app: design/deck/doc work uses 50% less usage for two weeks](entries/2026-10-01-claude-design-usage-promo.md) | `claude` `design` `promo` | Cheap Claude Design usage until ~Oct 15 |
| 2026-10-01 | [ChatGPT plugin that vectorizes logos in chat](entries/2026-10-01-chatgpt-logo-vectorize-plugin.md) | `branding` `vector` `chatgpt-plugin` | Quick SVG for brand assets |
| 2026-09-30 | [Termium: Chromium inside the terminal (OSS, MIT)](entries/2026-09-30-termium-chromium-in-terminal.md) | `terminal` `browser` `agent-tooling` | Browser view inside a terminal for agents |
| 2026-09-30 | [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md) | `image-to-3d` `low-poly` `local-models` `blender` `asset-pipeline` | Free local image-to-3D that keeps texture detail at 5k faces |
| 2026-09-30 | [Ideogram 4.5: multi-turn image editing without artifact build-up](entries/2026-09-30-ideogram-4-5-precise-edit.md) | `image-editing` `concept-art` `open-weights` | Iterative edits on key art without quality decay |
| 2026-09-30 | [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md) | `blender` `benchmark` `mcp` `3d-agents` | Which model to drive Blender MCP with, per task |
| 2026-09-28 | [Opus 5.5 prompting tips from Anthropic's guide (summary)](entries/2026-09-28-opus-5-5-prompting-tips.md) | `claude` `prompting` `multi-agent` `workflow` | Concrete prompting rules for long agent runs |

## By tag
### `claude-code`
- [A Claude skill that turns an SVG into a 60 fps animation](entries/2026-10-22-svg-to-60fps-motion-skill.md)
- [Anthropic donates the Agent Skills standard to the Agentic AI Foundation](entries/2026-10-22-agent-skills-donated-to-aaif.md)
- [Overnight agent runs: skip subagents to save usage](entries/2026-10-23-skip-subagents-overnight.md)
- [tstack: Theo publishes the agent skills he uses daily](entries/2026-10-26-tstack-published-agent-skills.md)
- [A roundup of large agent and skill repos for Claude Code (and which are actually Anthropic's)](entries/2026-10-18-agent-and-skill-repo-roundup.md)
- [T3 Code impressions: multi-machine, multi-provider agent threads](entries/2026-10-19-t3code-multi-machine-agents.md)
- [Routing Claude Code work across Sonnet, Haiku and Opus by job](entries/2026-10-19-model-routing-sonnet-haiku-opus.md)
- [190 GB of leftover agent worktrees: make cleanup part of the loop](entries/2026-10-20-agent-worktree-cleanup.md)
- [Epic's Unreal Engine skills plugin lets Claude Code drive a running Unreal Editor](entries/2026-10-20-epic-unreal-engine-claude-code-plugin.md)
- [Claude Code replaces an ad-heavy Android TV launcher](entries/2026-10-17-claude-code-android-tv-launcher.md)
- [Have subagents red-team a site before shipping](entries/2026-10-16-security-red-team-subagents.md)
- [Claude Code idle compaction saves uncached-input cost](entries/2026-10-14-claude-code-idle-compaction.md)
- [X research skill + media download for video editing workflows](entries/2026-10-13-x-research-skill-video-workflows.md)
- [Claude Code hands off X research to GrokBot via a webhook skill](entries/2026-10-11-claude-code-grokbot-handoff.md)
- [oh-my-mermaid: architecture diagrams from a codebase via Claude Code](entries/2026-10-08-oh-my-mermaid-architecture-diagrams.md)
- [Emil Kowalski skills: /mobile-native and /break-ui](entries/2026-10-04-emil-kowalski-mobile-native-break-ui.md)
- [A CLAUDE.md built from Boris Cherny's workflow tips](entries/2026-10-04-claude-md-best-practices.md)
- [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md)
- [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md)
- [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md)
- [Claude Code built-in plugin: You Should Know](entries/2026-10-02-claude-code-you-should-know-plugin.md)
- [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md)
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
### `claude`
- [DeepSeek V4.1 Flash vs Opus 5.5 on a one-prompt 3D Bowser test: $0.15 vs $3.85](entries/2026-10-17-deepseek-flash-vs-opus-bowser-3d.md)
- [A benchmark of how models handle pushback: GPT-4o caves, Opus 5.5 digs in](entries/2026-10-19-sycophancy-pushback-benchmark.md)
- [How to be more ambitious with models: altitude, depth and range (plus a /be-ambitious skill)](entries/2026-10-13-be-ambitious-with-models.md)
- [Concept art to playable 3D world via blockout + painted projection](entries/2026-10-17-concept-art-to-playable-3d.md)
- [A 25-minute animated episode written entirely as code by Opus](entries/2026-10-16-claude-coded-anime-episode.md)
- [The Little Prince as a 3D story game in 16 days with Opus, Tripo and Blender](entries/2026-10-13-little-prince-3d-story-game.md)
- [Launch video from HTML + GSAP rendered by HyperFrames](entries/2026-10-08-hyperframes-launch-video.md)
- [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md)
- [Claude Startups program expands](entries/2026-10-06-claude-startups-program.md)
- [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
- [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md)
- [Claude app: design/deck/doc work uses 50% less usage for two weeks](entries/2026-10-01-claude-design-usage-promo.md)
- [Opus 5.5 prompting tips from Anthropic's guide (summary)](entries/2026-09-28-opus-5-5-prompting-tips.md)
### `marketing`
- [Analysing 4.5M TikToks: viral UGC isn't luck, and it isn't the format](entries/2026-10-20-tiktok-ugc-virality-analysis.md)
- [Lessons from a vibe-coded iOS app with 4K Reddit-only downloads](entries/2026-10-16-reddit-4k-downloads-ios-app.md)
- [An indie developer's ranking of mobile app marketing channels](entries/2026-10-13-mobile-app-marketing-channels.md)
- [Apple Search Ads playbook for indie apps](entries/2026-10-13-apple-search-ads-playbook.md)
- [Submit sitemaps to Bing Webmaster Tools and IndexNow](entries/2026-10-11-bing-indexnow-sitemap.md)
- [Launch video from HTML + GSAP rendered by HyperFrames](entries/2026-10-08-hyperframes-launch-video.md)
- [20 repos for agent-made motion design (claude-motion, HyperFrames, Remotion, GSAP)](entries/2026-10-08-20-motion-design-repos.md)
- [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md)
- [SEO: agent-assisted backlink outreach](entries/2026-10-07-agent-backlink-outreach.md)
- [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md)
### `mcp`
- [10 free repos for building 3D games with Claude Code](entries/2026-10-20-ten-repos-3d-games-claude-code.md)
- [Epic's Unreal Engine skills plugin lets Claude Code drive a running Unreal Editor](entries/2026-10-20-epic-unreal-engine-claude-code-plugin.md)
- [open-browser-use: agents drive your real, logged-in Chrome over MCP](entries/2026-10-13-open-browser-use-logged-in-chrome.md)
- [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md)
- [Build ChatGPT plugins: point Codex at openai/mcp-extensions](entries/2026-10-08-openai-mcp-extensions-chatgpt-plugins.md)
- [Hugging Bay: searchable model hub with checksums, torrents and MCP](entries/2026-10-05-hugging-bay-model-hub.md)
- [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md)
- [Designeer: curated hub of design galleries, components, AI tools and MCP servers](entries/2026-10-03-designeer-design-resource-hub.md)
- [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md)
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
- [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md)
- [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md)
### `skills`
- [A Claude skill that turns an SVG into a 60 fps animation](entries/2026-10-22-svg-to-60fps-motion-skill.md)
- [Anthropic donates the Agent Skills standard to the Agentic AI Foundation](entries/2026-10-22-agent-skills-donated-to-aaif.md)
- [tstack: Theo publishes the agent skills he uses daily](entries/2026-10-26-tstack-published-agent-skills.md)
- [A roundup of large agent and skill repos for Claude Code (and which are actually Anthropic's)](entries/2026-10-18-agent-and-skill-repo-roundup.md)
- [10 free repos for building 3D games with Claude Code](entries/2026-10-20-ten-repos-3d-games-claude-code.md)
- [Epic's Unreal Engine skills plugin lets Claude Code drive a running Unreal Editor](entries/2026-10-20-epic-unreal-engine-claude-code-plugin.md)
- [How to be more ambitious with models: altitude, depth and range (plus a /be-ambitious skill)](entries/2026-10-13-be-ambitious-with-models.md)
- [Skill Issue: agent skills ranked by what people actually use](entries/2026-10-19-skill-issue-ranked-agent-skills.md)
- [X research skill + media download for video editing workflows](entries/2026-10-13-x-research-skill-video-workflows.md)
- [Claude Code hands off X research to GrokBot via a webhook skill](entries/2026-10-11-claude-code-grokbot-handoff.md)
- [break-ui skill throws worst-case realistic data at a UI](entries/2026-10-09-break-ui-skill-praise.md)
- [anti-slop: filters generic AI-generated UI, text and code](entries/2026-10-09-anti-slop-filter.md)
- [Primitives → skills → feature loop against AI slop](entries/2026-10-08-primitives-skills-loop.md)
- [20 repos for agent-made motion design (claude-motion, HyperFrames, Remotion, GSAP)](entries/2026-10-08-20-motion-design-repos.md)
- [Emil Kowalski skills: /mobile-native and /break-ui](entries/2026-10-04-emil-kowalski-mobile-native-break-ui.md)
- [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md)
### `agents`
- [Anthropic donates the Agent Skills standard to the Agentic AI Foundation](entries/2026-10-22-agent-skills-donated-to-aaif.md)
- [A self-maintaining second-brain wiki run by three bots: reader, librarian, checker](entries/2026-10-18-three-bot-second-brain-wiki.md)
- [Phishing emails that target the AI reading your inbox](entries/2026-10-18-email-prompt-injection-ai-assistants.md)
- [A roundup of large agent and skill repos for Claude Code (and which are actually Anthropic's)](entries/2026-10-18-agent-and-skill-repo-roundup.md)
- [Genex 0.1.10: an open-source desktop app for making games with any AI, now on Windows](entries/2026-10-19-genex-open-source-ai-game-maker.md)
- [open-browser-use: agents drive your real, logged-in Chrome over MCP](entries/2026-10-13-open-browser-use-logged-in-chrome.md)
- [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md)
- [Skill Issue: agent skills ranked by what people actually use](entries/2026-10-19-skill-issue-ranked-agent-skills.md)
- [Claude Code replaces an ad-heavy Android TV launcher](entries/2026-10-17-claude-code-android-tv-launcher.md)
- [Lessons from a vibe-coded iOS app with 4K Reddit-only downloads](entries/2026-10-16-reddit-4k-downloads-ios-app.md)
- [Anthropic's Scion: source control rebuilt for agent-scale merges](entries/2026-10-13-scion-agent-scale-source-control.md)
- [Railway free Linux VMs with Claude Code/Codex preinstalled](entries/2026-10-10-railway-free-agent-vms.md)
- [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md)
- [SEO: agent-assisted backlink outreach](entries/2026-10-07-agent-backlink-outreach.md)
- [Graphical: design visual languages and style components for coding agents](entries/2026-10-05-graphical-visual-language-tool.md)
### `mobile`
- [A Claude skill that turns an SVG into a 60 fps animation](entries/2026-10-22-svg-to-60fps-motion-skill.md)
- [Seven principles for feature flags at scale on iOS](entries/2026-10-18-ios-feature-flags-principles.md)
- [Starting a first app today: web prototype first, one flow at a time](entries/2026-10-20-first-app-path-web-prototype-first.md)
- [Analysing 4.5M TikToks: viral UGC isn't luck, and it isn't the format](entries/2026-10-20-tiktok-ugc-virality-analysis.md)
- [How Block Blast! designs losses around ads](entries/2026-10-15-block-blast-ad-design-breakdown.md)
- [An indie developer's ranking of mobile app marketing channels](entries/2026-10-13-mobile-app-marketing-channels.md)
- [20 speed fixes for vibe-coded apps](entries/2026-10-12-speedmaxxing-vibe-coded-apps.md)
- [Avoiding Apple rejections for 'spam/slop' apps](entries/2026-10-09-apple-app-review-slop-rejections.md)
- [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md)
- [Emil Kowalski skills: /mobile-native and /break-ui](entries/2026-10-04-emil-kowalski-mobile-native-break-ui.md)
- [Template 'matrix' shipping: reskinning app templates at scale (Chinese post)](entries/2026-10-01-template-matrix-shipping.md)
### `workflow`
- [Primitives → skills → feature loop against AI slop](entries/2026-10-08-primitives-skills-loop.md)
- [A CLAUDE.md built from Boris Cherny's workflow tips](entries/2026-10-04-claude-md-best-practices.md)
- [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md)
- [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md)
- [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md)
- [Claude Code built-in plugin: You Should Know](entries/2026-10-02-claude-code-you-should-know-plugin.md)
- [Opus 5.5 prompting tips from Anthropic's guide (summary)](entries/2026-09-28-opus-5-5-prompting-tips.md)
### `ios`
- [Seven principles for feature flags at scale on iOS](entries/2026-10-18-ios-feature-flags-principles.md)
- [Rejected under 2.5.19 for test switches left in a release build](entries/2026-10-18-hidden-test-switches-app-review.md)
- [Checklist for fast App Store approval](entries/2026-10-18-apple-fast-approval-checklist.md)
- [Apple updates App Review Guidelines amid developer account terminations](entries/2026-10-17-app-review-guidelines-update.md)
- [App Store Review Guideline 2.5.19 and remote config / A/B testing](entries/2026-10-16-app-store-guideline-2-5-19.md)
- [Apple Search Ads playbook for indie apps](entries/2026-10-13-apple-search-ads-playbook.md)
- [Avoiding Apple rejections for 'spam/slop' apps](entries/2026-10-09-apple-app-review-slop-rejections.md)
- [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md)
### `app-store`
- [Rejected under 2.5.19 for test switches left in a release build](entries/2026-10-18-hidden-test-switches-app-review.md)
- [The "boring pages" an AI-built app still needs before launch](entries/2026-10-19-legal-pages-before-launch.md)
- [Checklist for fast App Store approval](entries/2026-10-18-apple-fast-approval-checklist.md)
- [Apple updates App Review Guidelines amid developer account terminations](entries/2026-10-17-app-review-guidelines-update.md)
- [App Store Review Guideline 2.5.19 and remote config / A/B testing](entries/2026-10-16-app-store-guideline-2-5-19.md)
- [Apple Search Ads playbook for indie apps](entries/2026-10-13-apple-search-ads-playbook.md)
- [Avoiding Apple rejections for 'spam/slop' apps](entries/2026-10-09-apple-app-review-slop-rejections.md)
### `blender`
- [Genex 0.1.10: an open-source desktop app for making games with any AI, now on Windows](entries/2026-10-19-genex-open-source-ai-game-maker.md)
- [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md)
- [The Little Prince as a 3D story game in 16 days with Opus, Tripo and Blender](entries/2026-10-13-little-prince-3d-story-game.md)
- [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
- [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md)
### `launch`
- [The "boring pages" an AI-built app still needs before launch](entries/2026-10-19-legal-pages-before-launch.md)
- [Starting a first app today: web prototype first, one flow at a time](entries/2026-10-20-first-app-path-web-prototype-first.md)
- [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md)
- [Checklist for fast App Store approval](entries/2026-10-18-apple-fast-approval-checklist.md)
- [Lessons from a vibe-coded iOS app with 4K Reddit-only downloads](entries/2026-10-16-reddit-4k-downloads-ios-app.md)
- [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md)
- [Avoiding Apple rejections for 'spam/slop' apps](entries/2026-10-09-apple-app-review-slop-rejections.md)
- [6 legal traps in AI-built apps (COPPA, GDPR fonts, CIPA, CAN-SPAM)](entries/2026-10-06-vibe-coded-app-legal-traps.md)
### `on-device`
- [Tencent Hy-MT2: 440 MB offline translator, 33 languages (Turkish post)](entries/2026-10-08-tencent-hy-mt2-offline-translator.md)
- [NeuDecide: 43 MB speech-to-tool-call model on one CPU thread](entries/2026-10-08-neudecide-audio-tool-calls.md)
- [ruNNtime: porting new models to the browser with Claude](entries/2026-10-07-ruNNtime-browser-models.md)
- [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md)
- [Decision models on-device in llama.cpp (Kev-4B GGUF)](entries/2026-10-02-kev-4b-llamacpp.md)
### `agents-md`
- [Design inspiration sites, including DESIGN.md files for agents](entries/2026-10-17-ai-design-inspiration-sites.md)
- [How to trust agents' work: the inverse pyramid](entries/2026-10-16-trust-agents-inverse-pyramid.md)
- [Primitives → skills → feature loop against AI slop](entries/2026-10-08-primitives-skills-loop.md)
- [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md)
### `audio`
- [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md)
- [10 open-source repos for an AI content pipeline](entries/2026-10-17-open-source-content-factory-repos.md)
- [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md)
- [Sound-design prompt for Opus/Fable motion design](entries/2026-10-09-opus-sound-design-prompt.md)
- [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md)
### `compression`
- [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md)
- [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md)
- [Qwen3.5 9B distilled from Kimi k3 (GGUF)](entries/2026-10-08-qwen3-5-9b-kimi-distill.md)
- [NeuDecide: 43 MB speech-to-tool-call model on one CPU thread](entries/2026-10-08-neudecide-audio-tool-calls.md)
- [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md)
- [Decision models on-device in llama.cpp (Kev-4B GGUF)](entries/2026-10-02-kev-4b-llamacpp.md)
### `context`
- [Claude Code idle compaction saves uncached-input cost](entries/2026-10-14-claude-code-idle-compaction.md)
- [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md)
- [Leviathan: agents search huge databases in ~436 tokens](entries/2026-10-05-leviathan-agent-indexer.md)
- [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md)
### `design`
- [Skill Issue: agent skills ranked by what people actually use](entries/2026-10-19-skill-issue-ranked-agent-skills.md)
- [Design inspiration sites, including DESIGN.md files for agents](entries/2026-10-17-ai-design-inspiration-sites.md)
- [Ask: a dataset of 1-10k beautiful landing pages](entries/2026-10-05-landing-page-dataset-ask.md)
- [Designeer: curated hub of design galleries, components, AI tools and MCP servers](entries/2026-10-03-designeer-design-resource-hub.md)
- [Claude app: design/deck/doc work uses 50% less usage for two weeks](entries/2026-10-01-claude-design-usage-promo.md)
### `docs`
- [How Railway grew via AI recommendations (AI SEO)](entries/2026-10-14-railway-ai-seo-playbook.md)
- [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md)
- [Prompt: output architecture as a C4 model in HTML (Japanese)](entries/2026-10-10-c4-architecture-html-prompt.md)
- [oh-my-mermaid: architecture diagrams from a codebase via Claude Code](entries/2026-10-08-oh-my-mermaid-architecture-diagrams.md)
### `game-dev`
- [Genex 0.1.10: an open-source desktop app for making games with any AI, now on Windows](entries/2026-10-19-genex-open-source-ai-game-maker.md)
- [10 free repos for building 3D games with Claude Code](entries/2026-10-20-ten-repos-3d-games-claude-code.md)
- [Epic's Unreal Engine skills plugin lets Claude Code drive a running Unreal Editor](entries/2026-10-20-epic-unreal-engine-claude-code-plugin.md)
- [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md)
- [Gemini 4 Argon builds a Subway Surfers-style flying runner](entries/2026-10-16-gemini-flying-roadster-runner.md)
- [The Little Prince as a 3D story game in 16 days with Opus, Tripo and Blender](entries/2026-10-13-little-prince-3d-story-game.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
- [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md)
### `local-models`
- [Genex 0.1.10: an open-source desktop app for making games with any AI, now on Windows](entries/2026-10-19-genex-open-source-ai-game-maker.md)
- [Qwen3.5 9B distilled from Kimi k3 (GGUF)](entries/2026-10-08-qwen3-5-9b-kimi-distill.md)
- [Decision models on-device in llama.cpp (Kev-4B GGUF)](entries/2026-10-02-kev-4b-llamacpp.md)
- [FreeVideo: local video generation on 8GB VRAM](entries/2026-10-02-freevideo-local-video-gen.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
### `motion-graphics`
- [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md)
- [Sound-design prompt for Opus/Fable motion design](entries/2026-10-09-opus-sound-design-prompt.md)
- [Launch video from HTML + GSAP rendered by HyperFrames](entries/2026-10-08-hyperframes-launch-video.md)
- [20 repos for agent-made motion design (claude-motion, HyperFrames, Remotion, GSAP)](entries/2026-10-08-20-motion-design-repos.md)
- [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md)
### `subscriptions`
- [Checklist for fast App Store approval](entries/2026-10-18-apple-fast-approval-checklist.md)
- [Don't report instantly cancelled trials to Meta](entries/2026-10-12-meta-ads-filter-instant-cancels.md)
- [6 legal traps in AI-built apps (COPPA, GDPR fonts, CIPA, CAN-SPAM)](entries/2026-10-06-vibe-coded-app-legal-traps.md)
- [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md)
### `testing`
- [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md)
- [Have subagents red-team a site before shipping](entries/2026-10-16-security-red-team-subagents.md)
- [break-ui skill throws worst-case realistic data at a UI](entries/2026-10-09-break-ui-skill-praise.md)
- [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md)
- [Evidence: agent-written unit/integration tests don't improve success](entries/2026-10-08-ai-written-tests-dont-help.md)
### `threejs`
- [10 free repos for building 3D games with Claude Code](entries/2026-10-20-ten-repos-3d-games-claude-code.md)
- [10 resources for AI-assisted 3D and animated web design](entries/2026-10-18-web-3d-design-resource-list.md)
- [A 25-minute animated episode written entirely as code by Opus](entries/2026-10-16-claude-coded-anime-episode.md)
- [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
### `ui`
- [A Claude skill that turns an SVG into a 60 fps animation](entries/2026-10-22-svg-to-60fps-motion-skill.md)
- [Design inspiration sites, including DESIGN.md files for agents](entries/2026-10-17-ai-design-inspiration-sites.md)
- [break-ui skill throws worst-case realistic data at a UI](entries/2026-10-09-break-ui-skill-praise.md)
- [Graphical: design visual languages and style components for coding agents](entries/2026-10-05-graphical-visual-language-tool.md)
- [Emil Kowalski skills: /mobile-native and /break-ui](entries/2026-10-04-emil-kowalski-mobile-native-break-ui.md)
### `video`
- [10 open-source repos for an AI content pipeline](entries/2026-10-17-open-source-content-factory-repos.md)
- [X research skill + media download for video editing workflows](entries/2026-10-13-x-research-skill-video-workflows.md)
- [Launch video from HTML + GSAP rendered by HyperFrames](entries/2026-10-08-hyperframes-launch-video.md)
- [20 repos for agent-made motion design (claude-motion, HyperFrames, Remotion, GSAP)](entries/2026-10-08-20-motion-design-repos.md)
### `3d`
- [DeepSeek V4.1 Flash vs Opus 5.5 on a one-prompt 3D Bowser test: $0.15 vs $3.85](entries/2026-10-17-deepseek-flash-vs-opus-bowser-3d.md)
- [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md)
- [Concept art to playable 3D world via blockout + painted projection](entries/2026-10-17-concept-art-to-playable-3d.md)
- [The Little Prince as a 3D story game in 16 days with Opus, Tripo and Blender](entries/2026-10-13-little-prince-3d-story-game.md)
- [image-blaster: photo to explorable 3D world (repost of a May demo)](entries/2026-10-03-image-blaster-photo-to-3d-world.md)
### `3d-agents`
- [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md)
- [Mixar: a team of AI agents that model, texture and light a 3D scene](entries/2026-10-01-mixar-multi-agent-3d.md)
- [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md)
### `ads`
- [How Block Blast! designs losses around ads](entries/2026-10-15-block-blast-ad-design-breakdown.md)
- [Apple Search Ads playbook for indie apps](entries/2026-10-13-apple-search-ads-playbook.md)
- [Don't report instantly cancelled trials to Meta](entries/2026-10-12-meta-ads-filter-instant-cancels.md)
### `agent-workflow`
- [Overnight agent runs: skip subagents to save usage](entries/2026-10-23-skip-subagents-overnight.md)
- [tstack: Theo publishes the agent skills he uses daily](entries/2026-10-26-tstack-published-agent-skills.md)
- [A self-maintaining second-brain wiki run by three bots: reader, librarian, checker](entries/2026-10-18-three-bot-second-brain-wiki.md)
- [A benchmark of how models handle pushback: GPT-4o caves, Opus 5.5 digs in](entries/2026-10-19-sycophancy-pushback-benchmark.md)
- [Routing Claude Code work across Sonnet, Haiku and Opus by job](entries/2026-10-19-model-routing-sonnet-haiku-opus.md)
- [Starting a first app today: web prototype first, one flow at a time](entries/2026-10-20-first-app-path-web-prototype-first.md)
- [190 GB of leftover agent worktrees: make cleanup part of the loop](entries/2026-10-20-agent-worktree-cleanup.md)
- [How to be more ambitious with models: altitude, depth and range (plus a /be-ambitious skill)](entries/2026-10-13-be-ambitious-with-models.md)
- [How to trust agents' work: the inverse pyramid](entries/2026-10-16-trust-agents-inverse-pyramid.md)
- [Solo developer's 50-agent stack: $545k MRR, 1,089 PRs in a week](entries/2026-10-13-solo-dev-50-agent-stack.md)
- [Codex memory: swap the default memory models in config](entries/2026-10-13-codex-memory-model-upgrade.md)
### `asset-pipeline`
- [DeepSeek V4.1 Flash vs Opus 5.5 on a one-prompt 3D Bowser test: $0.15 vs $3.85](entries/2026-10-17-deepseek-flash-vs-opus-bowser-3d.md)
- [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md)
- [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md)
- [Concept art to playable 3D world via blockout + painted projection](entries/2026-10-17-concept-art-to-playable-3d.md)
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
### `checklist`
- [The "boring pages" an AI-built app still needs before launch](entries/2026-10-19-legal-pages-before-launch.md)
- [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md)
- [Have subagents audit 20 web performance issues](entries/2026-10-13-perf-audit-subagents.md)
- [20 speed fixes for vibe-coded apps](entries/2026-10-12-speedmaxxing-vibe-coded-apps.md)
- [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md)
### `codex`
- [Anthropic donates the Agent Skills standard to the Agentic AI Foundation](entries/2026-10-22-agent-skills-donated-to-aaif.md)
- [tstack: Theo publishes the agent skills he uses daily](entries/2026-10-26-tstack-published-agent-skills.md)
- [T3 Code impressions: multi-machine, multi-provider agent threads](entries/2026-10-19-t3code-multi-machine-agents.md)
- [Codex memory: swap the default memory models in config](entries/2026-10-13-codex-memory-model-upgrade.md)
- [Codex usage resets can only be used near the limit](entries/2026-10-04-codex-reset-caveat.md)
- [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md)
### `cost`
- [Overnight agent runs: skip subagents to save usage](entries/2026-10-23-skip-subagents-overnight.md)
- [DeepSeek V4.1 Flash vs Opus 5.5 on a one-prompt 3D Bowser test: $0.15 vs $3.85](entries/2026-10-17-deepseek-flash-vs-opus-bowser-3d.md)
- [Routing Claude Code work across Sonnet, Haiku and Opus by job](entries/2026-10-19-model-routing-sonnet-haiku-opus.md)
- [A 25-minute animated episode written entirely as code by Opus](entries/2026-10-16-claude-coded-anime-episode.md)
- [Claude Code idle compaction saves uncached-input cost](entries/2026-10-14-claude-code-idle-compaction.md)
- [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md)
### `image-to-3d`
- [The Little Prince as a 3D story game in 16 days with Opus, Tripo and Blender](entries/2026-10-13-little-prince-3d-story-game.md)
- [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
### `multi-agent`
- [Claude Code hands off X research to GrokBot via a webhook skill](entries/2026-10-11-claude-code-grokbot-handoff.md)
- [Mixar: a team of AI agents that model, texture and light a 3D scene](entries/2026-10-01-mixar-multi-agent-3d.md)
- [Opus 5.5 prompting tips from Anthropic's guide (summary)](entries/2026-09-28-opus-5-5-prompting-tips.md)
### `open-source`
- [tstack: Theo publishes the agent skills he uses daily](entries/2026-10-26-tstack-published-agent-skills.md)
- [T3 Code impressions: multi-machine, multi-provider agent threads](entries/2026-10-19-t3code-multi-machine-agents.md)
- [Genex 0.1.10: an open-source desktop app for making games with any AI, now on Windows](entries/2026-10-19-genex-open-source-ai-game-maker.md)
- [10 free repos for building 3D games with Claude Code](entries/2026-10-20-ten-repos-3d-games-claude-code.md)
- [open-browser-use: agents drive your real, logged-in Chrome over MCP](entries/2026-10-13-open-browser-use-logged-in-chrome.md)
- [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md)
- [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md)
- [10 open-source repos for an AI content pipeline](entries/2026-10-17-open-source-content-factory-repos.md)
- [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md)
- [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md)
### `prompts`
- [Prompt: output architecture as a C4 model in HTML (Japanese)](entries/2026-10-10-c4-architecture-html-prompt.md)
- [Sound-design prompt for Opus/Fable motion design](entries/2026-10-09-opus-sound-design-prompt.md)
- [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md)
### `resources`
- [A roundup of large agent and skill repos for Claude Code (and which are actually Anthropic's)](entries/2026-10-18-agent-and-skill-repo-roundup.md)
- [10 free repos for building 3D games with Claude Code](entries/2026-10-20-ten-repos-3d-games-claude-code.md)
- [Skill Issue: agent skills ranked by what people actually use](entries/2026-10-19-skill-issue-ranked-agent-skills.md)
- [10 resources for AI-assisted 3D and animated web design](entries/2026-10-18-web-3d-design-resource-list.md)
- [Design inspiration sites, including DESIGN.md files for agents](entries/2026-10-17-ai-design-inspiration-sites.md)
- [Designeer: curated hub of design galleries, components, AI tools and MCP servers](entries/2026-10-03-designeer-design-resource-hub.md)
### `seo`
- [How Railway grew via AI recommendations (AI SEO)](entries/2026-10-14-railway-ai-seo-playbook.md)
- [Submit sitemaps to Bing Webmaster Tools and IndexNow](entries/2026-10-11-bing-indexnow-sitemap.md)
- [SEO: agent-assisted backlink outreach](entries/2026-10-07-agent-backlink-outreach.md)
### `agent-tooling`
- [Anthropic donates the Agent Skills standard to the Agentic AI Foundation](entries/2026-10-22-agent-skills-donated-to-aaif.md)
- [T3 Code impressions: multi-machine, multi-provider agent threads](entries/2026-10-19-t3code-multi-machine-agents.md)
- [Epic's Unreal Engine skills plugin lets Claude Code drive a running Unreal Editor](entries/2026-10-20-epic-unreal-engine-claude-code-plugin.md)
- [open-browser-use: agents drive your real, logged-in Chrome over MCP](entries/2026-10-13-open-browser-use-logged-in-chrome.md)
- [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md)
- [Leviathan: agents search huge databases in ~436 tokens](entries/2026-10-05-leviathan-agent-indexer.md)
- [Termium: Chromium inside the terminal (OSS, MIT)](entries/2026-09-30-termium-chromium-in-terminal.md)
### `analytics`
- [Lessons from a vibe-coded iOS app with 4K Reddit-only downloads](entries/2026-10-16-reddit-4k-downloads-ios-app.md)
- [Don't report instantly cancelled trials to Meta](entries/2026-10-12-meta-ads-filter-instant-cancels.md)
### `android`
- [Claude Code replaces an ad-heavy Android TV launcher](entries/2026-10-17-claude-code-android-tv-launcher.md)
- [Google Play lets you install private vibe-coded apps](entries/2026-10-13-google-play-private-vibe-coded-apps.md)
### `animation`
- [A Claude skill that turns an SVG into a 60 fps animation](entries/2026-10-22-svg-to-60fps-motion-skill.md)
- [A 25-minute animated episode written entirely as code by Opus](entries/2026-10-16-claude-coded-anime-episode.md)
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
### `browser`
- [open-browser-use: agents drive your real, logged-in Chrome over MCP](entries/2026-10-13-open-browser-use-logged-in-chrome.md)
- [ruNNtime: porting new models to the browser with Claude](entries/2026-10-07-ruNNtime-browser-models.md)
- [Termium: Chromium inside the terminal (OSS, MIT)](entries/2026-09-30-termium-chromium-in-terminal.md)
### `chatgpt-plugin`
- [Build ChatGPT plugins: point Codex at openai/mcp-extensions](entries/2026-10-08-openai-mcp-extensions-chatgpt-plugins.md)
- [ChatGPT plugin that vectorizes logos in chat](entries/2026-10-01-chatgpt-logo-vectorize-plugin.md)
### `ci`
- [Solo developer's 50-agent stack: $545k MRR, 1,089 PRs in a week](entries/2026-10-13-solo-dev-50-agent-stack.md)
- [Anthropic's Scion: source control rebuilt for agent-scale merges](entries/2026-10-13-scion-agent-scale-source-control.md)
### `claude-md`
- [A CLAUDE.md built from Boris Cherny's workflow tips](entries/2026-10-04-claude-md-best-practices.md)
- [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md)
### `coding-agents`
- [Evidence: agent-written unit/integration tests don't improve success](entries/2026-10-08-ai-written-tests-dont-help.md)
- [Coding agent harness tier list ('Very important discussion')](entries/2026-10-04-coding-agent-tier-list.md)
### `compliance`
- [Rejected under 2.5.19 for test switches left in a release build](entries/2026-10-18-hidden-test-switches-app-review.md)
- [Apple updates App Review Guidelines amid developer account terminations](entries/2026-10-17-app-review-guidelines-update.md)
- [App Store Review Guideline 2.5.19 and remote config / A/B testing](entries/2026-10-16-app-store-guideline-2-5-19.md)
### `concept-art`
- [Concept art to playable 3D world via blockout + painted projection](entries/2026-10-17-concept-art-to-playable-3d.md)
- [Ideogram 4.5: multi-turn image editing without artifact build-up](entries/2026-09-30-ideogram-4-5-precise-edit.md)
### `distribution`
- [Google Play lets you install private vibe-coded apps](entries/2026-10-13-google-play-private-vibe-coded-apps.md)
- [Build ChatGPT plugins: point Codex at openai/mcp-extensions](entries/2026-10-08-openai-mcp-extensions-chatgpt-plugins.md)
### `infra`
- [Anthropic's Scion: source control rebuilt for agent-scale merges](entries/2026-10-13-scion-agent-scale-source-control.md)
- [Railway free Linux VMs with Claude Code/Codex preinstalled](entries/2026-10-10-railway-free-agent-vms.md)
### `music`
- [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md)
- ['I may have vibe coded the best thing ever' (video only)](entries/2026-10-03-armand-vibe-coded-setup.md)
### `open-weights`
- [Cloudflare drops 'clef' on Hugging Face (Apache 2.0)](entries/2026-10-01-cloudflare-clef-hf.md)
- [Ideogram 4.5: multi-turn image editing without artifact build-up](entries/2026-09-30-ideogram-4-5-precise-edit.md)
### `performance`
- [Have subagents audit 20 web performance issues](entries/2026-10-13-perf-audit-subagents.md)
- [20 speed fixes for vibe-coded apps](entries/2026-10-12-speedmaxxing-vibe-coded-apps.md)
### `prototyping`
- [Starting a first app today: web prototype first, one flow at a time](entries/2026-10-20-first-app-path-web-prototype-first.md)
- [Gemini 4 Argon builds a Subway Surfers-style flying runner](entries/2026-10-16-gemini-flying-roadster-runner.md)
- [Google Play lets you install private vibe-coded apps](entries/2026-10-13-google-play-private-vibe-coded-apps.md)
### `research`
- [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md)
- [X research skill + media download for video editing workflows](entries/2026-10-13-x-research-skill-video-workflows.md)
- [Claude Code hands off X research to GrokBot via a webhook skill](entries/2026-10-11-claude-code-grokbot-handoff.md)
### `security`
- [Take your VPS off the public internet with Tailscale and Cloudflare Tunnel](entries/2026-10-23-vps-tailscale-cloudflare-tunnel.md)
- [Phishing emails that target the AI reading your inbox](entries/2026-10-18-email-prompt-injection-ai-assistants.md)
- [A roundup of large agent and skill repos for Claude Code (and which are actually Anthropic's)](entries/2026-10-18-agent-and-skill-repo-roundup.md)
- [open-browser-use: agents drive your real, logged-in Chrome over MCP](entries/2026-10-13-open-browser-use-logged-in-chrome.md)
- [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md)
- [Have subagents red-team a site before shipping](entries/2026-10-16-security-red-team-subagents.md)
- [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md)
### `subagents`
- [Overnight agent runs: skip subagents to save usage](entries/2026-10-23-skip-subagents-overnight.md)
- [Routing Claude Code work across Sonnet, Haiku and Opus by job](entries/2026-10-19-model-routing-sonnet-haiku-opus.md)
- [Have subagents red-team a site before shipping](entries/2026-10-16-security-red-team-subagents.md)
- [Have subagents audit 20 web performance issues](entries/2026-10-13-perf-audit-subagents.md)
### `tts`
- [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md)
- [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md)
### `unity`
- [Rejected under 2.5.19 for test switches left in a release build](entries/2026-10-18-hidden-test-switches-app-review.md)
- [Genex 0.1.10: an open-source desktop app for making games with any AI, now on Windows](entries/2026-10-19-genex-open-source-ai-game-maker.md)
- [10 free repos for building 3D games with Claude Code](entries/2026-10-20-ten-repos-3d-games-claude-code.md)
- [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md)
- [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md)
### `video-editing`
- [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md)
- [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md)
### `ab-testing`
- [Seven principles for feature flags at scale on iOS](entries/2026-10-18-ios-feature-flags-principles.md)
- [App Store Review Guideline 2.5.19 and remote config / A/B testing](entries/2026-10-16-app-store-guideline-2-5-19.md)
### `ai-search`
- [How Railway grew via AI recommendations (AI SEO)](entries/2026-10-14-railway-ai-seo-playbook.md)
### `architecture`
- [Prompt: output architecture as a C4 model in HTML (Japanese)](entries/2026-10-10-c4-architecture-html-prompt.md)
### `aso`
- [An indie developer's ranking of mobile app marketing channels](entries/2026-10-13-mobile-app-marketing-channels.md)
### `benchmark`
- [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md)
### `branding`
- [ChatGPT plugin that vectorizes logos in chat](entries/2026-10-01-chatgpt-logo-vectorize-plugin.md)
### `browser-games`
- [Gemini 4 Argon builds a Subway Surfers-style flying runner](entries/2026-10-16-gemini-flying-roadster-runner.md)
### `code-quality`
- [How to trust agents' work: the inverse pyramid](entries/2026-10-16-trust-agents-inverse-pyramid.md)
### `code-review`
- [tstack: Theo publishes the agent skills he uses daily](entries/2026-10-26-tstack-published-agent-skills.md)
- [Solo developer's 50-agent stack: $545k MRR, 1,089 PRs in a week](entries/2026-10-13-solo-dev-50-agent-stack.md)
### `coding`
- [Qwen3.5 9B distilled from Kimi k3 (GGUF)](entries/2026-10-08-qwen3-5-9b-kimi-distill.md)
### `comfyui`
- [FreeVideo: local video generation on 8GB VRAM](entries/2026-10-02-freevideo-local-video-gen.md)
### `comparison`
- [Coding agent harness tier list ('Very important discussion')](entries/2026-10-04-coding-agent-tier-list.md)
### `config`
- [Codex memory: swap the default memory models in config](entries/2026-10-13-codex-memory-model-upgrade.md)
### `content`
- [10 open-source repos for an AI content pipeline](entries/2026-10-17-open-source-content-factory-repos.md)
### `credits`
- [Claude Startups program expands](entries/2026-10-06-claude-startups-program.md)
### `design-system`
- [Graphical: design visual languages and style components for coding agents](entries/2026-10-05-graphical-visual-language-tool.md)
### `devices`
- [Claude Code replaces an ad-heavy Android TV launcher](entries/2026-10-17-claude-code-android-tv-launcher.md)
### `diagrams`
- [oh-my-mermaid: architecture diagrams from a codebase via Claude Code](entries/2026-10-08-oh-my-mermaid-architecture-diagrams.md)
### `distillation`
- [Qwen3.5 9B distilled from Kimi k3 (GGUF)](entries/2026-10-08-qwen3-5-9b-kimi-distill.md)
### `environment`
- [image-blaster: photo to explorable 3D world (repost of a May demo)](entries/2026-10-03-image-blaster-photo-to-3d-world.md)
### `evals`
- [Evidence: agent-written unit/integration tests don't improve success](entries/2026-10-08-ai-written-tests-dont-help.md)
### `ffmpeg`
- [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md)
### `game-design`
- [How Block Blast! designs losses around ads](entries/2026-10-15-block-blast-ad-design-breakdown.md)
### `gaussian-splat`
- [image-blaster: photo to explorable 3D world (repost of a May demo)](entries/2026-10-03-image-blaster-photo-to-3d-world.md)
### `gemini`
- [Gemini 4 Argon builds a Subway Surfers-style flying runner](entries/2026-10-16-gemini-flying-roadster-runner.md)
### `google-play`
- [Google Play lets you install private vibe-coded apps](entries/2026-10-13-google-play-private-vibe-coded-apps.md)
### `growth`
- [Analysing 4.5M TikToks: viral UGC isn't luck, and it isn't the format](entries/2026-10-20-tiktok-ugc-virality-analysis.md)
- [How Railway grew via AI recommendations (AI SEO)](entries/2026-10-14-railway-ai-seo-playbook.md)
### `harness`
- [Coding agent harness tier list ('Very important discussion')](entries/2026-10-04-coding-agent-tier-list.md)
### `huggingface`
- [Cloudflare drops 'clef' on Hugging Face (Apache 2.0)](entries/2026-10-01-cloudflare-clef-hf.md)
### `image-editing`
- [Ideogram 4.5: multi-turn image editing without artifact build-up](entries/2026-09-30-ideogram-4-5-precise-edit.md)
### `indexing`
- [Submit sitemaps to Bing Webmaster Tools and IndexNow](entries/2026-10-11-bing-indexnow-sitemap.md)
### `landing-page`
- [Ask: a dataset of 1-10k beautiful landing pages](entries/2026-10-05-landing-page-dataset-ask.md)
### `legal`
- [The "boring pages" an AI-built app still needs before launch](entries/2026-10-19-legal-pages-before-launch.md)
- [6 legal traps in AI-built apps (COPPA, GDPR fonts, CIPA, CAN-SPAM)](entries/2026-10-06-vibe-coded-app-legal-traps.md)
### `licensing`
- [Hugging Bay: searchable model hub with checksums, torrents and MCP](entries/2026-10-05-hugging-bay-model-hub.md)
### `limits`
- [Codex usage resets can only be used near the limit](entries/2026-10-04-codex-reset-caveat.md)
### `llama-cpp`
- [Decision models on-device in llama.cpp (Kev-4B GGUF)](entries/2026-10-02-kev-4b-llamacpp.md)
### `localization`
- [Tencent Hy-MT2: 440 MB offline translator, 33 languages (Turkish post)](entries/2026-10-08-tencent-hy-mt2-offline-translator.md)
### `low-poly`
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
### `memory`
- [A self-maintaining second-brain wiki run by three bots: reader, librarian, checker](entries/2026-10-18-three-bot-second-brain-wiki.md)
- [Codex memory: swap the default memory models in config](entries/2026-10-13-codex-memory-model-upgrade.md)
### `model-porting`
- [ruNNtime: porting new models to the browser with Claude](entries/2026-10-07-ruNNtime-browser-models.md)
### `models`
- [DeepSeek V4.1 Flash vs Opus 5.5 on a one-prompt 3D Bowser test: $0.15 vs $3.85](entries/2026-10-17-deepseek-flash-vs-opus-bowser-3d.md)
- [A benchmark of how models handle pushback: GPT-4o caves, Opus 5.5 digs in](entries/2026-10-19-sycophancy-pushback-benchmark.md)
- [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md)
- [Hugging Bay: searchable model hub with checksums, torrents and MCP](entries/2026-10-05-hugging-bay-model-hub.md)
### `monetization`
- [How Block Blast! designs losses around ads](entries/2026-10-15-block-blast-ad-design-breakdown.md)
### `motion`
- [10 resources for AI-assisted 3D and animated web design](entries/2026-10-18-web-3d-design-resource-list.md)
### `openai`
- [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md)
### `ops`
- [190 GB of leftover agent worktrees: make cleanup part of the loop](entries/2026-10-20-agent-worktree-cleanup.md)
- [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md)
- [Codex usage resets can only be used near the limit](entries/2026-10-04-codex-reset-caveat.md)
### `orchestration`
- [Solo developer's 50-agent stack: $545k MRR, 1,089 PRs in a week](entries/2026-10-13-solo-dev-50-agent-stack.md)
### `pdf`
- [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md)
### `plugin`
- [Claude Code built-in plugin: You Should Know](entries/2026-10-02-claude-code-you-should-know-plugin.md)
### `privacy`
- [The "boring pages" an AI-built app still needs before launch](entries/2026-10-19-legal-pages-before-launch.md)
- [6 legal traps in AI-built apps (COPPA, GDPR fonts, CIPA, CAN-SPAM)](entries/2026-10-06-vibe-coded-app-legal-traps.md)
### `promo`
- [Claude app: design/deck/doc work uses 50% less usage for two weeks](entries/2026-10-01-claude-design-usage-promo.md)
### `prompting`
- [How to be more ambitious with models: altitude, depth and range (plus a /be-ambitious skill)](entries/2026-10-13-be-ambitious-with-models.md)
- [Opus 5.5 prompting tips from Anthropic's guide (summary)](entries/2026-09-28-opus-5-5-prompting-tips.md)
### `quality`
- [How to be more ambitious with models: altitude, depth and range (plus a /be-ambitious skill)](entries/2026-10-13-be-ambitious-with-models.md)
- [anti-slop: filters generic AI-generated UI, text and code](entries/2026-10-09-anti-slop-filter.md)
### `retrieval`
- [Leviathan: agents search huge databases in ~436 tokens](entries/2026-10-05-leviathan-agent-indexer.md)
### `sandbox`
- [Railway free Linux VMs with Claude Code/Codex preinstalled](entries/2026-10-10-railway-free-agent-vms.md)
### `scene-generation`
- [Mixar: a team of AI agents that model, texture and light a 3D scene](entries/2026-10-01-mixar-multi-agent-3d.md)
### `shaders`
- [Concept art to playable 3D world via blockout + painted projection](entries/2026-10-17-concept-art-to-playable-3d.md)
### `source-control`
- [Anthropic's Scion: source control rebuilt for agent-scale merges](entries/2026-10-13-scion-agent-scale-source-control.md)
### `sprites`
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
### `startup-programs`
- [Claude Startups program expands](entries/2026-10-06-claude-startups-program.md)
### `static-analysis`
- [How to trust agents' work: the inverse pyramid](entries/2026-10-16-trust-agents-inverse-pyramid.md)
### `strategy`
- [Template 'matrix' shipping: reskinning app templates at scale (Chinese post)](entries/2026-10-01-template-matrix-shipping.md)
### `templates`
- [Template 'matrix' shipping: reskinning app templates at scale (Chinese post)](entries/2026-10-01-template-matrix-shipping.md)
### `terminal`
- [Termium: Chromium inside the terminal (OSS, MIT)](entries/2026-09-30-termium-chromium-in-terminal.md)
### `tool-calling`
- [NeuDecide: 43 MB speech-to-tool-call model on one CPU thread](entries/2026-10-08-neudecide-audio-tool-calls.md)
### `tools`
- [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md)
### `translation`
- [Tencent Hy-MT2: 440 MB offline translator, 33 languages (Turkish post)](entries/2026-10-08-tencent-hy-mt2-offline-translator.md)
### `ugc`
- [Analysing 4.5M TikToks: viral UGC isn't luck, and it isn't the format](entries/2026-10-20-tiktok-ugc-virality-analysis.md)
- [An indie developer's ranking of mobile app marketing channels](entries/2026-10-13-mobile-app-marketing-channels.md)
### `vector`
- [ChatGPT plugin that vectorizes logos in chat](entries/2026-10-01-chatgpt-logo-vectorize-plugin.md)
### `vibe-coding`
- [Starting a first app today: web prototype first, one flow at a time](entries/2026-10-20-first-app-path-web-prototype-first.md)
- [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md)
- ['I may have vibe coded the best thing ever' (video only)](entries/2026-10-03-armand-vibe-coded-setup.md)
### `video-gen`
- [FreeVideo: local video generation on 8GB VRAM](entries/2026-10-02-freevideo-local-video-gen.md)
### `voice`
- [NeuDecide: 43 MB speech-to-tool-call model on one CPU thread](entries/2026-10-08-neudecide-audio-tool-calls.md)
### `web`
- [Have subagents audit 20 web performance issues](entries/2026-10-13-perf-audit-subagents.md)
### `web-design`
- [10 resources for AI-assisted 3D and animated web design](entries/2026-10-18-web-3d-design-resource-list.md)
### `workstation`
- ['I may have vibe coded the best thing ever' (video only)](entries/2026-10-03-armand-vibe-coded-setup.md)
### `world-gen`
- [image-blaster: photo to explorable 3D world (repost of a May demo)](entries/2026-10-03-image-blaster-photo-to-3d-world.md)
### `writing`
- [anti-slop: filters generic AI-generated UI, text and code](entries/2026-10-09-anti-slop-filter.md)
### `cad`
- [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md)
### `world-models`
- [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md)
### `sfx`
- [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md)
### `cli`
- [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md)
### `unreal`
- [Epic's Unreal Engine skills plugin lets Claude Code drive a running Unreal Editor](entries/2026-10-20-epic-unreal-engine-claude-code-plugin.md)
### `godot`
- [10 free repos for building 3D games with Claude Code](entries/2026-10-20-ten-repos-3d-games-claude-code.md)
- [Genex 0.1.10: an open-source desktop app for making games with any AI, now on Windows](entries/2026-10-19-genex-open-source-ai-game-maker.md)
### `worktrees`
- [190 GB of leftover agent worktrees: make cleanup part of the loop](entries/2026-10-20-agent-worktree-cleanup.md)
### `disk`
- [190 GB of leftover agent worktrees: make cleanup part of the loop](entries/2026-10-20-agent-worktree-cleanup.md)
### `tiktok`
- [Analysing 4.5M TikToks: viral UGC isn't luck, and it isn't the format](entries/2026-10-20-tiktok-ugc-virality-analysis.md)
### `model-routing`
- [Routing Claude Code work across Sonnet, Haiku and Opus by job](entries/2026-10-19-model-routing-sonnet-haiku-opus.md)
### `benchmarks`
- [A benchmark of how models handle pushback: GPT-4o caves, Opus 5.5 digs in](entries/2026-10-19-sycophancy-pushback-benchmark.md)
- [DeepSeek V4.1 Flash vs Opus 5.5 on a one-prompt 3D Bowser test: $0.15 vs $3.85](entries/2026-10-17-deepseek-flash-vs-opus-bowser-3d.md)
### `sycophancy`
- [A benchmark of how models handle pushback: GPT-4o caves, Opus 5.5 digs in](entries/2026-10-19-sycophancy-pushback-benchmark.md)
### `multi-machine`
- [T3 Code impressions: multi-machine, multi-provider agent threads](entries/2026-10-19-t3code-multi-machine-agents.md)
### `plugins`
- [A roundup of large agent and skill repos for Claude Code (and which are actually Anthropic's)](entries/2026-10-18-agent-and-skill-repo-roundup.md)
### `prompt-injection`
- [Phishing emails that target the AI reading your inbox](entries/2026-10-18-email-prompt-injection-ai-assistants.md)
### `email`
- [Phishing emails that target the AI reading your inbox](entries/2026-10-18-email-prompt-injection-ai-assistants.md)
### `release`
- [Rejected under 2.5.19 for test switches left in a release build](entries/2026-10-18-hidden-test-switches-app-review.md)
### `feature-flags`
- [Seven principles for feature flags at scale on iOS](entries/2026-10-18-ios-feature-flags-principles.md)
### `live-ops`
- [Seven principles for feature flags at scale on iOS](entries/2026-10-18-ios-feature-flags-principles.md)
### `knowledge-base`
- [A self-maintaining second-brain wiki run by three bots: reader, librarian, checker](entries/2026-10-18-three-bot-second-brain-wiki.md)
### `wiki`
- [A self-maintaining second-brain wiki run by three bots: reader, librarian, checker](entries/2026-10-18-three-bot-second-brain-wiki.md)
### `deepseek`
- [DeepSeek V4.1 Flash vs Opus 5.5 on a one-prompt 3D Bowser test: $0.15 vs $3.85](entries/2026-10-17-deepseek-flash-vs-opus-bowser-3d.md)
### `github`
- [tstack: Theo publishes the agent skills he uses daily](entries/2026-10-26-tstack-published-agent-skills.md)
### `devops`
- [Take your VPS off the public internet with Tailscale and Cloudflare Tunnel](entries/2026-10-23-vps-tailscale-cloudflare-tunnel.md)
### `vps`
- [Take your VPS off the public internet with Tailscale and Cloudflare Tunnel](entries/2026-10-23-vps-tailscale-cloudflare-tunnel.md)
### `networking`
- [Take your VPS off the public internet with Tailscale and Cloudflare Tunnel](entries/2026-10-23-vps-tailscale-cloudflare-tunnel.md)
### `infrastructure`
- [Take your VPS off the public internet with Tailscale and Cloudflare Tunnel](entries/2026-10-23-vps-tailscale-cloudflare-tunnel.md)
### `usage-limits`
- [Overnight agent runs: skip subagents to save usage](entries/2026-10-23-skip-subagents-overnight.md)
### `standards`
- [Anthropic donates the Agent Skills standard to the Agentic AI Foundation](entries/2026-10-22-agent-skills-donated-to-aaif.md)
### `svg`
- [A Claude skill that turns an SVG into a 60 fps animation](entries/2026-10-22-svg-to-60fps-motion-skill.md)
