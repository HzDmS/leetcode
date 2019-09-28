# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        return self.convert(head, None)
        
    def convert(self, head, tail):
        if head == tail:
            return None
        if head.next == tail:
            return TreeNode(head.val)
        slow, fast = head, head
        while not fast == tail and not fast.next == tail:
            slow = slow.next
            fast = fast.next.next
        node = TreeNode(slow.val)
        node.left = self.convert(head, slow)
        node.right = self.convert(slow.next, tail)
        return node

