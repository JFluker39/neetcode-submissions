class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l = 0
        r = 0
        for i in range(len(nums)):
            r = i
            
            while r < len(nums) and abs(r - i) <= k:
                if nums[r] == nums[i] and r != i:
                    return True
                else:
                    r += 1
        return False     
