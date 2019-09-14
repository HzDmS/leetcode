# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        
        def build(inorder, postorder, stop):
            if inorder[-1] == stop:
                return None
            val = postorder.pop()
            node = TreeNode(val)
            node.right = build(inorder, postorder, val)
            inorder.pop()
            node.left = build(inorder, postorder, stop)
            return node
        
        return build([None] + inorder, postorder, None)

#         def build(inorder, postorder):
#             if not postorder:
#                 return None
#             val = postorder[-1]
#             node = TreeNode(val)
#             i = inorder.index(val)
#             node.left = build(inorder[:i], postorder[:i])
#             node.right = build(inorder[i + 1:], postorder[i: -1])
#             return node
        
#         return build(inorder, postorder)

