class LFUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_dict = {}
        self.freq_dict = {}
        self.head = None

    def get(self, key: int) -> int:
        if key in self.key_dict:
            key_node = self.key_dict[key]
            self.update(key, key_node.val)
            return key_node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if self.capacity == 0:
            return
        if key in self.key_dict:
            self.update(key, value)
        else:
            if len(self.key_dict) == self.capacity:
                self.deleteKeyNode(self.head.last)
            self.insertKeyNode(key, value)
          
    def update(self, key, val):
        key_node = self.key_dict[key]
        key_node.val = val
        freq_node = self.freq_dict[key_node.freq]
        next_freq = freq_node.next
        key_node.freq += 1
        if not next_freq or key_node.freq < next_freq.freq:
            next_freq = self.insertFreqNode(key_node.freq, freq_node, next_freq)
        self.unlink(key_node, freq_node)
        self.link(key_node, next_freq)
                
    def deleteKeyNode(self, key_node):
        self.unlink(key_node, self.freq_dict[key_node.freq])
        self.key_dict.pop(key_node.key)
        
    def insertKeyNode(self, key, val):
        key_node = self.key_dict[key] = KeyNode(key, val, 1)
        freq_node = self.freq_dict.get(1, None)
        if not freq_node:
            freq_node = self.freq_dict[1] = FreqNode(1, None, self.head)
            if self.head:
                self.head.prev = freq_node
            self.head = freq_node
        self.link(key_node, freq_node)
            
    def insertFreqNode(self, freq, freq_node, next_node):
        new_node = FreqNode(freq, freq_node, next_node)
        self.freq_dict[freq] = new_node
        freq_node.next = new_node
        if next_node:
            next_node.prev = new_node
        return new_node
            
    def delFreqNode(self, freq_node):
        prev_node, next_node = freq_node.prev, freq_node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        if freq_node == self.head:
            self.head = next_node
        self.freq_dict.pop(freq_node.freq)
        
    def unlink(self, key_node, freq_node):
        prev_node = key_node.prev
        next_node = key_node.next
        if prev_node:
            prev_node.next = next_node
        if next_node:
            next_node.prev = prev_node
        if freq_node.first == key_node:
            freq_node.first = next_node
        if freq_node.last == key_node:
            freq_node.last = prev_node
        if not freq_node.first:
            self.delFreqNode(freq_node)
            
    def link(self, key_node, freq_node):
        first_node = freq_node.first
        freq_node.first = key_node
        key_node.prev = None
        key_node.next = first_node
        if first_node:
            first_node.prev = key_node
        if not freq_node.last:
            freq_node.last = key_node

        
class KeyNode:
    
    def __init__(self, key, val, freq):
        self.key = key
        self.val = val
        self.freq = freq
        self.prev = self.next = None
        

class FreqNode:
    
    def __init__(self, freq, prev, nextt):
        self.freq = freq
        self.prev = prev
        self.next = nextt
        self.first = self.last = None
        


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
