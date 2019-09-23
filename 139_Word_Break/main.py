class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i):
                if s[j: i] in wordDict:
                    dp[i] = dp[j]
                if dp[i]: break
        return dp[n]
                    

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordDict = set(wordDict)
        visited = set()
        return self.dfs(0, s, wordDict, visited)
        
    def dfs(self, start, s, wordDict, visited):
        if start >= len(s):
            return True
        cur = ""
        visited.add(start)
        for i in range(start, len(s)):
            cur += s[i]
            if cur not in wordDict:
                continue
            else:
                if i + 1 in visited:
                    continue
                else:
                    if self.dfs(i + 1, s, wordDict, visited):
                        return True
        return False
