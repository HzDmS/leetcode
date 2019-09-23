class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        visited = {}
        ans = []
        self.dfs(0, [], s, wordDict, visited, ans)
        return ans
        
    def dfs(self, start, sentence, s, wordDict, visited, ans):
        if start >= len(s):
            ans.append(" ".join(sentence))
            return True
        cur = ""
        res = False
        for i in range(start, len(s)):
            cur += s[i]
            if cur not in wordDict:
                continue
            if i + 1 in visited and not visited[i + 1]:
                continue
            sentence.append(cur)
            res = self.dfs(i + 1, sentence, s, wordDict, visited, ans)
            sentence.pop()
        visited[start] = res
        return res     

