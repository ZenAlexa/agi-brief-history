# Embodied AI / Humanoid Robots

> Last updated: 2026-03-27

## Core Contradiction

**Capital demands a 2-year commercialization timeline for technology that realistically needs 10+ years of hardware-software co-evolution.** The result: companies optimize for fundraising narratives over engineering milestones, and the gap between demo capabilities and production reliability remains vast.

- 150+ companies in China alone, 330+ humanoid models released in 2025
- >95% of humanoid robot revenue comes from entertainment, education, and exhibitions — not productivity replacement
- UBS analyst: "No humanoid robot company has truly passed the proof-of-concept stage"
- Musk (Q4 2025 earnings): "No Optimus robots are doing useful work — they are for learning and data collection only"

## The Money: Where It Comes From, Where It Goes

### Global Funding Trajectory

| Year | Humanoid Robot Funding | YoY Growth |
|------|----------------------|------------|
| 2023 | ~$277M | — |
| 2024 | ~$1.05B | ~280% |
| 2025 | ~$2.65B (humanoid only) | +152% |
| 2026 Q1 | $5.8B+ YTD globally; China alone >200亿元 | Accelerating |

### Who Is Investing

| Type | Key Players | Strategy |
|------|------------|---------|
| Tech giants | NVIDIA, Microsoft, Google, OpenAI, Amazon, Tencent, Meituan | Cross-stake multiple companies |
| Mega VCs | SoftBank ($1.4B into Skild alone), Sequoia, a]16z | Global bets |
| Sovereign wealth | Qatar Investment Authority, Saudi Aramco/Prosperity7 | Middle East deep in |
| China national funds | 国家大基金三期, 中国移动链长基金, 国信投资 | State-backed national champions |
| Industrials | Mercedes-Benz, BMW, BYD, CATL, John Deere, Bosch | Use-case-driven |

### Top Funded Companies

| Company | Total Raised | Latest Valuation | Revenue (2025 est.) | Profitable? |
|---------|-------------|-----------------|--------------------|----|
| **Figure AI** (US) | >$2.6B | **$39.5B** | ~$0 (zero recurring) | No |
| **Skild AI** (US) | >$2B | $14B | N/A (foundation model) | No |
| **Apptronik** (US) | $935M | $5B | Pre-revenue | No |
| **Physical Intelligence** (US) | >$1B | $5.6B | $0 (no product) | No |
| **Unitree** (CN) | >15亿元 | 420亿元 (IPO) | **17亿元** | **Yes** (6亿 net) |
| **Galbot** (CN) | >60亿元 | >300亿元 | Undisclosed (est. tens of millions) | No |
| **Agibot** (CN) | 11 rounds | ~150亿元 | ~10亿元 | No |
| **UBTECH** (CN) | Public (HK:9880) | ~500亿 HKD | ~12亿元 | No (cumulative loss ~30亿) |
| **Fourier** (CN) | ~8亿元 | ~80亿元 | Undisclosed | No |

**Where the money goes** (Unitree IPO breakdown): 48% on AI foundation models (GPU compute), 26% on hardware R&D, 15% on manufacturing base, 11% on new products.

### The Investment Chain

```
Government policy ("未来产业") → National funds (大基金三期) → Signal to VCs
    → VCs compete on valuation → Companies raise at 100x+ P/S
        → Spend on: GPU compute (48%) + hardware R&D (26%) + factory (15%)
            → Revenue mostly from: education/research (74%) + entertainment (17%)
                → Industrial productivity replacement: <9% of revenue
                    → Fundraise again to survive → Repeat
```

## Technology Supply Bottlenecks

### Why Hardware Cannot Match Software Hype

| Bottleneck | Severity | Reality |
|-----------|----------|---------|
| **Actuators** | CRITICAL | 51% of BOM. Harmonic drives $2K-5K/unit, 10-40 needed per robot. Japan controls ~70% of global supply. |
| **Data for foundation models** | CRITICAL | "5-6 orders of magnitude short" of needed training data. Teleoperation: $50-500/hr. |
| **Dexterous manipulation** | HIGH | Human hand has ~17,000 tactile sensors. Current robot hands: nowhere close. Cannot learn tactile skills from video. |
| **Sim-to-real gap** | HIGH | Locomotion: largely solved. Rigid manipulation: improving. Deformable objects, contact-rich tasks: fundamentally limited. |
| **Tactile sensors** | MEDIUM | Early commercial (GelSight, XELA), but fragile, expensive, hard to integrate at fingertip scale. |
| **Battery life** | MEDIUM | 2-4 hours continuous work vs. human 8-12 hour shifts. ~5-8%/yr energy density improvement — physics, not software. |
| **Vision/compute** | LOW | Solved. Commodity hardware from automotive/smartphone supply chain. |

### Hardware Iteration Cycle

- Traditional: **18-24 months** concept-to-prototype
- Simulation-accelerated: **7-10 months** (NVIDIA Isaac Sim pipeline)
- But physical qualification (machining, testing): irreducibly **6-12 months** per generation
- Software updates: weekly. **Hardware updates: semi-annually at best.**

### Foundation Model Status

| Model | Developer | Capability | Limitation |
|-------|-----------|-----------|------------|
| GR00T N2 | NVIDIA | Cross-task generalization, sim-trained | Requires fine-tuning per hardware |
| π0 / π0.5 | Physical Intelligence | "Generalist policy", laundry folding | Manipulation only, short-horizon |
| RT-2 / RT-X | Google DeepMind | Pioneered VLA paradigm | Superseded, limited |
| Octo | UC Berkeley | Cross-robot generalization | Limited task complexity |

**No model can handle truly open-ended tasks in unstructured environments.** Long-horizon planning, error recovery, and cross-embodiment transfer remain fragile.

## Bubble Signals

| Signal | Evidence |
|--------|---------|
| Valuation-revenue disconnect | Figure AI: $39.5B / $0 revenue. Galbot: 300亿元 / tens of millions revenue. Industry average: 60% of companies valued >100x revenue. |
| Overcapacity | Unitree alone plans 75K humanoid/yr capacity — exceeds IDC's 2030 China demand forecast of 60K total. |
| Speed of fundraising | 智平方 (X Square): 12 rounds in 1 year. Manifold AI: 2亿元 Pre-A at 10 months old. |
| Related-party transactions | 《财经》 reports many 2026 orders are 关联交易, not arm's-length commercial deals. |
| Policy-driven FOMO | Every tier-1/2 Chinese city racing to build robotics parks with 100亿+ funds. |
| NDRC warning | Nov 2025: explicit bubble risk warning — 150+ companies, severe homogeneity. |
| Analyst forecast divergence | $18B (MarketsandMarkets 2030) vs. $24T (ARK 2050) — **1,000x spread** = nobody knows. |

## Historical Parallel: Autonomous Driving

| Dimension | Autonomous Driving (2016-2024) | Humanoid Robots (2024-2026) |
|-----------|-------------------------------|----------------------------|
| Total invested | >$100B | >$18B (and accelerating) |
| Core promise | "Full autonomy by 2020" | "Million units by 2027" |
| Actual timeline | 8+ years delayed, still limited | TBD |
| Survivors | Waymo (Google), cruise through GM collapse | TBD |
| Pattern | Real tech progress + real demand + massive overpromise → most companies die, 5-10 year delay |

## Realistic Timeline

| Phase | Timeline | What Happens |
|-------|----------|-------------|
| Structured industrial (NOW) | 2025-2027 | Repetitive tasks in factories/warehouses. 10Ks of units. $50K-150K/unit. |
| Expanded industrial + limited service | 2028-2030 | Broader task repertoire in controlled environments. 100Ks of units. Price must hit $20-30K. |
| Consumer / general-purpose | 2032-2035+ | Requires 10x improvement in manipulation, foundation models, and actuator cost. $10-20K target. |

## Key Voices

- **Rodney Brooks** (iRobot co-founder, MIT): "Humanoid robot bubble is destined to burst. Video-based learning cannot teach dexterity — you can't learn touch from watching."
- **朱啸虎** (GSR Ventures): Publicly exited humanoid robot positions in 2025, questioned "imaginary customers."
- **Gartner**: By 2028, fewer than 20 companies will actually deploy humanoids in supply chain/manufacturing.
- **NDRC** (Nov 2025): First-ever official risk warning for the sector — "prevent products piling up with high redundancy."
- **Unitree CEO 王兴兴**: "The GPT moment for embodied AI is still 2-3 years away."

## References

- Goldman Sachs, "Humanoid Robot Outlook" (revised 2024): $38B by 2035
- Morgan Stanley, "The Humanoid 100" (Feb 2025): $5T by 2050
- Forrester, "The State of Humanoid Robots, 2026" (March 2026)
- Aljalbout et al., "The Reality Gap in Robotics", Annual Review of Control, Robotics, and Autonomous Systems (2026)
- Physical Intelligence, π0 Technical Report (Oct 2024)
- NVIDIA GTC 2026: GR00T N2, Isaac Sim, Jetson Thor announcements
- Unitree IPO Prospectus (March 2026, 科创板)
- 《财经》, China's humanoid robot boom reality check (March 2026)
- 开源证券, 具身智能融资分析 (2025)
- NDRC 李超, 具身智能行业风险提示 (Nov 27, 2025)
- Brooks, R., "Why Today's Humanoids Won't Learn Dexterity" (Sep 2025)
- Lepora, N., "Tactile Robotics: Past and Future", IJRR (Feb 2026)
