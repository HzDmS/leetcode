# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        return self.buildTree(preorder, 0, len(preorder) - 1)
    
    def buildTree(self, preorder: List[int], start: int, end: int) -> TreeNode:
        
        if start > end:
            return None
        
        val = preorder[start]
        root = TreeNode(val)
        
        idx = start + 1
        while idx <= end:
            if preorder[idx] < val:
                idx += 1
            else:
                break
        root.left = self.buildTree(preorder, start + 1, idx - 1)
        root.right = self.buildTree(preorder, idx, end)
        return root

