# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        ans = []
        stack, cur = [], root
        while stack or cur:
            while cur:
                if cur.right:
                    stack.append(cur.right)
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.right and self.peek(stack) == cur.right:
                stack.pop()
                stack.append(cur)
                cur = cur.right
            else:
                ans.append(cur.val)
                cur = None
        return ans
    
    def peek(self, stack):
        if stack:
            return stack[-1]
        return None

