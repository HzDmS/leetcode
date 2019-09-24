from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        queue = deque()
        for i in range(k - 1):
            self.push(queue, i, nums)
        ans = []
        for i in range(k - 1, len(nums)):
            self.push(queue, i, nums)
            ans.append(nums[queue[0]])
            if queue[0] == i - k + 1:
                queue.popleft()
        return ans
    
    def push(self, queue, i, nums):
        while queue and nums[queue[-1]] < nums[i]:
            queue.pop()
        queue.append(i)

