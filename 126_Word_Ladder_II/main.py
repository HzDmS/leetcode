from collections import defaultdict, deque


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        wordDict = defaultdict(list)
        for word in wordList + [beginWord]:
            for i in range(len(word)):
                key = word[:i] + "*" + word[i + 1:]
                wordDict[key].append(word)
        distance = self.bfs(endWord, wordDict)
        ans = []
        visited = set()
        self.dfs(beginWord, endWord, [beginWord], distance, visited, wordDict, ans)
        return ans
        
    def bfs(self, endWord, wordDict):
        distance = {endWord: 0}
        queue = deque()
        queue.append((endWord, 0))
        while queue:
            cur, dist = queue.popleft()
            for i in range(len(cur)):
                key = cur[:i] + "*" + cur[i + 1:]
                for nex in wordDict[key]:
                    if nex not in distance:
                        dist_nex = dist + 1
                        distance[nex] = dist_nex
                        queue.append((nex, dist_nex))
        return distance
    
    def dfs(self, cur, endWord, path, distance, visited, wordDict, ans):
        if cur == endWord:
            ans.append(path)
            return
        visited.add(cur)
        for i in range(len(cur)):
            key = cur[:i] + "*" + cur[i + 1:]
            for nex in wordDict[key]:
                if nex in visited or not distance[nex] == distance[cur] - 1:
                    continue
                else:
                    self.dfs(nex, endWord, path + [nex], distance, visited, wordDict, ans)
        visited.remove(cur)

