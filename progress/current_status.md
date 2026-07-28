# Current Status — July 27, 2026 (evening update)

Interview: Thursday July 30. Two 45-min coding rounds.

## Strong
- Pattern recognition: correctly identifies which pattern to use
- Brute force → optimized reasoning flow
- Delayed rewrites show significant improvement (LC 215: 6→10, LC 15: 4→7)
- Intervals pattern is clean (9/10 first attempt)
- Behavioral and domain rounds (self-assessed 8-9/10)

## Current bottleneck (updated)

**P0: Problem semantics + first-pass pattern fidelity**
- LC 209: misread "subarray" as "subset", solved wrong problem
- Under pressure, may invoke adjacent-but-wrong pattern (e.g., prefix sum for 3Sum)
- Must ask before coding: contiguous? ordered? positive/negative? duplicates?

**Co-P0: Python API recall**
- Keeps inventing methods that don't exist: `.top()`, `.heapappend()`, `.push()`
- 5 wrong attempts to call `set.add()` in one session
- Container API must be automatic

**P1: Loop structure and invariant**
- Sliding window `while` shrink (remove s[left], then left += 1)
- BFS level loop: `for _ in range(len(queue))`
- 3Sum dedup: `continue` for i, `while` for left/right inside `else`

**P1: Complexity explanation**
- Sort-dominated = O(n log n), not O(n)
- Sliding window = O(n), not O(n²)
- 3Sum = O(n²)

## Core Pattern Coverage

| # | Pattern | Drilled | Mock tested | Delayed rewrite | Confidence |
|---|---------|---------|-------------|-----------------|------------|
| 1 | HashMap / Prefix Sum | yes | - | - | high |
| 2 | Sliding Window | yes | Mock 02 (7/10), drill (5/10) | pending | medium |
| 3 | BFS / DFS | yes | Mock 04 (7/10), LC200 (8/10) | pending | medium |
| 4 | Intervals | yes | drill (9/10) | - | high |
| 5 | Heap / Top-K | yes | Mock 03 (9/10), drill (6→10/10) | done ✓ | high |
| 6 | Two Pointers | yes | drill (4→7/10) | done ✓ | medium |

## All scores (chronological)

| Date | Problem | Pattern | Score | Notes |
|------|---------|---------|-------|-------|
| 7/25 | LC 3 mock | Sliding Window | 7/10 | |
| 7/26 | LC 215 mock | Heap | 9/10 | |
| 7/27 | LC 994 mock | BFS | 7/10 | |
| 7/27 | LC 200 drill | DFS | 8/10 | |
| 7/27 | LC 215 drill 1 | Heap | 6/10 | regressed — API bugs |
| 7/27 | LC 3 drill | Sliding Window | 5/10 | regressed — set.add() |
| 7/27 | LC 56 drill | Intervals | 9/10 | cleanest of the day |
| 7/27 | LC 15 drill 1 | Two Pointers | 4/10 | O(n³), no two pointers |
| 7/27 | LC 15 drill 2 | Two Pointers | 7/10 | delayed rewrite ↑ |
| 7/27 | LC 215 drill 2 | Heap | 10/10 | delayed rewrite ↑ |
| 7/27 | LC 209 mini mock | Sliding Window | 6/10 | subarray vs subset |

## Plan: Tue 7/28

**Warm-up (20 min, no notes)**
- 3 skeleton templates: sliding window, BFS level, 3Sum
- Write container API from memory

**Round 1 (45 min)** — unknown problem, full interview flow
**15 min break**
**Round 2 (45 min)** — different pattern, unknown problem
**Debrief (30 min)** — score, update bug ledger, fix one worst issue

## Plan: Wed 7/29
- If both rounds ≥7: light taper, pattern cards only
- If any round <7: 30 min fix on that one issue, then stop

## Plan: Thu 7/30 — Interview
- 15-20 min warm-up: 2 templates from memory, then stop
