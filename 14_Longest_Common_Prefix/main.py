class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        cur = strs[0]
        for string in strs:
            cur = self.find(cur, string)
            if cur == "":
                break
        return cur
    
    @staticmethod
    def find(a, b):
        i = 0
        while i < min(len(a), len(b)):
            if not a[i] == b[i]:
                break
            i += 1
        return a[:i]
                    
