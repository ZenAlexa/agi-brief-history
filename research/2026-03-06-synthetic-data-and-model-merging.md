# Research: Synthetic Data & Model Merging for LLMs (Early 2026)

Date: 2026-03-06

---

## Part 1: Synthetic Data

### 1.1 Latest Approaches from Frontier Models

#### Phi-4 (Microsoft) — "Data-First" SFT Methodology
- Phi-4 is a 14B parameter model that prioritizes **data quality over scale**.
- Trained on just **1.4 million carefully chosen prompt-response pairs** for SFT.
- Key innovation: selecting "teachable" examples at the **edge of the model's abilities** rather than brute-force scaling.
- Heavy use of **synthetic data generation** for reasoning, math, and STEM tasks.
- The Phi-4 approach proves that **strategic data curation** can make a 14B model compete with much larger ones.
- Phi-4-reasoning-vision (March 2026) extends this with multimodal reasoning, using a **mixture of reasoning and non-reasoning data**.
- Source: [VentureBeat — Phi-4 data-first SFT](https://venturebeat.com/ai/phi-4-proves-that-a-data-first-sft-methodology-is-the-new-differentiator)
- Paper: [arxiv:2412.08905](https://arxiv.org/abs/2412.08905)

#### Qwen3 (Alibaba) — 36T Token Dataset
- Pre-trained on **over 36 trillion tokens** spanning **119 languages and dialects** (nearly 2x the 18T tokens used in Qwen2.5).
- Data sources include **web crawls + PDF-like documents** processed via Qwen2.5-VL for high-quality extraction.
- **Targeted synthetic data generation** using Qwen2.5-Math and Qwen2.5-Coder to augment the corpus with math problem solutions and code snippets.
- Two-stage pre-training: Stage 1 builds foundational knowledge on broad data; Stage 2 increases proportion of STEM, code, and reasoning data.
- Post-training uses **multi-stage RL pipeline** with hybrid thinking/non-thinking modes.
- Source: [Qwen3 Technical Report](https://arxiv.org/html/2505.09388v1)
- Source: [Decoding Qwen3's Training](https://www.cometapi.com/decoding-qwen3s-training-a-deep-dive/)
- Source: [Kili Technology — Data Story: Qwen3's Data Pipeline](https://kili-technology.com/blog/data-story-qwen3)

#### DeepSeek V3 & R1 — RL-Driven + Distillation
- DeepSeek-V3: 671B MoE model pre-trained on **14.8 trillion diverse and high-quality tokens**.
- DeepSeek-R1: Pioneered **reasoning via pure reinforcement learning** (GRPO) without SFT (R1-Zero), demonstrating that reasoning capabilities can emerge from RL alone.
- The V3/R1 relationship is symbiotic: R1 generates reasoning data used in V3's SFT stage; V3-Base serves as the foundation for R1 training.
- **Distillation pipeline**: R1's reasoning patterns distilled into 6 smaller dense models (1.5B-70B) based on Qwen and Llama architectures.
- February 2026 controversy: Anthropic alleged that DeepSeek (and other Chinese labs) used Claude outputs to generate synthetic training data, creating 24,000+ accounts and 16M+ exchanges.
- Paper: [DeepSeek-V3 Technical Report](https://arxiv.org/pdf/2412.19437)
- Paper: [DeepSeek-R1 Paper](https://deepseek-r1.com/paper-deepseek-r1-incentivizing-reasoning-capability-in-llms-via-reinforcement-learning/)

#### The Broader 2025 Trend (Sebastian Raschka's State of LLMs 2025)
- 2025 was "the year of reasoning, RLVR, and GRPO."
- Synthetic data is now central to the training pipeline, not an afterthought.
- The industry consensus: we are running out of high-quality human text (Epoch AI projects exhaustion by 2026-2028).
- Source: [State of LLMs 2025 — Sebastian Raschka](https://magazine.sebastianraschka.com/p/state-of-llms-2025)

---

### 1.2 Model Collapse Research

#### Key Findings

**"Collapse or Thrive?" (Kazdan, Schaeffer, Donoho et al., 2025)**
- Studied three training workflows across three generative model settings.
- Confirms that **replacing all real data with successive synthetic generations causes collapse**.
- However, collapse **can be contained** by managing how data is used:
  - Accumulating synthetic data alongside real data (not replacing it) avoids collapse.
  - Single-round synthetic augmentation (n=1) is much safer than recursive/iterative generation.
- Paper: [arxiv:2410.16713](https://arxiv.org/pdf/2410.16713)

**Meta FAIR — "Demystifying Synthetic Data in LLM Pre-training" (Oct 2025, EMNLP 2025)**
- Massive empirical study: **>1000 LLMs trained with >100k GPU hours**.
- Key findings:
  - Pre-training on **rephrased synthetic data alone is NOT faster** than natural web text.
  - **1/3 rephrased synthetic + 2/3 natural web text** can speed up training 5-10x at larger data budgets.
  - **Textbook-style synthetic data alone** results in notably higher loss on many downstream domains.
  - Optimal synthetic ratio empirically converges to **~30% for rephrased synthetic data**.
  - **Larger generator models do NOT necessarily produce better pre-training data** than ~8B-param generators.
  - Rephrased synthetic data shows **no degradation at foreseeable scales** (single-round), while textbook-style pure-generated data shows collapse patterns.
- Paper: [arxiv:2510.01631](https://arxiv.org/abs/2510.01631)

**"Data Value in the Age of Scaling" (Nov 2025)**
- Identifies a **three-phase scaling behavior** with two breakpoints reflecting transitions in head vs. tail knowledge learning.
- Synthetic data introduces **systematic distributional discrepancies**, particularly underrepresenting long-tail knowledge (due to top-p sampling, temperature scaling, finite sampling).
- Proposes an LLM generalization bound for real-synthetic mixtures.
- Paper: [arxiv:2511.13640](https://arxiv.org/abs/2511.13640)

**Epoch AI / General Consensus (2026)**
- High-quality human-generated text predicted to be exhausted by **2026-2028**.
- The community increasingly treats model collapse as a **manageable risk**, not an insurmountable barrier — provided best practices are followed (diversity, real data anchoring, quality filtering).
- Source: [Level Up Coding — Can AI Models Learn Without Collapsing?](https://levelup.gitconnected.com/can-ai-models-learn-from-synthetic-data-without-collapsing-d8ab1e83e962)

---

### 1.3 Open-Source Tools & Pipelines

| Tool | Maintainer | Description | URL |
|------|-----------|-------------|-----|
| **Distilabel** | Argilla | Framework for synthetic data generation and AI feedback. Supports complex multi-step pipelines, multiple LLM providers, YAML-based configuration. Most mature option. | [distilabel.argilla.io](https://distilabel.argilla.io/latest) |
| **InstructLab / SDG** | Red Hat / IBM | Skills-based taxonomy approach. Contributors define skill recipes (input/output examples), system generates synthetic data, then fine-tunes. Community-driven model improvement. | [instructlab.ai](https://instructlab.ai/) / [github.com/instructlab/sdg](https://github.com/instructlab/sdg) |
| **SDG Hub** | Red Hat | Modular open-source framework for designing and orchestrating synthetic data pipelines. YAML-based orchestration, schema discovery, async execution. | [Red Hat Developer](https://developers.redhat.com/articles/2025/11/25/building-domain-specific-llms-synthetic-data-and-sdg-hub) |
| **DataGen (UniGen)** | ICLR 2025 | Unified synthetic dataset generation framework via LLMs. Academic origin, research-grade. | [github.com/HowieHwong/UniGen](https://github.com/HowieHwong/UniGen) |
| **DeepFabric** | Community (lukehinds) | End-to-end pipeline: generate synthetics, train, measure, evaluate. Supports distillation, HuggingFace integration, Unsloth. 840+ stars, actively maintained (v4.12.0, Feb 2026). | [github.com/always-further/deepfabric](https://github.com/lukehinds/promptwright) |
| **synth_gen** | Meta (FAIR) | Synthetic data generation with execution-based verification and grounding for LLM training. | [github.com/facebookresearch/synth_gen](https://github.com/facebookresearch/synth_gen) |
| **Kiln** | Kiln-AI | GUI-based tool for fine-tuning, synthetic data generation, and dataset collaboration. Easiest UX for non-technical users. | [github.com/kiln-ai/kiln](https://github.com/kiln-ai/kiln) |
| **Evidently (0.7.11+)** | Evidently AI | Synthetic data generation specifically for LLM system testing (RAG, chatbots, agents). Focused on evaluation datasets. | [evidentlyai.com](https://www.evidentlyai.com/blog/synthetic-data-generator-python) |
| **Kolosal-Plane** | Genta Technology | On-device synthetic data generation for LLM and embedding models. | [github.com/genta-technology/kolosal-plane](https://github.com/genta-technology/kolosal-plane) |

---

### 1.4 Best Practices

#### Optimal Synthetic-to-Real Data Ratios
- **Meta FAIR's finding**: ~30% rephrased synthetic + ~70% natural web data is the empirically optimal ratio for pre-training (converges across model sizes and data budgets).
- **1/3 synthetic + 2/3 real** can speed up training 5-10x compared to pure real data.
- Pure synthetic data alone does NOT outperform natural data for pre-training.
- For SFT/fine-tuning: higher synthetic ratios are acceptable (Phi-4 uses heavily curated synthetic data for SFT).
- The optimal ratio depends on: model size, data budget, type of synthetic data (rephrased vs. generated), and downstream task.

#### Quality Filtering Approaches
1. **Curriculum-based selection** (Phi-4): Choose examples at the "edge" of model capability — not too easy, not too hard.
2. **Execution-based verification** (Meta synth_gen): Verify code/math synthetic data by actually executing it.
3. **LLM-as-judge** filtering: Use a stronger model to score/filter synthetic outputs before including in training set.
4. **Diversity enforcement**: Ensure synthetic data covers the full distribution, especially long-tail knowledge that generators tend to underrepresent.
5. **Deduplication**: Remove near-duplicate synthetic outputs that reduce effective dataset diversity.
6. **Domain-specific generators**: Use specialized models (e.g., Qwen2.5-Math for math, Qwen2.5-Coder for code) rather than a single general model.

#### Anti-Patterns to Avoid
- **Recursive/iterative synthetic generation** (training on synthetic, generating more synthetic, repeat) — leads to model collapse.
- **Pure textbook-style synthetic data** for pre-training — high loss on many downstream domains.
- **Assuming bigger generators are better** — 8B-param generators can produce pre-training data as good as larger models.
- **Ignoring long-tail distribution** — synthetic data systematically underrepresents rare knowledge.

#### Scaling Laws Reference
- NeurIPS 2025: "Scaling Laws for Optimal Data Mixtures" — proposes systematic methods to determine optimal data mixtures using scaling laws, validated across LLM, multimodal, and vision model pre-training.
- Source: [NeurIPS 2025 Poster](https://neurips.cc/virtual/2025/poster/115404)

---

## Part 2: Model Merging

### 2.1 Techniques (Current as of Early 2026)

#### Established Methods

| Method | How It Works | Best For |
|--------|-------------|----------|
| **Linear (Weighted Average)** | Simple weighted average of model parameters | Baseline; surprisingly effective for similar models |
| **SLERP** (Spherical Linear Interpolation) | Interpolates along the hypersphere surface, preserving weight magnitude/geometry | Merging exactly 2 models; smooth interpolation |
| **TIES** (Trim, Elect Sign, Scale) | Trims low-magnitude changes, resolves sign conflicts via majority vote, scales remaining | Resolving conflicts between multiple adapters |
| **DARE** (Drop And REscale) | Randomly drops delta parameters and rescales survivors | Highly specialized adapters; reducing interference |
| **Task Arithmetic** | Computes "task vectors" (fine-tuned - base), then adds/subtracts them | Adding/removing specific capabilities |
| **Model Soups** | Averages multiple fine-tuned checkpoints of the same base | Improving robustness without capability conflicts |

#### New Methods (2025-2026)

**Evolutionary Model Merging (Sakana AI, published Nature Machine Intelligence Jan 2025)**
- Uses **evolutionary algorithms** (CMA-ES) to automatically discover optimal merge recipes.
- Evolves both **layer-level mixing coefficients** and **data flow paths** between models.
- No human intuition needed for hyperparameter selection — the algorithm searches the space.
- Implemented in MergeKit by Arcee AI, making it available to the community.
- Paper: [Nature Machine Intelligence](https://www.nature.com/articles/s42256-024-00975-8)

**M2N2 — Model Merging of Natural Niches (Sakana AI, Aug-Sep 2025)**
- Extends evolutionary merging to evolve **merge boundaries** (not just coefficients).
- Uses **complementarity** to select parent models — picks models that cover each other's weaknesses.
- Can merge across modalities (text + image models).
- Example: Fused WizardMath-7B (math) + AgentEvol-7B (agent tasks) into a versatile model excelling at both.
- Source: [In-Depth M2N2 Analysis](https://blog.greeden.me/en/2025/09/02/definitive-guide-in-depth-analysis-of-sakana-ais-m2n2-the-new-frontier-of-model-merging-via-evolution-mechanism-effects-comparisons-and-adoption-roadmap-september-2025-edition/)

**Arcee Fusion (MergeKit v0.1, Feb 2025)**
- Enterprise-grade merging with multi-GPU acceleration.
- Expanded model support and premium features.
- Source: [Arcee Blog — MergeKit v0.1](https://arcee.ai/blog/meet-mergekit-v0-1-arcee-fusion-expanded-model-support-multi-gpu-acceleration)

---

### 2.2 Tooling Landscape

| Tool | Maintainer | Status | Notes |
|------|-----------|--------|-------|
| **MergeKit** | Arcee AI | Dominant (6.8k+ stars, v0.1.4, Oct 2025) | Industry standard. Supports Linear, SLERP, TIES, DARE, Task Arithmetic, Passthrough, Model Soups, Evolutionary. Out-of-core approach (CPU-only or 8GB VRAM). YAML config. Last push: Jan 2026. |
| **MergeKit Enterprise** | Arcee AI | Commercial | Licensed version with Arcee Fusion, multi-GPU, premium support. |
| **HuggingFace Model Merging** | HuggingFace | Built-in | Basic merging capabilities integrated into the HF ecosystem. |
| **LazyMergekit** | Maxime Labonne | Community | Automated notebook/Colab wrapper for MergeKit — easiest way to get started. |

MergeKit remains the **unchallenged dominant tool** in this space. No serious competitor has emerged. The GitHub repo: [github.com/arcee-ai/mergekit](https://github.com/arcee-ai/mergekit)

---

### 2.3 Practical Results & Competitions

#### NeurIPS 2024 LLM Merging Competition
- Official competition: "Building LLMs Efficiently through Merging."
- Rules: models must be reproducible, <1 hour to merge/fine-tune on a single A6000 (48GB), open-sourced after competition.
- Restricted to publicly available HuggingFace models <=8B parameters uploaded before May 2024.
- Source: [llm-merging.github.io](https://llm-merging.github.io/rules.html)

#### Open LLM Leaderboard Impact
- Model merging has historically produced many top-ranking models on the Open LLM Leaderboard.
- Maxime Labonne's **Marcoro14-7B-slerp** was the #1 model on the Open LLM Leaderboard (Jan 2024) — created purely through SLERP merging.
- In 2025-2026, merged models continue to appear on leaderboards, though the competitive landscape has shifted toward reasoning models (DeepSeek-R1, Qwen3, etc.).

#### Real-World Applications (from MergeKit Research Spotlight, June 2025)
- **Pre-training merging**: Combining models trained on different data distributions.
- **Healthcare data privacy**: Merging models fine-tuned on separate hospital datasets without sharing patient data.
- **Language support**: Adding multilingual capabilities by merging language-specific fine-tunes.
- Source: [Arcee Research Spotlight](https://www.arcee.ai/blog/research-spotlight-3-learnings-from-3-use-cases-of-mergekit)

#### Key Insight (Zylos Research, Jan 2026)
- Model merging is now "a core skill in the open-source LLM ecosystem."
- Many community models on HuggingFace rely on merging to combine chat ability, coding strength, reasoning, and domain skills into a single deployable model.
- Source: [Zylos Research — Model Merging 2026](https://zylos.ai/research/2026-01-24-model-merging-llm)

---

### 2.4 Best Tutorials & Resources

#### Essential Reads

1. **Maxime Labonne — "Merge Large Language Models with mergekit"** (HuggingFace Blog)
   - The definitive practical tutorial. Covers SLERP, TIES, DARE, Task Arithmetic with MergeKit YAML configs. Includes LazyMergekit notebook.
   - URL: [huggingface.co/blog/mlabonne/merge-models](https://huggingface.co/blog/mlabonne/merge-models)

2. **Cameron R. Wolfe — "Model Merging: A Survey"** (Deep Learning Focus, Sep 2024)
   - Academic-grade survey covering history from early ML to modern LLM applications.
   - URL: [cameronrwolfe.substack.com/p/model-merging](https://cameronrwolfe.substack.com/p/model-merging)

3. **Ionio — "A Comprehensive Guide on Merging Language Models"**
   - Hands-on implementation guide covering Model Soups, SLERP, Task Arithmetic, TIES, MoE with MergeKit.
   - URL: [ionio.ai/blog/merge-ai-models-using-mergekit](https://www.ionio.ai/blog/merge-ai-models-using-mergekit)

4. **Zylos Research — "Model Merging for Large Language Models 2026"** (Jan 2026)
   - Up-to-date executive summary of the entire field as of early 2026.
   - URL: [zylos.ai/research/2026-01-24-model-merging-llm](https://zylos.ai/research/2026-01-24-model-merging-llm)

5. **Agent Factory — "Merging Techniques Deep Dive"** (Updated Mar 2026)
   - Technical deep dive into Linear, SLERP, TIES, DARE with parameter interference explanations.
   - URL: [agentfactory.panaversity.org — Merging Techniques](https://agentfactory.panaversity.org/docs/Turing-LLMOps-Proprietary-Intelligence/model-merging-optimization/merging-techniques)

6. **EnnengYang — "Awesome Model Merging Methods, Theories, Applications"** (ACM Computing Surveys 2025)
   - Comprehensive paper list and taxonomy. The go-to academic reference.
   - URL: [github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications](https://github.com/EnnengYang/Awesome-Model-Merging-Methods-Theories-Applications)

7. **Maxime Labonne — "Fine-Tuning & Merging LLMs" Talk** (Apr 2025)
   - Video/talk covering the three stages of LLM training (pre-training, SFT, alignment) and how merging fits in.
   - URL: [Medium summary](https://medium.com/%40space.57930/how-to-make-your-ai-agent-smarter-fine-tuning-merging-llms-with-maxime-labonne-21fc2d62916e)

8. **MergeKit Paper** (Arcee, arxiv 2024, updated 2025)
   - Official MergeKit paper describing the toolkit architecture and supported algorithms.
   - URL: [arxiv.org/html/2403.13257v3](https://arxiv.org/html/2403.13257v3)

---

## Summary of Key Takeaways

### Synthetic Data
- Frontier models (Phi-4, Qwen3, DeepSeek) all use synthetic data heavily but with different strategies: Phi-4 emphasizes quality curation, Qwen3 emphasizes scale + domain-specific generation, DeepSeek emphasizes RL + distillation.
- Model collapse is real but manageable: avoid recursive generation, maintain real data anchoring, cap synthetic at ~30% for pre-training.
- The tooling ecosystem is maturing: Distilabel (Argilla), InstructLab (Red Hat/IBM), and DeepFabric lead the open-source space.
- Meta's large-scale study (1000+ LLMs) provides the most rigorous empirical guidance on ratios and practices.

### Model Merging
- Core techniques (SLERP, TIES, DARE) remain dominant; evolutionary optimization (Sakana AI) is the major new addition.
- MergeKit is the unchallenged standard tool (6.8k stars, active development).
- Merging is now a "core skill" in the open-source LLM ecosystem, with many HuggingFace models being merges.
- The NeurIPS 2024 competition formalized the practice; Maxime Labonne's tutorials remain the best starting point.
