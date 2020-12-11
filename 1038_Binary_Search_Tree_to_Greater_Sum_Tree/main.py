# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.traverse(root, 0)
        return root
        
    def traverse(self, root: TreeNode, val: int) -> int:
        if root is None:
            return val
        cur = self.traverse(root.right, val)
        root.val += cur
        cur = self.traverse(root.left, root.val)
        return cur

