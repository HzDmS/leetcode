class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        for i, t in enumerate(T):
            while stack and T[stack[-1]]  < t:
                j = stack.pop()
                T[j] = i - j
            stack.append(i)
        while stack:
            T[stack.pop()] = 0
        return T
