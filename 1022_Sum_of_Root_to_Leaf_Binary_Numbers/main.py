# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        values = []
        
        def helper(node):
            values.append(str(node.val))
            total = 0
            if node.left or node.right:
                for child in [node.left, node.right]:
                    if child:
                        total += helper(child)
                        values.pop()
                return total
            else:
                return int(''.join(values), 2)
        
        return helper(root)
        
