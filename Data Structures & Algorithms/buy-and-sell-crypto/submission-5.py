class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxP = 0
        buy = 101
        for p in prices:
            buy = min(p, buy)
            maxP = max(maxP, p - buy)
        return maxP