# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        head = list1
        m, n, p, q = None, None, list2, None
        
        cnt = 0
        while list1:
            cnt += 1
            if cnt == a:
                m = list1
            if cnt == b + 1:
                n = list1.next
            list1 = list1.next
        
        while list2:
            if list2.next is None:
                q = list2
            list2 = list2.next
        
        m.next, q.next = p, n
        
        return head

