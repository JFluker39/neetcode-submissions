class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total = 0
        sell = -1
        buy = 11,000
        bought = False
        for num in prices:
            if bought == False:
                buy = num
                bought = True
            elif bought == True and num < buy:
                buy = num
                sell = -1
            elif num > sell:
                t = num - buy
                buy = num
                print(num)
                print(buy)
                total += t
            else:
                sell = -1
                buy = num
        return total