class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        local = [0] * 3
        dp = [0] * 3
        for i in range(len(prices) - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(2, 0, -1):
                local[j] = max(dp[j - 1] + max(diff, 0), local[j] + diff)
                dp[j] = max(local[j], dp[j])
        return dp[2]
