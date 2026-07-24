class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        my_dict = {}
        for i in range(len(s)):
            if s[i] in my_dict:
                my_dict[s[i]] += 1
            else:
                my_dict[s[i]] = 1
        print(my_dict)

        for i in range(len(t)):
            if t[i] not in my_dict:
                return False
            elif my_dict[t[i]] <= 0:
                return False
            else:
                my_dict[t[i]] -= 1
        
        return True

        
