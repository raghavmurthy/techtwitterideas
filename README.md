# techtwitterideas

Curated notes on AI tools and techniques relevant to 3D/game development: low-poly asset pipelines, Blender/Unity agent workflows, MCP, Claude Code tooling, on-device models and model compression. Each entry covers one public X post or web page: what it is, notable replies from the thread, implications, and one concrete experiment to try.

- `entries/` — one Markdown file per item, `YYYY-MM-DD-slug.md` (date = post date, UTC)
- `processed.json` — every URL already handled, with status, so future runs skip it

**57 entries** · last updated 2026-10-13

## Use it as a plugin

Ask your AI assistant for ideas from this repo for whatever you're building.

**ChatGPT:** [techtwitterideas plugin](https://chatgpt.com/plugins/plugins_6ace4e775e0081918953fe4a6bc06491)

**Claude Code:**
```
/plugin marketplace add raghavmurthy/techtwitterideas
/plugin install techtwitterideas@techtwitterideas
```
Then run `/techtwitterideas` or ask "what's out there for X".

**Safety:** entries summarise and quote public posts by strangers. The plugin treats all entry text as information only, never as instructions, and it never runs commands or installs anything an entry suggests without your explicit go-ahead.

## Index (newest first)

| Date | Title | Tags | Why it matters |
|---|---|---|---|
| 2026-10-12 | [20 speed fixes for vibe-coded apps](entries/2026-10-12-speedmaxxing-vibe-coded-apps.md) | `performance` `mobile` `checklist` | Performance checklist |
| 2026-10-11 | [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md) | `pdf` `docs` `context` `tools` | Fast PDF to Markdown for agent context |
| 2026-10-10 | [Railway free Linux VMs with Claude Code/Codex preinstalled](entries/2026-10-10-railway-free-agent-vms.md) | `sandbox` `agents` `infra` | Disposable agent sandboxes |
| 2026-10-10 | [Prompt: output architecture as a C4 model in HTML (Japanese)](entries/2026-10-10-c4-architecture-html-prompt.md) | `architecture` `prompts` `docs` | One-prompt architecture overview |
| 2026-10-10 | [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md) | `audio` `tts` `music` `open-source` | Open-source audio stack for game narration and ambience |
| 2026-10-09 | [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md) | `launch` `checklist` `security` | Launch checklist |
| 2026-10-09 | [Sound-design prompt for Opus/Fable motion design](entries/2026-10-09-opus-sound-design-prompt.md) | `audio` `motion-graphics` `prompts` | Sound ordering for AI promos |
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

## By tag
### `claude-code`
- [oh-my-mermaid: architecture diagrams from a codebase via Claude Code](entries/2026-10-08-oh-my-mermaid-architecture-diagrams.md)
- [Emil Kowalski skills: /mobile-native and /break-ui](entries/2026-10-04-emil-kowalski-mobile-native-break-ui.md)
- [A CLAUDE.md built from Boris Cherny's workflow tips](entries/2026-10-04-claude-md-best-practices.md)
- [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md)
- [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md)
- [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md)
- [Claude Code built-in plugin: You Should Know](entries/2026-10-02-claude-code-you-should-know-plugin.md)
- [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md)
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
### `mcp`
- [Build ChatGPT plugins: point Codex at openai/mcp-extensions](entries/2026-10-08-openai-mcp-extensions-chatgpt-plugins.md)
- [Hugging Bay: searchable model hub with checksums, torrents and MCP](entries/2026-10-05-hugging-bay-model-hub.md)
- [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md)
- [Designeer: curated hub of design galleries, components, AI tools and MCP servers](entries/2026-10-03-designeer-design-resource-hub.md)
- [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md)
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
- [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md)
- [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md)
### `claude`
- [Launch video from HTML + GSAP rendered by HyperFrames](entries/2026-10-08-hyperframes-launch-video.md)
- [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md)
- [Claude Startups program expands](entries/2026-10-06-claude-startups-program.md)
- [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
- [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md)
- [Claude app: design/deck/doc work uses 50% less usage for two weeks](entries/2026-10-01-claude-design-usage-promo.md)
### `workflow`
- [Primitives → skills → feature loop against AI slop](entries/2026-10-08-primitives-skills-loop.md)
- [A CLAUDE.md built from Boris Cherny's workflow tips](entries/2026-10-04-claude-md-best-practices.md)
- [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md)
- [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md)
- [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md)
- [Claude Code built-in plugin: You Should Know](entries/2026-10-02-claude-code-you-should-know-plugin.md)
### `marketing`
- [Launch video from HTML + GSAP rendered by HyperFrames](entries/2026-10-08-hyperframes-launch-video.md)
- [20 repos for agent-made motion design (claude-motion, HyperFrames, Remotion, GSAP)](entries/2026-10-08-20-motion-design-repos.md)
- [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md)
- [SEO: agent-assisted backlink outreach](entries/2026-10-07-agent-backlink-outreach.md)
- [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md)
### `on-device`
- [Tencent Hy-MT2: 440 MB offline translator, 33 languages (Turkish post)](entries/2026-10-08-tencent-hy-mt2-offline-translator.md)
- [NeuDecide: 43 MB speech-to-tool-call model on one CPU thread](entries/2026-10-08-neudecide-audio-tool-calls.md)
- [ruNNtime: porting new models to the browser with Claude](entries/2026-10-07-ruNNtime-browser-models.md)
- [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md)
- [Decision models on-device in llama.cpp (Kev-4B GGUF)](entries/2026-10-02-kev-4b-llamacpp.md)
### `skills`
- [anti-slop: filters generic AI-generated UI, text and code](entries/2026-10-09-anti-slop-filter.md)
- [Primitives → skills → feature loop against AI slop](entries/2026-10-08-primitives-skills-loop.md)
- [20 repos for agent-made motion design (claude-motion, HyperFrames, Remotion, GSAP)](entries/2026-10-08-20-motion-design-repos.md)
- [Emil Kowalski skills: /mobile-native and /break-ui](entries/2026-10-04-emil-kowalski-mobile-native-break-ui.md)
- [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md)
### `agents`
- [Railway free Linux VMs with Claude Code/Codex preinstalled](entries/2026-10-10-railway-free-agent-vms.md)
- [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md)
- [SEO: agent-assisted backlink outreach](entries/2026-10-07-agent-backlink-outreach.md)
- [Graphical: design visual languages and style components for coding agents](entries/2026-10-05-graphical-visual-language-tool.md)
### `blender`
- [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
- [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md)
### `compression`
- [Qwen3.5 9B distilled from Kimi k3 (GGUF)](entries/2026-10-08-qwen3-5-9b-kimi-distill.md)
- [NeuDecide: 43 MB speech-to-tool-call model on one CPU thread](entries/2026-10-08-neudecide-audio-tool-calls.md)
- [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md)
- [Decision models on-device in llama.cpp (Kev-4B GGUF)](entries/2026-10-02-kev-4b-llamacpp.md)
### `local-models`
- [Qwen3.5 9B distilled from Kimi k3 (GGUF)](entries/2026-10-08-qwen3-5-9b-kimi-distill.md)
- [Decision models on-device in llama.cpp (Kev-4B GGUF)](entries/2026-10-02-kev-4b-llamacpp.md)
- [FreeVideo: local video generation on 8GB VRAM](entries/2026-10-02-freevideo-local-video-gen.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
### `mobile`
- [20 speed fixes for vibe-coded apps](entries/2026-10-12-speedmaxxing-vibe-coded-apps.md)
- [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md)
- [Emil Kowalski skills: /mobile-native and /break-ui](entries/2026-10-04-emil-kowalski-mobile-native-break-ui.md)
- [Template 'matrix' shipping: reskinning app templates at scale (Chinese post)](entries/2026-10-01-template-matrix-shipping.md)
### `motion-graphics`
- [Sound-design prompt for Opus/Fable motion design](entries/2026-10-09-opus-sound-design-prompt.md)
- [Launch video from HTML + GSAP rendered by HyperFrames](entries/2026-10-08-hyperframes-launch-video.md)
- [20 repos for agent-made motion design (claude-motion, HyperFrames, Remotion, GSAP)](entries/2026-10-08-20-motion-design-repos.md)
- [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md)
### `3d-agents`
- [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md)
- [Mixar: a team of AI agents that model, texture and light a 3D scene](entries/2026-10-01-mixar-multi-agent-3d.md)
- [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md)
### `audio`
- [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md)
- [Sound-design prompt for Opus/Fable motion design](entries/2026-10-09-opus-sound-design-prompt.md)
- [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md)
### `context`
- [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md)
- [Leviathan: agents search huge databases in ~436 tokens](entries/2026-10-05-leviathan-agent-indexer.md)
- [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md)
### `design`
- [Ask: a dataset of 1-10k beautiful landing pages](entries/2026-10-05-landing-page-dataset-ask.md)
- [Designeer: curated hub of design galleries, components, AI tools and MCP servers](entries/2026-10-03-designeer-design-resource-hub.md)
- [Claude app: design/deck/doc work uses 50% less usage for two weeks](entries/2026-10-01-claude-design-usage-promo.md)
### `docs`
- [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md)
- [Prompt: output architecture as a C4 model in HTML (Japanese)](entries/2026-10-10-c4-architecture-html-prompt.md)
- [oh-my-mermaid: architecture diagrams from a codebase via Claude Code](entries/2026-10-08-oh-my-mermaid-architecture-diagrams.md)
### `prompts`
- [Prompt: output architecture as a C4 model in HTML (Japanese)](entries/2026-10-10-c4-architecture-html-prompt.md)
- [Sound-design prompt for Opus/Fable motion design](entries/2026-10-09-opus-sound-design-prompt.md)
- [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md)
### `agent-tooling`
- [Leviathan: agents search huge databases in ~436 tokens](entries/2026-10-05-leviathan-agent-indexer.md)
- [Termium: Chromium inside the terminal (OSS, MIT)](entries/2026-09-30-termium-chromium-in-terminal.md)
### `agents-md`
- [Primitives → skills → feature loop against AI slop](entries/2026-10-08-primitives-skills-loop.md)
- [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md)
### `asset-pipeline`
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
### `browser`
- [ruNNtime: porting new models to the browser with Claude](entries/2026-10-07-ruNNtime-browser-models.md)
- [Termium: Chromium inside the terminal (OSS, MIT)](entries/2026-09-30-termium-chromium-in-terminal.md)
### `chatgpt-plugin`
- [Build ChatGPT plugins: point Codex at openai/mcp-extensions](entries/2026-10-08-openai-mcp-extensions-chatgpt-plugins.md)
- [ChatGPT plugin that vectorizes logos in chat](entries/2026-10-01-chatgpt-logo-vectorize-plugin.md)
### `checklist`
- [20 speed fixes for vibe-coded apps](entries/2026-10-12-speedmaxxing-vibe-coded-apps.md)
- [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md)
### `claude-md`
- [A CLAUDE.md built from Boris Cherny's workflow tips](entries/2026-10-04-claude-md-best-practices.md)
- [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md)
### `codex`
- [Codex usage resets can only be used near the limit](entries/2026-10-04-codex-reset-caveat.md)
- [AGENTS.md that stops agents over-engineering](entries/2026-10-04-agents-md-simplest-code.md)
### `coding-agents`
- [Evidence: agent-written unit/integration tests don't improve success](entries/2026-10-08-ai-written-tests-dont-help.md)
- [Coding agent harness tier list ('Very important discussion')](entries/2026-10-04-coding-agent-tier-list.md)
### `game-dev`
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
- [universal-modder: skills + fal MCP so Claude Code can mod PC games](entries/2026-10-01-universal-modder-claude-game-modding.md)
### `image-to-3d`
- [GPT-6.1 Sol + Blender MCP: multi-view photos to textured model in <10 min](entries/2026-10-03-gpt-sol-blender-mcp-photos-to-3d.md)
- [Pixel Match: local image-to-3D that keeps source pixels after retopo](entries/2026-09-30-pixel-match-image-to-3d.md)
### `launch`
- [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md)
- [6 legal traps in AI-built apps (COPPA, GDPR fonts, CIPA, CAN-SPAM)](entries/2026-10-06-vibe-coded-app-legal-traps.md)
### `music`
- [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md)
- ['I may have vibe coded the best thing ever' (video only)](entries/2026-10-03-armand-vibe-coded-setup.md)
### `open-source`
- [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md)
- [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md)
### `open-weights`
- [Cloudflare drops 'clef' on Hugging Face (Apache 2.0)](entries/2026-10-01-cloudflare-clef-hf.md)
- [Ideogram 4.5: multi-turn image editing without artifact build-up](entries/2026-09-30-ideogram-4-5-precise-edit.md)
### `subscriptions`
- [6 legal traps in AI-built apps (COPPA, GDPR fonts, CIPA, CAN-SPAM)](entries/2026-10-06-vibe-coded-app-legal-traps.md)
- [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md)
### `testing`
- [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md)
- [Evidence: agent-written unit/integration tests don't improve success](entries/2026-10-08-ai-written-tests-dont-help.md)
### `threejs`
- [475 Claude Opus 5.5 demo videos with prompts in one repo](entries/2026-10-03-475-opus-video-demos-repo.md)
- [Opus 5.5 builds a Three.js night-city game with Blender + image-gen](entries/2026-10-02-opus-threejs-city-game.md)
### `tts`
- [10 open-source repos for voice, music and SFX](entries/2026-10-10-10-open-source-audio-repos.md)
- [Paradee: Kokoro TTS distilled to 8M params (9 MB)](entries/2026-10-07-paradee-8m-tts.md)
### `ui`
- [Graphical: design visual languages and style components for coding agents](entries/2026-10-05-graphical-visual-language-tool.md)
- [Emil Kowalski skills: /mobile-native and /break-ui](entries/2026-10-04-emil-kowalski-mobile-native-break-ui.md)
### `unity`
- [Boris Cherny's 28-min Claude Code talk (CLAUDE.md, memory, parallel sessions)](entries/2026-10-04-boris-cherny-claude-code-talk.md)
- [Matt Pocock: /retro your agent sessions to make the repo easier to navigate](entries/2026-10-02-retro-repo-navigability.md)
### `video`
- [Launch video from HTML + GSAP rendered by HyperFrames](entries/2026-10-08-hyperframes-launch-video.md)
- [20 repos for agent-made motion design (claude-motion, HyperFrames, Remotion, GSAP)](entries/2026-10-08-20-motion-design-repos.md)
### `video-editing`
- [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md)
- [OpenCut: open-source CapCut alternative with an MCP server](entries/2026-10-01-opencut-open-source-capcut.md)
### `3d`
- [image-blaster: photo to explorable 3D world (repost of a May demo)](entries/2026-10-03-image-blaster-photo-to-3d-world.md)
### `animation`
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
### `architecture`
- [Prompt: output architecture as a C4 model in HTML (Japanese)](entries/2026-10-10-c4-architecture-html-prompt.md)
### `benchmark`
- [Blender Bench v1: frontier LLMs on 20 real Blender workflows](entries/2026-09-30-blender-bench-v1.md)
### `branding`
- [ChatGPT plugin that vectorizes logos in chat](entries/2026-10-01-chatgpt-logo-vectorize-plugin.md)
### `coding`
- [Qwen3.5 9B distilled from Kimi k3 (GGUF)](entries/2026-10-08-qwen3-5-9b-kimi-distill.md)
### `comfyui`
- [FreeVideo: local video generation on 8GB VRAM](entries/2026-10-02-freevideo-local-video-gen.md)
### `comparison`
- [Coding agent harness tier list ('Very important discussion')](entries/2026-10-04-coding-agent-tier-list.md)
### `concept-art`
- [Ideogram 4.5: multi-turn image editing without artifact build-up](entries/2026-09-30-ideogram-4-5-precise-edit.md)
### `cost`
- [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md)
### `credits`
- [Claude Startups program expands](entries/2026-10-06-claude-startups-program.md)
### `design-system`
- [Graphical: design visual languages and style components for coding agents](entries/2026-10-05-graphical-visual-language-tool.md)
### `diagrams`
- [oh-my-mermaid: architecture diagrams from a codebase via Claude Code](entries/2026-10-08-oh-my-mermaid-architecture-diagrams.md)
### `distillation`
- [Qwen3.5 9B distilled from Kimi k3 (GGUF)](entries/2026-10-08-qwen3-5-9b-kimi-distill.md)
### `distribution`
- [Build ChatGPT plugins: point Codex at openai/mcp-extensions](entries/2026-10-08-openai-mcp-extensions-chatgpt-plugins.md)
### `environment`
- [image-blaster: photo to explorable 3D world (repost of a May demo)](entries/2026-10-03-image-blaster-photo-to-3d-world.md)
### `evals`
- [Evidence: agent-written unit/integration tests don't improve success](entries/2026-10-08-ai-written-tests-dont-help.md)
### `ffmpeg`
- [Opus 5.5 edits video in chunks for fast re-renders](entries/2026-10-07-opus-chunked-video-editing.md)
### `gaussian-splat`
- [image-blaster: photo to explorable 3D world (repost of a May demo)](entries/2026-10-03-image-blaster-photo-to-3d-world.md)
### `harness`
- [Coding agent harness tier list ('Very important discussion')](entries/2026-10-04-coding-agent-tier-list.md)
### `huggingface`
- [Cloudflare drops 'clef' on Hugging Face (Apache 2.0)](entries/2026-10-01-cloudflare-clef-hf.md)
### `image-editing`
- [Ideogram 4.5: multi-turn image editing without artifact build-up](entries/2026-09-30-ideogram-4-5-precise-edit.md)
### `infra`
- [Railway free Linux VMs with Claude Code/Codex preinstalled](entries/2026-10-10-railway-free-agent-vms.md)
### `ios`
- [baguette: browser-based iOS simulators that agents can drive](entries/2026-10-08-baguette-ios-sim-agents.md)
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
### `model-porting`
- [ruNNtime: porting new models to the browser with Claude](entries/2026-10-07-ruNNtime-browser-models.md)
### `models`
- [Hugging Bay: searchable model hub with checksums, torrents and MCP](entries/2026-10-05-hugging-bay-model-hub.md)
### `multi-agent`
- [Mixar: a team of AI agents that model, texture and light a 3D scene](entries/2026-10-01-mixar-multi-agent-3d.md)
### `openai`
- [What AI coding subscriptions are worth at API prices](entries/2026-10-01-subscription-vs-api-cost.md)
### `ops`
- [Codex usage resets can only be used near the limit](entries/2026-10-04-codex-reset-caveat.md)
### `pdf`
- [OpenDataLoader: CPU-only PDF → Markdown at ~100 pages/s (Chinese post)](entries/2026-10-11-opendataloader-pdf.md)
### `performance`
- [20 speed fixes for vibe-coded apps](entries/2026-10-12-speedmaxxing-vibe-coded-apps.md)
### `plugin`
- [Claude Code built-in plugin: You Should Know](entries/2026-10-02-claude-code-you-should-know-plugin.md)
### `privacy`
- [6 legal traps in AI-built apps (COPPA, GDPR fonts, CIPA, CAN-SPAM)](entries/2026-10-06-vibe-coded-app-legal-traps.md)
### `promo`
- [Claude app: design/deck/doc work uses 50% less usage for two weeks](entries/2026-10-01-claude-design-usage-promo.md)
### `quality`
- [anti-slop: filters generic AI-generated UI, text and code](entries/2026-10-09-anti-slop-filter.md)
### `resources`
- [Designeer: curated hub of design galleries, components, AI tools and MCP servers](entries/2026-10-03-designeer-design-resource-hub.md)
### `retrieval`
- [Leviathan: agents search huge databases in ~436 tokens](entries/2026-10-05-leviathan-agent-indexer.md)
### `sandbox`
- [Railway free Linux VMs with Claude Code/Codex preinstalled](entries/2026-10-10-railway-free-agent-vms.md)
### `scene-generation`
- [Mixar: a team of AI agents that model, texture and light a 3D scene](entries/2026-10-01-mixar-multi-agent-3d.md)
### `security`
- [20-item pre-launch prompt for vibe-coded apps](entries/2026-10-09-pre-launch-20-checks.md)
### `seo`
- [SEO: agent-assisted backlink outreach](entries/2026-10-07-agent-backlink-outreach.md)
### `sprites`
- [Scenario Iso Cycles: Claude Code + Scenario MCP makes 8-direction sprite sheets](entries/2026-10-01-scenario-iso-cycles-mcp-sprites.md)
### `startup-programs`
- [Claude Startups program expands](entries/2026-10-06-claude-startups-program.md)
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
### `vector`
- [ChatGPT plugin that vectorizes logos in chat](entries/2026-10-01-chatgpt-logo-vectorize-plugin.md)
### `vibe-coding`
- ['I may have vibe coded the best thing ever' (video only)](entries/2026-10-03-armand-vibe-coded-setup.md)
### `video-gen`
- [FreeVideo: local video generation on 8GB VRAM](entries/2026-10-02-freevideo-local-video-gen.md)
### `voice`
- [NeuDecide: 43 MB speech-to-tool-call model on one CPU thread](entries/2026-10-08-neudecide-audio-tool-calls.md)
### `workstation`
- ['I may have vibe coded the best thing ever' (video only)](entries/2026-10-03-armand-vibe-coded-setup.md)
### `world-gen`
- [image-blaster: photo to explorable 3D world (repost of a May demo)](entries/2026-10-03-image-blaster-photo-to-3d-world.md)
### `writing`
- [anti-slop: filters generic AI-generated UI, text and code](entries/2026-10-09-anti-slop-filter.md)
