class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        low, high = 1, num // 2
        while low <= high:
            mid = (low + high) // 2
            if mid ** 2 < num:
                low = mid + 1
            else:
                high = mid - 1
        
        return low ** 2 == num
