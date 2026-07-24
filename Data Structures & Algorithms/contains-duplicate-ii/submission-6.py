class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        check = set()
        l = 0
        r = 0
        while r < len(nums):
            while r - l <= k and r < len(nums):
                if nums[r] in check:
                    return True
                check.add(nums[r])
                r += 1
            check.remove(nums[l])
            l += 1
        return False