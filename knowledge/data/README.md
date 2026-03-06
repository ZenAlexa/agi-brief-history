# Data Pipelines & Datasets

> Last updated: 2026-03-06

## Core Insight

**Data quality > data quantity.** DCLM and FineWeb-Edu prove that carefully filtered datasets vastly outperform brute-force collection.

## Processing Tools

| Tool | Maintainer | Purpose | Status |
|------|-----------|---------|--------|
| **datatrove** | HuggingFace | Modular pipeline, Slurm distributed | Powers FineWeb (15T tokens) |
| **Data-Juicer** | ModelScope | All-in-one, 20+ operators, multimodal | Very active (v1.4.5, Jan 2026) |
| **Dolma Toolkit** | Allen AI | Trillion-token dataset assembly | OLMo data foundation |
| **smallpond** | DeepSeek | 3FS-based processing | Production-validated (V3/R1) |
| **DataFlow** | OpenDCAI | LLM-driven data prep | Emerging (Jun 2025) |

→ [pipelines/](pipelines/) | [infra/data/](../../infra/data/)

## Key Open Datasets

| Dataset | Scale | Maintainer | Notes |
|---------|-------|-----------|-------|
| **RedPajama-V2** | 30T tokens | Together AI | Largest public LLM training set, 40+ quality annotations |
| **FineWeb** | 15T tokens | HuggingFace | 96 CommonCrawl snapshots, outperforms other open pretraining data |
| **FineWeb-Edu** | 1.3T tokens | HuggingFace | Education-filtered, strong reasoning benchmarks |
| **DCLM-Baseline** | 240T raw → filtered | ML Foundations | 7B model reaches 64% MMLU (5-shot) |
| **Dolma** | 3T tokens | Allen AI | OLMo training set, fully open and traceable |

→ [datasets/](datasets/)

## Data Quality Hierarchy

```
Raw Web Crawl (CommonCrawl ~300T tokens)
  → Language filtering + dedup → RedPajama-V2 (30T)
    → Quality classifiers → FineWeb (15T)
      → Educational content filter → FineWeb-Edu (1.3T)
        → Task-specific curation → domain datasets
```

## Pipeline Architecture Pattern

```
Source (CC/web/synthetic)
  → Extract (warc → text)
  → Clean (dedup, language ID, quality score)
  → Filter (classifier-based or rule-based)
  → Mix (domain proportions)
  → Tokenize
  → Shuffle + Pack
  → Train
```

Both datatrove and Data-Juicer follow this pattern with different operator ecosystems.
