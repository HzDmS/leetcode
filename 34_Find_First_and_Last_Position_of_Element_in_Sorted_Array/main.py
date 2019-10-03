class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.searchLeft(nums, 0, len(nums) - 1, target)
        right = self.searchRight(nums, 0, len(nums) - 1, target)
        return [left, right]

    
    def searchLeft(self, nums, l, r, target):
        if l > r:
            return -1
        mid = l + (r - l) // 2
        if nums[mid] == target:
            if mid > 0 and nums[mid - 1] < target:
                return mid
            elif mid == 0:
                return mid
            else:
                return self.searchLeft(nums, l, mid - 1, target)
        if nums[mid] > target:
            return self.searchLeft(nums, l, mid - 1, target)
        if nums[mid] < target:
            return self.searchLeft(nums, mid + 1, r, target)
        
    def searchRight(self, nums, l, r, target):
        if l > r:
            return -1
        mid = l + (r - l) // 2
        if nums[mid] == target:
            if mid < len(nums) - 1 and nums[mid + 1] > target:
                return mid
            elif mid == len(nums) - 1:
                return mid
            else:
                return self.searchRight(nums, mid + 1, r, target)
        if nums[mid] > target:
            return self.searchRight(nums, l, mid - 1, target)
        if nums[mid] < target:
            return self.searchRight(nums, mid + 1, r, target)
        
