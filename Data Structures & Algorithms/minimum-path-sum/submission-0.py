class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 and j == 0:
                    continue
                up = grid[i - 1][j] if i - 1 >= 0 else 201
                left = grid[i][j - 1] if j - 1>= 0 else 201

                grid[i][j] = grid[i][j] + min(up, left)
        return grid[ROWS - 1][COLS - 1]