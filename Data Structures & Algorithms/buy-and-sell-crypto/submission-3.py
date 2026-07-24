class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfit = 0
        min_value = prices[0]
        for i in range(1, len(prices)):
            if prices[i] - min_value > maxProfit:
                maxProfit = prices[i] - min_value
            if prices[i] < min_value:
                min_value = prices[i]
            
        return maxProfit







        
        