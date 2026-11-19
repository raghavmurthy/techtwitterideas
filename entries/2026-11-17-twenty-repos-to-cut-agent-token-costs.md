# 20 open-source repos for cutting what an agent swarm burns in tokens

**X post:** https://x.com/irongiantXBT/status/2122709093102285099  
**Author:** Iron Giant (@irongiantXBT) · posted 2026-11-17 (UTC) · 2,866 likes, 143 replies  
**Source:** the post itself (all links point to public GitHub repos); the headline story is unverified

## What it is
The post claims a 16-year-old student cut the cost of running 300 agents from about $4,500 a week to under $0.02 per agent per week by removing pointless status checks, not rereading full chat histories, killing endless retry loops, and leaving agents idle until real work arrives. That story comes with no evidence and should be treated as marketing; the useful part is the list of 20 real open-source projects, grouped here by what they do:

- **Shrink inputs before the model reads them:** markitdown (Microsoft; PDFs, Office files and HTML to clean Markdown), LLMLingua (Microsoft; prompt compression that keeps key facts), Firecrawl (web pages to Markdown or structured data), rtk (compresses common command output before it enters context), Chonkie (document chunking), FlagEmbedding (reranking retrieved passages).
- **Remember and reuse instead of regenerating:** mem0 (selected memory across runs), Graphiti (changing facts in a searchable graph), GPTCache (serve saved answers to similar requests), Portkey Gateway (shared response cache), Prefect (cache finished task results), hishel and requests-cache (HTTP caching for fetch tools).
- **Do the waiting in code, not in the model:** Celery (worker queues), APScheduler (scheduled lightweight checks that batch non-urgent work).
- **Route and cap spending:** RouteLLM (send easy requests to a cheaper model), Semantic Router (pick workflows with local embeddings instead of a large model), LiteLLM (spending tracking and budgets), pybreaker (circuit breaker that stops calls to a failing service).
- **Measure:** Arize Phoenix (trace workflows and compare optimisations against output quality).

The post's suggested order is filter before reading, reuse before generating, check for changes, stop failed loops, then measure finished work against total usage including the surrounding tools. It ends by promoting a paid course.

## Thread highlights
> **@undercl0ck:** Good principles here: filter before reading, reuse before generating, stop failed loops. Those are worth doing. I'd be careful with the headline numbers, though. There are no receipts

> **@AlchemistJedi:** Some of these posts have some good ideas on what you can do with your bots just most of them are hyped up way more than what they actually are

> **@Saurabh45584900:** cut the status checks and the chat history rereads and suddenly the swarm is cheap. my api bill basically is status checks lol

## Implications
- **The principles are sound even if the numbers are not:** most agent cost comes from polling, re-reading history and retries, not from the useful work.
- **Asset-pipeline agents benefit too:** converting docs and specs to Markdown first, caching repeated lookups (asset metadata, store pages, API docs) and routing simple classification to a small local model are cheap wins.
- **Ties to model compression:** prompt compression (LLMLingua) and small-model routing are the text-side cousins of quantising models for mobile; both trade a little fidelity for a large cost cut, so measure quality before and after.
- **Experiment:** log one week of a recurring agent workflow, tag each call as useful work, status check, history re-read or retry, then add one fix for the largest non-useful bucket (a cache, a scheduler or a circuit breaker) and compare cost and output quality for the following week.

## Tags
`cost` `tokens` `agents` `caching` `open-source` `compression` `agent-tooling` `observability`
