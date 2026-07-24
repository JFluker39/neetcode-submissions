class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        m = set()
        for n in nums:
            if n in m:
                m.discard(n)
            else:
                m.add(n)
        return m.pop()