# Task Plan: v0.0.41 — Massive Expansion & Bug Fixes

## Project Context

- **Path**: `/Users/zimingwang/Developer/GitHub/llm-observatory/knowledge/techniques/llm-training-landscape/`
- **Main file**: `llm-training-landscape.tex`
- **Template**: `hkustthesis.cls` at `/Users/zimingwang/Library/texmf/tex/latex/hkustthesis/`
- **Current version**: v0.0.40, 21,863 lines, ~227 pages, 15 chapters
- **Target version**: v0.0.41
- **Language**: All LaTeX content in Chinese (简体中文); all code/comments in English

## Chapter Structure & Current Sizes

| Chapter | File | Lines | Sections | Expansion Target |
|---------|------|-------|----------|-----------------|
| Ch01: 为什么「预测下一个词」能产生智能？ | ch01-intro.tex | 719 | 23 | → 1,500+ (2x) |
| Ch02: Transformer——注意力就是一切 | ch02-transformer.tex | 1,643 | 57 | → 2,800+ (1.7x) |
| Ch03: 分词——教机器「认字」 | ch03-tokenization.tex | 1,038 | 40 | → 2,000+ (2x) |
| Ch04: 数据工程——万亿 Token 的炼金术 | ch04-data.tex | 1,651 | 58 | → 2,800+ (1.7x) |
| Ch05: 预训练——从随机噪声到语言理解 | ch05-pretraining.tex | 1,967 | 54 | → 3,200+ (1.6x) |
| Ch06: MoE——参数效率的极致 | ch06-moe.tex | 1,108 | 35 | → 2,200+ (2x) |
| Ch07: 长上下文——让模型阅读整本书 | ch07-long-context.tex | 1,464 | 43 | → 2,500+ (1.7x) |
| Ch08: 后训练——从语言模型到 AI 助手 | ch08-post-training.tex | 2,642 | 72 | → 4,000+ (1.5x) |
| Ch09: 推理优化——让模型跑得更快 | ch09-inference.tex | 1,453 | 43 | → 2,500+ (1.7x) |
| Ch10: 推理时计算缩放 | ch10-test-time.tex | 1,241 | 32 | → 2,200+ (1.8x) |
| Ch11: 评估与安全 | ch11-evaluation.tex | 1,599 | 49 | → 2,800+ (1.7x) |
| Ch12: 团队与组织 | ch12-team.tex | 1,333 | 32 | → 2,500+ (1.9x) |
| Ch13: 前沿展望——LLM 的下一步 | ch13-frontier.tex | 1,534 | 42 | → 2,800+ (1.8x) |
| Ch14: 完整训练流水线速查 (Appendix) | ch14-appendix.tex | 369 | 7 | → 600+ |
| Ch15: 2026 Agent 大战 | ch15-agent-wars.tex | 1,806 | 46 | → 3,000+ (1.7x) |

**Total target: 21,863 → ~38,000+ lines (~400+ pages)**

---

## Phase 0: Infrastructure & Bug Fixes (Agent-Infra)

### Bug 1: TOC Duplication
The Table of Contents itself appears duplicated. Root cause in `hkustthesis.cls` line 319:
```latex
\addcontentsline{toc}{chapter}{\l__hkust_toc_title_text}
```
This adds "Table of Contents" as a TOC entry, creating self-referencing. Combined with `\frontmatter`, this may cause a double entry. Fix: suppress or guard this line.

### Bug 2: Appendix TOC Text Overlap
In the TOC, "Appendix A" prefix overlaps with the chapter title. Root cause in `hkustthesis.cls` line 310:
```latex
\protect\renewcommand{\protect\cftchappresnum}{\appendixname\space}
```
The prefix "Appendix " + chapter number is too wide for the allocated `\cftchapnumwidth`. Fix: increase `\cftchapnumwidth` after `\appendix`, e.g.:
```latex
\setlength{\cftchapnumwidth}{7.5em}  % enough for "Appendix A"
```

### Bug 3: Version Bump
Update cover page: `Draft v0.0.40` → `Draft v0.0.41` (line 266 of main tex file).

### Task: Global TikZ Design System
Define a unified color palette inspired by Nature/Science/Springer journals. Create a shared file `tikz-preamble.tex` with:

```latex
% === Global scientific figure palette (4 primary + 2 accent) ===
% Inspired by Nature/Science/Springer Lecture Notes
\definecolor{figBlue}{HTML}{2166AC}     % Primary: Trust, depth (Nature blue)
\definecolor{figRed}{HTML}{B2182B}      % Secondary: Alert, contrast
\definecolor{figGreen}{HTML}{1B7837}    % Tertiary: Growth, success
\definecolor{figOrange}{HTML}{E66101}   % Quaternary: Warmth, attention
\definecolor{figGray}{HTML}{636363}     % Neutral: Text, borders
\definecolor{figLightGray}{HTML}{F0F0F0} % Background: Subtle fills

% === Reusable TikZ styles ===
% Use positioning library with explicit spacing (right=12mm of nodeA)
% Use fit library for grouping boxes
% Set generous inner sep (8pt+), minimum width (25mm+), minimum height (10mm+)
% Use on background layer for shaded regions
% Think GRID LAYOUT first, then connect
```

Chapters should `\input{tikz-preamble}` or these should go into the main preamble. All TikZ figures across all chapters MUST use only these 6 colors.

---

## Phase 1: Chinese Name Verification (Agent-Names)

### Methodology
1. Extract ALL person names from ALL chapter files (grep for Chinese names, pinyin names, company founder names)
2. For each Chinese person name:
   - Verify the correct Chinese characters (汉字) via `/agent-reach` (search Exa, Twitter/X, official profiles)
   - Verify the standard English transliteration (pinyin order: family name first or last?)
   - Cross-check against the person's own publications, GitHub, or official pages
3. Key names to verify (non-exhaustive):
   - Junyang Lin (阿里通义千问) — 林俊洋 or 林峻洋?
   - Shunyu Yao (Princeton, ReAct/Tree of Thoughts) — 姚顺宇 or 姚顺雨?
   - Any DeepSeek team members
   - Any Kimi/Moonshot, Zhipu, StepFun, ByteDance AI team leads
   - Jensen Huang (黄仁勋) — verify consistency
4. Output a verification table in `findings.md`

---

## Phase 2: Content Expansion (Agents 3–10)

### Global Expansion Rules

**Quality Standard (ICML Reviewer Test)**:
- NO math washing (formulas only when they add insight)
- NO trivial preamble + sudden jump
- NO linear enumeration without thought flow (ideas must build, contrast, echo)
- NO padding with obvious statements
- NO uniform paragraph density (varied rhythm: short punchy + long analytical)
- NO boilerplate transitions ("In this section, we will discuss...")
- Every paragraph must pass the "so what" test
- Intuition BEFORE formalism
- Non-obvious connections between concepts

**Content Sourcing**:
- Use `/agent-reach` for every major claim (Exa search, arXiv, Twitter/X, HackerNews)
- SSOT: Original papers > Official blog posts > Verified reporting > Community discussion
- For 2025-2026 developments: prioritize arXiv papers, official announcements, verified benchmarks
- Add `\cite{}` for every non-trivial claim (bibliography entries will be added to refs.bib)
- Chinese person names: use verified names from Phase 1

**TikZ Figures** (add 1-3 per chapter where valuable):
- Use ONLY the 6-color palette from Phase 0
- Use positioning library with explicit spacing, NOT manual coordinates
- Use fit library for grouping, backgrounds layer for shading
- Minimum node sizes: inner sep=8pt, minimum width=25mm, minimum height=10mm
- Test for overlaps by considering text width + padding
- Think GRID LAYOUT first, then connect

**Structural Rules**:
- Each chapter MUST have at least ONE TikZ figure (architecture diagram, comparison chart, timeline, etc.)
- Thin subsections (< 15 lines of prose) must be expanded to 40+ lines
- Add new subsections where gaps exist in the topic coverage
- Cross-reference other chapters where relevant (`\ref{sec:...}`)
- Maintain chapter-internal logical flow: each section should naturally lead to the next

---

### Agent 3: ch01-intro (719 → 1,500+) + ch03-tokenization (1,038 → 2,000+)

**ch01-intro expansions**:
- Expand the "scaling laws" section with Chinchilla, compute-optimal analysis, Kaplan vs Hoffmann debate
- Add section on "LLM training as a new paradigm" — why next-token prediction is fundamentally different from previous ML
- Expand the training pipeline overview with more detail on each phase
- Add TikZ: LLM training pipeline overview diagram (data → tokenization → pretraining → post-training → inference)

**ch03-tokenization expansions**:
- Expand BPE algorithm explanation with step-by-step worked example
- Add coverage of tokenizer-free approaches (byte-level models, MegaByte, etc.)
- Expand multilingual tokenization challenges (CJK fertility, Arabic/Hebrew RTL, code tokens)
- Add section on tokenization's impact on downstream performance (tokenizer choice as hyperparameter)
- Add TikZ: BPE merge operation visualization

### Agent 4: ch02-transformer (1,643 → 2,800+)

**Expansions**:
- Expand self-attention mechanism with more geometric/intuitive explanation
- Add section on attention variants: Multi-Query Attention, Grouped-Query Attention, Sliding Window, Linear Attention
- Expand positional encoding section: RoPE deep dive, ALiBi, position interpolation
- Add section on Flash Attention (algorithmic innovation, memory hierarchy, IO-awareness)
- Expand normalization discussion: Pre-LN vs Post-LN vs RMSNorm, why Pre-LN became standard
- Add section on activation functions: GeLU, SiLU/Swish, GeGLU, evolution and rationale
- Add TikZ: Multi-head attention architecture diagram with Q/K/V flow

### Agent 5: ch04-data (1,651 → 2,800+) + ch05-pretraining (1,967 → 3,200+)

**ch04-data expansions**:
- Expand data quality filtering pipeline with quantitative thresholds (perplexity, dedup rates)
- Add section on synthetic data generation (Phi-series, Cosmopedia, textbook-quality data thesis)
- Expand data mixing strategies: DoReMi, RegMix, domain proportions, curriculum learning
- Add section on data governance, licensing, copyright (NYT lawsuit, The Pile, C4 composition)
- Add TikZ: Data pipeline flowchart (crawl → filter → dedup → classify → mix → tokenize)

**ch05-pretraining expansions**:
- Expand distributed training: FSDP vs DeepSpeed ZeRO, 3D parallelism taxonomy
- Add section on training stability: loss spikes, gradient explosion, learning rate warmup/decay schedules
- Expand hardware section: H100/H200/B200 comparison, NVLink evolution, InfiniBand vs RoCE
- Add section on Jensen Huang's "Five Layers of AI" vision (silicon → systems → foundation models → platforms → applications) with analysis of where each layer stands in 2026
- Add section on training data scheduling and curriculum (what order to show data, annealing)
- Add TikZ: 3D parallelism diagram (TP × PP × DP)

### Agent 6: ch06-moe (1,108 → 2,200+) + ch07-long-context (1,464 → 2,500+)

**ch06-moe expansions**:
- Expand expert routing mechanisms: Top-k, Expert Choice, hash routing, soft routing
- Add section on MoE training dynamics: load balancing loss, expert specialization, auxiliary losses
- Expand DeepSeek MoE architecture analysis (shared experts, fine-grained experts)
- Add section on Mixtral/DBRX/Grok architecture comparison
- Add section on MoE inference challenges: expert parallelism, all-to-all communication, offloading
- Add TikZ: MoE architecture diagram with router + expert selection visualization

**ch07-long-context expansions**:
- Expand RoPE scaling methods: NTK-aware, YaRN, Dynamic NTK, theoretical analysis
- Add section on context compression: LLMLingua, selective context, landmark attention
- Expand retrieval-augmented approaches: RAG vs long context tradeoff analysis
- Add section on RULER/NIAH benchmarks and what they actually measure
- Add TikZ: Attention pattern comparison (full vs sliding window vs sparse)

### Agent 7: ch08-post-training (2,642 → 4,000+)

**Expansions**:
- Expand RLHF pipeline: reward model training, PPO optimization, practical challenges
- Add section on DPO/IPO/KTO — direct preference optimization family, theoretical comparison
- Expand GRPO (DeepSeek's approach) with mathematical formulation and why it eliminates critic
- Add section on constitutional AI and RLAIF — Anthropic's approach
- Expand tool use / function calling training methodology
- Add section on reasoning model training: how to train o1/R1-style chain-of-thought (process reward models, MCTS, outcome supervision)
- Expand safety alignment: red teaming methodologies, jailbreak taxonomy, defense techniques
- Add TikZ: RLHF pipeline diagram (SFT → RM training → PPO → evaluation)

### Agent 8: ch09-inference (1,453 → 2,500+) + ch10-test-time (1,241 → 2,200+)

**ch09-inference expansions**:
- Expand KV cache optimization: PagedAttention deep dive, vLLM architecture
- Add section on speculative decoding (draft model, Medusa, EAGLE, tree-based verification)
- Expand quantization: GPTQ, AWQ, SqueezeLLM, FP8 training vs inference quantization
- Add section on inference serving systems comparison (vLLM, TensorRT-LLM, SGLang, TGI)
- Add section on disaggregated serving (prefill/decode separation, Mooncake architecture)
- Add TikZ: Speculative decoding tree verification diagram

**ch10-test-time expansions**:
- Expand reasoning scaling analysis: when does more compute help, when doesn't it
- Add section on search strategies: best-of-N, beam search, MCTS, their compute/quality tradeoffs
- Expand process reward models (PRM) vs outcome reward models (ORM) comparison
- Add section on verification: how to verify chain-of-thought, self-consistency, majority voting
- Add TikZ: Test-time compute scaling curve (compute vs accuracy, showing diminishing returns)

### Agent 9: ch11-evaluation (1,599 → 2,800+) + ch12-team (1,333 → 2,500+)

**ch11-evaluation expansions**:
- Expand benchmark taxonomy: knowledge (MMLU), reasoning (GSM8K, MATH), coding (HumanEval, SWE-bench), multimodal
- Add section on contamination detection and mitigation strategies
- Expand LLM-as-judge: Arena, Chatbot Arena Elo, AlpacaEval methodology and biases
- Add section on capability-specific evaluations: tool use, instruction following, creative writing
- Add section on safety evaluations: TruthfulQA, BBQ bias benchmark, HarmBench
- Add TikZ: Benchmark landscape taxonomy diagram

**ch12-team expansions**:
- Expand each major lab profile: OpenAI (culture shift, board crisis aftermath), Anthropic (safety DNA), Google DeepMind (merger dynamics), Meta FAIR (open source strategy), xAI (Grok trajectory)
- Add section on Chinese AI lab ecosystem: DeepSeek (quant fund DNA), Moonshot AI, Zhipu AI, 01.AI, StepFun, MiniMax, ByteDance Doubao — founding stories, differentiation, competitive dynamics
- Expand Jensen Huang's "Five Layers" vision analysis (detailed breakdown of each layer with current progress)
- Add section on AI talent market: compensation, brain drain, geographic concentration
- Add section on compute governance: export controls, NVIDIA H20, Ascend 910C ecosystem
- Add TikZ: Global AI lab competitive landscape map

### Agent 10: ch13-frontier (1,534 → 2,800+) + ch15-agent-wars (1,806 → 3,000+)

**ch13-frontier expansions**:
- Expand world models section: Sora, video generation as world simulation, limitations
- Add section on multimodal native models: Gemini 2.5, GPT-4o, native audio/image/video understanding
- Expand embodied AI / robotics: Figure 02, 1X Neo, Unitree humanoids, sim-to-real transfer
- Add section on science models: AlphaFold 3, protein design, materials discovery, weather prediction
- Expand AI and society: job displacement data, regulatory landscape (EU AI Act, US executive orders)
- Add TikZ: Frontier capability radar chart or timeline

**ch15-agent-wars expansions**:
- Expand MCP protocol technical details with more architectural analysis
- Add section on Computer Use agents: Claude Computer Use, browser automation, OS-level agents
- Expand multi-agent systems: CrewAI, AutoGen, LangGraph, orchestration patterns
- Add section on agent evaluation: real-world task completion rates, failure modes, reliability gaps
- Expand Chinese model details: verify all team lead names, add architecture specifics, training compute
- Add TikZ: Agent architecture layers diagram (LLM → tools → memory → orchestration)

---

## Phase 3: Compilation & Final Verification

After all agents complete:
1. Full `latexmk` compilation — fix all errors and warnings
2. TOC verification — no duplication, no text overlap
3. Figure/table numbering verification (chapter-prefixed: 1.1, 2.1, etc.)
4. Cross-reference check (`\ref{}` all resolve)
5. Page count verification (target: 350-450 pages)
6. Visual spot-check of all new TikZ figures

---

## Agent Assignment Summary

| Agent ID | Name | Scope | Model | Mode |
|----------|------|-------|-------|------|
| 1 | Agent-Infra | Bug fixes + TikZ design system + version bump | sonnet | bypassPermissions |
| 2 | Agent-Names | Chinese name verification (all chapters) | sonnet | bypassPermissions |
| 3 | Agent-Expand-A | ch01 + ch03 | opus | bypassPermissions |
| 4 | Agent-Expand-B | ch02 | opus | bypassPermissions |
| 5 | Agent-Expand-C | ch04 + ch05 | opus | bypassPermissions |
| 6 | Agent-Expand-D | ch06 + ch07 | opus | bypassPermissions |
| 7 | Agent-Expand-E | ch08 | opus | bypassPermissions |
| 8 | Agent-Expand-F | ch09 + ch10 | opus | bypassPermissions |
| 9 | Agent-Expand-G | ch11 + ch12 | opus | bypassPermissions |
| 10 | Agent-Expand-H | ch13 + ch15 | opus | bypassPermissions |

**Critical rule**: Each agent edits ONLY its assigned chapter files. No agent touches another agent's files. The main tex file is edited ONLY by Agent-Infra.
