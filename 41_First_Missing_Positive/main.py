class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            while not nums[i] - 1 == i and nums[i] > 0:
                if nums[i] - 1 < len(nums) and not nums[nums[i] - 1] == nums[i]:
                    tmp = nums[nums[i] - 1]
                    nums[nums[i] - 1] = nums[i]
                    nums[i] = tmp
                else:
                    nums[i] = 0
        for i in range(len(nums)):
            if nums[i] <= 0:
                return i + 1
        return len(nums) + 1

