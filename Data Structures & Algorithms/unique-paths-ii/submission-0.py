class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        ROWS = len(obstacleGrid)
        COLS = len(obstacleGrid[0])
        
        for i in range(ROWS):
            for j in range(COLS):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = -1
        if obstacleGrid[0][0] == -1:
            return 0
        else:
            obstacleGrid[0][0] = 1
        for i in range(ROWS):
            if obstacleGrid[i][0] == 1:
                continue
            elif obstacleGrid[i][0] == 0 and obstacleGrid[i -1][0] == 1:
                obstacleGrid[i][0] = 1
            else:
                obstacleGrid[i][0] = -1
        
        for i in range(COLS):
            if obstacleGrid[0][i] == 1:
                continue
            elif obstacleGrid[0][i] == 0 and obstacleGrid[0][i - 1] == 1:
                obstacleGrid[0][i] = 1
            else:
                obstacleGrid[0][i] = -1
        
        for i in range(ROWS):
            for j in range(COLS):
                if i == 0 or j == 0 or obstacleGrid[i][j] == -1:
                    continue
                elif obstacleGrid[i - 1][j] >= 0  and obstacleGrid[i][j -1] >=0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
                elif obstacleGrid[i - 1][j] < 0:
                    obstacleGrid[i][j] = obstacleGrid[i][j - 1]
                elif obstacleGrid[i][j - 1] < 0:
                    obstacleGrid[i][j] = obstacleGrid[i - 1][j]
                else:
                    obstacleGrid[i][j] = -1
        print(obstacleGrid)
        return obstacleGrid[i][j] if obstacleGrid[i][j] >= 0 else 0

        