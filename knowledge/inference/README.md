# Inference Systems

> Last updated: 2026-03-06

## Selection Matrix

| Scenario | Recommended | Why |
|----------|-------------|-----|
| Production API serving | **vLLM** | Ecosystem maturity, OpenAI-compatible API, PyTorch member |
| Max throughput + prefix sharing | **SGLang** | RadixAttention, ~29% higher throughput |
| NVIDIA latest hardware | **TensorRT-LLM** | B200 optimization, NVFP4, EAGLE-3 |
| Personal/dev local | **Ollama** | One-command deployment |
| Edge/CPU/embedded | **llama.cpp** | Pure C++, GGUF standard |
| MoE + Chinese model ecosystem | **LMDeploy** | High concurrency, InternLM/Qwen optimized |
| Cross-platform mobile | **MLC-LLM** | ML compilation, iOS/Android/Web |

## Tier 1: Production GPU Serving

| Framework | Stars | Key Innovation | Maintainer |
|-----------|-------|---------------|------------|
| [vLLM](vllm.md) | ~72K | PagedAttention, continuous batching | UC Berkeley → PyTorch |
| [SGLang](sglang.md) | ~24K | RadixAttention, zero-overhead CPU scheduler | LMSYS |
| TensorRT-LLM | ~10K | NVIDIA hardware-specific optimization | NVIDIA |
| LMDeploy | ~7.5K | High decode speed, Chinese model optimization | Shanghai AI Lab |

## Tier 2: Local/Edge

| Framework | Stars | Key Feature |
|-----------|-------|-------------|
| Ollama | ~164K | One-click local deployment |
| [llama.cpp](llama-cpp.md) | ~97K | C/C++ native, CPU/GPU hybrid |
| MLC-LLM | ~20K | Cross-platform ML compilation |

## Tier 3: Maintenance Mode

| Framework | Status |
|-----------|--------|
| HuggingFace TGI | Maintenance mode since Dec 2025, bugfixes only |

## Key Techniques

- **PagedAttention** — Non-contiguous KV cache paging, 2-4x throughput (vLLM origin, now universal)
- **RadixAttention** — Radix tree KV cache management, automatic prefix reuse (SGLang)
- **Continuous Batching** — Dynamic request batching, 3-10x throughput improvement
- **Speculative Decoding** — Draft model proposes, large model verifies in parallel, up to 3.6x speedup
- **Disaggregated Serving** — Separate prefill and decode to different GPUs

## Benchmarks (H100)

| Framework | Peak Throughput | Notes |
|-----------|----------------|-------|
| SGLang | ~16,200 tok/s | Tied with LMDeploy, 29% ahead of vLLM |
| LMDeploy | ~16,200 tok/s | Best high-concurrency stability |
| vLLM | ~12,500 tok/s | Most mature ecosystem |
| TensorRT-LLM | Highest on B200 | Hardware-specific advantage |

## Quantization Landscape

| Method | Precision | Quality Retention | Best For |
|--------|-----------|-------------------|----------|
| FP8 | 8-bit float | ~99% | H100/B200 native |
| NVFP4 | 4-bit NVIDIA | ~95% | B200/RTX 50 series |
| AWQ | 4-bit weight-only | ~95% | GPU inference, quality priority |
| GPTQ | 4/3/2-bit | ~90% | GPU inference, max compression |
| GGUF | Various K-quant | ~92% | CPU/hybrid, llama.cpp ecosystem |

→ Deep dives: [vllm.md](vllm.md) | [sglang.md](sglang.md) | [llama-cpp.md](llama-cpp.md)
