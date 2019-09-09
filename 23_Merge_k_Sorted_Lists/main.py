# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

import heapq


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        
        # time: O(nlogk)
        # space: O(k)
        
        n = len(lists)
        
        head = ListNode(0)
        heap = [(lists[i].val, i) for i in range(n) if lists[i]]
        for i in range(n):
            lists[i] = lists[i].next if lists[i] else None
        heapq.heapify(heap)
        
        cur = head
        while heap:
            val, i = heapq.heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, i))
                lists[i] = lists[i].next
        
        return head.next
            
