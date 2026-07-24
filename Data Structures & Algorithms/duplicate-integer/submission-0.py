class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dict1 = set()
        for i in range(len(nums)):
            if nums[i] in dict1:
                return True
            else:
                dict1.add(nums[i])
        return False
        