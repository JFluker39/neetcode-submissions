class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        L = 0
        for i in range(len(prices)):
            profit = max(profit, prices[i] - prices[L])
            if prices[i] < prices[L]:
                L = i
        return profit