from collections import defaultdict
import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        
        graph = defaultdict(list)
        for u, v, w in times:
            graph[u].append((v, w))
                
        dist = {}
        pq = [(0, K)]
        while pq:
            d, node = heapq.heappop(pq)
            if node in dist:
                continue
            dist[node] = d
            for nei, d2 in graph[node]:
                if nei not in dist:
                    heapq.heappush(pq, (d + d2, nei))
        return max(dist.values()) if len(dist) == N else -1
        
#         graph = defaultdict(list)
#         for i, j, w in times:
#             graph[i].append((w, j))
            
#         dist = {}
        
#         def dfs(i, time):
#             if i not in dist:
#                 dist[i] = float('inf')
#             if time >= dist[i]:
#                 return
#             dist[i] = time
#             for w, j in sorted(graph[i]):
#                 dfs(j, time + w)
            
#         dfs(K, 0)
#         if len(dist) < N:
#             return -1
#         ans = 0
#         for k, v in dist.items():
#             ans = max(ans, v)
#         return ans

