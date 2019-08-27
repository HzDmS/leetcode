class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        sorted_heights = sorted(heights)
        for x, y in zip(heights, sorted_heights):
            if not x == y:
                count += 1
        
        return count
        
