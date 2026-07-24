class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2
        arr = []
        for i in range(n):
            if i == 0:
                arr.append(0)
            elif i == 1:
                arr.append(1)
            elif i == 2:
                arr.append(2)
            else:
                arr.append(arr[i - 1] + arr[i - 2])
        return arr[n - 1] + arr[n - 2]
        