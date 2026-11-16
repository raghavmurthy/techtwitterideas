# Six more legal checks before launching a vibe-coded app

**X post:** https://x.com/suraj_sharma14/status/2121785257200701671  
**Author:** Suraj Sharma (@suraj_sharma14) · posted 2026-11-15 (UTC) · 82 likes, 16 replies  
**Source:** the post itself

## What it is
Suraj Sharma, whose X bio says he helps builders get into AI, startups and global opportunities, argues that you can ship an app in a weekend and break six laws in the same weekend without knowing it. His list, framed mostly around US law plus the EU AI Act:

1. **Launch texts:** sending launch SMS without prior express written consent breaks the US TCPA, which he puts at $500 to $1,500 per text.
2. **Unlabelled buttons:** missing accessible labels on buttons and forms can trigger ADA demands; under California's Unruh Act he says statutory damages start at $4,000 per violation for covered businesses.
3. **AI-written testimonials:** fake or AI-generated reviews on a landing page break the FTC's Consumer Reviews Rule, which he puts at up to $53,088 per violation.
4. **Face or voice uploads:** capturing a face scan or voiceprint from an Illinois user without a written release and retention policy can trigger BIPA claims of $1,000 to $5,000 per person.
5. **Undisclosed AI chat:** he says EU AI Act Article 50 requires telling EU users at the first message that they are talking to AI, from August 2, 2026, with fines up to €15M or 3 percent of global turnover.
6. **Missing privacy policy:** collecting emails or analytics from California visitors without a posted privacy policy can lead to $2,500 per violation if not fixed after notice.

He closes that none of these cost much to fix but all of them cost a lot to ignore. He includes a short pre-launch brief for a coding agent that asks it to check for these six issues, fix what it can, and list what the founder must handle personally. He notes it is not legal advice. The figures are his and were not checked here.

## Thread highlights
> **@RRomcym:** Asking it to list what you have to do yourself, not just fix in code, is a smart split, since consent flows and privacy policies still need a human to sign off.

> **@SamuelSu540455:** One more for anyone shipping a support bot: disclose it's a bot (California's BOT Act, EU AI Act transparency rules), and log every answer it gives. Air Canada was held to a refund policy its bot made up.

> **@OpportifyAI:** 7) SMS pumping: OTP signup with no per-IP cap lets bots text high-cost numbers on your bill

> **@techhdive:** make sure you don't store or log sensitive card details at your end. use the payment gateway's components to handle card information

> **@k_d_patel007:** play store at least makes you fill a privacy policy and data safety form before launch. a weekend web app gets no checkpoint like that.

## Implications
- **Games are not exempt:** AI companions or NPC chat that players can talk to, voice-capture features, face-scan avatars, and review widgets on a store page all fall into these categories.
- **Accessibility is also a legal surface:** labelling buttons and inputs on web landing pages and in-game UI built with web tech is cheap, and it overlaps with what agent-built UIs usually miss.
- **Split code fixes from human obligations:** the useful part of his agent brief is asking for two lists, things the agent can fix in code and things only a human can do (consent wording, privacy policy, releases).
- **Jurisdiction matters:** the list is US and EU oriented; builders elsewhere should check local rules, and none of this replaces a lawyer.
- **Experiment:** before your next launch, ask your coding agent for an audit-only pass against these six categories plus SMS-pumping limits and bot disclosure, with two output lists (fixable in code, needs a human). Fix the code list, then take the human list to whoever handles your legal pages.

## Tags
`legal` `compliance` `launch` `privacy` `vibe-coding` `checklist` `accessibility` `agent-workflow`
