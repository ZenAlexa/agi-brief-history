# 001 - Repository Structure

**Status**: Accepted
**Date**: 2026-03-06
**Context**: Need a systematic way to track and learn the open-source LLM ecosystem covering inference, training, post-training, data pipelines, and frontier models. Must balance comprehensive knowledge with practical code access on a Mac with limited storage.
**Decision**: Adopt a hybrid knowledge-base + git-submodule architecture. Knowledge base as primary content in `knowledge/`, infrastructure code as shallow-clone submodules in `infra/`. Automation via GitHub Actions for paper tracking and submodule updates.
**Consequences**:
- ~3-5GB disk usage for shallow submodules (manageable on Mac)
- Knowledge base is human-curated, submodules auto-update
- Clear separation: WHAT we know vs. HOW it's built
- Trade-off: submodule operations require familiarity with git submodule commands
