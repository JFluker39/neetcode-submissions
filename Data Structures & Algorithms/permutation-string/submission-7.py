class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        freq = [0] * 26
        for s in s1:
            freq[ord(s) - 97] += 1
        l = 0
        r = 0
        out = [0] * 26
        while r < len(s1) - 1:
            out[ord(s2[r]) - 97] += 1
            r += 1
        
        while r < len(s2):
            out[ord(s2[r]) - 97] += 1
            print(freq)
            print(out)
            if out == freq:
                return True
            out[ord(s2[l]) - 97] -= 1
            l += 1
            r += 1
        return False