class Solution:
    def rob(self, nums: List[int]) -> int:
        my_arr = []
        n = len(nums)
        for i in range(len(nums)):
            if i == 0:
                my_arr.append(nums[i])
            elif i == 1:
                my_arr.append(max(nums[i], nums[i-1]))
            else:
                my_arr.append(max(my_arr[i-1], nums[i] + my_arr[i-2]))
        return max(my_arr[n-1], my_arr[n-2])