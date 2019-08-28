class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        left, right, n, maximum = 0, 0, len(nums), 0
        while right < n:
            if nums[right] == 0:
                maximum = max(maximum, right - left)
                right += 1
                left = right
            else:
                right += 1
        if not right == left:
            maximum = max(maximum, right - left)
        return maximum
