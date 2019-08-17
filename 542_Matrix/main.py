import queue


class Solution:
    
    def updateMatrix(self, matrix):
        
        m, n = len(matrix), len(matrix[0])
        dp = [[float('inf') for i in range(n)] for j in range(m)]
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    dp[i][j] = 0
                else:
                    if i > 0:
                        dp[i][j] = min(dp[i][j], dp[i - 1][j] + 1)
                    if j > 0:
                        dp[i][j] = min(dp[i][j], dp[i][j - 1] + 1)
        
        for i in range(m - 1, -1 ,-1):
            for j in range(n - 1, -1, -1):
                if i < m - 1:
                    dp[i][j] = min(dp[i][j], dp[i + 1][j] + 1)
                if j < n - 1:
                    dp[i][j] = min(dp[i][j], dp[i][j + 1] + 1)
                        
        return dp
        


# class Solution:
#     def updateMatrix(self, matrix):
        
#         m, n = len(matrix), len(matrix[0])
#         distance = [[float('inf') for i in range(n)] for j in range(m)]
        
#         if m == 0:
#             return matrix
        
#         q = queue.Queue()
        
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] == 0:
#                     distance[i][j] = 0
#                     q.put([i, j])
        
#         directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        
#         while not q.empty():
#             i, j = q.get()
#             for direction in directions:
#                 new_i, new_j = i + direction[0], j + direction[1]
#                 if new_i >= 0 and new_i < m and new_j >= 0 and new_j < n:
                    
#                     if distance[new_i][new_j] > distance[i][j] + 1:
#                         distance[new_i][new_j] = distance[i][j] + 1
#                         q.put([new_i, new_j])
                        
#         return distance
        
        
