# Model Merging

> Last updated: 2026-03-06

## What Is It

Combine multiple fine-tuned models into one without additional training. Enables creating custom models with **no GPU required** (CPU-only with Mergekit).

## Key Techniques

| Method | Approach | Notes |
|--------|----------|-------|
| **SLERP** | Spherical linear interpolation | Smooth blending of two models |
| **TIES-Merging** | Trim, elect sign, merge | Handles conflicting parameter updates |
| **DARE** | Drop 90-99% of task vector weights | Surprisingly effective sparsification |
| **Task Arithmetic** | Add/subtract task vectors | Simple but powerful |
| **Model Soups** | Average multiple fine-tuned checkpoints | Improves robustness |

## Tools

- **Mergekit** (Arcee AI): Standard tool, runs on CPU or 8GB VRAM
- **LazyMergekit** (Maxime Labonne): Colab notebook for one-click merging

## Maturity

Evolved from experimental technique to ACM Computing Surveys 2026 review-level research. Individual developers can create competitive custom models without training.

## References

- [Merge Models with Mergekit - HuggingFace](https://huggingface.co/blog/mlabonne/merge-models)
- [Model Merging Introduction - NVIDIA](https://developer.nvidia.com/blog/an-introduction-to-model-merging-for-llms/)
