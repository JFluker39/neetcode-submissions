class Solution:
    def reverseBits(self, n: int) -> int:
        for i in range(0, 16):
            s = 31 - i
            x = 0
            y = 0
            if n & (1 << i) > 0:
                x = 1
            if n & (1 << s) > 0:
                y = 1
            if x ^ y:
                print("Switch", i, s, x, y)
                if x:
                    j = n
                    n = ~n & (x << s)
                    n = n | j
                    j = n
                    n = ~n | (x << i)
                    n = ~n
                else:
                    j = n
                    n = ~n & (y << i)
                    n = n | j
                    j = n
                    n = ~n | (y << s)
                    n = ~n 
        return n