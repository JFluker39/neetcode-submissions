class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if not s:
            return ""
        stack = []
        num = 1
        cur = []
        for x in s:
            cur.append(x)
        
        changed = []
        while changed != cur:
            stack.append(cur[0])
            for i in range(1, len(cur)):
                if stack and cur[i] == stack[-1]:
                    num += 1
                else:
                    num = 1
                stack.append(cur[i])
                if num == k:
                    while num > 1:
                        stack.pop()
                        num -= 1
                    stack.pop()
            changed = stack

            if changed != cur:
                cur =  changed
                changed = []
                stack = []
                num = 1
        return ''.join(cur)
        