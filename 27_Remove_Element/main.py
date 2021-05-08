class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        i, end = 0, n - 1
        while i <= end:
            while nums[i] == val and i <= end:
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            i += 1
        return end + 1

