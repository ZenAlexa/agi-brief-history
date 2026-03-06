# Mixture of Experts (MoE)

> Last updated: 2026-03-06

## Why MoE Matters

MoE is now the **de facto architecture** for all frontier open-source models. It reduces training cost by an order of magnitude while maintaining quality.

- DeepSeek-V3: $5.6M training cost vs. hundreds of millions for Western competitors
- DeepSeek-V4: ~1T total params, only ~32B activated per token

## How It Works

```
Input Token
  → Router (learned gating network)
    → Select top-K experts (typically 2 out of N)
      → Each expert processes independently
        → Weighted sum of expert outputs
```

## Key Innovations

| Technique | Origin | Contribution |
|-----------|--------|-------------|
| Fine-grained experts (256 experts) | DeepSeek-V3 | Better specialization at lower per-expert cost |
| Auxiliary-loss-free load balancing | DeepSeek-V3 | Eliminates quality degradation from load balancing loss |
| Multi-head Latent Attention (MLA) | DeepSeek-V2 | KV-cache compression, orthogonal to MoE but critical |
| Static top-2 routing + fused attention | Mixtral | Minimal communication overhead |
| Quantized MoE layers + expert dropout | Qwen/DeepSeek | Reduce inference cost without quality loss |
| iRoPE (interleaved NoPE layers) | LLaMA 4 | Ultra-long context with MoE |

## MoE Models Landscape

| Model | Total Params | Active Params | Experts | Router |
|-------|-------------|--------------|---------|--------|
| DeepSeek-V4 | ~1T | ~32B | 256+ fine-grained | Learned, aux-loss-free |
| DeepSeek-V3 | 671B | 37B | 256 fine-grained | Learned, aux-loss-free |
| Qwen3-235B | 235B | 22B | MoE | Learned |
| LLaMA 4 Maverick | ~400B | 17B | 128 | Learned |
| LLaMA 4 Scout | ~109B | 17B | 16 | Learned |
| Mistral Large 3 | 675B | 41B | MoE | Learned |
| Mixtral 8x22B | 141B | 39B | 8 | Top-2 |

## Infrastructure for MoE

| Component | Purpose | Source |
|-----------|---------|--------|
| **DeepEP** | All-to-all communication for expert dispatch | DeepSeek |
| **EPLB** | Expert parallel load balancing | DeepSeek |
| **DeepSpeed-MoE** | MoE training + inference support | Microsoft |
| **Megatron Expert Parallel** | EP dimension in 4D parallelism | NVIDIA |

## Training Challenges

1. **Load imbalance** — Some experts get more traffic than others → EPLB solves this
2. **Communication overhead** — All-to-all dispatch across GPUs → DeepEP optimizes
3. **Expert collapse** — All tokens route to same experts → Auxiliary loss or DeepSeek's aux-loss-free approach
4. **Memory** — Total params are huge even if active is small → Need careful sharding

## References

- [DeepSeek-V3 Technical Report](https://arxiv.org/abs/2412.19437)
- [Mixtral of Experts](https://arxiv.org/abs/2401.04088)
- [NVIDIA: MoE Powers Frontier AI](https://blogs.nvidia.com/blog/mixture-of-experts-frontier-models/)
