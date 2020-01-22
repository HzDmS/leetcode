# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if fast:
            slow = slow.next
        mid = self.reverse(slow)
        while head and mid:
            if not head.val == mid.val:
                return False
            head = head.next
            mid = mid.next
        return True

    
    def reverse(self, node):
        prev = None
        cur = node
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        return prev

