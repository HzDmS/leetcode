class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        ans = 0
        if not grid or not grid[0]:
            return ans
        m, n = len(grid), len(grid[0])
        visited = [[0] * n for _ in range(m)]
        
        def dfs(i, j):
            if i < 0 or i >= m or j < 0 or j >= n or visited[i][j] or grid[i][j] == "0":
                return
            else:
                visited[i][j] = 1
                dfs(i + 1, j)
                dfs(i - 1, j)
                dfs(i, j + 1)
                dfs(i, j - 1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    ans += 1
        return ans

