class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i == 0:
            nums.sort()
        else:
            self.reverse(nums, i, n - 1)
            j = i
            while not nums[j] > nums[i - 1]:
                j += 1
            nums[j], nums[i - 1] = nums[i - 1], nums[j]
    
    def reverse(self, nums, i, j):
        while not i >= j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
