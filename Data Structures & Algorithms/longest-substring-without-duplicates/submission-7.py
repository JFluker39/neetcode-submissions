class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 0
        m_s = 1
        my_set = set()
        while r < len(s):
            if s[r] not in my_set:
                my_set.add(s[r])
                m_s = max(m_s, r - l + 1)
                
            else:
                while s[r] != s[l] in my_set:
                    my_set.remove(s[l])
                    l += 1
                l += 1
            r += 1
        return m_s





        


        