# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        
        hashmap = defaultdict(int)
        
        def preorder(node, level):
            if not node:
                return
            else:
                preorder(node.left, level + 1)
                hashmap[level] += node.val
                preorder(node.right, level + 1)
        
        preorder(root, 1)
        
        max_k, max_v = 0, 0
        for k, v in hashmap.items():
            if v > max_v:
                max_k, max_v = k, v
        return max_k
        
