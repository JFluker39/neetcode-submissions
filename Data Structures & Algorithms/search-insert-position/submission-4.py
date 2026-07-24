class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        if nums[0] > target:
            return 0
        if nums[r] < target:
            return r + 1

        while l <= r:
            m = l + ((r - l) // 2)

            if nums[m] == target:
                return m
            elif nums[m] < target:
                if m + 1 < len(nums) and nums[m + 1] > target:
                    return m + 1
                else:
                    l = m + 1
            elif nums[m] > target:
                if m - 1 >= 0  and nums[m - 1] < target:
                    return m 
                else:
                    r = m - 1
        return m + 1