class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2 + 1
        my_dict = {}
        for i in range(len(nums)):
            if nums[i] in my_dict:
                my_dict[nums[i]] += 1
            else:
                my_dict[nums[i]] = 1
            if my_dict[nums[i]] >= majority:
                return nums[i]
