class Queue(object):
    """FIFO queue in python."""

    def __init__(self, maxsize):
        self.maxsize = maxsize
        self.queue = list()

    def push_back(self, x):
        """Push an element at the back of the queue.
        @Params:
            x: any type.
        @Return:
            bool,
                True if successful else False.
        """
        if not self.is_full():
            self.queue.insert(0, x)
            return True
        return False

    def pop(self):
        """Pop the front element of the queue.
        @Return:
            the front element if the queue is not empty,
            else raise a Error
        """
        if not self.is_empty():
            return self.queue.pop()
        else:
            print("Queue is empty!")
            exit()
    
    def is_full(self):
        """Check if the queue is full.
        @Return:
            True if the queue is full else False
        """
        if(len(self.queue) == self.maxsize):
            return True
        return False

    def is_empty(self):
        """Check if the queue is empty
        @Return:
            True if the queue is empty else False.
        """
        if len(self.queue) == 0:
            return True
        return False


if __name__ == '__main__':
    q = Queue(10)
    for i in range(11):
        if q.push_back(i):
            print("enqueue: {}".format(i))
        else:
            print("failed: {}".format(i))

    for i in range(11):
        if not q.is_empty():
            print("dequeue: {}".format(q.pop()))
        else:
            q.pop()
