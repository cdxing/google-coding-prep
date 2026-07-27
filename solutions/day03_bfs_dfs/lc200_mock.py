'''
Timer: 20 minutes. Start now.

  ---
  LC 200: Number of Islands

  Given an m x n 2D grid of '1's (land) and '0's (water), count the
  number of islands. An island is surrounded by water and formed by
  connecting adjacent lands horizontally or vertically.

  Example 1:
    grid = [["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]]
    → 1

  Example 2:
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    → 3

  Constraints:
  - m == grid.length
  - n == grid[i].length
  - 1 <= m, n <= 300
  - grid[i][j] is '0' or '1'

  Note: grid values are STRINGS, not integers.

  ---
  Before you code, write:
  1. Pattern
  2. Invariant
  3. Complexity

  Then code. Go.

'''

# 1. Pattern:
#
# 2. Invariant:
#
# 3. Complexity:
#


def numIslands(grid):
    pass




# --- Tests ---
grid = [["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]]
print(numIslands(grid))  # 1

grid = [["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]]
print(numIslands(grid))  # 3

grid = [["0"]]
print(numIslands(grid))  # 0

grid = [["1"]]
print(numIslands(grid))  # 1
