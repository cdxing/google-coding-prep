# Knowledge Tree: Graph, BFS, DFS

```
Graph Fundamentals
│
├── What is a Graph?
│   ├── Nodes (vertices) + Edges (connections)
│   ├── vs Tree: graphs can have cycles, multiple paths, no single root
│   ├── Directed vs Undirected
│   └── Representations
│       ├── Adjacency List: {node: [neighbors]}  ← most common in interviews
│       ├── Adjacency Matrix: grid[i][j] = 1/0
│       └── Implicit Grid: 2D array where neighbors = 4 directions
│
├── Traversal: how to visit every reachable node exactly once
│   │
│   ├── DFS (Depth-First Search)
│   │   ├── Idea: go as deep as possible, then backtrack
│   │   ├── Implementation
│   │   │   ├── Recursive: function calls = implicit stack
│   │   │   └── Iterative: explicit stack (append/pop = LIFO)
│   │   ├── Use cases
│   │   │   ├── Connected components (LC 200)
│   │   │   ├── Cycle detection
│   │   │   ├── Path finding
│   │   │   └── Clone graph (LC 133)
│   │   └── Key detail: mark visited BEFORE recursing
│   │
│   ├── BFS (Breadth-First Search)
│   │   ├── Idea: visit all neighbors first, then their neighbors
│   │   ├── Implementation
│   │   │   └── Queue: deque (append/popleft = FIFO)
│   │   ├── Use cases
│   │   │   ├── Shortest path in unweighted graph
│   │   │   ├── Level-order traversal
│   │   │   └── Nearest neighbor problems
│   │   └── Key detail: mark visited when ADDING to queue, not when popping
│   │
│   └── DFS vs BFS
│       ├── DFS: stack (LIFO) → deep first
│       ├── BFS: queue (FIFO) → wide first
│       ├── Both visit every node once → O(V + E) time
│       └── BFS guarantees shortest path; DFS does not
│
├── Cycle Handling
│   ├── Why needed: unlike trees, revisiting is possible
│   ├── Solution: visited set or mark-in-place
│   └── Topological Sort: only works on DAGs (no cycles)
│       ├── Idea: process nodes with no incoming edges first
│       ├── Implementation: Kahn's algorithm (BFS + in_degree array)
│       ├── Use case: dependency ordering (LC 207)
│       └── Cycle detection: if completed < total nodes → cycle exists
│
└── Python Building Blocks
    ├── deque: from collections import deque
    │   ├── deque() → create
    │   ├── .append(x) → add to right
    │   ├── .popleft() → remove from left (FIFO for BFS)
    │   └── .pop() → remove from right (LIFO for DFS)
    ├── set(): visited = set(); visited.add(node)
    └── defaultdict(list): graph = defaultdict(list)
```
