class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        hold, maximum = float('inf'), 0
        for i in range(n):
            hold = min(hold, prices[i])
            maximum = max(maximum, prices[i] - hold)
        return maximum
        
