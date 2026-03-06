#!/usr/bin/env python3
"""
Fetch and snapshot key LLM leaderboard data.
Stores results as markdown in knowledge/tracking/weekly/.
"""

import json
import os
import urllib.request
from datetime import datetime


def fetch_json(url: str, timeout: int = 30) -> dict | list | None:
    """Fetch JSON from URL with error handling."""
    try:
        req = urllib.request.Request(url)
        req.add_header("User-Agent", "llm-observatory/1.0")
        req.add_header("Accept", "application/json")
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            return json.loads(resp.read())
    except Exception as e:
        print(f"Error fetching {url}: {e}")
        return None


def generate_snapshot() -> str:
    """Generate a weekly leaderboard snapshot."""
    now = datetime.utcnow()
    lines = [
        f"# Weekly Leaderboard Snapshot — {now.strftime('%Y-W%W')}",
        "",
        f"> Generated: {now.strftime('%Y-%m-%d %H:%M UTC')}",
        "",
        "## Links (manual review)",
        "",
        "- [LMSYS Chatbot Arena](https://huggingface.co/spaces/lmarena-ai/chatbot-arena)",
        "- [Open LLM Leaderboard](https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard)",
        "- [BigCodeBench](https://bigcode-bench.github.io/)",
        "- [EvalPlus](https://evalplus.github.io/leaderboard.html)",
        "- [SWE-bench](https://www.swebench.com/)",
        "",
        "## Submodule Release Check",
        "",
    ]

    # Check latest releases for key repos
    repos = [
        "vllm-project/vllm",
        "sgl-project/sglang",
        "ggml-org/llama.cpp",
        "NVIDIA/Megatron-LM",
        "microsoft/DeepSpeed",
        "pytorch/torchtitan",
        "OpenRLHF/OpenRLHF",
        "modelscope/ms-swift",
        "hiyouga/LLaMA-Factory",
        "huggingface/trl",
        "huggingface/datatrove",
        "modelscope/data-juicer",
    ]

    for repo in repos:
        url = f"https://api.github.com/repos/{repo}/releases/latest"
        data = fetch_json(url)
        if data and "tag_name" in data:
            tag = data["tag_name"]
            date = data.get("published_at", "")[:10]
            lines.append(f"- **{repo}**: `{tag}` ({date})")
        else:
            # Try tags if no releases
            url_tags = f"https://api.github.com/repos/{repo}/tags?per_page=1"
            tags = fetch_json(url_tags)
            if tags and len(tags) > 0:
                lines.append(f"- **{repo}**: `{tags[0]['name']}` (tag)")
            else:
                lines.append(f"- **{repo}**: no release info")

    lines.append("")
    lines.append("## Notes")
    lines.append("")
    lines.append("<!-- Add manual observations here -->")
    lines.append("")

    return "\n".join(lines)


def main():
    snapshot = generate_snapshot()

    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    now = datetime.utcnow()
    out_dir = os.path.join(repo_root, "knowledge", "tracking", "weekly")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{now.strftime('%Y-W%W')}.md")

    with open(out_path, "w") as f:
        f.write(snapshot)

    print(f"Snapshot written to {out_path}")


if __name__ == "__main__":
    main()
