# A self-maintaining second-brain wiki run by three bots: reader, librarian, checker

**X post:** https://x.com/Argona0x/status/2111837226006921640  
**Author:** Argona (@Argona0x) · posted 2026-10-18 (UTC) · 4,872 likes, 218 replies  

## What it is
A setup the author frames as Andrej Karpathy's LLM-wiki ("second brain") pattern, run on Grok Bot with three bots in one group chat, each with its own memory. The reader takes in every link, PDF and voice note and never edits the raw sources. The librarian rewrites every wiki page a new source touches (usually 10 to 15). The checker runs nightly to find contradictions, stale claims and orphan pages. Answers to questions are filed back as pages, so the wiki grows from use as well as reading. When a new source contradicts an old page, the checker flags it to the human instead of silently overwriting it, and a page with no fresh source for 30 days is marked unconfirmed. Every page must show the claim, the source it came from and the date it was last confirmed. The author's advice is to start with one topic you actually work on, not your whole life.

## Thread highlights
> **@7xuanlux:** I run this pattern in production, not as a prompt setup. The same compiled wiki gets read by Claude Code, Codex and ChatGPT in my case. The rule that made it hold up: a human correction is a source too, and it outranks the compiled page. Otherwise the compiler quietly writes over the fix next run.

> **@relativeread:** why do you want to explain your whole life to AI?

## Implications
- **Agent workflows:** separating "collect", "write" and "doubt" into different agents avoids the single agent that grades its own summaries. The same split suits a project knowledge base or design wiki.
- **Knowledge bases:** claim, source and last-confirmed date per page is a simple schema that makes stale information visible; the reply about human corrections outranking compiled pages is a rule worth adopting.
- **Game dev:** a design-doc wiki (mechanics, tuning values, asset specs) maintained this way could stay in sync with playtest notes.
- **Experiment:** start a raw/ and wiki/ folder for one topic (say, mobile-game monetisation), feed it ten sources, and run a weekly contradiction check before trusting it.

## Tags
`knowledge-base` `memory` `agents` `agent-workflow` `wiki`
