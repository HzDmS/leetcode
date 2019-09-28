# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        return self.merge(t1, t2)
    
    def merge(self, node1, node2):
        if node1 and node2:
            merged = TreeNode(node1.val + node2.val)
            merged.left = self.merge(node1.left, node2.left)
            merged.right = self.merge(node1.right, node2.right)
            return merged
        elif not node1 and node2:
            return node2
        elif node1 and not node2:
            return node1
        else:
            return None

