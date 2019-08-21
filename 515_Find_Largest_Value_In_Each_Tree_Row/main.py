# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import deque


class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        
        ret = []
        
        if not root:
            return ret
        
        q = deque()
        q.append(root)
        
        while q:
            maximum = -float('inf')
            for _ in range(len(q)):
                node = q.popleft()
                maximum = max(maximum, node.val)
                for child in [node.left, node.right]:
                    if child:
                        q.append(child)
            ret.append(maximum)
        
        return ret
                        
        
