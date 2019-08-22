# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None


class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:
        
        def dfs(node, depth):

            if not node:
                return depth - 1, None

            l_depth, l_node = dfs(node.left, depth + 1)
            r_depth, r_node = dfs(node.right, depth + 1)
            
            # if imbalanced, return the side which is deepest.
            if l_depth < r_depth:
                return r_depth, r_node
            elif l_depth > r_depth:
                return l_depth, l_node
            else:
                # all leaves and balanced node
                return l_depth, node

        depth, node = dfs(root, 0)
        
        return node
        
