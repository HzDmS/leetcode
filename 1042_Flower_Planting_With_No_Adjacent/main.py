from collections import defaultdict


class Solution:
    def gardenNoAdj(self, N: int, paths: List[List[int]]) -> List[int]:
        ans = [0] * (N + 1)
        graph = defaultdict(set)
        for r, c in paths:
            graph[r].add(c)
            graph[c].add(r)
        
        for i in range(1, N + 1):
            colors = set()
            for neighbour in graph[i]:
                colors.add(ans[neighbour])
            for color in range(1, 5):
                if color in colors:
                    continue
                ans[i] = color
                break
        return ans[1:]
