"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""

class Solution:
    """
    @param root: the root of binary tree
    @return: the length of the longest consecutive sequence path
    """
    def longestConsecutive(self, root):
        # write your code here
        self.max = 0
        _ = self.traversal(root)
        return self.max
    
    def traversal(self, node):
        if not node:
            return 0
        left = self.traversal(node.left)
        right = self.traversal(node.right)
        cur = 0
        if node.left and node.val == node.left.val - 1:
            cur = max(cur, left)
        if node.right and node.val == node.right.val - 1:
            cur = max(cur, right)
        cur += 1
        self.max = max(self.max, cur)
        return cur

