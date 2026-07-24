class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify_max(nums)
        while k > 0:
            k -= 1
            j = heapq.heappop_max(nums)
        return j