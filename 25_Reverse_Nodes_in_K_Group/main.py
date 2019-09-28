# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        return self.reverse(head, k) 
        
    def reverse(self, node, k):
        prev, cur = None, node
        cnt = 0
        while cur and cnt < k:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
            cnt += 1
        if cnt == k:
            node.next = self.reverse(cur, k)
            return prev
        else:
            prev, cur = cur, prev
            while cur:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
            return prev

