class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        third = len(nums) // 3 + 1
        my_dict = {}
        my_list = []
        for num in nums:
            if num in my_dict:
                my_dict[num] += 1
            else:
                my_dict[num] = 1
        for key, value in my_dict.items():
            if value >= third:
                my_list.append(key)
        return my_list