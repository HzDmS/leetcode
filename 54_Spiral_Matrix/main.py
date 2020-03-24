class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        output = list()
        if not matrix:
            return output
        self.append(matrix, output, 0)
        return output
    
    def append(self, matrix: List[List[int]], output: List[int], cur: int) -> None:
        
        m, n = len(matrix), len(matrix[0])
        
        if cur > (min(m, n) - 1) // 2:
            return
        
        output.extend(matrix[cur][cur: n - cur])
        for i in range(cur + 1, m - cur):
            output.append(matrix[i][n - cur - 1])

        if cur == m // 2 or cur == n // 2:
            return

        output.extend(matrix[m - cur - 1][cur: n - cur - 1][::-1])
        for i in range(m - cur - 2, cur, -1):
            output.append(matrix[i][cur])
        
        self.append(matrix, output, cur + 1)
