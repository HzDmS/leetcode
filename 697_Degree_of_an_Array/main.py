class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        cnt, left, right = {}, {}, {}
        for i, num in enumerate(nums):
            if num not in cnt:
                cnt[num] = 0
                left[num] = i
            cnt[num] += 1
            right[num] = i
        
        max_c = max(cnt.values())
        minimum = float('inf')
        for k, c in cnt.items():
            if c == max_c:
                minimum = min(minimum, right[k] - left[k] + 1)
        
        return minimum

