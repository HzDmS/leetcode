class Solution:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        start, cur_end, next_end = 0, 0, 0
        while start <= next_end:
            for i in range(start, cur_end + 1):
                next_end = max(next_end, i + nums[i])
            if next_end >= n - 1:
                return True
            start = cur_end + 1
            cur_end = next_end
        return False

