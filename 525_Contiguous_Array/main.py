class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        sums, cur, ans = {0: -1}, 0, 0
        for i in range(n):
            cur += 1 if nums[i] else -1
            if cur not in sums:
                sums[cur] = i
            else:
                ans = max(ans, i - sums[cur])
        return ans

