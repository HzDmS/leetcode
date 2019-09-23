class Solution:
    def camelMatch(self, queries: List[str], pattern: str) -> List[bool]:
        ans = []
        for query in queries:
            i, j = 0, 0
            while i < len(query) and j < len(pattern):
                if query[i] == pattern[j]:
                    i += 1
                    j += 1
                elif query[i].isupper():
                    break
                else:
                    i += 1
            if j < len(pattern):
                ans.append(False)
            else:
                tmp = True
                while i < len(query):
                    if query[i].isupper():
                        tmp = False
                        break
                    i += 1
                ans.append(tmp)
        return ans
