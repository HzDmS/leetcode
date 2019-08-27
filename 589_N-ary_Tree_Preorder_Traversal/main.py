"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        
        ret = []
        
        if not root:
            return ret
        
        stack = []
        stack.append(root)
        
        while stack:
            node = stack.pop()
            ret.append(node.val)
            for i in range(len(node.children) - 1, -1, -1):
                stack.append(node.children[i])
        
        return ret
                
        
#         ret = []
        
#         def preorder(node):
#             if not node:
#                 return
#             ret.append(node.val)
#             for child in node.children:
#                 preorder(child)
                
#         preorder(root)
#         return ret
        
