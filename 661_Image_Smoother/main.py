class Solution:
    def imageSmoother(self, M: List[List[int]]) -> List[List[int]]:
        m, n = len(M), len(M[0])
        img = [[0] * n for _ in range(m)]
        
        dirs = [[1, 1], [1, -1], [0, 1], [0, -1],
                [-1, 1], [-1, -1], [1, 0], [-1, 0]]
        
        for i in range(m):
            for j in range(n):
                cnt, total = 1, M[i][j]
                for x, y in dirs:
                    p, q = i + x, j + y
                    if p >= 0 and p < m and q >= 0 and q < n:
                        cnt += 1
                        total += M[p][q]
                img[i][j] = total // cnt
        
        return img

