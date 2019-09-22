class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []
        self.dfs(nums, 0, [], ans)
        return ans
        
    
    def dfs(self, nums, start, cur, ans):
        ans.append(cur)
        for i in range(start, len(nums)):
            if i > start and nums[i - 1] == nums[i]:
                continue
            self.dfs(nums, i + 1, cur + [nums[i]], ans)

