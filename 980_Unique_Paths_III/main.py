class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:

        m, n = len(grid), len(grid[0])
        ans = 0
        visited = [[False] * n for _ in range(m)]
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        non_obs = 1
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    start = tuple([i, j])
                if grid[i][j] == 0:
                    non_obs += 1
        
        def dfs(i, j, length):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == -1:
                return 0
            else:
                if grid[i][j] == 2:
                    return length == non_obs
                else:
                    visited[i][j] = True
                    tmp = 0
                    for x, y in dirs:
                        tmp += dfs(i + x, j + y, length + 1)
                    visited[i][j] = False
                    return tmp

        return dfs(start[0], start[1], 0)

