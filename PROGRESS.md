# PROGRESS.md — weekly log

**Commitment:** 2 hrs/day, 7 days ≈ 14 hrs/week.
Pace assumption: ~45 min average per lesson + recall/quiz overhead ≈ **10-12 lessons/week**.
Updated at the end of each session. Reviewed at the start of each week.

---

## Week 1 · 2026-09-19 → 2026-09-25
**Target:** Phase 0 complete (all 12 lessons) — environment, git, GPU, APIs, notebooks, venvs, Docker, editor, data, shell, Linux, debugging.

| Lesson | Done | Quiz | Notes |
|---|---|---|---|
| P0-01 Dev Environment | ☑ | — | Fixed missing `python3` on Windows (PATH-level exe, not a shell alias). Preflight 2/2. |
| P0-02 Git & Collaboration | ☑ | — | Repointed origin to own repo, branched my-progress, committed + pushed. Workflow decision: my-progress = trunk, main = upstream mirror. |
| P0-03 GPU Setup & Cloud | ☑ | — | Colab T4 verified (15360MiB). Benchmark 13x speedup on 5000x5000. VRAM rule learned. |
| P0-04 APIs & Keys | ☐ | — | |
| P0-05 Jupyter Notebooks | ☐ | — | |
| P0-06 Python Environments | ☐ | — | |
| P0-07 Docker for AI | ☐ | — | |
| P0-08 Editor Setup | ☐ | — | |
| P0-09 Data Management | ☐ | — | |
| P0-10 Terminal & Shell | ☐ | — | |
| P0-11 Linux for AI | ☐ | — | |
| P0-12 Debugging & Profiling | ☐ | — | |

**Shaky this week:**
- No virtualenv yet - global Python. Resolve at P0-06.
- Token vs. cost confusion (baseline). Re-test at Phase 5.
- Embedding vs. vector DB confusion (baseline). Re-test at Phase 11.

**Next week's target:** Phase 1 lessons 01-10 (math re-derivation, slower pace)

---

## Baseline — pre-course concept check (2026-09-19)

Asked to define embedding / token / attention before any teaching.

| Term | Self-assessment | Verdict |
|---|---|---|
| Embedding | "words turned into vectors, called embeddings when stored in memory" | **Half right.** Vector part correct. "Stored in memory" is a confusion with vector databases — corrected in session 1. |
| Token | "numerical representation of the computing utilized by models to process prompts" | **Confused with billing.** Conflated the unit of text with the unit of cost. Corrected in session 1. |
| Attention | "not sure" | **Honest blank.** Best possible answer. Phase 7. |

Re-test these at end of Phase 5, and again at end of Phase 7.
