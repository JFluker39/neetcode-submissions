class Solution:
    def firstUniqChar(self, s: str) -> int:
        my_dict = {}
        for i in range(len(s)):
            if s[i] in my_dict:
                my_dict[s[i]] = -1
            else:
                my_dict[s[i]] = i

        min_val = 1000000000
        for key, value in my_dict.items():
            if value == -1:
                continue
            else:
                min_val = min(min_val, value)
        if min_val == 1000000000:
            return -1
        return min_val


        