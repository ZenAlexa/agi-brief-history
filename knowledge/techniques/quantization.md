# Quantization

> Last updated: 2026-03-06

## Overview

Quantization reduces model precision to decrease memory usage and increase inference speed, with controlled quality loss.

## Method Comparison

| Method | Precision | Quality Retention | Speed | Best For | Status |
|--------|-----------|-------------------|-------|----------|--------|
| **FP8** | 8-bit float | ~99% | Hardware-accelerated | H100/B200 native | Mainstream 2025+ |
| **NVFP4** | 4-bit NVIDIA | ~95% | Hardware-accelerated | B200/RTX 50 series | TRT-LLM support |
| **AWQ** | 4-bit weight-only | ~95% | Fast (Marlin-AWQ: 741 tok/s) | GPU, quality priority | Mature |
| **GPTQ** | 4/3/2-bit | ~90% | Fast | GPU, max compression | Mature |
| **GGUF** | Various K-quant | ~92% | CPU-optimized | CPU/hybrid, llama.cpp | Q4_K_M is gold standard |
| **BitsAndBytes** | 4/8-bit | ~93% | Moderate | HuggingFace integration | Mature |

## Decision Tree

```
Need maximum quality?
  → FP8 (if hardware supports) or AWQ 4-bit

Running on CPU or consumer GPU?
  → GGUF Q4_K_M via llama.cpp/Ollama

Running on NVIDIA datacenter GPU?
  → AWQ (quality) or GPTQ (compression)

Running on B200/RTX 50 series?
  → NVFP4 via TensorRT-LLM

Fine-tuning, not just inference?
  → QLoRA (4-bit base + LoRA adapters)
```

## Training-Time Quantization

- **FP8 mixed precision** — DeepSeek pioneered, now in TorchTitan (MXFP8)
- **QLoRA** — 4-bit quantized base model + LoRA adapters, enables 70B fine-tuning on single A100
- **LoftQ** — Joint quantization + adapter initialization optimization

## GGUF Format Details

GGUF (GPT-Generated Unified Format) is the standard for llama.cpp ecosystem:

| Quant | Bits/Weight | Quality | Use Case |
|-------|------------|---------|----------|
| Q2_K | 2.6 | Usable for small models | Extreme compression |
| Q3_K_M | 3.4 | Acceptable | Memory-constrained |
| Q4_K_M | 4.8 | **Gold standard** | Best quality/size balance |
| Q5_K_M | 5.7 | Very good | Quality priority |
| Q6_K | 6.6 | Near-FP16 | Minimal quality loss |
| Q8_0 | 8.0 | ~FP16 | Maximum quality |

## References

- [The New LLM Inference Stack 2025: FA-3, FP8 & FP4](https://www.stixor.com/blogs/new-inference-stack-2025)
- [AWQ vs GPTQ vs GGUF Comparison](https://localaimaster.com/blog/quantization-explained)
