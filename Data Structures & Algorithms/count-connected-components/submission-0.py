class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        compon = 0
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        nodes = set()
        
        def dfs(node):
            if node in nodes:
                return
            nodes.add(node)
            for n in adj[node]:
                dfs(n)
        
        for i in range(n):
            if i in nodes:
                continue
                
            compon += 1
            dfs(i)
            if len(nodes) == n:
                return compon