# Long Context Techniques

> Last updated: 2026-03-06

## Milestones

| Model | Context Window | Date |
|-------|---------------|------|
| LLaMA 4 Scout | **10M tokens** | Apr 2025 |
| Qwen2.5-1M | 1M tokens | Early 2025 |
| Mistral Large 3 | 256K tokens | Dec 2025 |
| Gemma 3 / DeepSeek-V3 | 128K tokens | 2025 |

## Key Techniques

### Ring Attention
- Distributes long sequences across GPUs in a ring topology
- Memory complexity: O(n²) → O(n) per device
- **Zig-Zag Ring Attention** fixes load imbalance in autoregressive models
- PyTorch integrated natively into ContextParallel API (late 2025)

### YaRN (Yet another RoPE extensioN)
- Extends context by keeping some RoPE dimensions fixed, stretching others
- Trade-off: may degrade short-task accuracy
- Used as building block by many models

### iRoPE (Meta, LLaMA 4)
- Interleaved NoPE (no positional encoding) layers + temperature scaling
- Foundation for LLaMA 4 Scout's 10M context window

### UltraLong
- Single-stage continued pretraining: 128K → 1M/2M/4M
- 100% accuracy on needle-in-a-haystack up to 4M range

### LongRoPE
- Extends to 2M+ tokens

## Challenge: Context Rot

Research finds that model performance degrades as input tokens increase — "Context Rot." Longer context window ≠ effective use of long context. This remains an active research area.

## Infrastructure Requirements

| Technique | Hardware Need |
|-----------|--------------|
| Ring Attention | Multi-GPU with fast interconnect |
| Sequence Parallelism | NVLink/InfiniBand between GPUs |
| KV Cache offloading | Large CPU RAM or NVMe |
| Chunked prefill | Standard GPU memory |
