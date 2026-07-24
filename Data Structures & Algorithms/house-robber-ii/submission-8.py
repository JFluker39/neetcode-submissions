class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])
        out1 = [0] * n
        out2 = [0] * n
        out1[1] = nums[1]
        out2[0] = nums[0]
        out2[1] = max(nums[1], nums[0])
        for i in range(2, n):
            out1[i] = max(out1[i- 1], nums[i] + out1[i - 2])
        for i in range(2, n - 1):
            out2[i] = max(out2[i - 1], nums[i] + out2[i - 2])
        
        return max(out1[n - 1], out2[n - 2])
