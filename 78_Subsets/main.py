class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans
        
    def dfs(self, nums, start, cur, ans):
        ans.append(cur)
        for i in range(start, len(nums)):
            self.dfs(nums, i + 1, cur + [nums[i]], ans)

