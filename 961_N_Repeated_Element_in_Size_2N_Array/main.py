class Solution:
    def repeatedNTimes(self, A: List[int]) -> int:
        hashset = set()
        
        for a in A:
            if a in hashset:
                return a
            else:
                hashset.add(a)
