class Solution:
    def longestPalindrome(self, s: str) -> str:
        l = 0
        r = len(s) - 1
        seen = set()
        def dfs(l, r):
            if (l, r) in seen:
                return [0, 0]
            seen.add((l, r))
            if l == r:
                return [l, r]
            t = s[l: r + 1]
            if t == t[::-1]:
                return [l, r]
            x, y = dfs(l + 1, r)
            i, j = dfs(l, r - 1)
            return [x, y] if (y - x) > (j - i) else [i, j] 
        a, b = dfs(l, r)
        return s[a: b + 1]