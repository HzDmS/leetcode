# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        stack, cur, prev = [], root, float('-inf')
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            node = stack.pop()
            if node.val <= prev:
                return False
            prev = node.val
            cur = node.right
        return True


class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        return self.inorder(root, float('-inf'), float('inf'))
    
    def inorder(self, node, minimum, maximum):
        if not node:
            return True
        if node.val <= minimum or node.val >= maximum:
            return False
        if not self.inorder(node.left, minimum, node.val):
            return False
        if not self.inorder(node.right, node.val, maximum):
            return False
        return True

