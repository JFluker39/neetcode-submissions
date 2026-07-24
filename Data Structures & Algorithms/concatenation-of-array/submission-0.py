class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = nums
        for i in range(len(nums)):
            n.append(nums[i])
        return n