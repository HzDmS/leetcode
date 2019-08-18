from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        
        fresh, q, visited, length = set(), deque(), set(), 0
        m, n = len(grid), len(grid[0])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                if grid[i][j] == 2:
                    q.append((i, j))
                    visited.add((i, j))
                    
        if not fresh:
            return 0
        
        while q:
            
            for _ in range(len(q)):
                
                i, j = q.popleft()
                
                for a, b in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_i, new_j = i + a, j + b
                    if (new_i, new_j) in visited:
                        continue
                    if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n:
                        if not grid[new_i][new_j] == 0:
                            q.append((new_i, new_j))
                            fresh.remove((new_i, new_j))
                            visited.add((new_i, new_j))
                            
            length += 1
                            
            if not fresh:
                return length
            
        return -1
