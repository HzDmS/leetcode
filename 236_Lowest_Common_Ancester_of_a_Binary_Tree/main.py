# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        self.ans = None
        _ = self.postOrder(root, p, q)
        return self.ans
        
    def postOrder(self, node, p, q):
        if not node:
            return 0
        left = self.postOrder(node.left, p, q)
        right = self.postOrder(node.right, p, q)
        mid = 0
        if node == p or node == q:
            mid = 1
        total = left + right + mid
        if not self.ans and total == 2:
            self.ans = node
        return total

