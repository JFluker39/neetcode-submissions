class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_element = 0
        for i in range(len(nums)):
            if nums[i] + i >= len(nums) - 1:
                return True
            if nums[i] == 0 and max_element == i:
                return False
            
            
            max_element = max(max_element, nums[i] + i)