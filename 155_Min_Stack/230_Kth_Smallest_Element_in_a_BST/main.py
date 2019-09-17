# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
          
        stack = []
        
        def inorder(node):
            if not node:
                return 0
            inorder(node.left)
            if len(stack) < k:
                stack.append(node.val)
            inorder(node.right)
        
        inorder(root)
        return stack[-1]
            
