from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents = [*range(len(edges) + 1)]
        ranks = [0] * (len(edges) + 1)
        
        def find(x):
            if not parents[x] == x:
                parents[x] = find(parents[x])
            return parents[x]
        
        def union(x, y):
            x_r, y_r = find(x), find(y)
            if x_r == y_r:
                return False
            elif ranks[x_r] < ranks[y_r]:
                parents[x_r] = y_r
            elif ranks[x_r] > ranks[y_r]:
                parents[y_r] = x_r
            else:
                parents[y_r] = x_r
                ranks[x_r] += 1
            return True
        
        for edge in edges:
            if not union(*edge):
                return edge


if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantConnection([[1,2], [2,3], [3,4], [1,4], [1,5]]))