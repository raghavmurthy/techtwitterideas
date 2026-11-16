# Scarlet: an open-source AI video editor driven by Claude Code or Codex

**X post:** https://x.com/MatthewBerman/status/2121297629711909166  
**Author:** Matthew Berman (@MatthewBerman) · posted 2026-11-13 (UTC) · 626 likes, 45 replies  
**Source:** https://github.com/Forward-Future/scarlet (MIT)

## What it is
Matthew Berman had posted a day earlier that he had built an AI video editing app and was looking for testers (over 3,000 replies). He then open-sourced it under the Forward-Future GitHub organisation, saying it is buggy but really does speed up his editing.

According to the README, Scarlet is a desktop editor for macOS and Windows, with an Ubuntu preview. You tell Claude Code or Codex what to change, by voice or text, then play the edit on the timeline; the original footage is never modified. It is aimed at dialogue-heavy material such as interviews, video podcasts and talking-head takes: shortening long pauses, removing repeated phrases, keeping the clearest take, or protecting a pause before a punchline.

Notable design choices from the README:
- It renders only the affected section, so you can hear a change in context, and you can toggle between the removed footage and the join.
- Edits you ask for go on the working timeline, while edits the agent suggests wait for approval. For a first cut, you can jump to the cuts the agent flagged for a second listen.
- Transcription runs locally (CrisperWhisper by default, or Whisper large-v3-turbo until its weights are installed). Your AI provider receives the editing request, not a local render.
- Export goes to MP4, or to a folder with an FCPXML and OTIO timeline for finishing in DaVinci Resolve, Final Cut Pro or Premiere Pro.
- Packaged releases send anonymous usage reports by default; there is a settings toggle to turn this off.

## Thread highlights
> **@MatthewBerman:** It's buggy but it really does speed up my editing process.

> **@codeswithroh:** have built my own skill with which i edit my videos on claude code with hyperframes will definitely see how scarlet can do things differently

> **@bidhuri59430:** AI need skill or small MCP for video editing. Rest is highly inefficient waste of tokens .

> **@MatthewBerman:** not yet, coming in 1-2 weeks likely

## Implications
- **Suggestions versus commands is the key UX split:** separating "edits I asked for" from "edits the agent proposes" keeps the human in charge of taste. The same split works for any agent that edits creative assets, such as scenes, animations or levels.
- **Interchange formats beat lock-in:** exporting OTIO and FCPXML means the agent does the rough cut and a human finishes in a real NLE. For devlogs and trailers, that is a realistic division of labour.
- **Game marketing:** devlogs, playtest commentary and founder videos are exactly the dialogue-heavy footage it targets. Cutting false starts automatically saves the most tedious part of making them.
- **Check telemetry and licences:** usage reporting is on by default in packaged builds, and some bundled skills and the CrisperWhisper weights are separately licensed.
- **Experiment:** take one 20-minute recorded playtest or devlog, run Scarlet's dialogue pass, and time it against a manual rough cut. Note how many flagged cuts you reject, then export to OTIO and confirm the timeline opens cleanly in your editor.

## Tags
`video-editing` `video` `open-source` `claude-code` `codex` `agents` `content` `marketing`
