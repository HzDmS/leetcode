from collections import defaultdict


class Solution:
    
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans = []
        m, n = len(board), len(board[0])
        dirs = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        words = set(words)
        
        def dfs(i, j, cur):
            if not trie.search(cur):
                return
            if cur in words:
                ans.append(cur)
                words.remove(cur)
            for x, y in dirs:
                new_i, new_j = i + x, j + y
                if new_i < 0 or new_i >= m or new_j < 0 or new_j >= n:
                    continue
                elif visited[new_i][new_j]:
                    continue
                else:
                    visited[new_i][new_j] = 1
                    dfs(new_i, new_j, cur + board[new_i][new_j])
                    visited[new_i][new_j] = 0  

        for i in range(m):
            for j in range(n):
                if trie.search(board[i][j]):
                    visited = [[0] * n for _ in range(m)]
                    visited[i][j] = 1
                    dfs(i, j, board[i][j])
        
        return ans

    
class TrieNode:

    def __init__(self):
        self.children = defaultdict(TrieNode)

class Trie:
    
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for c in word:
            node = node.children[c]
    
    def search(self, word):
        node = self.root
        for c in word:
            if c in node.children:
                node = node.children[c]
            else:
                return False
        return True
