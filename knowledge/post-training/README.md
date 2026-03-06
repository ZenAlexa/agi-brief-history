# Post-Training: SFT, Alignment, PEFT

> Last updated: 2026-03-06

## The Post-Training Pipeline

```
Pretrained Model
  → SFT (Supervised Fine-Tuning)
    → Alignment (RLHF / DPO / GRPO)
      → Quantization + Deployment
```

## SFT Frameworks

| Rank | Framework | Maintainer | Models Supported | Key Differentiator |
|------|-----------|-----------|-----------------|-------------------|
| 1 | [ms-swift](sft/ms-swift.md) | ModelScope/Alibaba | 1000+ LLM+MLLM | Megatron parallel, GRPO family, v4.0 (2026-03-03) |
| 2 | [LLaMA-Factory](sft/llama-factory.md) | Community | 200+ | Web UI, one-click, 360 sequence parallel |
| 3 | Axolotl | Community | 100+ | YAML config, production-grade, FSDP2 |
| 4 | Unsloth | Unsloth AI | 50+ | 2x speed + 60% memory savings, consumer GPUs |
| 5 | [TorchTune](sft/torchtune.md) | PyTorch/Meta | 20+ | PyTorch-native, SFT/DPO/PPO/GRPO/KD |
| 6 | [TRL](sft/trl.md) | HuggingFace | All HF Hub | HF ecosystem standard |

→ [sft/](sft/)

## Alignment / RL Frameworks

The field has evolved from RLHF (PPO) → DPO → GRPO → REINFORCE++.

| Rank | Framework | Architecture | Algorithms | Scale |
|------|-----------|-------------|-----------|-------|
| 1 | [OpenRLHF](alignment/openrlhf.md) | Ray + vLLM | PPO, REINFORCE++, GRPO, RLOO, DAPO, Async RL | 70B+, cross-GPU actor/reward separation |
| 2 | veRL | Volcano Engine | PPO, GRPO, GSPO, REINFORCE++, PRIME, DAPO | Validated 64×H800 GRPO LoRA |
| 3 | TRL | HuggingFace | SFT, DPO, PPO, RLHF | Medium scale, best HF integration |
| 4 | NeMo-Aligner | NVIDIA | RLHF, DPO, SteerLM | 100B+, NeMo ecosystem |

**Key trend**: REINFORCE++ is emerging as more stable than GRPO, faster than PPO.

→ [alignment/](alignment/)

## PEFT Ecosystem

| Method | Memory Reduction | Quality Retention | Best For |
|--------|-----------------|-------------------|----------|
| LoRA | 10-20x | ~95% | Standard parameter-efficient fine-tuning |
| QLoRA | 20-40x | ~93% | Single A100 can fine-tune 70B |
| LoftQ | 20-40x | ~94% | Joint quantization + adapter optimization |

HuggingFace PEFT library remains the core infrastructure.

→ [peft/](peft/)

## Infra Links

- [infra/post-training/openrlhf](../../infra/post-training/openrlhf/)
- [infra/post-training/ms-swift](../../infra/post-training/ms-swift/)
- [infra/post-training/llama-factory](../../infra/post-training/llama-factory/)
- [infra/post-training/trl](../../infra/post-training/trl/)
