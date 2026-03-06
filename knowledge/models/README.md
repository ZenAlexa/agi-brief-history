# Frontier Model Families

> Last updated: 2026-03-06

## Timeline (2024-2026)

```
2024-12  DeepSeek-V3 (671B MoE, $5.6M training cost → $1T stock selloff)
2025-01  DeepSeek-R1 (reasoning model, MIT, matches o1)
2025-02  DeepSeek Open Source Week (FlashMLA, DualPipe, DeepEP, EPLB, 3FS)
2025-03  Gemma 3 (270M-27B, 140+ languages, multimodal)
2025-04  Qwen 3 (hybrid thinking mode, 119 languages, Apache 2.0)
2025-04  LLaMA 4 Scout/Maverick (MoE + native multimodal, 10M context)
2025-08  DeepSeek-V3.1 (unified V3+R1)
2025-12  DeepSeek-V3.2 (Speciale surpasses GPT-5 on AIME/HMMT)
2025-12  Mistral Large 3 (675B/41B, 256K context, Apache 2.0)
2026-03  DeepSeek-V4 (~1T params, native multimodal, Ascend/Cambricon optimized)
```

## Openness Ranking

| Rank | Model | Weights | Training Code | Data | Logs |
|------|-------|---------|--------------|------|------|
| 1 | **OLMo 3** (Ai2) | Open | Full | Full | Full |
| 2 | **DeepSeek V3/R1** | Open (MIT) | Infra components | Closed | Detailed report |
| 3 | **Qwen 3** | Open (Apache 2.0) | ms-swift | Closed | Report |
| 4 | **LLaMA 4** (Meta) | Open | TorchTitan recipes | Closed | Report |
| 5 | **Mistral** | Open (Apache 2.0) | Partial | Closed | Limited |
| 6 | **Gemma 3** (Google) | Open | Partial | Closed | Limited |

## Model Family Deep Dives

- [deepseek.md](deepseek.md) — V3/V4/R1, MLA+MoE, FP8, $5.6M paradigm shift
- [qwen.md](qwen.md) — Hybrid thinking, 119 languages, Qwen3-VL multimodal
- [llama.md](llama.md) — MoE transition, 10M context, IMO/IOI gold
- [gemma.md](gemma.md) — Small but powerful, 27B beats 405B on LMArena
- [mistral.md](mistral.md) — European leader, 675B MoE, Apache 2.0
- [olmo.md](olmo.md) — Only truly fully-open frontier model
- [glm.md](glm.md) — GLM-5, Kimi K2.5, Chatbot Arena top-3

## Architecture Evolution

```
Dense (GPT/LLaMA-2) → MoE (Mixtral/DeepSeek-V2) → Fine-grained MoE (V3/V4)
                                                    + MLA (Multi-head Latent Attention)
                                                    + Native Multimodal (V4, LLaMA 4)
```

## Key Research Labs

| Lab | Location | Contribution | License |
|-----|----------|-------------|---------|
| **DeepSeek** | Hangzhou | V3/V4/R1, MLA, FP8 training, open infra | MIT |
| **Alibaba/Qwen** | Hangzhou | Qwen 3/3.5, hybrid thinking, ms-swift | Apache 2.0 |
| **Meta/FAIR** | US | LLaMA 4, TorchTitan/TorchTune | Community |
| **Google DeepMind** | US/UK | Gemma 3, small model efficiency | Mixed |
| **Mistral AI** | Paris | Large 3, European leader | Apache 2.0 |
| **Allen AI** | Seattle | OLMo 3, full transparency standard | Apache 2.0 |
| **Zhipu AI** | Beijing | GLM-5, Chatbot Arena top-3 | Mixed |
| **Moonshot** | Beijing | Kimi K2/K2.5, MuonClip optimizer | Mixed |
