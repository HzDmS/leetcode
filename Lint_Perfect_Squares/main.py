from collections import deque

import math


class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        nums = self.perfectSquares(n)
        cnt = 0
        queue, visited = deque(), set()
        queue.append(n)
        visited.add(n)
        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur == 0:
                    return cnt
                else:
                    for num in nums:
                        if cur - num >= 0 and (cur - num) not in visited:
                            queue.append(cur - num)
                            visited.add(cur - num)
            cnt += 1
        return cnt
        
    def perfectSquares(self, n):
        nums = []
        i = 1
        while i <= math.sqrt(n):
            nums.append(i ** 2)
            i += 1
        return nums

