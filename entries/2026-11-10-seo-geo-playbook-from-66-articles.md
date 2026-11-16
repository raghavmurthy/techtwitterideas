# An SEO and AI-search (GEO) playbook distilled from 66 articles, 48 skills and 14 repos

**X post:** https://x.com/TheoAGI/status/2120163220312699025  
**Author:** Theo (@TheoAGI) · posted 2026-11-10 (UTC) · 1,035 likes, 53 replies  
**Source:** the X article attached to the post, "The only SEO/GEO article you need, send it to your AI"

## What it is
Theo, a video editor and filmmaker building the AI video editor SpaceCut per his X bio, had a model read 66 SEO and GEO (generative engine optimisation) articles, a library of 48 free SEO skills for agents, and 13 more GitHub repos, then sort the advice and run basic checks on his own pre-launch site. The article is the result.

His four headline findings: about 90 percent of the advice is the same dozen ideas, mostly classic SEO; almost none of the big numbers come with data; the commonly quoted thresholds are rules of thumb; and GitHub stars don't tell you whether advice is current (one popular repo gets ChatGPT's search crawler wrong).

The playbook, in order:
1. **Foundation:** headline and main text must be in the raw HTML; check the live robots.txt (a CDN can inject rules); know that training crawlers (GPTBot, ClaudeBot, Google-Extended) differ from the ones that power live AI answers (OAI-SearchBot, Claude-SearchBot, PerplexityBot, Bingbot); add a sitemap of indexable pages, canonical tags and basic structured data, but no review stars without real reviews. His own site failed several of these.
2. **Bing:** set up Bing Webmaster Tools and IndexNow, since Copilot runs on Bing and ChatGPT has leaned on it; its AI Performance report is free citation data.
3. **Decision pages:** build "X vs Y", alternatives, "best X for" and pricing pages; answer in the first 40 to 80 words; 5 to 8 options per list; prices from vendor pages with a "checked on" date; one real drawback per option, including your own; don't rank yourself first; add something the top 10 results lack.
4. **What's new in GEO:** assistants run many hidden searches per question; most citations go to third-party pages; answers change week to week; AI engines get facts about you wrong, so publish a dated fact sheet and fix errors at their source.
5. **Free measurement:** 15 to 30 real buyer questions, run at least twice per engine logged out, logging who is named and which URLs are cited; report counts, not percentages, at low volume; add "How did you hear about us?" at signup.
6. **Links:** consistent listings on 20 to 30 directories, unlinked mentions, short evidence-based pitches to "best of" lists, disclosed participation on Reddit and Quora; avoid link exchanges, fake accounts, mass AI posts and templated city pages.
7. **If an agent does your SEO:** numbers must come from tools, never from the model; three permission tiers (read and draft freely, approval to publish or retitle, never alone to delete pages or touch robots.txt or canonicals), with the "never" enforced in a hook rather than a prompt; snapshot key pages before each deploy to catch noindex, canonical, 404 and robots.txt regressions; grade drafts before shipping.
8. **New domains:** one to four new pages a week, and wait two to three months before judging a change.

He also reviews the two vendors behind most of the articles he read and sorts the 14 repos into "worth installing", "worth it once you have data" and "take one idea, leave the rest", warning that site scores out of 100 were never validated against real rankings. The article ends with a step-by-step audit brief for an agent, which starts audit-only, asks for approval and a diff before each change, and forbids invented numbers.

## Thread highlights
> **@TheoAGI:** I don't think this one is built for local SEO, by the way! But what I did is compiling a lot of the resources I could find on X, a bit on GitHub, feeding Fable 5.2, and then using this as an SEO roadmap for myself as a beginner!

> **@Corpus_hq:** "Read the findings. Ignore the number." That line should be on every audit. I'd add one check: if your offer and price only appear after JavaScript runs, the crawler can get a 200 and still have a blank page.

> **@milhouscc:** The HTTP 200 check is useful for reachability. A request with a crawler user-agent still doesn't prove the real crawler fetched the page, indexed it, or cited it. Those need separate evidence.

> **@Jon_Cunningham:** You can't begin to scratch the surface of an "only one you need playbook" with 60 or even 1000 articles.

> **@louisfoweraker:** the one step your Claude couldn't do, reading what ChatGPT, Gemini, Perplexity and Google actually answer in your category.

## Implications
- **Research by distillation:** the method is as useful as the result. Feeding a model a pile of saved articles and asking it to find the overlap, the unsupported numbers and the outdated claims is a quick way to get a beginner roadmap in any field, as long as claims are checked against primary docs.
- **Game and app landing pages:** client-rendered landing pages built with game engines or heavy JS often fail the raw-HTML check. A static HTML shell with the pitch, platforms and price is the cheap fix.
- **Decision pages fit games too:** "X vs Y", "games like X" and "best X for" queries are how players choose. One honest comparison page with a real drawback is more likely to be cited than a generic feature list.
- **Agent guardrails generalise:** read, draft, approve and never tiers, with the "never" enforced in a hook, are a good template for any agent allowed near production config.
- **Experiment:** run section 1 against your own site: fetch the live robots.txt, check the raw HTML of the homepage for the headline, and request the page with the OAI-SearchBot user-agent. Then write 15 real player or buyer questions and run each twice in ChatGPT, Claude, Perplexity and Gemini, logging who gets named and which URLs are cited, as a baseline to repeat in a month.

## Tags
`seo` `ai-search` `launch` `web` `agent-workflow` `skills` `marketing` `checklist`
