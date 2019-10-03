# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        slow, fast = head, head
        prev = None
        cnt = 0
        while fast:
            if cnt < n:
                cnt += 1
            else:
                prev = slow
                slow = slow.next
            fast = fast.next
        if not prev:
            return head.next
        else:
            prev.next = slow.next
            return head

