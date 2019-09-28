# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return self.depth(root)
        
    def depth(self, node):
        if not node:
            return 0
        lDepth = self.depth(node.left)
        rDepth = self.depth(node.right)
        return max(lDepth, rDepth) + 1

