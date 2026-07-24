class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        my_dict = {0 : 1}
        res = 0
        cursum = 0
        for i in range(len(nums)):
            cursum += nums[i]
            if cursum - k in my_dict:
                res += my_dict[cursum - k]
            if cursum in my_dict:
                my_dict[cursum] += 1
            else:
                my_dict[cursum] = 1
        return res