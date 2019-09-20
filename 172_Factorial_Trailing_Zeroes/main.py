class Solution:
    def trailingZeroes(self, n: int) -> int:
        ans = 0
        base = 5
        while n // base:
            ans += n // base
            base *= 5
        return ans
        
