class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        out = []
        l = 0
        r = k - 1

        while r < len(nums):
            maxWin = -11000
            for i in range(l, r + 1):
                maxWin = max(maxWin, nums[i])
            out.append(maxWin)
            l += 1
            r += 1
        return out