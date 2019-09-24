class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        
        if not heights:
            return 0
        
        stack = [(-1, -1)]
        ans = 0
        for i, num in enumerate(heights):
            if num > stack[-1][1]:
                stack.append((i, num))
            else:
                while not num > stack[-1][1]:
                    _, tmp = stack.pop()
                    ans = max(ans, (i - stack[-1][0] - 1) * tmp)
                stack.append((i, num))
        n = len(heights)
        while len(stack) > 1:
            _, tmp = stack.pop()
            ans = max(ans, (n - stack[-1][0] - 1) * tmp)
        return ans

