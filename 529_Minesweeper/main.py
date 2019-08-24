class Solution:
    def updateBoard(self, board: List[List[str]], click: List[int]) -> List[List[str]]:
        
        m, n = len(board), len(board[0])
        visited = set()
        
        def reveal(i, j):
            stack = []
            
            if board[i][j] == 'M':
                board[i][j] = 'X'
                return
            
            stack.append([i, j])
            visited.add((i, j))
            
            while stack:
                x, y = stack.pop()
                board[x][y] = 'B'
                
                # explore the surrounding squares, to see if there is any mine.
                for a, b in [[1, 0], [-1, 0], [0, 1], [0, -1],
                             [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                    new_x, new_y = x + a, y + b
                    if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                        continue
                    if (new_x, new_y) in visited:
                        continue
                    if board[new_x][new_y] == "M":
                        if board[x][y].isdigit():
                            board[x][y] = str(int(board[x][y]) + 1)
                        if board[x][y] == 'B':
                            board[x][y] = '1'

                # if no mine is around, explore the surrounding squares.
                if not board[x][y].isdigit():
                    for a, b in [[1, 0], [-1, 0], [0, 1], [0, -1],
                                 [1, 1], [1, -1], [-1, 1], [-1, -1]]:
                        new_x, new_y = x + a, y + b
                        if new_x < 0 or new_x >= m or new_y < 0 or new_y >= n:
                            continue
                        if (new_x, new_y) in visited:
                            continue
                        if board[new_x][new_y] == 'E':
                            stack.append([new_x, new_y])
                        visited.add((new_x, new_y))
        
        reveal(click[0], click[1])
        
        return board
