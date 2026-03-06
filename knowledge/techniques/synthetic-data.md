# Synthetic Data

> Last updated: 2026-03-06

## Status

Synthetic data is now a **standard component** of frontier model training. The consensus for 2026: **synthetic + curated human data hybrid strategy**.

## Use Cases

| Use Case | Example |
|----------|---------|
| Code generation data | Qwen3 (36T tokens includes massive synthetic code) |
| Math reasoning | DeepSeek-R1 distillation data |
| Instruction following | Self-instruct, Evol-Instruct |
| Safety/alignment | Red-teaming synthetic data |
| Domain-specific | Medical, legal, scientific |

## Key Approaches

### Self-Instruct / Evol-Instruct
- LLM generates its own training data
- Evol-Instruct (WizardLM): iteratively evolves complexity

### Distillation
- Large model generates reasoning traces → train smaller model
- DeepSeek-R1 → R1-distill-1.5B/7B/8B/14B/32B/70B

### Synthetic-to-Real Pipeline
```
Strong Model (teacher)
  → Generate diverse examples
    → Quality filter (verifier model or rule-based)
      → Mix with human data (typically 50-80% synthetic)
        → Train target model
```

## Risks

### Model Collapse
Training exclusively on synthetic data can cause performance degradation over generations. The model "forgets" the tails of the distribution.

**Mitigation**: Always mix with curated human/web data. Typical ratio: 50-80% synthetic + 20-50% human.

## Notable Projects

- **Phi-4** (Microsoft): Built primarily on synthetic + curated public data
- **Cosmopedia** (HuggingFace): Synthetic textbook-quality data for pretraining
- **OpenHermes**: Community synthetic instruction dataset
