# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:
        
        q, leftmost, cur_node = deque(), 0, None
        q.append(root)
        
        while q:
            
            for n in range(len(q)):
                
                node = q.popleft()
                if n == 0:
                    cur_node = node
                
                for new_node in [node.left, node.right]:
                    if new_node:
                        q.append(new_node)
            
            if not q:
                leftmost = cur_node.val
        
        return leftmost
