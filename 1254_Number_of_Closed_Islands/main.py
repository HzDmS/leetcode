class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        cnt = 0
        m, n = len(grid), len(grid[0])
        for i in range(m):
            self.dfs(i, 0, grid)
            self.dfs(i, n - 1, grid)
        for j in range(n):
            self.dfs(0, j, grid)
            self.dfs(m - 1, j, grid)
        for i in range(1, m):
            for j in range(1, n):
                if grid[i][j] == 1:
                    continue
                else:
                    self.dfs(i, j, grid)
                    cnt += 1
        return cnt

    def dfs(self, i, j, grid):
        if grid[i][j] == 1:
            return
        grid[i][j] = 1
        for a, b in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            new_i, new_j = i + a, j + b
            if new_i < 0 or new_i >= len(grid) or new_j < 0 or new_j >= len(grid[0]):
                continue
            self.dfs(new_i, new_j, grid)

