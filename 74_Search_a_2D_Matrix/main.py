class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        if target < matrix[0][0] or target > matrix[m - 1][n - 1]:
            return False
        i = self.bin_search_col(matrix, target, 0, m - 1)
        return self.bin_search_row(matrix[i], target, 0, n - 1)
        
    def bin_search_col(self, matrix: List[List[int]], target: int, low: int, high: int):
        
        if low == high or low == high - 1:
            return low if target < matrix[high][0] else high

        mid = (low + high) // 2

        if matrix[mid][0] > target:
            return self.bin_search_col(matrix, target, low, mid - 1)
        elif matrix[mid][0] == target:
            return mid
        else:
            return self.bin_search_col(matrix, target, mid, high)
        
    def bin_search_row(self, row: List[int], target: int, low: int, high: int):
        if low >= high:
            return row[low] == target

        mid = (low + high) // 2
        if row[mid] > target:
            return self.bin_search_row(row, target, low, mid - 1)
        elif row[mid] == target:
            return True
        else:
            return self.bin_search_row(row, target, mid + 1, high)

