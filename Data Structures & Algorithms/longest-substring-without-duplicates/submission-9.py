class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        mySet = set()
        l = 0
        r = 0
        while r < len(s):
            if s[r] in mySet:
                while s[r] in mySet:
                    mySet.remove(s[l])
                    l += 1
            mySet.add(s[r])
            maxLen = max(maxLen, r - l + 1)
            r += 1
        return maxLen