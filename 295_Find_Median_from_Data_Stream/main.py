import heapq


class MedianFinder:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.max_heap = []
        self.min_heap = []
        

    def addNum(self, num: int) -> None:
        if len(self.max_heap) <= len(self.min_heap):
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        if not self.max_heap or not self.min_heap:
            return

        if -self.max_heap[0] > self.min_heap[0]:
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))
            

    def findMedian(self) -> float:
        if (len(self.min_heap) + len(self.max_heap)) & 1 == 0:
            return (self.min_heap[0] - self.max_heap[0]) * 0.5
        return -self.max_heap[0]
        


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
