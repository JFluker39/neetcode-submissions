class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        table = {}
        check = set()
        for t in trust:
            check.add(t[0])
            if t[1] in table:
                table[t[1]] += 1
            else:
                table[t[1]] = 1
        
        for i in range(1, n + 1):
            if i in table and table[i] == n - 1 and i not in check:
                return i
        return -1