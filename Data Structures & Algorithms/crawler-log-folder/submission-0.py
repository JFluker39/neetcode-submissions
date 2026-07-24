class Solution:
    def minOperations(self, logs: List[str]) -> int:
        out = 0
        for i in range(len(logs)):
            if logs[i] == "../" and out == 0:
                continue
            elif logs[i] == "../" and out > 0:
                out -= 1
            elif logs[i] == "./":
                continue
            else:
                out += 1
        return out
        