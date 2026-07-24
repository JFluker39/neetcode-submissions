class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        l, r = 0, k

        while r < len(arr):
            if abs(arr[r] - x) < abs(arr[l] - x) or arr[r] == arr[l]:
                l += 1
            else:
                break
            r += 1
        return arr[l: r]