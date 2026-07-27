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
# for these kind of questions, like, you want to, when there's an object, you want to go to as deep as possible. For example, first find one island, then you want to figure out how big it is, like, how, exhaust the size of the island, then move to the next one. So this way, which is called a depth-first search.
# 2. Invariant:

#I'm not sure about the invariant used here. So, if you are referring to the invariant that's constant in such a pattern, right? So, the invariant of this pattern is that you have a tree or a map, you go through the depths of the tree one branch as deep as possible, then count as one, then move to the next branch of the tree. I don't know if that answers the part for the invariant, but let me know if I got it not as expected.
# 3. Complexity:
# Something about for the brute force way, you look over all the items. So, for the time complexity, for, you go through the depth of the tree, and then back. So, for the space, I would say at order of n, and in the time-wise, I would give it an order of n as well, because you need to go as deep as possible. So at order of both space and time, that's my guess. Correct me if I'm wrong.


def numIslands(grid):
    rows = len(grid)
    cols = len(grid[0])
    island_count = 0

    def dfs(r, c):
        grid[r][c] = "0"

        for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            r_new = r + dr
            c_new = c + dc
            #if grid[r_new][c_new] == "1" and 0 <= r_new < rows and 0 <= c_new < cols:
            if 0 <= r_new < rows and 0 <= c_new < cols and grid[r_new][c_new] == "1":
                dfs(r_new, c_new)
            #else:
                #break

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == "1":
                dfs(r, c)
                island_count += 1

    return island_count

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
