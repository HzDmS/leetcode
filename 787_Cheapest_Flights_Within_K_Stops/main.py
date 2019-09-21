import heapq

from collections import defaultdict


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        graph = defaultdict(list)
        for i, j, k in flights:
            graph[i].append((j, k))
        queue = [(0, src, -1)]
        while queue:
            fee, node, conn = heapq.heappop(queue)
            if node == dst:
                return fee
            if conn == K:
                continue
            for nei, w in graph[node]:
                heapq.heappush(queue, (fee + w, nei, conn + 1))
        return -1

