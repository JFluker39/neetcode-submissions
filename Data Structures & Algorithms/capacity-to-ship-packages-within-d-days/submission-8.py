class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 1
        r = 0
        for we in weights:
            r += we
        while  l <= r:
            m = (l + r) // 2
            c = self.check(weights, m, days)
            if c:
                r = m - 1
            else:
                l = m + 1
        return l

    def check(self, weights: List[int], w, days) -> bool:
        i = 0
        m = w
        while days > 0 and i < len(weights):
            if  m - weights[i] >= 0:
                m -= weights[i]
                i += 1
            else:
                days -= 1
                m = w
        if i == len(weights) and days >= 0:
            return True
        else:
            return False