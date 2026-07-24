class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        out = 0
        
        my_set = set(nums)
        for r in nums:
            curr = 1
            if r - 1 in my_set:
                continue
            else:
                j = r
                while j + 1 in my_set:
                    j += 1
                    curr += 1
            out = max(out, curr)

        return out

        