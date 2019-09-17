"""
# Definition for a Node.
class Node:
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        node = root
        cur, head = Node(), None
        while node:
            if node.left:
                cur.next = node.left
                cur = cur.next
                if not head:
                    head = node.left
            if node.right:
                cur.next = node.right
                cur = cur.next
                if not head:
                    head = node.right
            node = node.next
            if not node:
                node = head
                cur, head = Node(), None
        return root
        
