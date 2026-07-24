class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        r = 0
        my_set = set()
        longest = 0
        while r < len(s):
            if s[r] not in my_set:
                my_set.add(s[r])
                longest = max(longest, r - l + 1)
                r += 1
                
            else:
                my_set.remove(s[l])
                l += 1
        return longest



        


        