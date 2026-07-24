class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        L = 0
        shortest = float('inf')
        total = 0

        for i in range(len(nums)):
            total += nums[i]
            while total >= target:
                shortest = min(shortest, i - L + 1)
                total -= nums[L]
                L += 1
        if shortest == float('inf'):
            return 0
        else:
            return shortest