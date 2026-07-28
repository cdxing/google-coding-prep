# Day 8 Summary — Monday July 27, 2026

## Training Results

### Drill Scores (first attempt → best rewrite)

| Problem | Pattern | First | Rewrite | Status |
|---------|---------|-------|---------|--------|
| LC 200 | DFS flood-fill | 8/10 | 10/10 | locked ✓ |
| LC 215 | Heap top-K | 6/10 | 10/10 | locked ✓ |
| LC 994 | Multi-source BFS | 7/10 | 8/10 | stable ✓ |
| LC 15 | 3Sum two pointers | 4/10 | 7/10 | improved |
| LC 3 | Sliding window | 5/10 | 10/10 | locked ✓ |
| LC 56 | Merge intervals | 9/10 | — | clean first pass |
| LC 209 | Sliding window (min) | 6/10 | — | subarray vs subset bug |
| API drill | — | 12 errors | 0 errors | locked ✓ |

### Key insight
Delayed rewrites work. Every pattern improved on second attempt with 30-90 min gap.

### Bottleneck diagnosis (updated)

**P0: Problem semantics**
- Must ask before coding: contiguous? ordered? positive/negative? duplicates?
- LC 209: sorted array when problem required subarray (contiguous)

**Co-P0: Python API recall**
- 8 of 20 total bugs were wrong method names
- Resolved: 0 errors on round 3 API drill
- Container API now memorized: set.add(), deque.append()/popleft(), heapq.heappush()/heappop(), len() for everything

**P1: Loop structure**
- Sliding window: while shrink, not if/else (finally locked in drill 3)
- BFS: for _ in range(len(queue)), not for _ in queue
- 3Sum: dedup i with continue, left/right with while inside else

**P1: Complexity explanation**
- Sort-dominated = O(n log n)
- Sliding window = O(n) (each element added/removed once)
- 3Sum = O(n²)
