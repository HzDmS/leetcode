# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack, cur = [], root
        while stack or cur:
            while cur:
                ans.append(cur.val)
                if cur.right:
                    stack.append(cur.right)
                cur = cur.left
            if stack:
                cur = stack.pop()
        return ans
        
