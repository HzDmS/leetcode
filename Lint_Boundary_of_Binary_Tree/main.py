"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import deque

class Solution:
    """
    @param root: a TreeNode
    @return: a list of integer
    """
    def boundaryOfBinaryTree(self, root):
        # write your code here
        if not root:
            return []
        left_boundary = self.findLeftBoundary(root.left)
        leaves = self.findLeaves(root)
        right_boundary = self.findRightBoundary(root.right)
        
        if left_boundary and leaves and left_boundary[-1] == leaves[0]:
            leaves = leaves[1:]
        if right_boundary and leaves and right_boundary[-1] == leaves[-1]:
            leaves = leaves[:-1]
        right_boundary.reverse()
        return [root.val] + left_boundary + leaves + right_boundary
    
    def findLeftBoundary(self, root):
        left_boundary = []
        while root:
            left_boundary.append(root.val)
            if root.left:
                root = root.left
            elif root.right:
                root = root.right
            else:
                break
        return left_boundary
    
    def findRightBoundary(self, root):
        right_boundary = []
        while root:
            right_boundary.append(root.val)
            if root.right:
                root = root.right
            elif root.left:
                root = root.left
            else:
                break
        return right_boundary
        
    def findLeaves(self, root):
        leaves = []
        stack, cur = [], root
        while stack or cur:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            if cur.right:
                cur = cur.right
            else:
                if not cur.left:
                    leaves.append(cur.val)
                cur = None
        # stack = [root]
        # while stack:
        #     node = stack.pop()
        #     if not node.left and not node.right:
        #         leaves.append(node.val)
        #     if node.right:
        #         stack.append(node.right)
        #     if node.left:
        #         stack.append(node.left)
        return leaves
            

