"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        self.helper(root)
        return root
    
    def helper(self, cur):
        
        if not cur:
            return
        
        head = None
        while cur:
            if cur.left and cur.right:
                if not head:
                    head = cur.left
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
            cur = cur.next
        self.helper(head)

