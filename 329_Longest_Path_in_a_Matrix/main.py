class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        
        if not matrix or not matrix[0]:
            return 0
        
        m, n = len(matrix), len(matrix[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        def dfs(i, j):
            if (i, j) in mem:
                return mem[(i, j)]
            visited.add((i, j))
            tmp = 1
            for x, y in dirs:
                ni, nj = i + x, j + y
                if ni < 0 or ni >= m or nj < 0 or nj >= n or (ni, nj) in visited:
                    continue
                if matrix[ni][nj] > matrix[i][j]:
                    tmp = max(tmp, dfs(ni, nj) + 1)
            mem[(i, j)] = tmp
            visited.remove((i, j))
            return tmp
        
        ans = 0
        mem = {}
        for i in range(m):
            for j in range(n):
                visited = set()
                ans = max(dfs(i, j), ans)
                
        return ans

