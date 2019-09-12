from collections import defaultdict


class Solution:
    """
    @param source : A string
    @param target: A string
    @return: A string denote the minimum window, return "" if there is no such a string
    """
    def minWindow(self, source , target):
        target_map = defaultdict(int)
        for c in target:
            target_map[c] += 1
        
        n = len(source)
        
        source_map = defaultdict(int)
        matched = 0
        goal = len(target_map)
        ans = ""
        min_len = n + 1
        j = 0
        for i in range(n):
            while j < n and matched < goal:
                source_map[source[j]] += 1
                if source_map[source[j]] == target_map[source[j]]:
                    matched += 1
                j += 1
            if j - i < min_len and matched == goal:
                ans = source[i: j]
                min_len = len(ans)
            if source[i] in target_map:
                if source_map[source[i]] == target_map[source[i]]:
                    matched -= 1
                source_map[source[i]] -= 1
        
        return ans
            
