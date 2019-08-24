class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        m, n = len(grid), len(grid[0])
        total = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    continue
                for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_i, new_j = i + x, j + y
                    if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                        total += 1
                        continue
                    if grid[new_i][new_j] == 0:
                        total += 1
        return total
