class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for c in s:
            if not stack:
                stack.append(c)
            else:
                if stack[-1] + c in ["()", "{}", "[]"]:
                    stack.pop()
                else:
                    stack.append(c)
        return not stack
        
