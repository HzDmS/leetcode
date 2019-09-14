from collections import defaultdict
from heapq import heapify
from heapq import heappop
from heapq import heappush


class Solution:
    """
    @param words: a list of words
    @return: a string which is correct order
    """
    def alienOrder(self, words):
        hashmap, ans, indegree = defaultdict(set), [], defaultdict(int)
        not_ordered = set()
        ordered = set()
        for i in range(len(words) - 1):
            j = 0
            first = True
            while j < max(len(words[i]), len(words[i + 1])):
                if first and not words[i][j] == words[i + 1][j]:
                    hashmap[words[i][j]].add(words[i + 1][j])
                    if words[i][j] not in indegree:
                        indegree[words[i][j]] = 0
                        ordered.add(words[i][j])
                    indegree[words[i + 1][j]] += 1
                    ordered.add(words[i + 1][j])
                    first = False
                else:
                    if j < len(words[i]):
                        not_ordered.add(words[i][j])
                    if j < len(words[i + 1]):
                        not_ordered.add(words[i + 1][j])
                j += 1
        total_len = len(indegree)
        rest = list(not_ordered.difference(ordered))

        queue = []
        for c, degree in indegree.items():
            if degree == 0:
                queue.append(c)
        heapify(queue)

        while queue:
            cur = heappop(queue)
            ans.append(cur)
            if cur not in hashmap:
                continue
            for nei in hashmap[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    heappush(queue, nei)
            hashmap.pop(cur)
        if len(ans) < total_len:
            return ""
        if rest:
            res = []
            rest = list(rest)
            i, j = 0, 0
            while i < len(ans) and j < len(rest):
                if ans[i] < rest[j]:
                    res.append(ans[i])
                    i += 1
                else:
                    res.append(rest[j])
                    j += 1
            if i < len(ans):
                res += ans[i:]
            if j < len(rest):
                res += rest[j:]
            return "".join(res)
        return "".join(ans)
