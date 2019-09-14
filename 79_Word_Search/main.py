from collections import defaultdict


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        starts = []
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    starts.append((i, j))
        
        dirs = [[1, 0], [-1, 0], [0, -1], [0, 1]]
        visited = [[0] * n for _ in range(m)]
        trie = Trie()
        trie.insert(word)
        
        def dfs(i, j, node):
            if board[i][j] not in node.next:
                return False
            if node.next[board[i][j]].is_end:
                return True
            visited[i][j] = 1
            ans = False
            for x, y in dirs:
                new_i, new_j = i + x, j + y
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n or visited[new_i][new_j]:
                    continue
                else:
                    ans = ans or dfs(new_i, new_j, node.next[board[i][j]])
            visited[i][j] = 0
            return ans
        
        ans = False
        for i, j in starts:
            ans = ans or dfs(i, j, trie.root)
        return ans


class TrieNode:
    def __init__(self):
        self.next = defaultdict(TrieNode)
        self.is_end = False
        

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.next[c]
        node.is_end = True
        
