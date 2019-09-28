class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        global_sum, global_diff = 0, float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            local_target = target - nums[i]
            local_sum, local_diff = 0, float('inf')
            while left < right:
                cur_sum = nums[left] + nums[right]
                cur_diff = abs(cur_sum - local_target)
                if cur_diff < local_diff:
                    local_sum = nums[left] + nums[right]
                    local_diff = cur_diff
                if cur_sum > local_target:
                    right -= 1
                else:
                    left += 1
            if local_diff < global_diff:
                global_sum = nums[i] + local_sum
                global_diff = local_diff
        return global_sum

