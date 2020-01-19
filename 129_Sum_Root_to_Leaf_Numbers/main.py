# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def __init__(self):
        self.sum = 0

    def sumNumbers(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.dfs(root, '')
        return self.sum
    
    def dfs(self, node, cur):
        if not node:
            return
        if not node.left and not node.right:
            self.sum += int(cur + str(node.val))
            return
        self.dfs(node.left, cur + str(node.val))
        self.dfs(node.right, cur + str(node.val))

