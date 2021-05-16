# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.cnt = 0
    
    def goodNodes(self, root: TreeNode) -> int:
        self.dfs(root, -10001)
        return self.cnt
    
    def dfs(self, cur: TreeNode, maximum: int):
        if not cur:
            return
        if cur.val >= maximum:
            maximum = cur.val
            self.cnt += 1
        self.dfs(cur.left, maximum)
        self.dfs(cur.right, maximum)
