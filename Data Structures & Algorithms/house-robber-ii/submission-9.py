class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        prev1 = nums[1]
        prev2 = 0
        
        for i in range(2, n):
            cur = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = cur
        num = prev1
        prev2 = nums[0]
        prev1 = max(nums[0], nums[1])
        for i in range(2, n - 1):
            cur = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = cur
        
        return max(num, prev1)
