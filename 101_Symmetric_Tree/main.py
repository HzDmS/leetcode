# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Solution:
    
    def isSymmetric(self, root: TreeNode) -> bool:
        
        def check(lnode, rnode):
            if not lnode and not rnode:
                return True
            elif lnode and rnode:
                if not lnode.val == rnode.val:
                    return False
                else:
                    return check(lnode.left, rnode.right) and check(lnode.right, rnode.left)
            else:
                return False
        
        if not root:
            return True
        else:
            return check(root.left, root.right)
        
#     def isSymmetric(self, root: TreeNode) -> bool:
        
#         lq, rq = deque(), deque()
#         if not root:
#             return True
#         lq.append(root.left)
#         rq.append(root.right)
        
#         while lq and rq:
#             lnode = lq.popleft()
#             rnode = rq.popleft()
#             if not lnode and not rnode:
#                 continue
#             elif lnode and rnode:
#                 if not lnode.val == rnode.val:
#                     return False
#                 else:
#                     lq.append(lnode.left)
#                     lq.append(lnode.right)
#                     rq.append(rnode.right)
#                     rq.append(rnode.left)
#             else:
#                 return False
#         if lq or rq:
#             return False
#         return True

