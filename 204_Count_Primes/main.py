import math


class Solution:
    def countPrimes(self, n: int) -> int:
        
        ans = 0
        composite = [False] * n
        for i in range(2, n):
            if not composite[i]:
                ans += 1
                for j in range(2, n):
                    if i * j >= n:
                        break
                    else:
                        composite[i * j] = True
        return ans

