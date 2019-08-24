# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    
    def tree2str(self, t: TreeNode) -> str:
        
        ret = ""
        if not t:
            return ret
        
        # DFS
        
        stack, visited = [], set()
        stack.append(t)
        
        while stack:
            top = stack[-1]
            if top in visited:
                stack.pop()
                if top is not t:
                    ret += ")"
                continue

            if not top:
                stack.pop()
                ret += "()"
                continue

            if top.right or top.left:
                if top.right:
                    stack.append(top.right)
                stack.append(top.left)
            if top is not t:
                ret += "("
            ret += str(top.val)
            if top:
                visited.add(top)
        
        return ret
            
        
    
    # def tree2str(self, t: TreeNode) -> str:
#         ret = []

         # Recursion
        
#         def preorder(node):
#             if not node:
#                 ret.append("()")
#                 return
#             ret.extend(["(", str(node.val)])
#             if node.left or node.right:
#                 preorder(node.left)
#                 if node.right:
#                     preorder(node.right)
#             ret.append(")")
        
#         preorder(t)
#         return "".join(ret[1:-1])
