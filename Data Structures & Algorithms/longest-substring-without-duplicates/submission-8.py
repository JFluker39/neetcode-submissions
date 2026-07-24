class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        L = 0
        window = set()
        for c in s:
            if c not in window:
                window.add(c)
                max_len = max(len(window), max_len)
            else:
                while c in window:
                    window.remove(s[L])
                    L += 1
                window.add(c)
                max_len = max(len(window), max_len)
        return max_len