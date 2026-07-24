class Solution:
    def maxArea(self, heights: List[int]) -> int:
        ans = 0
        l = 0
        n = len(heights)
        r = n - 1
        while l <= r:
            h = min(heights[l], heights[r])
            a = (r - l) * h
            ans = max(ans, a)

            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return ans