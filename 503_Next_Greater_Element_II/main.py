class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        hashmap = {}
        n = len(nums)
        for k in range(2):
            for i in range(n):
                while stack and nums[i] > nums[stack[-1]]:
                    hashmap[stack.pop()] = nums[i]
                if k == 0:
                    stack.append(i)
        while stack:
            hashmap[stack.pop()] = -1
        for i in range(n):
            nums[i] = hashmap[i]
        return nums

