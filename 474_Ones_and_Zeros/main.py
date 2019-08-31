class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        dp[m][n] = 0
        
        for i, s in enumerate(strs):
            p, q = s.count("0"), s.count("1")
            for j in range(m, p - 1, -1):
                for k in range(n, q - 1, -1):
                    dp[j][k] = max(dp[j][k], dp[j - p][k - q] + 1)
                    if i == len(strs) - 1:
                        break
        return dp[m][n]
