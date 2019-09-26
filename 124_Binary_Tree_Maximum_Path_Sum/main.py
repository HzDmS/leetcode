# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.ans = -float('inf')
        _ = self.pathSum(root)
        return self.ans
        
    def pathSum(self, node):
        if not node:
            return -float('inf')
        l = self.pathSum(node.left)
        r = self.pathSum(node.right)
        self.ans = max(self.ans, max(l, 0) + max(r, 0) + node.val)
        return max([l, r, 0]) + node.val

