# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        
        def merge(first, second):
            head = ListNode(0)
            cur = head
            while first and second:
                if first.val < second.val:
                    cur.next = first
                    first = first.next
                else:
                    cur.next = second
                    second = second.next
                cur = cur.next
            while first:
                cur.next = first
                cur = cur.next
                first = first.next
            while second:
                cur.next = second
                cur = cur.next
                second = second.next
            return head.next
        
        def mergeSort(head):
            
            if not head or not head.next:
                return head
            
            slow = fast = head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            fast = slow.next
            slow.next = None
            first = mergeSort(head)
            second = mergeSort(fast)
            return merge(first, second)
        
        return mergeSort(head)
            
                    
            
