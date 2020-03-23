class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return None

        m, n = len(board), len(board[0])
        for i in range(m):
            self.dfs(board, i, 0)
            self.dfs(board, i, n - 1)
        for j in range(n):
            self.dfs(board, 0, j)
            self.dfs(board, m - 1, j)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'
                else:
                    continue

    def dfs(self, board: List[List[str]], i, j) -> None:
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return
        if board[i][j] == 'X' or board[i][j] == 'T':
            return
        if board[i][j] == 'O':
            board[i][j] = 'T'
        for x, y in ((1, 0), (-1, 0), (0, 1), (0, -1)):
            self.dfs(board, i + x, j + y)
   
