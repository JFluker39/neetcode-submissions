class Solution:
    def numSquares(self, n: int) -> int:
        out = [n] * (n + 1)
        out[0] = 0

        for i in range(1, n + 1):
            for j in range(1, i + 1):
                square = j * j
                if i - square < 0:
                    break
                out[i] = min(out[i], 1 + out[i - square])
        return out[n]