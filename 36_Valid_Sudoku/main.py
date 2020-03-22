class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            if not self.isValidSet(i, i, 0, 8, board) or not self.isValidSet(0, 8, i, i, board):
                return False
        for i in range(3):
            for j in range(3):
                if not self.isValidSet(i * 3, (i + 1) * 3 - 1, j * 3, (j + 1) * 3 - 1, board):
                    return False
        return True
    
    def isValidSet(
        self,
        row_start: int,
        row_end: int,
        col_start: int,
        col_end: int,
        board: List[List[int]]
    ) -> bool:
        nums = set()
        for i in range(row_start, row_end + 1):
            for j in range(col_start, col_end + 1):
                if board[i][j] == ".":
                    continue
                if int(board[i][j]) < 1 or int(board[i][j]) > 9 or int(board[i][j]) in nums:
                    return False
                nums.add(int(board[i][j]))
        return True
        
