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
| Environment | Windows 11, Python 3.13.4, `python3` fixed at C:\Python313\python3.exe, Git 2.43, no venv yet |

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
- **Next lesson:** Phase 0 / 03 GPU Setup & Cloud
- **Completed:** 2 / 523

## Lesson log

| Date | Phase | Lesson | Quiz | Status |
|---|---|---|---|---|
| 2026-09-20 | 0 | 02 Git & Collaboration | — | Done. Fork/remote repoint, branch, commit, push. Grasped branch=pointer; shaky on diff/reachability. |
| 2026-09-20 | 0 | 01 Dev Environment | — | Done. Debugged missing `python3.exe`; correctly rejected shell-alias fix. Predicted preflight result accurately. |

## Review queue

_(concepts that were shaky — revisited at the start of the next session)_

- Virtualenvs - still on global Python (due P0-06)
- **Diagnosis precision**: read "no such file on PATH" vs "wrong program ran" as different causes. Assumed a version conflict where none existed. Re-test in any Phase 0-2 debugging.
- **library vs executable**: library = imported inside Python; executable = run by the shell. Used interchangeably.
- **shell-level vs system-level fixes**: a shell alias is private to one shell; a file on PATH is visible to the OS and every subprocess.
- **Commit message discipline**: writing date/lesson codes (`P0_L2_200926`) instead of what+why. Re-check at end of week 1.
- **Branch deletion / reachability**: deleting a branch deletes a label, not commits; commits are lost only when nothing can reach them. Diffs work on SHAs, no branch name needed.
- Token = unit of text, not unit of cost (Phase 5)
- Embedding is the vector itself, not the storage (Phase 11)
