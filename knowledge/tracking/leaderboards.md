# Leaderboards

> Last updated: 2026-03-06

## Primary Leaderboards

| Leaderboard | What It Measures | Update Frequency | Link |
|------------|-----------------|-----------------|------|
| **LMSYS Chatbot Arena** | Human preference ELO (6M+ votes) | Near real-time | [lmarena-ai/chatbot-arena](https://huggingface.co/spaces/lmarena-ai/chatbot-arena) |
| **Open LLM Leaderboard** | MMLU, MMLU-Pro, HumanEval, SWE-bench, GPQA, MATH-500 | Regular | [llm-stats.com](https://llm-stats.com/leaderboards/open-llm-leaderboard) |
| **BigCodeBench** | 1,140 coding tasks | Regular | [bigcode-bench.github.io](https://bigcode-bench.github.io/) |
| **EvalPlus** | HumanEval+ and MBPP+ | Regular | [evalplus.github.io](https://evalplus.github.io/leaderboard.html) |

## Chatbot Arena Top (2026-03)

GLM-5, Kimi K2.5, GLM-4.7 are top-3 with ELO scores within 6 points (1445-1451).

## Key Benchmarks Explained

| Benchmark | What | Why It Matters |
|-----------|------|---------------|
| **SWE-bench Verified** | Real GitHub issue resolution | Most practical coding benchmark (2026) |
| **AIME 2025** | Competition math | Tests deep reasoning |
| **MMLU-Pro** | Advanced MMLU | Harder, less saturated |
| **LiveCodeBench** | Dynamic coding benchmark | Prevents data contamination |
| **Chatbot Arena ELO** | Human preference | Most reliable real-world quality proxy |

## Monitoring Strategy

The `scripts/fetch-leaderboard.py` script snapshots these leaderboards on Mon/Wed/Fri at 14:43 UTC.
Snapshots stored in `knowledge/tracking/weekly/`.
