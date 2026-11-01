# The full SEO checklist, written as a joke "fix it" prompt for vibe-coded sites

**X post:** https://x.com/suraj_sharma14/status/2116062550416871512  
**Author:** Suraj Sharma (@suraj_sharma14) · posted 2026-10-30 (UTC) · 1,099 likes, 50 replies  

## What it is
A tongue-in-cheek "prompt" a vibe coder might paste when their AI-built site doesn't show up on Google, ending with "Page one by Monday. Make no mistakes." The punchline, per the author, is that the list really is the full SEO checklist. It covers three groups of work:
- **Getting crawled and indexed:** server-side rendering, an XML sitemap submitted in Search Console, robots.txt that lets Googlebot in, removing stray noindex tags, collapsing redirect chains, fixing broken links and setting canonical URLs.
- **On-page basics:** a unique title and meta description per page, one H1 per page, FAQ and Article structured data, breadcrumbs, internal links to orphan pages and alt text on images.
- **Speed and trust:** WebP images, layout shift (CLS) under 0.1, pages loading in under two seconds, rewriting text that reads as generic AI output, a real author with a real bio, and backlinks from trusted sites.

The author's advice is to hand the list to a coding agent and do the last two items (real author, earned backlinks) yourself, since those can't be automated.

## Thread highlights
> **@launchpalapp:** Two I'd do before any of it: open URL Inspection in Search Console and click View crawled page, so you know whether Google sees your text or an empty page. And give every page its own title. Plenty of vibe-coded sites are all "Vite + React".

> **@prestonsusant0:** Worth adding a before and after check: save the rendered HTML of each key page with curl, run the prompt, then diff. Pages where the title, canonical or robots tag changed get a manual look, since an agent can strip a noindex you meant to keep.

> **@Indexabledev:** Lovable already serves SSR or prerendered HTML to verified crawlers, so the gap is often per route: the same title on every page, or dead URLs returning 200.

> **@bradvin:** Add view source, check your text is actually in the HTML

> **@dcsan:** Looks like a cheat sheet for getting past the gatekeeper, the real lift still comes from content and intent

## Implications
- **Diagnose before you "fix":** the most useful replies say to first check what Google actually renders (URL Inspection, or the raw HTML) before switching rendering strategy; a client-only React page with one shared title is the usual culprit.
- **Agents can over-apply the list:** "strip every noindex tag" is dangerous on purpose-hidden pages (staging, legal drafts, private demos). Diff the rendered head tags before and after an agent pass.
- **Relevant to game and app landing pages:** store pages, devlogs and press kits built with AI tools hit the same client-rendering and duplicate-title problems; speed items (WebP, CLS, load time) also matter for trailer-heavy pages.
- **Experiment:** for one AI-built landing or devlog site, save each key page's rendered HTML, let a coding agent work through the crawl and on-page items, then diff titles, canonicals and robots tags, and compare Search Console's crawled-page view and indexed-page count two weeks later.

## Tags
`seo` `vibe-coding` `web` `checklist` `launch` `agent-workflow`
