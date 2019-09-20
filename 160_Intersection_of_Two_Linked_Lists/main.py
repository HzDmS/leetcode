# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        ptra, ptrb = headA, headB
        while not ptra == ptrb:
            if not ptra:
                ptra = headB
            else:
                ptra = ptra.next
            if not ptrb:
                ptrb = headA
            else:
                ptrb = ptrb.next
        return ptra

