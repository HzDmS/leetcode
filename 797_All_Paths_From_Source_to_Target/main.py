class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        paths = []
        self.dfs(graph, 0, [], paths)
        return paths
        
    def dfs(self, graph: List[List[int]], cur: int, path: List[int], paths: List[List[int]]):
        
        if cur == len(graph) - 1:
            paths.append(path + [cur])
            return
        for neighbor in graph[cur]:
            self.dfs(graph, neighbor, path + [cur], paths)

