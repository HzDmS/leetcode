# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.current_level = 0
        self.sum = 0
    
    def deepestLeavesSum(self, root: TreeNode) -> int:
        self.traverse(root, 0)
        return self.sum
        
    def traverse(self, root: TreeNode, level: int) -> None:
        if not root:
            return
        if self.current_level < level:
            self.current_level += 1
            self.sum = root.val
        elif self.current_level == level:
            self.sum += root.val
        else:
            pass
        self.traverse(root.left, level + 1)
        self.traverse(root.right, level + 1)
        
        
