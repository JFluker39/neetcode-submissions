class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        closest = []
        for p in points:
            d = math.sqrt(p[0]**2 + p[1]**2)
            heapq.heappush_max(closest, (d, p[0], p[1]))
            if len(closest) > k:
                heapq.heappop_max(closest)
        ret = []
        for c in closest:
            ret.append([c[1], c[2]])
        return ret
