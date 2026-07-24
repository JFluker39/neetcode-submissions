class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        num = 0
        rows = len(grid)
        cols = len(grid[0])
        visit = set()
        
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or grid[i][j] == "0":
                return
            if (i, j) in visit:
                return

            visit.add((i, j))
            dfs(i, j + 1)
            dfs(i + 1, j)
            dfs(i, j - 1)
            dfs(i - 1, j)
        i = 0
        while i < rows:
            j = 0
            while j < cols:
                if grid[i][j] == "1" and (i, j) not in visit:
                    print("DFS")
                    num += 1
                    dfs(i, j)
                    print(visit)
                j += 1
            i += 1
        return num