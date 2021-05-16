class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = {}
        for i, ID in enumerate(manager):
            if ID not in graph:
                graph[ID] = []
            graph[ID].append(i)
        return self.dfs(graph, headID, informTime)
        
    def dfs(self, graph, cur, informTime):
        subordinates = graph.get(cur, None)
        if not subordinates:
            return 0
        total = 0
        for subordinate in subordinates:
            total = max(total, self.dfs(graph, subordinate, informTime))
        return total + informTime[cur]
        
