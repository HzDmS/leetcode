from collections import deque


class Solution:
    
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        q = deque()
        visited = set()
        q.append((0, 0))
        
        while q:
            cnt, total = q.popleft()
            if total == amount:
                return cnt
            if total > amount:
                continue
            for coin in coins:
                if total + coin in visited:
                    continue
                visited.add(total + coin)
                q.append((cnt + 1, total + coin))
        return -1
