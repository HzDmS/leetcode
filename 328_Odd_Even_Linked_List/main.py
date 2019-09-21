# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if not head or not head.next or not head.next.next:
            return head
        
        prev_odd, even = head, head.next
        while even and even.next:
            odd = even.next
            even.next = odd.next
            prev_odd.next, odd.next = odd, prev_odd.next
            even = even.next
            prev_odd = odd
        return head

