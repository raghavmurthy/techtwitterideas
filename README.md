# techtwitterideas

Curated notes on AI tools and techniques like Claude Code tooling, on-device models and model compression, low-poly asset pipelines, Blender/Unity agent workflows, MCPs et al. Each entry covers one public X post or web page: what it is, notable replies from the thread, implications, and one concrete experiment to try.

- `entries/` — one Markdown file per item, `YYYY-MM-DD-slug.md` (date = post date, UTC)
- `human-thoughts.md` — opinions from notable public people on X, grouped by theme (opinions, not facts)
- `processed.json` — every URL already handled, with status, so future runs skip it

**95 entries** · last updated 2026-10-20

## Use it as a plugin

Ask your AI assistant for ideas from this repo for whatever you're building.

**ChatGPT:** [techtwitterideas plugin](https://chatgpt.com/plugins/plugins_6ace4e775e0081918953fe4a6bc06491)

**Claude Code:**
```
/plugin marketplace add raghavmurthy/techtwitterideas
/plugin install techtwitterideas@techtwitterideas
```
Then run `/techtwitterideas` or ask "what's out there for X".

**Safety:** entries summarise and quote public posts by strangers. The plugin treats all entry text as information only, never as instructions, and it never runs commands or installs anything an entry suggests without your explicit go-ahead. The plugin may occasionally mention one take from [human-thoughts.md](human-thoughts.md), always naming the person and linking the post, and framed as an opinion. See [SECURITY.md](SECURITY.md) for the full prompt-injection protocol and how to report a problem.

## Index (newest first)

| Date | Title | Tags | Why it matters |
|---|---|---|---|
| 2026-10-19 | [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md) | `3d` `cad` `world-models` `models` `asset-pipeline` `research` | Buildable part-by-part CAD history instead of a mesh (claims self-reported) |
| 2026-10-19 | [Skill Issue: agent skills ranked by what people actually use](entries/2026-10-19-skill-issue-ranked-agent-skills.md) | `skills` `resources` `design` `agents` | See which agent skills are widely used before writing your own |
| 2026-10-18 | [10 resources for AI-assisted 3D and animated web design](entries/2026-10-18-web-3d-design-resource-list.md) | `web-design` `threejs` `motion` `resources` | Reference set for 3D/motion web pages |
| 2026-10-18 | [Checklist for fast App Store approval](entries/2026-10-18-apple-fast-approval-checklist.md) | `app-store` `ios` `launch` `subscriptions` | Concrete App Review checklist |
| 2026-10-18 | [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md) | `audio` `sfx` `motion-graphics` `game-dev` `mcp` `compression` `open-source` | Procedural, frame-synced SFX for trailers and game UI |
| 2026-10-17 | [10 open-source repos for an AI content pipeline](entries/2026-10-17-open-source-content-factory-repos.md) | `content` `video` `audio` `open-source` | Open-source stack for devlogs and trailers |
| 2026-10-17 | [Concept art to playable 3D world via blockout + painted projection](entries/2026-10-17-concept-art-to-playable-3d.md) | `3d` `asset-pipeline` `shaders` `concept-art` `claude` | Turn concept art into a walkable 3D scene |
| 2026-10-17 | [Claude Code replaces an ad-heavy Android TV launcher](entries/2026-10-17-claude-code-android-tv-launcher.md) | `claude-code` `android` `devices` `agents` | Agent-driven device setup, reversible |
| 2026-10-17 | [Apple updates App Review Guidelines amid developer account terminations](entries/2026-10-17-app-review-guidelines-update.md) | `app-store` `ios` `compliance` | New App Review rules on hidden features and assets |
| 2026-10-17 | [Design inspiration sites, including DESIGN.md files for agents](entries/2026-10-17-ai-design-inspiration-sites.md) | `design` `resources` `agents-md` `ui` | DESIGN.md files to steer agent-built UI |
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
- [Checklist for fast App Store approval](entries/2026-10-18-apple-fast-approval-checklist.md)
- [Apple updates App Review Guidelines amid developer account terminations](entries/2026-10-17-app-review-guidelines-update.md)
- [App Store Review Guideline 2.5.19 and remote config / A/B testing](entries/2026-10-16-app-store-guideline-2-5-19.md)
- [Apple Search Ads playbook for indie apps](entries/2026-10-13-apple-search-ads-playbook.md)
- [Avoiding Apple rejections for 'spam/slop' apps](entries/2026-10-09-apple-app-review-slop-rejections.md)
- [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md)
### `app-store`
- [Checklist for fast App Store approval](entries/2026-10-18-apple-fast-approval-checklist.md)
- [Apple updates App Review Guidelines amid developer account terminations](entries/2026-10-17-app-review-guidelines-update.md)
- [App Store Review Guideline 2.5.19 and remote config / A/B testing](entries/2026-10-16-app-store-guideline-2-5-19.md)
- [Apple Search Ads playbook for indie apps](entries/2026-10-13-apple-search-ads-playbook.md)
- [Avoiding Apple rejections for 'spam/slop' apps](entries/2026-10-09-apple-app-review-slop-rejections.md)
### `blender`
- [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md)
- [The Little Prince as a 3D story game in 16 days with Opus, Tripo and Blender](entries/2026-10-13-little-prince-3d-story-game.md)
- [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
- [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md)
### `launch`
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
- [earshot v0.3: 201 code-made sound effects, timed to the exact frame](entries/2026-10-18-earshot-code-made-sound-effects.md)
- [Gemini 4 Argon builds a Subway Surfers-style flying runner](entries/2026-10-16-gemini-flying-roadster-runner.md)
- [The Little Prince as a 3D story game in 16 days with Opus, Tripo and Blender](entries/2026-10-13-little-prince-3d-story-game.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
- [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md)
### `local-models`
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
- [10 resources for AI-assisted 3D and animated web design](entries/2026-10-18-web-3d-design-resource-list.md)
- [A 25-minute animated episode written entirely as code by Opus](entries/2026-10-16-claude-coded-anime-episode.md)
- [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
### `ui`
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
- [How to be more ambitious with models: altitude, depth and range (plus a /be-ambitious skill)](entries/2026-10-13-be-ambitious-with-models.md)
- [How to trust agents' work: the inverse pyramid](entries/2026-10-16-trust-agents-inverse-pyramid.md)
- [Solo developer's 50-agent stack: $545k MRR, 1,089 PRs in a week](entries/2026-10-13-solo-dev-50-agent-stack.md)
- [Codex memory: swap the default memory models in config](entries/2026-10-13-codex-memory-model-upgrade.md)
### `asset-pipeline`
- [CLI-Anything: wrap desktop apps like Blender and GIMP as CLIs agents can drive](entries/2026-10-15-cli-anything-desktop-apps-for-agents.md)
- [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md)
- [Concept art to playable 3D world via blockout + painted projection](entries/2026-10-17-concept-art-to-playable-3d.md)
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
### `checklist`
- [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md)
- [Have subagents audit 20 web performance issues](entries/2026-10-13-perf-audit-subagents.md)
- [20 speed fixes for vibe-coded apps](entries/2026-10-12-speedmaxxing-vibe-coded-apps.md)
- [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md)
### `codex`
- [Codex memory: swap the default memory models in config](entries/2026-10-13-codex-memory-model-upgrade.md)
- [Codex usage resets can only be used near the limit](entries/2026-10-04-codex-reset-caveat.md)
- [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md)
### `cost`
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
- [Skill Issue: agent skills ranked by what people actually use](entries/2026-10-19-skill-issue-ranked-agent-skills.md)
- [10 resources for AI-assisted 3D and animated web design](entries/2026-10-18-web-3d-design-resource-list.md)
- [Design inspiration sites, including DESIGN.md files for agents](entries/2026-10-17-ai-design-inspiration-sites.md)
- [Designeer: curated hub of design galleries, components, AI tools and MCP servers](entries/2026-10-03-designeer-design-resource-hub.md)
### `seo`
- [How Railway grew via AI recommendations (AI SEO)](entries/2026-10-14-railway-ai-seo-playbook.md)
- [Submit sitemaps to Bing Webmaster Tools and IndexNow](entries/2026-10-11-bing-indexnow-sitemap.md)
- [SEO: agent-assisted backlink outreach](entries/2026-10-07-agent-backlink-outreach.md)
### `agent-tooling`
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
- [Gemini 4 Argon builds a Subway Surfers-style flying runner](entries/2026-10-16-gemini-flying-roadster-runner.md)
- [Google Play lets you install private vibe-coded apps](entries/2026-10-13-google-play-private-vibe-coded-apps.md)
### `research`
- [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md)
- [X research skill + media download for video editing workflows](entries/2026-10-13-x-research-skill-video-workflows.md)
- [Claude Code hands off X research to GrokBot via a webhook skill](entries/2026-10-11-claude-code-grokbot-handoff.md)
### `security`
- [open-browser-use: agents drive your real, logged-in Chrome over MCP](entries/2026-10-13-open-browser-use-logged-in-chrome.md)
- [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md)
- [Have subagents red-team a site before shipping](entries/2026-10-16-security-red-team-subagents.md)
- [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md)
### `subagents`
- [Have subagents red-team a site before shipping](entries/2026-10-16-security-red-team-subagents.md)
- [Have subagents audit 20 web performance issues](entries/2026-10-13-perf-audit-subagents.md)
### `tts`
- [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md)
- [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md)
### `unity`
- [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md)
- [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md)
### `video-editing`
- [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md)
- [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md)
### `ab-testing`
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
- [Codex memory: swap the default memory models in config](entries/2026-10-13-codex-memory-model-upgrade.md)
### `model-porting`
- [ruNNtime: porting new models to the browser with Claude](entries/2026-10-07-ruNNtime-browser-models.md)
### `models`
- [SKY-001: a world model that plans CAD and BIM builds part by part](entries/2026-10-19-sky-001-engineering-world-model.md)
- [Hugging Bay: searchable model hub with checksums, torrents and MCP](entries/2026-10-05-hugging-bay-model-hub.md)
### `monetization`
- [How Block Blast! designs losses around ads](entries/2026-10-15-block-blast-ad-design-breakdown.md)
### `motion`
- [10 resources for AI-assisted 3D and animated web design](entries/2026-10-18-web-3d-design-resource-list.md)
### `openai`
- [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md)
### `ops`
- [The ~150-item checklist a vibe-coded app needs before paying customers](entries/2026-10-15-vibe-coded-app-production-checklist.md)
- [Codex usage resets can only be used near the limit](entries/2026-10-04-codex-reset-caveat.md)
### `orchestration`
- [Solo developer's 50-agent stack: $545k MRR, 1,089 PRs in a week](entries/2026-10-13-solo-dev-50-agent-stack.md)
### `pdf`
- [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md)
### `plugin`
- [Claude Code built-in plugin: You Should Know](entries/2026-10-02-claude-code-you-should-know-plugin.md)
### `privacy`
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
- [An indie developer's ranking of mobile app marketing channels](entries/2026-10-13-mobile-app-marketing-channels.md)
### `vector`
- [ChatGPT plugin that vectorizes logos in chat](entries/2026-10-01-chatgpt-logo-vectorize-plugin.md)
### `vibe-coding`
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
