# A passwords.txt honeypot that cuts the network when anything reads it

**X post:** https://x.com/semenov_roman_/status/2121866549778608342  
**Author:** Roman Semenov (@semenov_roman_) · posted 2026-11-15 (UTC) · 15,833 likes, 89 replies  
**Source:** the post and the author's replies (no code shared)

## What it is
Roman Semenov, of Tornado Cash per his X bio, shared a simple trick: put a decoy `passwords.txt` file in your home directory, run a script that watches for anything reading it, and when that happens, notify you and shut down networking.

In his replies he explains the reasoning and the details:
- **Why cut the network instead of using a canary key:** a canary token tells you something was stolen after the fact. Killing the network is meant to stop a malicious script from sending all your other real secrets back to its server before it finishes.
- **What triggers it:** reading the file's contents, not listing the directory.
- **Coding agents:** he says an agent shouldn't be reading your keys and passwords into its context anyway, since that context is sent to the model provider (unless the model runs locally), and he calls it alarming how many people are comfortable with that.
- **False positives:** start in notify-only mode, handle a few accidental trips, and after that nothing unexpected should be sniffing around your home directory. If it does trip, keep the network off until you've inspected what happened.

## Thread highlights
> **@semenov_roman_:** The point of this vs canary keys is it prevents the attacker script from sending all your other real keys it stole back to its servers.

> **@semenov_roman_:** Your agent is not supposed to read your keys and passwords into its context (that it sends to the cloud), unless you use a local LLM model for that.

> **@semenov_roman_:** Set it to only notify at first, handle a few accidental trip ups, after that nothing unexpected should be sniffing around your home dir.

> **@nopara73:** i considered that but i dont want my computer to constantly get in my way because of false positives, so i opted for just a notification.

> **@bhiduboi:** nice trick. put a canary token inside the file too, so you learn which machine leaked it, not just that someone read it.

> **@d1gitize:** It could be doing some work and read from it very accidentally.

## Implications
- **Agents are a new kind of reader of your home directory:** coding agents and their tool calls scan files for context. A decoy file is a cheap way to find out whether an agent, a plugin or a dependency is reading things it has no reason to read.
- **Supply-chain defence for dev machines:** game and app projects pull in many packages, editor plugins and asset-store scripts. A post-install script that hunts for secrets is exactly what a content-read tripwire catches.
- **Keep real secrets out of agent reach:** separate tokens per project, keep keys in a password manager or OS keychain rather than plain files, and scope what directories an agent may read.
- **Start gentle:** as the replies point out, false positives are the main cost; notify-only first, then add the network kill once the noise is gone.
- **Experiment:** on a development machine, create a decoy file with obviously fake contents, set up a file-access monitor that only notifies on content reads, and leave it for one week of normal work with your coding agent and build tools. Log every process that opens it; only then decide whether to add an automatic network cut-off.

## Tags
`security` `agents` `coding-agents` `privacy` `devops` `prompt-injection`
