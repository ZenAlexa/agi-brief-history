# Infrastructure — Git Submodules

All submodules use shallow clone (`--depth 1`) to minimize disk usage (~3-5GB total).

## Initialize

```bash
git submodule update --init --depth 1
```

## Update All

```bash
./scripts/update-submodules.sh
```

## Submodule Inventory

### Inference (3)
| Submodule | Upstream | Stars | Purpose |
|-----------|----------|-------|---------|
| `inference/vllm` | [vllm-project/vllm](https://github.com/vllm-project/vllm) | ~72K | Production GPU inference, PagedAttention |
| `inference/sglang` | [sgl-project/sglang](https://github.com/sgl-project/sglang) | ~24K | Highest throughput, RadixAttention |
| `inference/llama.cpp` | [ggml-org/llama.cpp](https://github.com/ggml-org/llama.cpp) | ~97K | CPU/edge inference, GGUF standard |

### Training (4)
| Submodule | Upstream | Purpose |
|-----------|----------|---------|
| `training/megatron-lm` | [NVIDIA/Megatron-LM](https://github.com/NVIDIA/Megatron-LM) | 3D/4D parallel, production pretraining |
| `training/deepspeed` | [microsoft/DeepSpeed](https://github.com/microsoft/DeepSpeed) | ZeRO optimizer, MoE support |
| `training/torchtitan` | [pytorch/torchtitan](https://github.com/pytorch/torchtitan) | PyTorch-native, FSDP2, FP8 |
| `training/nanotron` | [huggingface/nanotron](https://github.com/huggingface/nanotron) | Minimal 3D parallel |

### Post-Training (4)
| Submodule | Upstream | Purpose |
|-----------|----------|---------|
| `post-training/openrlhf` | [OpenRLHF/OpenRLHF](https://github.com/OpenRLHF/OpenRLHF) | RL alignment (PPO/GRPO/REINFORCE++) |
| `post-training/ms-swift` | [modelscope/ms-swift](https://github.com/modelscope/ms-swift) | 1000+ model fine-tuning |
| `post-training/llama-factory` | [hiyouga/LLaMA-Factory](https://github.com/hiyouga/LLaMA-Factory) | Web UI fine-tuning |
| `post-training/trl` | [huggingface/trl](https://github.com/huggingface/trl) | HF ecosystem SFT/DPO/PPO |

### Data (2)
| Submodule | Upstream | Purpose |
|-----------|----------|---------|
| `data/datatrove` | [huggingface/datatrove](https://github.com/huggingface/datatrove) | Modular data pipeline (powers FineWeb) |
| `data/data-juicer` | [modelscope/data-juicer](https://github.com/modelscope/data-juicer) | All-in-one data processing |

### DeepSeek Infrastructure (4)
| Submodule | Upstream | Purpose |
|-----------|----------|---------|
| `deepseek/FlashMLA` | [deepseek-ai/FlashMLA](https://github.com/deepseek-ai/FlashMLA) | Hopper MLA decode kernel |
| `deepseek/DeepEP` | [deepseek-ai/DeepEP](https://github.com/deepseek-ai/DeepEP) | MoE all-to-all communication |
| `deepseek/DualPipe` | [deepseek-ai/DualPipe](https://github.com/deepseek-ai/DualPipe) | Bidirectional pipeline parallelism |
| `deepseek/EPLB` | [deepseek-ai/EPLB](https://github.com/deepseek-ai/EPLB) | Expert parallel load balancer |
