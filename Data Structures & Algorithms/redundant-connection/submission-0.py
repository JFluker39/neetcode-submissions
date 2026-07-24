class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        last_red = (-1, -1)
        n = len(edges)
        adj = defaultdict(set)
        for u, v in edges:
            adj[u].add(v)
            adj[v].add(u)

        def dfs(node, parent, seen):
            if node in seen:
                return False
            seen.add(node)
            if len(seen) == n:
                return True

            for nei in adj[node]:
                if nei == parent:
                    continue
                else:
                    if dfs(nei, node, seen):
                        return True
            return False

        for u, v in edges:
            adj[u].discard(v)
            adj[v].discard(u)
            if dfs(u, -1, set()):
                last_red = (u, v)
            adj[u].add(v)
            adj[v].add(u)
        return list(last_red)       