# Contributing to AGI简史

[中文](#贡献指南) | [English](#contributing-guide)

---

## 贡献指南

感谢你对本项目的兴趣！我们欢迎所有形式的贡献。

### 贡献方式

#### 📝 内容改进（最受欢迎）

- **修正错误**：事实错误、过时信息、错别字
- **补充内容**：为现有知识文章添加缺失的信息
- **新增文章**：在 `knowledge/techniques/` 下添加新的技术专题
- **改进书籍**：修正 LaTeX 书籍中的错误或补充章节内容

#### 🔧 技术改进

- **脚本优化**：改进 ArXiv 摘要、排行榜快照等自动化脚本
- **新增追踪**：添加新的数据源或追踪维度
- **CI/CD 改进**：优化 GitHub Actions 工作流

#### 🌐 翻译

- 帮助将知识文章翻译为英文
- 改进现有英文内容的质量

### 提交流程

1. **Fork** 本仓库
2. 创建你的分支：`git checkout -b feat/your-feature`
3. 提交改动：`git commit -m 'feat: add xxx'`
4. 推送到分支：`git push origin feat/your-feature`
5. 创建 **Pull Request**

### Commit 规范

我们使用 [Conventional Commits](https://www.conventionalcommits.org/)：

| 前缀 | 用途 | 示例 |
|------|------|------|
| `feat:` | 新内容或新功能 | `feat: add reinforcement learning techniques article` |
| `fix:` | 修正错误 | `fix: correct DeepSeek V3 parameter count` |
| `docs:` | 文档改进 | `docs: improve README navigation` |
| `chore:` | 维护性工作 | `chore: update submodules` |
| `refactor:` | 重构 | `refactor: reorganize knowledge directory structure` |

### 知识文章规范

新增知识文章请遵循以下格式：

```markdown
# Topic Name

> Last updated: YYYY-MM-DD

## Overview
Brief introduction to the topic.

## Key Concepts
Core technical concepts with explanations.

## Ecosystem
Major tools, frameworks, and projects.

## References
- Links to papers, repos, and resources
```

### LaTeX 书籍贡献

- 书籍源码在 `knowledge/techniques/*/` 目录下
- 每本书有独立的 `chapters/` 目录
- 使用 `xelatex` 编译，确保 TikZ 图表正常渲染
- 参考文献使用 BibLaTeX（`refs.bib`）
- 提交前请确保 PDF 可以正常编译

### 行为准则

请参阅 [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md)。

---

## Contributing Guide

Thank you for your interest in this project! We welcome contributions of all kinds.

### How to Contribute

#### 📝 Content Improvements (Most Wanted)

- **Fix errors**: Factual mistakes, outdated info, typos
- **Add content**: Fill gaps in existing knowledge articles
- **New articles**: Add technique articles under `knowledge/techniques/`
- **Improve books**: Fix errors or add content to LaTeX books

#### 🔧 Technical Improvements

- **Script optimization**: Improve automation scripts
- **New tracking**: Add new data sources or tracking dimensions
- **CI/CD improvements**: Optimize GitHub Actions workflows

#### 🌐 Translation

- Help translate knowledge articles to/from English and Chinese

### Submission Process

1. **Fork** this repository
2. Create your branch: `git checkout -b feat/your-feature`
3. Commit changes: `git commit -m 'feat: add xxx'`
4. Push to branch: `git push origin feat/your-feature`
5. Open a **Pull Request**

### Commit Convention

We use [Conventional Commits](https://www.conventionalcommits.org/):

| Prefix | Purpose | Example |
|--------|---------|---------|
| `feat:` | New content or feature | `feat: add reinforcement learning article` |
| `fix:` | Fix errors | `fix: correct DeepSeek V3 parameter count` |
| `docs:` | Documentation | `docs: improve README navigation` |
| `chore:` | Maintenance | `chore: update submodules` |
| `refactor:` | Restructuring | `refactor: reorganize knowledge directory` |

### Code of Conduct

Please read our [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md).
