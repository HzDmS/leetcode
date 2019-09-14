from collections import Counter, defaultdict


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        ans, ans_len = "", float("inf")
        target_cnt = Counter(t)
        cur_cnt = defaultdict(int)
        filtered = []
        for i, c in enumerate(s):
            if c in target_cnt:
                filtered.append((c, i))
        
        left, right, matched, goal = 0, 0, 0, len(target_cnt)
        while right < len(filtered):
            rc = filtered[right][0]
            cur_cnt[rc] += 1
            if cur_cnt[rc] == target_cnt[rc]:
                matched += 1
            while left <= right and matched == goal:
                end = filtered[right][1]
                start = filtered[left][1]
                lc = filtered[left][0]
                if end - start + 1 < ans_len:
                    ans = s[start: end + 1]
                    ans_len = end - start + 1
                cur_cnt[lc] -= 1
                if cur_cnt[lc] < target_cnt[lc]:
                    matched -= 1
                left += 1
            right += 1
        return ans

