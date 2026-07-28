# Bug Ledger

Tracks repeated mechanical errors across mock interviews to identify patterns.

| Date | Problem | Bug | Category | Fix | Retest |
|------|---------|-----|----------|-----|--------|
| 7/25 | LC 3 | `string.size` instead of `len(s)` | API recall | Python: `len()` | done |
| 7/25 | LC 3 | nested for loops instead of sliding window | loop structure | left pointer + while loop | done |
| 7/26 | LC 215 | `from collections import heapq` | API recall | `import heapq` (top-level module) | done |
| 7/26 | LC 215 | `heapq.heapop()` | API recall | `heapq.heappop()` (double p) | done |
| 7/27 | LC 994 | `for r in rows` (int not iterable) | syntax | `for r in range(rows)` | done (LC200) |
| 7/27 | LC 994 | `queue.top()` | API recall | `deque.popleft()` | done (LC200) |
| 7/27 | LC 994 | no bounds check before grid access | boundary | `0 <= r < rows and 0 <= c < cols` | done (LC200) |
| 7/27 | LC 994 | minute++ per element, not per level | loop structure | `for _ in range(len(queue))` | done (LC200) |
| 7/27 | LC 200 | bounds check AFTER grid access | boundary | bounds check must come BEFORE grid[r][c] | pending |
| 7/27 | LC 200 | `else: break` in direction loop | loop structure | don't break — check all 4 directions | pending |
| 7/27 | LC 215 drill | `heapq.heapappend` | API recall | `heapq.heappush` | done (drill2 clean) |
| 7/27 | LC 215 drill | `topk.top()` | API recall | `topk[0]` (index, no method) | done (drill2 clean) |
| 7/27 | LC 3 drill | 5 wrong attempts for `set.add()` | API recall | set: `.add()`, not `.append()`/`.push()` | pending |
| 7/27 | LC 3 drill | `seen.remove(s[right])` instead of `s[left]` | logic | shrink removes leftmost char, not the duplicate | pending |
| 7/27 | LC 15 drill | O(n³) brute force, no two pointers | pattern | sort + fix i + two pointers left/right | done (drill2) |
| 7/27 | LC 15 drill | broken duplicate skip with `while` in `for` loop | loop structure | `if i > 0 and nums[i]==nums[i-1]: continue` | done (drill2) |
| 7/27 | LC 15 drill2 | left/right increment outside `else` block | indentation | move inside `else` after dedup while loops | done |
| 7/27 | LC 209 | sorted array (subarray ≠ subset) | problem semantics | subarray = contiguous, cannot reorder | done (v2) |
| 7/27 | LC 209 | infinite loop (missing left increment) | loop structure | shrink while valid, move left | done (v2) |
| 7/27 | LC 209 | said O(n²) instead of O(n) | complexity | each element added/removed once → O(n) | done |

## Error frequency by category

| Category | Count | Examples |
|----------|-------|---------|
| API recall | 8 | `string.size`, wrong import, `heapop`, `queue.top()`, `heapappend`, `topk.top()`, `set.append/push` |
| Loop structure | 5 | nested loops, per-element BFS, `else: break`, broken dedup, missing left increment |
| Boundary | 2 | bounds check missing, bounds check after access |
| Problem semantics | 1 | subarray vs subset (LC 209) |
| Logic | 1 | removing wrong element in shrink |
| Indentation | 1 | left/right outside else |
| Complexity explanation | 1 | O(n²) vs O(n) for sliding window |
| Syntax | 1 | `rows` instead of `range(rows)` |

## Diagnosis (updated 7/27 evening)

**P0: Problem semantics + first-pass pattern fidelity.**
LC 209 showed that misreading "subarray" as "subset" leads to solving the wrong problem entirely. Before coding, always ask: Can I reorder? Must be contiguous? Positive/negative/mixed?

**Co-P0: Python API recall.**
8 of 20 bugs are wrong method names. `.top()` doesn't exist anywhere. Container API:
```
set:   add(), remove(), discard()
list:  append(), pop()
heapq: heappush(h, v), heappop(h), h[0]
deque: append(), popleft(), d[0]
```

**P1: Loop structure and invariant.**
5 bugs from wrong loop shape. Key patterns:
- Sliding window: `for right` expand, `while` shrink (remove `s[left]`, then `left += 1`)
- BFS: `for _ in range(len(queue))` for level-by-level
- 3Sum: dedup i with `continue`, dedup left/right with `while` inside `else`

**P1: Complexity explanation.**
Sort-dominated = O(n log n). Sliding window = O(n) (each element touched twice max). 3Sum = O(n²).
