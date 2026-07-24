class Solution:
    def validPalindrome(self, s: str) -> bool:
        def palin(l, r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True


        l = 0
        r = len(s) - 1
        times = 0
        while l <= r:
            if s[l] != s[r]:
                return palin(l, r - 1) or palin(l + 1, r) if l <= r - 1 and times == 0 else False
            l += 1
            r -= 1           
        return True