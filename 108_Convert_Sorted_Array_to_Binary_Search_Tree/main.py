# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        return self.convert(0, len(nums) - 1, nums)
        
    def convert(self, start, end, nums):
        if start > end:
            return None
        mid = (start + end) // 2
        node = TreeNode(nums[mid])
        node.left = self.convert(start, mid - 1, nums)
        node.right = self.convert(mid + 1, end, nums)
        return node

