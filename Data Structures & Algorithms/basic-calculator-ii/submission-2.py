class Solution:
    def calculate(self, s: str) -> int:
        stack = []
        res = 0
        L = 0
        while L < len(s):
            if s[L] in "+-/*":
                stack.append(s[L])
            elif s[L].isdigit():
                stack.append(s[L])
                while L + 1 < len(s) and s[L + 1].isdigit():
                    stack[-1] += s[L + 1]
                    L += 1
            L += 1
        
        stack_1 = []
        for st in stack:
            if stack_1 and st.isdigit() and stack_1[-1] == "*":
                stack_1.pop()
                x = stack_1[-1]
                stack_1.pop()
                y = int(x) * int(st)
                stack_1.append(str(y))
            elif stack_1 and st.isdigit() and stack_1[-1] == "/":
                stack_1.pop()
                x = stack_1[-1]
                stack_1.pop()
                y = int(x) // int(st)
                stack_1.append(str(y))
            else:
                stack_1.append(st)
        print(stack_1)
        l = 1
        cur = int(stack_1[0])
        while l < len(stack_1):
            op = stack_1[l]
            y = stack_1[l + 1]
            if op == "+":
                cur = cur + int(y)
            else:
                cur = cur - int(y)
            l += 2
        return cur