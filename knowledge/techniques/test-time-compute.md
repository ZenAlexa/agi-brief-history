# Test-Time Compute / Inference Scaling

> Last updated: 2026-03-06

## Core Insight

**7B model + 100x inference compute ≈ 70B model standard inference.**

Inference demand is projected to exceed training demand by 118x in 2026.

## Three Strategies

### 1. Parallel Scaling
- Generate multiple outputs, aggregate (majority vote, best-of-N)
- Easy to implement, linearly scalable
- Example: Sample 100 solutions, take consensus

### 2. Sequential Scaling
- Guide subsequent computation based on intermediate steps
- "Chain of thought" on steroids
- Example: DeepSeek-R1's thinking tokens, step-by-step verification

### 3. Hybrid Scaling
- Combine parallel and sequential approaches
- ThreadWeaver (2025): parallel reasoning with 1.53x latency speedup while maintaining accuracy

## Reasoning Models

| Model | Approach | Key Result |
|-------|---------|------------|
| DeepSeek-R1 | RL-trained reasoning | AIME 2025: 87.5% (R1-0528) |
| Qwen3 | Hybrid thinking/non-thinking mode | Unified framework, no model switching |
| QwQ | Dedicated reasoning model | 32B, strong math/code |
| P1 | RL + test-time agents | Physics Olympiad gold medal |

## Distillation

Reasoning capabilities can be compressed from 671B → 8B or even 1.5B through distillation. DeepSeek's 6 open distilled checkpoints (based on Qwen2.5 and Llama3) dramatically lowered the barrier.

## Implications

1. **Hardware investment shifts** — Inference GPUs become more valuable than training GPUs
2. **Smaller models become viable** — With enough inference budget, small models compete with large ones
3. **Cost model changes** — Pay-per-quality becomes possible (more compute = better answer)
4. **Architecture rethink** — Models designed for inference scaling differ from training-optimized ones

## References

- [Art of Scaling Test-Time Compute](https://arxiv.org/abs/2512.02008)
- [Lilian Weng: Why We Think](https://lilianweng.github.io/)
