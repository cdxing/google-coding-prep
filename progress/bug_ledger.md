# Bug Ledger

Tracks repeated mechanical errors across mock interviews to identify patterns.

| Date | Problem | Bug | Category | Fix | Retest |
|------|---------|-----|----------|-----|--------|
| 7/25 | LC 3 | `string.size` instead of `len(s)` | API recall | Python: `len()` | done (rewrote) |
| 7/25 | LC 3 | nested for loops instead of sliding window | loop structure | left pointer + while loop | done (rewrote) |
| 7/26 | LC 215 | `from collections import heapq` | API recall | `import heapq` (top-level module) | done |
| 7/26 | LC 215 | `heapq.heapop()` | API recall | `heapq.heappop()` (double p) | done |
| 7/27 | LC 994 | `for r in rows` (int not iterable) | syntax | `for r in range(rows)` | pending |
| 7/27 | LC 994 | `queue.top()` | API recall | `deque.popleft()` | pending |
| 7/27 | LC 994 | no bounds check before grid access | boundary | `0 <= r < rows and 0 <= c < cols` | pending |
| 7/27 | LC 994 | minute++ per element, not per level | loop structure | `for _ in range(len(queue))` | pending |

## Error frequency by category

| Category | Count | Examples |
|----------|-------|---------|
| API recall | 4 | `string.size`, wrong `heapq` import, `heapop`, `queue.top()` |
| Loop structure | 2 | nested loops instead of sliding window, per-element instead of per-level BFS |
| Boundary | 1 | missing bounds check on grid access |
| Syntax | 1 | `rows` instead of `range(rows)` |

## Diagnosis
**Primary gap: Python API fluency.** 4 of 8 bugs are wrong function/method names or import paths. This is mechanical, not conceptual. Fix: write templates from memory repeatedly until API calls are automatic.

**Secondary gap: BFS level-by-level loop.** The `for _ in range(len(queue))` pattern must become reflexive.
