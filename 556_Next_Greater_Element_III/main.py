class Solution:
    def nextGreaterElement(self, n: int) -> int:
        nums = list(str(n))
        i = len(nums) - 1
        while i > 0:
            if nums[i] > nums[i - 1]:
                break
            i -= 1
        if i == 0:
            return -1
        self.reverse(nums, i, len(nums) - 1)
        j = i
        while not nums[j] > nums[i - 1]:
            j += 1
        nums[i - 1], nums[j] = nums[j], nums[i - 1]
        tmp = int("".join(nums))
        return tmp if tmp < (1 << 31) else -1
        
    
    def reverse(self, nums, start, end):
        while not start >= end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
        
