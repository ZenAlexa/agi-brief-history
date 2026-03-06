# 002 - Submodule Selection

**Status**: Accepted
**Date**: 2026-03-06
**Context**: Need to select which open-source projects to include as submodules. Criteria: (1) category leader or uniquely innovative, (2) actively maintained, (3) production-validated.

**Decision**: 16 submodules across 5 categories:

### Inference (3)
- **vLLM** — Production GPU inference standard, 72K stars, PyTorch ecosystem member
- **SGLang** — Highest throughput via RadixAttention, LMSYS team
- **llama.cpp** — CPU/edge inference standard, 97K stars, GGUF format

### Training (4)
- **Megatron-LM** — Large-scale pretraining standard, 3D/4D parallelism
- **DeepSpeed** — ZeRO optimizer series, MoE support
- **TorchTitan** — PyTorch-native, FSDP2, rising star
- **Nanotron** — Minimal 3D parallel implementation, HuggingFace

### Post-Training (4)
- **OpenRLHF** — Best RL alignment toolkit, Ray+vLLM distributed
- **ms-swift** — 1000+ model support, ModelScope/Alibaba
- **LLaMA-Factory** — Web UI, one-click fine-tuning
- **TRL** — HuggingFace ecosystem standard

### Data (2)
- **datatrove** — Modular pipeline, powers FineWeb
- **Data-Juicer** — All-in-one processing, ModelScope

### DeepSeek Infrastructure (3)
- **FlashMLA** — Hopper GPU MLA decode kernel
- **DeepEP** — MoE all-to-all communication library
- **DualPipe** — Bidirectional pipeline parallelism

**Consequences**:
- Covers all major categories with clear leaders
- DeepSeek infra included as reference for cutting-edge techniques
- Missing: Unsloth (not submoduled due to narrow scope, covered in knowledge base), veRL (covered in knowledge base)
- Can add/remove submodules per quarterly review
