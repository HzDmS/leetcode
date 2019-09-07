"""
# Definition for a Node.
class Node:
    def __init__(self, val, neighbors):
        self.val = val
        self.neighbors = neighbors
"""
from collections import deque


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        queue = deque()
        visited = {}
        queue.append(node)
        visited[node] = Node(node.val, [])
        while queue:
            cur = queue.popleft()
            for neighbor in cur.neighbors:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited[neighbor] = Node(neighbor.val, [])
                visited[cur].neighbors.append(visited[neighbor])
        return visited[node]

