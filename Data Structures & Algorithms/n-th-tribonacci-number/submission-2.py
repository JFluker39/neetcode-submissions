class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 1
        out = [0] * (n + 1)
        out[1] = 1
        out[2] = 1
        for i in range(3, n + 1):
            out[i] = out[i - 1] + out[i - 2] + out[i - 3]
        return out[n]