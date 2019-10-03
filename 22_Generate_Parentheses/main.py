class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        self.dfs(n, n, "", ans)
        return ans
        
    def dfs(self, l, r, cur, ans):
        if l > r:
            return
        if l == r == 0:
            ans.append(cur)
        if l > 0:
            self.dfs(l - 1, r, cur + "(", ans)
        if r > 0:
            self.dfs(l, r - 1, cur + ")", ans)

