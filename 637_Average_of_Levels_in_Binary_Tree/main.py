# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        
        ret = []
        
        if not root:
            return ret
        
        queue = deque()
        queue.append(root)
        
        while queue:
            leaves = []
            for _ in range(len(queue)):
                node = queue.popleft()
                if node:
                    leaves.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ret.append(sum(leaves) / len(leaves))
        
        return ret
