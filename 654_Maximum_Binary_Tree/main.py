# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if len(nums) == 0:
            return None
        idx, maximum = self.findMaximum(nums)
        root = TreeNode(maximum)
        root.left = self.constructMaximumBinaryTree(nums[:idx])
        root.right = self.constructMaximumBinaryTree(nums[(idx + 1):])
        return root
    
    def findMaximum(self, nums: List[int]) -> Tuple[int, int]:
        idx, maximum = 0, nums[0]
        for i, num in enumerate(nums):
            if num > maximum:
                idx = i
                maximum = num
        return idx, maximum

