# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        self.list = nestedList
        self.stack = [_ for _ in nestedList[::-1]]
        

    def next(self):
        """
        :rtype: int
        """
        if self.hasNext():
            return self.stack.pop().getInteger()
        return None
        

    def hasNext(self):
        """
        :rtype: bool
        """
        if not self.stack:
            return False
        while not self.stack[-1].isInteger():
            last = self.stack.pop().getList()
            self.stack.extend(last[::-1])
            if not self.stack:
                return False
        return True
            
        
        

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
