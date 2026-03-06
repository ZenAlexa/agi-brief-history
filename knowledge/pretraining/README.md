# Pretraining Frameworks

> Last updated: 2026-03-06

## Selection Matrix

| Scenario | Recommended | Why |
|----------|-------------|-----|
| 100B+ production pretraining | **Megatron-LM + DeepSpeed** | Validated at 1T+ params |
| PyTorch-native path | **TorchTitan** | FSDP2, FP8, no external deps |
| 1B-100B research | **Nanotron** | Minimal 3D parallel, HuggingFace |
| Education/speedrun | **nanochat** | Karpathy's GPT-2 reference |

## Tier 1: Production-Scale

### Megatron-LM (NVIDIA)
- **Scale**: 10B-1T+ parameters
- **Parallelism**: 3D/4D (TP+PP+DP+SP), Megatron Core modular rewrite
- **Validated**: Kimi-K2 (1T MoE), numerous frontier models
- **Key**: De facto standard for large-scale pretraining
- → [megatron-lm.md](megatron-lm.md) | [infra/training/megatron-lm](../../infra/training/megatron-lm/)

### DeepSpeed (Microsoft)
- **Scale**: 1B-1T+ parameters
- **Innovation**: ZeRO Stage 1-3 optimizer, MoE support, heterogeneous hardware
- **Validated**: BLOOM, GLM series
- → [deepspeed.md](deepspeed.md) | [infra/training/deepspeed](../../infra/training/deepspeed/)

### TorchTitan (PyTorch/Meta)
- **Scale**: 1B-100B+ parameters
- **Innovation**: FSDP2 + DTensor, FP8/MXFP8 training, Blackwell GPU support
- **Notable**: IBM trained LLaMA 3 derivative 70B at 1/3 original budget using FP8
- **FSDP2 vs DeepSpeed ZeRO-3**: 5x faster at 100M-1B scale; DeepSpeed wins at 10B+ via memory savings
- → [torchtitan.md](torchtitan.md) | [infra/training/torchtitan](../../infra/training/torchtitan/)

## Tier 2: Research

### Nanotron (HuggingFace)
- Minimal 3D parallel implementation
- Companion: [ultrascale-playbook](https://huggingface.co/spaces/nanotron/ultrascale-playbook)
- → [infra/training/nanotron](../../infra/training/nanotron/)

### LitGPT (Lightning AI)
- 20+ model support, CLI-friendly
- Good for 1B-70B experiments

### GPT-NeoX (EleutherAI)
- Open-source pioneer, historically significant

## Tier 3: Education

### nanochat (Karpathy)
- Successor to nanoGPT (deprecated)
- GPT-2 speedrun leaderboard
- modded-nanogpt: 2-minute GPT-2 124M training

## Distributed Training Techniques

| Dimension | Technique | Scope |
|-----------|-----------|-------|
| Data Parallel | FSDP2, DeepSpeed ZeRO 1-3 | Base scaling |
| Tensor Parallel | Megatron TP | Intra-node GPU |
| Pipeline Parallel | Megatron PP, DualPipe (DeepSeek) | Cross-node |
| Sequence/Context Parallel | Ring Attention, DeepSpeed-Ulysses | Long context (1M+) |
| Expert Parallel | DeepSpeed-MoE, DeepEP, EPLB | MoE models |

## DeepSeek Open Infrastructure (Feb 2025)

5 production-validated components, 50K+ combined stars:
1. **FlashMLA** — Hopper MLA decode kernel (3000 GB/s, 580 TFLOPS)
2. **DualPipe** — Bidirectional pipeline parallelism
3. **DeepEP** — MoE all-to-all communication
4. **EPLB** — Expert parallel load balancer
5. **3FS + smallpond** — Parallel filesystem (6.6 TiB/s) + data processing

→ [infra/deepseek/](../../infra/deepseek/)
