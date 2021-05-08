class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i, j = 0, 0
        cur, cnt = nums[0], 0
        while j < n:
            if cur == nums[j]:
                if cnt < 2:
                    nums[i], nums[j] = nums[j], nums[i]
                    cnt += 1
                    i += 1
                j += 1
            else:
                cur = nums[j]
                cnt = 0
        return i

