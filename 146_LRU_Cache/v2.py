class ListNode:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = ListNode("head", 0)
        self.tail = ListNode("tail", 0)
        self.dict = {}
        self.connect(self.head, self.tail)

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        node = self.dict[key]
        self.update(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.update(node)
        else:
            node = ListNode(key, value)
            if len(self.dict) == self.capacity:
                self.pop()
            self.insert(node)
        self.dict[key] = node
    
    def connect(self, a, b):
        a.next, b.prev = b, a

    def insert(self, node):
        self.connect(self.tail.prev, node)
        self.connect(node, self.tail)
        
    def update(self, node):
        self.connect(node.prev, node.next)
        self.insert(node)
    
    def pop(self):
        first = self.head.next
        self.connect(self.head, first.next)
        self.dict.pop(first.key)
