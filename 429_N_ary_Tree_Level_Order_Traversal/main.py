"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
from collections import deque


class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        
        ret = []
        if not root:
            return ret
        
        q = deque()
        q.append(root)

        while q:
            
            cur = []
            
            for _ in range(len(q)):
                
                node = q.popleft()
                cur.append(node.val)
                
                for child in node.children:
                    if child:
                        q.append(child)
            ret.append(cur)

        return ret
            
