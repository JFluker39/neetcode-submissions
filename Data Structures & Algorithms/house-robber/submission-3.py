class Solution:
    def rob(self, nums: List[int]) -> int:
        out = [0] * len(nums)
        if nums:
            out[0] = nums[0]
        if 1 < len(nums):
            out[1] = max(nums[1], nums[0])
        else:
            return nums[0]
        for i in range(2, len(nums)):
            out[i] = max(out[i - 1], out[i - 2] + nums[i])
        print(out)
        return out[len(nums) - 1]
