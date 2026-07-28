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
| 7/28 | LC 253 | typos `invervals`/`inverval` | syntax | spell check variable names | done |
| 7/28 | LC 133 | `dfs(nd.neighbors)` — passed list not node | data type | loop over neighbors, call `dfs(neighbor)` | pending |
| 7/28 | LC 133 | `visited[nd] = nd_clone` after recursion | ordering | register in visited BEFORE recursing (cycle-break) | pending |
| 7/28 | LC 133 | missing `return nd_clone` | control flow | every branch of recursive function must return | pending |
| 7/28 | LC 133 | redundant outer clone + inner dfs clone | problem structure | DFS function IS the entry point, no outer clone needed | pending |
| 7/28 | LC 133 | said O(n) instead of O(V+E) | complexity | graph traversal = O(V+E), not O(n) | pending |

## Error frequency by category

| Category | Count | Examples |
|----------|-------|---------|
| API recall | 8 | `string.size`, wrong import, `heapop`, `queue.top()`, `heapappend`, `topk.top()`, `set.append/push` |
| Loop structure | 5 | nested loops, per-element BFS, `else: break`, broken dedup, missing left increment |
| Problem structure | 1 | redundant outer clone vs inner DFS (LC 133) |
| Data type | 1 | passed list instead of node to DFS (LC 133) |
| Ordering | 1 | visited assignment after recursion — infinite loop (LC 133) |
| Control flow | 1 | missing return in recursive branch (LC 133) |
| Boundary | 2 | bounds check missing, bounds check after access |
| Complexity explanation | 2 | O(n²) vs O(n) sliding window, O(n) vs O(V+E) graph |
| Problem semantics | 1 | subarray vs subset (LC 209) |
| Logic | 1 | removing wrong element in shrink |
| Indentation | 1 | left/right outside else |
| Syntax | 2 | `rows` instead of `range(rows)`, typos in variable names |

**Total: 27 bugs across 13 problems**

## Diagnosis (updated 7/28 post-simulation)

**P0: Translating algorithm to code structure.**
LC 133 exposed a new failure mode: understanding the algorithm verbally but unable to produce the code. Four bugs all stemmed from not designing the function structure before coding. Started coding with a confused outer/inner split. **Fix: for recursive DFS, the recursive function IS the entry point. Design the function signature and base case first, then fill in.**

**Co-P0: Python API recall.**
8 of 27 bugs are wrong method names. Resolved through 3-round API drill (12→4→0). Likely stable now.

**P1: Loop structure and invariant.**
5 bugs from wrong loop shape. Key patterns locked in through drills.

**P1: Complexity explanation.**
Graph = O(V+E). Sort-dominated = O(n log n). Sliding window = O(n). 3Sum = O(n²).

## Simulation results

| Round | Problem | Pattern | Score | Independent? |
|-------|---------|---------|-------|-------------|
| R1 | LC 253 Meeting Rooms II | Sweep line | 8/10 | Yes |
| R2 | LC 133 Clone Graph | DFS + hashmap | 6/10 | No (4 hints) |

**Afternoon repair target:** DFS-on-graph recursive structure — drill the "recursive function is the entry point" pattern.
