# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        
        if not root:
            return root
            
        stack, visited, prev = [], set(), 0
        stack.append(root)

        while stack:
            node = stack.pop()

            # if node is None, continue
            if not node:
                continue
            
            # if visited, update the values.
            if node in visited:
                node.val += prev
                prev = node.val
                continue
            
            # if not visited, visit this node.
            for next_node in [node.left, node, node.right]:
                stack.append(next_node)
            if node:
                visited.add(node)
                
        return root
        
#         def traversal(node, val):
#             if not node:
#                 return val
#             val = traversal(node.right, val)
#             node.val += val
#             val = traversal(node.left, node.val)
#             return val
        
#         traversal(root, 0)
        
#         return root
