# LC 200 - Number of Islands
#
# Given an m x n 2D grid of '1's (land) and '0's (water),
# return the number of islands.
#
# An island is surrounded by water and is formed by connecting
# adjacent lands horizontally or vertically. You may assume all
# four edges of the grid are surrounded by water.
#
# Example:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3

# Write your solution below:
def NumberOfIslands(grid):
    # define the rows and cols
    rows = len(grid)
    cols = len(grid[0])

    # add counts outside of the dfs
    count = 0

    def dfs(r, c, islands):
        if r >= 0 and r < rows and c >= 0 and c < cols:
            if islands[r][c] == "1":
                islands[r][c] = "0"
                for dr, dc in (+1, 0), (-1, 0), (0, +1), (0, -1):
                    dfs(r + dr, c + dc, islands)
            else:
                return
        else:
            return

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == "1":
                count += 1
                dfs(row, col, grid)

    return count



grid = [
   ["1","1","0","0","0"],
   ["1","1","0","0","0"],
   ["0","0","1","0","0"],
   ["0","0","0","1","1"]
]
print(NumberOfIslands(grid))

