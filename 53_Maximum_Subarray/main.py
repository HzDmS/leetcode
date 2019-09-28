class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans, tmp = -float("inf"), -float("inf")
        for num in nums:
            tmp = max(tmp + num, num)
            ans = max(ans, tmp)
        return ans
