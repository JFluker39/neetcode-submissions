class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1 = {}
        for i in range(len(nums)):
            find = target - nums[i]
            if find in dict1:
                return [dict1[find], i]
            else:
                dict1[nums[i]] = i

    
        