class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        my_set = {}
        for i in range(len(nums)):
            if nums[i] in my_set and abs(i - my_set[nums[i]]) <= k:
                return True


            my_set[nums[i]] = i
        return False            
