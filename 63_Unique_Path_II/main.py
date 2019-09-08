class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        # dp solution
        # time: O(m * n)
        
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if obstacleGrid[i][j] == 1:
                    obstacleGrid[i][j] = 0
                elif i == m - 1 and j == n - 1:
                    obstacleGrid[i][j] = 1
                else:
                    if i == m - 1:
                        obstacleGrid[i][j] = obstacleGrid[i][j + 1]
                    elif j == n - 1:
                        obstacleGrid[i][j] = obstacleGrid[i + 1][j]
                    else:
                        obstacleGrid[i][j] = obstacleGrid[i + 1][j] + obstacleGrid[i][j + 1]
        return obstacleGrid[0][0]
        
        # dfs solution with memorization
        # time: O(m * n)
        # space: O(m * n)

#         m, n = len(obstacleGrid), len(obstacleGrid[0])
#         hashmap = {}
        
#         def dfs(i, j):
#             if i >= m or j >= n or obstacleGrid[i][j] == 1:
#                 return 0
#             elif i == m - 1 and j == n - 1:
#                 return 1
#             else:
#                 key = tuple([i, j])
#                 if key not in hashmap:
#                     ways = dfs(i + 1, j) + dfs(i, j + 1)
#                     hashmap[key] = ways
#                     return ways
#                 else:
#                     return hashmap[key]

#         return dfs(0, 0)
