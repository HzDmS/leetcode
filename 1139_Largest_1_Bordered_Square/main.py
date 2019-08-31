class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        up, left = [[0] * n for _ in range(m)], [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if grid[i][j]:
                    up[i][j] = up[i][j - 1] + 1 if j > 0 else 1
                    left[i][j] = left[i - 1][j] + 1 if i > 0 else 1
        
        for l in range(min(m, n) - 1, -1, -1):
            for i in range(m - 1, l - 1, -1):
                for j in range(n - 1, l - 1, -1):
                    if left[i][j] >= (l + 1) and left[i][j - l] >= (l + 1) and \
                       up[i][j] >= (l + 1) and up[i - l][j] >= (l + 1):
                        return (l + 1) ** 2
        
        return 0
                    
