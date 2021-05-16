from typing import Set

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class ResultType:
    
    def __init__(self, max_depth: int, node: TreeNode):
        self.max_depth = max_depth
        self.node = node

class Solution:
    
    def __init__(self):
        self.node = None
    
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        res = self.get_depth(root, 0)
        return res.node
        
    def get_depth(self, root: TreeNode, depth: int) -> ResultType:
        if not root:
            return ResultType(depth, None)
        
        left_res = self.get_depth(root.left, depth + 1)
        right_res = self.get_depth(root.right, depth + 1)
        
        if left_res.max_depth == right_res.max_depth:
            return ResultType(left_res.max_depth, root)
        
        if left_res.max_depth > right_res.max_depth:
            return left_res
        
        return right_res
