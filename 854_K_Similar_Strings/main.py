from collections import deque


class Solution:
    def kSimilarity(self, A: str, B: str) -> int:
        i = 0
        queue = deque()
        queue.append((A, 0))
        visited = set()
        visited.add(A)
        while queue:
            cur, cnt = queue.popleft()
            if cur == B:
                return cnt
            i = 0
            while i < len(cur):
                if not cur[i] == B[i]:
                    break
                i += 1
            j = i + 1
            while j < len(cur):
                if cur[j] == B[i] and not B[j] == cur[j]:
                    tmp = cur[:i] + cur[j] + cur[i + 1: j] + cur[i] + cur[j + 1:]
                    if tmp not in visited:
                        visited.add(tmp)
                        queue.append((tmp, cnt + 1))
                j += 1

