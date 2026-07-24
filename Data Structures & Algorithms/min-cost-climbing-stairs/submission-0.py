class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        my_arr = []
        n = len(cost)
        for i in range(len(cost)):
            if i == 0:
                my_arr.append(cost[i])
            elif i == 1:
                my_arr.append(cost[i])
            else:
                my_arr.append(cost[i] + min(my_arr[i-1], my_arr[i-2]))
        return min(my_arr[n-1], my_arr[n-2])