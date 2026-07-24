class Solution:
    def isPalindrome(self, s: str) -> bool:
        s1 = s.lower().replace(" ", "")
        print(s1)
        res = ""
        for c in s1:
            if c.isalpha() or c.isdigit():
                res += c
        print(res)

        start = 0
        end = len(res) - 1
        while start < end:
            if res[start] != res[end]:
                return False
            start += 1
            end -= 1
        return True
        