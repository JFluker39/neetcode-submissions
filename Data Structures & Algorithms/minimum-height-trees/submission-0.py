class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        def dfs(node, parent):
            hgt = 0
            for nei in adj[node]:
                if nei == parent:
                    continue
                hgt = max(hgt, 1 + dfs(nei, node))
            return hgt
        
        minhgt = n
        res = []
        for i in range(n):
            curhgt = dfs(i, -1)
            if curhgt == minhgt:
                res.append(i)
            elif curhgt < minhgt:
                res = [i]
                minhgt = curhgt
        return res