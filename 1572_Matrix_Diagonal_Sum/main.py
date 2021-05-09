class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        n = len(mat)
        dsum, i = 0, 0
        for row in mat:
            if i != n - 1 - i:
                dsum = dsum + row[i] + row[n - 1 - i]
            else:
                dsum += row[i]
            i += 1
        return dsum

