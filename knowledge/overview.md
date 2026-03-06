# Open-Source LLM Ecosystem Overview

> Last updated: 2026-03-06

## Landscape Map

```
┌─────────────────────────────────────────────────────────────┐
│                    DATA LAYER                                │
│  RedPajama-V2 (30T) │ FineWeb (15T) │ DCLM │ Dolma (3T)    │
│  datatrove │ Data-Juicer │ smallpond (DeepSeek)             │
├─────────────────────────────────────────────────────────────┤
│                  PRETRAINING                                 │
│  Megatron-LM │ DeepSpeed │ TorchTitan │ Nanotron           │
│  3D/4D Parallelism │ ZeRO │ FSDP2 │ FP8 Mixed Precision   │
├─────────────────────────────────────────────────────────────┤
│                 POST-TRAINING                                │
│  SFT: ms-swift │ LLaMA-Factory │ Axolotl │ Unsloth │ TRL  │
│  Alignment: OpenRLHF │ veRL │ GRPO │ REINFORCE++ │ DPO     │
│  PEFT: LoRA │ QLoRA │ LoftQ                                │
├─────────────────────────────────────────────────────────────┤
│                   INFERENCE                                  │
│  GPU: vLLM (72K★) │ SGLang (24K★) │ TensorRT-LLM │ LMDeploy│
│  Local: Ollama (164K★) │ llama.cpp (97K★) │ MLC-LLM        │
├─────────────────────────────────────────────────────────────┤
│                 FRONTIER MODELS                              │
│  DeepSeek V4 (~1T) │ Qwen 3.5 │ LLaMA 4 │ Mistral Large 3 │
│  Gemma 3 │ OLMo 3 │ GLM-5 │ Kimi K2.5                     │
└─────────────────────────────────────────────────────────────┘
```

## Key Trends (2025-2026)

1. **MoE is the standard** — All frontier models use Mixture of Experts
2. **China leads open-source** — DeepSeek and Qwen dominate downloads and quality
3. **Open-closed gap: weeks, not months** — Some open models surpass closed ones
4. **Test-time compute > bigger models** — 7B + 100x inference compute ≈ 70B standard
5. **GRPO family replacing PPO** — REINFORCE++ emerging as most stable RL algorithm
6. **FP8 training is mainstream** — Native on H100/B200, spreading to all frameworks
7. **Papers With Code shut down (Jul 2025)** — HuggingFace Trending Papers is successor

## Category Leaders

| Category | Leader | Why |
|----------|--------|-----|
| GPU Inference | **vLLM** | Ecosystem maturity, PyTorch member, 72K stars |
| Throughput | **SGLang** | RadixAttention, ~29% higher throughput than vLLM |
| Local Inference | **llama.cpp** | Pure C++, GGUF standard, 97K stars |
| Pretraining | **Megatron-LM** | Validated at 1T+ params (Kimi-K2) |
| Fine-tuning | **ms-swift** | 1000+ models, AAAI 2025 |
| RL Alignment | **OpenRLHF** | Ray+vLLM, GRPO/REINFORCE++/PPO, 70B+ scale |
| Data Pipeline | **datatrove** | Powers FineWeb (15T tokens) |
| Fully Open Model | **OLMo 3** | Only model with open data + code + logs |
| Frontier Model | **DeepSeek V4** | ~1T params, native multimodal, MIT license |

## Reading Order for Beginners

1. [knowledge/techniques/](techniques/) — Start with core concepts (MoE, quantization, etc.)
2. [knowledge/models/](models/) — Understand model families and evolution
3. [knowledge/inference/](inference/) — How models are served
4. [knowledge/pretraining/](pretraining/) — How models are trained from scratch
5. [knowledge/post-training/](post-training/) — SFT, alignment, PEFT
6. [knowledge/data/](data/) — Data pipelines and datasets
7. [knowledge/tracking/](tracking/) — Stay current
