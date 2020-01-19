# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from collections import defaultdict, deque

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, K: int) -> List[int]:
        if K == 0:
            return [target.val]

        adj = defaultdict(list)
        self.preorder(root, adj)
        res = []
        
        cnt = 0
        queue = deque()
        visited = set()
        
        queue.append(target.val)
        visited.add(target.val)
        
        while queue:
            for _ in range(len(queue)):
                x = queue.popleft()
                for neighbor in adj[x]:
                    if neighbor in visited:
                        continue
                    if cnt == K - 1:
                        res.append(neighbor)
                        continue
                    else:
                        queue.append(neighbor)
                        visited.add(neighbor)
                    
            cnt += 1
        
        return res
        
    
    def preorder(self, node, adj):
        if not node:
            return
        if node.left:
            adj[node.val].append(node.left.val)
            adj[node.left.val].append(node.val)
            self.preorder(node.left, adj)
        if node.right:
            adj[node.val].append(node.right.val)
            adj[node.right.val].append(node.val)
            self.preorder(node.right, adj)
        
