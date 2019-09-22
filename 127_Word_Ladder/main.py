from collections import deque, defaultdict


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        if not beginWord or not endWord or not wordList or endWord not in wordList:
            return 0
        
        self.wordMap = defaultdict(list)
        for word in wordList:
            for i in range(len(beginWord)):
                self.wordMap[word[:i] + "*" + word[(i + 1):]].append(word)
        
        queue, queue_ = deque(), deque()
        queue.append((beginWord, 1))
        queue_.append((endWord, 1))
        visited, visited_ = {beginWord: 1}, {endWord: 1}
        
        while queue and queue_:
            tmp = self.visit(queue, visited, visited_)
            if tmp:
                return tmp
            tmp = self.visit(queue_, visited_, visited)
            if tmp:
                return tmp
        
        return 0
        
        
    def visit(self, queue, visited, visited_):
        cur, cnt = queue.popleft()
        for i in range(len(cur)):
            key = cur[:i] + "*" + cur[i + 1:]
            for nex in self.wordMap[key]:
                if nex in visited_:
                    return cnt + visited_[nex]
                if nex not in visited:
                    queue.append((nex, cnt + 1))
                    visited[nex] = cnt + 1
        return None


# class Solution:
#     def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
#         wordMap = defaultdict(list)
#         for word in wordList:
#             for i in range(len(beginWord)):
#                 wordMap[word[:i] + "*" + word[(i + 1):]].append(word)
        
#         queue = deque()
#         queue.append((beginWord, 1))
#         visited = set()
#         visited.add(beginWord)

#         while queue:
#             cur, cnt = queue.popleft()
#             if cur == endWord:
#                 return cnt
#             for i in range(len(cur)):
#                 key = cur[:i] + "*" + cur[(i + 1):]
#                 for nex in wordMap[key]:
#                     if nex not in visited:
#                         queue.append((nex, cnt + 1))
#                         visited.add(nex)

#         return 0
