class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l = 1
        r = 500 * 50000
        final = 0
        while  l <= r:
            m = (l + r) // 2
            c = self.check(weights, m, days)
            if c:
                print("Weight works")
                r = m - 1
            else:
                print("Weight doesn't work")
                l = m + 1
            final = m
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