class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0] * n] * m
        ROW = len(grid)
        COL = len(grid[0])

        for i in range(ROW):
            grid[i][0] = 1
        for i in range(COL):
            grid[0][i] = 1
        
        for i in range(ROW):
            for j in range(COL):
                if i == 0 or j == 0:
                    continue
                grid[i][j] = grid[i - 1][j] + grid[i][j - 1]
        return grid[m - 1][n - 1]
