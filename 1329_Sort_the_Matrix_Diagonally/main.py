class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        for i in range(m):
            elements = self.extractDiagonal(i, 0, mat)
            elements.sort()
            self.insertDiagonal(i, 0, mat, elements)
        for j in range(1, n):
            elements = self.extractDiagonal(0, j, mat)
            elements.sort()
            self.insertDiagonal(0, j, mat, elements)
        return mat
    
    def insertDiagonal(self, i: int, j: int, mat: List[List[int]], elements: List[int]) -> None:
        m, n = len(mat), len(mat[0])
        for idx, element in enumerate(elements):
            mat[i + idx][j + idx] = element
    
    def extractDiagonal(self, i: int, j: int, mat: List[List[int]]) -> List:
        elements = []
        m, n = len(mat), len(mat[0])
        while i < m and j < n:
            elements.append(mat[i][j])
            i += 1
            j += 1
        return elements

