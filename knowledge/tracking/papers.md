# Paper Tracking

> Last updated: 2026-03-06

## Daily Sources

| Source | What | Link |
|--------|------|------|
| **HuggingFace Trending Papers** | Daily AI paper trends (successor to Papers With Code) | [huggingface.co/papers](https://huggingface.co/papers) |
| **ArXiv cs.CL** | Computation and Language | [arxiv.org/list/cs.CL/recent](https://arxiv.org/list/cs.CL/recent) |
| **ArXiv cs.AI** | Artificial Intelligence | [arxiv.org/list/cs.AI/recent](https://arxiv.org/list/cs.AI/recent) |
| **ArXiv cs.LG** | Machine Learning | [arxiv.org/list/cs.LG/recent](https://arxiv.org/list/cs.LG/recent) |
| **alphaXiv** | ArXiv discussion + trends | [alphaxiv.org](https://www.alphaxiv.org/) |

## Weekly Curations

| Source | Curator | Link |
|--------|---------|------|
| **ML Papers of the Week** | DAIR.AI | [GitHub](https://github.com/dair-ai/ML-Papers-of-the-Week) |
| **Sebastian Raschka's Lists** | Sebastian Raschka | [2025 Jan-Jun](https://magazine.sebastianraschka.com/p/llm-research-papers-2025-list-one) / [Jul-Dec](https://magazine.sebastianraschka.com/p/llm-research-papers-2025-part2) |

## Tools

| Tool | Purpose |
|------|---------|
| **ArXiv RSS** | `https://rss.arxiv.org/rss/{category}` — daily feed |
| **ArxivDigest** | GPT-based personalized paper recommendations |
| **Semantic Scholar** | Citation-filtered trending papers |

## Must-Read Papers (Foundational)

### Architecture
- Attention Is All You Need (Vaswani et al., 2017)
- LLaMA: Open and Efficient Foundation Language Models (Touvron et al., 2023)
- DeepSeek-V3 Technical Report (2024)
- Qwen3 Technical Report (2025)

### Training
- ZeRO: Memory Optimizations Toward Training Trillion Parameter Models
- Megatron-LM: Training Multi-Billion Parameter Language Models
- Scaling Laws for Neural Language Models (Kaplan et al., 2020)

### Inference
- Efficient Memory Management for LLM Serving with PagedAttention (vLLM)
- SGLang: Efficient Execution of Structured Language Model Programs

### Alignment
- Training Language Models to Follow Instructions with Human Feedback (InstructGPT)
- Direct Preference Optimization (DPO)
- DeepSeekMath: Pushing the Limits of Mathematical Reasoning (GRPO origin)

### Data
- The RefinedWeb Dataset (Falcon)
- DataComp-LM: In Search of the Next Generation of Training Sets

## Automation

Daily ArXiv digest runs at 03:17 UTC via `scripts/arxiv-digest.py`.
Results stored in `knowledge/tracking/arxiv/YYYY-MM-DD.md`.
