from collections import deque


class LRUCache:

    def __init__(self, capacity: int):
        self.next = {}
        self.prev = {}
        self.cache = {}
        self.capacity = capacity
        self.head = "head"
        self.tail = "tail"
        self.connect(self.head, self.tail)
        
    def get(self, key: int) -> int:
        if not key in self.cache:
            return -1
        self.update(key)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            self.update(key)
        else:
            if len(self.cache) == self.capacity:
                self.pop()
            self.cache[key] = value
            self.append(key)

        
    def connect(self, a, b):
        self.next[a], self.prev[b] = b, a
        
    def pop(self):
        first = self.next[self.head]
        self.connect(self.head, self.next[first])
        self.next.pop(first), self.prev.pop(first), self.cache.pop(first)
    
    def append(self, key):
        last = self.prev[self.tail]
        self.connect(last, key)
        self.connect(key, self.tail)
        
    def update(self, key):
        self.connect(self.prev[key], self.next[key])
        self.append(key)
        

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
