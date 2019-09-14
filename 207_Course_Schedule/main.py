from collections import defaultdict
from collections import deque


class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         graph = defaultdict(set)
#         indegree = defaultdict(int)
#         for start, end in prerequisites:
#             graph[start].add(end)
#             if start not in indegree:
#                 indegree[start] = 0
#             indegree[end] += 1
        
#         queue = deque()
#         for i in range(numCourses):
#             if indegree[i] == 0:
#                 queue.append(i)
#         total_len = len(indegree)
        
#         cnt = 0
#         while queue:
#             node = queue.popleft()
#             if node in indegree:
#                 cnt += 1
#             for end in graph[node]:
#                 indegree[end] -= 1
#                 if indegree[end] == 0:
#                     queue.append(end)
#             graph.pop(node)
            
#         return cnt == total_len
        
            
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        for start, end in prerequisites:
            graph[start].add(end)
        
        def dfs(i):
            if i in visited:
                return False
            else:
                cycle = True
                if i not in graph:
                    return cycle
                if i in mem:
                    return mem[i]
                visited.add(i)
                for end in graph[i]:
                    cycle = cycle and dfs(end)
                mem[i] = cycle
                visited.remove(i)
                return cycle
        
        ans = True
        mem = {}
        for i in graph.keys():
            visited = set()
            ans = ans and dfs(i)
        return ans
