# 003 - Update Frequency and Automation

**Status**: Accepted
**Date**: 2026-03-06
**Context**: The field moves at daily pace. Need automated tracking that doesn't miss important developments but remains manageable.

**Decision**:

| Schedule | Cron (UTC) | Action |
|----------|-----------|--------|
| Daily | `17 3 * * *` (03:17) | ArXiv paper digest — cs.CL, cs.AI, cs.LG |
| Mon/Wed/Fri | `43 14 * * 1,3,5` (14:43) | Submodule update check + leaderboard snapshot |
| Weekly | `23 6 * * 1` (06:23 Mon) | Comprehensive weekly digest combining all signals |

All cron times use non-round minutes to avoid GitHub Actions congestion.

**Paper pipeline**: Daily automated ArXiv parsing. Consider 24hr cloud service if openclaw integration proves valuable.

**Consequences**:
- Daily paper coverage ensures no major publication is missed
- 3x/week infra updates catch new releases within 48 hours
- Weekly digest provides human-reviewable summary
- Non-round cron times reduce CI queue delays
