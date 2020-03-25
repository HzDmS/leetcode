class Solution:
    def calculate(self, s: str) -> int:
        if s == "0":
            return 0

        stack, num, op = [], 0, "+"
        n = len(s)
        for i in range(n):
            if s[i].isdigit():
                num = num * 10 + ord(s[i]) - ord("0")
            if not s[i].isdigit() and not s[i].isspace() or i == n - 1:
                if op == "*":
                    stack.append(num * stack.pop())
                elif op == "+":
                    stack.append(num)
                elif op == "-":
                    stack.append(-num)
                else:
                    numerator = stack.pop()
                    if numerator < 0 and not numerator % num == 0:
                        stack.append(numerator // num + 1)
                    else:
                        stack.append(numerator // num)
                num, op = 0, s[i]
        return sum(stack)

