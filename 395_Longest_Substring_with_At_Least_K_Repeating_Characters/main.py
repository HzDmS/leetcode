import heapq

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        cnt = dict()
        for c in s:
            if c not in cnt:
                cnt[c] = 0
            cnt[c] += 1
        
        for c in s:
            if cnt[c] < k:
                return max(self.longestSubstring(cur, k) for cur in s.split(c))
        return len(s)

