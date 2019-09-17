class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [0] * n
        ans[0] = nums[0]
        for i in range(1, n - 1):
            ans[i] = ans[i - 1] * nums[i]
        ans[n - 1] = ans[n - 2]
        backward = nums[-1]
        for j in range(n - 2, 0, -1):
            ans[j] = ans[j - 1] * backward
            backward = backward * nums[j]
        ans[0] = backward
        return ans     
            
