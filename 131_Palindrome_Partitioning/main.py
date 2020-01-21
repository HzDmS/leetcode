class Solution:
    
    def __init__(self):
        self.mem = set()
    
    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return []
        res = []
        self.dfs(0, [], s, res)
        return res
        
    def dfs(self, start, cur, s, res):
        if start >= len(s):
            res.append(cur)
            return
        for end in range(start, len(s)):
            if not self.isPalindrome(start, end, s):
                continue
            else:
                self.dfs(end + 1, cur + [s[start: end + 1]], s, res)
    
    def isPalindrome(self, x, y, s):
        if (x, y) in self.mem:
            return True
        else:
            i, j = x, y
            while i <= j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                else:
                    return False
            self.mem.add((x, y))
            return True

