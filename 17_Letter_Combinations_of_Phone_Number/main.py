class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        if not digits:
            return res

        letters = ['abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
        mapping = {}
        for i in range(8):
            mapping[str(i + 2)] = letters[i]
        self.dfs('', 0, mapping, digits, res)
        return res
        
    
    def dfs(self, cur, i, mapping, digits, res):
        if i == len(digits):
            res.append(cur)
            return

        for letter in mapping[digits[i]]:
            self.dfs(cur + letter, i + 1, mapping, digits, res)
            
            
        
