class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        # DFS
        # time complexity: O(r * c)
        # space complexity: O(r * c)
        
        tf_map = [[True if x == 0 else False for x in row] for row in grid]
        m, n = len(grid), len(grid[0])
        
        def dfs(i, j):
            
            if i < 0 or i >= m or j < 0 or j >= n or tf_map[i][j]:
                return 0
            tf_map[i][j] = True
            cur_area = 1
            for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                cur_area += dfs(i + x, j + y)
            
            return cur_area
        
        maximum = 0
        for i in range(m):
            for j in range(n):
                if not tf_map[i][j]:
                    maximum = max(maximum, dfs(i, j))
                    
        return maximum
