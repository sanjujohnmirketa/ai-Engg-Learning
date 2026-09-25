# LEARNING.md — Sanju's study plan

**Started:** 2026-09-19
**Tutor contract:** see CLAUDE.md (teach, don't do)

## Profile

| | |
|---|---|
| Language | Python (primary, all 523 lessons) |
| Python level | Beginner — loops, ifs, functions, lists solid; classes/generators/numpy need explaining |
| Math level | Rusty — saw linear algebra & calculus years ago, needs re-derivation not review |
| LLM internals | Vocabulary yes, mechanics no |
| Environment | Windows 11, Python 3.13.4, `python3` fixed at C:\Python313\python3.exe, Git 2.43, no venv yet, no PyTorch |
| GPU | AMD Vega 8 integrated, no CUDA, no ROCm support. Ryzen 5 3500U, 9.9GB RAM. Cloud/Colab for Phase 10+. Buy decision deferred to Phase 10. |
| Repo | origin = github.com/sanjujohnmirketa/ai-Engg-Learning. Trunk = `my-progress` (also GitHub default). `main` = upstream mirror, never commit. |

## Route

Phase 0 (12) → Phase 1 (22) → Phase 2 (18) → Phase 3 (13) → Phase 5 (29)
→ Phase 7 (16) → Phase 10 (24) → Phase 11 (17) → Phase 13 (31) → Phase 14 (54)

Target: build a real LLM and real agents from first principles.
Branches (Vision P4, Speech P6, RL P9, GenAI P8) deferred — revisit after Phase 10.
Phase 9 (RL, 12 lessons) inserted before Phase 10 only if RLHF lessons demand it.

**Deliberate detour:** Python fundamentals get taught *inside* Phase 0 and Phase 1
lessons rather than as a separate course. Every new idiom explained at first use.

## Current position

- **Phase:** 0 — Setup & Tooling
- **Next lesson:** Phase 0 / 04 APIs & Keys
- **Completed:** 3 / 523

## Lesson log

| Date | Phase | Lesson | Quiz | Status |
|---|---|---|---|---|
| 2026-09-21 | 0 | 03 GPU Setup & Cloud | — | Done. Colab T4, 13x benchmark. Strong: asked why questions mattered. Gap: CUDA context/caching allocator was new. |
| 2026-09-20 | 0 | 02 Git & Collaboration | — | Done. Fork/remote repoint, branch, commit, push. Grasped branch=pointer; shaky on diff/reachability. |
| 2026-09-20 | 0 | 01 Dev Environment | — | Done. Debugged missing `python3.exe`; correctly rejected shell-alias fix. Predicted preflight result accurately. |

## Tutor notes

- **2026-09-22:** Graded a volunteered aside as a wrong answer and called it a pattern
  ("third slip"). Learner correctly pushed back: the question asked only for 3B x 2 bytes.
  Retracted. RULE: grade the answer to the question asked. If extra context is offered,
  treat it as thinking-aloud, not as a claim under test. State question scope precisely.

- **2026-09-21:** Learner flagged that P0-03 assumed GPU/ML vocabulary (tensor, kernel,
  cuBLAS, quantization, gradients, activations, optimizer state). Self-reported ~10-20%
  comprehension on the VRAM/memory section. Re-taught from scratch. Enforcement rule
  added to CLAUDE.md. Check comprehension explicitly on dense material.

## Review queue

_(concepts that were shaky — revisited at the start of the next session)_

- Virtualenvs - still on global Python (due P0-06)
- **Diagnosis precision**: read "no such file on PATH" vs "wrong program ran" as different causes. Assumed a version conflict where none existed. Re-test in any Phase 0-2 debugging.
- **library vs executable**: library = imported inside Python; executable = run by the shell. Used interchangeably.
- **shell-level vs system-level fixes**: a shell alias is private to one shell; a file on PATH is visible to the OS and every subprocess.
- **Commit message discipline**: writing date/lesson codes (`P0_L2_200926`) instead of what+why. Re-check at end of week 1.
- **Branch deletion / reachability**: deleting a branch deletes a label, not commits; commits are lost only when nothing can reach them. Diffs work on SHAs, no branch name needed. [CONFIRMED - answered correctly from .git/refs inspection]
- **Reflog**: local journal of every HEAD position, survives branch deletion, ~30-90 day expiry, never pushed. Recovery = find SHA, point a new ref at it.
- **Arithmetic slips (x2)**: 5000x5000 read as 50M (is 25M); 10GB/2bytes read as 500M (is 5B).
  Both order-of-magnitude, both inside posed questions. FIX: write the arithmetic down.
  [RETRACTED a third: the 15.4-3-6 remark was volunteered context outside the question asked,
  graded unfairly. Tutor error, not learner error.]
- **Precision matters for memory math**: torch.randn defaults to fp32 (4 bytes), not fp16 (2 bytes). Always confirm dtype before sizing.
- **Training vs inference memory**: inference ~= weights. Training = weights + gradients + optimizer state (Adam: 2x) + activations, roughly 4x or more. Revisit at P1-08 (optimization) and P3 (backprop).
- **VRAM re-teach PASSED (2026-09-22)**: after re-teaching from scratch, correctly computed
  3B fp16 = 6GB and correctly applied the 4x training rule to conclude training fails on a T4.
  Comprehension went ~15% -> solid. Re-teach approach (define every term, one idea, three steps) worked.
- **VOCABULARY DEBT (re-taught 2026-09-21)**: tensor, kernel, cuBLAS, quantization,
  gradients, activations, optimizer state, fp16/fp32, caching allocator. All introduced
  at P0-03 without definition. Re-test understanding at P1-12 (tensor ops) and P3.
- **VRAM rule**: fp16 = 2 bytes/param. T4 reports 15360MiB; minus ~3GB real overhead = ~12.3GB usable = ~6.1B params. So a 7B fp16 model does NOT fit a T4 -> hence quantization. Why 7B is a standard size. Trust reported figures over spec sheets.
- **GPU speedup scales with problem size**: 5000x5000 gave only 13x because fixed overheads (kernel launch, sync) dominate a small job. Bigger jobs -> bigger ratios.
- **CUDA context + caching allocator**: MEASURED on T4 = 3005MiB held for only 300MB of tensors (10x). Overhead = CUDA context + cuBLAS workspace + allocator chunks. nvidia-smi shows RESERVED memory, not tensor usage. Use torch.cuda.memory_allocated() vs memory_reserved(). Source of phantom "memory leak" confusion.
- **GPU-Util vs memory are independent columns**: full memory + idle util usually = data loading bottleneck (Phase 17 skill).
- **PyTorch installs without CUDA**: CPU-only build works fine; no GPU needed to use torch. Misconception corrected at P0-03.
- **Protective refusals**: git/GitHub refuse operations that would create an invalid state (unmerged branch, current branch, remote default branch). Read the refusal as a diagnosis naming the invariant.
- Token = unit of text, not unit of cost (Phase 5)
- Embedding is the vector itself, not the storage (Phase 11)
