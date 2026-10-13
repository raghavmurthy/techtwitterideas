# FreeVideo: local video generation on 8GB VRAM

**X post:** https://x.com/HaochengXiUCB/status/2106149968994291933  
**Author:** Haocheng Xi 🚗 COLM (@HaochengXiUCB) · posted 2026-10-02 (UTC) · 2479 likes, 94 replies  

## What it is
@HaochengXiUCB introduced FreeVideo (github.com/FlashML-org/FreeVideo), running MiniMax H3 + Video DeltaNet locally with as little as 8GB VRAM + 16GB RAM, with ComfyUI integration, LoRAs and custom workflows. Replies flag poor speed/quality on Mac and a Windows suspicious-exe warning.

## Thread highlights
- @VantageCoach: “Why is this being flagged by Windows as suspicious and there should be no exe in Open Source that cannot be compiled.”
- @dinh_ethan: “Impressive! Thanks for sharing mate. How to do image to video with this tool?”
- @briandonatiello: “speed and quality on mac is horrible though”

## Implications
- Local video generation can produce ambient loops and trailer b-roll without per-clip fees. Given the Windows exe warning, build from source.
- **Experiment:** on an NVIDIA machine, generate a 5 s nature loop and judge it as a menu background.

## Tags
`video-gen` `local-models` `comfyui`
