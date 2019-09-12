class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        n = len(height)
        stack = []
        i = 0
        while i < n:
            if not stack:
                stack.append((height[i], i))
                i += 1
            else:
                if height[i] < stack[-1][0]:
                    stack.append((height[i], i))
                    i += 1
                else:
                    if len(stack) == 1:
                        stack.pop()
                    else:
                        h, k = stack.pop()
                        ans += (min(height[i], stack[-1][0]) - h) * (i - stack[-1][1] - 1)
        return ans
        
