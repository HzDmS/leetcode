class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        missed = []
        for i in range(len(nums)):
            if nums[abs(nums[i]) - 1] > 0:
                nums[abs(nums[i]) - 1] *= -1
        for i, num in enumerate(nums):
            if num > 0:
                missed.append(i + 1)
        
        return missed
