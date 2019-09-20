from collections import defaultdict


class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        E, F = defaultdict(int), defaultdict(int)
        for a in A:
            for b in B:
                E[a + b] += 1
                
        for c in C:
            for d in D:
                F[c + d] += 1
        ans = 0
        for e in E.keys():
            if 0 - e in F:
                ans += E[e] * F[0 - e]
        return ans
