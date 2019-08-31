class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        if not triangle:
            return 0
        
        prev = triangle[0]
        for i in range(1, len(triangle)):
            cur = [0] * len(triangle[i])
            for j in range(len(triangle[i])):
                if j == 0:
                    cur[j] = prev[j] + triangle[i][j]
                elif j == i:
                    cur[j] = prev[j - 1] + triangle[i][j]
                else:
                    cur[j] = min(prev[j - 1], prev[j]) + triangle[i][j]
            prev = cur
        
        return min(prev)
