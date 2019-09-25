# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            node = queue.popleft()
            ans.append(str(node.val) if node else "*")
            if node:
                queue.append(node.left)
                queue.append(node.right)
        return " ".join(ans)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        bfs_nodes = [TreeNode(int(val)) if not val == "*" else None for val in data.split()]
        slow, fast = 0, 1
        root = bfs_nodes[0]
        nodes = [root]
        while slow < len(nodes):
            node = nodes[slow]
            slow += 1
            node.left = bfs_nodes[fast]
            fast += 1
            node.right = bfs_nodes[fast]
            fast += 1
            
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return root
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
