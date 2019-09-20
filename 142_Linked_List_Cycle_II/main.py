# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return None
        fast = slow = head
        while True:
            fast = fast.next.next
            slow = slow.next
            if not fast or not fast.next:
                return None
            if fast == slow:
                break
        cur = head
        while not cur == fast:
            fast = fast.next
            cur = cur.next
        return cur
        
