<div align="center">

# AGI简史

### A Brief History of AGI

**持续更新的 AGI 知识体系 — 从训练基础设施到前沿论文，一站式观测开源大模型生态**

*An ever-evolving knowledge system for the AGI era — tracking open-source LLM infrastructure, techniques, and frontier research*

<br>

![visitors](https://visitor-badge.laobi.icu/badge?page_id=ZenAlexa.llm-observatory)
[![GitHub stars](https://img.shields.io/github/stars/ZenAlexa/llm-observatory?style=social)](https://github.com/ZenAlexa/llm-observatory/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/ZenAlexa/llm-observatory?style=social)](https://github.com/ZenAlexa/llm-observatory/network/members)
[![MIT License](https://img.shields.io/github/license/ZenAlexa/llm-observatory)](LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/ZenAlexa/llm-observatory)](https://github.com/ZenAlexa/llm-observatory/commits/main)
[![GitHub pull request](https://img.shields.io/badge/PRs-welcome-blue)](https://github.com/ZenAlexa/llm-observatory/pulls)
[![ArXiv Digest](https://img.shields.io/badge/ArXiv_Digest-daily-orange)](knowledge/tracking/arxiv/)

<br>

[中文](#概览) | [English](#overview)

</div>

---

## 概览

这不是又一个 awesome-list。

这是一个**系统性的 AGI 知识工程**：5 本原创书籍/报告（98,000+ 行 LaTeX），覆盖技术演进、商业版图、关键人物与行业泡沫分析；结构化知识库横跨 LLM 全生命周期 7 大领域；16 个核心开源项目作为 Git 子模块实时追踪；GitHub Actions 自动化每日论文摘要与每周排行榜快照。

> 记录 AGI 时代最不可思议的五年。

---

## 📖 原创书籍

全部基于 LaTeX 排版，含 TikZ 架构图、参考文献索引，可直接下载 PDF。

| # | 书名 | 章节 | 主题 | PDF |
|---|------|------|------|-----|
| 1 | **Emergence: The Birth of AGI** | 16 章 | 从 Transformer 到 AGI 的完整技术脉络 — 预训练、MoE、长上下文、后训练、推理优化、评估体系 | [📥 下载](knowledge/techniques/emergence/emergence.pdf) |
| 2 | **AI Startup Landscape** | 23 章 | AI 创业全景 — GPU 云、芯片、模型公司、平台、开发工具、消费产品、企业应用、中国与全球格局 | [📥 下载](knowledge/techniques/ai-startup-landscape/ai-startup-landscape.pdf) |
| 3 | **AI Figures** | 16 章 | AI 关键人物志 — 从先驱到当下，OpenAI/Anthropic/DeepMind/Meta 及中国 AI 领军者 | [📥 下载](knowledge/techniques/ai-figures/ai-figures.pdf) |
| 4 | **Embodied AI** | 6 章 | 具身智能与人形机器人 — 资本泡沫、技术瓶颈、投资链条与现实时间线 | [📥 下载](knowledge/techniques/embodied-ai/embodied-ai.pdf) |
| 5 | **LLM Techniques Report** | — | 核心技术速查 — MoE、量化、长上下文、测试时计算、合成数据 | [📥 下载](knowledge/techniques/llm-techniques-report/llm-techniques-report.pdf) |

> 所有书籍源码（`.tex`）均在仓库中，欢迎 [PR 改进](CONTRIBUTING.md)。

---

## 🗂️ 知识库

结构化知识覆盖 LLM 全生命周期：

| 领域 | 知识文档 | 基础设施子模块 |
|------|---------|---------------|
| **推理** | [inference/](knowledge/inference/) | [vLLM](infra/inference/vllm) · [SGLang](infra/inference/sglang) · [llama.cpp](infra/inference/llama.cpp) |
| **预训练** | [pretraining/](knowledge/pretraining/) | [Megatron-LM](infra/training/megatron-lm) · [DeepSpeed](infra/training/deepspeed) · [TorchTitan](infra/training/torchtitan) · [Nanotron](infra/training/nanotron) |
| **后训练** | [post-training/](knowledge/post-training/) | [OpenRLHF](infra/post-training/openrlhf) · [ms-swift](infra/post-training/ms-swift) · [LLaMA-Factory](infra/post-training/llama-factory) · [TRL](infra/post-training/trl) |
| **数据** | [data/](knowledge/data/) | [datatrove](infra/data/datatrove) · [Data-Juicer](infra/data/data-juicer) |
| **模型** | [models/](knowledge/models/) | — |
| **技术专题** | [techniques/](knowledge/techniques/) — MoE · 量化 · 长上下文 · 测试时计算 · 合成数据 · 模型合并 · 具身智能 | [DeepSeek Infra](infra/deepseek/) (FlashMLA · DualPipe · DeepEP · EPLB) |
| **追踪** | [tracking/](knowledge/tracking/) — 里程碑论文 · 排行榜 · 课程 · 社区 | — |

> 全景地图详见 [knowledge/overview.md](knowledge/overview.md)

---

## 🔭 生态观测（自动化）

GitHub Actions 持续追踪 LLM 生态变化：

| 频率 | 内容 | 输出 |
|------|------|------|
| **每日** 03:17 UTC | ArXiv 论文摘要 (cs.CL, cs.AI, cs.LG) | [`knowledge/tracking/arxiv/`](knowledge/tracking/arxiv/) |
| **每周一三五** 14:43 UTC | 子模块更新 + 排行榜快照 | [`knowledge/tracking/weekly/`](knowledge/tracking/weekly/) |
| **每周一** 06:23 UTC | 综合周报 | [`knowledge/tracking/weekly/`](knowledge/tracking/weekly/) |

---

## 🚀 快速开始

```bash
# 克隆（含子模块浅克隆）
git clone --recurse-submodules --shallow-submodules https://github.com/ZenAlexa/llm-observatory.git

# 或先克隆再初始化子模块
git clone https://github.com/ZenAlexa/llm-observatory.git
cd llm-observatory
git submodule update --init --depth 1

# 更新所有子模块到最新
./scripts/update-submodules.sh
```

---

## 项目结构

```
.
├── knowledge/              # 结构化知识库
│   ├── overview.md         # 全景地图
│   ├── inference/          # 推理框架
│   ├── pretraining/        # 预训练基础设施
│   ├── post-training/      # 后训练 (SFT/RLHF/PEFT)
│   ├── data/               # 数据管线
│   ├── models/             # 模型族谱
│   ├── techniques/         # 技术专题 + 原创书籍
│   └── tracking/           # ArXiv 日报 + 周报 + 排行榜
├── infra/                  # 16 个核心开源项目 (Git 子模块)
│   ├── inference/          # vLLM, SGLang, llama.cpp
│   ├── training/           # Megatron-LM, DeepSpeed, TorchTitan, Nanotron
│   ├── post-training/      # OpenRLHF, ms-swift, LLaMA-Factory, TRL
│   ├── data/               # datatrove, Data-Juicer
│   └── deepseek/           # FlashMLA, DualPipe, DeepEP, EPLB
├── scripts/                # 自动化脚本
│   ├── arxiv-digest.py     # 每日 ArXiv 论文摘要
│   ├── fetch-leaderboard.py # 排行榜快照
│   └── update-submodules.sh # 子模块更新
└── .github/workflows/      # CI/CD 自动化
```

---

## Overview

A systematic knowledge engineering project for the AGI era, featuring:

- **5 original books/reports** (98,000+ lines of LaTeX) covering technical evolution, startup landscape, key figures, and industry analysis
- **Structured knowledge base** across 7 domains of the LLM lifecycle
- **16 core open-source projects** tracked as Git submodules
- **Automated tracking** — daily ArXiv digests, weekly leaderboard snapshots via GitHub Actions

See the [books section](#-原创书籍) for PDF downloads, [knowledge base](#️-知识库) for the full navigation map.

---

## 🤝 Contributing

We welcome all contributions! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

**Quick ways to contribute:**
- 📝 Fix typos or improve content in books and knowledge articles
- 📚 Add new technique articles or knowledge entries
- 🔧 Improve automation scripts
- 🌐 Help with English translations
- ⭐ Star this repo to help others discover it

---

## Contributors

<a href="https://github.com/ZenAlexa/llm-observatory/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=ZenAlexa/llm-observatory" />
</a>

---

## Star History

<a href="https://star-history.com/#ZenAlexa/llm-observatory&Date">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/svg?repos=ZenAlexa/llm-observatory&type=Date&theme=dark" />
    <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/svg?repos=ZenAlexa/llm-observatory&type=Date" />
    <img alt="Star History Chart" src="https://api.star-history.com/svg?repos=ZenAlexa/llm-observatory&type=Date" />
  </picture>
</a>

---

## License

[MIT](LICENSE) — 知识应该是开放的。

---

<div align="center">

*Observing the most extraordinary five years in AI.*

</div>
