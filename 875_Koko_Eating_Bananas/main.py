class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        low, high = 1, max(piles)
        while low < high:
            mid = low + (high - low) // 2
            time = sum(map(lambda x: x // mid if x % mid == 0 else x // mid + 1, piles))
            if time > h:
                low = mid + 1
            elif time < h:
                high = mid
            else:
                return mid
        return low

