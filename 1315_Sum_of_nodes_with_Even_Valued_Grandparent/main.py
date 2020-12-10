# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        res = 0
        if root is None:
            return res
        if root.val & 1 == 0:`
            res += self.sumChildren(root)
        if root.left:
            res += self.sumEvenGrandparent(root.left)
        if root.right:
            res += self.sumEvenGrandparent(root.right)
        return res

    def sumChildren(self, root: TreeNode) -> int:
        res = 0
        if root.left:
            res += self.sumGrandChildren(root.left)
        if root.right:
            res += self.sumGrandChildren(root.right)
        return res

    def sumGrandChildren(self, root: TreeNode) -> int:
        res = 0
        if root.left:
            res += root.left.val
        if root.right:
            res += root.right.val
        return res

