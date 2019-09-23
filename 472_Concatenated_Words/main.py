class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        wordSet = set(words)
        ans = []
        for word in words:
            wordSet.remove(word)
            if self.isConcatenated(word, wordSet):
                ans.append(word)
            wordSet.add(word)
        return ans
    
    def isConcatenated(self, word, wordSet):
        n = len(word)
        if n == 0:
            return False
        dp = [False] * (n + 1)
        dp[0] = True
        for i in range(1, n + 1):
            for j in range(i - 1, -1, -1):
                if not dp[j]:
                    continue
                if word[j: i] in wordSet:
                    dp[i] = True
                    break
        return dp[n]
