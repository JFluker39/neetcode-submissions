class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        out = [1] * len(nums)

        for i in range(1, len(nums)):
            for j in range(i + 1):
                if nums[j] < nums[i] and out[j] >= out[i]:
                    out[i] = out[j] + 1
        print(out)
        m = 0
        for o in out:
            m = max(m, o)
        return m