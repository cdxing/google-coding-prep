'''
Timer: 15 minutes. Delayed rewrite. Closed-book.

  ---
  LC 200: Number of Islands

  Given an m x n 2D grid of '1's (land) and '0's (water), count the
  number of islands. An island is formed by connecting adjacent lands
  horizontally or vertically.

  Note: grid values are STRINGS '0' and '1', not integers.

  Example 1:
    grid = [["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]]
    → 3

  ---
  Invariant: After DFS returns, the entire connected component
  has been marked visited.

  Checklist:
  - bounds check BEFORE grid access
  - check all 4 directions (no break)

  Code. Go.

'''


def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    count = 0

    def dfs(r, c):
        grid[r][c] = "0"
        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            r_new = r + dr
            c_new = c + dc
            if 0 <= r_new < rows and 0 <= c_new < cols and grid[r_new][c_new] == "1":
                dfs(r_new, c_new)

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r,c)
                count += 1
    return count






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

grid = [["1","0","1"],
        ["0","1","0"],
        ["1","0","1"]]
print(numIslands(grid))  # 5
