'''
Timer: 45 minutes. Start now.

  ---
  LC 994: Rotting Oranges

  You are given an m x n grid where each cell can have one of three values:
    0 — empty cell
    1 — fresh orange
    2 — rotten orange

  Every minute, any fresh orange that is 4-directionally adjacent
  to a rotten orange becomes rotten.

  Return the minimum number of minutes that must elapse until no cell
  has a fresh orange. If this is impossible, return -1.

  Example 1:
    grid = [[2,1,1],
            [1,1,0],
            [0,1,1]]
    → 4

  Example 2:
    grid = [[2,1,1],
            [0,1,1],
            [1,0,1]]
    → -1

  Example 3:
    grid = [[0,2]]
    → 0

  Constraints:
  - 1 <= m, n <= 10
  - grid[i][j] is 0, 1, or 2

  ---
  Before you code, say out loud (write in comments):
  1. Clarify the problem in your own words
  2. Baseline approach and its complexity
  3. Pattern you'll use and why
  4. The invariant

  Then code. Go.

'''

# 1. Clarify:
# A question that basically you want the situation you want to C the graph or great trees are connected. 我脑袋里，If not then the connected graph cannot reach the wholearea of interest, then you minus one and step by step right and what's the next step situation can get, so the complication need to find the adjacent adjacent parts that become from one to one from one to two right so the question is how to do that, So my answer to this question is to use the use the so called b searching so each layer search the next layer that's how it propagate, so that's my basic ideas let me. Know your perspective, your input, common
# 2. Baseline:
#
# 3. Pattern:
#
# 4. Invariant:
#

from collections import deque

def oranges_rotting(grid):
    # First we need to scan, go through the GRE To count all the truth and all the words the the words we know they are fresh and for的，The one adjacent to that in the next step next minute would be what right So we want to because by the end of the day, we need to count if there is still fresh fresh tomato to decide we return minus one or
    cols = len(grid[0])
    rows = len(grid)
    fresh = 0
    #rot = 0
    minute = 0
    queue = deque()
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                #rot += 1
                queue.append((r, c))


    # B FS is a GRE algorithm Model Thinking Model That I need to that you can give more questions like this, so I can build up my memory and also connect these DFS with some but we will Google pass infrastructure to my research, that I can have a connection with the with the kind of questions that I probably will deal with in the future; Better in a way that comparable because I think b FS is better to be acquired along with DFS, its counter alternative in many applications and also going through some grab or network things like that, make those patterns become muscle memory
    while queue:
        #r = queue.top()[0]
        #c = queue.top()[1]
        for _ in range(len(queue)):
            r, c = queue.popleft()
            for dr, dc in ((+1, 0), (-1, 0), (0, +1), (0, -1)):
                r_new = r + dr
                c_new = c + dc
                if 0<= r_new < rows and 0<= c_new < cols and grid[r_new][c_new] == 1:
                    grid[r_new][c_new] = 2
                    fresh -= 1
                    queue.append((r_new, c_new))
            #queue.pop()
        minute += 1
        
    if fresh == 0:
        return max(minute-1, 0)
        #return minute
    else:
        return -1




# --- Tests ---
grid = [[2,1,1],
        [1,1,0],
        [0,1,1]]
print(oranges_rotting(grid))  # 4

grid = [[2,1,1],
        [0,1,1],
        [1,0,1]]
print(oranges_rotting(grid))  # -1

grid = [[0,2]]
print(oranges_rotting(grid))  # 0

# ============================================================
# PATTERN CARD — BFS Level-by-Level (Multi-source)
# ============================================================
#
# Trigger:   "minimum time to spread/infect", "shortest distance from
#            multiple sources", "how many steps until all X become Y"
# Invariant: At the start of each while-loop iteration, the queue holds
#            all nodes at distance `t`; after processing, `t += 1`.
# Bug:       Forgetting the level loop `for _ in range(len(queue))` —
#            without it you lose track of which "round" you're in.
#            deque API: popleft() to dequeue, append() to enqueue.
#            Always bounds-check before accessing grid[r][c].
#
# Template:
#   from collections import deque
#   queue = deque(all_sources)          # seed with ALL starting points
#   visited or mark grid in-place
#   time = 0
#   while queue:
#       for _ in range(len(queue)):     # ← process entire level
#           node = queue.popleft()
#           for neighbor in 4_directions:
#               if in_bounds and unvisited:
#                   mark visited
#                   queue.append(neighbor)
#       time += 1
#   return time - 1  (or max(time-1, 0))
#
# Complexity: O(m*n) time, O(m*n) space
#
# BFS vs DFS on grids:
#   BFS — use when you need shortest distance / minimum time
#   DFS — use when you need to count/label connected components
#
# Related problems:
#   - LC 200  Number of Islands (DFS/BFS to count components)
#   - LC 286  Walls and Gates (multi-source BFS)
#   - LC 1091 Shortest Path in Binary Matrix (single-source BFS)
#   - LC 542  01 Matrix (multi-source BFS from all 0s)
# ============================================================


# ============================================================
# FOLLOW-UP: LC 200 — Number of Islands (DFS counterpart)
# ============================================================
#
# Given an m x n 2D grid of '1's (land) and '0's (water), count
# the number of islands. An island is surrounded by water and is
# formed by connecting adjacent lands horizontally or vertically.
#
# Example 1:
#   grid = [["1","1","1","1","0"],
#           ["1","1","0","1","0"],
#           ["1","1","0","0","0"],
#           ["0","0","0","0","0"]]
#   → 1
#
# Example 2:
#   grid = [["1","1","0","0","0"],
#           ["1","1","0","0","0"],
#           ["0","0","1","0","0"],
#           ["0","0","0","1","1"]]
#   → 3
#
# Key difference from LC994:
#   - No "time" tracking needed — just counting components
#   - DFS is simpler here: when you find a '1', DFS-flood to sink
#     the entire island (mark visited), increment count
#   - BFS also works but DFS is more natural for "explore entire component"
#
# Pattern:
#   Trigger:   "count connected components", "number of islands/regions"
#   Invariant: each DFS/BFS call fully explores one component;
#              counter increments once per component
#
# Template:
#   def numIslands(grid):
#       rows, cols = len(grid), len(grid[0])
#       count = 0
#       def dfs(r, c):
#           if r < 0 or r >= rows or c < 0 or c >= cols:
#               return
#           if grid[r][c] != '1':
#               return
#           grid[r][c] = '0'           # sink it (mark visited)
#           for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
#               dfs(r+dr, c+dc)
#       for r in range(rows):
#           for c in range(cols):
#               if grid[r][c] == '1':
#                   dfs(r, c)
#                   count += 1
#       return count
#
# Complexity: O(m*n) time, O(m*n) space (recursion stack worst case)
# ============================================================
