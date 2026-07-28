'''
Timer: 15 minutes. Delayed rewrite. Closed-book.

  ---
  LC 994: Rotting Oranges

  Given an m x n grid where:
    0 = empty, 1 = fresh orange, 2 = rotten orange

  Every minute, fresh oranges adjacent (4-dir) to rotten ones become rotten.
  Return minimum minutes until no fresh orange remains, or -1 if impossible.

  Example 1: [[2,1,1],[1,1,0],[0,1,1]] → 4
  Example 2: [[2,1,1],[0,1,1],[1,0,1]] → -1
  Example 3: [[0,2]] → 0

  ---
  Invariant: At the start of each while-loop iteration, the queue holds
  all oranges rotting at time t. After processing, t += 1.

  Code. Go.

'''

from collections import deque


def orangesRotting(grid):
    queue = deque()

    rows = len(grid)
    cols = len(grid[0])
    fresh = 0
    time = 0
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                queue.append((r, c))

    while queue:
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                r_new = r + dr
                c_new = c + dc
                if 0 <= r_new < rows and 0 <= c_new < cols and grid[r_new][c_new] == 1:
                    grid[r_new][c_new] = 2
                    queue.append((r_new, c_new))
                    fresh -= 1
        if queue:
            time += 1
    return -1 if fresh > 0 else time




# --- Tests ---
print(orangesRotting([[2,1,1],[1,1,0],[0,1,1]]))  # 4
print(orangesRotting([[2,1,1],[0,1,1],[1,0,1]]))  # -1
print(orangesRotting([[0,2]]))                      # 0
print(orangesRotting([[1]]))                        # -1
print(orangesRotting([[2]]))                        # 0
print(orangesRotting([[0]]))                        # 0
