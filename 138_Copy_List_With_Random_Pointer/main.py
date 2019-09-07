"""
# Definition for a Node.
class Node:
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        hm = {}
        prev, cur = None, head
        while cur:
            hm[cur] = Node(cur.val, None, None)
            if prev:
                hm[prev].next = hm[cur]
            prev = cur
            cur = cur.next
        for key, value in hm.items():
            if key.random:
                value.random = hm[key.random]
        return hm[head] if head else head

