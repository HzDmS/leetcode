class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        if k > n / 2:
            return self.unlimited(prices)

        local = [0] * (k + 1)
        dp = [0] * (k + 1)
        for i in range(n - 1):
            diff = prices[i + 1] - prices[i]
            for j in range(k, 0, -1):
                local[j] = max(dp[j - 1] + max(0, diff), local[j] + diff)
                dp[j] = max(dp[j], local[j])
        return dp[k]
    
    def unlimited(self, prices: List[int]) -> int:
        profit = 0
        for i in range(len(prices) - 1):
            profit += max(0, prices[i + 1] - prices[i])
        return profit
