# A 24-model local AI pack: open LLMs, image, video, voice and music weights to keep on disk

**X post:** https://x.com/superalesha/status/2121562286078963975  
**Author:** Alexey Fateev (@superalesha) · posted 2026-11-14 (UTC) · 4,393 likes, 131 replies  
**Source:** the post itself (all links point to Hugging Face model pages)

## What it is
Alexey Fateev, whose X bio is about how far four RTX 3090s can go, followed up an earlier post urging people to download open weights by listing the exact 24 repos. His argument: two repos on the list already require a login to download, Hugging Face has removed uncensored repos without warning before, and an API account can be cut off or repriced, while files already on your drive can't be taken away.

The list, by category:
- **LLMs (original weights, a standard GGUF, and an "abliterated" GGUF with refusals removed):** Qwen3.8-27B, Qwen3.8 Flash-Next, GLM-5.3-Flash and DeepSeek V4.1 Flash 1017. For two of them, the abliterated quants are his own uploads.
- **Image:** Qwen-Image 2.1, MOSS-Image Base (Apache 2.0), FLUX.3 Klein for ComfyUI (gated).
- **Video:** Wan 2.2 text-to-video and image-to-video A14B (Apache 2.0), HunyuanVideo 1.5, LTX-2.5 (gated).
- **Voice and TTS:** Fish Audio S2 Pro (non-commercial research licence), Qwen3-TTS 12Hz 1.7B Base (Apache 2.0).
- **Music:** ACE-Step 1.5 (MIT), a YuE2 ComfyUI bundle (non-commercial CC-BY-NC-4.0).
- **Speech to text:** Whisper Large v3 Turbo (MIT).

His download advice, paraphrased: use the official Hugging Face CLI; in a GGUF repo, filter for a single quant level (and all its split shards) instead of pulling every quant; for original weights and media models also keep the configs, tokenizers, text encoders, VAEs, README and LICENSE files; for gated repos, accept the terms on the model card and log in first.

Replies push back on the urgency. An automated reply in the thread estimated the full set at roughly 2.5 to 3.5 TB, and several people note you'll realistically run only a couple of these. Another warns that uncensored quants from unknown uploaders are a supply-chain risk.

## Thread highlights
> **@superalesha:** If a provider bans your account, raises prices or rewrites its rules next month, nobody can take away files that are already on your drive.

> **@JamesTakesOnAI:** 24 models on one disk is a hoarding hobby. you'll run two of them. and "uncensored quants" from random uploaders is where the malicious pickles live, so check hashes and use safetensors before the panic-download.

> **@shibumi_synapse:** Improved, but image model choices are still so bad. Krea 2 and Moss are current top tier.

> **@lostinnews:** If anyone thinks these models will be taken down, upload them to @internetarchive.

## Implications
- **Licences decide what you can ship:** the list mixes Apache 2.0 and MIT models with non-commercial ones (Fish Audio S2 Pro, the YuE2 bundle) and gated ones. For anything that ends up in a commercial game or app, the licence column matters more than the benchmark.
- **Pick one quant, not the repo:** the single most useful tip for disk budgets is filtering a GGUF repo to one quant level. For on-device or laptop use, a Q4-class quant of a 27B model is a very different footprint from the original weights.
- **A local asset pipeline is now plausible end to end:** image (concept art, textures), video (trailer drafts), TTS (placeholder voice lines), music (temp tracks) and Whisper (subtitles) can all run on your own GPU, which removes per-call cost and API policy risk for prototyping.
- **Treat third-party quants as untrusted code paths:** prefer safetensors, check hashes against the original repo where possible, and be cautious with abliterated uploads from individuals.
- **Experiment:** pick the three models you would actually use (for example one LLM quant, one image model, one TTS model), check each licence, download only one quant per LLM, and record disk size, VRAM use and time per output on your own machine. Compare quality against the hosted model you use today on five real tasks before deciding what to keep.

## Tags
`local-models` `open-weights` `models` `huggingface` `compression` `licensing` `tts` `music` `video-gen` `asset-pipeline`
