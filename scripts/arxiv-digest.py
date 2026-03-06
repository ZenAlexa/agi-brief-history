#!/usr/bin/env python3
"""
Daily ArXiv digest for LLM-related papers.
Fetches recent papers from cs.CL, cs.AI, cs.LG and generates a markdown summary.
"""

import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta
import re
import os

CATEGORIES = ["cs.CL", "cs.AI", "cs.LG"]
ARXIV_API = "http://export.arxiv.org/api/query"
MAX_RESULTS_PER_CAT = 50

# Keywords that signal LLM relevance
LLM_KEYWORDS = [
    "language model", "llm", "transformer", "attention",
    "fine-tun", "rlhf", "dpo", "grpo", "reinforcement learning from human",
    "mixture of experts", "moe", "quantiz", "inference",
    "pretraining", "pre-training", "post-training",
    "instruction", "alignment", "chat", "reasoning",
    "chain of thought", "test-time", "speculative decod",
    "tokeniz", "scaling law", "distillat", "multimodal",
    "vision-language", "long context", "retrieval augmented",
    "deepseek", "qwen", "llama", "gemma", "mistral", "olmo",
]


def fetch_papers(category: str) -> list[dict]:
    """Fetch recent papers from ArXiv API for a given category."""
    query = f"cat:{category}"
    url = f"{ARXIV_API}?search_query={query}&sortBy=submittedDate&sortOrder=descending&max_results={MAX_RESULTS_PER_CAT}"

    req = urllib.request.Request(url)
    req.add_header("User-Agent", "llm-observatory/1.0 (daily digest)")

    with urllib.request.urlopen(req, timeout=30) as resp:
        data = resp.read()

    root = ET.fromstring(data)
    ns = {"atom": "http://www.w3.org/2005/Atom", "arxiv": "http://arxiv.org/schemas/atom"}

    papers = []
    for entry in root.findall("atom:entry", ns):
        title = entry.find("atom:title", ns).text.strip().replace("\n", " ")
        summary = entry.find("atom:summary", ns).text.strip().replace("\n", " ")
        arxiv_id = entry.find("atom:id", ns).text.strip().split("/")[-1]
        published = entry.find("atom:published", ns).text.strip()[:10]

        categories = [c.get("term") for c in entry.findall("atom:category", ns)]
        authors = [a.find("atom:name", ns).text for a in entry.findall("atom:author", ns)]

        papers.append({
            "id": arxiv_id,
            "title": title,
            "summary": summary[:300],
            "published": published,
            "categories": categories,
            "authors": authors[:5],
            "url": f"https://arxiv.org/abs/{arxiv_id}",
        })

    return papers


def is_llm_relevant(paper: dict) -> bool:
    """Check if paper is relevant to LLM research."""
    text = (paper["title"] + " " + paper["summary"]).lower()
    return any(kw in text for kw in LLM_KEYWORDS)


def generate_digest(all_papers: list[dict]) -> str:
    """Generate markdown digest from papers."""
    today = datetime.utcnow().strftime("%Y-%m-%d")
    lines = [
        f"# ArXiv Daily Digest — {today}",
        "",
        f"> Auto-generated at {datetime.utcnow().strftime('%Y-%m-%d %H:%M UTC')}",
        f"> Sources: {', '.join(CATEGORIES)}",
        f"> Total fetched: {len(all_papers)} | LLM-relevant: shown below",
        "",
    ]

    relevant = [p for p in all_papers if is_llm_relevant(p)]
    # Deduplicate by arxiv ID
    seen = set()
    unique = []
    for p in relevant:
        if p["id"] not in seen:
            seen.add(p["id"])
            unique.append(p)

    if not unique:
        lines.append("No LLM-relevant papers found today.")
        return "\n".join(lines)

    lines.append(f"## Papers ({len(unique)})")
    lines.append("")

    for i, p in enumerate(unique, 1):
        authors_str = ", ".join(p["authors"])
        if len(p["authors"]) == 5:
            authors_str += " et al."
        lines.append(f"### {i}. {p['title']}")
        lines.append(f"- **ID**: [{p['id']}]({p['url']})")
        lines.append(f"- **Authors**: {authors_str}")
        lines.append(f"- **Categories**: {', '.join(p['categories'])}")
        lines.append(f"- **Summary**: {p['summary']}...")
        lines.append("")

    return "\n".join(lines)


def main():
    all_papers = []
    for cat in CATEGORIES:
        try:
            papers = fetch_papers(cat)
            all_papers.extend(papers)
            print(f"Fetched {len(papers)} papers from {cat}")
        except Exception as e:
            print(f"Error fetching {cat}: {e}")

    digest = generate_digest(all_papers)

    # Determine output path
    repo_root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    today = datetime.utcnow().strftime("%Y-%m-%d")
    out_dir = os.path.join(repo_root, "knowledge", "tracking", "arxiv")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"{today}.md")

    with open(out_path, "w") as f:
        f.write(digest)

    print(f"Digest written to {out_path}")


if __name__ == "__main__":
    main()
