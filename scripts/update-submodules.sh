#!/usr/bin/env bash
# Update all git submodules to their latest remote HEAD (shallow)
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
cd "$REPO_ROOT"

echo "=== Updating all submodules ==="
git submodule foreach --recursive 'git fetch --depth 1 origin HEAD && git checkout FETCH_HEAD'
echo "=== Done. Run 'git diff --submodule' to see changes ==="
