# Take your VPS off the public internet with Tailscale and Cloudflare Tunnel

**X post:** https://x.com/levelsio/status/2113597275519803830  
**Author:** @levelsio (@levelsio) · posted 2026-10-23 (UTC) · 2,404 likes, 41 replies  

## What it is
Indie maker Pieter Levels (levelsio) reposts his own guide on hardening a VPS, saying it matters more now that AI is finding new exploits. He describes two ways into a server: through the site or app (he cites that week's PHP file-upload exploit) and through the server itself (SSH or another open port). His setup: put the public site behind a Cloudflare Tunnel, so the free plan's web application firewall sits in front of it and the server no longer answers on ports 80 or 443; put admin access on a Tailscale network, a private network that only your own devices can join; then block all inbound traffic in the host's firewall (he uses Hetzner and says to test it). Both tools connect outbound, so nothing needs to be open. He says SSH-key login alone doesn't cover this, and that the result is "much safer, not perfect". In a follow-up post he adds that both Cloudflare Tunnel and Tailscale are free and will probably stay free, because they make money from enterprise customers.

## Thread highlights
> **@levelsio:** Now you've reduced your attack vector to Tailscale and your Cloudflare Tunnel, much safer, not perfect btw, but nothing is

> **@grok:** Servers get tags; only allow your devices → servers on specific ports. No reverse paths or server-to-server, so a pwned VPS can't reach others or your laptop.

> **@4wmturner:** this is written for a less technical audience who are clueless about security best practices. No companies except for maybe the smallest startups follow this architecture. Zerotrust is still the way to go.

## Implications
- **Game backends and asset servers:** a small VPS hosting a leaderboard, build cache, or asset CDN origin is a common indie target; a tunnel plus a private admin network removes the open ports that automated scanners look for.
- **Agent infrastructure:** remote machines that run coding agents or render jobs can be reached over a private network instead of public SSH, which also suits multi-machine agent setups.
- **Not a full answer:** replies note this reduces exposure but isn't zero trust; tighten Tailscale access rules so a compromised server can't reach your other devices.
- **Experiment:** on a throwaway VPS, put a test site behind Cloudflare Tunnel and SSH behind Tailscale, close every inbound port in the provider firewall, then scan the public IP from outside to confirm nothing answers.

## Tags
`security` `devops` `vps` `networking` `infrastructure`
