# BFS / DFS Pattern Card

## DFS on Grid
```
Trigger:   Count/find connected components in a grid
Invariant: After dfs(r,c) returns, entire component containing (r,c) is marked visited
Bug:       Mark visited BEFORE recursing; check bounds BEFORE accessing grid
```

## BFS on Grid
```
Trigger:   Shortest path in unweighted grid, or level-order traversal
Invariant: Every cell in the queue is already marked visited
Bug:       Mark visited when ADDING to queue, not when POPPING (causes duplicates)
```

## Topological Sort (Kahn's BFS)
```
Trigger:   Dependency ordering, cycle detection in DAG
Invariant: Every node in queue has in_degree == 0
Bug:       Forgetting to check completed == num_nodes for cycle detection
```
