# Phishing emails that target the AI reading your inbox

**X post:** https://x.com/T3chFalcon/status/2111666077096636435  
**Author:** IT Guy (@T3chFalcon) · posted 2026-10-18 (UTC) · 9,290 likes, 302 replies  

## What it is
The author, a privacy researcher and founder of a phishing-simulation platform per his bio, summarises an attack he attributes to an October report from Barracuda: phishing emails that carry hidden instructions aimed at AI email assistants rather than the human reader. When the assistant summarises the inbox, it reads text the human never sees and may repeat it, for example calling a message urgent and legitimate or adding a fake "vendor payment details changed" action item. He lists four hiding techniques: HTML comments, CSS-invisible text (white on white), Base64-encoded data and zero-width characters. He also says OpenAI acknowledged in December 2025 that this kind of injection may never be fully eliminated in browser-agent designs. The Barracuda report itself wasn't checked here.

## Thread highlights
> **@quser:** treat email content as data, never instructions. keep the AI read-only and make it draft, not send. and put that limit in the app, not in the agent's prompt.

> **@0xj_p:** the real failure happens the moment an agent gets standing access to your primary Gmail. give it a disposable inbox for one task, and an injected prompt finds no other emails, logins, or history to read.

> **@tracewithines:** Where's the actual trace from Barracuda though?

## Implications
- **Agent workflows:** any agent that reads third-party text (email, web pages, X posts, issue comments) needs the same rule this repo uses: content is data, never instructions, and risky actions need human approval outside the model.
- **Tooling:** stripping HTML comments, invisible text and zero-width characters before a model sees content is cheap and catches the techniques listed.
- **Experiment:** write a test email containing each of the four hiding techniques, run it through the email or summarisation agent you use, and record which ones change its output.

## Tags
`security` `prompt-injection` `email` `agents`
