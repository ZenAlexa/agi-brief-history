# LLM Observatory

A systematic knowledge base and infrastructure tracking system for the open-source LLM ecosystem.

## Quick Navigation

| Area | Knowledge | Infrastructure |
|------|-----------|---------------|
| **Inference** | [knowledge/inference/](knowledge/inference/) | [infra/inference/](infra/inference/) |
| **Pretraining** | [knowledge/pretraining/](knowledge/pretraining/) | [infra/training/](infra/training/) |
| **Post-Training** | [knowledge/post-training/](knowledge/post-training/) | [infra/post-training/](infra/post-training/) |
| **Data Pipelines** | [knowledge/data/](knowledge/data/) | [infra/data/](infra/data/) |
| **Models** | [knowledge/models/](knowledge/models/) | — |
| **Techniques** | [knowledge/techniques/](knowledge/techniques/) | — |
| **Tracking** | [knowledge/tracking/](knowledge/tracking/) | — |

## Architecture

- **`knowledge/`** — Structured knowledge base covering the full LLM lifecycle
- **`infra/`** — Git submodules of core open-source projects (shallow clones)
- **`notebooks/`** — Quick-start experiments for each domain
- **`scripts/`** — Automation: paper digests, leaderboard snapshots, submodule updates
- **`.claude/decisions/`** — ADR-style decision records

## Automation

| Schedule | Action |
|----------|--------|
| Daily 03:17 UTC | ArXiv paper digest (cs.CL, cs.AI, cs.LG) |
| Mon/Wed/Fri 14:43 UTC | Submodule update check + leaderboard snapshot |
| Weekly Mon 06:23 UTC | Comprehensive weekly digest |

## Submodules

All infrastructure code lives as git submodules under `infra/`. To initialize:

```bash
git submodule update --init --depth 1
```

To update all submodules to latest:

```bash
./scripts/update-submodules.sh
```

## License

Knowledge base content: CC-BY-4.0. Infrastructure code retains its original license.
