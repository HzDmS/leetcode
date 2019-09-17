# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next
        carry = 0
        head = ListNode(0)
        while s1 and s2:
            s = s1.pop() + s2.pop() + carry
            carry = s // 10
            tmp = head.next
            head.next = ListNode(s % 10)
            head.next.next = tmp
        r = s1 if s1 else s2
        while r:
            s = r.pop() + carry
            carry = s // 10
            tmp = head.next
            head.next = ListNode(s % 10)
            head.next.next = tmp
        if carry:
            tmp = head.next
            head.next = ListNode(carry)
            head.next.next = tmp
        return head.next
                
        
        
#         def reverse(head):
#             prev = None
#             while head:
#                 tmp = head.next
#                 head.next = prev
#                 prev = head
#                 head = tmp
#             return prev
        
#         l1, l2 = reverse(l1), reverse(l2)
        
#         n1, n2 = l1, l2
#         head = ListNode(0)
#         cur = head
#         carry = 0
#         while n1 and n2:
#             tmp = (n1.val + n2.val + carry) 
#             cur.next = ListNode(tmp % 10)
#             carry = tmp // 10
#             n1 = n1.next
#             n2 = n2.next
#             cur = cur.next
#         while n1:
#             tmp = (n1.val + carry) 
#             cur.next = ListNode(tmp % 10)
#             carry = tmp // 10
#             n1 = n1.next
#             cur = cur.next
#         while n2:
#             tmp = (n2.val + carry) 
#             cur.next = ListNode(tmp % 10)
#             carry = tmp // 10
#             n2 = n2.next
#             cur = cur.next
#         if carry:
#             cur.next = ListNode(carry)
#         return reverse(head.next)
                
