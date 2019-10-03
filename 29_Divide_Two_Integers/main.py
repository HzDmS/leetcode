class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        INT_MAX = 2 ** 31 - 1
        neg = (dividend > 0 and divisor < 0) or (dividend < 0 and divisor > 0)
        dividend = abs(dividend)
        divisor = abs(divisor)
        ans = 0
        for i in range(31, -1, -1):
            if (dividend >> i) >= divisor:
                ans = ans + (1 << i)
                dividend = dividend - (divisor << i)
        if neg:
            ans = 0 - ans
        if ans > INT_MAX:
            return INT_MAX
        return ans

