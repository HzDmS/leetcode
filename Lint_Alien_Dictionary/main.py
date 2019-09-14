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
        unique = set()
        for i in range(len(words) - 1):
            j = 0
            first = True
            while j < max(len(words[i]), len(words[i + 1])):
                if first and not words[i][j] == words[i + 1][j]:
                    hashmap[words[i][j]].add(words[i + 1][j])
                    indegree[words[i + 1][j]] += 1
                    first = False
                if j < len(words[i]):
                    unique.add(words[i][j])
                if j < len(words[i + 1]):
                    unique.add(words[i + 1][j])
                j += 1
        total_len = len(indegree)

        queue = []
        for c in unique:
            if indegree[c] == 0:
                queue.append(c)
        heapify(queue)

        cnt = 0
        while queue:
            cur = heappop(queue)
            ans.append(cur)
            if cur not in hashmap:
                continue
            cnt += 1
            for nei in hashmap[cur]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    heappush(queue, nei)
            hashmap.pop(cur)
        if cnt < total_len:
            return ""
        return "".join(ans)
