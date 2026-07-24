class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]

        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        cnt = {}
        leaves = deque()

        for node, nex in adj.items():
            cnt[node] = len(nex)
            if len(nex) == 1:
                leaves.append(node)

        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                node = leaves.popleft()
                n -= 1
                for nei in adj[node]:
                    cnt[nei] -= 1
                    if cnt[nei] == 1:
                        leaves.append(nei)