# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        
        # time complexity: O(#Node)
        # space complexity: O(1)
        
        # core idea: on each path from the root to a leaf, V = |max_val - min_val|.
        # go througn all paths from the root to the leaves, and return the maximum.
        
        def dfs(node, min_val, max_val):
            if not node:
                return abs(min_val - max_val)
            min_val = min(node.val, min_val)
            max_val = max(node.val, max_val)
            l_max = dfs(node.left, min_val, max_val)
            r_max = dfs(node.right, min_val, max_val)
            
            return max([l_max, r_max])
        return dfs(root, root.val, root.val)
            
        
#     def maxAncestorDiff(self, root: TreeNode) -> int:
        
#         stack = []
        
#         def dfs(node):
            
#             if not node:
#                 return 0
            
#             stack.append(node.val)
#             l_max = dfs(node.left)
#             r_max = dfs(node.right)
#             cur = stack.pop()
            
#             cur_max = 0
#             for val in stack:
#                 cur_max = max(cur_max, abs(val - cur))
            
#             return max([cur_max, l_max, r_max])
        
#         maximum = dfs(root)
#         return maximum
