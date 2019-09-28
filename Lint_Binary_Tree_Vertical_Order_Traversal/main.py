"""
Definition of TreeNode:
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None
"""
from collections import defaultdict, deque

class Solution:
    """
    @param root: the root of tree
    @return: the vertical order traversal
    """
    def verticalOrder(self, root):
        # write your code here
        if not root:
            return []
        hashmap = defaultdict(list)
        queue = deque()
        queue.append((root, 0))
        while queue:
            node, key = queue.popleft()
            hashmap[key].append(node.val)
            if node.left:
                queue.append((node.left, key - 1))
            if node.right:
                queue.append((node.right, key + 1))
        ans = []
        for key in sorted(hashmap.keys()):
            ans.append(hashmap[key])
        return ans
