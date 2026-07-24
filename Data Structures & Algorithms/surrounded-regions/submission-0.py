class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        edge_o = []
        for i in range(rows):
            if board[i][0] == "O":
                edge_o.append([i, 0])
            if board[i][cols - 1] == "O":
                edge_o.append([i, cols - 1])
        for i in range(cols):
            if board[0][i] == "O":
                edge_o.append([0, i])
            if board[rows - 1][i] == "O":
                edge_o.append([rows - 1, i])
        visit = set()
        def dfs(i, j):
            if i < 0 or j < 0 or i >= rows or j >= cols or (i, j) in visit:
                return
            visit.add((i, j))
            if i + 1 < rows and board[i + 1][j]== "O":
                dfs(i + 1, j)
            if i - 1 >= 0 and board[i - 1][j]== "O":
                dfs(i - 1, j)
            if j + 1 < cols and board[i][j + 1]== "O":
                dfs(i, j + 1)
            if j - 1 >= 0 and board[i][j - 1]== "O":
                dfs(i, j - 1)
        
        for i, j in edge_o:
            if (i, j) not in visit:
                dfs(i, j)
        print(visit)
        for i in range(rows):
            for j in range(cols):
                if (i, j) not in visit and board[i][j] == "O":
                    board[i][j] = "X"
        