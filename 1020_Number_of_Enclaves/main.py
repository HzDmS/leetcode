class Solution:
    
    def numEnclaves(self, A: List[List[int]]) -> int:
        m, n = len(A), len(A[0])
        
        def dfs(i, j):
            if A[i][j] == 0:
                return
            stack = []
            stack.append([i, j])
            while stack:
                x, y = stack.pop()
                A[x][y] = 0
                for a, b in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
                    new_x, new_y = x + a, y + b
                    if new_x >= 0 and new_x < m and new_y >= 0 and new_y < n and A[new_x][new_y] == 1:
                        stack.append([new_x, new_y])
                        
        border_slots = []
        border_slots.extend([[x, 0] for x in range(m)])
        border_slots.extend([[x, n - 1] for x in range(m)])
        border_slots.extend([[0, x] for x in range(n)])
        border_slots.extend([[m - 1, x] for x in range(n)])
        
        for i, j in border_slots:
            dfs(i, j)
        
        total = 0
        for i in range(m):
            total += sum(A[i])
            
        return total     
    
#     def numEnclaves(self, A: List[List[int]]) -> int:
#         m, n = len(A), len(A[0])
#         tf_map = [[True if x == 0 else False for x in row] for row in A]
#         def dfs(i, j):
#             if i < 0 or i >= m or j < 0 or j >= n:
#                 return 1, 0
#             if tf_map[i][j]:
#                 return 0, 0
            
#             tf_map[i][j] = True
#             flag, cnt = 0, 1
#             for x, y in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
#                 cur_f, cur_c = dfs(i + x, j + y)
#                 flag |= cur_f
#                 cnt += cur_c
            
#             return flag, cnt
        
#         total = 0
            
#         for i in range(m):
#             for j in range(n):
#                 flag, cnt = dfs(i, j)
#                 if not flag:
#                     total += cnt
        
#         return total
            
