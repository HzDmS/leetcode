import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        nums = []
        visited = set()
        queue = [1]
        
        while queue:
            node = heapq.heappop(queue)
            if len(nums) == n:
                break
            nums.append(node)
            for d in [2, 3, 5]:
                idx = node * d
                if idx not in visited:
                    heapq.heappush(queue, idx)
                    visited.add(idx)
        return nums[-1]

