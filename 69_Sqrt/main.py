class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0 or x == 1:
            return x
        if x == 2 or x == 3:
            return 1
        l, r = 1, x // 2 + 1
        while l < r - 1:
            m = l + (r - l) // 2
            cur = m ** 2
            if cur == x:
                return m
            if cur < x:
                l = m
            else:
                r = m
        return l
        
