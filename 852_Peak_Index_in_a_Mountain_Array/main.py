class Solution:
    def peakIndexInMountainArray(self, A: List[int]) -> int:
        low, high = 0, len(A) - 1
        
        while low < high - 1:
            mid = (low + high) // 2
            if A[mid - 1] < A[mid] and A[mid] < A[mid + 1]:
                low = mid
            elif A[mid - 1] > A[mid] and A[mid] > A[mid + 1]:
                high = mid
            else:
                return mid
        
        # while low < high:
        #     mid = (low + high) // 2
        #     if A[mid] < A[mid + 1]:
        #         low = mid + 1
        #     else:
        #         high = mid
        # return low
