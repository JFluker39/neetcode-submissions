class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pj = defaultdict(list)
        pi = []
        for p in points:
            s = math.sqrt(p[0]**2 + p[1]**2)
            pi.append(s)
            pj[s].append([p[0], p[1]])

        heapq.heapify_max(pi)
        while len(pi) > k:
            pop = heapq.heappop_max(pi)
            pj.pop(pop, None)
        ret = []
        for key, value in pj.items():
            ret += value
        return ret
