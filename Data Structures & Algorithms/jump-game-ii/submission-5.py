class Solution:
    def jump(self, nums: List[int]) -> int:
        num_jumps = 1
        max_element = nums[0]
        cur_max = nums[0]
        n = len(nums)
        if n == 1:
            return 0
        if n == 2 or nums[0] >= n - 1:
            return 1
        i = 1
        while i < n:
            while i <= max_element:
                if i + nums[i] >= n - 1:
                    return num_jumps + 1
                cur_max = max(cur_max, i + nums[i])
                i += 1
            
            num_jumps += 1
            max_element = cur_max
        return num_jumps