# Chinese Name Verification Results

Generated: 2026-03-20
Scope: All chapter files (`chapters/ch*.tex`) in the LLM Training Landscape book.

## Verified Name Table

| English Name | Chinese in Chapters | Correct Chinese | Affiliation | Verified Source | Status |
|---|---|---|---|---|---|
| Liang Wenfeng | 梁文锋 | 梁文锋 | DeepSeek founder / CEO | Baidu Baike, AP News | ✅ Correct |
| Shunyu Yao | 姚顺雨 | 姚顺雨 | OpenAI researcher (fmr. Princeton); Tencent Chief AI Scientist Dec 2025 | ysymyth.github.io title "About – Shunyu Yao – 姚顺雨" | ✅ Correct |
| Junyang Lin | 林俊阳 | **林俊旸** | Alibaba Qwen tech lead (departed Mar 3 2026) | Baidu Baike "林俊旸"; TechCrunch; Yahoo Finance | ❌ Wrong character in chapter |
| Yu Bowen | 余博文 | **郁博文** | Alibaba Qwen post-training lead (departed Mar 3 2026; joined ByteDance Seed Mar 12 2026) | ChinaNews.ai "Yu Bowen (郁博文)"; Wallstreet CN 郁博文; NetEase 163.com | ❌ Wrong character in chapter |
| Liu Zhiping (Martin Lau) | 刘炽平 | 刘炽平 | Tencent President | Baidu Baike; Wikipedia zh; Tencent official profile | ✅ Correct |

## Names NOT Found in Chapters (from priority list)

The following names from the verification priority list were searched but do NOT appear in any chapter file:

| Name | Notes |
|---|---|
| Jensen Huang (黄仁勋) | No mention in any ch*.tex file |
| Yang Zhilin (杨植麟) | Moonshot AI founder not referenced |
| Tang Jie (唐杰) | Zhipu AI not referenced by name |
| Kai-Fu Lee (李开复) | 01.AI not referenced |
| Han Song (韩松) | MIT model compression not attributed by name |
| Jia Yangqing (贾扬清) | Lepton AI / Caffe not mentioned |

## Corrections Needed

### 1. 林俊旸 — Wrong character in ch12-team.tex

- **File:** `chapters/ch12-team.tex`
- **Line:** 1096
- **Current:** `通义实验室大模型技术负责人林俊阳也已离职`
- **Correct:** `通义实验室大模型技术负责人林俊旸也已离职`
- **Explanation:** The correct character is 旸 (yang, "rising sun"), not 阳 (yang, "positive/sun"). Both are homophones but different characters. Baidu Baike has a dedicated entry at /item/林俊旸/67148281. The AlphaMatch.ai Traditional Chinese article writes 林俊揚, which Simplified maps to 林俊旸 — same person. All major English-language sources (TechCrunch, Yahoo Finance, China Daily) use the romanization "Lin Junyang" but do not specify the character; the Baidu Baike entry definitively resolves this.

### 2. 郁博文 — Wrong character in ch12-team.tex

- **File:** `chapters/ch12-team.tex`
- **Line:** 1093
- **Current:** `Qwen 大模型后训练负责人\textbf{余博文}`
- **Correct:** `Qwen 大模型后训练负责人\textbf{郁博文}`
- **Explanation:** The surname is 郁 (yu4), not 余 (yu2). Multiple authoritative Chinese-language sources consistently write 郁博文: ChinaNews.ai provides the parenthetical "(郁博文)" alongside the English "Yu Bowen"; the Wallstreet CN (华尔街见闻) report, NetEase 163.com, and Futunn all use 郁博文. The chapter incorrectly uses the more common surname 余.

## Notes on Name Consistency

- **梁文锋 / Liang Wenfeng:** Appears in ch01, ch02, ch07, ch10, ch12, ch15. Chinese characters are always 梁文锋 — correct throughout. Note: ch10-test-time.tex uses "(Liang Wenfeng)" while ch12-team.tex uses "(Wenfeng Liang)" — both romanizations are acceptable (Chinese vs. Western name order convention).
- **姚顺雨 / Shunyu Yao:** Appears only in ch12-team.tex. Characters confirmed correct. The task brief suggested possible misspelling 姚顺宇 — that character combination does NOT appear anywhere in the chapters; the chapter correctly uses 姚顺雨.

## Verification Sources

- Shunyu Yao personal website: https://ysymyth.github.io/
- Liang Wenfeng Baidu Baike (EN): https://baike.baidu.com/en/item/Liang%20Wenfeng/943430
- Lin Junyang (林俊旸) Baidu Baike: https://baike.baidu.com/item/%E6%9E%97%E4%BF%8A%E6%97%B8/67148281
- Yu Bowen (郁博文) ChinaNews.ai: https://chinanews.ai/story/ifeng_8rQgMCfEnsF/
- Yu Bowen (郁博文) Futunn/Wallstreet CN: https://news.futunn.com/en/post/69960206/
- Liu Zhiping (刘炽平) Baidu Baike: https://baike.baidu.com/item/%E5%88%98%E7%82%BD%E5%B9%B3/5577473
- Junyang Lin LinkedIn: https://linkedin.com/in/junyang-lin-0b2b38151
- TechCrunch on Qwen departures: https://techcrunch.com/2026/03/03/alibabas-qwen-tech-lead-steps-down-after-major-ai-push/
